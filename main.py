from models import Authors,Quotes
import connect

while True:
    a=input("To get quotes by author enter command like 'name:author'\nTo get quotes by tag enter commant like 'tag:tag1,tag2...'\n'exit' for exit. ")
    if a=="exit":
        break
    else:
        k=a.split(":")[0]
        v=a.split(":")[1]
        v_v=v.split(",")
    # if k=="name":
    #     authors=Authors.objects(fullname=v)
    #     quotes=Quotes.objects()
    #     for a in authors:
    #         print(a.to_mongo().to_dict())
    #         for q in quotes:
    #             print(q.to_mongo().to_dict())
    #             # if a.id==q.id:
    if k=="tag":
        quotes=Quotes.objects(tags=v)
        for q in quotes:
            print(q.tags,q.quote)
    if k=="tags":
        quotes=Quotes.objects(tags__in=v_v)
        for q in quotes:
            print(q.tags,q.quote)
