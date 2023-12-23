import csv

def get_last_index(database_file: str) -> int:
    last = [0]
    with open(database_file, "r") as db:
        reader = csv.reader(db, delimiter=";")
        next(reader)
        for value in reader:
            last = value
    return int(last[0])+1

def get_column_names(database_file: str):
    with open(database_file, "r") as db:
        reader = csv.reader(db, delimiter=";")
        data: str = next(reader)
    return data
