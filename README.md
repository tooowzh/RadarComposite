# Radar Composite: a scalable framework for digesting and analyzing WSR-88D radar data

[![Build Status](https://travis-ci.org/striges/RadarComposite.svg?branch=master)](https://travis-ci.org/striges/RadarComposite)

## Highlights:
* Big Data ready: Apache Spark based parallel engine with Apache Hadoop based storage.
* Cross-platform: run on Windows, Mac and Linux
* Scalable anywhere: from personal PC to High-performance cluster environments (PBS). 
* Plugable interface to accept almost any MapReduce function
* Spatial analysts compatibility: Run geoprocessing scripts without standalone GIS software, and in parallel

License: LGPLv3

We're actively moving this project to completely free-of-use. We're actively removing any components that rely on closed source product.

On-going task:
* Migrating to SBT. Handle Python codes in SBT tasks
* Adopting Py-ART and wradlib to support more data type
* Providing quality control and data correction.
* 3D wind field retrieval.
* Increase compatibility on Windows platform. Utilizing docker and Hyper-V to adapt any software from Linux
* Increase GIS compatibility on Linux

**This a data-processing framework, thus there is no visualization in this system. We have no plan to add any visualization function in this framework.**

To load radar data into GIS, please check Radar Toolkit for ArcGIS.

**We're moving code to GitHub as SBT project. Codes may not be complete now. Please go back and check often.**

*You must obtain your own ArcGIS Runtime Developer license (free) to execute geoprocessing function. Due to license restriction, we **only** provide source code.*
*You need ArcGIS Desktop to build geoprocessing package. (Guides will be provided later)*

## Acknowledgements:

Py-ART: https://github.com/ARM-DOE/pyart
wradlib: http://wradlib.bitbucket.org/
WDSS-II: http://www.wdssii.org/
Py-ART forks by Kirk North: https://github.com/kirknorth