ingreso_mensual = float(input("Ingrese el sueldo mensual "))
gastos_salud = float(input("Ingrese los gastos en SALUD "))
gastos_vivienda = float(input("Ingrese los gastos en VIVIENDA "))
gastos_alimentacion = float(input("Ingrese los gastos en ALIMENTACIÓN "))
gastos_educacion = float(input("Ingrese los gastos en EDUCACIÓN "))
gastos_vestimenta = float(input("Ingrese los gastos en VESTIMENTA "))
sueldo_anual = ingreso_mensual * 12
iess = ((sueldo_anual * 11.35) / 100)
suma_de_gastos = (gastos_salud + gastos_vivienda + gastos_alimentacion +
                  gastos_educacion + gastos_vestimenta)
base_imponible = (sueldo_anual - iess) - suma_de_gastos
if base_imponible <= 11315.00:
    print('No paga impuesto a la renta')
elif 11315.01 <= base_imponible <= 14416.00:
    impuesto_renta = ((base_imponible - 11315.01) * 0.05)
    print("El impuesto a la renta anual es $", impuesto_renta)
elif 14416.01 <= base_imponible <= 18018.00:
    impuesto_renta = ((base_imponible - 14416.01) * 0.1) + 155
    print("El Impuesto a la renta anual es $", impuesto_renta)
elif 18018.01 <= base_imponible <= 21639.00:
    impuesto_renta = ((base_imponible - 18018.01) * 0.12) + 515
    print("El impuesto a la renta es $", impuesto_renta)
elif 21639.01 <= base_imponible <= 43268.00:
    impuesto_renta = ((base_imponible - 21639.01) * 0.15) + 950
    print("El impuesto a la renta es $", impuesto_renta)
elif 43268.01 <= base_imponible <= 64887.00:
    impuesto_renta = ((base_imponible - 43268.01) * 0.2) + 4.194
    print("El impuesto a la renta es $", impuesto_renta)
elif 64887.01 <= base_imponible <= 86516.00:
    impuesto_renta = ((base_imponible - 64887.01) * 0.25) + 8.518
    print("El impuesto a la renta es $", impuesto_renta)
elif 86516.01 <= base_imponible <= 115338.00:
    impuesto_renta = ((base_imponible - 86516.01) * 0.3) + 13.925
    print("El impuesto a la renta es $", impuesto_renta)
elif base_imponible >= 115338.01:
    impuesto_renta = ((base_imponible - 115338.01) * 0.35) + 22.572
    print("El impuesto a la renta es $", impuesto_renta)
else:
    print("Datos no válidos")
