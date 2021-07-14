from dataclasses import dataclass


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
