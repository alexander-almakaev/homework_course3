from utils import get_latest_transactions

if __name__ == "__main__":
    amount = input("Сколько операций хотите посмотреть?: ")
    get_latest_transactions("operations.json", amount)
