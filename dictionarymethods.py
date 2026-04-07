college={
    "name":"GEC Aurangabad",
    "principal":"Dr. Prashant Mani",
    "dept":["CSE","IT","ELECTRICAL","MECHANICAL"],
    "established":2020,
    1:"Python",
    2:"ML"
}
print(college)
print(type(college))
print(f"Name of the college is {college['name']}")
print(f"Principal of the college is {college['principal']}")
print(f"Departments in the college are {college['dept']}")
print(f"I am a student of {college['dept'][0]} department")

# trying to update a value using key
college["name"]="Government Engineering College Aurangabad"
print(college['name'])
# trying to add a new key value pair
college["location"]="Rafiganj, Aurangabad"
print(f"Location is {college['location']}")

#dictionary methods
print(college.keys())
print(college.values())

keys=["Bihar ranking","State ranking","National ranking"]
values=[22,2568,123456]
m=college.fromkeys(keys,"Unknown")
print(m)
print(college.clear())

#trying to update a key, or replace a key
# college['Availablebranches']=college['dept']
# del college['dept']
# print(college)
# print("Key updated successfully")