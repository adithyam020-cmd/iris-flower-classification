# 🌸 Iris Flower Classification


## 🚀 Live Demo

👉 https://iris-flower-classification-yvsnzyvrqcf4jhhcbqtokv.streamlit.app/

## 📌 Project Description

**Iris Flower Classification** is a Machine Learning-based web application that predicts the species of an Iris flower based on its physical measurements.

The application takes four measurements as input:

* 🌿 Sepal Length
* 🌿 Sepal Width
* 🌸 Petal Length
* 🌸 Petal Width

Using a trained **Logistic Regression** Machine Learning model, the application predicts one of three Iris species:

* 🌼 Iris Setosa
* 🌷 Iris Versicolor
* 🌺 Iris Virginica

The predicted flower species, confidence percentage, and a representative flower image are displayed through an interactive **Streamlit web application**.

## 🎯 Project Objectives

* Understand the basic workflow of Machine Learning classification.
* Analyze the Iris flower dataset.
* Train a classification model using Logistic Regression.
* Predict Iris flower species from user-provided measurements.
* Build an interactive and user-friendly web application.
* Demonstrate a practical application of Machine Learning.

## 🧠 Machine Learning Model

The project uses **Logistic Regression** for classification.

The model is trained using four features:

| Feature      | Description               |
| ------------ | ------------------------- |
| Sepal Length | Length of the sepal in cm |
| Sepal Width  | Width of the sepal in cm  |
| Petal Length | Length of the petal in cm |
| Petal Width  | Width of the petal in cm  |

The dataset contains **150 Iris flower samples** belonging to three species.

The trained model achieved **100% accuracy on the selected test split** used during model evaluation.

> Note: This accuracy refers to the specific test split used during training and evaluation; it does not guarantee 100% accuracy on every future flower sample.

## 🌐 Web Application

The Streamlit application contains two main pages:

### 🌸 Home Page

The home page introduces the project and explains:

* Project purpose
* Why the project is useful
* Real-world applications
* The three Iris species
* How the classification process works
* Technologies used

### 🔮 Prediction Page

Users can enter the four flower measurements and click **Predict Flower**.

The application then displays:

* Predicted Iris species
* Representative flower image
* Prediction confidence
* Information about the flower measurements

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Matplotlib
* Seaborn

## 📂 Project Structure

```text
Iris_Flower_Classification/
│
├── app.py
├── Iris.csv
├── train_model.py
├── iris_model.pkl
├── requirements.txt
├── README.md
│
├── images/
│   ├── setosa/
│   ├── versicolor/
│   └── virginica/
│
└── pages/
    └── Prediction.py
```

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/adithyam020-cmd/iris-flower-classification.git
```

### 2. Open the project folder

```bash
cd iris-flower-classification
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your web browser.

## 🔄 Project Workflow

```text
Iris Dataset
     ↓
Data Preparation
     ↓
Train Logistic Regression Model
     ↓
Evaluate Model
     ↓
Save Trained Model
     ↓
Streamlit Web Application
     ↓
User Enters Measurements
     ↓
Model Predicts Species
     ↓
Flower Image + Confidence
```

## 🌍 Applications

The project demonstrates how Machine Learning classification can be used to:

* Identify flower species
* Analyze biological measurements
* Build educational Machine Learning applications
* Demonstrate classification algorithms
* Create interactive prediction systems

## 👨‍💻 Project Type

**College Mini Project — BSc Data Science and Analytics**

## 📜 License

This project is created for educational and academic purposes.
