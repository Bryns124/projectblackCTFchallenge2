with open("binaryMessageReformatted.txt", "r") as f:
    lines = f.readlines()
    message = []
    for line in lines:
        line = line.strip()
        message.append(chr(int(line, 2)))
    
message = ''.join(message)
print(message)