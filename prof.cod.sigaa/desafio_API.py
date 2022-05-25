import http.client
import json


valor = float(input("Quantos EUR você está trocando? "))
print("Obtendo cotação online...")
conn = http.client.HTTPConnection("api.exchangeratesapi.io")
conn.request("GET", "/v1/latest?access_key=a076127e5fbfa2911168cbf0112ef978&symbols=USD,AUD,CAD,PLN,BRL,MXN&format=1")
r1 = conn.getresponse()


if(r1.status == 200):
    print("Cotação obtida com sucesso!")
    data = json.loads(r1.read())  # This will return entire content.
    for rate in data['rates']:
        convertido = valor*data['rates'][rate]
        print("-> {} EUR são {} {}".format(valor,convertido,rate))
else:
    print("Não foi possível obter cotação :[")