
# Solver Module Documentation


## getEnergyTensor.m

Inputs:
* `metric`: Metric struct (verified and covariant).
* `tryGPU`: Flag for GPU computation (0 or 1, default 0).
* `diffOrder`: Finite difference order ('second' or 'fourth', default 'fourth').

Outputs:
* `energy`: Energy tensor struct.

Functionality:
This function calculates the energy tensor from a given metric. It supports GPU computation and different finite difference orders. The input metric should be verified using `verifyTensor` and be in covariant form. The function returns an energy tensor struct containing the calculated tensor, coordinates, index type, and other metadata.

## verifyTensor.m

Inputs:
* `inputTensor`: The tensor struct to be verified.
* `suppressMsgs`: Flag to suppress messages (0 or 1, default is 0).

Outputs:
* `verified`: 1 if the tensor is verified, 0 otherwise.

Functionality:
This function verifies if the input tensor struct is correctly formatted. It checks for the existence and validity of fields like 'type' (must be "Metric" or "Stress-Energy"), 'tensor' (must be a 4x4 cell array of 4D values), 'coords' (currently only 'cartesian' is supported), and 'index' (must be "contravariant", "covariant", "mixedupdown", or "mixeddownup"). It returns 1 if the tensor is verified, and 0 otherwise. It also provides informative messages about the verification process, which can be suppressed using the `suppressMsgs` flag.


