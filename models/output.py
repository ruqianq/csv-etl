from dataclasses import dataclass
from typing import List


@dataclass
class FacilityLocation:
    name: str
    state: str
    address: str
    zipcode: str
    country: str
    purpose: str


@dataclass
class ToxicAirPollutionByCompany:
    id: str
    report_date: str
    company_names: str
    toxic_air_pollution: int
    facility_locations: List[FacilityLocation]
    chemicals_released: List[str]
