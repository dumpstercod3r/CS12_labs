# pyright: strict

from lab01e import simulate2048

def test_simulate2048():
    assert simulate2048([
            [2, 2, 0],
            [4, 0, 0],
            [0, 0, 0],
        ], "EW") == [
            [1, 4, 1],
            [4, 0, 0],
            [0, 0, 0],
        ]