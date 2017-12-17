

def q_parse(sentence):
    s_split = sentence.split()
    ret_dic = {'and' : [s_split[0]], 'or': [], 'not' : []}
    i = 1
    while (i < len(s_split)):
        if (s_split[i] in ['and','or','not'] and i != len(s_split)):
            ret_dic[s_split[i]].append(s_split[i+1])
        i += 1
    return ret_dic

def get_inv_match(want_list, or_list, not_list, i_index):
    ands = get_inv_and(want_list,i_index)
    ors = get_inv_or(or_list, i_index)
    nots = get_inv_not(not_list, i_index)
    ret_list = []
    comb_list = ands + ors
    for sent in comb_list:
        if (sent not in nots):
            ret_list.append(sent)
    return ret_list

def get_match_condensed(sentence, i_index):
    d = q_parse(sentence)
    return get_inv_match(d['and'],d['or'],d['not'], i_index)


def get_inv_and(want_list, i_index):
    counter = 0
    hold = []
    for x in want_list:
        if (x in i_index):
            counter += 1
            hold.extend(i_index[x])
    if (counter == len(want_list)):
        return hold
    else:
        return []

def get_inv_or(or_list, i_index):
    hold = []
    for x in or_list:
        if (x in i_index):
            hold.extend(i_index[x])
    return hold

def get_inv_not(not_list, i_index):
    counter = 0
    hold = []
    for x in not_list:
        if (x in i_index):
            counter += 1
            hold.extend(i_index[x])
    if (counter == len(not_list)):
        return hold
    else:
        return []




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


exindex = {'love': ['I love btc hey chicken', 'I love btc hey chicken lol'], 'i': ['I love btc hey chicken', 'I love btc hey chicken lol'], 'hey': ['I love btc hey chicken', 'I love btc hey chicken lol'], 'lol': ['I love btc hey chicken lol'], 'btc': ['I love btc hey chicken', 'I love btc hey chicken lol'], 'chicken': ['I love btc hey chicken', 'I love btc hey chicken lol']}

q = "btc and chicken or hey not lol and pie or knicks"
ex = q_parse("btc and chicken or hey not lol and pie or knicks")
#print(ex)
#print(get_match(ex['and'],ex['or'],ex['not'],["I love btc hey chicken","I love btc hey chicken lol"]))
#print get_match_condensed(q, exindex)
