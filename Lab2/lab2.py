#Problem 2
def display_current_value():
    print(current_value)

#Problem 3
def add(to_add):
    preveouse()
    global current_value
    current_value = to_add + current_value

#Problem 5
def multiply(to_multiply):
    preveouse()
    global current_value
    current_value = to_multiply * current_value

def divide(to_divide):
    global current_value
    if to_divide == 0:
        print("Can't divide by 0")
    else:
        preveouse()
        current_value = current_value / to_divide

#Problem 6
def commitToMemory():
    global memory
    global current_value
    memory=current_value

def recall():
    preveouse()
    global memory
    global current_value
    current_value=memory


#Problem 7
def preveouse():
    global prev
    global current_value
    prev=current_value

def undo():
    global prev
    global current_value
    current_value = prev +current_value
    prev = current_value-prev
    current_value-=prev

def initialize():
    global current_value
    global prev
    global memory
    current_value = 0.0
    memory = 0.0
    prev = 0.0

def get_current_value():
    global current_value
    if(current_value==None):
        initialize()
    return current_value

#Problem 1
if __name__ == '__main__':
    current_value = 0.0
    memory = 0.0
    prev = 0.0
    print("Welcome to the calculator program")
    print("Current value: " + str(current_value))
    add(4)
    display_current_value()







