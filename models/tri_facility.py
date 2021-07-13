from dataclasses import dataclass


@dataclass
class TriFacility:
    tri_facility_id: str
    facility_name: str
    street_address: str
    city_name: str
    county_name: str
    state_abbr: str
    zip_code: str
    region: int
    fac_closed_ind: int
    mail_name: str
    mail_street_address: str
    mail_city: str
    mail_state_abbr: str
    mail_province: str
    mail_country: str
    mail_zip_code: str
    asgn_federal_ind: str
    asgn_agency: str
    frs_id: str
    parent_co_db_num: str
    parent_co_name: str
    fac_latitude: int
    fac_longtitude: int
    pref_latitude: float
    pref_longtitude: float
    pref_accuracy: int
    pref_collect_meth: str
    pref_desc_category: str
    pref_horizontal_datum: int
    pref_source_scale: str
    pref_qa_code: str
    asgn_partial_ind: int
    asgn_public_contact: str
    asgn_public_phone: int
    asgn_public_contact_email: str
    bia_code: str
    standardized_parent_company: str
    asgn_public_phone_ext: str
    epa_registry_id: str

