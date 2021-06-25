#1/usr/bin/env python3
def string_word_counter(string):
    split_string=string.split()
    count_dict={}
    for word in split_string:
        if word not in count_dict:
            count_dict[word]=1
        else:
            count_dict[word]+=1
    print(count_dict)

string="how many words many words words words"
string_word_counter(string)