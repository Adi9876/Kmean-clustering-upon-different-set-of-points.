import numpy as np
import matplotlib.pyplot as plt 
import random

c2 = np.load("mild_4.npy")

# plt.scatter(c2[:,0],c2[:,1])

k1 = c2[random.randint(0,1000)]
k2 = c2[random.randint(0,1000)]
k3 = c2[random.randint(0,1000)]
k4 = c2[random.randint(0,1000)]
emp=[0,0]
def centroid(arr,emp):
	p,q=0,0
	for i in arr:
		p+=i[0]
		q+=i[1]
	x=p/len(arr)
	y=q/len(arr)
	emp[0],emp[1]=x,y 
	return np.array(emp)

for j in range(100):
		near_1 = []
		near_2 = []
		near_3= []
		near_4 = []

		for i in range(0,1000):
			a=np.linalg.norm(k1 - c2[i])
			b=np.linalg.norm(k2 - c2[i])
			c=np.linalg.norm(k3 - c2[i])
			d=np.linalg.norm(k4 - c2[i])
			if min(a,b,c,d) == a :
				near_1.append(list(c2[i]))
			if min(a,b,c,d) == b :
				near_2.append(list(c2[i]))
			if min(a,b,c,d) == c :
				near_3.append(list(c2[i]))
			if min(a,b,c,d) == d :
				near_4.append(list(c2[i]))

		# near_1.sort()
		# near_2.sort()
		# near_3.sort()
		# near_4.sort()
		near_1=np.array(near_1)
		near_2=np.array(near_2)
		near_3=np.array(near_3)
		near_4=np.array(near_4)

# scattering the points

		plt.scatter(near_1[:,0],near_1[:,1],color="orange",s=10)
		plt.scatter(near_2[:,0],near_2[:,1],color="green",s=10)
		plt.scatter(near_3[:,0],near_3[:,1],color="red",s=10)
		plt.scatter(near_4[:,0],near_4[:,1],color="grey",s=10)


# plotting the k's 
		
		plt.scatter(k1[0],k1[1],color="blue",s=99,marker="x")
		plt.scatter(k2[0],k2[1],color="red",s=99,marker="x")
		plt.scatter(k3[0],k3[1],color="green",s=99,marker="x")
		plt.scatter(k4[0],k4[1],color="black",s=99,marker="x")

		plt.savefig(str(j+1)+".png")
		plt.clf()
		

# new k's
		new_k1=centroid(near_1,emp)
		new_k2=centroid(near_2,emp)
		new_k3=centroid(near_3,emp)
		new_k4=centroid(near_4,emp)

		print(j)
		if k2[0]==new_k2[0] and k2[1]==new_k2[1] and k1[0]==new_k1[0] and k1[1]==new_k1[1] and k3[0]==new_k3[0] and k3[1]==new_k3[1] and k4[0]==new_k4[0] and k4[1]==new_k4[1]:
			break		
		
		k1=new_k1
		k2=new_k2
		k3=new_k3
		k4=new_k4
		
		
