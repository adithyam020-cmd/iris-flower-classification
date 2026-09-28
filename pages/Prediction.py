import streamlit as st
import joblib
import random
from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Flower Prediction",
    page_icon="🌸",
    layout="wide"
)


# =========================================================
# PROJECT PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "iris_model.pkl"

IMAGE_DIRS = {
    "Iris-setosa": BASE_DIR / "images" / "setosa",
    "Iris-versicolor": BASE_DIR / "images" / "versicolor",
    "Iris-virginica": BASE_DIR / "images" / "virginica"
}


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Background */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(139, 92, 246, 0.20),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(236, 72, 153, 0.18),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #080b16,
            #10182d 50%,
            #080b16
        );
}


/* Container */

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}


/* Heading */

.page-title {
    text-align: center;
    color: white;
    font-size: 46px;
    font-weight: 900;
}


.page-subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 17px;
    margin-bottom: 30px;
}


/* Input section */

.input-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 24px;
    padding: 30px;

    backdrop-filter: blur(15px);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.25);
}


/* Labels */

label {
    color: #e2e8f0 !important;
    font-weight: 700 !important;
}


/* Prediction result */

.result-card {
    margin-top: 30px;

    background:
        linear-gradient(
            135deg,
            rgba(236,72,153,0.15),
            rgba(139,92,246,0.15)
        );

    border: 1px solid rgba(255,255,255,0.15);

    border-radius: 24px;

    padding: 30px;

    text-align: center;
}


.result-title {
    color: #94a3b8;
    font-size: 16px;
}


.result-name {
    color: white;
    font-size: 38px;
    font-weight: 900;
    margin-top: 8px;
}


.confidence {
    color: #f9a8d4;
    font-size: 20px;
    font-weight: 800;
    margin-top: 10px;
}


/* Image card */

.image-card {
    background: rgba(255,255,255,0.06);

    border: 1px solid rgba(255,255,255,0.12);

    border-radius: 24px;

    padding: 20px;

    text-align: center;

    margin-top: 30px;
}


/* Information card */

.info-card {
    background: rgba(255,255,255,0.055);

    border: 1px solid rgba(255,255,255,0.10);

    border-radius: 20px;

    padding: 25px;

    margin-top: 25px;
}


.info-title {
    color: white;

    font-size: 21px;

    font-weight: 800;

    margin-bottom: 15px;
}


.info-text {
    color: #aeb8c8;

    font-size: 15px;

    line-height: 1.7;
}


/* Prediction button */

.stButton > button {

    height: 55px;

    border-radius: 14px;

    border: none;

    background:
        linear-gradient(
            90deg,
            #ec4899,
            #8b5cf6
        );

    color: white;

    font-size: 17px;

    font-weight: 800;

    transition: 0.25s ease;
}


.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 10px 30px
        rgba(139,92,246,0.45);
}


/* Footer */

.footer {
    text-align: center;

    color: #64748b;

    font-size: 14px;

    margin-top: 45px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PAGE HEADER
# =========================================================

st.markdown(
    '<div class="page-title">🌸 Flower Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="page-subtitle">'
    'Enter the flower measurements to predict its Iris species'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# INPUT CARD
# =========================================================

st.markdown(
    '<div class="input-card">',
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='color:white;'>📏 Flower Measurements</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color:#94a3b8;'>"
    "Enter all measurements in centimeters."
    "</p>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    sepal_length = st.number_input(
        "🌿 Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "🌿 Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )


with col2:

    petal_length = st.number_input(
        "🌸 Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "🌸 Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )


st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PREDICT BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

predict_button = st.button(
    "🔮 PREDICT FLOWER SPECIES",
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

    classes = model.classes_

    confidence = max(probabilities) * 100


    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    st.markdown(
        f"""
        <div class="result-card">

            <div class="result-title">
                Predicted Flower Species
            </div>

            <div class="result-name">
                🌸 {prediction}
            </div>

            <div class="confidence">
                Confidence: {confidence:.2f}%
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # FLOWER IMAGE
    # -----------------------------------------------------

    image_folder = IMAGE_DIRS.get(prediction)

    if image_folder and image_folder.exists():

        image_files = [
            file
            for file in image_folder.iterdir()
            if file.suffix.lower() in
            [".jpg", ".jpeg", ".png", ".webp"]
        ]

        if image_files:

            selected_image = random.choice(image_files)

            st.markdown(
                '<div class="image-card">',
                unsafe_allow_html=True
            )

            st.markdown(
                "<h3 style='color:white;'>🌺 Predicted Flower</h3>",
                unsafe_allow_html=True
            )

            st.image(
                str(selected_image),
                width=400
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

    else:

        st.warning(
            "Flower image folder was not found."
        )


    # -----------------------------------------------------
    # CLASS PROBABILITIES
    # -----------------------------------------------------

    st.markdown(
        '<div class="info-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-title">'
        '📊 Prediction Probabilities'
        '</div>',
        unsafe_allow_html=True
    )

    for class_name, probability in zip(classes, probabilities):

        st.write(
            f"**{class_name}** — "
            f"{probability * 100:.2f}%"
        )

        st.progress(
            float(probability)
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # INPUT SUMMARY
    # -----------------------------------------------------

    st.markdown(
        '<div class="info-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-title">'
        '📋 Input Summary'
        '</div>',
        unsafe_allow_html=True
    )

    summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

    with summary_col1:
        st.metric(
            "Sepal Length",
            f"{sepal_length:.1f} cm"
        )

    with summary_col2:
        st.metric(
            "Sepal Width",
            f"{sepal_width:.1f} cm"
        )

    with summary_col3:
        st.metric(
            "Petal Length",
            f"{petal_length:.1f} cm"
        )

    with summary_col4:
        st.metric(
            "Petal Width",
            f"{petal_width:.1f} cm"
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    Iris Flower Classification • BSc Data Science and Analytics
</div>
""", unsafe_allow_html=True)