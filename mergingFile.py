with open("hello2.txt","r") as file:
    with open("hello.py","r") as file2:
        data = file.read()
        data2 = file2.read()
    with open("newFile.txt","w") as file3:
        file3.write(data + data2)
