import pytest
import yaml
from pathlib import Path

@pytest.fixture(scope="session")
def load_openapi_spec():
    def _loader(path: str) -> dict:
        with open(Path(path), "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    return _loader