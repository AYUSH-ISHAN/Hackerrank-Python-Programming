def fun(s):
    # return True if s is a valid email, else return False
    count = 0
    #  checking part for '@' and '.'..
    for i in s:
        if i == '@' or i == '.':
            count += 1
            if count > 2:
                return False
    if count < 2:
        return False
    username_part = s.split('@')  # list have [username, rest part]
    if len(username_part) == 2:
        username = username_part[0]
        rest_part = username_part[1]
    else:
        return False
    ext_part = rest_part.split('.')
    if len(ext_part) == 2:
        extension = ext_part[1]
        website = ext_part[0]

    else:
        return False
    if len(extension) > 3:
        return False
    if len(website) == 0 or len(username) == 0 or len(extension) == 0:
        return False
    ## yaha tak sab sahi hai..

    # ord('h')  use this for ascii values

    ##  checking for username :
    for i in username:
        asc = ord(i)
        if 97 <= asc <= 122:  # small letters
            pass
        elif 65 <= asc <= 90:  # capital letters
            pass
        elif 48 <= asc <= 57:  # numbers
            pass
        elif asc == 95 or asc == 45:  # hphens and dash...
            pass
        else:
            return False

    ## checking website part ..

    for i in website:
        asc = ord(i)
        if 97 <= asc <= 122:  # small letters
            pass
        elif 65 <= asc <= 90:  # capital letters
            pass
        elif 48 <= asc <= 57:  # numbers
            pass
        else:
            return False

    # extension part

    for i in extension:
        asc = ord(i)
        if 97 <= asc <= 122:  # small letters
            pass
        elif 65 <= asc <= 90:  # capital letters
            pass
        else:
            return False
    return True


#def filter_mail(emails):