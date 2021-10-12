from PyDictionary import PyDictionary

dictionary1 = PyDictionary()

def meaning(search_term):
    x = dictionary1.meaning(search_term)

    temp_list = []

    for key in x:
        meaning_type = "**" + key + "**" + " : \n" + "\n".join(x[key]) + "\n"
        temp_list.append(meaning_type)
    return("\n".join(temp_list))
