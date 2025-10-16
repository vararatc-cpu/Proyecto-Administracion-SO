def generar_reporte(usuarios):
    print("=== Reporte de Usuarios ===")
    for u in usuarios:
        print(f"- {u}")

usuarios = ["Ana", "Luis", "Carlos"]
generar_reporte(usuarios)
