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