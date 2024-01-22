#generate multipication table of any number
fh = open('practical9.txt', 'w')
i = 1
number = int(input('Enter a number:'))

while i <= 10:
    fh.write(f"{number} X {i} = {number*i}\n")
    i += 1

fh.close()
