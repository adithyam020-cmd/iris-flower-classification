import streamlit as st
import os
import random

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Iris Flower Classification",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS ONLY
# ============================================================

st.markdown("""
<style>

/* Hide Streamlit default elements */
#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stSidebar"] {
    display: none;
}

/* Main background */
.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(255, 190, 220, 0.45),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(205, 190, 255, 0.40),
            transparent 25%
        ),
        radial-gradient(
            circle at 50% 90%,
            rgba(190, 240, 210, 0.35),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #fff8fc,
            #f8f4ff,
            #f3fff8
        );
}

/* Main width */
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* All normal text */
.stMarkdown,
.stMarkdown p,
.stMarkdown span {
    color: #5d5065;
}

/* Main title */
.main-title {
    font-size: 48px;
    font-weight: 900;
    color: #633b72;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 10px;
}

/* Subtitle */
.main-subtitle {
    font-size: 18px;
    color: #796c80;
    text-align: center;
    line-height: 1.7;
    margin-bottom: 25px;
}

/* Section titles */
.section-title {
    font-size: 30px;
    font-weight: 850;
    color: #633b72;
    text-align: center;
    margin-top: 45px;
    margin-bottom: 5px;
}

.section-subtitle {
    font-size: 14px;
    color: #817485;
    text-align: center;
    margin-bottom: 25px;
}

/* Start button */
.stButton {
    text-align: center;
}

.stButton > button {
    border: none !important;
    border-radius: 40px !important;
    background: linear-gradient(
        135deg,
        #d85c9f,
        #8d68d8
    ) !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    padding: 0.65rem 2.5rem !important;
    box-shadow: 0 10px 25px rgba(130, 90, 180, 0.25);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 30px rgba(130, 90, 180, 0.35);
}

/* Streamlit bordered containers */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.70);
    border: 1px solid rgba(255, 255, 255, 0.95);
    border-radius: 22px;
    box-shadow: 0 8px 25px rgba(80, 50, 90, 0.07);
}

/* Card headings */
.card-heading {
    font-size: 19px;
    font-weight: 800;
    color: #633b72;
}

.card-text {
    font-size: 14px;
    color: #6d6072;
    line-height: 1.7;
}

/* Species images */
[data-testid="stImage"] {
    border-radius: 18px;
}

/* Caption */
.stCaption {
    color: #817485 !important;
}

/* Divider */
hr {
    border: none;
    height: 1px;
    background: rgba(110, 80, 120, 0.12);
    margin: 35px 0;
}

/* Footer */
.footer-text {
    text-align: center;
    color: #8b7e90;
    font-size: 13px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    '<div class="main-title">🌸 Iris Flower Classification 🌸</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="main-subtitle">
        Discover the species of an Iris flower using
        Machine Learning and physical measurements.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")


# ============================================================
# START PROJECT
# ============================================================

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🚀 Start Project", use_container_width=True):
        st.switch_page("pages/Prediction.py")


st.write("")
st.write("")


# ============================================================
# ABOUT THE PROJECT
# ============================================================

st.markdown(
    '<div class="section-title">🌺 About The Project</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Turning flower measurements into intelligent predictions</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    st.markdown(
        '<div class="card-heading">🌸 What is Iris Flower Classification?</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        Iris Flower Classification is a Machine Learning project
        that predicts the species of an Iris flower using four
        physical measurements.

        The model uses:

        **🌿 Sepal Length   •   🌿 Sepal Width   •   🌸 Petal Length   •   🌸 Petal Width**

        The flower is classified into one of three species:

        **Iris Setosa, Iris Versicolor, or Iris Virginica.**

        This project demonstrates how data analysis, Machine Learning
        and an interactive web application can work together.
        """
    )


# ============================================================
# WHY THIS PROJECT
# ============================================================

st.markdown(
    '<div class="section-title">💡 Why This Project?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Understanding the purpose behind the project</div>',
    unsafe_allow_html=True
)

reason1, reason2, reason3, reason4 = st.columns(4)

with reason1:
    with st.container(border=True):
        st.markdown("### 📊 Data Analysis")
        st.write(
            "Explore flower measurements and discover patterns "
            "inside the dataset."
        )

with reason2:
    with st.container(border=True):
        st.markdown("### 🤖 Machine Learning")
        st.write(
            "Train a classification model that learns from "
            "existing flower measurements."
        )

with reason3:
    with st.container(border=True):
        st.markdown("### 🔮 Prediction")
        st.write(
            "Use the trained model to predict the species "
            "of a new Iris flower."
        )

with reason4:
    with st.container(border=True):
        st.markdown("### 💻 Real Application")
        st.write(
            "Turn a Machine Learning model into an interactive "
            "web application."
        )


# ============================================================
# REAL LIFE APPLICATIONS
# ============================================================

st.markdown(
    '<div class="section-title">🌍 Real-Life Applications</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Where similar Machine Learning concepts can be useful</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    st.markdown("### 🌱 Automated Classification")

    st.write(
        "Automated classification is useful when large amounts "
        "of biological or environmental data need to be analyzed."
    )

    st.write("")

    st.markdown("🌿 **Botanical Research**")
    st.write(
        "Machine Learning can support plant species identification "
        "and biological analysis."
    )

    st.markdown("🌾 **Agriculture**")
    st.write(
        "Data-driven systems can analyze measurable characteristics "
        "of plants and crops."
    )

    st.markdown("🔬 **Biological Research**")
    st.write(
        "Classification techniques can help researchers identify "
        "patterns in biological measurements."
    )

    st.markdown("📷 **Computer Vision**")
    st.write(
        "Similar classification concepts can be combined with "
        "images for automated species recognition."
    )

    st.markdown("🌳 **Environmental Monitoring**")
    st.write(
        "Machine Learning can support biodiversity and ecological "
        "monitoring systems."
    )


# ============================================================
# IRIS SPECIES
# ============================================================

st.markdown(
    '<div class="section-title">🌼 The Three Iris Species</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">The model recognizes these three flower categories</div>',
    unsafe_allow_html=True
)

species_data = [
    ("setosa", "🌼", "Iris Setosa"),
    ("versicolor", "🌷", "Iris Versicolor"),
    ("virginica", "🌺", "Iris Virginica")
]

species_columns = st.columns(3)

for column, (folder, emoji, name) in zip(species_columns, species_data):

    with column:

        image_folder = os.path.join("images", folder)

        image_files = []

        if os.path.exists(image_folder):

            image_files = [
                os.path.join(image_folder, file)
                for file in os.listdir(image_folder)
                if file.lower().endswith(
                    (".jpg", ".jpeg", ".png")
                )
            ]

        if image_files:

            selected_image = random.choice(image_files)

            st.image(
                selected_image,
                use_container_width=True
            )

        with st.container(border=True):

            st.markdown(f"### {emoji} {name}")

            st.write(
                "One of the three Iris species that can be "
                "identified by the Machine Learning model."
            )


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown(
    '<div class="section-title">⚙️ How It Works</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">From flower measurements to classification</div>',
    unsafe_allow_html=True
)

step1, step2, step3, step4, step5 = st.columns(5)

steps = [
    ("🌿", "Measurements", "Enter four flower measurements."),
    ("📊", "Processing", "Prepare the values for the model."),
    ("🤖", "ML Model", "The trained model analyzes the measurements."),
    ("🔮", "Prediction", "The flower species is predicted."),
    ("🌸", "Result", "The predicted flower and confidence are displayed.")
]

for column, (icon, title, description) in zip(
    [step1, step2, step3, step4, step5],
    steps
):

    with column:

        with st.container(border=True):

            st.markdown(f"### {icon}")

            st.markdown(f"**{title}**")

            st.caption(description)


# ============================================================
# TECHNOLOGY
# ============================================================

st.markdown(
    '<div class="section-title">🛠 Technology Used</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Tools used to build this project</div>',
    unsafe_allow_html=True
)

tech1, tech2, tech3 = st.columns(3)

with tech1:
    with st.container(border=True):
        st.markdown("### 🐍 Python")
        st.write(
            "Programming language used for data processing "
            "and Machine Learning."
        )

with tech2:
    with st.container(border=True):
        st.markdown("### 📚 Pandas & NumPy")
        st.write(
            "Used for dataset handling, numerical operations "
            "and analysis."
        )

with tech3:
    with st.container(border=True):
        st.markdown("### 🤖 Scikit-learn")
        st.write(
            "Used to train the Logistic Regression classification model."
        )

tech4, tech5, tech6 = st.columns(3)

with tech4:
    with st.container(border=True):
        st.markdown("### 📈 Matplotlib & Seaborn")
        st.write(
            "Used to visualize patterns and relationships in the data."
        )

with tech5:
    with st.container(border=True):
        st.markdown("### 🌐 Streamlit")
        st.write(
            "Used to create the interactive web application."
        )

with tech6:
    with st.container(border=True):
        st.markdown("### 💾 Joblib")
        st.write(
            "Used to save and load the trained Machine Learning model."
        )


# ============================================================
# FINAL MESSAGE
# ============================================================

st.write("")
st.write("")

with st.container(border=True):

    st.markdown(
        """
        ### 🌸 Ready To Identify Your Iris Flower?

        Click **🚀 Start Project** at the top of the page and
        enter the flower measurements to get a Machine Learning prediction.
        """
    )
# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer-text">
        🌸 Iris Flower Classification
        <br>
        Machine Learning • Data Analysis • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)