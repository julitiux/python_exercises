#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#    print(contents)

#filename = 'pi_digits.txt'
#with open(filename) as file_object:
#    for line in file_object:
#        print(line.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
#get all content of file and get it in a list
print(lines)
for line in lines:
    print(line.rstrip())
