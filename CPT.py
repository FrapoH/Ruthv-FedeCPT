def prime_numbers(x,y):
    prime = True
    non_prime_list = []
    prime_list = []
    for number in range (x, y+1):
        prime = True
        if number == 0 or number == 1:
              prime = False
        for z in range (2, number):
            if number % z == 0:
                prime = False
                break
        if prime == True:
            prime_list.append(number)
    print(prime_list)

x = input("Pick the min:")
y = input("Pick the max:")
prime_numbers(int(x), int(y))