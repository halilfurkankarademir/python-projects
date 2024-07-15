## A simple currency converter using freecurrencyAPI.
## You need to sign up at https://freecurrencyapi.com/ to use this program.
## Once you have signed up, copy the default key from the dashboard and paste it into line 6.

import freecurrencyapi

# Paste your API key here.
client = freecurrencyapi.Client('fca_live_wxzkUN7fyWAoQBl4WJsZrek0yTswmRDzYQPt9CNi')

def currencyConverter():
    while True:
        datas = client.latest()
        available_currencies = list(datas['data'].keys())
        print("\nAvailable currencies:", ", ".join(available_currencies),"\n")
        option = input("Enter the currency you want to convert to (e.g., USD, EUR): ").upper()
        
        if option not in datas['data']:
            print("%s is an invalid currency" % option)
        else:
            base = input("Enter the base currency you want to convert from (e.g., USD, EUR): ").upper()
                
            if base not in datas['data']:
                print("%s is an invalid currency" % base)
            else:
                duplicate = float(input("Enter the amount of %s you want to convert to %s: " % (base, option)))
                results = client.latest(base_currency=base)
                valueCurrency = float(results['data'][option])
                print(duplicate, base, "=", valueCurrency * duplicate, option,"\n")
                    

currencyConverter()
