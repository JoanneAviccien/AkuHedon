def input_handler(prompt):
    not_valid = True

    while not_valid:
        result = input(prompt)

        if result != '':
            not_valid = False
        else:
            print("Masukkan Data Dengan Benar!")
        

    return result