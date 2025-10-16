Any calcular_ingredientes(harina_kg):

    # Proporciones basadas en la harina
    agua = harina_kg * 0.6  # litros (600 ml)
    levadura = harina_kg * 0.02  # kg (20 g)
    sal = harina_kg * 0.02  # kg (20 g)
    aceite = harina_kg * 0.03  # litros (30 ml)
    # Convertir a gramos y mililitros para mejor comprensión
    agua_ml = agua * 1000
    levadura_g = levadura * 1000
    sal_g = sal * 1000
    aceite_ml = aceite * 1000
    print(f"Para {harina_kg} kg de harina necesitas:")
    print(f"- Agua: {agua_ml:.0f} ml")
    print(f"- Levadura: {levadura_g:.0f} g")
    print(f"- Sal: {sal_g:.0f} g")
    print(f"- Aceite: {aceite_ml:.0f} ml")
# Calcular para 1 kg de harina
calcular_ingredientes(1)