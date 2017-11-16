#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# basic_types.py

intValue = 1
print(intValue)

intValue2 = 0x2
print(intValue2)

floatValue = 1.3
print(floatValue)

boolValue1 = True
boolValue2 = False
print('\nboolValue1:', boolValue1)
print('boolValue2:', boolValue2)
print("bool equal?", boolValue1 == boolValue2)
print('bool and?', boolValue1 and boolValue2)
print('bool or?', boolValue1 or boolValue2)
print('bool not?', not boolValue2 == boolValue1)

nullValue = None
print("\nNone value:", nullValue)

strValue1 = 'hello'
print("\n" + strValue1)

strValue2 = r"I'm from China.\n"
print(strValue2)

strValue3 = 'I\'m hungry.\n'
print(strValue3)

strValue4 = '''My name is Haha. I'm from Beijing, China.
I'm so glad to meet you guys here.
Thank you very much!\n'''
print(strValue4)

strValue5 = r'''My name is Hey. \nI'm from Beijing, China.
I'm so glad to meet you guys here.
Thank you very much!\n'''
print(strValue5)


print("\nord('a') =", ord('a'))
print("ord('一') =", ord('一'))
print("chr(98) =", chr(98))
print("chr(20108) =", chr(20108))
print("\u4e2d\u6587\n")

print('abc'.encode('ascii'))
print('abc中文'.encode('utf-8'))
print(b'abc'.decode('ascii'))
print(b'abc\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print('\n')
print("len('ABC') =", len('ABC'))
print("len('中文') =", len('中文'))
print("len('中文'.encode('utf-8')) =", len('中文'.encode('utf-8')))

print('\n')
print('My name is %s' % 'Hello')
print("1 + 1 = %d, 3 / 2 = %f, 3 // 2 = %.2f, hex(32)=0x%04x" % (1 + 1, 3 / 2, 3 // 2, 32))
print("{0}'s height is {1:.2f}m".format("Tom", 1.835))