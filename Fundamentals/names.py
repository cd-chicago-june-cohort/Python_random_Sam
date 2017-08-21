def print_names(lst):
    for i in range(len(lst)):
        print lst[i]["first_name"], lst[i]["last_name"]

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#print_names(students)

def print_names_two(users):
    for key, value in users.iteritems():
        print key
        for i in range(len(value)):
            print str(i+1) + " - " + value[i]["first_name"] + " " + value[i]["last_name"] + " - " + str(len(value[i]["first_name"]) + len(value[i]["last_name"]))


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print_names_two(users)