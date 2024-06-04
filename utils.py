import json


def read_src(file):
    json_data = []
    with open(file) as src:
        json_src = json.load(src)
    for i in json_src:
        if "id" in i and i["state"] == "EXECUTED":
            json_data.append(i)
    sort_by_date = sorted(json_data, key=lambda x: x["date"], reverse=True)
    return sort_by_date
