
# Function to convert decimal number
# to binary using recursion
def DecimalToBinaryy(num):
    if num > 1:
        DecimalToBinaryy(num // 2)
    print(num % 2, end='')


# Driver Code
if __name__ == '__main__':
    # decimal value
    dec_val = 24

    # Calling function
    DecimalToBinaryy(dec_val)


DecimalToBinaryy(4)