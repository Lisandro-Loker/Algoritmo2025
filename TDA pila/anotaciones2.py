from typing import Any, Optional


class Stack:

    def __Init__(self):
        self.__elements = []
    
    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )
    
    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
       return (
           self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        print(self.__elements)

stack = Stack()

from random import randint

for i in range(5):
    stack.push(randint(1,100))

stack.show()
print(stack.pop())
stack.show()