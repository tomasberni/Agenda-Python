#AGENDA DE CONTACTOS BY TOMAS BERNI
contactos = [[],[]]

while True: 
    seleccion = str(input("1-Si deseas crear un nuevo registro en la agenda (nombre, telefono)\n 2-Buscar un contacto por nombre y mostrar su teléfonoBuscar un contacto por nombre y mostrar su teléfono\n 3-Modificar teléfono de un contacto existente \n 4-Eliminar un contacto\n 5-Mostrar los contacto\n Selecciona cual es de tu preferencia:"))
    if seleccion == "1":
        nombre = str(input("Escribe el nombre"))
        numero = str(input("Escribe el numero telefonico"))
        contactos[0].append(nombre.title())
        contactos[1].append(numero.title())
        print("\nContactos agregados correctamente\n")
        print(contactos)
        
    elif seleccion == "2":
        busca_contacto = str(input("Ingresa el nombre o numero que quieres buscar: "))
        encontrado = False
        for i in range(len(contactos[0])):
            if contactos[0][i] == busca_contacto.title():
                print(f"Nombre: {contactos[0][i]}, Teléfono: {contactos[1][i]}")
                encontrado = True
                break
            elif contactos[1][i] == busca_contacto.title():
                print(f"Nombre: {contactos[0][i]}, Teléfono: {contactos[1][i]}")
                encontrado = True
                break
        if not encontrado:
            print(f"{busca_contacto} no encontrado en la lista de contactos.")
    elif seleccion == "3":
        modifica_contacto = str(input("Ingresa el nombre que quieres modificar: "))
        if modifica_contacto.title() in contactos[0]:
            indice = contactos[0].index(modifica_contacto.title())
            nuevo_numero = str(input("Ingresa el nuevo número de teléfono: "))
            contactos[1][indice] = nuevo_numero
            print("\nTeléfono modificado correctamente\n")
            print(contactos)
        else:
            print(f"{nombre} no encontrado en la lista de contactos.")
    elif seleccion == "4":
        nombre = str(input("Ingresa el nombre del contacto que deseas eliminar: "))
        if nombre.title() in contactos[0]:
            indice = contactos[0].index(nombre.title())
            del contactos[0][indice]  
            del contactos[1][indice]
            print("\nContacto eliminado correctamente\n")
            print(contactos)
        else:
            print(f"{nombre} no encontrado en la lista de contactos.")

    elif seleccion == "5":
        if len(contactos[0]) == 0:
            print("\nNo hay contactos en la agenda.\n")
        else:
            print("\nLista de contactos:\n")
            for i in range(len(contactos[0])):
                print(f"Nombre: {contactos[0][i]}, Telefono: {contactos[1][i]}")
        print("Contacto Eliminado")

    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")
#AGENDA DE CONTACTOS BY TOMAS BERNI
