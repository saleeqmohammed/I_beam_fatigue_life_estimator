#!/usr/bin/env python
#author: Mohammed saleeq k
#print("importing environment...")
import os
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)
import subprocess
import sys
#print("importing csv parser...")
import csv
print("importing matplotlib...")
try:
    import matplotlib.pyplot as plt
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip","install",'matplotlib'])
finally:
    import matplotlib.pyplot as plt 
print("importing numpy...")
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable,"-m","pip","install",'numpy'])
finally:
    import numpy as np
print("importing rainflow algorithm...")
import rainflow as rf
print("            Data               ")
print("-------------------------------")
flm = 129
print("Fatigue load mean: {}".format(flm))
correction_factor = 0.4006
print("correction factor: {}".format(correction_factor))
sfd = 922
print("sigma f prime: {}".format(sfd))
b = 0.109
print(" SN constant b : {}".format(-b))
print("------------------------------")
print("Loading WISPER data...")
load_data = []
#Data entries
#sf = #enter sigma f prime or Sf
with open('load_spectrum.csv','r') as input_file:
    csv_reader = csv.reader(input_file)
    next(csv_reader)
    for line in csv_reader:
        load_data.append(float(line[1])*flm)  

# array of load points
array_ext = np.array(load_data)    
# calculate cycle counts with default values for lfm (0), 
#  uc_mult (0.5) count scaling
print("Excecuting rainflow counting...")
array_out = rf.rainflow(array_ext)
    
# sort array_out by cycle range
array_out = array_out[:,array_out[0,:].argsort()]
#arranging output data
print("arranging output data...")
Range = array_out[0]
Mean = array_out[1]
count = array_out[2]
rows=[]
i=0
for item in Range:
    row =[Range[i],Mean[i],count[i]]
    rows.append(row)
    #print(row)
    i+=1
print("saving rainflow counting results...")    
#writing to csv file
with open('rainflow_out.csv','w',newline='') as output_file:
    fieldnames = ['Range','Mean','Number of cycles']
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(fieldnames)
    i=0
    for row in rows:
        csv_writer.writerow(row)
        
print("Calculating SN curves...")
print("Estimating minor damage...")
#calculating sn curves and minor damage
Nf=[]
minor_damage =0
for row in rows:
    val = correction_factor*((sfd)-row[1])/(row[0]/2)
    Nfi=0.5*pow(val,1/b)
    minor_damage = minor_damage + (row[2]/Nfi)
    Nf.append(Nfi)
#print(Nf)
print("minor damage fraction : {}".format(minor_damage))
print("Number of blocks possible: {}".format(1/minor_damage))


print("Lifetime in years: {}".format((7.128611111111111/minor_damage)/8766))
print("plotting...")
print("press q to quit")
#plot the stess data for better visualization
plt.figure(1,figsize=(10,4))
plt.clf()   
plt.plot(load_data)
plt.grid('on')
plt.xlabel('Time')
plt.ylabel('Stress')
plt.title('Loding spectrum')
plt.tight_layout()
plt.show()
print("Exiting...")