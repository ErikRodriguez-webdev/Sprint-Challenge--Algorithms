'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# set up a list track th
th_count = []


def count_th(word):
    # empty string, so return count
    if word == "":
        return len(th_count)

    # if "th" in word, then remove them
    if "th" in word:
        th_count.append(0)
        new_word = word.replace("th", "0", 1)
        return count_th(new_word)
    # else return the count and clear list
    else:
        value = len(th_count)
        th_count.clear()
        return value
