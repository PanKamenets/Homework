list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
list2 = []
for item in list:
    for k in item.values():
        list2.append(k)
endlist = set(list2)
print(endlist)

