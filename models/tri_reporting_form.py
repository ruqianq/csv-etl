from dataclasses import dataclass


@dataclass
class TriReportingForm:
    doc_ctrl_num: int
    active_status: int
    tri_facility_id: str
    tri_chem_id: str
    report_year: int
    max_amount_of_chem: int
    cas_chem_name: str
