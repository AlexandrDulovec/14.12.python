import os
file = open("names.txt", "rt")



data = file.read()
category = data.split()


for x in category:
    category.count("/a/")
    category.count("/b/")
    category.count("/c/")
    category.count("/d/")


print(category.count("/a/"))
print(category.count("/b/"))
print(category.count("/c/"))
print(category.count("/d/"))