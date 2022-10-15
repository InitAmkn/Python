
'''Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''


something_text = "забвенный крем перец абвер зимбабвийский река gfdзимбабвийскийggre"

# было


def censorship(delete_word, something_text):
    something_text = something_text + "|"
    while (something_text.find(delete_word) != -1):
        x = something_text.find(delete_word)
        i_start = x
        i_finish = x
        while something_text[i_start].isalpha() == True and i_start > 0:
            i_start -= 1
        while something_text[i_finish].isalpha() == True and i_finish < len(something_text):
            i_finish += 1
        something_text = something_text.replace(
            something_text[i_start:i_finish], '', 1)
        x = something_text.find(delete_word)
    return something_text[:-1]


# стало
def censorship_corrected(delete_word, something_text=""):
    list_text = something_text.split()
    list_ = [i for i in list_text if delete_word not in i]
    return " ".join(list_)


print(censorship("абв", something_text))

print(censorship_corrected("абв", something_text))
