from mongoengine import connect
from mongoengine import EmbeddedDocument, Document, ReferenceField
from mongoengine.fields import BooleanField, DateTimeField,EmbeddedDocumentField, ListField,StringField
import json
connect(host="mongodb+srv://guest:guest@dreamwave.dhurwpi.mongodb.net/module8?retryWrites=true&w=majority")

class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    description = StringField()
    meta = {"allow_inheritance": True}
    

class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors)
    quote = StringField()
    meta = {"allow_inheritance": True}




def quotes_to_base():
    with open("quotes.json") as file:
        data = json.load(file)
        for quote in data:
            quote:dict
            mongo = Quotes(
                tags = quote.get("tags"),
                author = quote.get("author"),
                quote = quote.get("quote")
                ).save()

def author_to_base():
    with open("authors.json") as file:
        data = json.load(file)
        for author in data:
            author:dict
            mongo = Authors(
                fullname = author.get("name"),
                born_date = author.get("born"),
                description = author.get("description")
                ).save()



quotes_to_base()
author_to_base()





















