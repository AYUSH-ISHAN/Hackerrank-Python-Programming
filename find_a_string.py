def count_substring(string, sub_string):
    count = 0
    len_sub_str = len(sub_string)
    # string[i:i+len_sub_str]
    for i in range(0, len(string)-len_sub_str+1):
        dummy_str = string[i:i+len_sub_str]
        if sub_string == dummy_str:
            count += 1
    
    return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)