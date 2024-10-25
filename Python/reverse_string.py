###  Input
string = "Test Automation Engineer Level"
print(string)
#### Out Put : reenignE noitamotuA tseT
def rev_str(data):
    rev=""
    for i in data:
        rev=i+rev
    print(rev)



#### Out Put : tseT noitamotuA reenignE
def rev_word_str(data):
    split_word=data.split()
    tmp_rev=[]
    for val in split_word:
        tmp_rev.insert(0,val[::-1])
    tmp_rev_data=tmp_rev[::-1]
    tmp_rev_data=" ".join(tmp_rev_data)
    print(tmp_rev_data)

rev_str(string)
rev_word_str(string)

