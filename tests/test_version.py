"""Unit tests for the version number."""

import importlib
import re

import sips


def test_version_attribute():
    """Test the attribute `sips.__version__`."""

    assert hasattr(sips, "__version__")

    version = sips.__version__
    assert isinstance(version, str)
    assert re.match(r"\d*\.\d*\.\d*", version).group() == version
    assert importlib.metadata.version("sips") == version
