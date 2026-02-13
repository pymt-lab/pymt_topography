from __future__ import absolute_import

import pathlib
from importlib_resources import files

from bmi_topography import BmiTopography as Topography

Topography.__name__ = "Topography"
Topography.METADATA = pathlib.Path(files(__name__) / "data" / Topography.__name__)

__all__ = [
    "Topography",
]
