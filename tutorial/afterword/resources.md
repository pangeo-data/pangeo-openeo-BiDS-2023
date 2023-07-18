
![Pangeo logo](.././figures/pangeo_name_logo.png) 

**A community platform for Big Data geoscience** 

### Join the community!

| Information | Links                                                                                                                                                                                                                                                                                    |
| :--- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Website** | https://pangeo.io/                                                                                                                                                                                                                                                                       |
| **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Pangeo--data-blue?logo=github)](https://github.com/pangeo-data)                                                                                                                                                                           |
| **Examples** | [![Gallery](https://img.shields.io/badge/Pangeo-Gallery-orange)](http://gallery.pangeo.io/)                                                                                                                                                                                              |
| **Chat** | [![Gitter](https://img.shields.io/badge/Gitter-Chat-yellow?logo=gitter)](https://gitter.im/pangeo-data/Lobby)  [![Pangeo - Discourse](https://img.shields.io/discourse/users?server=https%3A%2F%2Fdiscourse.pangeo.io%2F&style=flat-square&logo=discourse)](https://discourse.pangeo.io) |
| **News** | [![Medium - Blog](https://img.shields.io/badge/Medium-Blog-2ea44f?logo=medium)](https://medium.com/pangeo) [![Fllo](https://img.shields.io/twitter/follow/pangeo_data?style=social)](https://twitter.com/pangeo_data)                                                                    |

### Meetings
- [General](https://pangeo.io/meeting-notes.html#community-meeting): Pangeo holds community meetings meetings every Wednesday. The meetings alternate between 12PM and 4PM US Eastern Time to encourage participants from a wider range of time zones. 
- [Continental meetings](https://pangeo.io/meeting-notes.html#continental-community-meetings): to adress different time zones among the globe continental meetings have been organized in Europe/Africa and Oceania.
- [Showcases](https://pangeo.io/pangeo-showcase.html#pangeo-showcase): 15 minutes talks which are an opportunity for anyone to meet other members of the Pangeo community and let them know what you are working on. The talks are recorded, given a DOI, and made available on the [Pangeo YouTube Channel](https://youtube.com/playlist?list=PLuQQBBQFfpgq0OvjKbjcYgTDzDxTqtwua). If you are interested in giving a talk, [fill out this short form](https://forms.gle/QwxKusVvrvDakSNs8).

### Cloud infrastructure
- [2i2c JupyterHub](https://us-central1-b.gcp.pangeo.io/hub/login?next=%2Fhub%2F): serves Pangeo on open source infrastructure. It's operated and designed by [2i2c](https://2i2c.org/), and funded by [NSF EarthCube Program (Award ICER-2026932)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2026932). The service is **open to anyone** that a hub administrator has approved the application form (see [here](https://docs.google.com/forms/d/e/1FAIpQLSeqKncKG-s365pC_Lfe4_UetJ-wcFfjOSyHhYYQjXbKRHzswQ/viewform)). Find a blog post informing the 2i2c/Pangeo partnership [here](https://2i2c.org/blog/2021/pangeo-goes-live/).

### Data life cycle
- [Pangeo Forge](https://pangeo-forge.org/):  a tool designed to aid the extraction, transformation, and loading of datasets.

### Most recent trainings (2021/22)
- [Galaxy training in climate data](https://training.galaxyproject.org/training-material/topics/climate/): contains two modules introducing Pangeo, _Pangeo ecosystem 101 for everyone_ and _Pangeo Notebook in Galaxy - Introduction to Xarray_ showcasing how the Pangeo stack assists processing and analysing big climate datasets.
- [BIOGEOMON 2022 Python Pangeo Workshop](https://github.com/LandscapeGeoinformatics): led by [Landscape Geoinformatics](https://github.com/LandscapeGeoinformatics) includes Jupyter notebooks demonstrating Xarray for working with labeled multi-dimensional arrays of data. The material also shows a few basic steps how to improve reproducibility and pro-actively apply FAIR principles when sharing and archiving data and code online for publishing via [GitHub](https://github.com/) and [Zenodo](https://zenodo.org/).
- [FOSS4G 2021](https://github.com/pangeo-data/foss4g-2021): focuses on data discovery with SpatioTemporal Asset Catalogs (STAC), data loading with Cloud-optimized formats (Cloud-Optimized Geotiff, ZARR), and scalable analysis with Xarray and Dask libraries.

## Additional resources/initiatives consuming Pangeo stack
_List of some active initiatives. Find more in https://github.com/pangeo-data_.

- [CarbonPlan](https://carbonplan.org/): _non-profit initiative_, analyzes climate solutions based on the best available science and data. The team works collaboratively with the Pangeo community to build open tools and resources for the evaluation and deployment of robust climate programs.
- [CliMetLab](https://github.com/ecmwf/climetlab): _package_, aims at simplifying access to climate and meteorological datasets, allowing users to focus on science instead of technical issues such as data access and data formats. 
- [climpred](https://github.com/pangeo-data/climpred): _package_, aims to be the primary package used to analyze output from initialized dynamical forecast models, ranging from short-term weather forecasts to decadal climate forecasts.
- [Digital Earth Africa Sandbox](https://sandbox.digitalearth.africa/): _platform_, a cloud-based computational platform that operates through a Jupyter Lab environment. It provides a limited, but free compute resource for technical users and data scientists to explore DE Africa data and products. The platform consumes `xarray` and `dask` to optimize the processing and analysis of the curated datasets. 
- [EOOffshore](https://eooffshore.github.io/): _research project_, presents a case study that demonstrates the utility of the Pangeo software ecosystem to address these issues in the development of offshore wind speed and power density estimates, increasing wind measurement coverage of offshore renewable energy assessment areas in the [Irish Continental Shelf](https://www.marine.ie/Home/site-area/irelands-marine-resource/real-map-ireland) region.
- [Fastscape LEM](https://fastscape.org/): _software stack_, aims at making landscape evolution models and topographic analysis algorithms readily accessible to a wide range of users, from experts in landscape evolution modelling to scientists, researchers and teachers in the broader Earth science community.
- [flox](https://github.com/xarray-contrib/flox): _package_, explores strategies for fast GroupBy reductions with `dask.array`. It used to be called dask_groupby.
- [NetCarbon](https://www.netcarbon.fr/home): _startup company_, offering farmers a free solution for measuring and monetizing their sequestered carbon to contribute towards carbon neutrality. 
- [Planetary Computer](https://planetarycomputer.microsoft.com/): _platform_, a cloud-based computational platform aiming to combine a petabyte catalog of analysis-ready geospatial data, an API that facilitates spatiotemporal querying over that data and a computing environment that simplifies distributed computing workloads.
- [PyGMT](https://github.com/GenericMappingTools/pygmt): _package_, facilitates processing geospatial and geophysical data and making publication quality maps and figures. 
- [scivision](https://github.com/alan-turing-institute/scivision): _package_, aims to connect computer vision model developers to image data providers from diverse scientific fields. The project builds upon existing libraries to create and manipulate data catalogues e.g. `intake`, and `xarray` to handle N-dimensional data for exploring CV models.
- [Urban Grammar AI research project](https://urbangrammarai.xyz/): _research project_, proposes a conceptual framework to characterize urban structure through the notions of spatial signatures and urban grammar. In addition to consume the Pangeo stack, the resource demonstrates some notebooks using [`dask_geopandas`](https://github.com/geopandas/dask-geopandas) to optimize processing and analysing spatial operations on geometric types.
- [verde](https://github.com/fatiando/verde), _package_, aims at processing spatial data (bathymetry, geophysics surveys, etc) and interpolating it on regular grids (i.e., gridding).
- [xarray-sentinel](https://github.com/bopen/xarray-sentinel): _package_, facilitates access and exploration of the SAR data products of the Copernicus Sentinel-1 satellite mission.
- [xESMF](https://github.com/pangeo-data/xESMF): _package_, a regridding tool suited for non-orthogonal grids. xESMF tries to be simple and intuitive.
- [xMIP](https://github.com/jbusecke/xMIP): _package_, facilitates the cleaning, organization and interactive analysis of Model Intercomparison Projects (MIPs) within the Pangeo software stack.