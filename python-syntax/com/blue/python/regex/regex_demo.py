import re

regex_string = '\\d+'

regex = re.compile(regex_string)

print(re.match('\\d*', 'abc') is not None)
print(re.match('\\d+', 'abc') is not None)
print(re.match('\\d*', '') is not None)
print(re.match('\\d*', 'az234g3d52c') is not None)
print(re.match('\\d+', 'az234g3d52c') is not None)
print(re.match('on', 'food on the table') is None)
print(re.match('foo', 'food on the table') is not None)

print(re.match('foo', 'food on the table').group())

print(re.search('\\d+', 'az234g3d52c').group())
print(regex.match('9az234g3d52c').group())
print(re.match(regex_string, '14').group())
