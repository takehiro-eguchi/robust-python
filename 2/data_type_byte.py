from binascii import hexlify
from ctypes import string_at
from sys import getsizeof

a = 0b01010000_01000001_01010100
print(f"Direct = {a}")

# メモリに格納されている変数の中身を表示する
object_id = id(a)
a_str = string_at(object_id, getsizeof(a))
print(f"string = {a_str}")
hex_str = hexlify(a_str)
print(f"hex_str = {hex_str}")

text = "PAT"
text_id = id(text)
text_str = string_at(text_id, getsizeof(text))
text_hex_str = hexlify(text_str)
print(f"text_hex_str = {text_hex_str}")
