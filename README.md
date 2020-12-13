Am205 Final Project
## A Distributed Flood Inundation Model Using GIS and Remote Sensising Data	
### Han River, China as a Study Case


Scarlett Gong, wenlin_gong@g.harvard

Qinyi Chen, qychen@g.harvard.edu

**Goal**: Besides Covid-19, another natural catastrophe--a 21 numbered floods (floods of a certain large scale) hit China in 2020 and is described as the worst floods since 1998. Started in early June 2020, heavy rains caused by the regional rainy season led to floods severely affecting large areas of southern China including the Yellow river and the Hanshui river. According to the Ministry of Water Resources, a total of 443 rivers nationwide have been flooded, with 33 of them swelling to the highest levels ever recorded. 

The **2020 China floods** has affected 63.46 million people and caused a direct economic loss of 178.96 billion CNY. Flood hazard has always been one of the most harmful disasters in China, so it is significant to obtain information on flood characteristics and vulnerability assessment of flood regions. With the goal to develops a GIS-based distributed model for simulating flood inundation, we choose the Hanshui river as a study case and collected precipitation data, inflow dischagre, and water level information from 11 hydropower stations along the Hanshui river. We apply the Shuttle Radar Topography Mission (SRTM) DEM data in the environment of GIS, and use LISFLOOD-FP, a raster-based flood inundation simulation software designed by the University of Bristol. We design a model that takes a one-dimensional diffusion wave representation for channel flow and a two-dimensional diffusion wave approximation of overland flow solved with the application of an implicit finite difference scheme. And the exchange of flows between river channel and overland surface is calculated through Manning’s formula.

