from models import Authors, Quotes
import connect

while True:
    a = input(
        "To get quotes by author enter command like 'name:author'\nTo get quotes by tag enter command like 'tag:tag1,"
        "tag2...'\n'exit' for exit. ")
    if a == "exit":
        break
    else:
        k = a.split(":")[0]
        v = a.split(":")[1]
        v_v = v.split(",")
    # if k == "name":
    #     auth=Authors.objects(fullname=v)
    #     quotes = Quotes.objects(author=auth)
    #     for q in quotes:
    #         print(q.to_mongo())
    #     for a in auth:
    #         print(a.to_mongo())
        
    if k == "name":
        auth=Authors.objects(fullname=v).all()
        for author in auth:
            quotes = Quotes.objects(author=author)
            for q in quotes:
                print(v,q.quote)

    if k == "tag":
        quotes = Quotes.objects(tags=v)
        for q in quotes:
            print(q.tags, q.quote)
    if k == "tags":
        quotes = Quotes.objects(tags__in=v_v)
        for q in quotes:
            print(q.tags, q.quote)
