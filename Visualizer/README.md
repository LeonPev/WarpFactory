
# Visualizer Module Documentation


## plotTensor.m

Inputs:
* `tensor`: Tensor struct (metric or stress-energy).
* `alpha`: Alpha value for surface grid (0-1, default 0.2).
* `slicedPlanes`: Coordinates to slice (e.g., [1, 4] for X-Y plane, default [1, 4]).
* `sliceLocations`: Slice locations (default is the center).

Outputs:
* (None)

Functionality:
This function plots the unique elements of a tensor based on the specified slice plane and location. It handles both metric and stress-energy tensors. The `alpha` parameter controls the transparency of the surface grid. The `slicedPlanes` parameter defines the slicing plane, and `sliceLocations` specifies the location of the slices. If `sliceLocations` is not provided, the function defaults to the center of the tensor.

## plotThreePlusOne.m

Inputs:
* `metric`: Metric tensor struct.
* `slicedPlanes`: Coordinates to slice (e.g., [1, 4] for X-Y plane, default [1, 4]).
* `sliceLocations`: Slice locations (default is center).
* `alpha`: Alpha value for surface grid (0-1, default 0.2).

Outputs:
* (None)

Functionality:
This function plots the 3+1 components (lapse, shift, and 3-metric) of a given metric tensor. The `slicedPlanes` parameter defines the slicing plane, and `sliceLocations` specifies the location of the slices. The `alpha` parameter controls the transparency of the surface grid. If `sliceLocations` is not provided, the function defaults to the center of the metric.


