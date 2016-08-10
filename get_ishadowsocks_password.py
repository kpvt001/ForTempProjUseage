#Get ishadowsocks servers' password.

import sys, urllib.request

class ServerInfo:
	def __init__ (self, svr_name, svr_pwd_header):
		self.name = svr_name
		self.pwd_header = svr_pwd_header
		self.password = ""



#defines
password_string_header_len = 8
password_len = 8
us_password_header = 'A密码:'
hk_password_header = 'B密码:'
jp_password_header = 'C密码:'



us_name = 'US'
hk_name = 'HK'
jp_name = 'JP'
password_file_name = 'ishadowsocks_passwords.txt'
url = "http://www.ishadowsocks.org/" #网页地址

us_svr_info = ServerInfo('US', 'A密码:')
hk_svr_info = ServerInfo('HK', 'B密码:')
jp_svr_info = ServerInfo('JP', 'C密码:')

result = ''

url_request = urllib.request.urlopen(url)
content = url_request.read()

# Get US server password
find_str_index = content.find(us_password_header.encode())

start_index = find_str_index + password_string_header_len
end_index = start_index + password_len
t = content[start_index:end_index]

svr_name = us_name
if t.decode().isdigit():
	svr_ret = svr_name + ' Server password is: ' + t.decode()
else:
	svr_ret = svr_name + ' Server password not found'
result = result + svr_ret +'\n'
print(svr_ret)

# Get HK server password
find_str_index = content.find(hk_password_header.encode())

start_index = find_str_index + password_string_header_len
end_index = start_index + password_len
t = content[start_index:end_index]

svr_name = hk_name
if t.decode().isdigit():
	svr_ret = svr_name + ' Server password is: ' + t.decode()
else:
	svr_ret = svr_name + ' Server password not found'
result = result + svr_ret +'\n'
print(svr_ret)

# Get JP server password
find_str_index = content.find(jp_password_header.encode())

start_index = find_str_index + password_string_header_len
end_index = start_index + password_len
t = content[start_index:end_index]

svr_name = jp_name
if t.decode().isdigit():
	svr_ret = svr_name + ' Server password is: ' + t.decode()
else:
	svr_ret = svr_name + ' Server password not found'
result = result + svr_ret +'\n'
print(svr_ret)


#Write to file
psw_file = open(password_file_name, 'w+')
psw_file.write(result)
psw_file.close()


def GetServerPassword(content, svr):
	find_str_index = content.find(svr.pwd_header.encode())
	start_index = find_str_index + password_string_header_len
	end_index = start_index + password_len

	t = content[start_index:end_index]

	if t.decode().isdigit():
		svr.password = t.decode()
	else:
		svr.password = ""
		
	return t.decode()
