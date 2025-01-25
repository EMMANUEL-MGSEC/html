with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am Penguin and i love coding")
file.close()

with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in ths file are....")
    for line in data:
        word= line.split()
        print (word)
        file.close()