import re

with open('address.txt', 'rt', encoding='utf-8') as f:
    text = f.read()
    a = re.findall(r'\d{3}-\d{4}',text)
    print(a)