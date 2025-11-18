from principal import GestorPrincipal

def main():
    app = GestorPrincipal()
    
    while True:
        print("\nBienvenido a GestorApp 📝\n")
        print("Menú principal 🏠\n")
        print("Que ncesitas gestionar hoy? \n")
        print("1. Integrantes")
        print("2. Cuotas")
        print("3. Gastos")
        print("4. Salir")

        opcion = input("Ingresa una opción (1-4): ").strip()

        #opciones
        #integrantes
        if opcion == "1":
            while True:
                print("\n Menú Integrantes \n")
                print("1. Agregar integrante")
                print("2. Ver integrantes")
                print("3. Editar integrante")
                print("4. Volver al menú principal")

                sub_opcion = input("Elige una opción (1-4): ").strip()

                #agregar integrante
                if sub_opcion == "1":
                    nombre = input("Nombre: ")
                    direccion = input("Direccion: ")
                    telefono = input("Telefono: ")
                    app.agregar_integrante(nombre, direccion, telefono)
                    print("Integrante agregado ✅")

                #ver todos los integrantes
                elif sub_opcion == "2":
                    if not app.integrantes:
                        print("\n--Aún no hay integrantes registrados 😥")
                    else:
                        for i in app.integrantes:
                            print(i.mostrar())

                #editar integrante
                elif sub_opcion == "3":
                    buscar = input("Nombre del integrante a editar: ")
                    encontrado = None
                    for i in app.integrantes:
                        if i.nombre.lower() == buscar.lower():
                            encontrado = i
                            break
                    if encontrado:
                        nuevo_nombre = input("Nuevo nombre (Enter para dejar igual): ")
                        nueva_direccion = input("Nueva direccion (Enter para dejar igual): ")
                        nuevo_telefono = input("Nuevo telefono (Enter para dejar igual): ")
                        encontrado.editar(
                            nombre=nuevo_nombre if nuevo_nombre else None,
                            direccion=nueva_direccion if nueva_direccion else None,
                            telefono=nuevo_telefono if nuevo_telefono else None,
                        )
                        print("Integrante actualizado ✅")
                    else:
                        print("No se encontró el integrante 😥")

                #volver
                elif sub_opcion == "4":
                    break

                else:
                    print("Ingresa una opción válida ❌")


        #opcion 2/cuotas
        elif opcion == "2":
            while True:
                print("\n Menú cuotas \n")
                print("1. Registrar pago de cuota")
                print("2. Ver pagos por persona")
                print("3. Ver todos los pagos")
                print("4. Volver al menú principal")

                sub_opcion = input("\nElige una opción (1-4): ").strip()

                #registrar pago
                if sub_opcion == "1":
                    buscar = input("Nombre del integrante: ")
                    encontrado = None
                    for i in app.integrantes:
                        if i.nombre.lower() == buscar.lower():
                            encontrado = i
                            break

                    if encontrado:
                        mes = input("Mes pagado: ")
                        fecha = input("Fecha pago: ")
                        monto = int(input("Monto pagado: "))
                        app.registrar_cuota(encontrado, mes, fecha, monto)
                        print("Pago registrado ✅")
                    else:
                        print("Integrante no encontrado 😥")

                #mostrar pagos de x persona
                elif sub_opcion == "2":
                    buscar = input("Nombre del integrante: ")
                    encontrado = None
                    for i in app.integrantes:
                        if i.nombre.lower() == buscar.lower():
                            encontrado = i
                            break
                    if encontrado:
                        pagos = [c for c in app.cuotas if c.integrante == encontrado]
                        if not pagos:
                            print("No hay pagos registrados para esa persona 😥")
                        else:
                            for c in pagos:
                                print(c.mostrar())
                    else:
                        print("Integrante no encontrado 😥")

                #ver todos los pagos
                elif sub_opcion == "3":
                    if not app.cuotas:
                        print("Aún no hay pagos registrados 😑")
                    else:
                        for c in app.cuotas:
                            print(c.mostrar())

                #volver
                elif sub_opcion == "4":
                    break

                else:
                    print("Ingresa una opción válida ❌")


        #op 3 / gastos
        elif opcion == "3":
            while True:
                print("\n Menú gastos \n")
                print("1. Registrar gasto")
                print("2. Ver gasto específico")
                print("3. Ver todos los gastos")
                print("4. Volver al menú principal")

                sub_opcion = input("\nElige una opción (1-4): ").strip()


                #registrar gasto
                if sub_opcion == "1":        
                    nombre = input("Nombre actividad: ")
                    fecha = input("Fecha: ")
                    gasto = app.registrar_gasto(nombre, fecha)

                    #agregar detalles del gasto
                    while True:
                        item = input("Item (ej: DJ, bebidas, etc): ")
                        monto = int(input("Monto: "))
                        gasto.agregar_detalle(item, monto)

                        otro = input("Agregar otro item? (si/no): ").strip().lower()
                        if otro != "si":
                            break

                    print("Gasto registrado ✅")
                    print(gasto.mostrar())


                #ver gasto especifico
                elif sub_opcion == "2":
                    buscar = input("Nombre de la actividad: ")
                    encontrado = None
                    for i in app.gastos:
                        if i.nombre.lower() == buscar.lower():
                            encontrado = i
                            break
                    if encontrado:
                        print(encontrado.mostrar())
                    else:
                        print("Gasto no encontrado 😥")                


                #ver todos los gastos
                elif sub_opcion == "3":
                    if not app.gastos:
                        print("Aún no hay gastos registrados 😑")
                    else:
                        for c in app.gastos:
                            print(c.mostrar())

                #volver
                elif sub_opcion == "4":
                    break

                else:
                    print("Ingresa una opción válida ❌")                    



main()