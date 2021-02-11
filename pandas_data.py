import pandas as pd
import datetime as dt


df = pd.read_csv('POS_Data.csv')
df['TIMEDESC']=pd.to_datetime(df.TIMEDESC)
df['TIMEDESC'] = df.TIMEDESC.dt.strftime('%m/%d/%y')
df.to_csv('updated.csv')
print("done")