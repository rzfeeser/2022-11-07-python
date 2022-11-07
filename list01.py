#!/usr/bin/python3

# create an empty list
mylist = []


# dir([])
# dir(list)
# mylist = []
# dir(mylist)
# help(mylist.append) <- when asking for help DO NOT add trailing ()


mylist.append("time") # the () means "call this"
mylist.append("for")
mylist.append("lunch")

print(mylist)

# display JUST the first position
print(mylist[0])

people = [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}]

print(people[0])

