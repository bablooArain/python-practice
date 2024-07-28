# with open("hello2.txt","r") as f:
#     data = f.read()
#     if data.find("aqsa") != -1:
#         print("Found")
#     else:
#         print("Not Found!")

# Searching for a word in a file
search_word = 'aqsa'
with open('hello2.txt', 'r') as f:
    for line in f:
        if search_word in line:
            print(line.strip())
