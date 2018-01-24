import numpy as np
from numpy import reshape
from PIL import Image

###FOR CONVERTING IMAGE TO BIT ARRAY
#BNW IMAGE TO NUMPY ARRAY. RETURNS A NUMPY ARRAY OF THE IMAGE
def bnw_image_to_array(filename):
	img = Image.open(filename).convert("L")
	return np.array(img)

#Set viewable decimal places of numpy array
np_array_decimal_places = 2
np.set_printoptions(precision=np_array_decimal_places)
#Set filename of image
filename = "2_sese.png"

#call function then put numpy array into 'img_array_input'
img_array_input = bnw_image_to_array(filename)
#Invert the array
img_array_input = np.invert(img_array_input)
#Scale Down
img_array_input = img_array_input/255
print(img_array_input)

###FOR MAX POOLING
i = 0
j = 0
data = 0
#comparing values inside the matrix of the max pooling
def compare(tempdata,data):
	if data < tempdata:
		data = tempdata
	else:
		data = data
	return data
#max pooling of a 2x2 area inside the image
def max_pooling_area(matrix,i,j,data):
	data = matrix[i][j] #get data
	j=j+1
	tempdata = matrix[i][j]
	data = compare(tempdata,data)
	j=j-1
	i=i+1

	tempdata = matrix[i][j]
	data = compare(tempdata,data)

	j=j+1
	tempdata = matrix[i][j]
	data = compare(tempdata,data)
	return data

#max pooling of the whole image
def max_pooling(img_array_input,i,j,data):
	max_pooled_list = np.zeros((5,5))
	for x in range(0,5):
		for y in range (0,5):
			data = max_pooling_area(img_array_input,i,j,data)
			j = j+2
			max_pooled_list[x][y] = data
		j = 0
		i = i+2
	return max_pooled_list

print(max_pooling(img_array_input, i, j, data))
