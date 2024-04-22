import lightgbm as lgb
from fastapi import FastAPI
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import lightgbm as lgb


def load_data(path):
    df = pd.read_csv(path)
    # arham check this later
    # original = pd.read_csv('/kaggle/input/obesity-or-cvd-risk-classifyregressorcluster/ObesityDataSet.csv')
    # split to train test
    train_df, test_df = train_test_split(df, test_size=0.35, random_state=42)
    train_df = train_df.drop(["id"], axis=1).drop_duplicates().reset_index(drop=True)
    test_df = test_df.drop(["id"], axis=1).drop_duplicates().reset_index(drop=True)
    return train_df, test_df


path = "../01-Dataset/01-Data-for-model-building/train.csv"
train, test = load_data(path)


target = "NObeyesdad"
num_col = []
cat_col = []

for i in train.columns.drop([target]):
    if train[i].dtype == "object":
        cat_col.append(i)

    else:
        num_col.append(i)


train = pd.get_dummies(train, columns=cat_col)
test = pd.get_dummies(test, columns=cat_col)

target = "NObeyesdad"

le = LabelEncoder()
train["NObeyesdad"] = le.fit_transform(train["NObeyesdad"])


# load lgbm model from pickle
lgb_model_final = pickle.load(open("11-Docker/lgb_model_final.pkl", "rb"))


# predicting first row of test data
y_pred = lgb_model_final.predict(test.iloc[0].values.reshape(1, -1))
y_pred_proba = lgb_model_final.predict_proba(test.iloc[0].values.reshape(1, -1))

print(y_pred)
print(y_pred_proba)
