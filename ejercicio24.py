kmsRecorridos=float(input("ingrese los KMS recorridos: "))
precioCombustible=float(input("ingrese el precio del combustible: "))
kmsXlitro=float(input("ingrese los KMS recorridos por litro de combustible: "))
combustibleConsumido=float(kmsRecorridos/kmsXlitro)
importeCombustible=float(combustibleConsumido*precioCombustible)

print(f"Litros de combustible consumidos: {combustibleConsumido}")
print(f"Importe gastado en combustible: {importeCombustible}")