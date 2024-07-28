with open("hello2.txt","r+") as f:
    data = f.read()
    if data.replace("aqsa","babloo"):
        print()