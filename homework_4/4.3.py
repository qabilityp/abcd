import random
def random_numbers():
    my_list= [random.randint(1, 9) for i in range(random.randint(3, 10))]
    result = [my_list[0], my_list[2], my_list[-2]]
    print(my_list)
    print(result)

random_numbers()