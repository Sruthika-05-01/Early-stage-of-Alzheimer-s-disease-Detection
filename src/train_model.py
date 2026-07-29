
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data={
    'Age':[65,70,75,80,60],
    'Memory':[3,2,2,1,3],
    'Thinking':[3,2,2,1,3],
    'Decision':[3,2,2,1,3],
    'Result':[0,1,1,1,0]   
}

df=pd.DataFrame(data)


X=df[['Age','Memory','Thinking','Decision']]


y=df['Result']

model=RandomForestClassifier()
model.fit(X,y)

with open("alzheimer_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully")