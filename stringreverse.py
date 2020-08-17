def stringrev(n):
    str = ""
    for i in n:
        str = i + str
    return  str


n = 'emmanuel'
print("The original string  is : ", end="")
print(n)

print("The reversed string(using loops) is : ", end="")
print(stringrev(n))


