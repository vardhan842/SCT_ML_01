# SCT_ML_01
House Prices Prediction using Linear Regression
This project demonstrates a simple linear regression model to predict house prices using the House Prices: Advanced Regression Techniques dataset from Kaggle.

📁 Dataset
The dataset used is the train.csv file from the house-prices-advanced-regression-techniques.zip. It contains features related to residential homes in Ames, Iowa.

📊 Features Used
square_feet (LotArea)

bedrooms (BedroomAbvGr)

bathrooms (FullBath)

📌 Target
SalePrice (house price)

🛠️ Libraries Used
pandas

scikit-learn

zipfile

🚀 Steps
Extract and load the dataset from a ZIP file.

Select relevant features and the target variable.

Rename the columns for clarity.

Split the dataset into training and testing sets.

Fit a Linear Regression model.

Evaluate the model using Mean Squared Error (MSE).

🧪 How to Run
Place the house-prices-advanced-regression-techniques.zip in the same directory.

Make sure Python and the required libraries are installed.

Run task_01.py using any Python IDE or the command line:

bash
Copy
Edit
python task_01.py
📈 Output
The script will print:

The first few rows of the dataset.

Optionally, you can add evaluation metrics (e.g., MSE) to be printed after training.
