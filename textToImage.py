import os
import openai
def getCountryImage(country):
    openai.api_key = os.getenv("VN2p0xu8N0cyi0sd9Kw2T3BlbkFJOSdlxEeedWZT6UtWF3az")
    response = openai.Image.create(
    api_key="*******************",
    prompt="what does "+str(country)+" look like?",
    n=1,
    size="1024x1024"
    )

    return response['data'][0]['url']


