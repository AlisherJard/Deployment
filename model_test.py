from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error
import numpy as np

# Creating of dataframe for model from cleaned_data.csv

df_pd = pd.read_csv("cleaned_data.csv")
features = []
features = df_pd.drop(['Price'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(features, np.log(df_pd['Price']),test_size=0.2, random_state=0)

# rfr_model = 'model.pkl'
# joblib.dump(rfr_model, 'model_rf.pkl', compress=9)

loaded_model = joblib.load('model_rf.pkl')
#
# # Predict and evaluate

y_pred = loaded_model.predict(X_test)

score = loaded_model.score(X_test, y_test)
mae = mean_absolute_error(np.exp(y_test), np.exp(y_pred))

print(f"R2: {round(score,2)} %")
print(f"MAE: {round(mae,1)}")