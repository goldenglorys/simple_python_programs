#
# no_of_chars = 256
#
#
# def findSubString(input):
#     stringN = input[0]
#     stringK = input[1]
#
#     hash_pat = [0] * no_of_chars
#     hash_str = [0] * no_of_chars
#
#     for i in range(0, len(input[1])):
#         hash_pat[ord(stringK[i])] += 1
#
#     start, start_index, min_len = 0, -1, float('inf')
#     count = 0
#     for j in range(0, len(input[0])):
#         hash_str[ord(input[0][j])] += 1
#         if hash_str[ord(input[0][j])] <= hash_pat[ord(input[0][j])]:
#             count += 1
#
#         if count == stringK:
#             while (hash_str[ord(input[0][start])] >
#                    hash_pat[ord(input[0][start])] or
#                    hash_pat[ord(input[0][start])] == 0):
#                 if (hash_str[ord(input[0][start])] >
#                         hash_pat[ord(input[0][start])]):
#                     hash_str[ord(input[0][start])] -= 1
#                 start += 1
#             len_str = j - start + 1
#             if min_len > len_str:
#                 min_len = len_str
#                 start_index = start
#     if start_index == -1:
#         print("No such strings")
#         return ''
#     return input[0][start_index: start_index + min_len]
#
#
# if __name__ == "__main__":
#     print(findSubString(["ahffaksfajeeubsne", "jefaa"]))

