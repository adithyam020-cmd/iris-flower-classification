import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="Data Analysis",
    page_icon="📊",
    layout="wide"
)


# ==============================
# LOAD DATASET
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "Iris.csv"


@st.cache_data
def get_data():
    return pd.read_csv(DATA_FILE)


df = get_data()


# ==============================
# PAGE DESIGN
# ==============================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #1e1b4b
    );
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #93c5fd;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 17px;
    margin-bottom: 35px;
}

.card {
    background: rgba(255,255,255,0.08);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.12);
}

.number {
    font-size: 30px;
    font-weight: bold;
    color: #60a5fa;
}

.text {
    color: #cbd5e1;
    font-size: 14px;
}

.section {
    font-size: 26px;
    font-weight: bold;
    color: white;
    margin-top: 35px;
    margin-bottom: 15px;
}

.insight {
    background: rgba(255,255,255,0.07);
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 12px;
    color: #e2e8f0;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="title">📊 Data Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Explore the Iris dataset and understand its characteristics'
    '</div>',
    unsafe_allow_html=True
)


# ==============================
# OVERVIEW
# ==============================

st.markdown(
    '<div class="section">Dataset Overview</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class="card">
            <div class="number">{len(df)}</div>
            <div class="text">Samples</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="card">
            <div class="number">4</div>
            <div class="text">Features</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="card">
            <div class="number">{df["Species"].nunique()}</div>
            <div class="text">Species</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:

    missing_values = df.isnull().sum().sum()

    st.markdown(
        f"""
        <div class="card">
            <div class="number">{missing_values}</div>
            <div class="text">Missing Values</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==============================
# DATA PREVIEW
# ==============================

st.markdown(
    '<div class="section">🔍 Dataset Preview</div>',
    unsafe_allow_html=True
)

st.dataframe(
    df.head(10),
    use_container_width=True
)


# ==============================
# SPECIES COUNT
# ==============================

st.markdown(
    '<div class="section">🌸 Species Distribution</div>',
    unsafe_allow_html=True
)

species_count = df["Species"].value_counts()

fig, ax = plt.subplots()

ax.bar(
    species_count.index,
    species_count.values
)

ax.set_xlabel("Species")
ax.set_ylabel("Number of Samples")
ax.set_title("Iris Species Distribution")

st.pyplot(fig)

plt.close(fig)


# ==============================
# FEATURE STATISTICS
# ==============================

st.markdown(
    '<div class="section">📐 Feature Statistics</div>',
    unsafe_allow_html=True
)

features = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm"
]

st.dataframe(
    df[features].describe().round(2),
    use_container_width=True
)


# ==============================
# FEATURE SELECTOR
# ==============================

st.markdown(
    '<div class="section">📈 Feature Analysis</div>',
    unsafe_allow_html=True
)

selected_feature = st.selectbox(
    "Select a feature",
    features
)


# ==============================
# FEATURE BY SPECIES
# ==============================

average_values = df.groupby("Species")[selected_feature].mean()

fig2, ax2 = plt.subplots()

ax2.bar(
    average_values.index,
    average_values.values
)

ax2.set_xlabel("Species")
ax2.set_ylabel("Average Value")
ax2.set_title(
    "Average " + selected_feature + " by Species"
)

st.pyplot(fig2)

plt.close(fig2)


# ==============================
# PETAL RELATIONSHIP
# ==============================

st.markdown(
    '<div class="section">🔬 Petal Measurements</div>',
    unsafe_allow_html=True
)

fig3, ax3 = plt.subplots()

for species in df["Species"].unique():

    species_data = df[df["Species"] == species]

    ax3.scatter(
        species_data["PetalLengthCm"],
        species_data["PetalWidthCm"],
        label=species
    )

ax3.set_xlabel("Petal Length (cm)")
ax3.set_ylabel("Petal Width (cm)")
ax3.set_title("Petal Length vs Petal Width")
ax3.legend()

st.pyplot(fig3)

plt.close(fig3)


# ==============================
# KEY INSIGHTS
# ==============================

st.markdown(
    '<div class="section">💡 Key Insights</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="insight">
    <b>🌱 Dataset:</b>
    The dataset contains 150 Iris flower samples.
    </div>

    <div class="insight">
    <b>🌸 Species:</b>
    There are three species: Iris-setosa,
    Iris-versicolor and Iris-virginica.
    </div>

    <div class="insight">
    <b>📏 Features:</b>
    The model uses sepal length, sepal width,
    petal length and petal width.
    </div>

    <div class="insight">
    <b>🔬 Observation:</b>
    Petal measurements show noticeable differences
    between the three species.
    </div>

    <div class="insight">
    <b>✅ Data Quality:</b>
    The dataset contains no missing values.
    </div>
    """,
    unsafe_allow_html=True
)


# ==============================
# FOOTER
# ==============================

st.markdown(
    """
    <br>
    <p style="text-align:center;color:#94a3b8;">
    Iris Flower Classification • Data Analysis
    </p>
    """,
    unsafe_allow_html=True
)