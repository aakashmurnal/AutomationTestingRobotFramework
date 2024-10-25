### Input
string = "Test Automation Engineer Level"
### Out Put : Get Each Char Count
def count_of_each_char(data):
    tmp={}
    for i in data:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
    print(tmp)

# count_of_each_char(string)
### Out Put : Get vowel count from given string
def count_of_vowel(data):
    vowel="aeiou"
    tmp_count={}
    for i in vowel:
        tmp_count[i]=data.count(i)
    print(tmp_count)

count_of_each_char(string)
count_of_vowel(string)

