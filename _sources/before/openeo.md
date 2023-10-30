
# OpenEO

## Registration

<figure>
    <img src="https://raw.githubusercontent.com/openEOPlatform/documentation/main/join/Registration_Flow.png" alt="Registration Flow">
    <figcaption>Figure 1: Registration Flow</figcaption>
</figure>

Register for openEO Platform and immediately start a 30 day free trial:

<a href="https://sso.terrascope.be/auth/realms/terrascope/protocol/openid-connect/auth?client_id=openeoplatform&redirect_uri=https://openeo.cloud/welcome-to-openeo-platform/&state=0%2F95954a95-1968-4a64-8b88-fef0f47936fb&response_type=code&scope=openid" class="action-button" style="display: inline-block; font-size:1.2rem; color: #fff; background-color: #335e6f; padding: 0.8rem 1.6rem; border-radius: 4px; border-bottom: 1px solid #2e5564;">&rarr; Register for openEO Platform</a>

Free trial users receive **1000 free credits** upon registration. openEO Platform is a federation of services which include:
- EGI for Authentification & Authorization via [EGI Check-in](https://www.egi.eu/services/check-in/)
- Terrascope EOPlaza for Account management
- EODC for provisioning of JupyterLab
- Terrascope including Sentinel Hub connection via the EuroDataCube, EODC and Sentinel Hub backends

The Network of Resources a ESA sponsoring initiative to facilitate the use of cloud environments.
The registration link above will lead you automatically through a couple of phases,
which are explained in the graphic below.

### Connect with EGI Check-in

The first step is to become member of the *EGI User Community*, 
by creating an account there,
preferably by just connecting with an **existing account**
and filling in some additional information.


:::{tip} EGI Check-in based "Single Sign-on"
OpenEO Platform relies on
[EGI Check-in](https://www.egi.eu/services/check-in/)
(provided by the [EGI Foundation](https://egi.eu))
for authentication and authorization services,
which offers several benefits:

- Register and log in through an **existing account**
  from either your academic/scientific institution,
  or other social platforms such as Google, GitHub, Facebook or LinkedIn.
- No need to set up and remember yet another username-password combo.
- Neither openEO Platform nor the EGI Foundation see, handle or store your password.
- openEO Platform and EOPlaza only keep minimal user information (e.g. email address).
  Check the privacy policy of [openEO Platform](https://openeo.cloud/privacy-policy)
  and [EOPlaza](https://vito.be/en/privacy-policy) for further details.
- Use the same EGI account accross multiple scientific services
:::


:::{warning} Recommendation
We recommend using your **institutional account** whenever possible.
Nevertheless, if you are the first member of your institution to work with EGI Check-in, 
problems may occur and sometimes require your institution's IT team to properly
support EGI Check-in through EduGain.
[Contact EGI](https://www.egi.eu/service-contact/) for further support.
:::


:::{tip} Already connected?
Did you already connect an existing account with EGI Check-in in the past,
or you are unsure about that?
Just follow the procedure discussed here:
previously completed steps will be skipped automatically.
:::


To get an idea of how the EGI sign up flow works and what it will require from you,
you can consult an [illustrated step-by-step guide in the EGI Documentation](https://docs.egi.eu/users/aai/check-in/signup/).
If problems occur during this process, feel free to send a support request to `check-in <at> egi.eu`.


If you didn't see the list of institutions and (social) platforms, you are likely already logged in.
In this case you can simply select *'SIGN UP'*.

Afterward, you will have to complete a small registration procedure to connect your account.
You may have to fill any missing personal information: *Name*, *Email*, *Affiliation* and/or *Organisation*.

:::{danger} Patience required!
Please Wait until your registration is processed and you see the following Banner on top of your screen:
:::
<figure>
    <img src="https://raw.githubusercontent.com/openEOPlatform/documentation/main/join/join0.png" alt="Join EGI user community - process end">
    <figcaption>Figure 2: Join EGI user community - Screen when the process is finished</figcaption>
</figure>


After submitting the registration form, you will receive a verification e-mail.
The e-mail verification needs to be completed before you can contine with the next steps.


### EOPlaza

Once you finished the registration flow at EGI Check-in, 
you will be forwarded to EOPlaza for further set up of your openEO Platform account.

For example, on the [EOPlaza Dashboard](https://portal.terrascope.be/dashboard)
you can consult your balance of credits.
Whenever you consume processing resources on openEO Platform, credits will be deducted. 
You can increase the number of credits by a [Network of Resources](https://openeo.cloud/esa-network-of-resources-funding/) request, 
or acquiring them directly on EOPlaza.


If you have any questions about the enrollment to openEO Platform or the free trial period,
please [contact us](https://openeo.cloud/contact/).


### Working with openEO Platform

After you've been registered on openEO Platform, you can start working with
the platform through any of the clients. With all clients you will need to connect to
`https://openeo.cloud` and then authenticate through EGI Check-in with the 
account used above.

:::{tip} Tip
For your own convenience, we advise you to always log in with the same identity provider you originally registered with. Otherwise, you run the risk of creating a separate new EGI account, which in turn will have to go through the openEO Platform virtual organization acceptance process again.
It is possible to link multiple accounts from multiple identity providers to the same EGI account. However, this must be done before you use these accounts to log in, as explained in the [EGI documentation](https://docs.egi.eu/users/aai/check-in/linking/).
:::

See the getting started guides to find out more about how to use the clients for this:

* [Editor](../getting-started/editor/index.md)
* [JavaScript](../getting-started/javascript/index.md#authentication)
* [JupyterLab](../getting-started/jupyterlab/index.md)
* [Python](../getting-started/python/index.md#authentication)
* [R](../getting-started/r/index.md#authentication)

 
