import requests
def countryData(country):
    url="https://restcountries.com/v3.1/all?fields=name,capital,currencies,region,subregion,languages"

    z=requests.get(url)

    # I used requests module to fetch data from above link.
    data=z.json()

    #Asking the user for their country 
    try:
        index = None
        
        for x in range(len(data)):
            if data[x]['name']['common'] == country:
                index = x
                break
        
        name = data[index]["name"]["common"]

        capital = data[index]["capital"]
        if type(capital) is list:
            capital1 = ""
            for x in capital:
                capital1+=" "+x
            capital = capital1

        currency = data[index]["currencies"]
        currency1 = ""
        first = False
        for x in currency:
            if first:
                currency1 += ","
            currency1 += " " + x + " ("+currency[x]['symbol']+"): "+ currency[x]['name']
            first = True

        currency = currency1
        region = data[index]["region"]

        subregion = data[index]["subregion"]

        lang = data[index]["languages"]
        if type(lang) is dict:
            lang1 = ""
            first = False
            for x in lang:
                if first:
                    lang1 += ", "
                lang1 += lang[x]
                first = True
            lang = lang1

        return name, capital, currency, region, subregion, lang
        
    except:
        print("The country was not spelt correctly, double check your spelling!")

    


