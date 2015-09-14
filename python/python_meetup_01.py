def catch_pairs():
    #list of #s, find all pairs of integers
    num_list = [1,2,3,4,5,2,3,6,7,8,5,3,3,3,3,9,6]

    dict_list = {}
    for i in num_list:
        dict_list[i] = num_list.count(i)
    print(dict_list)

def ordered_letters():
    letter_list = ["a","b","c","e","f","a"]
    for i in range(len(letter_list)-1):
        asce = ord(letter_list[i])
        asceup = ord(letter_list[i+1])

        new_list = []
        big_list = []

        if (asceup-asce == 1) and (asceup != None):
            new_list.append(asce)
            if new_list > big_list:
                big_list = new_list
        else:
            new_list.append(asce)
            new_list = []

        print(big_list)



    # new_list = []
    # for i, j in enumerate(letter_list):
    #     if (letter_list[i+1] - letter_list[i] == 1):
    #         new_list += letter_list[i]


print(ordered_letters())
