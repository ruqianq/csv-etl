from typing import List

from models.input import TriReportingFormsPerFacility, TriFacility, TriReportingForm
from models.output import ToxicAirPollutionByCompany


def parse_json_to_input_model(json_response) -> List[TriReportingFormsPerFacility]:
    tri_reporting_forms_per_facility_list = []
    for i in json_response:
        tri_facility: TriFacility = TriFacility(tri_facility_id=i['TRI_FACILITY_ID'],
                                                facility_name=i['FACILITY_NAME'], street_address=i['STREET_ADDRESS'],
                                                city_name=i['CITY_NAME'], county_name=i['COUNTY_NAME'],
                                                state_abbr=i['STATE_ABBR'], zip_code=i['ZIP_CODE'],
                                                region=i['REGION'], fac_closed_ind=i['FAC_CLOSED_IND'],
                                                parent_co_name=i['PARENT_CO_NAME'])
        tri_reporting_forms = []
        if len(i['TRI_REPORTING_FORM']) > 0:
            for j in i['TRI_REPORTING_FORM']:
                tri_reporting_form: TriReportingForm = TriReportingForm(doc_ctrl_num=j['DOC_CTRL_NUM'],
                                                                        active_status=j['ACTIVE_STATUS'],
                                                                        tri_facility_id=j['TRI_FACILITY_ID'],
                                                                        tri_chem_id=j['TRI_CHEM_ID'],
                                                                        report_year=j['REPORTING_YEAR'],
                                                                        max_amount_of_chem=j['MAX_AMOUNT_OF_CHEM'],
                                                                        cas_chem_name=j['CAS_CHEM_NAME'])
                tri_reporting_forms.append(tri_reporting_form)
        tri_reporting_forms_per_facility_list.append(TriReportingFormsPerFacility(tri_facility=tri_facility,
                                                                                  tri_reporting_forms=tri_reporting_forms))
    return tri_reporting_forms_per_facility_list


def transform_input_to_output_model(
        tri_reporting_forms_per_facility_list: List[TriReportingFormsPerFacility]) -> List[ToxicAirPollutionByCompany]:
    toxic_air_pollution_by_company_list = []

    for i in tri_reporting_forms_per_facility_list:
        cas_chem_names = []
        toxic_air_pollution = 0

        if len(i.tri_reporting_forms) > 0:

            for j in i.tri_reporting_forms:
                toxic_air_pollution += int(j.max_amount_of_chem)

                if j.cas_chem_name not in cas_chem_names:
                    cas_chem_names.append(j.cas_chem_name)

        toxic_air_pollution_by_company: ToxicAirPollutionByCompany = ToxicAirPollutionByCompany(
            tri_facility_id=i.tri_facility.tri_facility_id, company_names=i.tri_facility.parent_co_name,
            street_address=i.tri_facility.street_address, city_name=i.tri_facility.city_name,
            county_name=i.tri_facility.county_name, state_abbr=i.tri_facility.state_abbr,
            zip_code=i.tri_facility.zip_code, cas_chem_names=cas_chem_names, toxic_air_pollution=toxic_air_pollution)
        toxic_air_pollution_by_company_list.append(toxic_air_pollution_by_company)

    return toxic_air_pollution_by_company_list
