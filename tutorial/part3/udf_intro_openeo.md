# OpenEO - User Defined Functions


The openEO user defined functions (UDF's), provide a way to run Pangeo code as part of a larger openEO workflow.
This allows you to get the best of both worlds:
- You can use openEO to get access to a wide variety and full archives of EO data.
- Preprocessing to ARD such as Sentinel-1 backscatter is easily done in openEO
- For very fast interactive debugging of the core of your algorithm, local testing based on Pangeo is faster than basically any cloud based service
- Once your algorithm is ready, you can run it in the cloud without worries thanks to openEO


To understand user defined functions, it is recommended to start here:

https://open-eo.github.io/openeo-python-client/udf.html

## When (not) to use UDF's

Use UDF's when:

1. You have an existing algorithm that is too large/complex to reimplement in terms of openEO processes.
2. You require a process that is not supported yet, and don't have the time to propose a new process that can be implemented by the backend.

Do not use UDF's when:

1. You start from scratch and the algorithm can be expressed in openEO processes
2. You want to achieve the highest possible level of portability, without depending on any specific technology.
3. You are running on a backend that simply does not support UDF's.

## From UDF to predefined process

The most widely heard criticism of UDF's is that they are bad for portability because they introduce a technology dependency in your workflow.

We therefore have some general recommendations when implementing them. The general idea is that UDF's in fact allow to quickly test and use pieces of code
that can eventually become predefined processes. The fact that UDF's allow you to test a process idea in practice is actually a great
way to finetune the implementation and definition of your process. This avoids defining something which may require changes later on.

1. Try to keep UDF's small and modular. Many authors tend to include bits that were relevant outside openEO, but actually can be removed.
2. Minimize your dependencies. OpenEO requires far fewer extras compared to a file based workflow. You may need to adjust some imports!

When you identified a UDF that does one clear thing well, you may want to get in touch with the openEO team or your backend provider to see how it can
become an openEO predefined process. Also note that your implementation in Python may be the basis for an actual implementation in the backend!
