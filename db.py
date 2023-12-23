import csv
from utils import get_column_names, get_last_index


def create_table_db(db_name: str, rows: list, delimetr: str = ";") -> bool:
    db_name = db_name + ".csv"
    rows.insert(0, "id")
    rows = delimetr.join(rows) + "\n"
    with open(db_name, "w") as db:
        db.write(rows)
    return True


def read_db(database_file: str) -> list[str]:
    datas: list = []
    key_names: list[str] = get_column_names(database_file)
    with open(database_file, "r") as db:
        reader = csv.reader(db, delimiter=";")
        next(reader)
        for row in reader:
            dict_value = {}
            for i in range(len(key_names)):
                dict_value[key_names[i]] = row[i]
            datas.append(dict_value)
    return datas


def append_data(database_file: str, new_data: dict):
    data_to_database: str = ""
    key_names: list[str] = get_column_names(database_file)
    index = get_last_index(database_file)
    new_data["id"] = index
    for key in key_names:
        data_to_database += str(new_data[key]) + ";"
    data_to_database = data_to_database[:-1] + "\n"
    with open(database_file, "a") as db:
        db.write(data_to_database)
    return True

