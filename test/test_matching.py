import pytest
from src.matching import resident_hospital_matcher


@pytest.mark.parametrize(
    "res_prefs, hos_prefs, hos_cap, want_result",
    [
        (
            {"Alice": ["h1", "h2"], "Bob": ["h1", "h2"], "Charlie": ["h1", "h2"]},
            {"h1": ["Alice", "Charlie", "Bob"], "h2": ["Bob", "Alice", "Charlie"]},
            {"h1": 2, "h2": 1},
            {"h2": ["Bob"], "h1": ["Charlie", "Alice"]},
        )
    ],
)
def test_resident_hospital_matcher(res_prefs, hos_prefs, hos_cap, want_result):
    match = resident_hospital_matcher(res_prefs, hos_prefs, hos_cap)
    assert match == want_result
