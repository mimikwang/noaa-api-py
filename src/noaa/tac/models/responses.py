from pydantic import Field

from .base import Base


class WaterLevel(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(
        ..., alias="v", description="Value - Measured water level height"
    )
    signma: str = Field(
        ...,
        alias="s",
        description="Sigma - Standard deviation of 1 second samples used to compute the water level height",
    )
    flags: str = Field(..., alias="f", description="Data Flags")
    quality: str = Field(
        ...,
        alias="q",
        description="Quality Assurance / Quality Control level - p for preliminary and v for verified",
    )


class HourlyHeight(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(
        ..., alias="v", description="Value - Measured water level height"
    )
    sigma: str = Field(
        ...,
        alias="s",
        description="Sigma - Standard deviation of 1 second samples used to compute the water level height",
    )
    flags: str = Field(..., alias="f", description="Data Flags")


class HighLow(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(
        ..., alias="v", description="Value - Measured water level height"
    )
    type_: str = Field(
        ..., alias="ty", description="Type - Designation of Water level height"
    )
    flags: str = Field(..., alias="f", description="Data Flags")


class DailyMean(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(
        ..., alias="v", description="Value - Mean hourly data over a 24 hour period"
    )
    flags: str = Field(..., alias="f", description="Data Flags")


class DailyMaxMin(Base):
    daily_max_hourly: str = Field(
        ...,
        alias="dailyMaxHourly",
        description="Daily maximum water level from the hourly water level data",
    )
    daily_min_hourly: str = Field(
        ...,
        alias="dailyMinHourly",
        description="Daily minimum water level from the hourly water level data",
    )
    daily_max_six_minute: str = Field(
        ...,
        alias="dailyMax6Min",
        description="Daily maximum water level from the 6-minute water level data",
    )
    daily_min_six_minute: str = Field(
        ...,
        alias="dailyMin6Min",
        description="Daily minimum water level from the 6-minute water level data",
    )
    date_six_minute: str = Field(
        ...,
        alias="date6Min",
        description="Time - Date of the six minute observation",
    )
    time_six_minute: str = Field(
        ...,
        alias="time6Min",
        description="Time - Time of the six minute observation",
    )
    value_six_minute: str = Field(
        ...,
        alias="value6Min",
        description="Value - Measured six minute water level height",
    )
    percent_complete_six_minute: str = Field(
        ...,
        alias="pcComplete6Min",
        description="Percent Completeness - Percentage of the six minute water level data in a day",
    )
    flag_six_minute: str = Field(
        ...,
        alias="flag6Min",
        description="Data Flags - A flag that when set to 1 indicates that the six minute water level value has been inferred",
    )
    date_hourly: str = Field(
        ..., alias="dateHourly", description="Time - Date of the hourly observation"
    )
    time_hourly: str = Field(
        ..., alias="timeHourly", description="Time - Time of the hourly observation"
    )
    value_hourly: str = Field(
        ...,
        alias="valueHourly",
        description="Value - Measured hourly water level height",
    )
    percent_complete_hourly: str = Field(
        ...,
        alias="pcCompleteHourly",
        description="Percent Completeness - Percentage of the hourly water level data in a day",
    )
    flag_hourly: str = Field(
        ...,
        alias="flagHourly",
        description="Data Flags - A flag that when set to 1 indicates that the hourly water level value has been inferred",
    )
    max_min_type: str = Field(
        ...,
        alias="max_min_type",
        description="Type - Designation of Water level height. max = observed daily maximum water level, min = observed daily minimum water level",
    )


class MonthlyMean(Base):
    year: str = Field(..., alias="year", description="Year")
    month: str = Field(..., alias="month", description="Month")
    highest: str = Field(..., alias="highest", description="Highest Tide")
    mhhw: str = Field(..., alias="MHHW", description="Mean Higher-High Water")
    mhw: str = Field(..., alias="MHW", description="Mean High Water")
    msl: str = Field(..., alias="MSL", description="Mean Sea Level")
    mtl: str = Field(..., alias="MTL", description="Mean Tide Level")
    mlw: str = Field(..., alias="MLW", description="Mean Low Water")
    mllw: str = Field(..., alias="MLLW", description="Mean Lower-Low Water")
    dtl: str = Field(..., alias="DTL", description="Mean Diurnal Tide Level")
    gt: str = Field(..., alias="GT", description="Great Diurnal Range")
    mn: str = Field(..., alias="MN", description="Mean Range of Tide")
    dhq: str = Field(..., alias="DHQ", description="Mean Diurnal High Water Inequality")
    dlq: str = Field(..., alias="DLQ", description="Mean Diurnal Low Water Inequality")
    hwi: str = Field(
        ..., alias="HWI", description="Greenwich High Water Interval (in Hours)"
    )
    lwi: str = Field(
        ..., alias="LWI", description="Greenwich Low Water Interval (in Hours)"
    )
    lowest: str = Field(..., alias="lowest", description="Lowest Tide")
    inferred: str = Field(
        ...,
        alias="inferred",
        description="A flag that when set to 1 indicates that the water level value has been inferred",
    )


class OneMinuteWaterLevel(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(
        ..., alias="v", description="Value - Measured water level height"
    )


class TidePredictions(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(
        ..., alias="v", description="Value - Predicted water level height"
    )


class AirGap(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(..., alias="v", description="Value - Measured air gap")
    sigma: str = Field(
        ...,
        alias="s",
        description="Sigma - Standard deviation of 1 second samples used to compute the air gap",
    )
    flags: str = Field(..., alias="f", description="Data Flags")


class Wind(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    speed: str = Field(..., alias="s", description="Speed - Measured wind speed")
    direction: str = Field(
        ..., alias="d", description="Direction - Wind direction in degrees"
    )
    direction_text: str = Field(
        ..., alias="dr", description="Direction - Wind direction in text"
    )
    gust: str = Field(..., alias="g", description="Gust - Measured wind gust speed")
    flags: str = Field(..., alias="f", description="Data Flags")


class AirPressure(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(..., alias="v", description="Value - Measured air pressure")
    flags: str = Field(..., alias="f", description="Data Flags")


class AirTemperature(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(..., alias="v", description="Value - Measured air temperature")
    flags: str = Field(..., alias="f", description="Data Flags")


class Visibility(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(..., alias="v", description="Value - Measured visibility")
    flags: str = Field(..., alias="f", description="Data Flags")


class Humidity(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(..., alias="v", description="Value - Measured humidity")
    flags: str = Field(..., alias="f", description="Data Flags")


class WaterTemperature(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(..., alias="v", description="Value - Measured water temperature")
    flags: str = Field(..., alias="f", description="Data Flags")


class Conductivity(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    value: str = Field(..., alias="v", description="Value - Measured conductivity")
    flags: str = Field(..., alias="f", description="Data Flags")


class Salinity(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    salinity: str = Field(..., alias="s", description="Salinity")
    specific_gravity: str = Field(..., alias="g", description="Specific Gravity")


class Currents(Base):
    time: str = Field(
        ..., alias="t", description="Time - Date and time of the observation"
    )
    speed: str = Field(..., alias="s", description="Speed - Measured current speed")
    direction: str = Field(
        ..., alias="d", description="Direction - Current direction in degrees"
    )
    bin: str = Field(..., alias="b", description="Bin number")
    echo_1: str = Field(
        ..., alias="echo1", description="Echo Intensity Beam 1 (Counts)"
    )
    echo_2: str = Field(
        ..., alias="echo2", description="Echo Intensity Beam 2 (Counts)"
    )
    echo_3: str = Field(
        ..., alias="echo3", description="Echo Intensity Beam 3 (Counts)"
    )
    echo_4: str = Field(
        ..., alias="echo4", description="Echo Intensity Beam 4 (Counts)"
    )
    corr_1: str = Field(
        ..., alias="corr1", description="Correlation Magnitude Beam 1 (Counts)"
    )
    corr_2: str = Field(
        ..., alias="corr2", description="Correlation Magnitude Beam 2 (Counts)"
    )
    corr_3: str = Field(
        ..., alias="corr3", description="Correlation Magnitude Beam 3 (Counts)"
    )
    corr_4: str = Field(
        ..., alias="corr4", description="Correlation Magnitude Beam 4 (Counts)"
    )


class CurrentsPrediction(Base):
    time: str = Field(
        ...,
        alias="Time",
        description="Time - Date and time of the current prediction",
    )
    velocity_major: str = Field(
        ..., alias="Velocity_Major", description="Velocity along major axis"
    )
    mean_ebb_direction: str = Field(
        ..., alias="meanEbbDir", description="Ebb direction in degrees"
    )
    mean_flood_direction: str = Field(
        ..., alias="meanFloodDir", description="Flood direction in degrees"
    )
    bin: str = Field(..., alias="Bin", description="Bin number")
    depth: str = Field(..., alias="Depth", description="Bin depth")
    speed: str = Field(
        ..., alias="Speed", description="Speed - Predicted current speed"
    )
    direction: str = Field(
        ..., alias="Direction", description="Direction - Current direction in degrees"
    )


class CurrentsHeader(Base):
    time: str = Field(
        ...,
        alias="Time",
        description="Time - Date and time of the observation (GMT only)",
    )
    heading: str = Field(
        ...,
        alias="h",
        description="Heading of the current meter relative to a reference direction, usually true or magnetic north",
    )
    pitch: str = Field(..., alias="p", description="Pitch in degrees")
    roll: str = Field(..., alias="r", description="Roll in degrees")
    temperature: str = Field(
        ..., alias="t", description="Temperature in degrees Celsius"
    )
    pressure: str = Field(..., alias="pr", description="Pressure in decibars")
    depth: str = Field(..., alias="d", description="Depth in meters")
    voltage: str = Field(
        ..., alias="v", description="Battery voltage measured in volts"
    )
