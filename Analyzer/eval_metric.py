
def get_energy_tensor(metric, try_gpu):
    pass  # TODO: Implement

def do_frame_transfer(metric, energy_tensor, frame, try_gpu):
    pass  # TODO: Implement

def get_energy_conditions(energy_tensor, metric, condition, num_angular_vec, num_time_vec, return_vec, try_gpu):
    pass  # TODO: Implement
    return 0, 0, 0

def get_scalars(metric):
    pass  # TODO: Implement
    return 0, 0, 0

def eval_metric(metric, try_gpu=0, keep_positive=1, num_angular_vec=100, num_time_vec=10):
    output = {}
    output["metric"] = metric

    output["energyTensor"] = get_energy_tensor(metric, try_gpu)
    output["energyTensorEulerian"] = do_frame_transfer(metric, output["energyTensor"], "Eulerian", try_gpu)

    output["null"], _, _ = get_energy_conditions(output["energyTensor"], metric, "Null", num_angular_vec, num_time_vec, 0, try_gpu)
    output["weak"], _, _ = get_energy_conditions(output["energyTensor"], metric, "Weak", num_angular_vec, num_time_vec, 0, try_gpu)
    output["strong"], _, _ = get_energy_conditions(output["energyTensor"], metric, "Strong", num_angular_vec, num_time_vec, 0, try_gpu)
    output["dominant"], _, _ = get_energy_conditions(output["energyTensor"], metric, "Dominant", num_angular_vec, num_time_vec, 0, try_gpu)

    if not keep_positive:
        output["null"][output["null"] > 0] = 0
        output["weak"][output["weak"] > 0] = 0
        output["strong"][output["strong"] > 0] = 0
        output["dominant"][output["dominant"] > 0] = 0

    output["expansion"], output["shear"], output["vorticity"] = get_scalars(metric)

    return output