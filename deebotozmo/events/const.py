"""Event constants."""
from typing import List, Mapping, Type

from ..commands import (
    Command,
    GetBattery,
    GetCachedMapInfo,
    GetChargeState,
    GetCleanInfo,
    GetCleanLogs,
    GetError,
    GetFanSpeed,
    GetLifeSpan,
    GetMajorMap,
    GetMapTrace,
    GetPos,
    GetStats,
    GetWaterInfo,
)
from ..commands.stats import GetTotalStats
from . import (
    BatteryEventDto,
    CleanLogEventDto,
    CustomCommandEventDto,
    ErrorEventDto,
    EventDto,
    FanSpeedEventDto,
    LifeSpanEventDto,
    MapEventDto,
    RoomsEventDto,
    StatsEventDto,
    StatusEventDto,
    TotalStatsEventDto,
    WaterInfoEventDto,
)

EVENT_DTO_REFRESH_COMMANDS: Mapping[Type[EventDto], List[Command]] = {
    BatteryEventDto: [GetBattery()],
    CleanLogEventDto: [GetCleanLogs()],
    CustomCommandEventDto: [],
    ErrorEventDto: [GetError()],
    FanSpeedEventDto: [GetFanSpeed()],
    LifeSpanEventDto: [GetLifeSpan()],
    MapEventDto: [GetMapTrace(), GetPos(), GetMajorMap()],
    RoomsEventDto: [GetCachedMapInfo()],
    StatsEventDto: [GetStats()],
    StatusEventDto: [GetChargeState(), GetCleanInfo()],
    TotalStatsEventDto: [GetTotalStats()],
    WaterInfoEventDto: [GetWaterInfo()],
}