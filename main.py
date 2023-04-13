from typing import Any, Literal, Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseEvent(BaseModel):
    type: Literal[
        "hourly_report",
        "shutdown",
        "extended_power_outage",
        "frequent_power_outage",
        "extended_inactivity",
    ]
    id: Optional[str]  # TODO: Make this required
    car_id: str


# V3 and V4 hardware events
class HourlyReport(BaseEvent):
    type: Literal["hourly_report"]
    doors: int
    trips: int
    report_dt: str
    max_speed: Optional[float]
    max_trip_duration: Optional[float]
    min_trip_duration: Optional[float]


class Shutdown(BaseEvent):
    type: Literal["shutdown"]
    started_at: str
    ended_at: Optional[str]
    shutdown_category: Union[Literal["standalone"], Literal["bank"]]
    detected_at: str


class ExtendedInactivity(BaseEvent):
    type: Literal["extended_inactivity"]
    started_at: str
    ended_at: Optional[str]


# V3 specific hardware events
class ExtendedPowerOutage(BaseEvent):
    type: Literal["extended_power_outage"]
    started_at: str
    ended_at: str


class FrequentPowerOutage(BaseEvent):
    type: Literal["frequent_power_outage"]
    started_at: str
    ended_at: Optional[str]
    outages_last_30: Optional[int]


LiftAIEvent = Union[
    HourlyReport, Shutdown, ExtendedPowerOutage, FrequentPowerOutage, ExtendedInactivity
]


@app.post("/")
async def root(data: LiftAIEvent):
    # Print the data or do whatever you want with it
    print(data)

    # Return a 200 OK response
    return {}
