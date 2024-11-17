import streamlit as st
import pandas as pd

@st.cache_data
def dummyDashboard():
    # Dummy data for the dashboard
    mock_data = {
        "Category": ["Transportation", "Energy Usage", "Diet", "Waste"],
        "Current Footprint (kg CO2)": [250, 300, 150, 50],
        "Projected Reduction (kg CO2)": [200, 240, 120, 40]
    }

    df_mock = pd.DataFrame(mock_data)

    # Section Title
    st.markdown("### 🌿 GreenShift Dashboard Preview")
    st.write("Here's a sneak peek of the insights you'll gain from tracking your carbon footprint with GreenShift.")

    # Dashboard columns
    col1, col2, col3 = st.columns(3)

    # Column 1: Current Footprint by Category - Bar Chart
    with col1:
        st.markdown("#### 📊 Current Carbon Footprint")
        st.bar_chart(df_mock.set_index("Category")["Current Footprint (kg CO2)"])

    # Column 2: Projected Reduction with GreenShift - Area Chart
    with col2:
        st.markdown("#### 📉 Projected Reduction")
        st.area_chart(df_mock.set_index("Category")["Projected Reduction (kg CO2)"])

    # Column 3: Comparison of Current vs Projected - Line Chart
    with col3:
        st.markdown("#### 📈 Current vs Projected Comparison")
        # Preparing data for line chart
        df_comparison = df_mock.set_index("Category")
        st.line_chart(df_comparison)

    # Insights and Summary
    st.markdown("### 📝 Sample Insights and Recommendations")
    st.write(
        """
        With GreenShift, you'll receive personalized insights like:
        
        - **Transportation**: "Switching to public transport or carpooling could reduce your carbon footprint by 20%!"
        - **Energy Usage**: "Turning off devices when not in use can save up to 30 kg CO2 monthly."
        - **Diet**: "Reducing meat intake by 50% could cut your carbon footprint by 50 kg CO2 per month."
        - **Waste**: "Recycling more and composting organic waste can further reduce emissions."

        Get detailed recommendations to adopt eco-friendly habits and track your progress over time!
        """
    )
