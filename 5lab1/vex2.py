from matplotlib import pyplot

#1. Prepare data
machin_counts = [18, 4, 2]

#2. Prepare labels
machin_names = ['PC', "MAC", "Linux"]

#3. Draw pie
pyplot.pie(machine_counts, label= machine_names, autopct="%.1f%%",shadow=True,explode=[0,0.05,0])
pyplot.axis("equal")
pyplot.title('PC vs MAC vs Linux usage')
#4. Show
pyplot.show()