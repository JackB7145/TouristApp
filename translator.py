#Can translate over 138 languages
from easygoogletranslate import EasyGoogleTranslate

def translate(statement, desiredLang):

    #Reading in the languages text file
    languages = open("lang.txt", "r")
    line = languages.readline().rstrip("\n").split()
    lang = {}
    while line != []: 
        lang[line[0]] = line[1] 
        line = languages.readline().rstrip("\n").split()

    try:
        translator = EasyGoogleTranslate(
            source_language='',
            target_language=lang[desiredLang.lower()],
        )
        result = translator.translate(statement)
        return result

    except:

        print("There is no language by that name, ensure that you entered language is correct")


        

