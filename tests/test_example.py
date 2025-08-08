from hexlet_pytest.hexlet_pytest.example import reverse # type: ignore
from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse():
    assert reverse("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverse("") == ""


def test_reverse_file():
    begin_string = read_file('string.txt')
    end_string = read_file('result_string.txt')
    result = reverse(begin_string)

    assert result == end_string