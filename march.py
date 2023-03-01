# page 6
lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# calcul de la moyenne
temp = 0
count = 0
for tab in lst:
    for t in tab:
        count += 1
        temp += t
        # print(t)
# print(temp, count)
calc = temp/count
print(calc)
# test = 1+2+3+4+5+6+7+8+9+10+11+12
# print(test)
# -------------------------------------------
# concat lists
lst_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
lst_names = ["jan", "feb", "mar", "apr", "may",
             "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
lst_month_count = []
i = 0
for day in lst_day:
    lst_month_count += [lst_names[i], lst_day[i]]
    i += 1
print(lst_month_count)
# -------------------------------
# add to object
i = 0
dic_month = {}
for day in lst_day:
    dic_month[lst_names[i]] = lst_day[i]
    i += 1
print(dic_month)
# ------------------------------------
# bisextil year
dic_month["feb"] = 29
print(dic_month)
# ---------------------------------
# without using max(), construct tool to return max number of list
interger_list = [12, 50, 20, 81, 92, 1, 7]
max_num = 0
for item in interger_list:
    if item >= max_num:
        max_num = item
    # print(item, max_num)

print("le nombre max : ", max_num)

# -------------------------------------
# construct tool to return 2list : 1 pair/ 2 impair
pair = []
imp = []
for item in interger_list:
    if item % 2 == 0:
        pair.append(item)
    if item % 2 == 1:
        imp.append(item)
print(pair, imp)
