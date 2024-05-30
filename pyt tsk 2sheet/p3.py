def genrate_list_and_tuple():

    user_input = input("enter a sq: ")

    num_list = user_input.split(",")

    num_tuple = tuple(num_list)

    print(num_list)
    print(num_tuple)

    genrate_list_and_tuple()