#Importing necessary libraries
import os
from easygoogletranslate import EasyGoogleTranslate

path = path = os.path.dirname(__file__)
def translate(statement, desiredLang):

    #Reading in the languages text file
    languages = open(path+r"/lang.txt", "r")
    line = languages.readline().rstrip("\n").split()
    lang = {}
    while line != []: 
        lang[line[0]] = line[1] 
        line = languages.readline().rstrip("\n").split()

    #Translating the data
    try:
        translator = EasyGoogleTranslate(
            source_language='',
            target_language=lang[desiredLang.lower()],
        )
        result = translator.translate(statement)
        return result

    #If the user enteres an invalid country
    except:

        print("There is no language by that name, ensure that you entered language is correct")

