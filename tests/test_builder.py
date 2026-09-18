import pytest

from noaa.builder import Builder


class TestBuilder:
    @pytest.mark.parametrize(
        "name, input, expected",
        [
            ("Should strip single", " hello", "hello"),
            ("Should join multiple", ["one", "two"], "one,two"),
            ("Should strip and join multiple", ["one ", " two"], "one,two"),
        ],
    )
    def test_format_single_or_multiple(self, name, input, expected):
        assert Builder.format_single_or_multiple(input) == expected, name
