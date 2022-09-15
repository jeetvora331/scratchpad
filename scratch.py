from tokenize import group

import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagrams(strs):
    hash = {}
    for s in strs:
        sorted_str = "".join(sorted(s))

        if sorted_str not in hash:
            hash[sorted_str] = []

        hash[sorted_str].append(s)

    return list(hash.values())


# def groupAnagrams(strs):

#     strs_table = {}

#     for string in strs:
#         sorted_string = ''.join(sorted(string))

#         if sorted_string not in strs_table:
#             strs_table[sorted_string] = []

#         strs_table[sorted_string].append(string)

#     return list(strs_table.values())


print(groupAnagrams(strs))

print()
