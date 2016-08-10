#Get ishadowsocks servers' password.

import sys, urllib.request

#defines
class ServerInfo:
	def __init__ (self, svr_name, svr_pwd_header):
		self.name = svr_name
		self.pwd_header = svr_pwd_header
		self.password = ""
		
password_string_header_len = 8
password_len = 8
password_file_name = 'ishadowsocks_passwords.txt'
url = "http://www.ishadowsocks.org/" #网页地址
us_svr_info = ServerInfo('US', 'A密码:')
hk_svr_info = ServerInfo('HK', 'B密码:')
jp_svr_info = ServerInfo('JP', 'C密码:')

def GetServerPassword(content, svr):
	find_str_index = content.find(svr.pwd_header.encode())
	start_index = find_str_index + password_string_header_len
	end_index = start_index + password_len

	t = content[start_index:end_index]

	if t.decode().isdigit():
		svr.password = t.decode()
		return True
	else:
		svr.password = ""
		return False

def BuildResultString(svr):
	if svr.name == "":
		tstr = svr.name + ' Server password not found' + '\n'
	else:
		tstr = svr.name + ' Server password is: ' + svr.password

	return tstr

#begin
result = ''
url_request = urllib.request.urlopen(url)
content = url_request.read()

svr_list = [us_svr_info, hk_svr_info, jp_svr_info]

for svr_item in svr_list:
	if GetServerPassword(content, svr_item):
		result = result + BuildResultString(svr_item) + '\n'

print(result)

#Write to file
psw_file = open(password_file_name, 'w+')
psw_file.write(result)
psw_file.close()
