# content of conftest.py
import pytest

@pytest.fixture
def device():
    return "npu"

def pytest_configure(config):
    config.addinivalue_line("markers", "interpreter: indicate whether interpreter supports the test")
