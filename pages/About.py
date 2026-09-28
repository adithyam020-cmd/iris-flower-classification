import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="About Project",
    page_icon="👥",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #fce4ec 0%, transparent 35%),
        radial-gradient(circle at bottom right, #e8eaf6 0%, transparent 35%),
        linear-gradient(135deg, #ffffff 0%, #f8f9fc 100%);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.title {
    color: #111111;
    font-size: 42px;
    font-weight: 900;
}

.subtitle {
    color: #555555;
    font-size: 18px;
    margin-bottom: 25px;
}

.section-title {
    color: #111111;
    font-size: 25px;
    font-weight: 900;
    margin-top: 25px;
    margin-bottom: 15px;
}

.card {
    background: white;
    border: 1px solid #dddddd;
    border-radius: 18px;
    padding: 25px;
    min-height: 150px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    text-align: center;
}

.card-title {
    color: #111111;
    font-size: 21px;
    font-weight: 900;
}

.card-text {
    color: #555555;
    font-size: 15px;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="title">👥 About the Project</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Iris Flower Classification using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# PROJECT INTRODUCTION
# =========================================================

st.markdown(
    '<div class="section-title">🌸 Project Introduction</div>',
    unsafe_allow_html=True
)

st.write("""
The Iris Flower Classification project is a machine learning
application developed to identify the species of an Iris flower
based on its physical measurements.

The system uses four measurements — sepal length, sepal width,
petal length and petal width — to classify a flower into one of
three species: Iris Setosa, Iris Versicolor or Iris Virginica.
""")


# =========================================================
# OBJECTIVE
# =========================================================

st.markdown(
    '<div class="section-title">🎯 Project Objective</div>',
    unsafe_allow_html=True
)

st.write("""
The main objectives of this project are:

- To understand the fundamentals of machine learning classification.
- To work with a real-world dataset.
- To preprocess and analyze the Iris dataset.
- To train a classification model.
- To evaluate the performance of the trained model.
- To develop an interactive web application using Streamlit.
- To demonstrate how machine learning can be used for automated classification.
""")


# =========================================================
# TECHNOLOGIES
# =========================================================

st.markdown(
    '<div class="section-title">🛠️ Technologies Used</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

technologies = [
    ("🐍", "Python", "Programming Language"),
    ("🐼", "Pandas", "Data Processing"),
    ("🤖", "Scikit-learn", "Machine Learning"),
    ("📊", "Matplotlib", "Data Visualization")
]

columns = [col1, col2, col3, col4]

for column, technology in zip(columns, technologies):

    with column:

        st.markdown(
            f"""
            <div class="card">

                <div style="font-size:32px;">
                    {technology[0]}
                </div>

                <div class="card-title">
                    {technology[1]}
                </div>

                <div class="card-text">
                    {technology[2]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


st.write("")


col1, col2, col3 = st.columns(3)

technologies_2 = [
    ("🌐", "Streamlit", "Web Application"),
    ("💾", "Joblib", "Model Storage"),
    ("📈", "NumPy", "Numerical Computing")
]

columns_2 = [col1, col2, col3]

for column, technology in zip(columns_2, technologies_2):

    with column:

        st.markdown(
            f"""
            <div class="card">

                <div style="font-size:32px;">
                    {technology[0]}
                </div>

                <div class="card-title">
                    {technology[1]}
                </div>

                <div class="card-text">
                    {technology[2]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# PROJECT TEAM
# =========================================================

st.markdown(
    '<div class="section-title">👨‍💻 Project Team</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">

        <div style="font-size:35px;">
            👨‍💻
        </div>

        <div class="card-title">
            Adithya M
        </div>

        <div class="card-text">
            BSc Data Science and Analytics
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">

        <div style="font-size:35px;">
            👨‍💻
        </div>

        <div class="card-title">
            Deva Surya C A
        </div>

        <div class="card-text">
            BSc Data Science and Analytics
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FUTURE SCOPE
# =========================================================

st.markdown(
    '<div class="section-title">🚀 Future Scope</div>',
    unsafe_allow_html=True
)

st.write("""
The project can be extended in several ways:

- Use additional machine learning algorithms.
- Compare the performance of different models.
- Add more flower species.
- Improve the user interface.
- Add image-based flower classification.
- Deploy the application for wider public use.
- Add automated model evaluation and comparison.
""")


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Iris Flower Classification • BSc Data Science and Analytics"
)