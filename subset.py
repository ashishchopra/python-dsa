import string

def get_intersection(arr1: [int], arr2: [int]) -> [int]:
    intersection = []
    value_map = {}

    for item in arr1:
        if item not in value_map:
            value_map[item] = True

    for item in arr2:
        if item in value_map:
            intersection.append(item)

    return intersection

def find_first_duplicate(str_arr: [str]) -> str:
    value_map = {}
    for str_item in str_arr:
        if str_item in value_map:
            return str_item
        else:
            value_map[str_item] = True

def missing_chars(input_str: str) -> [str]:
    char_dict = dict.fromkeys(string.ascii_lowercase, 0)
    missing = []
    for char in input_str:
        if char != " ":
            char_dict[char] += 1

    for key, value in char_dict.items():
        if value == 0:
            missing.append(key)

    return missing

arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 2, 4, 6, 8]

print(get_intersection(arr1, arr2))
print(find_first_duplicate(["a", "b", "c", "d", "e", "e", "f", "e", "d"]))
print(missing_chars("the quick brown box jumps over a lazy dog"))