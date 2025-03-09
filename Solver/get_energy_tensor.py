from datetime import date

def verify_tensor(input_tensor, suppress_msgs=False):
    verified = True

    if "type" in input_tensor:
        tensor_type = input_tensor["type"]
        if tensor_type.lower() == "metric":
            _disp_message("type: Metric", suppress_msgs)
        elif tensor_type.lower() == "stress-energy":
            _disp_message("Type: Stress-Energy", suppress_msgs)
        elif "type" not in input_tensor:
            print("Tensor type field does not exist. Must be either 'Metric' or 'Stress-Energy'")
            verified = False
        else:
            print("Unknown type")
            verified = False

        if "tensor" in input_tensor:
            tensor = input_tensor["tensor"]
            if isinstance(tensor, (list, tuple)) and len(tensor) == 4 and len(tensor[0]) == 4 and len(tensor[0][0].shape) == 4:
                _disp_message("tensor: Verified", suppress_msgs)
            else:
                print("Tensor is not formatted correctly. Tensor must be a 4x4 cell array of 4D values.")
                verified = False
        else:
            print("tensor: Empty")
            verified = False

        if "coords" in input_tensor:
            coords = input_tensor["coords"]
            if coords.lower() == "cartesian":
                _disp_message(f"coords: {coords}", suppress_msgs)
            else:
                print("Non-cartesian coordinates are not supported at this time. Set .coords to 'cartesian'.")
        else:
            print("coords: Empty")
            verified = False

        if "index" in input_tensor:
            index = input_tensor["index"]
            if index.lower() in ["contravariant", "covariant", "mixedupdown", "mixeddownup"]:
                _disp_message(f"index: {index}", suppress_msgs)
            else:
                print("Unknown index")
                verified = False
        else:
            print("index: Empty")
            verified = False
    else:
        print("Tensor type does not exist. Must be either 'Metric' or 'Stress-Energy'")
        verified = False

    

def _disp_message(msg, suppress_msgs):
    if not suppress_msgs:
        print(msg)



from .c4Inv import c4_inv
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
        elif input_tensor["index"].lower() == "contravariant" and index.lower() == "mixedupdown":
            if metric_tensor["index"].lower() == "contravariant":
                metric_tensor["tensor"] = c4_inv(metric_tensor["tensor"])
                metric_tensor["index"] = "covariant"
            output_tensor["tensor"] = _mix_index2(input_tensor, metric_tensor)["tensor"]
        elif input_tensor["index"].lower() == "contravariant" and index.lower() == "mixeddownup":
            if metric_tensor["index"].lower() == "contravariant":
                metric_tensor["tensor"] = c4_inv(metric_tensor["tensor"])
                metric_tensor["index"] = "covariant"
            output_tensor["tensor"] = _mix_index1(input_tensor, metric_tensor)["tensor"]
        elif input_tensor["index"].lower() == "covariant" and index.lower() == "mixedupdown":
            if metric_tensor["index"].lower() == "covariant":
                metric_tensor["tensor"] = c4_inv(metric_tensor["tensor"])
                metric_tensor["index"] = "contravariant"
            output_tensor["tensor"] = _mix_index1(input_tensor, metric_tensor)["tensor"]
        elif input_tensor["index"].lower() == "covariant" and index.lower() == "mixeddownup":
            if metric_tensor["index"].lower() == "covariant":
                metric_tensor["tensor"] = c4_inv(metric_tensor["tensor"])
                metric_tensor["index"] = "contravariant"
            output_tensor["tensor"] = _mix_index2(input_tensor, metric_tensor)["tensor"]
        elif input_tensor["index"].lower() == "mixedupdown" and index.lower() == "contravariant":
            if metric_tensor["index"].lower() == "covariant":
                metric_tensor["tensor"] = c4_inv(metric_tensor["tensor"])
                metric_tensor["index"] = "contravariant"
            output_tensor["tensor"] = _mix_index2(input_tensor, metric_tensor)["tensor"]
        # ... (Other cases)

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


from .c4Inv import c4_inv
from .ricciT import ricci_tensor
from .ricciS import ricci_scalar
from .einT import einstein_tensor
from .einE import energy_density

def met2den(metric_tensor, scaling):
    gu = c4_inv(metric_tensor)
    r_munu = ricci_tensor(gu, metric_tensor, scaling)
    r = ricci_scalar(r_munu, gu)
    e = einstein_tensor(r_munu, r, metric_tensor)
    energy_density_tensor = energy_density(e, gu)
    return energy_density_tensor

from .c4Inv2 import c4_inv_2
from .ricciT2 import ricci_tensor_2
from .ricciS2 import ricci_scalar_2
from .einT2 import einstein_tensor_2
from .einE2 import energy_density_2

def met2den2(metric_tensor, scaling, units=np.array([1, 1, 1])):
    gu = c4_inv_2(metric_tensor)
    r_munu = ricci_tensor_2(gu, metric_tensor, scaling)
    r = ricci_scalar_2(r_munu, gu)
    e = einstein_tensor_2(r_munu, r, metric_tensor)
    energy_density_tensor = energy_density_2(e, gu, units)
    return energy_density_tensor

def get_energy_tensor(metric, try_gpu=0, diff_order="fourth"):
    if not verify_tensor(metric, 1):
        raise ValueError("Metric is not verified. Please verify metric using verify_tensor(metric).")

    if metric["index"] != "covariant":
        metric = change_tensor_index(metric, "covariant")
        print(f"Changed metric from {metric['index']} index to covariant index")

    if try_gpu:
        # TODO: Implement GPU computation
        pass
    else:
        if diff_order == "fourth":
            energy_tensor = met2den(metric["tensor"], metric["scaling"])
        elif diff_order == "second":
            energy_tensor = met2den2(metric["tensor"], metric["scaling"])
        else:
            raise ValueError("Order Flag Not Specified Correctly. Options: 'fourth' or 'second'")

    energy = {
        "type": "Stress-Energy",
        "tensor": energy_tensor,
        "coords": metric["coords"],
        "index": "contravariant",
        "order": diff_order,
        "name": metric["name"],
        "date": date.today().strftime("%Y-%m-%d")
    }

    return energy

    return energy