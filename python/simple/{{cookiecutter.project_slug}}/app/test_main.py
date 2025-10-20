from .main import sum


def test_sum() -> None:
    assert sum(1, 2) == 3
