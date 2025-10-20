import pytest

from .main import root, sum


@pytest.mark.anyio
async def test_root() -> None:
    assert await root() == {"message": "Hello World"}


@pytest.mark.anyio
async def test_sum() -> None:
    assert await sum(1, 2) == {"result": 3}
