
from __future__ import annotations
from typing import Any


class Node(object):
    def __init__(self, data: Any, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node

class LinkedList(object):

    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self: Any) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data) -> None:

        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        previous_node = None
        current_node = self.head
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def reverseIterative(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            ## 1. Temporarily evacuate next_node for next loop
            temp_node = current_node.next

            ## 2. replace next_node direction to previous_node
            current_node.next = previous_node

            # for loop
            ## 3. put the current_node to previous_node
            previous_node = current_node
            ## 1. Temporarily evacuate next_node for next loop
            current_node = temp_node
        self.head = previous_node

if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.print()
    print("############")

    l.reverseIterative()
    # l.print()

