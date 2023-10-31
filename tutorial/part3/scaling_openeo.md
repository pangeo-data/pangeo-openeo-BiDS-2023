# Scaling openEO & under the hood

## Under the hood

openEO backends rely on the same principles as e.g. Dask and any other large scale parallel processing framework:

* The 'map/reduce' paradigm
* Data 'partitioning'

As openEO user, you don't really need to fully understand these things, but it can be useful to better understand performance. 
We give some examples:

An 'apply' process like 2*band_value is very efficient because each pixel can be processed independently.
A process like 'apply_dimension' over time can require the data to be reshuffled so it can be quite cost intensive over long time series.
Aggregate_spatial with a sum over pixels can be implemented as a 'reduce' style operation, making it again relatively efficient.

Data partitioning is also something that a backend normally does for you, but it may happen that it is not 'smart enough' to understand your use case.This
can lead for instance to 'out of memory' style errors.

### Understanding logs

An openEO backend provides logging, but it can be particularly hard to understand. This again has to do with the cloud based nature: 
when running your job on many machines in parallel, all kinds of 'warnings' and even 'error' messages can be generated. There
is however a level of fault-tolerance, so there may be errors that are not actually an issue, or there may be errors caused later on, where
the actual cause was logged earlier. 

So in general, it can help to look for those earliest errors if you see a lot of confusing messages. The log level filtering functionality can 
help you to do that.


## General performance tips

### Keep the size of your data cube in mind
Backends are distributed, cloud based programs, but it is still possible to overload them easily due to the sheer size of earth observation datasets.
If your algorithm at some point reduces dataset size, you may want to put this step early in the algorithm. 

Some typical examples:
- cloud filtering
- masking on a specific landcover type. (e.g. filtering on forest pixels only when you work on a forest app)
- reducing temporal resolution, e.g. 10-daily or monthly compositing
- reducing resolution
- fiter on bands, orbit direction, ...

### Try to keep the graph simple

Backends may try to 'understand' your process graph, to choose the most optimal evaluation path. 
Sometimes people introduce an unneeded amount of 'merge_cubes' processes, and the graph starts to look quite complex. 
At this point, also the backend may have trouble understanding this, and your execution is also slow.


### Data collection types

While openEO offers access to many different collections, not all of them use optimal formats or are stored close to the processing center. 
The result is that there can be quite large difference in performance depending on which collection you use. Hence, it may be smart to check 
with your backend provider on the specifics of a given collection before trying to use it at scale.

## Continental scale processing

Reference: https://docs.openeo.cloud/usecases/large-scale-processing/

