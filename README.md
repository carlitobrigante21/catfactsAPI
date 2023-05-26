
gives random facts about cats


This project is a Python script that interacts with the Cat Facts API to retrieve random cat facts and all available cat facts. It provides functions to access the API, store the data in a JSON file and a SQLite database, and display Windows notifications using the `win10toast` module.

## Requirements

- Python 3.x
- `requests` module
- `json` module
- `sqlite3` module
- `win10toast` module

## Usage

1. Clone the repository to your local machine:


2. Install the required Python packages:


3. Run the `cat_facts.py` script:


4. The script will retrieve a random cat fact, save it to a JSON file named `cat_fact.json`, print the fact, and store it in a SQLite database named `cat_facts.db`.

5. It will then retrieve all available cat facts, save them to a JSON file named `all_cat_facts.json`, print the total number of facts, and display a notification on Windows.


