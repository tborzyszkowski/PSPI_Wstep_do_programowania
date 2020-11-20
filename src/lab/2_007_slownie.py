def number_to_list(number):
    liczba = number
    result = []
    while liczba > 0:
        result.append(liczba % 10)
        liczba = liczba // 10
    result.reverse()
    return result


print(number_to_list(102))
# print(number_to_list(1234567890))

# def number_list_to_names(numb_list):
#     numbers = ["zero", "jeden", "dwa",
#                "trzy", "cztery", "piec",
#                "szesc", "siedem", "osiem", "dziewiec"]
#     return [el for el in map((lambda x: numbers[x]), numb_list)]
#
#
# n = 1997
# print(number_list_to_names(number_to_list(n)))
#
