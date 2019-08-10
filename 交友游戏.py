import copy

def choose(raw_team,team):
    if len(raw_team) == len(team):
        return team
        pass
    else:
        sublist = list(set(team) - set(raw_team))
        raw_team = copy.deepcopy(team)
        for each in sublist:
            index_list.remove(each)
            team += newlist[each-1]
        team = list(set(team))
        print(f'raw_team {raw_team}')
        print(f'team {team}')
        return choose(raw_team,team)


if __name__ == '__main__':
    raw_list = [[],[5,3],[8,4],[9],[9],[3],[],[7,9],[],[9,7]]
    newlist = copy.deepcopy(raw_list)
    print(newlist)
    index_list = [1,2,3,4,5,6,7,8,9,10]
    for index in range(len(index_list)):
        newlist[index].append(index + 1)
        for i in raw_list[index]:
            if index + 1 not in newlist[i-1]:
                newlist[i-1].append(index + 1)
    print(newlist)
    team_count = 0
    while len(index_list) !=0:
        item = index_list.pop(0)
        item_index = item - 1
        team = []

        if len(newlist[item_index]) == 1:
            team.append(item)
        else:
            team.append(item)
            team = choose(team,newlist[item_index])

        team_count += 1
        print(team)
    print(team_count)