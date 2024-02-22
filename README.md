
🖥️ Laptop Price Estimator: Predicting Laptop Prices with Machine Learning

![image](https://github.com/venkateshneu/Laptop_Price_Predictor/assets/141394492/aacc786d-10d7-4dc3-a17e-34989c4d6641)

Overview: This project endeavors to construct a machine learning model capable of predicting laptop prices based on a myriad of features including processor type, RAM, screen resolution, and more.

Data Preprocessing:

🛠️ Cleaning and Preprocessing: The dataset underwent meticulous cleaning and preprocessing to ensure data quality.
📊 Numeric Conversion: Non-numeric data was converted into numeric format for comprehensive analysis.
🔄 Feature Extraction: Relevant features such as CPU brand, touchscreen presence, and IPS display were extracted for enhanced analysis.
Exploratory Data Analysis (EDA):

📈 Price Distribution Exploration: The distribution of laptop prices was thoroughly explored.
📊 Feature Distribution Analysis: Key features like screen resolutions, CPU types, etc., were analyzed for their distributions.
🔍 Correlation Calculation: Correlations between features and laptop prices were calculated for deeper insights.
Feature Engineering:

🧮 PPI Calculation: Pixels per inch (PPI) were computed to quantify display sharpness.
🛠️ Processor Brand Extraction: Processor brand was extracted from CPU descriptions for further analysis.
Machine Learning Model Building:

🤖 Predictive Model Construction: A predictive model was built using various machine learning algorithms.
📊 Performance Evaluation: The model's performance was rigorously evaluated, and parameters were fine-tuned for improved accuracy.
Data Preprocessing (Continued):

Processor Labeling: Processor types were labeled using the fetch_processor(text) function, distinguishing between Intel Core i5/i7/i3 and other processors.
Memory Parsing: The "Memory" column was parsed meticulously, categorizing storage types and extracting numerical values for storage sizes.
GPU Labeling: GPU brands were extracted and categorized from the "Gpu" column.
Operating System Labeling: The "OpSys" column was transformed into categorical variables representing different operating system types.
Data Visualization:

📊 Processor Brands Bar Plot: The distribution of processor brands was visualized using a bar plot.
📦 GPU Brand Prices Box Plot: Prices were illustrated based on different GPU brands using a box plot.
📊 Operating System Type Prices Bar Plot: Another bar plot showcased price distributions based on operating system types.
📈 Weight and Price Distribution Plot: Density plots were used to visualize the distributions of weight and price.
Data Transformation:

➗ Log Transformation of Price: Price data underwent log transformation to achieve a normalized distribution.
Model Preparation:

📋 Feature Selection: Relevant columns were strategically dropped, and the dataset was split into features (X) and target (y) variables.
🛠️ Feature Encoding: Categorical variables were encoded for compatibility with machine learning algorithms.
⚙️ Modeling Process: Various machine learning algorithms including Linear Regression, Ridge Regression, Lasso Regression, and more were utilized. Feature engineering and preprocessing techniques like OneHotEncoding and ColumnTransformer were employed. Model performance was evaluated using metrics like R-squared score and Mean Squared Error.

📊 Model Performance: RandomForestRegressor yielded the highest R-squared score of approximately 0.886, indicating strong predictive capability. Other models such as XGBRegressor and BaggingRegressor also performed well with R-squared scores above 0.87.

🔧 Implementation: The best-performing model (RandomForestRegressor) was integrated into a Streamlit-based web application. The trained model was serialized using pickle for easy deployment. The web application provides a user-friendly interface for predicting laptop prices based on user input.

💡 Insights: RAM, GPU, weight, touchscreen, and CPU brand were identified as influential features in predicting laptop prices. The RandomForestRegressor model demonstrated robustness in capturing complex relationships between features and target variables.

🚀 Future Directions: Future plans include optimizing the web application for scalability and performance, continuously monitoring and updating the model to adapt to market trends, and exploring additional features or datasets to enhance model accuracy.

This comprehensive machine learning project successfully predicts laptop prices with high accuracy, offering valuable insights for consumers and sellers in the laptop market through a user-friendly web application interface.

