import pandas as pd
import numpy as np
import os
import sys

path= "D:\DIT\Python Programs\DataMining\data"
path_list=os.listdir(path)
df_list = []
#for p in path_list:
#    new_path=path+"\\"+p
#   filelist = os.listdir(new_path)
#    for file in filelist:
#       df_list.append(pd.read_csv(new_path+"\\"+file))

#i=0
#for df in df_list:
#    print(i)
#    i+=1
#    print(df)
path= "D:\DIT\Python Programs\DataMining\data\\april"
path_list=os.listdir(path)
df1=pd.read_csv(path+"\\"+"listings0.csv")
df2=pd.read_csv(path+"\\"+"listings.csv",usecols=[
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

df3=pd.merge(df1,df2,on=['id','name','latitude','longitude'],how="outer")
print(df3)
df3.to_csv('try.csv',index=False,header=True)

