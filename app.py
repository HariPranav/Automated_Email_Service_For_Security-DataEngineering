import time
import awswrangler as wr
import qgrid
import pandas as pd
import numpy as np
import json

# Ec2-> jupyter -> source DB -> query -> S3 -> AWS

df=wr.athena.read_sql_query("Select * from ", database="databasename")
df
x = df.to_string(header=False,
                  index=False,
                  index_names=False).split('\n')
vals = [','.join(ele.split()) for ele in x]


a = {"ToAddresses":  [], "CcAddresses": vals ,"BccAddresses": [] }

y = json.dumps(a)

#print(y)

with open(r"C:\Users\HP276VM\Desktop\destination.json", "w") as outfile:
    outfile.write(y)
    
# Execute the command to run the query

aws ses send-email --from Enter_Verified_Email --destination file://destination.json --message file://message.json
