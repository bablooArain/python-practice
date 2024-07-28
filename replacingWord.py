with open("hello2.txt","r+") as f:
    data = f.read()
    new_data = data.replace("aqsa","babloo")
    print(new_data)
    f.write(new_data)