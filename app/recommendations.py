import streamlit as st
import pandas as pd
import numpy as np
import emissionCalc as ec
import generateReport as gr
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from statsmodels.tsa.arima.model import ARIMA

# Check if user_data exists in session_state
if 'user_data' in st.session_state:
    user_data = st.session_state['user_data']

    # Personalized greeting
    st.title(f"🌍 Hi {user_data['user_name']}! See your Carbon Status 🏭.")
    st.write("**Analyze your carbon footprint and discover actionable ways to reduce your impact.**")
    st.write("---")

    # Calculate current emission
    current_emission = ec.calculate_current_emission(user_data)

    # Emission alert metric
    col1, col2, col3 = st.columns([4, 4, 5])
    with col1:
        if current_emission > 70:  # Threshold for high emission
            st.metric("Total Current Emission with houshold (kg CO2 Per Day)", f"{current_emission:.2f}", "🔴 High Depletion of Environment")
        elif 30 <= current_emission <= 70:  # Medium threshold
            st.metric("Total Current Emission with houshold (kg CO2)", f"{current_emission:.2f}", "🟠 Moderate Depletion of Environment")
        else:
            st.metric("Total Current Emission with houshold (kg CO2)", f"{current_emission:.2f}", "🟢 Low Depletion of Environment")

    # Breakdown and Savings
    with col2:
        st.subheader("🌱 Your Carbon Footprint Breakdown & Savings")
        savings_messages = []
        if user_data["distance_driven"] < 10:
            savings_messages.append("🚗 By driving less, you save ~0.2 kg CO2 per km!")
        if user_data["electricity_usage"] < 10:
            savings_messages.append("💡 By using energy-efficient appliances, you save ~0.3 kg CO2 per kWh!")
        if user_data["flights_per_year"] == 0:
            savings_messages.append("✈️ Avoiding flights saves ~1.5 kg CO2 per flight!")
        
        for msg in savings_messages:
            st.success(msg)

        if not savings_messages:
            st.info("Your actions reflect high resource consumption. Consider ways to reduce emissions.")

    # Carbon Impact Category using Clustering
    with col3:
        st.subheader("🧬 User Carbon Impact Category")
        # Real-world emission data (metric tons per year)
        emission_data = np.array([[1.9], [7.6], [14.6]])
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(emission_data)

        # User's current emission
        current_emission = 8  # Example user input
        user_cluster = kmeans.predict([[current_emission]])

        # Define categories
        categories = ["Low Impact", "Medium Impact", "High Impact"]
        st.metric("Your Carbon Impact Category (at Global Levels)", categories[user_cluster[0]])

    # Additional Components
    st.write("---")
    
    # Future Emission Forecast
    st.header("📊 Future Emission Forecast")
    forecast_col, co2_col = st.columns([5, 5])
    
    with forecast_col:
        st.subheader("Projected Carbon Emission Over Next 5 Years")
        years = np.array([2024, 2025, 2026, 2027, 2028]).reshape(-1, 1)
        reg_model = LinearRegression()
        reg_model.fit(years, np.array([current_emission * (1 + 0.02 * i) for i in range(5)]))
        future_emissions = reg_model.predict(years)

        future_data = pd.DataFrame({"Year": ["Year " + str(2025 + i) for i in range(1, 6)],
                                    "Projected Emission": future_emissions})
        st.bar_chart(future_data.set_index("Year"), height=300)

    # Climate Trends (CO2 Levels)
    with co2_col:
        st.subheader("🌍 Climate Trends (CO2 Levels)")
        co2_levels = [400, 420, 440, 460, 480]
        arima_model = ARIMA(co2_levels, order=(1, 1, 1))
        arima_model_fit = arima_model.fit()
        co2_forecast = arima_model_fit.forecast(steps=5)

        forecast_data = pd.DataFrame({"Year": ["Year " + str(2019 + i) for i in range(1, 6)], 
                                      "CO2 Levels (ppm)": co2_forecast})
        st.line_chart(forecast_data.set_index("Year"), height=300)

    # Additional Features
    st.write("---")
    emission, savings, category = st.columns([5, 5, 5])
    # Sector Contribution
    with emission:
        st.subheader("🏗️ Emission Contribution by Sector")
        sector_data = pd.DataFrame({
            "Sector": ["Transportation", "Electricity", "Flights", "Others"],
            "Emissions": [user_data["distance_driven"] * 0.2, 
                        user_data["electricity_usage"] * 0.3, 
                        user_data["flights_per_year"] * 1.5, 
                        current_emission * 0.1]
        })
        st.bar_chart(sector_data.set_index("Sector"))

    # Global Comparison
    with savings:    
        # Use a constant value for global emissions (53 billion metric tons per year)
        global_emission_yearly_metric_tons = 53 * 1e9  # 53 billion metric tons per year

        # Convert global emissions from metric tons to kg (1 metric ton = 1000 kg)
        global_emission_yearly_kg = global_emission_yearly_metric_tons * 1000  # Convert to kg

        # Convert global emissions from yearly to daily
        global_emission_daily_kg = global_emission_yearly_kg / 365  # Convert to daily value in kg

        # Calculate current emission (using a function from emissionCalc module)
        current_emission = ec.calculate_current_emission(user_data)

        # Display emission metrics
        st.metric("Your Daily Emission (kg CO2)", f"{current_emission:.2f}")


        st.metric("Global Average Daily Emission (kg CO2)", f"{global_emission_daily_kg:.2f}")

        # Compare user emission with global daily average
        if current_emission > global_emission_daily_kg:
            st.warning("Your emission is above the global daily average! Consider reducing it.")
        else:
            st.success("Great! Your emission is below the global daily average.")

    with category:
        # Interactive Recommendations
        st.subheader("💡 What-If Analysis")
        electricity_usage = user_data.get("electricity_usage", 10)  # Default value if key is missing

    
        if isinstance(electricity_usage, list) and len(electricity_usage) == 2:
        # If `electricity_usage` is a list, use a range slider
            slider = st.slider(
                "Select Electricity Usage Range (kWh)",
                min_value=0,
                max_value=100,
                value=electricity_usage,  # Expecting [low, high]
                step=1
            )
        else:
            # Otherwise, use a single value slider
            slider = st.slider(
                "Reduce Electricity Usage (kWh)",
                min_value=0,
                max_value=100,
                value=int(electricity_usage),  # Single integer fallback
                step=1
            )
        st.info(f"By reducing electricity usage to {slider} kWh, you save ~{(user_data['electricity_usage'] - slider) * 0.3:.2f} kg CO2.")

        # Let's consider reducing the number of children or adults and see the potential CO2 savings
        # Fetching household population from user data
        household_size = user_data.get("household_size", 0)  # Default to 4 if missing

        # Average CO2 emissions per person (adult), this can vary depending on lifestyle.
        # For simplicity, assume each adult emits 15 tons of CO2 per year (this is a rough global estimate for an average adult).
        adult_emission_per_year = 15  # in tons of CO2

        # Child's annual CO2 emission
        child_emission_per_year = 58.3  # in tons of CO2

        # Interactive sliders to adjust the number of children and household members
        adults_in_household = st.slider("Number of Adults in Household", min_value=1, max_value=10, value=household_size - 1, step=1)
        children_in_household = st.slider("Number of Children in Household", min_value=0, max_value=5, value=household_size - adults_in_household, step=1)

        # Calculating the total CO2 emissions for the household based on the number of adults and children
        total_adult_emissions = adults_in_household * adult_emission_per_year
        total_child_emissions = children_in_household * child_emission_per_year
        total_household_emissions = total_adult_emissions + total_child_emissions

        population_reduction = st.slider("Reduce Household Population (Number of People)", min_value=1, max_value=household_size, value=1, step=1)

        # Simulate reducing the population (either reduce children or adults)
        reduced_household_emissions = (adults_in_household - population_reduction) * adult_emission_per_year + (children_in_household - population_reduction) * child_emission_per_year

        # Calculate the savings
        emission_savings = total_household_emissions - reduced_household_emissions

        st.write("---")
        # Display the reduction
        st.info(f"By reducing the household population by **{population_reduction} person(s)**, you could save approximately **{emission_savings:.2f} tons CO2 annually**.")

        # Highlight the importance of mitigation
        if household_size <= 2:
            st.warning("🌱 **Low Population Household**: Small households (e.g., only 1-2 people) are more efficient in reducing carbon emissions. "
                    "Fewer people generally lead to lower consumption and fewer emissions.")
        else:
            st.info("🌍 **Impact of Population on Emissions**: The more people in a household, the higher the overall carbon emissions. "
                    "Reducing population size, especially by having fewer children, can have a significant impact on carbon emission reductions.")

        # Adding extra context
        st.write("🔬 **Real Data on CO2 Emissions**: On average, children in a household contribute significantly to carbon emissions, "
                "with each child generating around 58.3 tons of CO2 annually based on typical consumption patterns. "
                "Adults generally contribute around 15 tons of CO2 per year, but this can vary greatly depending on lifestyle and location.")


        savings_messages = [
                "🚗 Driving less saves ~0.2 kg CO2 per km!",
                "💡 Using energy-efficient appliances saves ~0.3 kg CO2 per kWh!"
            ] if current_emission > 50 else []

        total_household_emissions = (user_data.get("household_size", 4) - 1) * 15 + 1 * 58.3
        emission_savings = 10  # Example value

        pdf_buffer = gr.generate_pdf(user_data, current_emission, savings_messages, total_household_emissions, emission_savings)

        grBtn = st.download_button(
            label="📄 Export Report as PDF",
            data=pdf_buffer,
            file_name=f"{user_data['user_name']}_carbon_footprint_report.pdf",
            mime="application/pdf"
        )

        if grBtn:
            st.toast(f"✅ {user_data['user_name']}! Report downloaded successfully!")


st.write("---")
# Footer with motivation
st.write("### 🌍 Every Step Counts!")
st.write("By understanding your carbon footprint, you're taking the first step towards reducing your impact.")
st.write("Together, we can create a greener planet!")
st.write("🌟 Thank you for making a difference! 💚")