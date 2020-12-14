## Model 1： Uniform Kinematic Wave

### Model Parameter file (han_river_K.par)

### Digital Elevation file (DEM.asc)

This DEM file is used for all the models.

### Channel Information (han_river_K.river)

All our models simplify the Han river as a single channel with no tributary, and the channel is represented as a combination of multiple directed vector, which are connected by 40 points (including 9 hydropower stations)，which are projected onto the DEM raster grid. Characteristics of the channel include **width**, **Manning’s n friction coefficient** and **bed elevation**. The Manning’s n friction coefficient is determined according to a reference table provided by FishXing software (http://www.fsl.orst.edu/geowater/FX3/help/8_Hydraulic_Reference/Mannings_n_Tables.htm).

Model 1 assumes the channel is uniform. We only provide the three river characteristics' parameters - width, manning's n friction coefficient, and bed elevation for the starting (upstream) and end (downstream) points of the channel vector, and the code fills in intermediate points by linear interpolation. For boundary conditions, we input the recorded inflow Q on June 1st for the starting point.


### Boundary Conditions (han_river_K.river)