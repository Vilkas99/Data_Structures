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


# Problemas (Cracking the coding interview)

# 1 Codigo para remover duplicados de una lista no ordenada
def deleteRepeated(head):
    # [2, 3, 4, 2, 3, 1, 6, 7]
    myNumbers = []  # 2 3 4 1 6 7
    currentNode = head  # None
    prevNode = head  # 7
    while(currentNode):
        if(currentNode.value in myNumbers):
            if(currentNode == head):
                head = head.next_value
                prevNode = head.next_value

            prevNode.next_value = currentNode.next_value
            currentNode = currentNode.next_value

        else:
            myNumbers.append(currentNode.value)
            prevNode = currentNode
            currentNode = currentNode.next_value

    return myNumbers

# 2 Código para encontrar el n'th elemento desde el final de una lista

# Version 1 (Iterativa)


def nodoNth(number, head):
    # TESTCASE: [1, 3, 4, 7, 9] 3
    currentNode = head
    nodes = []
    while(currentNode):
        nodes.append(currentNode)
        currentNode = currentNode.next_value

    if(len(nodes) - number < 0):
        return "It cannot be done"

    negativeIndex = (number)*-1
    result = nodes[negativeIndex]  # Is it correct or i have to crea
    return result.value


# Version 2 (Iterativa con runners)
def nodoNthRunners(number, head):
    fast = head  # 1
    slow = head  # 4
    findNumber = False  # True
    counter = 1
    counter_slow = 1
    indexToFind = 0

    while(True):
        if(not findNumber):  # WE CAN'T FIND NUMBER'CAUSE WE DON'T KNOW LENGTH OF LINKED LIST
            # If we can have a nex_value...
            if(slow.next_value and fast.next_value):
                if(fast.next_value.next_value):  # There is a next next value?
                    fast = fast.next_value.next_value  # Move fast two positions forward
                    counter += 2  # Augment the counter
                else:  # If there are no nodes two positions ahead
                    fast = fast.next_value  # Move just only one
                    counter += 1  # Augment the counter by one

                slow = slow.next_value  # Either way slow always moves 1 position
                print("Slow value: ", slow.value)
                counter_slow += 1  # Augment counter for slow

            # If we've reached the end of the linked list
            else:
                fast = head  # We reset fast to the beggining
                indexToFind = counter - number  # We obtain the index
                counter = 0  # We start at 0 in our counter

                # If the index is less than 0 (There're less elements with respect to the number)
                if(indexToFind < 0):
                    return "It cannot be done"

                findNumber = True  # We stablished that we're ready to find the number
                print("Counter_Slow: ", counter)

        else:
            # If the counter of slow is less than the index...
            if(counter_slow-1 < indexToFind):
                print("Slow is less than index")
                slow = slow.next_value  # We move to the next index
                counter_slow += 1

            # If it's equal
            elif(counter_slow-1 == indexToFind):
                print("Final SLOW: ", slow)
                return slow.value  # Retun value of slow

            # If it's greater.. we should use fast
            else:
                # If the counter of fast is equal to the index...
                if(counter == indexToFind):
                    return fast.value  # We return fast value
                # Else, we look for it by moving to the next value and moddifyng the counter by one
                else:
                    fast = fast.next_value
                    counter += 1


# Version 3 (Recursiva)
def nodoNthRecursive(head, history, index):
    # TESTCASE: [1, 3, 4, 7, 9] 3

    if(head == None):
        return history[index*-1].value

    history.append(head)
    return nodoNthRecursive(head.next_value, history, index)

# 3 Eliminar nodo que se encuentre a la mitad


def deleteMiddle(head):

    slow = head
    fast = head
    end = False
    process = True

    while(process):
        if(not end):
            if(fast.next_value and slow.next_value):
                if(fast.next_value.next_value):
                    fast = fast.next_value.next_value
                else:
                    fast = fast.next_value
                slow = slow.next_value

            else:
                fast = head
                end = True

        else:
            if(fast.next_value == slow):
                fast.next_value = slow.next_value
                slow.next_value = None
                process = False

            fast = fast.next_value

    return head


def main():
    nodo2 = Node(3)
    nodo1 = Node(2, nodo2)
    head = Node(1, nodo1)

    traverse_linkedList(head)

    nuevo = Node(4)
    nuevo2 = Node(5)
    nuevo3 = Node(6)
    nuevo4 = Node(6)
    nuevo5 = Node(5)

    add_end(head, nuevo)
    add_end(head, nuevo2)
    add_end(head, nuevo3)
    add_end(head, nuevo4)
    add_end(head, nuevo5)

    print(traverse_linkedList(head))
    print(deleteRepeated(head))
    print(traverse_linkedList(head))
    print(nodoNthRunners(3, head))
    print(nodoNth(3, head))
    print(nodoNthRecursive(head, [], 3))
    print("------------------")
    print(traverse_linkedList(deleteMiddle(head)))


main()
