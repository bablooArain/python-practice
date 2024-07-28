with open("hello2.txt","r") as f:
    count =  sum(1 for lines in f)
print(f"lines are{count}")