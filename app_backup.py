import streamlit as st
import joblib
import random
import os


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("iris_model.pkl")


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Iris Flower Classification",
    page_icon="🌸",
    layout="wide"
)


# =========================================================
# CUSTOM DESIGN
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #fff0f7 0%,
        #f3e8ff 35%,
        #e8f8f0 70%,
        #fff8e1 100%
    );
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 900;
    color: #7b1fa2;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 19px;
    font-weight: 700;
    color: #2e7d32;
    margin-bottom: 25px;
}

.section-title {
    font-size: 27px;
    font-weight: 900;
    color: #8e24aa;
    margin-top: 15px;
    margin-bottom: 10px;
}

.stApp p {
    color: #333333;
}

label {
    color: #6a1b9a !important;
    font-weight: 700 !important;
}

div[data-baseweb="input"] {
    border-radius: 12px;
    border: 2px solid #ce93d8;
    background-color: white;
}

.stButton > button {
    width: 100%;
    min-height: 55px;
    background: linear-gradient(
        90deg,
        #ab47bc,
        #ec407a
    );
    color: white !important;
    border: none;
    border-radius: 15px;
    font-size: 18px;
    font-weight: 900;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #8e24aa,
        #d81b60
    );
    color: white !important;
}

.result-box {
    background: linear-gradient(
        135deg,
        #fce4ec,
        #f3e5f5
    );
    border: 3px solid #ab47bc;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    margin-top: 15px;
}

.result-title {
    color: #6a1b9a;
    font-size: 20px;
    font-weight: 800;
}

.flower-name {
    color: #c2185b;
    font-size: 36px;
    font-weight: 900;
}

.confidence-text {
    color: #2e7d32;
    font-weight: 800;
    font-size: 16px;
}

.project-card {
    background: rgba(255,255,255,0.92);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    border: 2px solid #e1bee7;
    min-height: 140px;
}

.project-card-title {
    color: #8e24aa;
    font-size: 20px;
    font-weight: 900;
}

.project-card-text {
    color: #424242;
    font-size: 15px;
    font-weight: 600;
    line-height: 1.8;
}

.footer {
    text-align: center;
    color: #6a1b9a;
    font-size: 15px;
    font-weight: 700;
    margin-top: 30px;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(
        90deg,
        #ec407a,
        #ab47bc,
        #66bb6a
    );
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🌸 Iris Flower Classification 🌸</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '🌿 Machine Learning Based Flower Species Prediction System 🌿'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# INTRODUCTION
# =========================================================

st.info(
    "🌺 This application uses a Machine Learning model to "
    "predict the species of an Iris flower using its "
    "sepal and petal measurements."
)


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🌿 Enter Flower Measurements</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter the flower measurements in centimeters (cm)."
)


col1, col2 = st.columns(2)


# =========================================================
# LEFT SIDE
# =========================================================

with col1:

    sepal_length = st.number_input(
        "🌿 Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "🍃 Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )


# =========================================================
# RIGHT SIDE
# =========================================================

with col2:

    petal_length = st.number_input(
        "🌸 Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "🌺 Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )


st.write("")


# =========================================================
# PREDICT BUTTON
# =========================================================

predict_button = st.button(
    "🌸 PREDICT FLOWER SPECIES 🌸",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    input_data = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    flower_names = {
        "Iris-setosa": "Setosa",
        "Iris-versicolor": "Versicolor",
        "Iris-virginica": "Virginica"
    }

    flower_name = flower_names.get(
        prediction,
        prediction
    )


    # =====================================================
    # RESULT
    # =====================================================

    st.divider()

    st.markdown(
        '<div class="section-title">🎯 Prediction Result</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="result-box">

            <div class="result-title">
                🌺 Predicted Flower Species
            </div>

            <div class="flower-name">
                Iris {flower_name}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    # =====================================================
    # IMAGE + CONFIDENCE
    # =====================================================

    image_col, confidence_col = st.columns(2)


    # =====================================================
    # FLOWER IMAGE
    # =====================================================

    with image_col:

        st.subheader("🌸 Identified Flower")

        if prediction == "Iris-setosa":

            folder = "images/setosa"

        elif prediction == "Iris-versicolor":

            folder = "images/versicolor"

        elif prediction == "Iris-virginica":

            folder = "images/virginica"

        else:

            folder = None


        if folder and os.path.exists(folder):

            image_files = [
                file
                for file in os.listdir(folder)
                if file.lower().endswith(
                    (".jpg", ".jpeg", ".png")
                )
            ]

            if image_files:

                selected_image = random.choice(
                    image_files
                )

                image_path = os.path.join(
                    folder,
                    selected_image
                )

                st.image(
                    image_path,
                    caption=f"Iris {flower_name}",
                    use_container_width=True
                )

            else:

                st.warning(
                    "No flower images found."
                )

        else:

            st.warning(
                "Flower image folder not found."
            )


    # =====================================================
    # CONFIDENCE
    # =====================================================

    with confidence_col:

        st.subheader("📊 Prediction Confidence")

        classes = model.classes_

        for class_name, probability in zip(
            classes,
            probabilities
        ):

            display_name = flower_names.get(
                class_name,
                class_name
            )

            st.markdown(
                f"""
                <div class="confidence-text">
                    🌸 Iris {display_name} —
                    {probability * 100:.2f}%
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(
                float(probability)
            )


    # =====================================================
    # INPUT SUMMARY
    # =====================================================

    st.divider()

    st.markdown(
        '<div class="section-title">📋 Input Summary</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Sepal Length",
            f"{sepal_length:.1f} cm"
        )

    with c2:
        st.metric(
            "Sepal Width",
            f"{sepal_width:.1f} cm"
        )

    with c3:
        st.metric(
            "Petal Length",
            f"{petal_length:.1f} cm"
        )

    with c4:
        st.metric(
            "Petal Width",
            f"{petal_width:.1f} cm"
        )


# =========================================================
# PROJECT INFORMATION
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">📚 Project Information</div>',
    unsafe_allow_html=True
)


info1, info2, info3 = st.columns(3)


with info1:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-card-title">
        📂 Dataset
        </div>

        <div class="project-card-text">
        Iris Flower Dataset<br>
        150 Samples<br>
        4 Input Features
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with info2:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-card-title">
        🤖 Algorithm
        </div>

        <div class="project-card-text">
        Logistic Regression<br>
        Supervised Learning<br>
        Classification
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with info3:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-card-title">
        🌺 Flower Classes
        </div>

        <div class="project-card-text">
        Iris Setosa<br>
        Iris Versicolor<br>
        Iris Virginica
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# TECHNOLOGIES
# =========================================================

st.write("")

tech1, tech2, tech3, tech4 = st.columns(4)


with tech1:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-card-title">
        🐍 Python
        </div>

        <div class="project-card-text">
        Programming Language
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with tech2:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-card-title">
        📊 Pandas
        </div>

        <div class="project-card-text">
        Data Processing
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with tech3:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-card-title">
        🧠 Scikit-learn
        </div>

        <div class="project-card-text">
        Machine Learning
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with tech4:

    st.markdown(
        """
        <div class="project-card">

        <div class="project-card-title">
        🖥️ Streamlit
        </div>

        <div class="project-card-text">
        Web Application
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        🌸 Iris Flower Classification |
        Machine Learning Mini Project 🌸
        <br>
        Built using Python, Scikit-learn and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)