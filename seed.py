from models import Authors, Quotes
import connect
import json

with open("authors.json","rb") as f:
    data_authors=json.load(f)
for i in data_authors:
    authors = Authors.from_json(json.dumps(i))
    authors.save()

with open("quotes.json","rb") as f:
    data_quotes=json.load(f)
for i in data_quotes:
    quotes=Quotes.from_json(json.dumps(i))
    quotes.save()