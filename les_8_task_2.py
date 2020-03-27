# Закодируйте любую строку по алгоритму Хаффмана.

import collections


# Создаем класс Node
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node[{self.value:^5}]'


# Функция, которая создает узлы
def create_node(x, lef, righ):
    t = Node(x)
    t.left = lef
    t.right = righ
    return t


# Функция, реализующая алгоритм Хаффмана. Возвращает корень дерева.
# Внутри функции создается очередь, которая сохраняет узлы дерева.
# И в конце в ней остается один элемент.
def haf_deque_man(st):  # На вход получаем строку
    # Посчитаем частоты всех символов с помощью словаря (буква: количество повторений в строке)
    counter = collections.Counter()
    for i in st:
        counter[i] += 1
    # Создаем очередь для дерева
    deq = collections.deque()
    n = len(counter)
    for i in range(n):
        deq.append(counter.most_common(n)[i])  # Добавляем элементы по убыванию.
    deq.reverse()  # РАзворачиваем, чтобы слева были минимальные по частоте

    i = 0
    while len(deq) > 1:
        # print(deq)
        # Берем два первых элемента из очереди и связываем их, создавая новый узел дерева.
        node_x = create_node(0, deq[0][0], deq[1][0])
        # Приоритет нового узла равен сумме приоритетов
        s = deq[0][1] + deq[1][1]
        deq.popleft()
        deq.popleft()
        # Добавляем узел обратно в очередь
        deq.appendleft((node_x, s))
        # Передвигаем его на его позицию по приоритету
        j = 0
        while j + 1 < len(deq) and deq[j][1] > deq[j + 1][1]:
            deq[j], deq[j + 1] = deq[j + 1], deq[j]
            j += 1
        # print('+', deq)
        i += 1
    # Возвращаем корень дерева
    return deq[0][0]

# Функция распечатывания. В листьях лежат строковые символы. А в узлах 0.
def postorder(tree, code):
    if isinstance(tree, str) != True:
        postorder(tree.left, code + '1')
        postorder(tree.right, code + '0')
    else: # Нашли строку. Печатаем значение и очищаем код.
        print(f'{code}: ', tree)
        code = ''


st_in = 'beep boop beer!'
# print(st_symbols)
# Запускаем Хаффмана, возвращаем корень дерева
root = haf_deque_man(st_in)
postorder(root, '')
