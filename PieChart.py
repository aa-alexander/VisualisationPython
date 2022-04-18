import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv("pie-data.tsv", delimiter="\t")
labels = data['Labels'].tolist()
values = data['Count'].tolist()
 
myexplode = [0, 0, 0, 0.1, 0, 0, 0]
colours = ['darkorange','teal','steelblue','royalblue','deeppink','gold','crimson']
 
fig, ax = plt.subplots()
values = data['Count'].tolist()
 
l = ax.pie(values, startangle=90, autopct='%.1f%%', explode = myexplode, shawdow = True, colors=colours)
 
for label, t in zip(labels, l[1]):
	x,y = t.get_position()
	angle = int(math.degrees(math.atan2(y,x)))
	ha = "left"
	
	if x<0:
		angle -= 180
		ha = "right"
	plt.annotate(label, xy=(x,y), rotation=angle, ha=ha, va="center", rotation_mode="anchor", size=8)
	
	
plt.savefig("pie-chart.png", dpi=1000)

