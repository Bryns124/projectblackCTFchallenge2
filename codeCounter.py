with open("htmlTextToCountCode.txt", "r") as file:
    file_contents = file.read()
    count = file_contents.count('code')
    print(f"'code' appears {count} times.")