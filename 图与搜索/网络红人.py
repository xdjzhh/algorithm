from collections import defaultdict
import copy
def fans(raw_team,team):
    if len(raw_team) == len(team):
        return team
        pass
    else:
        sublist = set(team) - set(raw_team)
        raw_team = copy.deepcopy(team)
        for each_member in sublist:
            team += team_dict[each_member]
        team = list(set(team))
        return fans(raw_team,team)



if __name__ == '__main__':
    total_member = 3
    total_pair = 3
    pair = '1 2 2 1 2 3'
    pair_list = pair.split(' ')
    print(pair_list)
    pairs = []
    for index in range(1,len(pair_list)+1):
        if index %2 != 0:
            each_pair = [pair_list[index - 1]]
        else:
            each_pair.insert(0,pair_list[index - 1])
            pairs.append(each_pair)
    print(pairs)
    dict_keys = set([item[0] for item in pairs])
    team_dict = {}
    for each in set(pair_list):
        team_dict[each] = [each]
    for each in pairs:
        team_dict[each[0]] = list(set(team_dict[each[0]] + each))
    print(team_dict)
    for each_key in team_dict.keys():
        team_dict[each_key] = fans([],team_dict[each_key])
    print(team_dict)
