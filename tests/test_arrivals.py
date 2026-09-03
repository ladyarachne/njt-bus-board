"""Tests for bus arrival processing."""
import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src"),
)

from arrivals import BusArrival
from display import format_arrival


def test_format_arrival():
    bus = BusArrival(
        route="31",
        stop_id="33218",
        destination="NEWARK PENN",
        minutes=4,
    )

    result = format_arrival(bus)

    assert "31" in result
    assert "NEWARK PENN" in result
    assert "4 MIN" in result
