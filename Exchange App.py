import requests
import json
import re

website = requests.get("https://api.exchangeratesapi.io/latest")
website = json.loads(website.text)
rates = website["rates"]
rates.update({"EUR": 1})


def key_check(currency):
    rates = website["rates"]
    rates.update({"EUR": 1})
    rates = json.dumps(rates)
    if not re.search(currency, rates):
        raise Exception(
            "This is not a currency")
    else:
        rates = json.loads(rates)


while True:
    print(rates)
    try:
        yourCurrency = input("Which currency do you have?: ").upper()
        key_check(yourCurrency)
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
    print(rates)
    try:
        exchangeCurrency = input(
            "Which currency would you like to buy?: ").upper()
        key_check(exchangeCurrency)
    except Exception as error:
        print(error)
    else:
        break


newMoney = (float(rates[exchangeCurrency]) /
            float(rates[yourCurrency]))*float(yourMoney)

print("You have:", "%.2f" % newMoney, exchangeCurrency)
