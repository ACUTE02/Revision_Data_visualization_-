import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import seaborn as sns
x=np.linspace(0,5,5)
# print(x)
y=x**2
# print()
# print(y)
# plt.plot(x,y)
# plt.xlabel("chacha...")
# plt.ylabel("chachaaaaaaaaaa...")
# plt.show()  

'''SUBPLOT'''
# plt.subplot(2,2,1)
# plt.plot(x*2,y)
# plt.subplot(2,2,4)
# plt.plot(x,y)
# plt.subplot(2,2,3)
# plt.plot(y,x)
# plt.subplot(2,2,2)
# plt.plot(x**2,x**2)
# plt.show()

'''Obejct oriented '''
# Object Oriented way

# Matplotlib allows the aspect ratio, DPI and figure size to be specified when the Figure object is created. 
# You can use the figsize and dpi keyword arguments.
# figsize is a tuple of the width and height of the figure in inches dpi is the dots-per-inch (pixel per inch).

# fig=plt.figure(figsize=(10,8),dpi=100)
# axes1=fig.add_axes([0.1,0.1,1,1])
# axes1.plot(x,y)
# axes2=fig.add_axes([0.3,0.4,0.3,.3])
# axes2.plot(y,x)
# plt.show()
# between 0 to 1 we can provide
# [[0.3,0.4,0.3,.3] 0.3=width,0.3=height ,left=0.3,bottom = 0.4 


'''Saving the plot'''
# fig=plt.figure()
# axis=fig.add_axes([0.1,0.1,0.8,0.8])
# axis.plot(x,y)
# plt.savefig("thegameoftatti")
# plt.show()
'''working with the images '''


# img=mpimg.imread("vaidika.jpeg")
# plt.imshow(img)
# plt.axis("off")
# plt.show()

# crop=img[1000:1200,200:800]
# plt.imshow(crop)
# plt.axis("off")
# plt.show()


'''type of plot '''
# plt.scatter(x,y)
# plt.show()
# from random import sample
# data = sample(range(1,1000),100)
# plt.hist(data)
# plt.show()

# plt.boxplot(x)
# plt.show()


'''Distribution plot '''
'''We use distribution plots to visualize the distribution of quantitative data.

Let's discuss some plots that allow us to visualize the distribution of a data set. These plots are:

distplot/histplot
jointplot
pairplot
rugplot'''
# df=sns.load_dataset("tips")
# print(df)
# print(df['size'].unique())

# plt.subplot(1,2,1)
# sns.histplot(df["total_bill"],bins=20,kde=True)
# plt.subplot(1,2,2)
# sns.histplot(df['tip'],bins=20,kde=True)
# plt.show()

'''Join plot compare ke liyee'''
# sns.jointplot(x='total_bill',y='tip',data=df,kind='reg')
# plt.show()
'''pair plot numercail to kar dega if sirf df diya ho '''
# sns.pairplot(df) #saari numrical data ka compair kiyaa
# sns.pairplot(df,hue='sex')
# sns.pairplot(df,hue='size',palette='rainbow')
# plt.show()

'''catrgorical plot'''
# count plot
# sns.countplot(x=df['sex'],hue=df['smoker'])
# bar plot
# x=categorical data and y=qantiative data
# sns.barplot(x = df['sex'],y = df['total_bill'])
'''You can change the estimator object to your own function, that converts a vector to a scalar Mean (default): 
np.mean Median: np.median Sum: np.sum Count: len (to count the number of observations) 
Standard Deviation: np.std Minimum: np.min Maximum: np.max''' 
# sns.barplot(x = df['sex'],y = df['tip'],estimator=np.sum)
# plt.show()

'''boxplot and violinplot
boxplots and violinplots are used to shown the distribution of categorical data.
A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons
between variables or across levels of a categorical variable. 
The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, 
except for points that are determined to be “outliers” using a method that is a function of the inter-quartile ra'''
# sns.boxplot(x="tip",y='day',data=df,palette='rainbow')
# plt.show()
# sns.violinplot(x='day',y='total_bill',data=df)
# plt.show()
# overlapping karna hai to upar wala plt.show() delete kar do 
'''stripplot and swarmplot
The stripplot will draw a scatterplot where one variable is categorical. A strip plot can be drawn on its own, 
but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation
of the underlying distribution.
The swarmplot is similar to stripplot(), but the points are adjusted (only along the categorical axis) so that they don’t overlap. 
This gives a better representation of the distribution of values, although it does not scale as well to large numbers of observations 
(both in terms of the ability to show all the points and in terms of the computation needed to arrange them).'''

# sns.stripplot(x='day',y='total_bill',data=df)
# plt.show()
# sns.swarmplot(x='day',y='total_bill',data=df)
# plt.show()

# overlapping the violin and swarnplot 
# sns.violinplot(x='day',y='total_bill',data=df)
# sns.swarmplot(x='day',y='total_bill',data=df)
# plt.show()


'''Matrix Plot '''
'''heat map'''
# flights=sns.load_dataset('flights')
# print(flights)
tips=sns.load_dataset('tips')
# print(tips)

# we need to have coorelation 
# tipscore=tips[['total_bill','tip','size']]
# print(tipscore)
# now make the coorelation 
# print(tipscore.corr())
# sns.heatmap(tipscore.corr(),annot=True)
# plt.show()

# sns.clustermap(tipscore.corr())
# plt.show()

'''pivot table '''
# pvtflight = flights.pivot_table(values = 'passengers',index = 'month',columns = 'year')
# print(pvtflight)
# sns.heatmap(pvtflight,annot=True)
# plt.show()
'''
lmplot()
regression plot is used in machine learning so we will not fully discuss what,
how and where it is used but we will see how it is created and what are the values we can put inside it'''
# sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
# plt.show()
# linear regression hota hai

'''ploty'''
import cufflinks as cf 
from plotly.offline import iplot
print(tips)
# tips['total_bill'].iplot()
tips.groupby('day')['tip'].mean().iplot(kind = 'bar')
tips.iplot(kind='scatter',x ='total_bill',y = 'tip',mode = 'markers')
tips[['total_bill','day']].iplot(kind = 'box',x = 'total_bill',y = 'day')
plt.show()      