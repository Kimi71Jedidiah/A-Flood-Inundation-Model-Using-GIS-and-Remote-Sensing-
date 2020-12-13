## Model 1

### Model Parameter file (.par)

### Digital Elevation file (DEM.asc)

### Channel Information

All our models simplify the Han river as a single channel with no tributary, and the channel is represented as a combination of multiple directed vector, which are connected by 20 points (including 11 hydropower stations and 9 cities along the Han river)，which are projected onto the DEM raster grid. In this model, we describe the channel in terms of its **width**, **Manning’s n friction coefficient** and **bed elevation**.

Model 1 assumes the channel is uniform - characteristics of the first and last point repre

Characteristics provided for the first and last points of the channel vector, and the code automatically fills in intermediate points by linear interpolation. By specifying the channel bed elevation at the first and last points on the channel vector the user is able to specify the (uniform) bed slope for that channel reach.
