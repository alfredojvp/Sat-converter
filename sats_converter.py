from forex_python.bitcoin import BtcConverter
from ascii_art import title

def decorator(func):
    def wrapper():
        print(title)
        print("\n")
        func()

    return wrapper


@decorator
def BTC_ER():
    BTC = BtcConverter()
    currency = str(input("Introduce el código de la moneda: ")).upper()
    choosed_currency = BTC.get_latest_price(currency)
    print("\n")
    print(f"La tasa de cambio se encuentra en {choosed_currency} {currency} en estos momentos")
    fiat_amount = int(input("¿Que monto deseas convertir?: "))
    calculated_amount = BTC.convert_to_btc(fiat_amount, currency)
    rounded_amount = round(calculated_amount, 8)
    satoshi = f"Equivalen a {str(rounded_amount*100000000)}  Satoshis"
    print("\n")
    print(satoshi)


if __name__ == '__main__':
    BTC_ER()