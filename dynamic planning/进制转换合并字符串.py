

string = input().strip().split()
string = string[0] + string[1]

string_even = sorted(list(string[::2]))
string_odd = sorted(list(string[1::2]))
print(string_odd,string_even)

def change(i):

    enc_str = '1234567890abcdefABCDEF'

    if i in enc_str:
        int_i = int(i, 16)
        revers_b = '{:04b}'.format(int_i)[::-1]
        chr_i = hex(int(revers_b, 2)).replace('0x', '')
        if chr_i.isalpha():
            result = chr_i.upper()
        else:
            result = chr_i
    else:
        result = i
    return result


newstring = ''
for i in range(len(string)):
    if i%2 == 0:
        char = string_even.pop(0)
        newstring+=change(char)
    else:
        char = string_odd.pop(0)
        newstring += change(char)

print(newstring)
