import json

inData = """[
    {
        "id": 1,
        "login": "admin"
    },
    {
        "id": 2,
        "login": "user"
    }
]"""

inData = json.loads(inData)

outData = json.dumps(inData, indent=4)


print(outData)