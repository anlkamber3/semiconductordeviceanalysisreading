import xlrd
from matplotlib import pyplot as plt
import math
data = xlrd.open_workbook("anil1.xls")
experiment = input("Which experiment do you want to analyze:")
version_Int_Experiment = int(experiment)

data_buffer = data.sheet_by_name(f"Append{experiment}")
values=[]
for i in range(1,data_buffer.nrows):
    buffer = abs(data_buffer.cell_value(rowx =i,colx=0))
    values.append(buffer)
voltages = []
for i in range(1,data_buffer.nrows):
    voltages.append(data_buffer.cell_value(rowx =i,colx=1))

plt.yscale(value = "log")

print(values)





plt.ylim(10**-13,10)
plt.plot(voltages,values)

plt.show()
