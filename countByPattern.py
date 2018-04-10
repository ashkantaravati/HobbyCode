import re
def SimpleReadFile(path):
    file=open(path)
    contents=file.read()
    return contents

def GetSumByPattern(pattern,input):
    found=re.findall(pattern,input)
    sum_of_found=0
    for i in found:
        sum_of_found=sum_of_found+int(i)
    return sum_of_found

def SimpleSumTotal(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i
    return sum

def AssertIntended(original,expected):
    if(expected==original):
        return 0
    else:
        return expected-original

def main():
    path=input('enter path\n')
    result=AssertIntended(GetSumByPattern(r'value = ([0-9]+)',SimpleReadFile(path)),SimpleSumTotal(1,200)*2)
    if(result==0):
        print('expectation is satisfied')
    else:
        print('{} difference'.format(result))

if __name__ == '__main__':
    main()