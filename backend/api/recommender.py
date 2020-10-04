import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from backend import settings
import numpy as np
from django.apps import AppConfig
import pickle
from pathlib import Path


DATA_DIR = Path(settings.BASE_DIR).parent.parent / "data"
PKL_FILE = str(DATA_DIR / "2019-full_refactored.pkl")
MODEL_FILE = str(DATA_DIR / "rf_trained_model.pkl")

sido_encoder = LabelEncoder()
gugun_encoder = LabelEncoder()
dong_encoder = LabelEncoder()
model = None
df = None


class AppConfigStartUp(AppConfig):
    name = 'api'

    def ready(self):
        initialize()


def make_prediction():
    global df
    df = df[(df["code"] > 2100)]
    sido = sido_encoder.fit_transform(df['sido'])
    gugun = gugun_encoder.fit_transform(df['gugun'])
    dong = dong_encoder.fit_transform(df['dong'])

    n = df.columns[2]
    df.drop(n, axis=1)
    df[n] = sido
    n = df.columns[3]
    df.drop(n, axis=1)
    df[n] = gugun
    n = df.columns[4]
    df.drop(n, axis=1)
    df[n] = dong

    features = pd.get_dummies(df, columns=['gender', 'age'])
    labels = np.array(features['code'])
    features = features.drop('code', axis=1)
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.1,
                                                                                random_state=42)
    prediction = model.predict_proba(test_features)
    prediction_df = pd.DataFrame(data=prediction, columns=model.classes_)
    user_prediction_df = prediction_df.sort_values(by=prediction_df.tail(1).index.item(), axis=1, ascending=False)
    return [user_prediction_df.columns[0], user_prediction_df.columns[1], user_prediction_df.columns[2]]


def get_model():
    return model


def encode_features(age, gender, sido, gugun, dong):
    global df
    df = df.append(pd.Series([gender, age, sido, gugun, dong, 2104], index=df.columns), ignore_index=True)


def initialize():
    global df
    global model
    df = pd.read_pickle(PKL_FILE)
    model = pickle.load(open(MODEL_FILE, 'rb'))
