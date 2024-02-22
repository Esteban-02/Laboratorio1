class Conjunto:
    def __init__(self, elementos=None):
        if elementos is None:
            elementos = []
        self.elementos = set(elementos)

    def agregar(self, elemento):
        self.elementos.add(elemento)

    def union(self, *otros_conjuntos):
        union = Conjunto(self.elementos)
        for otro_conjunto in otros_conjuntos:
            for elemento in otro_conjunto.elementos:
                union.agregar(elemento)
        return union

    def interseccion(self, *otros_conjuntos):
        interseccion = Conjunto(self.elementos)
        for otro_conjunto in otros_conjuntos:
            for elemento in self.elementos.copy():
                if elemento not in otro_conjunto.elementos:
                    interseccion.elementos.remove(elemento)
        return interseccion

    def diferencia(self, *otros_conjuntos):
        diferencia = Conjunto(self.elementos)
        for otro_conjunto in otros_conjuntos:
            for elemento in otro_conjunto.elementos:
                if elemento in diferencia.elementos:
                    diferencia.elementos.remove(elemento)
        return diferencia

    def complemento(self, *otros_conjuntos):
        conjunto_universal = Conjunto()
        for otro_conjunto in otros_conjuntos:
            conjunto_universal = conjunto_universal.union(otro_conjunto)

        complemento = Conjunto(conjunto_universal.elementos)
        for elemento in self.elementos:
            complemento.elementos.discard(elemento)
        return complemento

    def combinacion(self, *otros_conjuntos):
        combinacion = Conjunto()
        for elemento in self.elementos:
            combinacion.agregar(elemento)
        for otro_conjunto in otros_conjuntos:
            for elemento in otro_conjunto.elementos:
                combinacion.agregar(elemento)
        return combinacion

    def cardinalidad(self):
        return len(self.elementos)

    def es_subconjunto(self, otro_conjunto):
        return self.elementos.issubset(otro_conjunto.elementos)

    def es_disjunto(self, otro_conjunto):
        return self.interseccion(otro_conjunto).cardinalidad() == 0


def imprimir_menu():
    print("1. Crear nuevo conjunto")
    print("2. Agregar elemento a un conjunto")
    print("3. Realizar operaciones entre conjuntos")
    print("4. Salir")


def crear_conjunto():
    elementos = input("Ingrese los elementos separados por coma: ").split(",")
    conjunto = Conjunto(elementos)
    return conjunto


def agregar_elemento(conjunto):
    elemento = input("Ingrese el elemento a agregar: ")
    conjunto.agregar(elemento)


def obtener_conjuntos_para_operaciones(conjuntos):
    print("Conjuntos disponibles:")
    for i, conjunto in enumerate(conjuntos):
        print(f"{i + 1}. {conjunto.elementos}")
    indices_conjuntos = input("Seleccione los conjuntos a utilizar separados por coma (por ejemplo, '1,2,3'): ")
    indices = [int(index.strip()) - 1 for index in indices_conjuntos.split(",")]
    conjuntos_seleccionados = [conjuntos[index] for index in indices]
    return conjuntos_seleccionados


def realizar_operaciones(conjuntos):
    print("Operaciones disponibles:")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Complemento")
    print("5. Combinación")
    operacion = int(input("Seleccione la operación a realizar: "))

    conjuntos_seleccionados = obtener_conjuntos_para_operaciones(conjuntos)

    if operacion == 1:
        resultado = conjuntos_seleccionados[0].union(*conjuntos_seleccionados[1:])
    elif operacion == 2:
        resultado = conjuntos_seleccionados[0].interseccion(*conjuntos_seleccionados[1:])
    elif operacion == 3:
        resultado = conjuntos_seleccionados[0].diferencia(*conjuntos_seleccionados[1:])
    elif operacion == 4:
        universo = crear_conjunto()
        resultado = conjuntos_seleccionados[0].complemento(universo)
    elif operacion == 5:
        resultado = conjuntos_seleccionados[0].combinacion(*conjuntos_seleccionados[1:])
    else:
        print("Operación no válida")
        return

    print("Resultado:", resultado.elementos)


def main():
    conjuntos = []
    while True:
        imprimir_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            conjuntos.append(crear_conjunto())
        elif opcion == 2:
            if len(conjuntos) == 0:
                print("No hay conjuntos creados. Cree un conjunto primero.")
            else:
                print("Seleccione un conjunto:")
                for i, conjunto in enumerate(conjuntos):
                    print(f"{i + 1}. {conjunto.elementos}")
                indice_conjunto = int(input()) - 1
                agregar_elemento(conjuntos[indice_conjunto])
        elif opcion == 3:
            if len(conjuntos) < 2:
                print("Se necesitan al menos dos conjuntos para realizar operaciones.")
            else:
                realizar_operaciones(conjuntos)
        elif opcion == 4:
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
