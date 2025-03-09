
def verify_tensor(input_tensor, suppress_msgs=False):
    """Verifies the metric tensor and stress energy tensor structs."""

    verified = True

    def disp_message(msg, suppress_msgs):
        if not suppress_msgs:
            print(msg)

    if 'type' in input_tensor:
        if input_tensor['type'].lower() == "metric":
            disp_message("type: Metric", suppress_msgs)
        elif input_tensor['type'].lower() == "stress-energy":
            disp_message("Type: Stress-Energy", suppress_msgs)
        else:
            print('Tensor type field does not exist. Must be either "Metric" or "Stress-Energy"')
            verified = False
    else:
        print('Tensor type does not exist. Must be either "Metric" or "Stress-Energy"')

    if 'tensor' in input_tensor:
        if isinstance(input_tensor['tensor'], list) and len(input_tensor['tensor']) == 4 and len(input_tensor['tensor'][0]) == 4 and len(input_tensor['tensor'][0][0]) == 4:
            disp_message("tensor: Verified", suppress_msgs)
        else:
            print("Tensor is not formatted correctly. Tensor must be a 4x4 list of lists of 4D values.")
            verified = False
    else:
        print("tensor: Empty")
        verified = False

    if 'coords' in input_tensor:
        if input_tensor['coords'].lower() == "cartesian":
            disp_message("coords: " + input_tensor['coords'], suppress_msgs)
        else:
            print("Non-cartesian coordinates are not supported at this time. Set .coords to 'cartesian'.")
    else:
        print("coords: Empty")
        verified = False

    if 'index' in input_tensor:
        if input_tensor['index'].lower() in ["contravariant", "covariant", "mixedupdown", "mixeddownup"]:
            disp_message("index: " + str(input_tensor['index']), suppress_msgs)
        else:
            print("Unknown index")
            verified = False
    else:
        print("index: Empty")
        verified = False

    return verified
