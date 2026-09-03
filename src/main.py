from arrivals import BusArrival
from display import format_board


def main():
    arrivals = [
        BusArrival(
            route="31",
            stop_id="33218",
            destination="NEWARK PENN",
            minutes=4,
        ),
        BusArrival(
            route="94",
            stop_id="19033",
            destination="BLOOMFIELD",
            minutes=9,
        ),
        BusArrival(
            route="1",
            stop_id="19179",
            destination="JOURNAL SQUARE",
            minutes=13,
        ),
    ]

    arrivals.sort(key=lambda bus: bus.minutes)

    print(format_board(arrivals))


if __name__ == "__main__":
    main()
