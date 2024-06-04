import pytest
from utils import read_src
# from classes import Operation

def test_read_src():
    assert read_src("test.json")

# def test_oper_num_transform():
#     assert Operation.num_transform("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


# def test_get_latest_transactions():
#     result = ('08.12.2019 Открытие вклада\n'
#               'Источник не определен -> Счет **5907\n'
#               '41096.24 USD\n\n'
#               '07.12.2019 Перевод организации\n'
#               'Visa Classic 2842 87** **** 9012 -> Счет **3655\n'
#               '48150.39 USD\n\n'
#               '19.11.2019 Перевод организации\n'
#               'Maestro 7810 84** **** 5568 -> Счет **2869\n'
#               '30153.72 руб.')
#     assert get_latest_transactions("src/test.json", "3") == result
