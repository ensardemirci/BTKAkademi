import requests
import json

result = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
result = json.loads(result.text)
secim = input('Seçim yap: ')
kac = float(input('Miktar gir'))

sonuc = kac * float(result['rates'][secim])

print(sonuc,secim)