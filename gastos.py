def gestion_gastos():
    while True:
        print("\nRegistro de gastos 💰💰\n")
        print("1. Agregar gasto")
        print("2. Ver gastos")
        print("3. Buscar gasto")
        print("4. Editar gasto")
        print("5. Volver al menú principal")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            agregar_gasto()
        
        elif opcion == "2":
            ver_gastos()

        elif opcion == "3":
            buscar_gasto()

        elif opcion == "4":
            editar_gasto()

        elif opcion == "5":
            return

        else:
            print("❌ Elige una opción válida")



gastos = []

#agregar gasto
def agregar_gasto():
    print("\nAgregar un nuevo gasto 💰")
    nombre = input("Nombre de la actividad (ej: fiesta navidad): ").strip().lower()
    fecha = input("Fecha: ").strip().lower()

    detalles = []
    monto_total = 0

    while True:
        item = input(" nombre del gasto (ej: Bebidas, DJ, maestro): ").strip()
        monto = float(input("Monto del gasto: $ "))
        detalles.append({"item": item, "monto": monto})
        monto_total += monto

        continuar = input("Agregar otro item a los gastos si/no?: ").lower()
        if continuar != "si":
            break

    gasto = {
        "nombre": nombre,
        "fecha": fecha,
        "detalles": detalles,
        "monto_total": monto_total
    }

    gastos.append(gasto)
    print(f"\n Gasto registrado: {nombre} ({fecha}) - Total: ${monto_total}")



#ver gastos
def ver_gastos():
    if not gastos:
        print("\n No hay gastos registrados ⭕")
        return
    
    #calcular total acumulado de todos los gastos
    total_acumulado = sum(gasto["monto_total"] for gasto in gastos)

    print("\n Resumen de gastos")
    print(f"Total acumulado: ${total_acumulado}\n")

    #mostrar detalle por actividad
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. Actividad: {gasto['nombre']} - Fecha: {gasto['fecha']} - Total: ${gasto['monto_total']}")
        print("Detalles:")
        for detalle in gasto["detalles"]:
            print(f"{detalle['item']}: ${detalle['monto']}")




#buscar gasto
def buscar_gasto():
    print("\n--Buscar gasto")
    buscar_gasto = input("Nombre de la actividad: ").strip().lower()

    encontrado = False
    for gasto in gastos:
        if buscar_gasto == gasto['nombre'].strip().lower():
            print("\n Gasto encontrado: \n")

            print(f"Actividad: {gasto['nombre']} - Fecha: {gasto['fecha']} - Detalles: {gasto['detalles']} - Total: ${gasto['monto_total']}")

            encontrado = True

    if not encontrado:
        print("\n No se encontró ningún gasto con ese nombre 😥")



#editar gasto
def editar_gasto():
    print("\n Editar gasto")
    buscar_nombre = input("Nombre actividad a editar: ").strip().lower()

    encontrado = False
    for gasto in gastos:
        if buscar_nombre == gasto["nombre"].strip().lower():
            print("\n📌 Gasto encontrado:\n")
            # print(integrante)
            print(f"Nombre: {gasto['nombre']} - Fecha: {gasto['fecha']} - Detalles: {gasto['detalles']} - Total: ${gasto['monto_total']}")

            encontrado = True

            while True:
                print("Que deseas hacer? ❓\n")
                print("1. Actualizar gasto")
                print("2. Eliminar gasto")
                print("3. Cancelar")
                opcion = input("\nElige una opción: ").strip()

                #actualizar datos gasto
                if opcion == "1":
                    print("\n Selecciona el dato que deseas actualizar 📌")
                    while True:
                        print("1. Nombre")
                        print("2. Fecha")
                        print("3. Cancelar")
                        opcion = input("\nIngresa una opción: ")

                        if opcion == "1":
                            nuevo_nombre = input("Nuevo nombre: ").strip().lower()
                            gasto["nombre"] = nuevo_nombre

                        elif opcion == "2":
                            nueva_fecha = input("Nueva : fecha").strip().lower()
                            gasto["fecha"] = nueva_fecha

                        elif opcion == "3":
                            break

                        else:
                            print("❌ Ingresa una opcion valida")
                            continue

                        print(f"\nGasto {gasto['nombre']} actualizado! 🤗\n")

                        continuar = input("Deseas editar otro dato de la misma actividad (si/no): ")
                        if continuar.lower() != "si" :
                            return

                #elimnar gasto
                elif opcion == "2":
                    print(f"Estás segura de eliminar la actividad: {gasto['nombre']}? ")
                    opcion = input("si/no ").lower().strip()

                    if opcion == "si":
                        gastos.remove(gasto)
                        print(f"Se ha eliminado a: {gasto['nombre']} ❌")
                        return
                    else:
                        break

                elif opcion == "3":
                    break

                else:
                    print("❌ Ingresa una opcion válida")
                    continue

    if not encontrado:
        print("No se encontró ningún gasto con ese nombre 😥")