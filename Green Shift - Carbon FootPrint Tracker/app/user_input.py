import streamlit as st

def get_user_input():
    st.header("📄 Log Your Daily Activities")
    st.write("---")

    # Capture user's name
    st.subheader("👨‍⚖️ Personal Details")
    user_name = st.text_input(label="Your Name",placeholder="Name")

    # Population Impact
    st.subheader("👪 Population Impact")
    household_size = st.number_input("How many people live in your household?", min_value=1, step=1)
    st.write("---")

    # Transportation
    st.subheader("🚗 Transportation")
    distance_driven = st.number_input("How far did you drive today? (in km)", min_value=0.0, step=1.0)
    fuel_type = st.selectbox("Select the type of fuel used in your vehicle", ["Gasoline", "Diesel", "Electric", "Hybrid"])
    flights_per_year = st.number_input("How many flights do you take per year?", min_value=0, step=1)
    st.write("---")

    # Energy Usage
    st.subheader("⚡ Energy Usage")
    electricity_usage = st.number_input("How much electricity did your household consume today? (in kWh)", min_value=0.0, step=1.0)
    gas_usage = st.number_input("How much natural gas did you use for heating today? (in cubic meters)", min_value=0.0, step=1.0)
    renewable_energy = st.selectbox("Is your household powered by renewable energy sources?", ["Yes", "Partially", "No"])
    home_insulation = st.selectbox("How would you rate your home’s insulation?", ["Excellent", "Good", "Fair", "Poor"])
    st.write("---")

    # Diet
    st.subheader("🍖 | 🌾 Dietary Habits")
    meat_consumption = st.selectbox("Select your daily meat consumption level", ["High", "Moderate", "Low", "Vegetarian", "Vegan"])
    dairy_intake = st.selectbox("How often do you consume dairy products?", ["Daily", "A few times a week", "Rarely", "Never"])
    imported_produce = st.selectbox("How often do you consume imported produce (e.g., avocados, tropical fruits)?", ["Daily", "A few times a week", "Rarely", "Never"]) 
    rice_consumption = st.selectbox("How often do you consume rice?", ["Daily", "A few times a week", "Rarely", "Never"])
    st.write("---")

    # Waste and Recycling
    st.subheader("📦 Waste and Recycling")
    waste_generated = st.number_input("How much waste did you generate today? (in kg)", min_value=0.0, step=1.0)
    recycling_rate = st.slider("What percentage of your waste was recycled?", min_value=0, max_value=100, value=50)
    st.write("---")

    # Water Usage
    st.subheader("🚿 Water Usage")
    water_usage = st.number_input("How much water did your household consume today? (in liters)", min_value=0, max_value=100, step=1)
    st.write("---")

    # Shopping Frequency
    st.subheader("🛒 Shopping and Consumer Goods")
    shopping_frequency = st.selectbox("How frequently do you shop for new items (e.g., clothes, electronics)?", ["Daily", "Weekly", "Monthly", "Rarely"])
    st.write("---")

    # Organize data into a dictionary
    user_data = {
        "user_name": user_name,
        "household_size": household_size,
        "distance_driven": distance_driven,
        "fuel_type": fuel_type,
        "flights_per_year": flights_per_year,
        "electricity_usage": electricity_usage,
        "gas_usage": gas_usage,
        "renewable_energy": renewable_energy,
        "home_insulation": home_insulation,
        "meat_consumption": meat_consumption,
        "dairy_intake": dairy_intake,
        "imported_produce": imported_produce,
        "rice_consumption": rice_consumption,
        "waste_generated": waste_generated,
        "recycling_rate": recycling_rate,
        "water_usage": water_usage,
        "shopping_frequency": shopping_frequency
    }

    return user_data

user_data = get_user_input()

if st.button("Generate My Dashboard"):
    # Send data to the next page (recommendations.py)
    st.session_state['user_data'] = user_data
    st.experimental_rerun()



