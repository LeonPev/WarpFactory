
from .get_energy_conditions import verify_tensor, _disp_message
from .c4Inv import c4_inv
from .utils.getEulerianTransformationMatrix import get_eulerian_transformation_matrix
from .utils.tensorCell2Array import tensor_cell_2_array
import numpy as np

def change_tensor_index(input_tensor, index, metric_tensor=None):
    if metric_tensor is None:
        if input_tensor["type"].lower() != "metric":
            raise ValueError("metric_tensor is needed as third input when changing index of non-metric tensors.")

    if index.lower() not in ["mixedupdown", "mixeddownup", "covariant", "contravariant"]:
        raise ValueError("Transformation selected is not allowed, use either: \"covariant\", \"contravariant\", \"mixedupdown\", \"mixeddownup\"")

    output_tensor = input_tensor.copy()

    if input_tensor["type"].lower() == "metric":
        if (input_tensor["index"].lower() == "covariant" and index.lower() == "contravariant") or (input_tensor["index"].lower() == "contravariant" and index.lower() == "covariant"):
            output_tensor["tensor"] = c4_inv(input_tensor["tensor"])
        elif input_tensor["index"].lower() in ["mixedupdown", "mixeddownup"]:
            raise ValueError("Input tensor is a Metric tensor of mixed index.")
        elif index.lower() in ["mixedupdown", "mixeddownup"]:
            raise ValueError("Cannot convert a metric tensor to mixed index.")
    else:
        if metric_tensor["index"].lower() in ["mixedupdown", "mixeddownup"]:
            raise ValueError("Metric tensor cannot be used in mixed index.")

        if input_tensor["index"].lower() == "covariant" and index.lower() == "contravariant":
            if metric_tensor["index"].lower() == "covariant":
                metric_tensor["tensor"] = c4_inv(metric_tensor["tensor"])
                metric_tensor["index"] = "contravariant"
            output_tensor["tensor"] = _flip_index(input_tensor, metric_tensor)["tensor"]
        elif input_tensor["index"].lower() == "contravariant" and index.lower() == "covariant":
            if metric_tensor["index"].lower() == "contravariant":
                metric_tensor["tensor"] = c4_inv(metric_tensor["tensor"])
                metric_tensor["index"] = "covariant"
            output_tensor["tensor"] = _flip_index(input_tensor, metric_tensor)["tensor"]
        # ... other cases

    output_tensor["index"] = index
    return output_tensor

def _flip_index(tensor, metric):
    new_tensor = np.zeros_like(tensor["tensor"])
    for mu in range(4):
        for nu in range(4):
            for alpha in range(4):
                for beta in range(4):
                    new_tensor[mu, nu] += tensor["tensor"][alpha, beta] * metric["tensor"][alpha, mu] * metric["tensor"][beta, nu]
    return {"tensor": new_tensor, "coords": tensor["coords"], "index": metric["index"], "type": tensor["type"]}

def _mix_index1(tensor, metric):
    new_tensor = np.zeros_like(tensor["tensor"])
    for mu in range(4):
        for nu in range(4):
            for alpha in range(4):
                new_tensor[mu, nu] += tensor["tensor"][alpha, nu] * metric["tensor"][alpha, mu]
    return {"tensor": new_tensor, "coords": tensor["coords"], "index": "mixedupdown", "type": tensor["type"]}

def _mix_index2(tensor, metric):
    new_tensor = np.zeros_like(tensor["tensor"])
    for mu in range(4):
        for nu in range(4):
            for alpha in range(4):
                new_tensor[mu, nu] += tensor["tensor"][mu, alpha] * metric["tensor"][alpha, nu]
    return {"tensor": new_tensor, "coords": tensor["coords"], "index": "mixeddownup", "type": tensor["type"]}

def do_frame_transfer(metric, energy_tensor, frame, try_gpu=0):
    transformed_energy_tensor = energy_tensor.copy()
    if not verify_tensor(metric, 1):
        raise ValueError("Metric is not verified. Please verify metric using verify_tensor(metric).")
    if not verify_tensor(energy_tensor, 1):
        raise ValueError("Stress-energy is not verified. Please verify Stress-energy tensor using verify_tensor(energy_tensor).")

    if frame.lower() == "eulerian" and (("frame" not in energy_tensor) or (energy_tensor["frame"].lower() != "eulerian")):
        energy_tensor = change_tensor_index(energy_tensor, "covariant", metric)
        array_energy_tensor = tensor_cell_2_array(energy_tensor, try_gpu)
        array_metric_tensor = tensor_cell_2_array(metric, try_gpu)
        m = get_eulerian_transformation_matrix(array_metric_tensor, metric["coords"])

        # Transformed tensor calculation
        transformed_tensor = np.einsum('ij...,jk...,kl...->il...', m, array_energy_tensor, m)

        # Convert array tensor into cell format
        z = transformed_tensor.shape
        transformed_energy_tensor["tensor"] = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                transformed_energy_tensor["tensor"][i][j] = transformed_tensor[i, j, ...]

        # Transform to contravariant
        for i in range(1, 4):
            transformed_energy_tensor["tensor"][0][i] *= -1
            transformed_energy_tensor["tensor"][i][0] *= -1

        transformed_energy_tensor["frame"] = "Eulerian"
        transformed_energy_tensor["index"] = "contravariant"

    elif frame.lower() != "eulerian":
        print("Frame not found")

    return transformed_energy_tensor