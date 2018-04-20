# Boyer Moore String Search implementation in Python
# Ameer Ayoub <ameer.ayoub@gmail.com>

# Generate the Bad Character Skip List
import csv
import sys
def generateBadCharShift(term):
    skipList = {}
    for i in range(0, len(term)-1):
        skipList[term[i]] = len(term)-i-1
    return skipList

# Generate the Good Suffix Skip List
def findSuffixPosition(badchar, suffix, full_term):
    for offset in range(1, len(full_term)+1)[::-1]:
        flag = True
        for suffix_index in range(0, len(suffix)):
            term_index = offset-len(suffix)-1+suffix_index
            if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                pass
            else:
                flag = False
        term_index = offset-len(suffix)-1
        if flag and (term_index <= 0 or full_term[term_index-1] != badchar):
            return len(full_term)-offset+1

def generateSuffixShift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = findSuffixPosition(key[len(key)-1-i], buffer, key)
        buffer = key[len(key)-1-i] + buffer
    return skipList
    
# Actual Search Algorithm
def BMSearch(haystack, needle):
    goodSuffix = generateSuffixShift(needle)
    badChar = generateBadCharShift(needle)
    i = 0
    while i < len(haystack)-len(needle)+1:
        j = len(needle)
        while j > 0 and needle[j-1] == haystack[i+j-1]:
            j -= 1
        if j > 0:
            badCharShift = badChar.get(haystack[i+j-1], len(needle))
            goodSuffixShift = goodSuffix[len(needle)-j]
            if badCharShift > goodSuffixShift:
                i += badCharShift
            else:
                i += goodSuffixShift
        else:
            return i
    return -1

def main():
            
    while(1):
        choice = input("Do you want to enter college name(n)/college area(a)/college fees(f)/exit(e) :")
        if choice == 'a':
            address = input("Enter the address to be searched :")
            with open('collegedata.csv', 'r') as f:
                reader = csv.reader(f)
                your_list = list(reader)
            header = your_list[0]
            your_list = your_list[1:]    
            for each in your_list:
                if BMSearch(str(each[2]).lower(), address.lower()) >= 0:
                    for i, each1 in enumerate(each):
                        print (header[i],"|:", each1)
                    print("\n\n")

        if choice == 'n':
            name = input("Enter the name to be searched :")
            with open('collegedata.csv', 'r') as f:
                reader = csv.reader(f)
                your_list = list(reader)
            header = your_list[0]
            your_list = your_list[1:]
            for each in your_list:
                if BMSearch(str(each[1]).lower(), name.lower()) >= 0:
                    #each[2] = each[2][9:]
                    for i, each1 in enumerate(each):
                        print (header[i],"|:", each1)
                    print("\n\n")

                    print()
        if choice == 'f':
            fees = input("Enter the fees :")
            with open('collegedata.csv', 'r') as f:
                reader = csv.reader(f)
                your_list = list(reader)
            header = your_list[0]
            your_list = your_list[1:]
            for each in your_list:
                found = False
                for each3 in each[-6:]:
                    try:
                        if int(each3[1:].replace(',','')) <= int(fees):
                            print(int(each3[1:].replace(',','')))
                            found = True
                    except:
                        continue
                if found == True:
                    #each[2] = each[2][9:]
                    for i, each1 in enumerate(each):
                        print (header[i],"|:", each1)

                    print("\n\n")
        if choice == 'e':
            sys.exit()
main()
