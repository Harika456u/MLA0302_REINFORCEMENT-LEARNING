import numpy as np
import matplotlib.pyplot as plt

# Grid size
rows = 4
cols = 4

gamma = 0.9

reward = -1

goal = (3,3)

obstacles = [(1,1),(2,2)]

V = np.zeros((rows,cols))

actions = [(-1,0),(1,0),(0,-1),(0,1)]

iterations = 100

for _ in range(iterations):

    newV = V.copy()

    for i in range(rows):
        for j in range(cols):

            if (i,j)==goal:
                newV[i,j]=10
                continue

            if (i,j) in obstacles:
                continue

            values=[]

            for dx,dy in actions:

                ni=i+dx
                nj=j+dy

                if 0<=ni<rows and 0<=nj<cols and (ni,nj) not in obstacles:
                    values.append(reward+gamma*V[ni,nj])

            if values:
                newV[i,j]=max(values)

    V=newV

print("State Value Function\n")
print(np.round(V,2))

plt.imshow(V,cmap='viridis')

plt.colorbar(label="State Value")

for i in range(rows):
    for j in range(cols):
        if (i,j)==goal:
            plt.text(j,i,"G",ha='center',color='white',fontsize=12)
        elif (i,j) in obstacles:
            plt.text(j,i,"X",ha='center',color='red',fontsize=12)
        else:
            plt.text(j,i,round(V[i,j],1),ha='center',color='white')

plt.title("Warehouse Robot Value Function")
plt.show()
