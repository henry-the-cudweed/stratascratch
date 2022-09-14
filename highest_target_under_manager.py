#Find the highest target achieved by the employee or employees who works under the manager id 13. Output the first name of the employee and target achieved.
#The solution should show the highest target achieved under manager_id=13 and which employee(s) achieved it.

#salesforce_employes
#id:int64
#first_name:object
#last_name:object
#age:int64
#sex:object
#employee_title:object
#department:object
#salary:int64
#target:int64
#bonus:int64
#email:object
#city:object
#address:object
#manager_id:int64

# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
### I filtered for only employees under the given manager
df = salesforce_employees.where(salesforce_employees["manager_id"] == 13).dropna(0,how="all")

### Sort by target in descending order, reset the index and rename the index to "rank", and reset index again so that the rank is a column instead of an index
df = df.sort_values("target", ascending = False).reset_index()
df.index.name="rank"
df = df.reset_index()

### Place the value of the highest target in a list
rank0 = df['target'].where(df['rank'] == 0).tolist()

### iterate over all values in the list and remove anything that is not a number
rank0 = [i for i in rank0 if not(pd.isnull(i)) == True]

### search for all employees whose target equals the highest ranking target 
df2 = df.loc[(df['target']).isin(rank0)]

### answer
df2[["first_name","target"]]

############ notes
### i could have also used the pandas function df.max() to find the top value instead of making a rank, and throwing the top ranking value into a list
