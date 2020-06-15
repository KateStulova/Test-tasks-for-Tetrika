with open('task_2_data.txt') as inf:
    normalized_string = inf.readline().strip().replace('"', '').split(',')
    normalized_string.sort()

    all_letters_and_numbers_mult = 0
    names_parameters = {}
    eng_letters_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for name in range(len(normalized_string)):
        letters_sum = names_parameters.get(normalized_string[name], 0)
        letters_and_numbers_mult = 0
        if letters_sum == 0:
            for letter in normalized_string[name]:
                letters_sum += eng_letters_caps.find(letter) + 1
        letters_and_numbers_mult = (name + 1) * letters_sum
        names_parameters[normalized_string[name]] = letters_sum
        all_letters_and_numbers_mult += letters_and_numbers_mult

    print(f'Сумма произведений алфавитных сумм каждого имени и порядковых номеров имени в отсортированной строке равна'
          f' {all_letters_and_numbers_mult}.')
