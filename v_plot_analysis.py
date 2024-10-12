import sys
import matplotlib.pyplot as plt

x, y = 1001, 501
arr = [[0 for _ in range(x)] for _ in range(y)]

for line in sys.stdin:
    data = line.split()
    row = int(data[1])
    column = int(data[0])
    arr[row][column+500] += 1

freq = arr

fig, ax = plt.subplots(figsize=(8, 6))

img = ax.imshow(freq, cmap='Blues', interpolation='nearest', extent=(-500, 500, 0, 500), vmin=0)

ax.set_xlabel('location of fragment length from the binding site')
ax.set_ylabel('length of fragment')
ax.set_title('v-plot analysis')

fig.colorbar(img, ax=ax)

ax.axis('tight')
ax.set_facecolor('white')
ax.invert_yaxis()  # Add this line to invert the y-axis

plt.savefig('v_plot.png', bbox_inches='tight')
plt.show()
