# Energy Saver Recommendation System

A simple machine learning web app that predicts household electricity usage and helps estimate how appliance usage affects monthly energy cost.

This project was built to explore how machine learning can be used for everyday energy planning in a way that feels practical, interactive, and easy to understand.

## Demo


## Features

- Predicts household energy consumption from appliance usage data
- Estimates monthly electricity bills
- Interactive Streamlit interface
- Real-time updates when input values change
- Visual charts for better understanding
- Clean and easy-to-use UI

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **Data Handling:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Version Control:** Git, GitHub

## How It Works

1. The user enters appliance usage details.
2. The app processes the inputs and prepares them for prediction.
3. A regression model estimates energy consumption.
4. The app shows the predicted value and billing estimate.
5. Charts and visuals help make the output easier to interpret.

What I Learned

This project helped me get more comfortable with:

Building a machine learning workflow from scratch
Data preprocessing and feature engineering
Regression modeling
Creating interactive web apps with Streamlit
Presenting results through charts and simple visuals
Using Git and GitHub for project management
Future Improvements

A few things I would like to add later:

Smarter recommendations based on usage patterns
Better model tuning for improved accuracy
Support for real-time energy data
A more detailed dashboard
Deployment on a public hosting platform
Author

Krupal Ameti
Computer Science Engineering Student
Interested in Artificial Intelligence, Machine Learning, and Full-Stack Development

GitHub: github.com/Krupal-ApexAI
LinkedIn: linkedin.com/in/krupal-ameti-24235a319
License

This project is open for learning and personal use.

## Project Setup

Energy-Saver/
│
├── app.py
├── train_model.py
├── requirements.txt
├── data/
├── models/
└── README.md

### Clone the repository
```bash
git clone https://github.com/Krupal-ApexAI/Energy-Saver.git

cd Energy-Saver

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
