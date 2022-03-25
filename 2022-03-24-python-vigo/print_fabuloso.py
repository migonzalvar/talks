message = "Hola Python Vigo!"
print(message)

palos = ["Oros", "Copas", "Bastos", "Espadas"]
print(palos)
print(*palos)
print(*palos, sep="/")

for c in reversed(range(10)):
     print(c, end="")
print()

d = {"nombre": "Python", "popularidad": 99.9}
print(d)
print(f"d={d}")
print(f"{d=}")

print(f"{d['nombre']}")
