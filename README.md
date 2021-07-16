# csv-etl

Here is the example script to fetch data from Envirofacts Data Service API.

The script would generate a csv under `out` directory.

## Installation

**Installation via `requirements.txt`**:
```shell
$ git clone https://github.com/ruqianq/csv-etl
$ cd csv-etl
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ python main.py
```
**Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)**:

```shell
$ git clone https://github.com/ruqianq/csv-etl
$ cd csv-etl
$ pipenv shell
$ pipenv update
$ python main.py
```

## How dose this script work?

1. The script starts with generating a query string for api calling. 

In this case, our output data is based on two tables: `TRI_REPORTING_FORM` and `TRI_FACILITY`

* Table `TRI_FACILITY` provides facility information 
* Table `TRI_REPORTING_FORM` provides the detailed information per EPA form.

EPA provides many API endpoints for users to query the database. This script query the joint table of `TRI_REPORTING_FORM` and `TRI_FACILITY` using the endpoint below:
/tri_facility/tri_reporting_form/JSON/rows/0:10

The script also allows user to add column conditions and change the report format to CSV, XML or EXCEL

For more information of how to utilize other API please see https://www.epa.gov/enviro/envirofacts-data-service-api

2. Construct a HTTP request using the query string to and use `requests` package from python to retrieve JSON data. 
   https://enviro.epa.gov/enviro/efservice/tri_facility/tri_reporting_form/JSON/rows/0:10

3. The JSON data would be converted into the input model. The input model serves as a data structure, so that we can gatekeep our input.  
   For example if the API change the data format or schema, our process stop the data ingestion to prevent polluting downstream analysis

4. Convert the input model into output model (the data structure match the desired output). 

5. Once the convert is completed, then produce a csv file. 
