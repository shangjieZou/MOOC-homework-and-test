
if(0):
    s = raw_input()
    y = 0

    for i in s:
        y += 1
        print y, i

    s1 = raw_input()
    index = 0
    s2 = ''

    while index < len(s1) - 1:
        if s1[index] > s1[index + 1]:
            s2 += s1[index]
        else:
            s2 = s2 * 2

        index += 1

    print s2


# Test T3
if (0):
    f = open("names.txt", 'r')
    def is_pali(name):
        low = 0
        high = -1
        while low < len(name)/2:
            if name[low] != name[high]:
                return False
            else:
                low += 1
                high -= 1
        return True


    pali_list = []
    for line in f:
        line = line.strip()
        if is_pali(line):
            pali_list.append(line)
    print pali_list

    longest_pali = "a"
    for i in range(len(pali_list)-1):
        if len(pali_list[i]) > len(longest_pali):
            longest_pali = pali_list[i]
        print longest_pali



# Homework T1 mine
if(0):
    string = raw_input()
    string = string.split()

    def is_Yuanyin(item):
        if item in "aeiou":
            return True
        else:
            if item in 'y' and word.find(item) != 0:
                return True
            else:
                return False

    def transferWord(word):
        stop_index = 0
        word = word.lower()
        if is_Yuanyin(word[0])==True:
            NewWord = word + "hay"
        elif word[0:2] == "qu":
            NewWord = word[2:len(word)+1]+"quay"
        else:
            list_Fuyin = []
            for i in range(0, len(word)):
                if is_Yuanyin(word[i])==False:
                    list_Fuyin.append(word[i])
                else:
                    stop_index = i
                    break
            NewWord = word[stop_index:len(word)+1]+word[0:stop_index]+"ay"
        return NewWord


    Newword_List=[]
    for i in range(len(string)):
        word = string[i]
        Newword_List.append(transferWord(word))

    NewSentenceString = (" ".join(Newword_List))
    print NewSentenceString


# Homework T1 online
if(0):
    new_words = ''
    Output_Words = ''
    # Input_Words = []
    Input_Words = raw_input().split()

    for Word in Input_Words:
        Word = Word.lower()
        # print Word
        if Word[0] in 'aeiou':
            new_words = Word + 'hay'
        elif Word[0:2] == 'qu':
            new_words = Word[2:len(Word)] + 'quay'
        else:
            Tmp_Chars = Word[0]
            # print 'haha:',Tmp_Chars
            for Char in Word[1:len(Word)]:
                if Char not in 'aeiouy':
                    Tmp_Chars = Tmp_Chars + Char
                else:
                    break

            n = len(Tmp_Chars)
            if n == len(Word):
                new_words = Word + 'ay'
            else:
                new_words = Word[n:len(Word)] + Word[0:n] + 'ay'
        if len(Output_Words) == 0:
            Output_Words = Output_Words + new_words
        else:
            Output_Words = Output_Words + ' ' + new_words
    print Output_Words


# Homework T2
if(0):
    import keyword
    import string


    def Identifier(s):
        if s not in keyword.kwlist:
            if s[0] in (letter + '_'):
                for i in s[1:]:
                    if i not in (letter + digits + '_'):
                        return False
                return True
        return False


    String_list = []

    letter = string.ascii_letters
    digits = string.digits
    while True:
        s = raw_input()
        if s == '':
            break
        else:
            String_list.append(s)

    for s in String_list:
        if Identifier(s) == True:
            print True
        else:
            print False



if(0):
    import re

    stopword = ""
    string = ""
    for line in iter(raw_input, stopword):
        string += line + "\n"

    words_list = []
    for i in range(len(string.split())):
        words_list.append(string.split()[i])

    for i in range(len(words_list)):
        if not re.search(u"^[_a-zA-Z0-9_]+$", words_list[i]):
            print "False"
        elif not re.search(u"^[a-zA-Z_]+$", words_list[i][0]):
            print "False"
        else:
            print "True"

# Homework T3
if(0):
    stopword = ""
    string = ""

    for line in iter(raw_input, stopword):
        string += line + "\n"

    dict_transferNum = dict(zip('abcdefghijklmnopqrstuvwxyz', [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]))
    string = string.lower()
    string_item = 'abcdefghijklmnopqrstuvwxyz'


    def item_to_num(fra):
        if fra not in string_item:
            return 0
        else:
            return dict_transferNum[fra]

    string = string.split()
    for i in range(len(string)):
        sum_num = 0
        for j in range(len(string[i])):
            sum_num += item_to_num(string[i][j])
        print sum_num

if(0):
    string = ""
    string_list = []
    for i in range(3):
        line = raw_input()
        string_list.append(line)

    dict_transferNum = dict(zip('abcdefghijklmnopqrstuvwxyz', [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]))
    string_Lower_list = []
    for i in range(3):
        string = string_list[i].lower()
        string_Lower_list.append(string)

    string_item = 'abcdefghijklmnopqrstuvwxyz'


    def item_to_num(fra):
        if fra not in string_item:
            return 0
        else:
            return dict_transferNum[fra]


    for i in range(len(string_Lower_list)):
        sum_num = 0
        for j in range(len(string_Lower_list[i])):
            sum_num += item_to_num(string_Lower_list[i][j])
        print sum_num