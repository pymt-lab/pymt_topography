#! /usr/bin/env python
from importlib.metadata import version

__version__ = version("pymt_topography")


from .bmi import Topography

__all__ = [
    "Topography",
]
