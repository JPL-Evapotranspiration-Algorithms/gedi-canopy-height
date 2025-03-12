# `gedi-canopy-height` Python Package

[![CI](https://github.com/JPL-Evapotranspiration-Algorithms/gedi-canopy-height/actions/workflows/ci.yml/badge.svg)](https://github.com/JPL-Evapotranspiration-Algorithms/gedi-canopy-height/actions/workflows/ci.yml)

The `gedi-canopy-height` Python package generates rasters of the [Global Forest Canopy Height 2019](https://glad.umd.edu/dataset/gedi/) dataset derived from Global Ecosystem Dynamics Investigation (GEDI).

[Gregory H. Halverson](https://github.com/gregory-halverson-jpl) (they/them)<br>
[gregory.h.halverson@jpl.nasa.gov](mailto:gregory.h.halverson@jpl.nasa.gov)<br>
NASA Jet Propulsion Laboratory 329G

## Prerequisites

This packages uses the `wget` command line tool and the `gdal` command line tools.

On macOS, these can be installed with Homebrew:

```
brew install wget
```

```
brew install gdal
```

These tools can also be installed with `mamba`:

```
mamba install wget
```

```
mamba install gdal
```

## Installation

This package is available on PyPi as a [pip package](https://pypi.org/project/gedi-canopy-height/) called `gedi-canopy-height` with dashes.

```bash
pip install gedi-canopy-height
```

## Usage

Import this package as `gedi_canopy_height` with under-scores.

```python
import gedi_canopy_height
```

## References

P. Potapov, X. Li, A. Hernandez-Serna, A. Tyukavina, M.C. Hansen, A. Kommareddy, A. Pickens, S. Turubanova, H. Tang, C.E. Silva, J. Armston, R. Dubayah, J. B. Blair, M. Hofton (2020) Mapping and monitoring global forest canopy height through integration of GEDI and Landsat data. Remote Sensing of Environment, 112165[^1^][5].

