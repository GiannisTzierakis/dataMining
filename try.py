import sys
from functools import reduce

import pandas as pd
import numpy as np

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

Location1 = r'C:\Users\pltzi\Desktop\data mining\data\april\listings.csv'
Location2 = r'C:\Users\pltzi\Desktop\data mining\data\febrouary\listings.csv'
Location3 = r'C:\Users\pltzi\Desktop\data mining\data\march\listings.csv'

# filelist1 = os.listdir(Location1) # April
# filelist2 = os.listdir(Location2) # February
# filelist3 = os.listdir(Location3) # March
#
#
# print(filelist1)
# print(filelist2)
# print(filelist3)

# df_list = []
# i = 0
#
# for file in filelist:
#     fin = os.path.join(Location1,filelist[i])
#     df = pd.read_csv(fin,low_memory=False)
#     df_list.append(df)
#     i = i + 1
#
# big_df = pd.concat(df_list)
# print(big_df)

df1 = pd.read_csv(Location1, usecols=[
    'id',
    'zipcode',
    'transit',
    'bedrooms',
    'beds',
    'review_scores_rating',
    'number_of_reviews',
    'neighbourhood',
    'name',
    'latitude',
    'longitude',
    'last_review',
    'instant_bookable',
    'host_since',
    'host_response_rate',
    'host_identity_verified',
    'host_has_profile_pic',
    'first_review',
    'description',
    'city',
    'cancellation_policy',
    'bed_type',
    'bathrooms',
    'accommodates',
    'amenities',
    'room_type',
    'property_type',
    'price',
    'availability_365',
    'minimum_nights',
    'room_type'
])

df2 = pd.read_csv(Location2, usecols=[
    'id',
    'zipcode',
    'transit',
    'bedrooms',
    'beds',
    'review_scores_rating',
    'number_of_reviews',
    'neighbourhood',
    'name',
    'latitude',
    'longitude',
    'last_review',
    'instant_bookable',
    'host_since',
    'host_response_rate',
    'host_identity_verified',
    'host_has_profile_pic',
    'first_review',
    'description',
    'city',
    'cancellation_policy',
    'bed_type',
    'bathrooms',
    'accommodates',
    'amenities',
    'room_type',
    'property_type',
    'price',
    'availability_365',
    'minimum_nights'
])

df3 = pd.read_csv(Location3, usecols=[
    'id',
    'zipcode',
    'transit',
    'bedrooms',
    'beds',
    'review_scores_rating',
    'number_of_reviews',
    'neighbourhood',
    'name',
    'latitude',
    'longitude',
    'last_review',
    'instant_bookable',
    'host_since',
    'host_response_rate',
    'host_identity_verified',
    'host_has_profile_pic',
    'first_review',
    'description',
    'city',
    'cancellation_policy',
    'bed_type',
    'bathrooms',
    'accommodates',
    'amenities',
    'room_type',
    'property_type',
    'price',
    'availability_365',
    'minimum_nights'
])

df = df1

# MERGE
# df = pd.merge(df1, df2, on=['id', 'name', 'latitude', 'longitude'], how="outer")
# df = pd.merge(df, df3, on=['id', 'name', 'latitude', 'longitude'], how="outer")

# Combine first solution

# df.combine_first(df2)
# df.combine_first(df3)

dfs=[df1,df2,df3]
df4=reduce(lambda left,right: pd.merge(left,right,on='id'),dfs)

# # method for finding all missing data
# bool_series = pd.isnull(df)
# print(bool_series)


# method for dropping all rows with null values
new_df = df4.dropna(axis=0, how="any")

# #drop duplicates with distinct subset
# new_df.sort_values("id", inplace = True)
# new_df.drop_duplicates(subset="id", keep=False, inplace=True)
# new_df.to_csv('train.csv',index = False,header = True)
# print(new_df)

# drop duplicate rows
new_df.sort_values("id", inplace=True)
new_df.drop_duplicates(keep=False, inplace=True)
new_df.to_csv('train.csv', index=False, header=True)
print(new_df)

rtypes = new_df['room_type'].value_counts()
print(rtypes)

