import pickle
import pandas as pd
df=pd.read_csv('VulRepair_raw_preds_wild2_beam1.csv')
obj=df.to_dict()
f=open('VulRepair_raw_preds_wild2_beam1.pkl','wb')
pickle.dump(obj,f)
f.close()
