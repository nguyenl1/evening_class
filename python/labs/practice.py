# try:
#     f = open("./practice.txt")
#     contents = f.read()
#     print(contents)
# except (IOError, OSError) as e:
#     print(e)
# finally:
#     f.close()

import csv
import matplotlib.pyplot as plt 

with open("./practice.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0

    x= []
    y = []

    for row in csv_reader: 
        if line_count == 0:
            line_count += 1
        else:
            x.append(row[0])
            y.append(row[1])
            line_count += 1

plt.scatter(x,y)
plt.show()
        
