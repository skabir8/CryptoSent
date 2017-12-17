

def q_parse(sentence):
    s_split = sentence.split()
    ret_dic = {'and' : [s_split[0]], 'or': [], 'not' : []}
    i = 1
    while (i < len(s_split)):
        if (s_split[i] in ['and','or','not'] and i != len(s_split)):
            ret_dic[s_split[i]].append(s_split[i+1])
        i += 1
    return ret_dic




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


print(q_parse("btc and chicken or hey not lol and pie or knicks"))
