import pytest
import json
from utils import read_src, get_latest_transactions
from classes import Operation

def test_read_src():
    data = read_src("test.json")
    with open("test_filtered.json", "r", encoding="utf-8") as sample:
        data_filtered = json.load(sample)
    assert type(data) == list
    assert len(data) == 7
    assert data == data_filtered
    for i in data:
        assert type(i) == dict
        assert i["state"] == "EXECUTED"


@pytest.fixture()
def small_data():
    item_from_src = {'id': 441945886,
                              'state': 'EXECUTED',
                              'date': '2019-08-26T10:50:58.294041',
                              'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                              'description': 'Перевод организации',
                              'from': 'Maestro 1596837868705199',
                              'to': 'Счет 64686473678894779589'}
    return Operation(item_from_src)


def test_init(small_data):
    assert small_data.description == "Перевод организации"
    assert small_data.count == 1
    assert small_data.amount == "31957.58"
    assert small_data.currency == "руб."
    assert small_data.sender == "Maestro 1596 83** **** 5199"
    assert small_data.receiver == "Счет **9589"
    assert small_data.date == "26.08.2019"


def test_get_date(small_data):
    assert small_data.get_date() == "26.08.2019"

def test_num_transform(small_data):
    assert small_data.num_transform("Счет 64686473678894779589") == "Счет **9589"
    assert small_data.num_transform("VISA 7335907743721234") == "VISA 7335 90** **** 1234"
    assert small_data.num_transform("Карта и номер 1111222233334444") == "Карта и номер 1111 22** **** 4444"


@pytest.fixture()
def small_data_without_sender():
    item_from_src = {'id': 587085106,
                     'state': 'EXECUTED',
                     'date': '2018-03-23T10:45:06.972075',
                     'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                     'description': 'Открытие вклада',
                     'to': 'Счет 41421565395219882431'}
    return Operation(item_from_src)


def test_get_sender(small_data_without_sender):
    assert small_data_without_sender.get_sender() == "Источник не определен"


    # some_small_collection = [{'id': 441945886,
    #                           'state': 'EXECUTED',
    #                           'date': '2019-08-26T10:50:58.294041',
    #                           'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
    #                           'description': 'Перевод организации',
    #                           'from': 'Maestro 1596837868705199',
    #                           'to': 'Счет 64686473678894779589'},
    #                          {'id': 214024827,
    #                           'state': 'EXECUTED',
    #                           'date': '2018-12-20T16:43:26.929246',
    #                           'operationAmount': {'amount': '70946.18', 'currency': {'name': 'USD', 'code': 'USD'}},
    #                           'description': 'Перевод организации',
    #                           'from': 'Счет 10848359769870775355',
    #                           'to': 'Счет 21969751544412966366'},
    #                          {'id': 587085106,
    #                           'state': 'EXECUTED',
    #                           'date': '2018-03-23T10:45:06.972075',
    #                           'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
    #                           'description': 'Открытие вклада',
    #                           'to': 'Счет 41421565395219882431'}
    #                          ]
