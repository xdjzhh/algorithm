import re


def change(dict_character):
    for i in dict_character:
        if isinstance(dict_character[i],str):
            all_split = []
            member = []
            flag = 0
            int_flag = 0
            for j in dict_character[i]:
                if j == '{':
                    int_flag = 1
                    continue
                if j == '}':
                    int_flag = 0
                    all_split.append(int(''.join(m for m in member)))
                    member = []
                if j == '[':
                    flag = 1
                if j == ']':
                    flag = 0
                    member.append(j)
                    all_split.append(''.join(m for m in member))
                    member = []
                if (flag == 1) or (int_flag == 1):
                    member.append(j)
                if j in ['+','-','*','/']:
                    all_split.append(j)
            dict_character[i] = all_split
    return dict_character

def check(dict_character):
    all_count = 0
    for i in dict_character:
        if not isinstance(dict_character[i],int):
            all_count+=1
            count = len(dict_character[i])
            for index in range(len(dict_character[i])):
                if dict_character[i][index] in ['+','-','*','/']:
                    count-=1
                elif isinstance(dict_character[i][index],int):
                    count-=1
                else:
                    if isinstance(dict_character[dict_character[i][index]],int):
                        dict_character[i][index] = dict_character[dict_character[i][index]]
                        count -= 1
                if count == 0:
                    string = ''.join(str(term) for term in dict_character[i])
                    dict_character[i] = eval(string)
                    all_count-=1
    if all_count == 0:
        return dict_character
    else:
        return check(dict_character)








if __name__ == '__main__':
    string = input().split(';')
    formula = string[0]
    character = string[1]
    formula_list = formula.split(',')
    character_list = character.split(',')

    print(formula_list)
    print(character_list)

    dict_character = {}
    for i in character_list:
        a = re.match(r'(\[\d+\])=(\d+)',i)
        item = a.groups()
        dict_character[item[0]] = int(item[1])
    print(dict_character)

    for j in formula_list:
        a = re.match(r'(\[\d+\])=(.+)', j)
        dict_character[a.group(1)] = a.group(2)

    dict_character = change(dict_character)
    print(dict_character)
    dict_character = check(dict_character)

    print(dict_character)

#[1234]=[12]+[34]+[123]/{5},[123]=[12]+[34];[12]=4,[34]=5