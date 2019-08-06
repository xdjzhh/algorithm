def rotation(string):
    length = len(string)
    if length == 1 :
        return string
    else:
        if length%2 == 0 :
            left =  string[:length//2]
            right = string[length//2:length]
            left_rotation = rotation(left)
            right_rotation = rotation(right)
            new_string = right_rotation + left_rotation
            return new_string
        else:
            left =  string[:length//2]
            mid = string[length//2]
            right = string[length//2 + 1:length]
            left_rotation = rotation(left)
            right_rotation = rotation(right)
            new_string = right_rotation + mid + left_rotation
            return new_string

if __name__ == '__main__':
    print(rotation('aaaaaaaadssssssss'))

