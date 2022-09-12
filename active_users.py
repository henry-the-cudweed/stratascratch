# Import your libraries
#solution for 10322.py
#Write a query that'll identify returning active users. 
#A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. 
#Output a list of user_ids of these returning active users.
#customers dataframe
#id:int64
#user_id:int64
#item:object
#created_at:datetime64[ns]
#revenue:int64

import pandas as pd
import numpy as np
df = amazon_transactions

#each row in this dataframe represents a customer purchase

#how my solution worked: i removed all customers with only one purchase by creating list with all users with more than one purchase
df2 = df.groupby(['user_id']).count().reset_index()
df3 = df2[df2.id > 1].sort_values(by="id")
list = df3['user_id'].tolist()
df4 = df[df['user_id'].isin(list)]

#then i sorted by user id and purchase date
df5 = df4.sort_values(["user_id", "created_at"]).drop(["id"], axis=1).reset_index().drop(["index"], axis=1)
df5.index.name="index"
 
#to calculate the difference between dates of purchase, i created a new column representing the next date each customer made a purchase, using shift() which 
#moved all the columns up 
df5['next_date'] = df5['created_at'].shift(-1)

#i then filtered out whether or not the next_date column was actually drawing the next_date based on the customer's next purchase, or based on a new set of
#purchases from another user
df5['is_next_date_same_user'] = df5["user_id"] == df5["user_id"].shift(-1)

#i calcuated the difference in days between purchases
df5['difference'] = (df5['next_date'] - df5['created_at']).dt.days

#i made sure the differences were within the specified time frame 
df6 = (df5[df5['difference'] <= 7])
df7 = df6[df6['difference'] >= 0] 
df8 = df7[df7['is_next_date_same_user'] == True]

#i generated a list of unique user_ids from the remaining rows 
answer = df8['user_id'].unique().tolist()

answer

#apparently the difference between values in rows can be calculated using .diff() in python, and i didn't need to use shift() at all! 


