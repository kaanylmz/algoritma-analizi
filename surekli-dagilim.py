import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt
n=10
p=0.3
k=np.arange(0,21)
binomial=binom.pmf(k,n,p)
binomial

plt.plot(k, binomial,'o-')
plt.title('Binomial: n=%i , p=%.2f' % (n,p),fontsize=15)
plt.xlabel('Number of successes')
plt.ylabel('Probability of successes', fontsize=15)
plt.show()


from scipy.stats import poisson
plt.ylabel('Probability of car passing')
plt.xlabel('Number of cars')
plt.title('Probability Distribution Curve')
arr = []
rv = poisson(25)
for num in range(0,40):
    arr.append(rv.pmf(num))
# print(rv.pmf(28))
prob = rv.pmf(28)
plt.grid(True)
plt.plot(arr, linewidth=2.0)
plt.plot([28], [prob], marker='o', markersize=6, color="red")
plt.show()


from scipy.stats import norm
mu =0
sigma = 1
x = np.arange(-5,5,0.1)

y=norm.pdf(x,0,1)
plt.plot(x,y)
plt.title('Normal: $\mu$=%.1f, $\sigma^2$=%.1f' % (mu,sigma))
plt.xlabel('x')
plt.ylabel('Probability density')
plt.show()



from scipy.stats import beta
a=0.5
b=0.5
x=np.arange(0.01,1,0.01)
y=beta.pdf(x,a,b)
plt.plot(x,y)
plt.title('Beta: a=%.1f, b=%.1f' % (a,b))
plt.xlabel('x')
plt.ylabel('Probability density')
plt.show()



from scipy.stats import expon
data=expon.rvs(scale=2,size=1000)
print ("mean: %g" % np.mean(data))
print ("SD: %g" % np.std(data, ddof=1))

plt.figure()
plt.hist(data, bins=20, normed=True)
plt.xlim(0,15)
plt.title("Simulating exponential random variables")
plt.show