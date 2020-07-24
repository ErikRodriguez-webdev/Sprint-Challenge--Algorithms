'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # check if word is empty strings
    if word == "":
        # then return 0
        return 0

    # check if word is not lowercase
    if word.islower() == False:
        # then return word.lower()
        word = word.lower()

    # check if arr[i] is equal to 't' and arr[i + 1] is equal to 'h'
    if word[0] == 't' and word[1] == 'h':
        # then return 1
        return 1 + count_th(word[2:])

    # return count_th(word)
    return count_th(word[1:])


print(count_th("abcthxyz"))
