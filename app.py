import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Calorie Calculator - Lakshmi",
    page_icon="🥗",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #fff5e6, #ffe0b2);
    }

    .title {
        text-align: center;
        color: #8B4513;
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #5d4037;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .result-box {
        padding: 25px;
        border-radius: 15px;
        background-color: #ffffff;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
    }

    .footer {
        text-align: center;
        color: #6d4c41;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)


# Title
st.markdown(
    '<div class="title">🥗 Calorie Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Know your estimated daily calorie requirement with Lakshmi 💚</div>',
    unsafe_allow_html=True
)


# Personal details
st.header("👤 Personal Details")

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=20,
    step=1
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

weight = st.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=200.0,
    value=60.0,
    step=0.5
)

height = st.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=220.0,
    value=165.0,
    step=0.5
)


# Activity level
st.header("🏃 Activity Level")

activity = st.selectbox(
    "Select your activity level",
    [
        "Sedentary - little or no exercise",
        "Lightly Active - exercise 1-3 days/week",
        "Moderately Active - exercise 3-5 days/week",
        "Very Active - exercise 6-7 days/week",
        "Extra Active - very intense exercise"
    ]
)


# Activity multipliers
activity_multipliers = {
    "Sedentary - little or no exercise": 1.2,
    "Lightly Active - exercise 1-3 days/week": 1.375,
    "Moderately Active - exercise 3-5 days/week": 1.55,
    "Very Active - exercise 6-7 days/week": 1.725,
    "Extra Active - very intense exercise": 1.9
}


# Calculate button
if st.button("🧮 Calculate Calories", use_container_width=True):

    # BMR calculation using Mifflin-St Jeor equation
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # Daily calorie requirement
    calorie_requirement = bmr * activity_multipliers[activity]

    # Display result
    st.success("Calculation completed successfully! 🎉")

    st.markdown(
        f"""
        <div class="result-box">
            <h2>🔥 Your Estimated Daily Calories</h2>
            <h1>{calorie_requirement:.0f} kcal/day</h1>
            <p>Your estimated BMR is <b>{bmr:.0f} kcal/day</b>.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Interpretation
    st.subheader("💡 Simple Interpretation")

    st.info(
        f"Based on the details you entered, your estimated daily "
        f"calorie requirement is approximately "
        f"{calorie_requirement:.0f} kcal per day."
    )

    st.warning(
        "This is only an estimate for educational purposes. "
        "Actual calorie needs can vary from person to person."
    )


# Footer
st.markdown(
    '<div class="footer">🥗 Calorie Calculator • Created by Lakshmi</div>',
    unsafe_allow_html=True
)