import json

data = '{"firstName":"gurkan","lastName":"altunok"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])

customer = {
    "firstName":"gurkan",
    "email":"oguzgurkan2001@gmail.com"
}

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Gurkan"))