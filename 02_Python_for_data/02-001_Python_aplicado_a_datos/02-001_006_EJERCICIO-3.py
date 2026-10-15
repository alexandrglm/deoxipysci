
# EJERCICIO 3
print("\n --- EJERCIO 3------ \n")
heredoc = """
Dadas estas listas, combina cada producto con su importe usando zip()

productos = ["A", "B", "C"]
importes = [60, 105, 24]

"""
print(heredoc)


productos = ["A", "B", "C"]
importes = [60, 105, 24, 99] # Meto un valor de mas para autorecordarme que zip() se detendrá en el momento en que unos valores con otros se unan

merged_zip = list(zip(productos, importes))

print("\n Lista mezclada de importes y productos: ", merged_zip)
