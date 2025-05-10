import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import zipfile

# Load dataset from the zip file
# Replace 'house-prices-advanced-regression-techniques.zip' with your actual file path
with zipfile.ZipFile('/house-prices-advanced-regression-techniques.zip') as z:
    # Assuming 'train.csv' is the file you want to load
    with z.open('train.csv') as f:
        df = pd.read_csv(f)

# Preview the data (optional)
print(df.head())

# Feature columns and target column
# Assuming 'SalePrice' is the name of your price column
# Also check for correct column names for square feet, bedrooms, bathrooms
X = df[['LotArea', 'BedroomAbvGr', 'FullBath']]
y = df['SalePrice']

# Rename columns to match your original code
X = X.rename(columns={'LotArea': 'square_feet', 'BedroomAbvGr': 'bedrooms', 'FullBath': 'bathrooms'})

# Split data into training and testing sets
X_train, X_test, y_train, y_test = t