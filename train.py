import sys
import pandas as pd
import matplotlib.pyplot as plt

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

Location1 = r'C:\Users\pltzi\Desktop\data mining\data\april\listings.csv'
Location2 = r'C:\Users\pltzi\Desktop\data mining\data\febrouary\listings.csv'
Location3 = r'C:\Users\pltzi\Desktop\data mining\data\march\listings.csv'

# filelist1 = os.listdir(Location1) # April
# filelist2 = os.listdir(Location2) # February
# filelist3 = os.listdir(Location3) # March

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

# # method for finding all missing data
# bool_series = pd.isnull(df)
# print(bool_series)

df = df1.append(df2)
df = df.append(df3)

# #drop duplicates with distinct subset
# new_df.drop_duplicates(subset="id", keep=False, inplace=True)

# drop all duplicate rows

df.sort_values("price", inplace=True)
df.drop_duplicates(keep=False, inplace=True)
# method for dropping all rows with null values
new_df = df.dropna(axis='rows', how="any")

new_df.to_csv('train.csv', index=False, header=True)
print(new_df)

# 1.1

rtypes = new_df['room_type'].value_counts().index[0]
most_rtype = new_df['room_type'].value_counts().max()
print(rtypes+": %d" % most_rtype)

# 1.2

new_df.plot(x='price', kind='hist')
plt.show()

# 1.3