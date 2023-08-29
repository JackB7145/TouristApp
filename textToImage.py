#Importing neccesary libraries
import os
import openai

#Initializing the api key
key = "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"

#Initializing the main function
def getCountryImage(country):

    #evaluating the key
    openai.api_key = os.getenv(key)

    #Sending the data to the open ai model
    response = openai.Image.create(
    api_key=key,
    prompt="what does "+str(country)+" look like?",
    n=1,
    size="1024x1024"
    )

    #Sending the response
    return response['data'][0]['url']

