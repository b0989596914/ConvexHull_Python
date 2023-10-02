import numpy as np
import matplotlib.pyplot as plt

def Turn_Right_Draw(para1, para2, para3):       # if 有 CCW turn
	if (para3[1] - para1[1]) * (para2[0] - para1[0]) >= (para2[1] - para1[1]) * (para3[0] - para1[0]):
		return 0
	return 1
	
def Convex_Hull(dot_array):
	dot_array.sort()			
	upper_line = [dot_array[0], dot_array[1]]	

	for i in range(2, len(dot_array)):
		upper_line.append(dot_array[i])
		while len(upper_line) > 2 and not Turn_Right_Draw(upper_line[-1], upper_line[-2], upper_line[-3]):
			del upper_line[-2]
	lower_line = [dot_array[-1], dot_array[-2]]

	for i in range(len(dot_array)-3,-1,-1):
		lower_line.append(dot_array[i])
		while len(lower_line) > 2 and not Turn_Right_Draw(lower_line[-1],lower_line[-2],lower_line[-3]):
			del lower_line[-2]
	del lower_line[0], lower_line[-1]
	
	return np.array(upper_line + lower_line)

enter_number = int(input("Enter Dot Number : "))

random_dot_array = [(np.random.randint(0,300), np.random.randint(0,300)) for i in range(enter_number)]
line_array = Convex_Hull(random_dot_array)
random_dot_array = np.array(random_dot_array)

# Draw plt
plt.figure()
plt.plot(line_array[:, 0], line_array[:, 1], 'b-', picker = 5)
plt.plot([line_array[-1, 0], line_array[0, 0]], [line_array[-1, 1], line_array[0, 1]], 'b-', picker = 5)
plt.plot(random_dot_array[:, 0], random_dot_array[:, 1],".r")
plt.show()