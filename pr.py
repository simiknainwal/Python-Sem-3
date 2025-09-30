import re
names=["ria sharma","Sachin tendulkar","123alia","dhoni","Aa d"]
for i in names:
    print(i," ",bool(re.match(r'[a-zA-Z][a-zA-Z][a-zA-Z]+',i)))