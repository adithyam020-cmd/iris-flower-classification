import streamlit as st
import joblib
import os
import random
import pandas as pd


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM DESIGN
# =========================================================

st.markdown("""
<style>

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

.stApp {
    background:
        radial-gradient(
            circle at 8% 10%,
            rgba(255, 190, 220, 0.42),
            transparent 25%
        ),
        radial-gradient(
            circle at 92% 15%,
            rgba(205, 190, 255, 0.38),
            transparent 25%
        ),
        radial-gradient(
            circle at 50% 95%,
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

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    color: #633b72 !important;
}

p {
    color: #665a6d;
}

.stNumberInput label {
    color: #633b72 !important;
    font-weight: 700 !important;
}

.stNumberInput input {
    color: #43364b !important;
    background: white !important;
    border-radius: 12px !important;
}

.stButton {
    text-align: center;
}

.stButton > button {
    border: none !important;
    border-radius: 35px !important;
    background: linear-gradient(
        135deg,
        #d85c9f,
        #8d68d8
    ) !important;
    color: white !important;
    font-size: 17px !important;
    font-weight: 800 !important;
    padding: 0.65rem 2rem !important;
    box-shadow: 0 8px 20px rgba(130, 90, 180, 0.20);
}

.stButton > button:hover {
    transform: translateY(-2px);
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.78);
    border: 1px solid rgba(255, 255, 255, 0.95);
    border-radius: 22px;
    box-shadow: 0 8px 25px rgba(80, 50, 90, 0.08);
}

[data-testid="stImage"] {
    border-radius: 18px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FIND PROJECT FOLDER
# =========================================================

CURRENT_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    CURRENT_FOLDER,
    "iris_model.pkl"
)

IMAGE_FOLDER = os.path.join(
    CURRENT_FOLDER,
    "images"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    return joblib.load(MODEL_PATH)


model = load_model()


# =========================================================
# PAGE TITLE
# =========================================================

st.title("🌸 Iris Flower Prediction")

st.markdown(
    "### Enter the flower measurements and let the Machine Learning model identify the Iris species."
)

st.write("")


# =========================================================
# MEASUREMENTS
# =========================================================

with st.container(border=True):

    st.subheader("🌿 Enter Flower Measurements")

    st.write(
        "Enter the four flower measurements in centimeters."
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        sepal_length = st.number_input(
            "🌿 Sepal Length (cm)",
            min_value=0.0,
            max_value=10.0,
            value=5.1,
            step=0.1,
            format="%.1f"
        )

        sepal_width = st.number_input(
            "🌿 Sepal Width (cm)",
            min_value=0.0,
            max_value=10.0,
            value=3.5,
            step=0.1,
            format="%.1f"
        )

    with col2:

        petal_length = st.number_input(
            "🌸 Petal Length (cm)",
            min_value=0.0,
            max_value=10.0,
            value=1.4,
            step=0.1,
            format="%.1f"
        )

        petal_width = st.number_input(
            "🌸 Petal Width (cm)",
            min_value=0.0,
            max_value=10.0,
            value=0.2,
            step=0.1,
            format="%.1f"
        )


# =========================================================
# PREDICT BUTTON
# =========================================================

st.write("")

button_col1, button_col2, button_col3 = st.columns(
    [1, 1, 1]
)

with button_col2:

    predict_button = st.button(
        "🔮 Predict Flower",
        use_container_width=True
    )


# =========================================================
# SPECIES INFORMATION
# =========================================================

species_info = {

    "Iris-setosa": {
        "name": "Iris Setosa",
        "emoji": "🌼",
        "folder": "setosa",
        "description": "A small Iris flower with narrow petals."
    },

    "Iris-versicolor": {
        "name": "Iris Versicolor",
        "emoji": "🌷",
        "folder": "versicolor",
        "description": "An Iris species with medium-sized petals."
    },

    "Iris-virginica": {
        "name": "Iris Virginica",
        "emoji": "🌺",
        "folder": "virginica",
        "description": "A larger Iris species with longer petals."
    }

}


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # -----------------------------------------------------
    # CREATE DATAFRAME
    # -----------------------------------------------------

    input_data = pd.DataFrame(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]],
        columns=[
            "SepalLengthCm",
            "SepalWidthCm",
            "PetalLengthCm",
            "PetalWidthCm"
        ]
    )

    # -----------------------------------------------------
    # PREDICT
    # -----------------------------------------------------

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    confidence = max(probabilities) * 100

    result = species_info[prediction]


    # =====================================================
    # RESULT
    # =====================================================

    st.write("")
    st.write("")

    with st.container(border=True):

        st.subheader("🌸 Prediction Result")

        st.write("")

        result_col1, result_col2 = st.columns(2)


        # -------------------------------------------------
        # FIND FLOWER IMAGE
        # -------------------------------------------------

        with result_col1:

            flower_folder = os.path.join(
                IMAGE_FOLDER,
                result["folder"]
            )

            image_files = []

            if os.path.exists(flower_folder):

                for file in os.listdir(flower_folder):

                    if file.lower().endswith(
                        (".jpg", ".jpeg", ".png")
                    ):

                        image_files.append(
                            os.path.join(
                                flower_folder,
                                file
                            )
                        )


            # ---------------------------------------------
            # DISPLAY IMAGE
            # ---------------------------------------------

            if len(image_files) > 0:

                selected_image = random.choice(
                    image_files
                )

                st.image(
                    selected_image,
                    caption=result["name"],
                    use_container_width=True
                )

            else:

                st.info(
                    "Flower image not found."
                )


        # -------------------------------------------------
        # RESULT INFORMATION
        # -------------------------------------------------

        with result_col2:

            st.write("")
            st.write("")

            st.subheader(
                result["emoji"] + " " + result["name"]
            )

            st.write(
                result["description"]
            )

            st.write("")

            st.write(
                "### 🎯 Prediction Confidence"
            )

            st.progress(
                int(confidence)
            )

            st.write(
                f"**Confidence: {confidence:.2f}%**"
            )


# =========================================================
# HOW IT WORKS
# =========================================================

st.write("")
st.write("")

st.subheader("⚙️ How The Prediction Works")

st.write(
    "The system follows four simple Machine Learning steps."
)

st.write("")

step1, step2, step3, step4 = st.columns(4)


with step1:

    with st.container(border=True):

        st.subheader("1️⃣ Input")

        st.write(
            "Enter the four flower measurements."
        )


with step2:

    with st.container(border=True):

        st.subheader("2️⃣ Prepare")

        st.write(
            "The measurements are prepared for the model."
        )


with step3:

    with st.container(border=True):

        st.subheader("3️⃣ Predict")

        st.write(
            "Logistic Regression analyzes the measurements."
        )


with step4:

    with st.container(border=True):

        st.subheader("4️⃣ Result")

        st.write(
            "The predicted Iris species is displayed."
        )


# =========================================================
# MEASUREMENT INFORMATION
# =========================================================

st.write("")

with st.container(border=True):

    st.subheader("📖 Understanding The Measurements")

    info1, info2 = st.columns(2)

    with info1:

        st.markdown("**🌿 Sepal Length**")

        st.write(
            "The length of the sepal measured in centimeters."
        )

        st.markdown("**🌿 Sepal Width**")

        st.write(
            "The width of the sepal measured in centimeters."
        )


    with info2:

        st.markdown("**🌸 Petal Length**")

        st.write(
            "The length of the petal measured in centimeters."
        )

        st.markdown("**🌸 Petal Width**")

        st.write(
            "The width of the petal measured in centimeters."
        )


# =========================================================
# MODEL INFORMATION
# =========================================================

st.write("")

with st.container(border=True):

    st.subheader("🤖 Model Information")

    model_col1, model_col2, model_col3 = st.columns(3)

    with model_col1:

        st.write("**Algorithm**")

        st.write("Logistic Regression")


    with model_col2:

        st.write("**Input Features**")

        st.write("4 Flower Measurements")


    with model_col3:

        st.write("**Output Classes**")

        st.write("3 Iris Species")


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")

st.caption(
    "🌸 Iris Flower Classification • Powered by Machine Learning • Logistic Regression"
)