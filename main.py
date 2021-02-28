# Listas ligadas (LINKED LISTS)
class Node:
    def __init__(self, myValue,  next_value=None):
        self.next_value = next_value
        self.value = myValue


def traverse_linkedList(base):
    results = []
    currentNode = base
    while(currentNode):
        print(currentNode.value)
        results.append(currentNode.value)
        currentNode = currentNode.next_value
    return results


def add_beggining(base, newNode):
    newNode.next_value = base


def add_end(base, newNode):
    currentNode = base
    while(currentNode.next_value):
        currentNode = currentNode.next_value

    currentNode.next_value = newNode


def delete(base, value):
    currentNode = base
    if(currentNode.value == value):
        currentNode.next_value = None

    while(currentNode.next_value):
        if(currentNode.next_value.value == value):
            if(currentNode.next_value.next_value):
                currentNode.next_value = currentNode.next_value.next_value
            else:
                currentNode.next_value = None
            break

        currentNode = currentNode.next_value


def twoRunners(base):
    runner1 = base  # Corredor lento
    runner2 = base  # Corredor rapido
    modify = False  # Modificar

    if(base.next_value.next_value):  # Si existen al menos tres elementos...
        # Establecemos la posición del rápido en el tercer valor
        runner2 = base.next_value.next_value

    while(True):
        if(not modify):  # Si aun no es necesario modificar los elementos de la lista
            if(runner1.next_value):  # Si hay un elemento siguiente
                runner1 = runner1.next_value  # Nos desplazamos con el corredor lento
            else:
                break
            if(runner2.next_value):  # Si hay un elemento siguiente
                # Y este elemento a su vez tiene otro elemento a su derecha
                if(runner2.next_value.next_value):
                    runner2 = runner2.next_value.next_value
                # En caso de que no, solo lo movemos al siguiente elemento
                else:
                    runner2 = runner2.next_value

            # Si el runner dos ya llegó al final de la lista...
            else:
                modify = True  # Establecemos que es hora de modificar la lista
                runner2 = base  # Lo regresamos a la cabeza (base)
        else:
            # Con este método combinamos las listas (O los elementos de esta)
            if(runner1):  # Si el runner 1 aun tiene valor...
                headReference = runner2  # Creamos una referencia al runner 2
                runner2 = runner2.next_value  # Nos movemos al siguiente
                # Establecemos que el siguiente de la referencia será el runner 1
                headReference.next_value = runner1
                valueReference = runner1  # Creamos una referencia para el runner 1

                if(runner1.next_value):  # Si el runner 1 aun tiene elementos a su derecha
                    runner1 = runner1.next_value  # Nos desplazamos
                    # Asignamos que el valor referencia su siguiente valor será el del runner 2
                    valueReference.next_value = runner2
                    print("-------------------")
                    print(headReference.value)
                    print(headReference.next_value.value)
                    print("-------------------")
                else:
                    print("-------------------")
                    print(headReference.value)
                    print(headReference.next_value.value)
                    print("-------------------")
                    break

            else:  # Si el runner 1 ya no tiene valor (Llegamos al final)
                break


def main():
    nodo2 = Node(3)
    nodo1 = Node(2, nodo2)
    head = Node(1, nodo1)

    traverse_linkedList(head)

    nuevo = Node(4)
    nuevo2 = Node(5)
    nuevo3 = Node(6)
    add_end(head, nuevo)
    add_end(head, nuevo2)
    add_end(head, nuevo3)

    twoRunners(head)
    print(traverse_linkedList(head))


main()
