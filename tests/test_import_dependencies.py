import pytest

# List of dependencies
dependencies = [
    "matplotlib",
    "numpy",
    "rasters"
]

# Generate individual test functions for each dependency
@pytest.mark.parametrize("dependency", dependencies)
def test_dependency_import(dependency):
    __import__(dependency)
