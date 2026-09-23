import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load the dataset
data = pd.read_csv("Iris.csv")

# Remove unnecessary Id column
data = data.drop("Id", axis=1)

# Separate features and target
X = data.drop("Species", axis=1)
y = data["Species"]

# Split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create the machine learning model
model = LogisticRegression(max_iter=200)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model trained successfully!")
print("Accuracy:", accuracy)
print("Accuracy percentage:", accuracy * 100)

# Save the trained model
joblib.dump(model, "iris_model.pkl")

print("Model saved successfully!")