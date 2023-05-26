import requests
import json
import sqlite3
from win10toast import ToastNotifier



def get_cat_fact():
    url = "https://cat-fact.herokuapp.com/facts/random"
    response = requests.get(url)
    return response.json()

def get_status_code(response):
    return response.status_code

def get_headers(response):
    return response.headers

def get_all_facts():
    url = "https://cat-fact.herokuapp.com/facts"
    response = requests.get(url)
    return response.json()



def save_json_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)



def print_interesting_info(data):
    print("Cat Fact:")
    print(data["text"])



def create_table():
    conn = sqlite3.connect("cat_facts.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS cat_facts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fact TEXT,
            length INTEGER
        )
    """)
    conn.commit()
    conn.close()

def store_data_in_db(data):
    conn = sqlite3.connect("cat_facts.db")
    c = conn.cursor()
    c.execute("INSERT INTO cat_facts (fact, length) VALUES (?, ?)", (data["text"], len(data["text"])))
    conn.commit()
    conn.close()



def display_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)



def main():

    cat_fact = get_cat_fact()
    save_json_file(cat_fact, "cat_fact.json")
    print_interesting_info(cat_fact)
    store_data_in_db(cat_fact)


    all_facts = get_all_facts()
    save_json_file(all_facts, "all_cat_facts.json")
    print(f"Total Cat Facts: {len(all_facts)}")


    display_notification("Cat Facts API", "Data retrieval complete!")

if __name__ == "__main__":
    create_table()
    main()
