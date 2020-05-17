import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = result.text

result2 = json.loads(result)

for i in result2:
    print(i['title'])
