def menu(starter,meal,dessert):
    d={
        "starter-item":starter,
        "meal-food":meal,
        "sweets/dessert":dessert
    }
    print("We offer starter as {}, meal as {} and desserts as{}".format(starter,meal,dessert))

def menuWithOwner(name,*items):
    print("We are from {}".format(name))
    for item in items:
        print(item)

menu("Soup","Pulao-daal makhni","Moongdaal halwa")
menuWithOwner("AnnapurnaCatterings","Soup","Chinese","Pulao","Daal makhni","Rasgulla")