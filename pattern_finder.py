#two indecies in a for loop

def main():
    str_input = "aabababaaaba"
    pattern = "abab"
    count = 0
    for i in range(len(str_input)):
        if str_input[i:i + len(pattern)] == pattern:
            count += 1
    print(count)

def Repeating(str_input):
    print("test")



def NonRepeating(str_input, pattern):
    
    pat_indxs = []
    currStr = ""

    pat_len = len(pattern)
    pat_indx = 0

    for i in range(len(str_input)):    

        if pattern[pat_indx] == str_input[i]:
            currStr += str_input[i]
            pat_indx += 1
        else:
            currStr = ""
            pat_indx = 0

        if currStr == pattern:
            print("\"" + pattern + "\" found at index: " + str(i - (pat_len - 1)))
            pat_indx = 0
            currStr = ""    


    

if __name__ == "__main__":
    main()