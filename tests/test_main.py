import csv
import unittest
from typing import List

from main import parse_json_to_input_model, transform_input_to_output_model, convert_output_model_to_csv
from models.input import TriReportingFormsPerFacility, TriFacility, TriReportingForm
from models.output import ToxicAirPollutionByCompany


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

    # def test_fetch_epa_tri_facility_count(self):
    #     test_query = construct_query_str([self.query_condition_with_condition], rows='10:11')
    #     response = fetch_epa_tri_table(test_query)
    #     self.assertEqual(response.status_code, 200)

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

    def test_transform_input_to_output_model(self):
        expected_output: List[ToxicAirPollutionByCompany] = [
            ToxicAirPollutionByCompany(tri_facility_id="00602BXTRF111CO", company_name="BAXTER SALES CORP",
                                       toxic_air_pollution=4, street_address="111 COLON ST", city_name="AGUADA",
                                       county_name="AGUADA MUNICIPIO", state_abbr="PR", zip_code="00602",
                                       cas_chem_names='Ethylene oxide')
        ]
        test_input_model = parse_json_to_input_model(self.mock_json_response)
        self.assertEqual(expected_output[0].toxic_air_pollution,
                         transform_input_to_output_model(test_input_model)[0].toxic_air_pollution)
        self.assertEqual(expected_output[0].cas_chem_names,
                         transform_input_to_output_model(test_input_model)[0].cas_chem_names)

    def test_convert_output_model_to_csv(self):
        test_input_model = parse_json_to_input_model(self.mock_json_response)
        test_output_model = transform_input_to_output_model(test_input_model)[0]

        convert_output_model_to_csv([test_output_model], output_dir='mock_data', output_csv_name='test_output.csv')
        with open('mock_data/test_output.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                self.assertEqual(9, len(row))
                self.assertEqual(
                    ['BAXTER SALES CORP', '00602BXTRF111CO', '4', '111 COLON ST', 'AGUADA', 'AGUADA MUNICIPIO',
                     'PR', '00602', 'Ethylene oxide'], row)


if __name__ == '__main__':
    unittest.main()
