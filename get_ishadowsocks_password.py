#Get ishadowsocks servers' password.

import sys, urllib.request

class ServerInfo:
	def __init__ (self, svr_name, svr_pwd_header):
		self.name = svr_name
		self.pwd_header = svr_pwd_header
		self.password = ""

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

#defines
password_string_header_len = 8
password_len = 8
password_file_name = 'ishadowsocks_passwords.txt'
url = "http://www.ishadowsocks.org/" #网页地址

us_svr_info = ServerInfo('US', 'A密码:')
hk_svr_info = ServerInfo('HK', 'B密码:')
jp_svr_info = ServerInfo('JP', 'C密码:')

result = ''

url_request = urllib.request.urlopen(url)
content = url_request.read()

# Get US server password

if GetServerPassword(content, us_svr_info):
	result = result + BuildResultString(us_svr_info) + '\n'

# Get HK server password

if GetServerPassword(content, hk_svr_info):
	result = result + BuildResultString(hk_svr_info) + '\n'

# Get JP server password
if GetServerPassword(content, jp_svr_info):
	result = result + BuildResultString(jp_svr_info) + '\n'

print(result)

#Write to file
psw_file = open(password_file_name, 'w+')
psw_file.write(result)
psw_file.close()
