# encoding
# bytes are sent over a network not data types( str, int, float)
# 1010101010



string_var = "something"

print(type(string_var))

string_var = str.encode(string_var)

print(type(string_var))

string_var = string_var.decode()

print(type(string_var))







