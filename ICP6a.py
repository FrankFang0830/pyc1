import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use(style='ggplot')#a pre-defined style called “ggplot”, which emulates the aesthetics of ggplot
plt.rcParams['figure.figsize'] = (10, 6)# set the size 10*6
train=pd.read_csv('train.csv')
print(train.SalePrice.describe())
#check the degree of asymmetry
print("the skew of sale price is: %f" %train.SalePrice.skew())
plt.hist(train.SalePrice)
plt.show()
#then we do log-transform to enhance accuracy of linearity
logTrain=np.log(train.SalePrice)
print("the skew after log transformed is: %f" %logTrain.skew())
plt.hist(logTrain)
plt.show()

numeric_features = train.select_dtypes(include=[np.number]) # select quantitative features
#print(numeric_features)
corr=numeric_features.corr() # calculate correlation in numeric_features and results are in a matrix
print(corr)
print(corr['SalePrice'].sort_values(ascending=False)[:5], '\n')#extract row=sale price and select top5
#acccording to the result we can find the overallQual and sale price have strong correlation


#now, we plot GaurageArea field and SalePrice in scatter plot
quality_pivot = train.pivot_table(index='GarageArea',
                                  values='SalePrice', aggfunc=np.median)
print(quality_pivot)
quality_pivot.plot(kind='bar',color ='blue')
plt.show()


plt.scatter(train['GarageArea'],train['SalePrice'])
plt.show()
print(train['GarageArea'].size)

zerodata=train[(train['GarageArea'].values == 0)].index.tolist()
train=train.drop(zerodata)
print("After removed zero data the plot will be:")
plt.scatter(train['GarageArea'],train['SalePrice'])
plt.show()
print(train['GarageArea'].size)

anormaldata=train[(train['GarageArea'].values > 1100)].index.tolist()
train=train.drop(anormaldata)
print("After remove extreme data the plot will be:")
plt.scatter(train['GarageArea'],train['SalePrice'])
plt.show()
print(train['GarageArea'].size)

