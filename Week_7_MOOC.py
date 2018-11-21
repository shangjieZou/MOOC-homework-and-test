# Reverse Direction Maximum Matching Method,RMM
def load_word_dic(word_list):
    word_dic = set()
    max_length = 1
    for i in range(len(word_list)):
        word_list[i] = unicode(word_list[i], 'utf-8')
        word = word_list[i]
        word_dic.add(word)
        if len(word) > max_length:
            max_length = len(word)
    return max_length, word_dic


def longest_word_search(sent, max_len, word_dic):
    words = []
    sent = unicode(sent, 'utf-8')
    end = len(sent)
    while end > 0:
        for m in range(end - max_len, end):
            if sent[m:end] in word_dic:
                words.append(sent[m:end])
                break
        end = m
    return words


word_list = []
Whole_dictionary = raw_input()
line = Whole_dictionary.split(" ")
for j in range(len(line)):
    word_list.append(line[j])


if(0):
    sent_list = []
    while True:
        test = raw_input()
        sent_list.append(test)
        if not test:
            break

if(0):
    sent_list = []
    stopword = ""
    string = ""
    for line in iter(raw_input, stopword):
        string += line + "\n"
    for i in range(len(string.split())):
        sent_list.append(string.split()[i])


max_len, word_dic = load_word_dic(word_list)
for k in range(len(sent_list)):
    words = longest_word_search(sent_list[k], max_len, word_dic)
    words.reverse()
    words_string = (" ".join(words))
    print words_string