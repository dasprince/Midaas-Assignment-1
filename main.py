user_input = ""
from_ = 0
to_ = 0
method_name = ""
num_list = []
temp = []
loop = True


def input_of_user():
    global user_input, from_, to_
    user_input = input("enter two numbers separated by space :")

    from_ = int(user_input.split()[0])
    to_ = int(user_input.split()[1])




def menu():
    global method_name
    method_name = input("Select which method you want to use to find prime numbers\n"
                        "(A) simple method O(N)\n"
                        "(B) Brut force O(sqrt(N))\n"
                        "(C) sieve of erathosthenes O(N log (log N))\n")


def simple_method(num):
    if num == 1:
        return False
    factors = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1

    if factors == 2:
        return True

    return False


def brut_force(num):
    if num == 1:
        return False

    k = 2
    while k * k <= num:
        if num % k == 0:
            return False
        k += 1
    return True


def sieve_of_erathosthenes(num):
    flag_list = [True for a in range(num + 1)]
    flag_list[0] = False
    flag_list[1] = False
    n = 2
    i = 2
    while n * i <= num:
        while n * i <= num:
            flag_list[n * i] = False
            i += 1
        n += 1
        i = 2
    for i in range(len(flag_list)):
        if flag_list[i] and i in temp:
            num_list.append(i)


while loop:

    menu()
    try:
        input_of_user()
        if from_ < 0 or to_ < 0:
            print("numbers cannot be less than ZERO")
            continue
    except:
        print("Wrong input")
        continue

    if to_ < from_:
        print("invalid range")
        continue

    if method_name.upper() == "A":

        for i in range(from_, to_ + 1):
            if simple_method(i):
                num_list.append(i)

    elif method_name.upper() == "B":

        for i in range(from_, to_ + 1):
            if brut_force(i):
                num_list.append(i)

    elif method_name.upper() == "C":

        for i in range(from_, to_ + 1):
            temp.append(i)
        sieve_of_erathosthenes(to_)

    else:
        print("Wrong Input")
        continue

    print("Prime numbers in the given range are: ", num_list)
    user_input = ""
    from_ = 0
    to_ = 0
    method_name = ""
    num_list = []
    temp = []
    choice = input("Do you want to check another result(y/n)")
    if choice.lower() != "y":
        loop = False
