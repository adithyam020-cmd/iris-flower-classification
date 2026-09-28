import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(139, 92, 246, 0.18), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(236, 72, 153, 0.15), transparent 30%),
        linear-gradient(135deg, #080b16, #10182d 50%, #080b16);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
}


/* Main heading */

.dashboard-title {
    font-size: 45px;
    font-weight: 900;
    color: white;
}

.dashboard-subtitle {
    color: #94a3b8;
    font-size: 17px;
    margin-bottom: 30px;
}


/* Metric cards */

.metric-card {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    min-height: 135px;
    backdrop-filter: blur(15px);
}

.metric-icon {
    font-size: 30px;
}

.metric-value {
    color: white;
    font-size: 32px;
    font-weight: 900;
    margin-top: 5px;
}

.metric-label {
    color: #94a3b8;
    font-size: 14px;
}


/* Section headings */

.section-title {
    color: white;
    font-size: 26px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 18px;
}


/* Information cards */

.info-card {
    background: rgba(255, 255, 255, 0.055);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 20px;
    padding: 25px;
    min-height: 175px;
}

.info-title {
    color: white;
    font-size: 19px;
    font-weight: 800;
    margin-bottom: 10px;
}

.info-text {
    color: #aeb8c8;
    font-size: 15px;
    line-height: 1.7;
}


/* Workflow */

.workflow {
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
}

.workflow-number {
    color: #f9a8d4;
    font-size: 28px;
    font-weight: 900;
}

.workflow-title {
    color: white;
    font-weight: 800;
    margin-top: 8px;
}

.workflow-text {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 5px;
}


/* Feature tags */

.feature-box {
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 16px;
    padding: 18px;
    color: #dbe4f0;
    text-align: center;
    font-weight: 700;
}


/* Footer */

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="dashboard-title">📊 Project Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'A quick overview of the Iris Flower Classification system'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# KEY METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🌱</div>
        <div class="metric-value">150</div>
        <div class="metric-label">Dataset Samples</div>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">📐</div>
        <div class="metric-value">4</div>
        <div class="metric-label">Input Features</div>
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🌸</div>
        <div class="metric-value">3</div>
        <div class="metric-label">Flower Species</div>
    </div>
    """, unsafe_allow_html=True)


with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🎯</div>
        <div class="metric-value">100%</div>
        <div class="metric-label">Test Accuracy</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# PROJECT OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">🔎 Project Overview</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    st.markdown("""
    <div class="info-card">

        <div class="info-title">
            🌸 What does this project do?
        </div>

        <div class="info-text">
            This application uses a machine learning classification
            model to identify the species of an Iris flower based on
            four physical measurements.
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="info-card">

        <div class="info-title">
            🤖 Machine Learning Model
        </div>

        <div class="info-text">
            A Logistic Regression classification model is trained
            using the Iris dataset and used to predict three
            different Iris flower species.
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# WORKFLOW
# =========================================================

st.markdown(
    '<div class="section-title">⚙️ Machine Learning Workflow</div>',
    unsafe_allow_html=True
)

steps = [
    ("01", "Dataset", "Iris flower data"),
    ("02", "Preprocessing", "Prepare features"),
    ("03", "Training", "Train classifier"),
    ("04", "Prediction", "Classify flower"),
    ("05", "Result", "Display species")
]

cols = st.columns(5)

for col, (number, title, description) in zip(cols, steps):

    with col:

        st.markdown(
            f"""
            <div class="workflow">

                <div class="workflow-number">
                    {number}
                </div>

                <div class="workflow-title">
                    {title}
                </div>

                <div class="workflow-text">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# INPUT FEATURES
# =========================================================

st.markdown(
    '<div class="section-title">📏 Input Features</div>',
    unsafe_allow_html=True
)

feature_cols = st.columns(4)

features = [
    ("🌿", "Sepal Length", "cm"),
    ("🌿", "Sepal Width", "cm"),
    ("🌸", "Petal Length", "cm"),
    ("🌸", "Petal Width", "cm")
]

for col, (icon, name, unit) in zip(feature_cols, features):

    with col:

        st.markdown(
            f"""
            <div class="feature-box">
                {icon} {name}<br>
                <span style="color:#94a3b8;font-size:13px;">
                    Measurement in {unit}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FLOWER SPECIES
# =========================================================

st.markdown(
    '<div class="section-title">🌺 Classification Classes</div>',
    unsafe_allow_html=True
)

species_cols = st.columns(3)

species = [
    ("🌸", "Iris Setosa"),
    ("🌷", "Iris Versicolor"),
    ("🌺", "Iris Virginica")
]

for col, (icon, name) in zip(species_cols, species):

    with col:

        st.markdown(
            f"""
            <div class="feature-box">
                {icon} {name}
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# IMPORTANT NOTE
# =========================================================

st.markdown(
    '<div class="section-title">📌 Model Performance</div>',
    unsafe_allow_html=True
)

st.info(
    "The Logistic Regression model achieved 100% accuracy on the "
    "selected 20% test split (30 samples). This result describes "
    "the evaluation performed on this particular test split."
)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    Iris Flower Classification • BSc Data Science and Analytics
</div>
""", unsafe_allow_html=True)
