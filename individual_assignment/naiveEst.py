print('Loading files.....')
#getting input from file data.txt
inputFile = open("data.txt", "r")

#writing output to the file output.txt
outputFile = open("output.txt", "a")

#reading the first line to get the values of m and n
firstLine = inputFile.readline()
commaIndex = firstLine.index(',')
n = int(firstLine[0:commaIndex])
m = int(firstLine[commaIndex+1:])
print("m={} n={} \n".format(m,n))

# 2D Array holding the data from the input file
data = []

#loop for transferring data from the file to the 2D Array
for x in inputFile:
  dataString = x.split(' ')     #splitting into constituent elements
  toNumbers = [float(n) for n in dataString]    #converting elements to float
  data.append(toNumbers)    #adding the float elements to the 2D array

# Initializing Volume as bin_width ^ m
bin_width = 2.0 # has been given 2 in the question
volume = 2 ** m
print('Volume= {} \n'.format(volume))

#loop referring to the instance under consideration
for X in range(len(data)):
    count = 0 # counts the number of instances in the same hyperplane as X
    for i in range(len(data)):
        flag = 0
        for j in range(len(data[i])):
            if(max(data[i][j],data[X][j])-min(data[i][j],data[X][j])<1):
                flag+=1
        if(flag == len(data[i])):
            count+=1

    probability = count/(volume*n)  # calculating probability using count, volume, n

    print('Append probability to output file.....')
    outputFile.write(str(probability)+'\n') # Writing the calculated probability to output file
    print('Count = {} Probability = {}'.format(count,probability))
    print("next X ------>\n")

print('Closing files.....')
inputFile.close()
outputFile.close()