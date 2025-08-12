# content of conftest.py
import pytest

@pytest.fixture
def device():
    return "npu"
