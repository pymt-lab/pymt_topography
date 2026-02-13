from __future__ import absolute_import

import pathlib

from bmi_topography import BmiTopography as Topography
from importlib_resources import files

Topography.__name__ = "Topography"
Topography.METADATA = pathlib.Path(files(__name__) / "data" / Topography.__name__)

__all__ = [
    "Topography",
]
