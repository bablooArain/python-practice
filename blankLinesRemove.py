with open("hello2.txt","r+") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip():
            f.write(line)
        