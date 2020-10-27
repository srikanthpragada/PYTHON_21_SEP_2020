import requests


def get_country_names(countries, codes):
    names = []
    for c in codes:
        country = list(filter(lambda d: d['alpha3Code'] == c, countries))[0]
        names.append(country['name'])

    return ",".join(names)


def get_currency_list(currencies):
    cl = []
    for c in currencies:
        cl.append(c['name'] + " - " + c['symbol'])

    return ",".join(cl)

    return ",".join(names)


code = 'BTN'
resp = requests.get(f"https://restcountries.eu/rest/v2/all")
countries = resp.json()

country = list(filter(lambda d: d['alpha3Code'] == code, countries))[0]

print('Name     :', country['name'])
print('Region   :', country['region'])
print('Borders  :', get_country_names(countries, country['borders']))
print('Currency :', get_currency_list(country['currencies']))
