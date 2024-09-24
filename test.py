from main import count_common_elements


def test_function():
    # initializing a list of results
    results = []
    # test 1
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    list3 = [4, 6, 7, 8]
    if count_common_elements(list1, list2, list3) == 1:
        results.append('true')
    else:
        results.append('false')
    # test 2
    list1 = [11, 23, 8, 4, 5]
    list2 = [61, 4, 5, 6, 7]
    list3 = [4, 5, 7, 8, 9]
    if count_common_elements(list1, list2, list3) == 2:
        results.append('true')
    else:
        results.append('false')
    # test 3
    list1 = [-9, 'elem', 12, 77, 0]
    list2 = [0, -4, 'test', 6, 'elem']
    list3 = [0, 'elem', -7.2, 98, 19]
    if count_common_elements(list1, list2, list3) == 2:
        results.append('true')
    else:
        results.append('false')
    # printing results
    return results


print(test_function())
