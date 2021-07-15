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

## Reference
Envirofacts Data Service API: https://www.epa.gov/enviro/envirofacts-data-service-api
