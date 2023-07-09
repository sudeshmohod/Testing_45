#!/usr/bin/env python
# coding: utf-8

# In[1]:


##imports
import pandas as pd
from sqlalchemy import create_engine
from colorama import Fore, Back, Style


# In[2]:


#create sql connection
server = "DESKTOP-QRNMQVD"
database = "HR"
driver="ODBC Driver 17 for SQL Server"
database_con=f'mssql://@{server}/{database}?driver={driver}'
engine=create_engine(database_con)
connection=engine.connect()


# In[3]:


#sql command to read the database data
# C:\Users\yasho\Desktop\Test_Automation\Queries
xldata=pd.read_excel(r"C:\Users\yasho\Desktop\Test_Automation\Queries\Sql_query.xlsx")
# C:\Users\yasho\Desktop\Test_Automation\Queries


# In[4]:


xldata


# In[5]:


# type(xldata)


# In[6]:


src_table_query=xldata["sql_query"][0]
print("Source_sql_query:",src_table_query)


# In[7]:


tgt_table_query=xldata["sql_query"][1]
print("Target_sql_query:",tgt_table_query)


# In[9]:


print(src_table_query)
print(tgt_table_query)


# In[11]:


src_df=pd.read_sql_query(src_table_query,connection)


# In[12]:


print(src_df)


# In[13]:


tgt_df=pd.read_sql_query(tgt_table_query,connection)


# In[14]:


print(tgt_df)


# In[15]:


src_df


# In[16]:


tgt_df


# In[17]:


src_count= len(src_df)


# In[18]:


src_count


# In[19]:


tgt_count= len(tgt_df)


# In[20]:


tgt_count


# In[21]:


src_count= len(src_df)
tgt_count= len(tgt_df)
if len(src_df) == len(tgt_df):
    status="Match"
    print(Fore.GREEN + "\n1) Test Case Pass:Source and Target count is getting matched.")
else:
    status="Not match"
    print(Fore.RED + "\n1) Test Case Fail" + ":Source and Target count is not getting matched.")


# In[ ]:


count_df=pd.DataFrame({
    'Source_count':src_count,
    'Target_count':tgt_count,
    'Status':status},index=[0])


# In[ ]:


len(src_df)


# In[ ]:


len(tgt_df)


# In[ ]:


count_df=pd.DataFrame({
    'Source_count':src_count,
    'Target_count':tgt_count,
    'Status':status},index=[0])


# In[ ]:


count_df


# In[ ]:


tgt_dup = tgt_df.duplicated()


# In[ ]:


tgt_dup


# In[ ]:


dup_tgt_records = tgt_df[tgt_df.duplicated()]


# In[ ]:


tgt_df


# In[ ]:


dup_tgt_records=tgt_df[tgt_df.duplicated()]


# In[ ]:


tgt_dup = tgt_df.duplicated().sum()
print(tgt_dup)


# In[ ]:


tgt_df.duplicated()


# In[ ]:


tgt_dup = tgt_df.duplicated().sum()
dup_tgt_records = tgt_df[tgt_df.duplicated()]


if tgt_dup > 0:
    print(Fore.RED + "2) Test Case Fail: Duplicate records are found in target table")
else:
    print(Fore.GREEN + "2) Test Case Pass: Duplicate records are not found in target table")


# In[ ]:


Data_validation_df=src_df.isin(tgt_df)
print(Data_validation_df)


# In[ ]:





# In[ ]:


path=r'C:\Users\yasho\Desktop\Test_Automation\Test_evidences.xlsx'
writer=pd.ExcelWriter(path, engine='xlsxwriter')
src_df.to_excel(writer, sheet_name='Source Data',index=False)
tgt_df.to_excel(writer, sheet_name='Target Data',index=False)
count_df.to_excel(writer,sheet_name='Count_validation')
dup_tgt_records.to_excel(writer, sheet_name='Duplicate Count', index=False)
Data_validation_df.to_excel(writer, sheet_name='Data_validation', index=False)
writer.save()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import pandas as pd
from sqlalchemy import create_engine
from colorama import Fore, Back, Style

#create sql connection
server = "DESKTOP-QRNMQVD"
database = "HR"
driver="ODBC Driver 17 for SQL Server"
database_con=f'mssql://@{server}/{database}?driver={driver}'
engine=create_engine(database_con)
connection=engine.connect()

#sql command to read the database data
# C:\Users\yasho\Desktop\Test_Automation\Queries
xldata=pd.read_excel(r"C:\Users\yasho\Desktop\Test_Automation\Queries\Sql_query.xlsx")


src_table_query=xldata["sql_query"][0]
##print("Source_sql_query:",src_table_query)

tgt_table_query=xldata["sql_query"][1]
##print("Target_sql_query:",tgt_table_query)

src_df=pd.read_sql_query(src_table_query,connection)
# print(src_df)
tgt_df=pd.read_sql_query(tgt_table_query,connection)
# print(tgt_df)

#Export to csv
path=r"C:\Users\yasho\Desktop\Test_Automation\Test_evidences\Test_evidences.xlsx"
# path=r'C:\Users\yasho\Desktop\Test_evidences.xlsx'
writer=pd.ExcelWriter(path, engine='xlsxwriter')
src_df.to_excel(writer, sheet_name='Source Data',index=False)
tgt_df.to_excel(writer, sheet_name='Target Data',index=False)
#1. Write the Count Validation status in excel
src_count= len(src_df)
tgt_count= len(tgt_df)
if len(src_df) == len(tgt_df):
    status="Match"
    print(Fore.GREEN + "\n1) Test Case Pass:Source and Target count is getting matched.")
else:
    status="Not match"
    print(Fore.RED + "\n1) Test Case Fail" + ":Source and Target count is not getting matched.")

count_df=pd.DataFrame({
    'Source_count':src_count,
    'Target_count':tgt_count,
    'Status':status},index=[0])

count_df.to_excel(writer,sheet_name='Count_validation')

# 2 Duplicate count
tgt_dup = tgt_df.duplicated().sum()
dup_tgt_records = tgt_df[tgt_df.duplicated()]
dup_tgt_records.to_excel(writer, sheet_name='Duplicate Count', index=False)

if tgt_dup > 0:
    print(Fore.RED + "2) Test Case Fail: Duplicate records are found in target table")
else:
    print(Fore.GREEN + "2) Test Case Pass: Duplicate records are not found in target table")

#3. Data validation method 1
Data_validation_df=src_df.isin(tgt_df)
Data_validation_df.to_excel(writer, sheet_name='Data_validation', index=False)

writer.save()


# In[ ]:




