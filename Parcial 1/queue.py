from typing import Any, Optional

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None: #AGREGA EL ELEMENTO AL FINAL DE LA COLA
        self.__elements.append(value)

    def attention(self) -> Optional[Any]: #ELIMINA Y DEVUELVE EL ELEMENTO DEL FRENTE
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int: #TAMAÑO DE LA COLA
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]: #VALOR DEL ELEMENTO DEL FRENTE SIN ELIMINARLO
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]: #MUEVE EL ELEMENTO DEL FRENTE AL FINAL
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    
    def show(self):
        for i in range(len(self.__elements)): # MOSTRAR COLA
            print(self.move_to_end())

