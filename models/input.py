from dataclasses import dataclass
from typing import List


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
    # mail_name: str
    # mail_street_address: str
    # mail_city: str
    # mail_state_abbr: str
    # mail_province: str
    # mail_country: str
    # mail_zip_code: str
    # asgn_federal_ind: str
    # asgn_agency: str
    # frs_id: str
    # parent_co_db_num: str
    parent_co_name: str
    # fac_latitude: int
    # fac_longtitude: int
    # pref_latitude: float
    # pref_longtitude: float
    # pref_accuracy: int
    # pref_collect_meth: str
    # pref_desc_category: str
    # pref_horizontal_datum: int
    # pref_source_scale: str
    # pref_qa_code: str
    # asgn_partial_ind: int
    # asgn_public_contact: str
    # asgn_public_phone: int
    # asgn_public_contact_email: str
    # bia_code: str
    # standardized_parent_company: str
    # asgn_public_phone_ext: str
    # epa_registry_id: str


@dataclass
class TriReportingForm:
    doc_ctrl_num: int
    active_status: int
    tri_facility_id: str
    tri_chem_id: str
    # form_type_ind: str
    report_year: int
    # certif_name: str
    # certif_official_title: str
    # partial_fac: int
    # entire_fac: int
    max_amount_of_chem: str
    # certif_signature: str
    # certif_date_signed: str
    # postmark_date: str
    # public_contact_person: str
    # public_contact_phone: int
    # additional_data_ind: int
    # one_time_release_qty: int
    # one_time_release_qty_na: int
    # production_ratio: float
    # production_ratio_na: int
    # mixture_name: str
    # received_date: str
    # revision_na: int
    # orig_postmark: str
    # orig_received: str
    # federal_fac_ind: int
    # goco_flag: str
    # generic_chem_name: str
    cas_chem_name: str
    # trade_secret_ind: int
    # sanitized_ind: int
    # dioxin_distribution_na: int
    # dioxin_distribution_1: int
    # dioxin_distribution_2: int
    # dioxin_distribution_3: int
    # dioxin_distribution_4: int
    # dioxin_distribution_5: int
    # dioxin_distribution_6: int
    # dioxin_distribution_7: int
    # dioxin_distribution_8: int
    # dioxin_distribution_9: int
    # dioxin_distribution_10: int
    # dioxin_distribution_11: int
    # dioxin_distribution_12: int
    # dioxin_distribution_13: int
    # dioxin_distribution_14: int
    # dioxin_distribution_15: int
    # dioxin_distribution_16: int
    # dioxin_distribution_17: int
    # public_contact_email: str
    # revision_code_1: str
    # revision_code_2: str
    # media_type: str
    # public_contact_phone_ext: int
    # production_ratio_or_activity: str
    # elemental_metal_included: str
    # waste_rock_managed_pile: str
    # waste_rock_quantity: int
    # trimeweb_form_preparation_type: str


@dataclass
class TriReportingFormsPerFacility:
    tri_facility: TriFacility
    tri_reporting_forms: List[TriReportingForm]
