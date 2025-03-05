
# MATLAB Code Documentation

## Analyzer/changeTensorIndex.m

This function changes the index of a given tensor (e.g., from covariant to contravariant). It takes the following inputs:

* `inputTensor`: The tensor to change the index of (struct).
* `index`: The desired index ('covariant', 'contravariant', 'mixedupdown', 'mixeddownup').
* `metricTensor`: The metric tensor (struct, optional). Required for non-metric tensors.

It returns the `outputTensor` with the changed index.  The function handles errors such as invalid input types and unsupported index transformations.


## Analyzer/doFrameTransfer.m

This function transforms the energy tensor into a selected frame (currently only 'Eulerian' is supported). It takes the following inputs:

* `metric`: The metric tensor (struct).
* `energyTensor`: The energy tensor (struct).
* `frame`: The target frame ('Eulerian').
* `tryGPU`: Flag to use GPU computation (0 or 1, optional, default is 0).

It returns the `transformedEnergyTensor` in the specified frame. The function performs several steps, including index changes, tensor format conversions, and applying the Eulerian transformation matrix.

---

## Analyzer/evalMetric.m

This function evaluates the metric and returns core analysis products. It takes the following inputs:

* `metric`: Metric tensor struct.
* `tryGPU`: Flag for GPU usage (0 or 1, optional).
* `keepPositive`: Flag to keep only positive energy condition values (0 or 1, optional).
* `numAngularVec`: Number of spatial vectors (optional).
* `numTimeVec`: Number of temporal shells (optional).

It returns a struct containing the metric, energy tensors, energy conditions (null, weak, strong, dominant), and scalars (expansion, shear, vorticity).

---

## Analyzer/getEnergyConditions.m

This function calculates energy conditions for a given energy tensor. It takes the following inputs:

* `energyTensor`: The energy tensor (struct).
* `metric`: The metric tensor (struct).
* `condition`: The energy condition to evaluate ('Null', 'Weak', 'Strong', 'Dominant').
* `numAngularVec`: Number of spatial vectors (optional).
* `numTimeVec`: Number of temporal shells (optional).
* `returnVec`: Flag to return all evaluations and vectors (0 or 1, optional).
* `tryGPU`: Flag for GPU usage (0 or 1, optional).

It returns the most violating evaluation (`map`), and optionally all evaluations (`vec`) and the vector field used (`vectorFieldOut`).

---

## Analyzer/getMomentumFlowLines.m

This function computes momentum flow lines for a given energy tensor. It takes the following inputs:

* `energyTensor`: Energy tensor (struct, contravariant index).
* `startPoints`: Cell array of starting points {X, Y, Z}.
* `stepSize`: Step size for propagation.
* `maxSteps`: Maximum number of steps.
* `scaleFactor`: Scaling factor for momentum density.

It returns `paths`, a cell array of momentum flow lines.

---

## Analyzer/getScalars.m

This function calculates scalar quantities (expansion, shear, vorticity) from a given metric. It takes the following input:

* `metric`: The metric tensor (struct).

It returns the following outputs:

* `expansionScalar`: Expansion scalar.
* `shearScalar`: Shear scalar.
* `vorticityScalar`: Vorticity scalar.

---

## Examples/1 Metrics

This directory contains examples demonstrating how to work with metrics. The files are MATLAB Live Scripts (.mlx) and cannot be directly displayed here.

* M1_First_Metric.mlx
* M2_Default_Metrics.mlx
* M3_Building_a_Metric.mlx

---

## Examples/2 Energy Tensor

This directory contains examples related to energy tensors. The files are MATLAB Live Scripts (.mlx).

* T1_First_Energy_Tensor.mlx
* T2_Cartoon_Methods.mlx
* T3_GPU_Computation.mlx
* T4_Second_vs_Fourth_Order.mlx
* T5_Errors.mlx

---

## Examples/3 Analysis

This directory contains analysis examples. The files are MATLAB Live Scripts (.mlx).

* A1_Energy_Conditions.mlx
* A2_Metric_Scalars.mlx
* A3_Eval_Metric.mlx
* A4_Momentum_Flow.mlx

---

## Examples/4 Warp Shell

This directory contains a warp shell example. The file is a MATLAB Live Script (.mlx).

* W1_Warp_Shell.mlx

---

## Metrics

This directory contains various metric implementations and related functions.

### Files:

* `setMinkowski.m`
* `setMinkowskiThreePlusOne.m`
* `threePlusOneBuilder.m`
* `threePlusOneDecomposer.m`

### Subdirectories:

* Alcubierre
* Lentz
* Minkowski
* ModifiedTime
* Schwarzschild
* VanDenBroeck
* WarpShell

---

### Metrics/Alcubierre

This subdirectory contains implementations of the Alcubierre metric.

* `metricGet_Alcubierre.m`
* `metricGet_AlcubierreComoving.m`

---

### Metrics/Lentz

This subdirectory contains implementations of the Lentz metric.

* `metricGet_Lentz.m`
* `metricGet_LentzComoving.m`

---

### Metrics/Minkowski

This subdirectory contains an implementation of the Minkowski metric.

* `metricGet_Minkowski.m`

---

### Metrics/ModifiedTime

This subdirectory contains implementations of the ModifiedTime metric.

* `metricGet_ModifiedTime.m`
* `metricGet_ModifiedTimeComoving.m`

---

### Metrics/Schwarzschild

This subdirectory contains an implementation of the Schwarzschild metric.

* `metricGet_Schwarzschild.m`

---

### Metrics/VanDenBroeck

This subdirectory contains implementations of the VanDenBroeck metric.

* `metricGet_VanDenBroeck.m`
* `metricGet_VanDenBroeckComoving.m`

---

### Metrics/WarpShell

This subdirectory contains an implementation of the WarpShell metric.

* `metricGet_WarpShellComoving.m`

---

## Solver

This directory contains solver implementations and related functions.

* `getEnergyTensor.m`
* `verifyTensor.m`

---

## Units

This directory contains unit conversion functions and universal constants.

### Files:

* `cm.m`
* `gram.m`
* `kg.m`
* `km.m`
* `meter.m`
* `mm.m`
* `ms.m`
* `second.m`
* `tonne.m`

### Subdirectories:

* 'Universal Constants'

---

### Units/Universal Constants

This subdirectory contains universal constants.

* `G.m`
* `c.m`

---

## Visualizer

This directory contains visualization functions.

* `plotTensor.m`
* `plotThreePlusOne.m`

---
---