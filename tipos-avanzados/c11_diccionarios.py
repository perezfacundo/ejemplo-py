"""PEP8"""

punto = {"x": 25, "y": 50}
print(punto["x"])
print(punto["y"])
punto["z"] = 45

if "a" in punto:
    print("encontre a", punto["a"])

print(punto.get("x"))
print(punto.get("a", 11))
