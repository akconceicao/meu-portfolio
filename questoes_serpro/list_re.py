import re

nested_list_of_string = [['HEY There'], [
    'Good AfternOOn'], ['How Is Your Day']]


def lower_string_in_nested_list(list_):
    def function(list_): return re.sub('[^A-Za-z]', ' ', list_[0]).lower()
    return [*map(function, list_)]


print(lower_string_in_nested_list(nested_list_of_string))
