web = set(["rahul", "vivek", "saidu", "venky"])
pyth = set(["vivek", "avinash", "smaran"])
print("Students in both web and python")
print (web.intersection(pyth))
inters = web.intersection(pyth)
only_web = web.difference(inters)
only_pyth = pyth.difference(inters)
print("Students not common in both classes")
no_inters = only_pyth | only_web
print(no_inters)




