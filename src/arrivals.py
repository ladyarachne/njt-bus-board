from dataclasses import dataclass


@dataclass
class BusArrival:
    route: str
    stop_id: str
    destination: str
    minutes: int
