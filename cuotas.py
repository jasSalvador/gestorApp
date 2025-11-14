from integrantes import integrantes

def gestion_cuotas(integrantes):
    while True:
        print("\nRegistro de cuotas 💰\n")
        print("1. Registrar pago de cuota")
        print("2. Ver cuotas pagadas por persona")
        print("3. Ver todos los pagos")
        print("4. Volver al menú principal")

        opcion = input("\nElige una opción (1-4): ")

        if opcion == "1":
            registrar_cuota(integrantes)
        
        elif opcion == "2":
            ver_pagos(integrantes)
        
        elif opcion == "3":
            ver_total_pagos(integrantes)

        elif opcion == "4":
            return

        else:
            ("❌ Elige una opción válida")


#registrar pago cuota
def registrar_cuota(integrantes):
    print("\nRegistro de pago 💸\n")
    buscar_nombre = input("Nombre integrante: ").strip().lower()

    encontrado = False
    for integrante in integrantes:
        if buscar_nombre == integrante["nombre"].strip().lower():
            print("\n📌 Integrante encontrado:\n")
            # print(integrante)
            print(f"Nombre: {integrante['nombre']} - Dirección: {integrante['direccion']}")

            encontrado = True

            fecha = input("Ingresa fecha del pago (30-07-2025): ")
            monto = int(input("Monto pagado $ "))
            print("Selecciona el mes correspondiente al pago 📆\n")

            while True:
                print("1. Enero")
                print("2. Febrero")
                print("3. Marzo")
                print("4. Abril")
                print("5. Mayo")
                print("6. Junio")
                print("7. Julio")
                print("8. Agosto")
                print("9. Septiembre")
                print("10. Octubre")
                print("11. Noviembre")
                print("12. Diciembre")

                opcion = input("Elige el mes pagado: ")

                meses = {
                    "1": "Enero", "2": "Febrero", "3": "Marzo", "4": "Abril", "5": "Mayo", "6": "Junio", 
                    "7": "Julio", "8": "Agosto", "9": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
                }

                if opcion in meses:
                    mes = meses[opcion]

                    cuota = {
                        "fecha": fecha,
                        "monto": monto,
                        "mes": mes
                    }

                    integrante["cuotas"].append(cuota)
                    print(f"Cuota de {mes} registrada ✅\n")
                    break

                else:
                    print("❌ Ingresa una opción válida")

            break

    if not encontrado:
        print("❌ Integrante no encontrado")



#ver estado cuotas por persona
def ver_pagos(integrantes):
    buscar_nombre = input("Ingresa el nombre de un integrante: ").strip().lower()

    encontrado = False
    for integrante in integrantes:
        if buscar_nombre == integrante["nombre"].strip().lower():

            print("\n📌 Integrante encontrado:\n")
            print(f"Cuotas registradas de: {integrante['nombre']} 📍\n")

            
            if integrante['cuotas']:
                for i, cuota in enumerate(integrante['cuotas'], start=1):
                    print(f"{i}. Mes: {cuota['mes']} - Fecha Pago: {cuota['fecha']} - Monto pagado: {cuota['monto']}\n")

            encontrado = True

    if not encontrado:
        print("❌ Integrante no encontrado")    



#ver todas las cuotas pagadas
def ver_total_pagos(integrantes):
    suma_total = 0

    print("\nResumen de pagos por integrante 📑")

    for integrante in integrantes:
        nombre = integrante['nombre']

        #si no hay cuotas, lista vacia
        if 'cuotas' in integrante:
            cuotas = integrante['cuotas']
        else:
            cuotas = []

        total_pagos = 0
        for cuota in cuotas:
            total_pagos += cuota['monto']

        print(f"{nombre} pagó: $ {total_pagos}")

        suma_total += total_pagos

    print(f"\nTotal recaudado en cuotas: $ {suma_total}")