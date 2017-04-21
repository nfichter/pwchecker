def helper(lower_char,upper_char,password):
    return [True if ord(char) >= ord(lower_char) and ord(char) <= ord(upper_char) else False for char in password]

def check_pw(password):
    lower = False
    upper = False
    num = False
    ll = helper('a','z',password)
    lower = True in ll
    ul = helper('A','Z',password)
    upper = True in ul
    nl = helper('0','9',password)
    num = True in nl
    return lower and upper and num

print "Wrong :",check_pw("Wrong")
print "wrong1:",check_pw("wron1")
print "WRONg1:",check_pw("WRON1")
print "Right1:",check_pw("Right1")

def check_pw_scale(password):
    bool_list = [False,False,False,False]
    ll = helper('a','z',password)
    bool_list[0] = True in ll
    ul = helper('A','Z',password)
    bool_list[1] = True in ul
    nl = helper('0','9',password)
    bool_list[2] = True in nl
    el = helper('!','.',password)
    bool_list[3] = True in el
    return (10.0/len(bool_list))*bool_list.count(True)

print "bad    :",check_pw_scale("bad")
print "Wrong  :",check_pw_scale("Wrong")
print "wrong1 :",check_pw_scale("wron1")
print "WRONg1 :",check_pw_scale("WRON1")
print "Right1 :",check_pw_scale("Right1")
print "Right1$:",check_pw_scale("Right1&")
