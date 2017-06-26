import requests
response = requests.get(
    "https://www.studential.com/personal-statement-examples/accounting-and-finance-personal-statement"
    )
txt = response.text
print(txt)
