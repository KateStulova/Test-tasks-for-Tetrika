def search_pairs(array, k):
    results = []
    already_used = []
    for i in range(len(array)):
        second_number = k - array[i]
        if second_number not in already_used:
            if second_number in array:
                results.append((array[i], second_number))
                already_used.extend([second_number, array[i]])
        else:
            continue

    return results


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))

