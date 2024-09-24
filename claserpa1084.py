class rpa1084:
    id_proveedor=0
    nom_prov=""
    ubc_prov=""
    empl_prov=""
    tel_prov=0
    email_prov=""
    id_producto=""
    def show_data(self):
        print(f"Id del proveedor: {prov.id_proveedor}")
        print(f"Nombre del proveedor: {prov.nom_prov}")
        print(f"Ubicacion del proveedor: {prov.ubc_prov}")
        print(f"Nombre del empleado que entregara el producto {prov.empl_prov}")
        print(f"Telefonon del proveedor: {prov.tel_prov}")
        print(f"Email del proveedor: {prov.email_prov}")
        print(f"Id del producto a entregar: {prov.id_producto}")
    def lprov(self):
        productos=["Guitarra","Bajo","Teclado","Bateria","Amplificador"]
        for x in productos:
            print(x)
    def tprov(self):
        cantidades=("10","5","7","4","12")
        for x in cantidades:
            print(x)
    def dprov(self):
        marcas={
            "Guitarra":"Dean",
            "Bajo":"Fender",
            "Teclado":"Yamaha",
            "Bateria":"Tama",
            "Amplificador":"Line6"
        }
        for x,y in marcas.items():
            print(x,y)
    def altas(self):
        print("Los datos se guardaron correctamente")
    def bajas(self):
        print("Los datos se borraron correctamente")
#Objeto
prov=rpa1084()
print("--------Datos del proveedor--------")
prov.id_proveedor=36
prov.nom_prov="Music Man"
prov.ubc_prov="Cd. Juarez, Chihuahua, Mexico"
prov.empl_prov="Uziel"
prov.tel_prov="656 690 4234"
prov.email_prov="a.22308051281084@cbtis128.edu.mx"
prov.id_producto=56
prov.show_data()
dat=rpa1084()
print("--------Lista--------")
print("Listado de productos que se entregan")
dat.lprov()
print("--------Tupla--------")
print("Tupla de cantidades a entregar por cada producto")
dat.tprov()
print("--------Diccionario--------")
print("Diccionarrio de marcas de cada producto")
dat.dprov()
print("")
dat.altas()
dat.bajas()