f = open('log0709.txt', 'r')
list = f.readlines()
for line in list:
    if line != "@":
        print(line)
f.close()

print(list)

# f = open('log0708.txt', 'r')
# line = f.readline()
# lines = line.split("@")
# # print(lines)

# for methods in lines:
#     splitmethods = methods.split("/")
#     splitmethods.remove('')
#     print(splitmethods)
#     print(len(splitmethods))


# print(lines[0])
# methods = lines[0].split("/")
# print(methods)
# print(lines[1])
# print(lines[2])