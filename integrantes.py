integrantes = []

def gestion_usuarios():
    while True:
        print("\nGestión de Integrantes 👥\n")
        print("1. Agregar Integrante")
        print("2. Ver Integrantes")
        print("3. Editar Integrante")
        print("4. Volver al menú principal ↩\n")

        opcion = input("\nIngresa una opción: ")

        #agregar integrante
        if opcion == "1":
            agregar_integrante()

        #mostrar lista integrantes
        elif opcion == "2":
            ver_integrantes()

        #editar integrante
        elif opcion == "3":
            editar_integrante()

        #volver
        elif opcion == "4":
            return      

        else:
            print("❌ Ingresa una opción valida")
            continue

#agregar integrante
def agregar_integrante():
    print("\nAgregar nuevo integrante 👤")
    nombre = input("Nombre: ").strip().lower()
    direccion = input("Dirección: ").strip().lower()
    telefono = input("N° whatsapp: ").strip().lower()

    if not nombre or not direccion or not telefono:
        print("❌ Debes ingresar todos los datos")
        return

    integrante = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "cuotas": []
        }

    integrantes.append(integrante)
    print("Integrante agregado correctamente ✅")
    # print(integrantes)
    print(f"Nombre: {integrante['nombre']} - Dirección: {integrante['direccion']} - Teléfono: {integrante['telefono']}")



#mostrar integrantes
def ver_integrantes():
    print("\n--Mostrando lista de integrantes 📌--")
    if not integrantes:
        print("Aún no hay integrantes registrados")

    else:
        for i, integrante in enumerate(integrantes, 1):
            print(f"{i}. Nombre: {integrante['nombre']} - Dirección: {integrante['direccion']} - Teléfono: {integrante['telefono']}")



#editar integrantes
def editar_integrante():
    print("\n--Editar integrante 📝--")
    buscar_nombre = input("Nombre integrante a editar: ").strip().lower()

    encontrado = False
    for integrante in integrantes:
        if buscar_nombre == integrante["nombre"].strip().lower():
            print("\n📌 Integrante encontrado:\n")
            # print(integrante)
            print(f"Nombre: {integrante['nombre']} - Dirección: {integrante['direccion']} - Teléfono: {integrante['telefono']}")

            encontrado = True

            while True:
                print("Que deseas hacer? ❓")
                print("1. Actualizar integrante")
                print("2. Eliminar integrante")
                print("3. Cancelar")
                opcion = input("Elige una opción: ").strip()


                #actualizar datos integrante
                if opcion == "1":
                    print("\n Selecciona el dato que deseas actualizar 📌")
                    while True:
                        print("1. Nombre")
                        print("2. Dirección")
                        print("3. Teléfono")
                        print("4. Cancelar")
                        opcion = input("\nIngresa una opción: ")

                        if opcion == "1":
                            nuevo_nombre = input("Nuevo nombre: ").strip().lower()
                            integrante["nombre"] = nuevo_nombre

                        elif opcion == "2":
                            nueva_direccion = input("Nueva dirección: ").strip().lower()
                            integrante["direccion"] = nueva_direccion

                        elif opcion == "3":
                            nuevo_telefono = input("Nuevo teléfono: ").strip().lower()
                            integrante["telefono"] = nuevo_telefono

                        elif opcion == "4":
                            break

                        else:
                            print("❌ Ingresa una opcion valida")
                            continue

                        print(f"\nIntegrante {integrante['nombre']} actualizado! 🤗\n")
                        # print(integrante)


                        continuar = input("Deseas editar otro dato del mismo integrante (si/no): ")
                        if continuar.lower() != "si" :
                            break


                #elimnar integrante
                elif opcion == "2":
                    print(f"Estás segura de eliminar al integrante: {integrante['nombre']}? ")
                    opcion = input("si/no ").lower().strip()

                    if opcion == "si":
                        integrantes.remove(integrante)
                        print(f"Se ha eliminado a: {integrante['nombre']} ❌")
                        return
                    else:
                        break

                elif opcion == "3":
                    break

                else:
                    print("❌ Ingresa una opcion válida")
                    continue

    if not encontrado:
        print("No se encontró ningún integrante con ese nombre 😥")




# gestion_usuarios()