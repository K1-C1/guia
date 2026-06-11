datos = {
    "nombre": input("ingrese su nombre: "),
    "telefono": input("Ingrese su telefono: "),
    "email": input("ingrese su correo: "),
    "edad": int(input("ingrese su edad: "))
}
while True:   
    print("----Menu----")
    print("1. ver ficha")
    print("2. editar datos")
    print("3. salir")
    
    opcion = int(input("ingrese una opcion: "))
    if opcion == 1:
        print("----ficha----")
        for clave, valor in datos.items():
            print(f"{clave:<10}: {valor}")
    elif opcion == 2:
        print("----editar----")
        for clave, valor in datos.items():
            print(f"{clave:<10}: {valor}")
        campo = input("¿que campo?: ")
        if campo in datos:
            nuevo = input("nuevo valor: ")
            if campo == "edad":
                datos[campo] = int(nuevo)
            else:
                datos[campo] = nuevo 
            print("actualizado")
        else:
            print("campo no existe")
    elif opcion == 3:
        print("----ficha final----")
        for clave, valor in datos.items():
            print(f"{clave:<10}: {valor}")
        print("hasta luego")
        break
    else: 
        print("opcion invalida")
print("saliendo")