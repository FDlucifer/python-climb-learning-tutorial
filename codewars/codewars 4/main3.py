# Simple Fun #112: Array Erasing

def array_erasing(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 1
    consequtive_streaks = []
    idx = 0
    while idx < len(lst) - 1:
        if lst[idx] == lst[idx + 1]:
            opposite = 0 if lst[idx] == 1 else 1
            if opposite in lst[idx:]:
                opposite_index = lst[idx:].index(opposite) + idx
                consequtive_streaks.append((idx, opposite_index - 1))
                idx = opposite_index
            else:
                consequtive_streaks.append((idx, len(lst) - 1))
                idx = len(lst) - 1
        else:
            idx += 1
    if consequtive_streaks == []:
        if len(lst) > 2:
            return 1 + array_erasing(lst[0:0] + lst[2:])
        else:
            return 2
    steps = []
    for streak in consequtive_streaks:
        steps.append(1 + array_erasing(lst[:streak[0]] + lst[streak[1]+1:]))
    return min(steps)