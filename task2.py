import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load the dataset (replace 'movie_data.csv' with your actual dataset file)
data = pd.read_csv('movie_data.csv')

# Feature Engineering: Convert categorical variables to numerical using one-hot encoding
encoder = OneHotEncoder(sparse=False)
encoded_features = encoder.fit_transform(data[['genre', 'director', 'actor']])
encoded_columns = encoder.get_feature_names(['genre', 'director', 'actor'])
encoded_df = pd.DataFrame(encoded_features, columns=encoded_columns)

# Combine encoded features with other numerical features
feature_columns = ['budget', 'runtime']
X = pd.concat([encoded_df, data[feature_columns]], axis=1)

# Target variable
y = data['rating']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'Root Mean Squared Error: {rmse:.2f}')
print(f'R-squared Score: {r2:.2f}')
