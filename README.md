
## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

API_KEY="_________"
```
## Setup

Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage



Run an example script:

```sh
#python app/my_script.py
```

Run stock report 

```sh
#python app/stocks.py
python -m app.stocks
```

Run an unemployment report from CSV:

```sh
#python app/unemployment_csv.py
```
Run an unemployment report from JSON:

```sh
#python app/unemployment_json.py
```
### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
