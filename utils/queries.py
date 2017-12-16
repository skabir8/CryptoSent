
def get_and(word1, word2, data):
    ret_list = []
    for sent in data:
        if (word1 in sent and word2 in sent):
            ret_list.append(sent)
    return ret_list


def get_or(word1, word2, data):
    ret_list = []
    for sent in data:
        if (word1 in sent or word2 in sent):
            ret_list.append(sent)
    return ret_list

def get_not(get_word, not_word, data):
    ret_list = []
    for sent in data:
        if (get_word in sent and not_word not in sent):
            ret_list.append(sent)
    return ret_list
