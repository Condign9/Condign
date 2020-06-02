import requests
import json

website = requests.get("https://api.exchangeratesapi.io/latest")
website = json.loads(website.text)
rates = website["rates"]
rates.update({"EUR": 1})


def key1_check():
    import re
    rates = website["rates"]
    rates.update({"EUR": 1})
    rates = json.dumps(rates)
    if not re.search(yourCurrency, rates):
        raise Exception(
            "This is not a currency")
    else:
        rates = json.loads(rates)


def key2_check():
    import re
    rates = website["rates"]
    rates.update({"EUR": 1})
    rates = json.dumps(rates)
    if not re.search(exchangeCurrency, rates):
        raise Exception(
            "This is not a currency")
    else:
        rates = json.loads(rates)


while True:
    try:
        yourCurrency = input("Which currency do you have?: ").upper()
        key1_check()
    except Exception as error:
        print(error)
    else:
        break

while True:
    try:
        yourMoney = float(input("How much money do you have?: "))
    except:
        print("This is not a float!")
    else:
        break


while True:
    try:
        exchangeCurrency = input(
            "Which currency would you like to buy?: ").upper()
        key2_check()
    except Exception as error:
        print(error)
    else:
        break


newMoney = (float(rates[exchangeCurrency]) /
            float(rates[yourCurrency]))*float(yourMoney)

print(f"You have: {newMoney} {exchangeCurrency}")
