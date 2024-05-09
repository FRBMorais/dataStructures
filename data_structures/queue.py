class Queue:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.iterable_list = self.__conversion__(self.iterable)

    def __conversion__(self, iterable) -> list:
        if isinstance(iterable, list):
            return iterable
        elif isinstance(iterable, tuple):
            return list(iterable)
        else:
            pass # error

    def offer(self, value) -> None:
        """insert the value at the tail of the queue
        
        Keyword arguments:
        argument -- a value to insert at the tail of the queue
        Return: None
        """
        
        self.iterable.append(value)

    def poll(self):
        """Removes the value at the head of the queue, and return it
        
        Keyword arguments:
        Return: the value at the head of the queue
        """
        
        value = self.iterable[0]
        del self.iterable[0]
        return value
    
    def peek(self):
        return self.iterable[0]
    
    def __str__(self) -> str:
        return f"Queue \ntail --> {self.iterable[::-1]} --> head"

