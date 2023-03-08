# # 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

# 2. Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    i = 0
    while i < len(some_list):
        for each_key in some_list[i]:
            print(each_key + " - " + some_list[i][each_key])
        i += 1

def iterateDictionaryRedux(some_list):
    for each_index in some_list:
        for each_key in each_index:
            print(each_key + " - " + each_index[each_key])

iterateDictionaryRedux(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    i = 0
    while i < len(some_list):
        print(some_list[i][key_name])
        i += 1

def iterateDictionary2Redux(keyname, some_list):
    for full_name in some_list:
        print(full_name[keyname])

iterateDictionary2Redux('first_name', students)
iterateDictionary2Redux('last_name', students)


# # 4. Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for each_key in some_dict:
        print(len(some_dict[each_key]), each_key.upper())
        i = 0
        while i < len(some_dict[each_key]):
            print (some_dict[each_key][i])
            i += 1
        print()

def printInfoRedux(some_dict):
    for each_key in some_dict:
        print(len(some_dict[each_key]), each_key.upper())
        for i in some_dict[each_key]:
            print(i)
        print()

printInfoRedux(dojo)