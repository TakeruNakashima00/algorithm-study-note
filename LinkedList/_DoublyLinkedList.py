from __future__ import annotations
from typing import Any


class Node():

    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList():

    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        current_node.prev = new_node
        new_node.next = current_node
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> Node:
        current_node = self.head
        # 先頭一致
        if current_node and current_node.data == data:
            # nextが存在しない
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return

        # 途中でヒット
        while current_node and current_node.data != data:
            current_node = current_node.next

        # 引っかからないかった場合
        if current_node is None:
            return

        # 最後でヒット
        if current_node.next is None:
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
            return
        else:
        # 途中でヒット
            next_node = current_node.next
            prev_node = current_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
            current_node = None
            return




if __name__ == '__main__':
    d = DoublyLinkedList()
    d.insert(0)
    d.append(1)
    d.append(2)
    d.append(3)
    d.print()
    print("######")
    d.remove(2)
    d.print()