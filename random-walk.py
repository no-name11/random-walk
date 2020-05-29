import random
import matplotlib.pyplot as plt
'''
we are making a random walk program and will try to plot the final location of a pointer after n no. of steps 
we will repat this experiment x np of times
thew graph will be a 2-D graph
both n and x will be given by the user
'''

current_location_x = 0
current_location_y = 0
way_next = 0
xl = []
yl = []

n = int(input('plz enter the no. of seps in one test:- '))
b = int(input('plz enter the no. of times u want to run the test:- '))

def direction():
    global way_next
    option = [1,2,3,4]
    way_next = random.choice(option)

def movement():
    global current_location_x
    global current_location_y
    '''
    we are using the no. given by way next to move tho pointer
    1 will make it go right(east)
    2 will make it go north(up)
    3 will make it go left(west)
    4 will make it go down(south)
    '''
    if way_next == 1:
        current_location_x += 1
    if way_next == 2:
        current_location_y += 1
    if way_next == 3:
        current_location_x -= 1
    if way_next == 4:
        current_location_y -= 1

def test():
    global n
    global current_location_x
    global current_location_y
    i = 0
    while i < n:
        direction()
        movement()
        i += 1

    xl.append(current_location_x)
    yl.append(current_location_y)
    current_location_x = 0
    current_location_y = 0

def test_run():
    global b
    a = 0
    while a < b:
        test()
        a += 1
    #print(xl)
    #print(yl)
    plt.scatter(xl, yl)
    plt.show()


test_run()

