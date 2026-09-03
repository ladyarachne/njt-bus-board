"""Display formatting for the NJ Transit bus board."""
from arrivals import BusArrival


def format_arrival(arrival: BusArrival) -> str:
    """Format a bus arrival for the display."""
    return (
        f"{arrival.route:<4}"
        f"{arrival.destination:<22}"
        f"{arrival.minutes:>3} MIN"
    )


def format_board(arrivals: list[BusArrival]) -> str:
    """Create the complete bus arrival board."""
    header = "NJ TRANSIT • BUS\n" + "=" * 36

    rows = [format_arrival(arrival) for arrival in arrivals]

    return "\n".join([header, *rows])
