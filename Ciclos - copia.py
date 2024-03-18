# Crear el diccionario de tipo Vuelo
vuelo = {
    'Aerolinea': 'Avianca',
    'Vuelo': 'AV3102',
    'Origen': 'CTG',
    'Destino': 'MDE',
    'Tipo_Maleta': ['Cabina', 'Mano', 'Bodega']
}

# Imprimir los valores del diccionario
print("Valores del diccionario:")
for key in vuelo:
    print(f"{key}: {vuelo[key]}")

# Imprimir los valores de tipo de maleta
print("\nValores de tipo de maleta:")
for tipo_maleta in vuelo['Tipo_Maleta']:
    print(tipo_maleta)
