
# Analyzer Module Documentation

This module contains functions for analyzing the results of the warp drive simulations.

## changeTensorIndex.m

This function handles the following index types: 'covariant', 'contravariant', 'mixedupdown', 'mixeddownup'.
It uses the metric tensor for transformations between covariant and contravariant indices.
It throws an error if the metric tensor is provided in a mixed index form.
It also throws an error if an invalid transformation is requested.

## doFrameTransfer.m

This function performs a frame transfer.
Inputs:
* `metric`: Metric struct (verified using `verifyTensor`).
* `energyTensor`: Energy struct (verified using `verifyTensor`).
* `frame`: Frame to transform to (currently only 'Eulerian' is supported).
* `tryGPU`: Flag for GPU computation (0=no, 1=yes, default is 0).

Outputs:
* `transformedEnergyTensor`: Transformed energy struct.

Functionality:
This function transforms the energy tensor into the specified frame (Eulerian). It converts the energy tensor to covariant index, performs the transformation using a matrix obtained from `getEulerianTransformationMatrix`, and then converts the result back to contravariant index. It updates the tensor metadata with the new frame and index information.
It takes the tensor, the velocity field, and the metric tensor as input. It returns the tensor in the new frame.

## evalMetric.m

Inputs:
* `metric`: Metric tensor struct.
* `tryGPU`: Flag for GPU computation (0=no, 1=yes, default is 0).
* `keepPositive`: Flag to keep only positive values of energy conditions (0=no, 1=yes, default is 1).
* `numAngularVec`: Number of spatial vectors to evaluate (default is 100).
* `numTimeVec`: Number of temporal shells to evaluate (default is 10).

Outputs:
* `output`: Struct containing analysis results (metric, energy tensors, energy conditions, scalars).

Functionality:
This function evaluates the provided metric tensor and returns a struct containing the analysis results. It calculates the energy tensor, transforms it to the Eulerian frame, evaluates the null, weak, strong, and dominant energy conditions, and calculates scalar quantities like expansion, shear, and vorticity.


## getEnergyConditions.m

Inputs:
* `energyTensor`: Energy struct (verified using `verifyTensor`).
* `metric`: Metric struct (verified using `verifyTensor`).
* `condition`: Energy condition to evaluate ("Null", "Weak", "Strong", or "Dominant").
* `numAngularVec`: Number of spatial vectors to evaluate (default is 100).
* `numTimeVec`: Number of temporal shells to evaluate (default is 10).
* `returnVec`: Flag to return all evaluations and vectors (0=no, 1=yes, default is 0).
* `tryGPU`: Flag for GPU computation (0=no, 1=yes, default is 0).

Outputs:
* `map`: Most violating evaluation at every point in spacetime.
* `vec`: Evaluations for every vector at every point (returned if `returnVec` is 1).
* `vectorFieldOut`: Vector field used for evaluation (returned if `returnVec` is 1).

Functionality:
This function calculates the specified energy condition for the given energy tensor and metric. It generates a uniform vector field and evaluates the energy condition for each vector at each point in spacetime. It returns the most violating evaluation at each point and optionally returns all evaluations and the vector field used.


## getMomentumFlowLines.m

Inputs:
* `energyTensor`: Energy struct (should be contravariant).
* `startPoints`: 1x3 cell array of starting points for flowlines {X, Y, Z}.
* `stepSize`: Step size for flowline propagation.
* `maxSteps`: Maximum number of propagation steps.
* `scaleFactor`: Scaling factor for momentum density.

Outputs:
* `paths`: 1xN cell array of N paths, each an Mx3 array of points.

Functionality:
This function calculates momentum flow lines from a given energy tensor. It takes starting points, step size, maximum steps, and a scaling factor as input. It uses the momentum components from the energy tensor to propagate the flow lines and returns a cell array of paths.


## getScalars.m

Inputs:
* `metric`: Metric tensor struct.

Outputs:
* `expansionScalar`: Expansion scalar.
* `shearScalar`: Shear scalar.
* `vorticityScalar`: Vorticity scalar.

Functionality:
This function calculates scalar quantities (expansion, shear, and vorticity) from the given metric tensor. It performs a 3+1 decomposition of the metric, calculates the four-velocity, and uses these to compute the scalar quantities.


