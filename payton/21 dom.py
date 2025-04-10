f = open("test5.txt", "w")
f.write("Замена строки в текстовом файле; \n изменить строку в списке; \n записать список в файл;")
f.close()

f = open("test3.txt", "r")
read_line = f.readlines()
print(read_line)
f.close()

pos1 = int(input("pos1 = "))
pos2 = int(input("pos2 = "))

if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
    read_line[pos1], read_line[pos2] = read_line[pos2],  read_line[pos1]
else:
    print("Такой строки нет")
