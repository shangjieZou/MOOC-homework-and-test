if(0):
    list_erwei = [909,919,929,939,949,959,969,979,989,999]
    list_sanwei = [11,22,33,44,55,66,77,88,99]

    for i in range(10):
        for j in range(9):
            print list_erwei[i]+list_sanwei[j]

# Test T2
if(0):
    list_Num = ["2", "3", "4", "5"]
    list_Cal = ["+", "-", "*", "/", "**"]
    s = 0
    for i in range(4):
        list_Num = ["2", "3", "4", "5"]
        strnum1 = list_Num[i]
        list_Num.remove(list_Num[i])
        for j in range(3):
            strnum2 = list_Num[j]
            for k in range(2):
                list_Num.remove(list_Num[j])
                strnum3 = list_Num[k]
                list_Num.remove(list_Num[k])
                strnum4 = list_Num[0]
                list_Num.insert(k, strnum3)
                list_Num.insert(j, strnum2)
                for l in range(5):
                    list_Cal = ["+", "-", "*", "/", "**"]
                    strcal1 = list_Cal[l]
                    list_Cal.remove(list_Cal[l])
                    for m in range(4):
                        strcal2 = list_Cal[m]
                        for n in range(3):
                            list_Cal.remove(list_Cal[m])
                            strcal3 = list_Cal[n]
                            list_Cal.insert(m, strcal2)
                            string = strnum1 + strcal1 + strnum2 + strcal2 + strnum3 + strcal3 + strnum4
                            if eval(string) == 28:
                                print string

# Homework T1--Loop
if(0):
    import math


    n = int(raw_input())

    stopword = ""
    string = ""
    for line in iter(raw_input, stopword):
        string += line + "\n"


    def prime_or_not(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for k in range(2, int(math.sqrt(n)+1)):
                if n % k == 0:
                    return False
                else:
                    continue
            return True


    def find_prime_index(x,list):
        low = 0
        high = len(list)-1
        while low <= high:
            mid = (low + high) / 2
            if list[mid] == int(x):
                return mid
            elif list[mid] < int(x):
                low = mid + 1
            elif list[mid] > int(x):
                high = mid - 1
        else:
            return -1


    prime_list = []
    for i in range(1, n):
        if prime_or_not(i) == True:
            prime_list.append(i)


    string = string.split()
    for i in range(len(string)):
        print find_prime_index(string[i], prime_list)


# Homework T1 Recursion
if(0):
    import math


    n = int(raw_input())

    input_word_list = []
    line=int(raw_input())
    input_word_list.append(line)
    while True:
        try:
            line = int(raw_input())
            input_word_list.append(line)
        except:
            break


    def prime_or_not(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for k in range(2, int(math.sqrt(n)+1)):
                if n % k == 0:
                    return False
                else:
                    continue
            return True


    def bi_search(x, list,low,high):
        mid = (low+high)/2

        if low <= high:
            if list[mid] == int(x):
                return mid
            elif int(x) < list[mid]:
                return bi_search(int(x), list, low, mid-1)
            elif int(x) > list[mid]:
                return bi_search(int(x), list, mid+1, high)
        else:
            return -1


    prime_list = []
    for i in range(1, n):
        if prime_or_not(i) == True:
            prime_list.append(i)


    for i in range(len(input_word_list)):
        print bi_search(input_word_list[i], prime_list, 0, len(prime_list)-1)

# Homework T2----Please check the output format
if(0):
    n = int(raw_input())

    def triangles():
      L = [1]
      while True:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]
    k = 0

    list_triangle = []
    for t in triangles():
        list_triangle.append(t)
        k = k + 1
        if k == n:
            break


    for i in range(len(list_triangle)-1):
        list_triangle[i].remove(0)


    list_triangle_add_indent = []
    for i in range(n):
        list_triangle_add_indent.append(0)

    for i in range(len(list_triangle)):
        for j in range(len(list_triangle[i])):
            list_triangle[i][j] = str(list_triangle[i][j])

        list_triangle_add_indent[i] = (" ".join(list_triangle[i]))


    total_len_of_strings = 2 * n - 1
    for i in range(len(list_triangle_add_indent)):
        list_triangle_add_indent[i] = ((total_len_of_strings - len(list_triangle_add_indent[i]))/2) * " " + list_triangle_add_indent[i]

        print list_triangle_add_indent[i]


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