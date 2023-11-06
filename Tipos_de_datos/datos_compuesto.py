#Son datos que dentro de ellos tienen otros datos

#creando una lista (se puede modifical)
lista = ["oscar mateo", "cositas", True, 1.80]
#nos saca por pantalla el dato 3 de la lista, ya que se empieza a contar desde el 0
print(lista[2])

#creando una tupla (no se puede modificar)
tupla = ("oscar mateo", "cositas", True, 1.80)
print(tupla[1])

#creando un conjunto (set)(no se accede a elementos por indice, no alamacena datos duplicados)
set = {"oscar mateo", "cositas", True, 1.80}
print (set)

#creando un diccionario (dict) (es clave : valor separados por comas)
dict = {
    "nombre" : "oscar mateo",
    "cositas" : "jesucristo",
    "altura" : 1.80
}
print(dict ["cositas"])