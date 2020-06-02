# coding=utf-8
w_len = 10
result = ""
str_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
length = len(str_list)
for i in xrange(w_len):
	result+="0 "
	result+=str(length-1)
	result+=" "
	result+="0 "
	result+=str(length-1)
	result+=" "
sstr = "CHFV"
for i in sstr:
	result+=str(str_list.index(i))
	result+=" "
	result+=str(str_list.index(i))
	result+=" "
	result+="0 "
	result+=str(length-1)
	result+=" "
print result
