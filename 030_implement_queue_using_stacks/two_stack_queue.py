class MyQueue:

    def __init__(self):
        self.valid_stack = 1
        self.stack_one = []
        self.stack_two = []
        self.peek_value = None
        self.pop_on = False

    def push(self, x: int) -> None:        
        
        if self.pop_on == True:
            self.stack_two, self.stack_one  = self.__reverse_lists__(self.stack_two, self.stack_one)
            self.pop_on = False

        if self.peek_value == None:
            self.peek_value = x

        self.stack_one.append(x)
        

    def pop(self) -> int:

        if self.pop_on == False:
            self.stack_one, self.stack_two = self.__reverse_lists__(self.stack_one, self.stack_two)
            self.pop_on = True

        return_value = self.stack_two.pop()
        
        if self.stack_two:
            self.peek_value = self.stack_two[-1]
        else:
            self.peek_value = None


        return return_value
    
    def peek(self) -> int:
        return self.peek_value

    def empty(self) -> bool:
        return not bool(self.stack_one) and not bool(self.stack_two)
    
    def __reverse_lists__(self, stack_one, stack_two):
        while len(stack_one):
            stack_two.append(stack_one.pop())
        return stack_one, stack_two
    

def main():
    tester = MyQueue()
    tester.push(1)
    tester.push(2)
    tester.push(3)
    tester.push(4)
    print(tester.pop())
    tester.push(5)
    print(tester.pop())
    print(tester.pop())
    print(tester.pop())
    print(tester.pop())
    print("Expected result [1,,2,3,4,5]")
if __name__ == "__main__":
    main()
