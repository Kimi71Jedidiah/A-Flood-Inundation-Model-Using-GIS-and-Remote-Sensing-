### This documentation explains inputs and outputs of our model, and detailed instruction about how to run it. 

#### 1 Model Inputs 

##### 1.1 Model Parameter file （model.par）

##### 1.2 Digital Elevation file (dem.asc)

This file specifies the Digital Elevation Model used by the model. It consists of a 2D raster array of ground elevations in ARC ascii raster format. The file may be manipulated using either the ARC-View or ARCGIS Geographical Information System platforms or manually edited using a text editor.

The file consists of a 6 line header followed by the numerical values of each data point on the grid as a 2D array of i rows and j columns. Each line of the header consists of a self-explanatory keyword followed by a numeric value. As an example is given below:

ncols         76          (Number of columns)

nrows         48          (Number of rows)

xllcorner     22950       (X cartesian co-ordinate of the lower left corner of the grid in metres)

yllcorner -2400           (Y cartesian co-ordinate of the lower left corner of the grid in metres)

cellsize 50.0             (Cell size in metres)

NODATA_value -9999        (Null value)

This DEM file is used for all the models.

##### 1.3 Channel Information (hanriver.river)

All our models simplify the Han river as a single channel with no tributary, and the channel is represented as a combination of multiple directed vector, which are connected by 9 points projected onto the DEM raster grid. Characteristics of the channel include **width**, **Manning’s n friction coefficient** and **bed elevation**. The Manning’s n friction coefficient is determined according to a reference table provided by FishXing software (http://www.fsl.orst.edu/geowater/FX3/help/8_Hydraulic_Reference/Mannings_n_Tables.htm).

We provide the three river characteristics' parameters - width, manning's n friction coefficient, and bed elevation for the starting (upstream) and end (downstream) points of the channel vector, and the code fills in intermediate points by linear interpolation. For boundary conditions, we input the recorded inflow Q on June 1st for the starting point.

We provide initial conditions for the starting point and ending point of the river. Initial 


### 1.4 Boundary Conditions (han_river_K.river)

#### 2 Model Outputs