def all_about_me(info):
    for key, value in info.iteritems():
        print "My " + key + " is " + value 

sam = {"name" : "Sam", "hometown" : "Denver", "age": "20", "favorite color" : "purple"}

all_about_me(sam)
