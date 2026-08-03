import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


df = pd.read_csv("kc_house_data.csv")

df = df[['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'waterfront', 'grade', 'price']]

X = df[['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'waterfront', 'grade']]
y = df['price']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=50,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))


joblib.dump(model,"model.pkl",compress=3)

print("✅ Model trained!")