class Node():
    def __init__(self, data, nextNode=None):
        self.myData = data
        self.myNext = nextNode


class Stack():
    def __init__(self, node):
        self.myTop = node

    def pop(self):
        node = self.myTop
        self.myTop = self.myTop.myNext
        return node.myData

    def push(self, node):
        temp = self.myTop
        node.myNext = temp
        self.myTop = node

    def peek(self):
        if(not self.myTop):
            return("Empty stack")

        return self.myTop.myData

    def isEmpty(self):
        return self.myTop == None


class Queue():
    def __init__(self, myFirst):
        self.first = myFirst
        self.last = myFirst

    def pop(self):
        if(not self.first):
            return "Empty Queue"

        temp = self.first
        self.first = temp.myNext
        return temp.myData

    def push(self, newNode):
        if(self.first == self.last):
            self.last = newNode
            self.first.myNext = newNode
        else:
            self.last.myNext = newNode
            self.last = newNode

    def remove(self):
        temp = self.first
        if(not temp):
            return "Empty queue"

        self.first = self.first.myNext
        if(self.first == None):
            self.last = None

        return temp.myData

    def peek(self):
        if(self.first):
            return self.first.myData
        return "Queue empty"

    def isEmpty(self):
        return self.first == None


# 1: Simulate 3 Stacks in array
class StackSimulated():
    def __init__(self, myCapacity):
        self.capacity = myCapacity  # Capacidad de cada stack
        self.numberStacks = 3  # Numero de stacks en el arreglo
        # Espacios totales para todos los valores
        self.valores = [0] * (self.capacity * self.numberStacks)
        # Arreglo con los tamaños de cada stack
        self.size = [0] * self.numberStacks

    # Función que nos brinda el índice disponible para insertar un valor
    def obtainIndex(self, numberStack):
        # Obtenemos el offset de acuerdo a que stack queramos añadir
        offset = numberStack * self.capacity
        # Obteneños el tamaño del stack en cuestión
        mySize = self.size[numberStack]
        # Regresamos el índice que es el offset + el tamaño menos 1
        return offset+mySize-1

    # Método para agragar un valor de acuerdo al stack seleccionado
    def pushValue(self, value, numberStack):
        # Si aun hay capacidad
        if(self.size[numberStack] < self.capacity):
            # Aumentamos el tamaño
            self.size[numberStack] += 1
            # Obtenemos el índice
            index = self.obtainIndex(numberStack)
            # Añadimos el valor en su espacio correspondiente
            self.valores[index] = value
            print(self.valores)

    # Método para sacar un valor dependiendo del stack seleccionado
    def popValue(self, numberStack):
        # Obtenemos el índice del ultimo elemento añaddido
        index = self.obtainIndex(numberStack)
        self.size[numberStack] -= 1  # Reducimos el tamaño
        # Regresamoe el valor en la posición adecuada
        return self.valores[index]


# 2 Design a Stack that returns the "minimum" number in O(1)
class StackMin():
    def __init__(self, top=None):
        self.myTop = top
        self.min = top

    def push(self, value):
        value.myNext = self.myTop
        self.myTop = value
        if(value.myData < self.min.myData):
            reference = value
            reference.myNext = self.min
            self.min = reference

    def pop(self):
        if(self.myTop == self.min):
            self.min = self.min.myNext

        reference = self.myTop
        self.myTop = self.myTop.myNext

        return reference.myData

    def minimum(self):
        return self.min.myData


def main():
    node1 = Node(12)
    node2 = Node(9)
    node3 = Node(4)
    node4 = Node(1)

    myStack = StackMin(node1)
    myStack.push(node2)
    myStack.push(node3)
    print(myStack.minimum())
    print("Pop: ", myStack.pop())
    print(myStack.minimum())
    myStack.push(node4)
    print(myStack.minimum())
    print("Pop: ", myStack.pop())
    print(myStack.minimum())


main()
