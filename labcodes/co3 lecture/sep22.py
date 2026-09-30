# poisson distribution histogram
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
# set the rate parameter (lambda) for the poisson distribution
lam = 4 # average number of events 
#generate poisson data 
data = np.random.poisson(lam, 1000) 
# plot histogram 
sns.histplot(data, kde=False,stat="density",bins=range(min(data),max(data)+1))
plt.title(f'Poisson Distribution Histogram (lambda={lam})')
plt.xlabel("Number of Events")
plt.ylabel("Density")
plt.show()
#--------------------------------------------------------------------------------------#
# Normal distribution histogram
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# set parameters for the normal distribution
mu = 0 # mean
sigma = 1 # standard deviation
# generate normal data
data = np.random.normal(mu, sigma, 1000)
# plot the KDE and histogram 
sns.histplot(data, kde=True, stat="density")
plt.title(f'Normal Distribution Histogram (mu={mu}, sigma={sigma})')
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
#--------------------------------------------------------------------------------------#
# uniform distribution histogram
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# set parameters for the uniform distribution
low = 0 # lower bound
high = 10 # upper bound
# generate uniform data
data = np.random.uniform(low, high, 1000)
# plot the KDE and histogram
sns.histplot(data, kde=True, stat="density")
plt.title(f"Uniform Distribution ({low}, {high})")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
#--------------------------------------------------------------------------------------#
# exponential distribution histogram
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
# set the rate parameter lambda 
lam = 1.5
# generate exponential data
data = np.random.exponential(1/lam, 1000)
# plot the KDE and histogram
sns.histplot(data, kde=True, stat="density")
plt.title(f"Exponential Distribution Histogram (lambda={lam})")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
#--------------------------------------------------------------------------------------#
