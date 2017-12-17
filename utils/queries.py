

def q_parse(sentence):
    s_split = sentence.split()
    ret_dic = {'and' : [s_split[0]], 'or': [], 'not' : []}
    i = 1
    while (i < len(s_split)):
        if (s_split[i] in ['and','or','not'] and i != len(s_split)):
            ret_dic[s_split[i]].append(s_split[i+1])

        i += 1

    return ret_dic


def get_match(want_list, or_list, no_list, all_data):
  ret_list = []
  for sent in all_data:
      ands = and_match(want_list, sent)
      ors = or_match(or_list, sent)
      nos = not_match(no_list, sent)
      for sent1 in nos:
          if (sent1 in ands or sent1 in ors):
              ret_list.append(sent1)
  return ret_list


def and_match(q_list, sent):
    counter = 0
    word_hold = []
    s_split = sent.split()
    for word in q_list:
        if word in s_split:
            counter += 1
    if ( counter == len(q_list)):
        word_hold.append(sent)
        return word_hold
    else:
        return []

def or_match(q_list, sent):
    word_hold = []
    s_split = sent.split()
    for word in q_list:
        if word in s_split:
            word_hold.append(sent)
            return word_hold
    return word_hold

def not_match(q_list, sent):
    counter = 0
    word_hold = []
    s_split = sent.split()
    for word in q_list:
        if word not in s_split:
            counter += 1
    if ( counter == len(q_list)):
        word_hold.append(sent)
        return word_hold
    else:
        return []

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





#ex = q_parse("btc and chicken or hey not lol and pie or knicks")
#print(get_match(ex['and'],ex['or'],ex['not'],["I love btc hey chicken","I love btc hey chicken lol"]))
