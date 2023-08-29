#Importing necessary variables
import requests

#Defining the main function
def countryData(country):

    #Requesting the data from the source
    url="https://restcountries.com/v3.1/all?fields=name,capital,currencies,region,subregion,languages"

    z=requests.get(url)

    #Receiving/interpreting the data 
    data=z.json()

    #Asking the user for their country 
    try:
        index = None

        #Reading in the data
        for x in range(len(data)):
            if data[x]['name']['common'] == country:
                index = x
                break
        #Selecting the name
        name = data[index]["name"]["common"]

        #Selecting the capital
        capital = data[index]["capital"]

        #Organizing the data
        if type(capital) is list:
            capital1 = ""
            for x in capital:
                capital1+=" "+x
            capital = capital1

        #Selecting the currency
        currency = data[index]["currencies"]
        currency1 = ""
        first = False

        #Organizing the data
        for x in currency:
            if first:
                currency1 += ","
            currency1 += " " + x + " ("+currency[x]['symbol']+"): "+ currency[x]['name']
            first = True

        currency = currency1

        #Selecting the region
        region = data[index]["region"]

        #Selecting the sub-region
        subregion = data[index]["subregion"]

        #Determining the common languages used in the country
        lang = data[index]["languages"]

        #Organizing the data
        if type(lang) is dict:
            lang1 = ""
            first = False
            for x in lang:
                if first:
                    lang1 += ", "
                lang1 += lang[x]
                first = True
            lang = lang1

        #Returning the data
        return name, capital, currency, region, subregion, lang

    #In case the user enters an invalid country that doesn't exist
    except:
        print("The country was not spelt correctly, double check your spelling!")

    


