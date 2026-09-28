import streamlit as st
import joblib
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Model Information",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "iris_model.pkl"


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()
except Exception as e:
    st.error("Unable to load the trained model.")
    st.code(str(e))
    st.stop()


# =========================================================
# HIDE SIDEBAR
# =========================================================

st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stSidebarCollapsedControl"] {
    display: none;
}


/* =====================================================
   BACKGROUND
   ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(59,130,246,0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 80%,
            rgba(139,92,246,0.15),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #020617,
            #0f172a,
            #111827
        );
}

.block-container {
    max-width: 1200px;
    padding-top: 35px;
    padding-bottom: 50px;
}


/* =====================================================
   HEADER
   ===================================================== */

.title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;

    background: linear-gradient(
        90deg,
        #60a5fa,
        #a78bfa,
        #f472b6
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 17px;
    margin-top: 10px;
    margin-bottom: 35px;
}


/* =====================================================
   SECTION
   ===================================================== */

.section {
    color: #f8fafc;
    font-size: 26px;
    font-weight: 750;
    margin-top: 35px;
    margin-bottom: 18px;
}


/* =====================================================
   CARDS
   ===================================================== */

.card {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.075),
            rgba(255,255,255,0.025)
        );

    border: 1px solid rgba(255,255,255,0.10);

    border-radius: 18px;

    padding: 24px;

    min-height: 145px;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.15);
}

.card-title {
    color: #f8fafc;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
}

.card-text {
    color: #aebbd0;
    font-size: 14px;
    line-height: 1.7;
}


/* =====================================================
   METRICS
   ===================================================== */

.metric {
    background: rgba(255,255,255,0.06);

    border: 1px solid rgba(255,255,255,0.09);

    border-radius: 18px;

    padding: 22px;

    text-align: center;
}

.metric-value {
    color: #93c5fd;
    font-size: 30px;
    font-weight: 800;
}

.metric-label {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 5px;
}


/* =====================================================
   FEATURE BOX
   ===================================================== */

.feature {
    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 15px;

    padding: 18px;

    text-align: center;
}

.feature-icon {
    font-size: 30px;
}

.feature-name {
    color: #f8fafc;
    font-weight: 700;
    margin-top: 8px;
}

.feature-description {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 5px;
}


/* =====================================================
   PROCESS
   ===================================================== */

.process {
    background: rgba(255,255,255,0.055);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 16px;

    padding: 20px;

    text-align: center;

    min-height: 130px;
}

.process-number {
    color: #a78bfa;
    font-size: 25px;
    font-weight: 800;
}

.process-title {
    color: #f8fafc;
    font-weight: 700;
    margin-top: 7px;
}

.process-text {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 5px;
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 45px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🤖 Model Information</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Understanding the machine learning model behind the prediction system'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# MODEL OVERVIEW
# =========================================================

st.markdown(
    '<div class="section">🧠 Model Overview</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

    <div class="card-title">
        Logistic Regression
    </div>

    <div class="card-text">

        This project uses <b>Logistic Regression</b> as the
        classification algorithm.

        The model learns the relationship between the four
        flower measurements and the corresponding Iris species.

        After training, the model can receive new measurements
        and predict whether the flower belongs to
        Iris-setosa, Iris-versicolor, or Iris-virginica.

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# MODEL STATISTICS
# =========================================================

st.markdown(
    '<div class="section">📊 Model Details</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric">
        <div class="metric-value">150</div>
        <div class="metric-label">Total Samples</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric">
        <div class="metric-value">120</div>
        <div class="metric-label">Training Samples</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric">
        <div class="metric-value">30</div>
        <div class="metric-label">Testing Samples</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric">
        <div class="metric-value">3</div>
        <div class="metric-label">Output Classes</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ALGORITHM
# =========================================================

st.markdown(
    '<div class="section">⚙️ Why Logistic Regression?</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">

        <div class="card-title">
            Classification Algorithm
        </div>

        <div class="card-text">

            Logistic Regression is a supervised machine learning
            algorithm commonly used for classification problems.

            Although its name contains "Regression", it can be
            used to classify observations into different classes.

        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">

        <div class="card-title">
            Prediction Output
        </div>

        <div class="card-text">

            The trained model predicts one of three Iris species.
            The application also uses the model's probability
            output to display a confidence value for the prediction.

        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# INPUT FEATURES
# =========================================================

st.markdown(
    '<div class="section">🌿 Model Input Features</div>',
    unsafe_allow_html=True
)

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown("""
    <div class="feature">

        <div class="feature-icon">📏</div>

        <div class="feature-name">
            Sepal Length
        </div>

        <div class="feature-description">
            Measured in centimeters
        </div>

    </div>
    """, unsafe_allow_html=True)


with f2:
    st.markdown("""
    <div class="feature">

        <div class="feature-icon">📐</div>

        <div class="feature-name">
            Sepal Width
        </div>

        <div class="feature-description">
            Measured in centimeters
        </div>

    </div>
    """, unsafe_allow_html=True)


with f3:
    st.markdown("""
    <div class="feature">

        <div class="feature-icon">🌱</div>

        <div class="feature-name">
            Petal Length
        </div>

        <div class="feature-description">
            Measured in centimeters
        </div>

    </div>
    """, unsafe_allow_html=True)


with f4:
    st.markdown("""
    <div class="feature">

        <div class="feature-icon">🌿</div>

        <div class="feature-name">
            Petal Width
        </div>

        <div class="feature-description">
            Measured in centimeters
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# OUTPUT CLASSES
# =========================================================

st.markdown(
    '<div class="section">🎯 Prediction Classes</div>',
    unsafe_allow_html=True
)

o1, o2, o3 = st.columns(3)

with o1:
    st.markdown("""
    <div class="feature">

        <div class="feature-icon">🌸</div>

        <div class="feature-name">
            Iris Setosa
        </div>

        <div class="feature-description">
            Classification output
        </div>

    </div>
    """, unsafe_allow_html=True)


with o2:
    st.markdown("""
    <div class="feature">

        <div class="feature-icon">🌷</div>

        <div class="feature-name">
            Iris Versicolor
        </div>

        <div class="feature-description">
            Classification output
        </div>

    </div>
    """, unsafe_allow_html=True)


with o3:
    st.markdown("""
    <div class="feature">

        <div class="feature-icon">🌺</div>

        <div class="feature-name">
            Iris Virginica
        </div>

        <div class="feature-description">
            Classification output
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# TRAINING PROCESS
# =========================================================

st.markdown(
    '<div class="section">🔄 Training Process</div>',
    unsafe_allow_html=True
)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.markdown("""
    <div class="process">

        <div class="process-number">01</div>

        <div class="process-title">
            Load Dataset
        </div>

        <div class="process-text">
            Read the Iris dataset
        </div>

    </div>
    """, unsafe_allow_html=True)


with p2:
    st.markdown("""
    <div class="process">

        <div class="process-number">02</div>

        <div class="process-title">
            Prepare Data
        </div>

        <div class="process-text">
            Select four input features
        </div>

    </div>
    """, unsafe_allow_html=True)


with p3:
    st.markdown("""
    <div class="process">

        <div class="process-number">03</div>

        <div class="process-title">
            Train Model
        </div>

        <div class="process-text">
            Train Logistic Regression
        </div>

    </div>
    """, unsafe_allow_html=True)


with p4:
    st.markdown("""
    <div class="process">

        <div class="process-number">04</div>

        <div class="process-title">
            Make Prediction
        </div>

        <div class="process-text">
            Predict new flower species
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# EVALUATION
# =========================================================

st.markdown(
    '<div class="section">📈 Model Evaluation</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

    <div class="card-title">
        Test Accuracy: 100%
    </div>

    <div class="card-text">

        The trained Logistic Regression model achieved
        <b>100% accuracy on the selected 20% test split</b>
        consisting of 30 samples.

        <br><br>

        This result represents the performance on that particular
        train/test split and should not be interpreted as a guarantee
        of 100% accuracy on every future flower sample.

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# MODEL CLASSES
# =========================================================

st.markdown(
    '<div class="section">🔎 Model Classes</div>',
    unsafe_allow_html=True
)

try:

    classes = model.classes_

    st.success(
        "The trained model recognizes the following classes:"
    )

    for item in classes:
        st.write("🌸", item)

except Exception:

    st.info(
        "The model classes could not be displayed, "
        "but the trained model is loaded successfully."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    Iris Flower Classification
    <br>
    Machine Learning Model Information
    <br><br>
    BSc Data Science and Analytics

</div>
""", unsafe_allow_html=True)