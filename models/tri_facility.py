from dataclasses import dataclass


@dataclass
class TriFacility:
    tri_facility_id: str
    facility_name: str
    street_address: str
    city_name: int
    county_name: str
    state_abbr: str
    zip_code: int
    region: int
    fac_closed_ind: int
    parent_co_name: str
    epa_registry_id: str


