### This documentation explains inputs and outputs of our model, and detailed instruction about how to run it. 

## 1 Model Inputs 

### 1.1 Model Parameter file （model.par）

### 1.2 Digital Elevation file (dem.asc)

This file specifies the Digital Elevation Model used by the model. It consists of a 2D raster array of ground elevations in ARC ascii raster format. The file may be manipulated using either the ARC-View or ARCGIS Geographical Information System platforms or manually edited using a text editor.

The file consists of a 6 line header followed by the numerical values of each data point on the grid as a 2D array of i rows and j columns. Each line of the header consists of a self-explanatory keyword followed by a numeric value. As an example is given below:

ncols         76          (Number of columns)

nrows         48          (Number of rows)

xllcorner     22950       (X cartesian co-ordinate of the lower left corner of the grid in metres)

yllcorner -2400           (Y cartesian co-ordinate of the lower left corner of the grid in metres)

cellsize 50.0             (Cell size in metres)

NODATA_value -9999        (Null value)

This DEM file is used for all the models.

### 1.3 Channel Information (hanriver.river)

All our models simplify the Han river as a single channel with no tributary, and the channel is represented as a combination of multiple directed vector, which are connected by 9 points projected onto the DEM raster grid. Characteristics of the channel include **width**, **Manning’s n friction coefficient** and **bed elevation**. The Manning’s n friction coefficient is determined according to a reference table provided by FishXing software (http://www.fsl.orst.edu/geowater/FX3/help/8_Hydraulic_Reference/Mannings_n_Tables.htm).

We provide the three river characteristics' parameters - width, manning's n friction coefficient, and bed elevation for the starting (upstream) and end (downstream) points of the channel vector, and the code fills in intermediate points by linear interpolation. For boundary conditions, we input the recorded inflow Q on June 1st for the starting point.

We provide initial conditions for the starting point and ending point of the river. Initial 


### 1.4 Boundary Conditions (han_river_K.river)

## 2 Model Outputs

### 2.1 Water depth Results (eg. res_4e8_f-0000.wd)

Water depth results files (.wd) can be viewed as an animation in FloodView.exe, which is bundled with the model and data files (windows only). Double-click the FloodView icon to open the program and load results files using File>Open (use the ctrl button to load multiple .wd files for animation). DEM files can be added to the animation using File>Load DEM. These options will work using other results files and filename extensions, however, FloodView expects files to be in ARC ascii raster format and the colour-scale for animations is set for the typical expected range of water depth values. FloodView is also fairly temperamental and usually likes things to be done in above order only.

All gridded output data from the model is in ARC ascii raster format and can be easily uploaded for visualisation and analysis in ARC-GIS software (note – file extensions will need to be changed to .asc). Alternatively, gridded or tabulated data files are often uploaded for quick visualisation or graphing into Excel using File>Open, selecting “All Files *.*” and a suitable delimiter. For more sophisticated data manipulation or visualisation files could be imported into MatLab. Some code has been written to facilitate quick import of LISFLOOD output files into MatLab and can be found at https://source.ggy.bris.ac.uk/wiki/LISFLOOD-FP_and_MATLAB.

### 2.2 (eg. res_4e8_f.mass)

This file gives details of the model mass balance performance and is written at the interval specified by the keyword massint in the parameter file. The output consists of 11 columns of data, space separated:

Column 1: Time. The time in seconds at which the data was saved.

Column 2: Tstep. Time step specified by the user (initial time step in the adaptive model) in seconds 

Column 3: MinTstep. Minimum time step used so far during the simulation in seconds

Column 4: NumTsteps. Number of time steps since the start of the simulation.

Column 5: Area. Area inundated in $m^2.$

Column 6: Vol. Volume of water in the domain in $m^3.$

Column 7: Qin. Inflow discharge in $m^3/s$.

Column 8: Hds. Water depth at the downstream exit of the model domain in meters.

Column 9: Qout. Calculated outflow discharge at the downstream exit of the model domain in $m^3/s$.

Column 10: Qerror. Volume error per second in $m^3/s$.

Column 11: Verror. Volume error per mass interval (massint variable in the parameter file) $m^3$.

Column 12: Rain-Inf+Evap. Cumulative effect of infiltration, evaporation and rainfall over the simulation in $10^3 m^3$ .

### 2.3 (eg. res_4e8_f.max)

This file consists of a grid in ARC ascii raster format of the maximum water depth (.mxa) predicted by the model for each pixel over the course of the simulation. Units are in metres. These values are the maximum values over the whole simulation (i.e. over each time step).

### 2.4 (eg. res_4e8_f.totalm)

This file consists of a grid in ARC ascii raster format of the total time for which a pixel is inundated (.totaltm). Units are in **hours** from the start of the simulation. .

### 2.5 Time of Initial Inundation (eg. res_4e8_f.inittm)

This file consists of a grid in ARC ascii raster format of the time of initial inundation for each pixel. Units are in **hours** from the start of the simulation.

### 2.6 Time of Maximum Depth (eg. res_4e8_f.maxtm)

This file consists of a grid in ARC ascii raster format of the time of maximum inundation depth in each pixel (.maxtm). Units are in **hours** from the start of the simulation.

### 2.7 (eg. res_4e8_f.segmask)

These files provides more information on the structure of the 1D river model after interpolation of the river vector to the 2D grid. They are in ARC ascii raster format. segmask is an integer raster showing the tributary numbers for the channels. By default these files are not produced and are only output if the keyword debug appears in the .par file.

### 2.8 (eg. res_4e8_f.chmask)

These files provides more information on the structure of the 1D river model after interpolation of the river vector to the 2D grid. They are in ARC ascii raster format. chmask is a raster showing the location of the channels. By default these files are not produced and are only output if the keyword debug appears in the .par file.

### 2.9 (eg. res_4e8_f.dem)

This file provides more information on the structure of the 1D river model after interpolation of the river vector to the 2D grid. They are in ARC ascii raster format. The modified DEM includes the channel bed elevations (in meters) in cells containing 1D rivers. By default these files are not produced and are only output if the keyword debug appears in the .par file.

### 2.10 (eg. res_4e8_f.op)

This file consist of a grid of water depths (in meters) in ARC ascii raster format for each pixel at the time of each satellite overpass specified using the parameter file keyword overpass, or overpassfile for multiple outputs (see lisflood-manual-v5.9.6). Numbering of overpass times commences at zero.
