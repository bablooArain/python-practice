with open("hello2.txt","r") as f:
    with open("hello.py","w") as new:
        for lines in f:
            new.write(lines)