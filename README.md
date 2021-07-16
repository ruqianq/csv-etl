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
The output data is based on two database in EPA: `TRI_REPORTING_FORM` and `TRI_FACILITY`

Table `TRI_FACILITY` provides facility information and table `TRI_REPORTING_FORM` provides the detailed information per EPA form.

EPA provides many API endpoints for user to query their database, this script query the joined table of `TRI_REPORTING_FORM` and `TRI_FACILITY` using the endpoint below:
https://enviro.epa.gov/enviro/efservice/tri_facility/tri_reporting_form/JSON/rows/0:10

for more information of how to utilize other API please see https://www.epa.gov/enviro/envirofacts-data-service-api

1, The ETL process starts with generating a query string, and user can add column condition to the table they want to query.

2, Pass the query string to a HTTP request and use `requests` package from python to retrieve JSON data.  User can also change the output format to CSV, XML or EXCEL

3, The JSON data would convert to input model. The input model serves as a data structure, so that we can gatekeep our input.  For example if the API change the data format or schema our process break to prevent polluting downstream analysis

4, Convert the input model into the data structure match the desired output. 

5, Once the convert is completed, produce a csv file. 
