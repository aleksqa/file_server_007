from src import utils


def test_uniqueness(mocker):
    generated_strings = []
    for _ in range(100):
        value = utils.random_string()
        assert value not in generated_strings
        generated_strings.append(value)
