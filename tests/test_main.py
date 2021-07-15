import unittest
from typing import List

from main import parse_json_to_input_model
from models.input import TriReportingFormsPerFacility, TriFacility, TriReportingForm


class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mock_json_response = [
            {
                'TRI_FACILITY_ID': "00602BXTRF111CO",
                'FACILITY_NAME': "BAXTER HEALTHCARE CORP, FENWAL DIV",
                'STREET_ADDRESS': "111 COLON ST",
                'CITY_NAME': "AGUADA",
                'COUNTY_NAME': "AGUADA MUNICIPIO",
                'STATE_ABBR': "PR",
                'ZIP_CODE': "00602",
                'REGION': 2,
                'FAC_CLOSED_IND': 1,
                'PARENT_CO_NAME': "BAXTER SALES CORP",
                'TRI_REPORTING_FORM': [
                    {
                        'DOC_CTRL_NUM': 1389035655796,
                        'ACTIVE_STATUS': 1,
                        'TRI_FACILITY_ID': "00602BXTRF111CO",
                        'TRI_CHEM_ID': "0000075218",
                        'REPORTING_YEAR': 1989,
                        'MAX_AMOUNT_OF_CHEM': "02",
                        'CAS_CHEM_NAME': "Ethylene oxide",
                    },
                    {
                        'DOC_CTRL_NUM': 1388025052414,
                        'ACTIVE_STATUS': 1,
                        'TRI_FACILITY_ID': "00602BXTRF111CO",
                        'TRI_CHEM_ID': "0000075218",
                        'REPORTING_YEAR': 1988,
                        'MAX_AMOUNT_OF_CHEM': "02",
                        'CAS_CHEM_NAME': "Ethylene oxide",
                    }
                ]
            },
            {
                'TRI_FACILITY_ID': "00602BXTRHRD115",
                'FACILITY_NAME': "DADE DIAGNOSTICS OF PR INC",
                'STREET_ADDRESS': "RD 115 KM 226",
                'CITY_NAME': "AGUADA",
                'COUNTY_NAME': "AGUADA MUNICIPIO",
                'STATE_ABBR': "PR",
                'ZIP_CODE': "00602",
                'REGION': 2,
                'FAC_CLOSED_IND': 0,
                'PARENT_CO_NAME': "DADE INTERNATIONAL INC",
                'TRI_REPORTING_FORM': []
            }
        ]

    def test_parse_json_to_input_model(self):
        expected_output: List[TriReportingFormsPerFacility] = [
            TriReportingFormsPerFacility(
                tri_facility=TriFacility(tri_facility_id="00602BXTRF111CO",
                                         facility_name="BAXTER HEALTHCARE CORP, FENWAL DIV",
                                         street_address="111 COLON ST", city_name="AGUADA",
                                         county_name="AGUADA MUNICIPIO", state_abbr="PR", zip_code="00602", region=2,
                                         fac_closed_ind=1, parent_co_name="BAXTER SALES CORP"
                                         ),
                tri_reporting_forms=[
                    TriReportingForm(doc_ctrl_num=1389035655796, active_status=1, tri_facility_id="00602BXTRF111CO",
                                     tri_chem_id="0000075218", report_year=1989, max_amount_of_chem='02',
                                     cas_chem_name="Ethylene oxide"),
                    TriReportingForm(doc_ctrl_num=1388025052414, active_status=1, tri_facility_id="00602BXTRF111CO",
                                     tri_chem_id="0000075218", report_year=1989, max_amount_of_chem='02',
                                     cas_chem_name="Ethylene oxide")
                ]
            ),
            TriReportingFormsPerFacility(tri_facility=TriFacility(tri_facility_id="00602BXTRHRD115",
                                                                  facility_name="DADE DIAGNOSTICS OF PR INC",
                                                                  street_address="RD 115 KM 226", city_name="AGUADA",
                                                                  county_name="AGUADA MUNICIPIO", state_abbr="PR",
                                                                  zip_code="00602", region=2, fac_closed_ind=0,
                                                                  parent_co_name="DADE INTERNATIONAL INC"),
                                         tri_reporting_forms=[])
        ]
        self.assertEqual(expected_output[1].tri_facility.tri_facility_id,
                         parse_json_to_input_model(self.mock_json_response)[1].tri_facility.tri_facility_id)
        self.assertEqual(2, len(parse_json_to_input_model(self.mock_json_response)))
        self.assertEqual([], parse_json_to_input_model(self.mock_json_response)[1].tri_reporting_forms)


if __name__ == '__main__':
    unittest.main()
