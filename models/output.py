from dataclasses import dataclass


@dataclass
class ToxicAirPollutionByCompany:
    tri_facility_id: str
    company_name: str
    toxic_air_pollution: int
    street_address: str
    city_name: str
    county_name: str
    state_abbr: str
    zip_code: str
    cas_chem_names: str
