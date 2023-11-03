# Scaling Big Data Analysis with Pangeo and OpenEO: Unlocking the Power of Space Data

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-10-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This repository contains the documentation and jupyter notebooks used for delivering tutorial to BiDS'23.

<img src="tutorial/figures/pangeo_openeo.png" /></a>
<br>

The content of this repository (folder `tutorial`) is rendered as an online document using [Jupyter Book](https://jupyterbook.org/en/stable/intro.html). **You can access it [here](https://pangeo-data.github.io/pangeo-openeo-BiDS-2023)**.

## Agenda

**Part-1: Pangeo**

- 9:00  Welcome (5 minutes)
- 9:05 Introduction and Motivation (15 minutes)
- 9:20 Overview of the Pangeo ecosystem (20 minutes)
- 9:40 Understanding Xarray to avoid common pitfalls (30 minutes)
- 10:10  Interactive Visualization with Hvplot (20 minutes)
- 10:30 Break (30 minutes)

**Part-2: OpenEO**

- 11:00 Getting started with OpenEO 
- 11:15 Finding Data, Running first graphs, difference to client-side processing
- 11:45 Integrate custom code into your workflow using User Defined Functions 
- 12:15 Feedback Block
- 12:30 Lunch

**Part-3: Unlocking the Power of Space Data with Pangeo & OpenEO**

- 14:00 Introduction to the afternoon session

- 14:05 Data discoverability and searchability
  - An overview of STAC and different sources and platforms (openeo.cloud, STAC browser, STAC Index ...)

- 14:30 Data and pre-processing general knowledge
  - Introduction to chunking examples with netcdf, zarr and Kerchunk
  - Parallelization with Dask

- 16:00 Different data exploitation approaches
  - How to exploit data on OpenEO (30 minutes)
  - Snow coverage example
  - How to exploit data on Pangeo (30 minutes)
  - Snow coverage pure xarray version

- 17:00 How to go beyond
  - Understanding how to create a custom algorithm: UDF (OpenEO) and ufunc (Xarray) (20 minutes)
  - Scaling with OpenEO (how it works underneath) (30 minutes)

- 17:45 Wrap-up and feedback survey (15 minutes)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/acocac"><img src="https://avatars.githubusercontent.com/u/13321552?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alejandro ©</b></sub></a><br /><a href="#ideas-acocac" title="Ideas, Planning, & Feedback">🤔</a> <a href="#design-acocac" title="Design">🎨</a> <a href="https://github.com/pangeo-data/foss4g-2022/commits?author=acocac" title="Code">💻</a> <a href="#content-acocac" title="Content">🖋</a> <a href="https://github.com/pangeo-data/foss4g-2022/commits?author=acocac" title="Documentation">📖</a> <a href="#tutorial-acocac" title="Tutorials">✅</a></td>
    <td align="center"><a href="http://www.mn.uio.no/geo/english/people/adm/annefou/"><img src="https://avatars.githubusercontent.com/u/8168508?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Anne Fouilloux</b></sub></a><br /><a href="#ideas-annefou" title="Ideas, Planning, & Feedback">🤔</a> <a href="#design-annefou" title="Design">🎨</a> <a href="https://github.com/pangeo-data/foss4g-2022/commits?author=annefou" title="Code">💻</a> <a href="#content-annefou" title="Content">🖋</a> <a href="https://github.com/pangeo-data/foss4g-2022/commits?author=annefou" title="Documentation">📖</a> <a href="#tutorial-annefou" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/guillaumeeb"><img src="https://avatars.githubusercontent.com/u/17138587?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Guillaume Eynard-Bontemps</b></sub></a><br /><a href="#ideas-guillaumeeb" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/pangeo-data/foss4g-2022/pulls?q=is%3Apr+reviewed-by%3Aguillaumeeb" title="Reviewed Pull Requests">👀</a> <a href="#userTesting-guillaumeeb" title="User Testing">📓</a> <a href="#content-guillaumeeb" title="Content">🖋</a> <a href="#infra-guillaumeeb" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/micafer"><img src="https://avatars.githubusercontent.com/u/4972699?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Miguel Caballer</b></sub></a><br /><a href="#platform-micafer" title="Packaging/porting to new platform">📦</a> <a href="#infra-micafer" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="http://about.me/rich.signell"><img src="https://avatars.githubusercontent.com/u/1872600?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rich Signell</b></sub></a><br /><a href="#ideas-rsignell-usgs" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://uk.linkedin.com/in/sebastianlunavalero/en"><img src="https://avatars.githubusercontent.com/u/5345517?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sebastian Luna-Valero</b></sub></a><br /><a href="#platform-sebastian-luna-valero" title="Packaging/porting to new platform">📦</a> <a href="#infra-sebastian-luna-valero" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/tinaok"><img src="https://avatars.githubusercontent.com/u/46813815?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tina Odaka</b></sub></a><br /><a href="#ideas-tinaok" title="Ideas, Planning, & Feedback">🤔</a> <a href="#design-tinaok" title="Design">🎨</a> <a href="https://github.com/pangeo-data/foss4g-2022/commits?author=tinaok" title="Code">💻</a> <a href="#content-tinaok" title="Content">🖋</a> <a href="https://github.com/pangeo-data/foss4g-2022/commits?author=tinaok" title="Documentation">📖</a> <a href="#tutorial-tinaok" title="Tutorials">✅</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/sustr4"><img src="https://avatars.githubusercontent.com/u/1583737?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Zdeněk Šustr</b></sub></a><br /><a href="#platform-sustr4" title="Packaging/porting to new platform">📦</a> <a href="#infra-sustr4" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/j34ni"><img src="https://avatars.githubusercontent.com/u/44261743?v=4?s=100" width="100px;" alt=""/><br /><sub><b>j34ni</b></sub></a><br /><a href="#platform-j34ni" title="Packaging/porting to new platform">📦</a> <a href="#infra-j34ni" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/pl-marasco"><img src="https://avatars.githubusercontent.com/u/22492773?v=4?s=100" width="100px;" alt=""/><br /><sub><b>pl.marasco</b></sub></a><br /><a href="#ideas-pl-marasco" title="Ideas, Planning, & Feedback">🤔</a> <a href="#design-pl-marasco" title="Design">🎨</a> <a href="https://github.com/pangeo-data/foss4g-2022/commits?author=pl-marasco" title="Code">💻</a> <a href="#content-pl-marasco" title="Content">🖋</a> <a href="https://github.com/pangeo-data/foss4g-2022/commits?author=pl-marasco" title="Documentation">📖</a> <a href="#tutorial-pl-marasco" title="Tutorials">✅</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
