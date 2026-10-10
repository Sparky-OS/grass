<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/sparky-stereo-os/sparkyos-swirl-light-128.png">
  <img src=".github/sparky-stereo-os/sparkyos-swirl-dark-128.png" alt="SparkyOS" width="128" height="128">
</picture>

## Sparky Stereo OS

This is the stereo version of GRASS by Sparky Stereo OS, forked from [OSGeo/grass](https://github.com/OSGeo/grass).
Its 3D view (NVIZ) can draw the scene from the left and the right eye, one world and two cameras, into an OpenGL quad-buffer stereo window when its stereo setting asks for it.
Without the setting nothing changes; on Sparky Stereo OS the desktop shows the stereo window on any 3D display.

Where it comes from:

- [GRASS](https://grass.osgeo.org/) is developed by the GRASS Development Team, with the people listed in [AUTHORS](AUTHORS), [contributors.csv](contributors.csv) and [contributors_extra.csv](contributors_extra.csv).
- [Debian](https://www.debian.org/) is the base of the system.
- [SparkyLinux](https://sparkylinux.org/), by Paweł "pavroo" Pijanowski, builds on Debian.
- [Sparky Stereo OS](https://github.com/Sparky-OS/sparky-stereo-os) is the stereo 3D edition of SparkyLinux: SparkyOS, powered by Debian.

The `stereo3d` branch holds this work on GRASS 8.5.0, the version Debian ships.
The licence is unchanged; see [COPYING](COPYING).

Sparky Stereo OS, Daniel Ramos's edition of SparkyLinux (by Paweł "pavroo" Pijanowski).

---

# GRASS Repository

[![GCC C/C++ standards check](https://github.com/OSGeo/grass/workflows/GCC%20C/C++%20standards%20check/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3A%22GCC+C%2FC%2B%2B+standards+check%22)
[![Python code quality check](https://github.com/OSGeo/grass/workflows/Python%20code%20quality%20check/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3A%22Python+code+quality+check%22)
[![General linting](https://github.com/OSGeo/grass/workflows/General%20linting/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3A%22General+linting%22)
[![Ubuntu](https://github.com/OSGeo/grass/workflows/Ubuntu/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3AUbuntu)
[![OSGeo4W](https://github.com/OSGeo/grass/workflows/OSGeo4W/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3AOSGeo4W)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/OSGeo/grass/badge)](https://securityscorecards.dev/viewer/?uri=github.com/OSGeo/grass)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/2470/badge)](https://www.bestpractices.dev/projects/2470)
[![Coverity](https://scan.coverity.com/projects/1038/badge.svg)](https://scan.coverity.com/projects/grass)  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5176030.svg)](https://doi.org/10.5281/zenodo.5176030)
[![Discourse](https://img.shields.io/badge/discourse-forum-blue?logo=discourse)](https://discourse.osgeo.org/c/grass/62)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/OSGeo/grass/main?labpath=doc%2Fexamples%2Fnotebooks%2Fjupyter_example.ipynb)  
[![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](http://numfocus.org)
[![Hosted by OSGeo](https://img.shields.io/badge/hosted%20by-OSGeo-4cb05b.svg?style=flat&labelColor=00393f)](https://www.osgeo.org/)

## Description

[GRASS](https://grass.osgeo.org/), Geographic Resources Analysis Support System,
is a powerful computational engine for raster, vector, and geospatial processing.
It supports terrain and ecosystem modeling, hydrology, data management,
and imagery processing. With a built-in temporal framework and Python API,
it enables advanced time series analysis and rapid geospatial programming,
optimized for large-scale analysis on various hardware configurations.

You can use GRASS as your desktop Geographic Information System (GIS)
or as a geoprocessing engine through command-line, Python or R interface.

GRASS is open-source and free software,
available under the [GNU General Public License](https://www.gnu.org/licenses/#GPL),
and hosted by the Open Source Geospatial Foundation ([OSGeo](https://www.osgeo.org/)).

[//]: # (numfocus-fiscal-sponsor-attribution)

GRASS uses a [custom governance model](./GOVERNANCE.md)
and is fiscally sponsored by [NumFOCUS](https://numfocus.org/). Consider making
a [tax-deductible donation](https://numfocus.org/donate-to-grass) to help the project
pay for developer time, professional services, travel, workshops,
and a variety of other needs.

<!-- markdownlint-disable MD033 -->
<div align="center">
  <a href="https://numfocus.org/donate-to-grass">
    <img height="60px"
         alt="NumFOCUS logo",
         src="https://raw.githubusercontent.com/numfocus/templates/master/images/numfocus-logo.png"
         align="center">
  </a>
</div>
<br>

NumFOCUS is a 501(c)(3) non-profit charity in the United States;
as such, donations to NumFOCUS are tax-deductible as allowed by law.
As with any donation, you should consult with your personal tax adviser or
the IRS about your particular tax situation.

## Downloads

See [download instructions](https://grass.osgeo.org/download/)
to get GRASS for your platform.

## Documentation

See [documentation](https://grass.osgeo.org/grass-devel/manuals/index.html)
and [tutorials](https://grass-tutorials.osgeo.org/) to start learning GRASS.

## Getting help

Join the GRASS community on [Discourse](https://discourse.osgeo.org/c/grass/grass-user/70)
or explore [GRASS commercial support](https://grass.osgeo.org/support/commercial/).

## Contributing

All contributions are welcome! Join GRASS developer community on [Discourse](https://discourse.osgeo.org/c/grass/developer/61)
to discuss your plans or simply open
a [pull request](https://github.com/OSGeo/grass/pulls).
See [CONTRIBUTING file](CONTRIBUTING.md) for more details.

## Compiling GRASS

See the [INSTALL.md file](INSTALL.md). In addition, there are
detailed [compile instructions](https://grasswiki.osgeo.org/wiki/Compile_and_Install)
in the Wiki.

## Docker

For using and building a GRASS docker image, see [docker/README.md](docker/README.md).

## Further documents

- [NumFOCUS Code of Conduct](CODE_OF_CONDUCT.md)
- [Roadmap](https://grass.osgeo.org/about/roadmap/)
- [Governance](https://grass.osgeo.org/about/governance/)

## Thanks to all contributors ❤

[![GRASS contributors](https://contrib.rocks/image?repo=OSGeo/grass "GRASS contributors")](https://github.com/OSGeo/grass/graphs/contributors)
