from hexlet_pytest.hexlet_pytest.example import reverse # type: ignore


def test_reverse():
    assert reverse("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverse("") == ""