from pathlib import Path

import pytest


@pytest.fixture
def example_data(): 
    return {"name": "Sobirjon", "age": 19}


@pytest.fixture
def temp_file():
    file = Path("test.txt")
    file.write_text("Hello PDP")
    # return file
    yield file
    file.unlink(missing_ok=True)
