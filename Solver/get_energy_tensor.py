
def verify_tensor(metric, condition):
    pass  # TODO: Implement

def change_tensor_index(metric, index):
    pass  # TODO: Implement

def met2den(metric_tensor, scaling):
    pass  # TODO: Implement

def met2den2(metric_tensor, scaling):
    pass  # TODO: Implement

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
        "date": "#TODO: Get current date",
    }

    return energy