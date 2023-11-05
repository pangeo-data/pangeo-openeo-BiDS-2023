# Copernicus Data Space Ecosystem

[The Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu) is the public service that provides access to the
full archives of Copernicus Sentinel data. 
Next to data access, it also offers services for analyzing satellite imagery.
Most of the Pangeo & openEO training materials can be executed using the Jupyter Notebooks 
in the Copernicus Dataspace ecosystem.

## Registration

If you do not have an account yet, register [here](https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/auth?client_id=cdse-public&response_type=code&scope=openid&redirect_uri=https%3A//dataspace.copernicus.eu/account/confirmed/333) to create a new account.


![Copernicus registration](../figures/copernicus_registration.png)

Click on the **REGISTER** Button and fill all the reguired fields to create a new account.

## Getting access to Copernicus Jupyter Notebooks

To access the Copernicus Jupyter Notebook JupyterHub, you need to login at [https://jupyterhub.dataspace.copernicus.eu/hub/spawn](https://jupyterhub.dataspace.copernicus.eu/hub/spawn).

Then you can choose among the 3 available flavors (as shown on the figure below):


![Copernicus Jupyter Notebook flavors](../figures/copernicus_flavors.png)


For the tutorial, we suggest you use the "Large Server".

## Getting access to openEO in Copernicus data space

The openEO endpoint for Copernicus is documented here:
https://documentation.dataspace.copernicus.eu/APIs/openEO/openEO.html

The endpoint you can use in your scripts is: `openeo.dataspace.copernicus.eu` .

