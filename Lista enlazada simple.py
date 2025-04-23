# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Insertar un nuevo valor al inicio de la lista
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente

        return False

    # Buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Imprimir todos los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Contar cantidad de nodos
    def cantidadNodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Sumar valores enteros
    def sumarValores(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

    # Imprimir el primer valor
    def imprimirPrimero(self):
        if self.cabeza:
            print(f"Primer valor de la lista: {self.cabeza.valor}")
        else:
            print("La lista está vacía")

# Solo se ejecuta si el archivo se corre directamente
if __name__ == "__main__":
    lista = ListaEnlazada()

    print("Ingrese números para insertar al final de la lista (ingrese 'fin' para terminar):")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break
        try:
            valor = int(entrada)
            lista.insertar(valor)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    lista.imprimir()

    print("\nInsertando 99 al inicio de la lista...")
    lista.insertar_inicio(99)
    lista.imprimir()

    print(f"Cantidad de nodos: {lista.cantidadNodos()}")
    print(f"Suma de los valores: {lista.sumarValores()}")
    lista.imprimirPrimero()
