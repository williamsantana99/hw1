# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '107061122.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:
      data.append(row)
     
#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.

first_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
second_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
third_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
fourth_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
fifth_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))

length1=len(first_data)
length2=len(second_data)
length3=len(third_data)
length4=len(fourth_data)
length5=len(fifth_data)

data1 = []
for j in range(length1):
  data1.append(first_data[j]['TEMP'])
data1_1 = []
data1_1=sorted(data1, reverse=True)

data2 = []
for k in range(length2):
  data2.append(second_data[k]['TEMP'])
data2_1 = []
data2_1=sorted(data2, reverse=True)

data3 = []
for m in range(length3):
  data3.append(third_data[m]['TEMP'])
data3_1 = []
data3_1=sorted(data3, reverse=True)

data4 = []
for n in range(length4):
  data4.append(fourth_data[n]['TEMP'])
data4_1 = []
data4_1=sorted(data4, reverse=True)

data5 = []
for p in range(length5):
  data5.append(fifth_data[p]['TEMP'])
data5_1 = []
data5_1=sorted(data5, reverse=True)

#=======================================

# Part. 4

#=======================================

# Print result

print('C0A880:',data2_1[0])
print('C0F9A0:',data3_1[0])
print('C0G640:',data4_1[0])
print('C0R190:',data5_1[0])
print('C0X260:',data1_1[0])

#========================================



