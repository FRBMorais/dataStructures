class Stack:
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
    
    def push(self, value) -> None:
        """sumary_line
        Insert a value at the end of the stack

        Keyword arguments:
        argument -- value to insert in the stack
        Return: None
        """
        self.iterable.append(value)

    def pop(self) -> None:
        """sumary_line
        Return the last element of the stack and remove it

        Keyword arguments:
        Return: last value of the stack
        """
        
        return self.iterable.pop()
    
    def peek(self) -> None:
        """sumary_line
        Return the last element of the stack

        Keyword arguments:
        Return: last value of the stack
        """
        
        return self.iterable[-1]

    def __str__(self) -> list:
        print(self.iterable)



stack_test = Stack([])

print(type(stack_test))

stack_test.__str__()
stack_test.push(1)
stack_test.push(2)
stack_test.push(4)
stack_test.push(3)
stack_test.__str__()

stack_test.pop()
stack_test.__str__()