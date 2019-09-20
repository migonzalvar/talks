import json

data = json.loads(open("listaEstacionsMeteo.json").read())
# print(data)


from glom import glom

# spec = ("listaEstacionsMeteo", ["estacion", "concello"])

spec = ("listaEstacionsMeteo", [{"est": "estacion", "con": "concello"}])
print(glom(data, spec))

# spec1 = ("listaEstacionsMeteo", ["estacion"])
# spec2 = ("listaEstacionsMeteo", ["estacion", "concello"])

# spec3 = ("listaEstacionsMeteo", [{"est": "estacion", "con": "concello"}])
