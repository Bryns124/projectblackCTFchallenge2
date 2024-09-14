import re

with open("binaryMessageHTML.txt", "r") as f:
    content = f.read()

line = re.sub('<code class="d-block">|</code>', '\n', content).strip()
line = re.sub(r'(\d)\s', r'\1', line)
line = re.sub(r'(\d{8})', r'0b\1', line)

with open("binaryMessageReformatted.txt", "w") as f:
    f.write(line)