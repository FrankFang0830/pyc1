import pandas as pd

##reading data set
train_df = pd.read_csv('./train.csv')
test_df = pd.read_csv('./test.csv')
print(train_df.head())            # the default value is 5 ,output the top 5 of set
print(train_df.columns.values)    # print the each predictors(features) of samples
train_df.info()                   # print the features' data types
print("-"*40)
test_df.info()
print(train_df.describe())
print(train_df.describe(include=['O']))
# calculate each gender's survival rate // group by male and female//mean():sum survived and calculate mean(survival rate)
print(train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))
