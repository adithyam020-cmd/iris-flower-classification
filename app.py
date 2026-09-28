import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Iris Flower Classification",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ---------- REMOVE SIDEBAR ---------- */

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stSidebarCollapsedControl"] {
    display: none;
}


/* ---------- MAIN BACKGROUND ---------- */

.stApp {
    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(59, 130, 246, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 20%,
            rgba(139, 92, 246, 0.15),
            transparent 30%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(236, 72, 153, 0.10),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #020617 0%,
            #0f172a 50%,
            #111827 100%
        );
}


/* ---------- PAGE WIDTH ---------- */

.block-container {
    max-width: 1200px;
    padding-top: 30px;
    padding-bottom: 50px;
}


/* ---------- HERO ---------- */

.hero {
    text-align: center;
    padding: 45px 20px 35px 20px;
}

.hero-icon {
    font-size: 70px;
    margin-bottom: 10px;
    filter: drop-shadow(0 0 25px rgba(244,114,182,0.35));
}

.hero-title {
    font-size: 52px;
    line-height: 1.1;
    font-weight: 850;
    letter-spacing: -1.5px;

    background: linear-gradient(
        90deg,
        #60a5fa,
        #a78bfa,
        #f472b6
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #e2e8f0;
    font-size: 21px;
    font-weight: 500;
    margin-top: 15px;
}

.hero-description {
    max-width: 760px;
    margin: 20px auto 0 auto;

    color: #94a3b8;
    font-size: 16px;
    line-height: 1.8;
}


/* ---------- BADGE ---------- */

.badge-container {
    text-align: center;
    margin-top: 5px;
}

.badge {
    display: inline-block;

    padding: 7px 16px;

    border-radius: 30px;

    background: rgba(96,165,250,0.10);

    border: 1px solid rgba(96,165,250,0.25);

    color: #bfdbfe;

    font-size: 13px;
    font-weight: 600;
}


/* ---------- SECTION TITLE ---------- */

.section-title {
    color: #f8fafc;
    font-size: 27px;
    font-weight: 750;

    margin-top: 35px;
    margin-bottom: 18px;
}


/* ---------- NAVIGATION CARDS ---------- */

div.stButton > button {

    width: 100%;
    min-height: 115px;

    border-radius: 18px;

    border: 1px solid rgba(255,255,255,0.10);

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.08),
            rgba(255,255,255,0.025)
        );

    color: #f8fafc;

    font-size: 17px;
    font-weight: 700;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.18);

    transition:
        transform 0.25s ease,
        border-color 0.25s ease,
        background 0.25s ease;
}


div.stButton > button:hover {

    transform: translateY(-5px);

    border-color: rgba(147,197,253,0.55);

    background:
        linear-gradient(
            145deg,
            rgba(96,165,250,0.16),
            rgba(167,139,250,0.08)
        );

    color: #ffffff;

    box-shadow:
        0 12px 35px rgba(59,130,246,0.15);
}


/* ---------- STAT CARDS ---------- */

.stat-card {

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.075),
            rgba(255,255,255,0.025)
        );

    border: 1px solid rgba(255,255,255,0.10);

    border-radius: 18px;

    padding: 22px;

    text-align: center;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.15);
}

.stat-number {
    color: #93c5fd;
    font-size: 31px;
    font-weight: 800;
}

.stat-label {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 5px;
}


/* ---------- INFO CARD ---------- */

.info-card {

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.065),
            rgba(255,255,255,0.025)
        );

    border: 1px solid rgba(255,255,255,0.09);

    border-radius: 20px;

    padding: 28px;

    margin-top: 10px;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.12);
}

.info-heading {
    color: #f8fafc;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 10px;
}

.info-text {
    color: #aebbd0;
    line-height: 1.8;
    font-size: 14px;
}


/* ---------- FEATURE CARDS ---------- */

.feature-card {

    background: rgba(255,255,255,0.045);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 16px;

    padding: 20px;

    text-align: center;

    min-height: 135px;
}

.feature-icon {
    font-size: 30px;
}

.feature-title {
    color: #f8fafc;
    font-size: 15px;
    font-weight: 700;
    margin-top: 8px;
}

.feature-text {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 5px;
}


/* ---------- TECHNOLOGY TAGS ---------- */

.tech-container {
    text-align: center;
    margin-top: 10px;
}

.tech {

    display: inline-block;

    padding: 8px 15px;

    margin: 5px;

    border-radius: 25px;

    background: rgba(96,165,250,0.08);

    border: 1px solid rgba(96,165,250,0.18);

    color: #bfdbfe;

    font-size: 13px;
}


/* ---------- DIVIDER ---------- */

.divider {
    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.15),
            transparent
        );

    margin: 40px 0;
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;

    color: #64748b;

    font-size: 13px;

    line-height: 1.8;

    margin-top: 45px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-icon">🌸</div>

    <div class="badge-container">
        <span class="badge">
            MACHINE LEARNING PROJECT
        </span>
    </div>

    <div class="hero-title">
        Iris Flower Classification
    </div>

    <div class="hero-subtitle">
        Intelligent Flower Species Prediction Using Machine Learning
    </div>

    <div class="hero-description">
        A machine learning application that analyzes four flower
        measurements and predicts the species of an Iris flower.
        Explore the dataset, analyze patterns, understand the model,
        and make real-time predictions through an interactive interface.
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

st.markdown(
    '<div class="section-title">Explore the Project</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button(
        "🌸\n\nMAKE A PREDICTION",
        use_container_width=True
    ):
        st.switch_page("pages/Prediction.py")


with col2:
    if st.button(
        "📊\n\nPROJECT DASHBOARD",
        use_container_width=True
    ):
        st.switch_page("pages/Dashboard.py")


with col3:
    if st.button(
        "📈\n\nDATA ANALYSIS",
        use_container_width=True
    ):
        st.switch_page("pages/Data_Analysis.py")


col4, col5 = st.columns(2)

with col4:
    if st.button(
        "🤖\n\nMODEL INFORMATION",
        use_container_width=True
    ):
        st.switch_page("pages/Model_Information.py")


with col5:
    if st.button(
        "ℹ️\n\nABOUT PROJECT",
        use_container_width=True
    ):
        st.switch_page("pages/About.py")


# =========================================================
# PROJECT STATISTICS
# =========================================================

st.markdown(
    '<div class="section-title">Project at a Glance</div>',
    unsafe_allow_html=True
)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">150</div>
        <div class="stat-label">Dataset Samples</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">4</div>
        <div class="stat-label">Input Features</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-label">Flower Species</div>
    </div>
    """, unsafe_allow_html=True)

with s4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">100%</div>
        <div class="stat-label">Test Accuracy*</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ABOUT THE PROJECT
# =========================================================

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">About the System</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">

    <div class="info-heading">
        🌿 What does this project do?
    </div>

    <div class="info-text">
        The system uses the measurements of an Iris flower's
        sepal and petal to identify its species.
        A Logistic Regression machine learning model is trained
        using the Iris dataset and integrated into a Streamlit
        web application for real-time prediction.
        <br><br>
        Users can enter the four measurements, receive the predicted
        flower species, view the prediction confidence, and explore
        the underlying dataset and machine learning model.
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INPUT FEATURES
# =========================================================

st.markdown(
    '<div class="section-title">🌿 Classification Features</div>',
    unsafe_allow_html=True
)

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📏</div>
        <div class="feature-title">Sepal Length</div>
        <div class="feature-text">
            Flower sepal length measured in centimeters
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📐</div>
        <div class="feature-title">Sepal Width</div>
        <div class="feature-text">
            Flower sepal width measured in centimeters
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌱</div>
        <div class="feature-title">Petal Length</div>
        <div class="feature-text">
            Flower petal length measured in centimeters
        </div>
    </div>
    """, unsafe_allow_html=True)

with f4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌿</div>
        <div class="feature-title">Petal Width</div>
        <div class="feature-text">
            Flower petal width measured in centimeters
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# SPECIES
# =========================================================

st.markdown(
    '<div class="section-title">🌺 Supported Species</div>',
    unsafe_allow_html=True
)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌸</div>
        <div class="feature-title">Iris Setosa</div>
        <div class="feature-text">
            One of the three classes in the dataset
        </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌷</div>
        <div class="feature-title">Iris Versicolor</div>
        <div class="feature-text">
            One of the three classes in the dataset
        </div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌺</div>
        <div class="feature-title">Iris Virginica</div>
        <div class="feature-text">
            One of the three classes in the dataset
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# TECHNOLOGIES
# =========================================================

st.markdown(
    '<div class="section-title">⚙️ Technologies</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="tech-container">

    <span class="tech">Python</span>
    <span class="tech">Pandas</span>
    <span class="tech">NumPy</span>
    <span class="tech">Scikit-learn</span>
    <span class="tech">Logistic Regression</span>
    <span class="tech">Streamlit</span>
    <span class="tech">Matplotlib</span>
    <span class="tech">Joblib</span>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    <b>Iris Flower Classification</b>
    <br>
    Machine Learning • Data Analysis • Interactive Prediction
    <br><br>
    BSc Data Science and Analytics
    <br><br>
    <span style="color:#475569;">
        *100% accuracy refers to the selected 20% test split
        used during model evaluation.
    </span>

</div>
""", unsafe_allow_html=True)