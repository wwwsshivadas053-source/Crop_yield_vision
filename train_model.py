import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import pickle

data = pd.read_csv("crop_yield.csv")

le_crop = LabelEncoder()
le_soil = LabelEncoder()
le_fertilizer = LabelEncoder()

data["Crop"] = le_crop.fit_transform(data["Crop"])
data["Soil"] = le_soil.fit_transform(data["Soil"])
data["Fertilizer_Used"] = le_fertilizer.fit_transform(data["Fertilizer_Used"])

X = data[["Crop","Soil","Temperature_C","Rainfall_mm","Fertilizer_Used"]]
y = data["Yield"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl","wb"))

# Save encoders
pickle.dump(le_crop, open("crop_encoder.pkl", "wb"))
pickle.dump(le_soil, open("soil_encoder.pkl", "wb"))
pickle.dump(le_fertilizer, open("fertilizer_encoder.pkl", "wb"))