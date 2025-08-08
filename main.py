from integrantes import gestion_usuarios, integrantes
from cuotas import gestion_cuotas

while True:
    print("\nBienvenido a GestorApp 📝\n")
    print("Menú principal 🏠\n")
    print("1. Integrantes")
    print("2. Cuotas")
    print("3. Gastos")
    print("4. Salir")

    opcion = input("Ingresa una opción: ")

    if opcion == "1":
        print("x")
        gestion_usuarios()

    elif opcion == "2":
        print("")
        gestion_cuotas(integrantes)
    
    elif opcion == "3":
        print("")


    #salir
    elif opcion == "4":
        print("Saliendo...")
        break      


    else:
        print("❌ Ingresa una opción valida")
        break

