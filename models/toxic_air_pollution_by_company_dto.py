from dataclasses import dataclass


@dataclass
class ToxicAirPollutionByCompany:
    id: int
    report_date: str
    company_names: str
    toxic_air_pollution: int
    unit: str
    description: str
