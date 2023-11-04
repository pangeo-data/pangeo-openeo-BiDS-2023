# Advanced workflows in openEO

## Authors & Contributors

- Jeroen Dries, VITO (Belgium)

## Objectives

- Learn about what is achievable with standardized openEO processes
- What are openEO platform 'credits'
- Learn about metadata generation in openEO

## Algorithm types

When writing an algorithm in openEO or Pangeo, the first thing to do is to determine the type of algorithm.
Once you know the type, you can fall back to well-known examples as a template to implement your algorithm.

Using the right method for your type of algorithm also ensures that it can be parallellized and executed 
in the most efficient way. An algorithm that only requires a single observation for instance, does not need
to bother with retrieving a full timeseries of observations.

In part 2 of this tutorial, we'll cover a few common types:
- single observation, single pixel
- temporal analysis over a single pixel

In part 3, we have an example of an analysis that requires multiple values in both space and time.


## Case 1 Rank composites 

Scientifically correct compositing is the foundation of many EO processing workflows.
This case shows a max-NDVI composite, which is also a template for more advanced composites.

Key takeaways:
- Use array_apply to 'loop' over data
- Create masks to selectively load data

Algorithm type: 
- Spatial neighborhood for cloud proximity score/masking
- Per pixel temporal analysis for scoring

https://github.com/Open-EO/openeo-community-examples/blob/main/python/RankComposites/rank_composites.ipynb

## Case 2 Machine learning training and inference

Timeseries based classification of pixels to assign categorical labels is another base-technique in the EO 
toolbox. This example uses Random Forest, which is superseded by more advanced AI models, but is still 
regarded by many as a baseline against which more complex approaches can be compared.

Operational products, like [Copernicus landcover 3.0](https://land.copernicus.eu/global/products/lc) are
also based on random forest.

Key takeaways:
- Transform a timeseries datacube into features for learning
- Use ML processes directly from openEO

Algorithm type: per-pixel timeseries analysis

Dynamic landcover: https://docs.openeo.cloud/usecases/landcover/

## Case 3 ESA WorldWater

ESA WorldWater is an example of rule based classification, using Sentinel-2 and Sentinel-1, it was developed
by DHI-GRAS.

Key takeaways:
- Use of complex, rule-based classification

Algorithm type: 

- temporal compositing into ARD
- single observation, single pixel, analysis

Note: the most recent code of this example is still under review in a pull request, so we include the relevant bits inline. 

https://github.com/DHI-GRAS/worldwater-toolbox
https://github.com/DHI-GRAS/worldwater-toolbox/blob/ccd01afef4d634c3727c7f3d06e423acf7680131/world_water_toolbox/wwt.py

ESA Worldwater formulas are written using predefined functions:

```python
from openeo.processes import if_, exp, array_element, log, count, gte, eq, sum

LOOKUPTABLE = {
"Deserts": {
    "S1": lambda vh, vv: 1 / (1 + exp(- (-7.03 + (-0.44 * vv)))),
    "S2": lambda ndvi, ndwi: 1 / (1 + exp(- (0.133 + (-5.92 * ndvi) + (14.82 * ndwi)))),
    "S1_S2": lambda vv, ndvi, ndwi: 1 / (1 + exp(- (-3.69 + (-0.25 * vv) + (0.47 * ndvi) + (15.3 * ndwi)))),
},
"Mountain": {
    "S1": lambda vh, vv: 1 / (1 + exp(- (-3.76 + (-0.262 * vv)))),
    "S2": lambda ndvi, ndwi: 1 / (1 + exp(- (0.262 + (0.75 * ndvi) + (12.65 * ndwi)))),
    "S1_S2": lambda vv, ndvi, ndwi: 1 / (1 + exp(- (-1.13 + (-0.11 * vv) + (3.03 * ndvi) + (13.21 * ndwi)))),
},
...
}

```


An openEO 'apply_dimension' over bands is used to compute final water occurance.

```python
from openeo.processes import if_, exp, array_element, log, count, gte, eq, sum

merged = s1_s2_water.merge_cubes(s2_median_water).merge_cubes(s1_median_water)

def combined(bands):
    s1_s2_water = bands.array_element(0)
    s1_s2_mask = s1_s2_water >= 0

    s2_median_water = bands.array_element(1)
    s2_mask = if_(s1_s2_mask == 0, s2_median_water) >= 0

    s1_median_water = bands.array_element(2)
    s1_mask = if_(s2_mask == 0, if_(s1_s2_mask == 0, s1_median_water)) >= 0

    s1_s2_masked = if_(s1_s2_mask != 0, s1_s2_water, 0)
    s2_masked = if_(s2_mask != 0, s2_median_water, 0)
    s1_masked = if_(s1_mask != 0, s1_median_water, 0)

    return s1_s2_masked + s2_masked + s1_masked

merge_all = merged.apply_dimension(combined, dimension='bands')

```

A similar water detection example is the AquaMonitor, developed by Deltares:
https://github.com/c-scale-community/use-case-aquamonitor

## Accounting in openEO platform

When running openEO scripts on small scale locally, you use your own resources. When running at larger
scale in the cloud, this generates a small cost per run. 

While these costs are often relatively small compared to the time savings, it is important to keep track of.
Here we explain how to do exactly that.

https://docs.openeo.cloud/federation/accounting.html
