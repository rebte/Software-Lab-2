from linked_list import LinkedList
from array_list import ArrayList

def demo_linked_list():
    print("=== Демонстрація LinkedList ===")
    lst = LinkedList()
    print("Додаємо елементи: a, b, c")
    lst.append('a')
    lst.append('b')
    lst.append('c')
    print(f"Поточний список: {[lst.get(i) for i in range(lst.length())]}")

    print("Вставляємо 'x' на позицію 1")
    lst.insert('x', 1)
    print(f"Після вставки: {[lst.get(i) for i in range(lst.length())]}")

    print("Видаляємо елемент з позиції 2")
    removed = lst.delete(2)
    print(f"Видалено: {removed}")
    print(f"Після видалення: {[lst.get(i) for i in range(lst.length())]}")

    print("Шукаємо перше входження 'x':", lst.findFirst('x'))
    print("Шукаємо останнє входження 'a':", lst.findLast('a'))

    print("Реверсуємо список")
    lst.reverse()
    print(f"Після реверсу: {[lst.get(i) for i in range(lst.length())]}")

    print("Клонуємо список")
    clone = lst.clone()
    print(f"Клон: {[clone.get(i) for i in range(clone.length())]}")

    print("Очищаємо список")
    lst.clear()
    print(f"Довжина після очищення: {lst.length()}\n")


def demo_array_list():
    print("=== Демонстрація ArrayList ===")
    lst = ArrayList()
    print("Додаємо елементи: 1, 2, 3")
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"Поточний список: {[lst.get(i) for i in range(lst.length())]}")

    print("Вставляємо 99 на позицію 0")
    lst.insert(99, 0)
    print(f"Після вставки: {[lst.get(i) for i in range(lst.length())]}")

    print("Видаляємо елемент з позиції 3")
    removed = lst.delete(3)
    print(f"Видалено: {removed}")
    print(f"Після видалення: {[lst.get(i) for i in range(lst.length())]}")

    print("Шукаємо перше входження 2:", lst.findFirst(2))
    print("Шукаємо останнє входження 3:", lst.findLast(3))

    print("Реверсуємо список")
    lst.reverse()
    print(f"Після реверсу: {[lst.get(i) for i in range(lst.length())]}")

    print("Клонуємо список")
    clone = lst.clone()
    print(f"Клон: {[clone.get(i) for i in range(clone.length())]}")

    print("Очищаємо список")
    lst.clear()
    print(f"Довжина після очищення: {lst.length()}\n")


if __name__ == '__main__':
    demo_linked_list()
    demo_array_list()
