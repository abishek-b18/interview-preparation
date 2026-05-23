import re


def extract_features(text):

    words=len(text.split())


    technical_words=[
        "python",
        "java",
        "sql",
        "ai",
        "ml",
        "flask",
        "html",
        "css"
    ]


    count=0


    for word in technical_words:

        if word in text.lower():

            count+=1


    return [

        words,

        count

    ]