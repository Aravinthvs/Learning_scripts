list = [1,1,2,3,4,5,5]

def find_dup(list):
    res = []
    seen = set()
    for i in list:
        if i in seen:
            res.append(i)
        else:
            seen.add(i)
    return res

print(f"duplicates in the list{find_dup(list)}")