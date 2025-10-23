#file = open(r"files/essay.txt", "r")
#contents = file.readlines()
#file.close()
#length=0
#for content in contents:
#    length = length+(len(content))
#print(f"the file contains {length} characters")


#file = open("file.txt",'w')
#file.writelines("snail")
#file.close()

#countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
#filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
#for country, filename in zip(countries, filenames):
#    with open(f"{filename}", "w") as file:
#        file.write(country)



#countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
#for country in countries:
#    with open(f"{country}.txt", "w") as file:
#        file.write(country)
#file.close()

new_member = input("Enter new member name: ")
file = open(r"files/members.txt", "a")
file.write(new_member+"\n")
file.close()


file = open(r"files/members.txt", "r")
contents = file.readlines()
file.close()
print("Current members:")
for content in contents:
    print(content.strip())
