import json
from classes import Operation

def read_src(file):
    """
    Функция чтения файла с исходными данными, их фильтрации и сортировки
    """
    json_data = []
    with open(file) as src:
        json_src = json.load(src)
    for i in json_src:
        if "id" in i and i["state"] == "EXECUTED":
            json_data.append(i)
    sort_by_date = sorted(json_data, key=lambda x: x["date"], reverse=True)
    return sort_by_date


def get_latest_transactions():
    """
    Функция создания экземпляров класса транзакций и вывода их на экран
    """
    filtered_list = read_src("operations.json")
    for item in filtered_list:
        operation = Operation(item)
        if operation.count <= 5:
            print(f'{operation.date} {operation.description}\n'
                  f'{operation.sender} -> {operation.receiver}\n'
                  f'{operation.amount} {operation.currency}\n')
