# list
colors = ['blue', 'red', 'yellow']
colors.append('green')
colors.extend(['black', 'white'])

# print(colors)
# colors.sort()
# print(colors)

# set
days = {'sunday', 'monday', 'monday', 'monday', 'monday', 'tuesday'}

print(days)
# print('monday' in days)
days.add('thursday')
# print(days)

# dictianery
grades = { 'Sam': 85, 'Bath': 95 }

print(grades['Sam'])
grades['Fred'] = 90
print(grades)
print(grades.keys())
print(grades.values())
