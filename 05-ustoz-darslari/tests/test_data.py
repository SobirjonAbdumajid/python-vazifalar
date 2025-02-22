def test_data(example_data):
    assert example_data["name"] == "Sobirjon"
    assert example_data["age"] == 19


def test_read_file(temp_file):
    assert temp_file.read_text() == "Hello PDP"
