from PIL import Image
import streamlit as st
import Ddashboard as dashboard

logo = Image.open("../Images/global-warming.png")  # Replace with your logo file path if available

# Logo and Title Section
st.image(logo, width=175)  # Adjust the width as per your design
st.title("🌍 GreenShift - Carbon Footprint Tracker")
st.subheader("Empowering Sustainable Choices 🌱")
st.markdown("**Take the first step towards understanding and reducing your carbon footprint.**")

st.image("../Images/Climate.jpg")

# Separator
st.markdown("---")

# Overview Section with Columns
st.markdown("### 🌟 Key Features of GreenShift")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### 🌍 Track Your Carbon Footprint")
    st.write("Monitor and analyze your carbon emissions based on daily activities like travel and energy use.")
with col2:
    st.markdown("#### 📊 Real-Time Climate Insights")
    st.write("Get updated on global climate trends and understand the impact of carbon emissions worldwide.")
with col3:
    st.markdown("#### 💡 Personalized Recommendations")
    st.write("Receive suggestions on how to make small changes that have a big impact on the environment.")

# Functional Tabs for Navigating Features
st.markdown("---")
st.markdown("### 🔍 Explore GreenShift")
tabs = st.tabs(["🚶 Track Footprint", "📈 Climate Insights", "💼 Recommendations"])

with tabs[0]:
    st.write("### Track Your Carbon Footprint")
    st.write("Log your daily activities, such as transportation, diet, and energy use, to calculate your carbon emissions.")
    track = st.button("Start Tracking")
    if track:
        st.switch_page("user_input.py")

with tabs[1]:
    st.write("### Real-Time Climate Insights")
    st.write("Discover the latest global climate data, including temperature trends and CO2 levels.")
    insights = st.button("View Climate Insights")
    if insights:
        st.switch_page("Global_Climate.py")

with tabs[2]:
    st.write("### Personalized Recommendations")
    st.write("Get customized tips to help you adopt eco-friendly habits and reduce your carbon footprint.")
    recommendations = st.button("Get Recommendations")
    if recommendations:
        st.switch_page("sustainability.py")

# FAQ Section with Expanders
st.markdown("---")
st.markdown("### ❓ Frequently Asked Questions")
with st.expander("What is Climate Change?", expanded=False):
    st.write("""Climate change is a long-term change in the average weather patterns that have come to define Earth’s local, regional and global climates. These changes have a broad range of observed effects that are synonymous with the term.

Changes observed in Earth’s climate since the mid-20th century are driven by human activities, particularly fossil fuel burning, which increases heat-trapping greenhouse gas levels in Earth’s atmosphere, raising Earth’s average surface temperature. Natural processes, which have been overwhelmed by human activities, can also contribute to climate change, including internal variability (e.g., cyclical ocean patterns like El Niño, La Niña and the Pacific Decadal Oscillation) and external forcings (e.g., volcanic activity, changes in the Sun’s energy output, variations in Earth’s orbit).""")
with st.expander("What is GreenShift?", expanded=False):
    st.write("🌎 GreenShift is a data-driven web application designed to help individuals track, understand, and reduce their carbon footprint. In today’s world, personal actions play a significant role in addressing climate change. GreenShift provides an easy way to quantify the environmental impact of daily activities and encourages users to adopt more sustainable habits.")
with st.expander("How do I track my carbon footprint?", expanded=False):
    st.write("Simply log your daily activities related to energy, transport, and diet to get an accurate measurement.")
with st.expander("Where does the climate data come from?", expanded=False):
    st.write("We source our data from reliable climate data APIs, including NASA and NOAA.")
# New expander for climate change factors
with st.expander("🌍 Top 5 Factors Driving Climate Change"):
    st.write("Climate change is a complex issue driven by various human and environmental factors. Here are the top contributors:")
    
    st.markdown("#### 1.👨‍👩‍👦 Increasing Population (Major Contributor - High Risk 🛑)")
    st.write(
        """
        The global population is growing rapidly, leading to higher demands for resources like food, water, and energy.
        This increase in consumption directly contributes to greater greenhouse gas emissions and environmental degradation.
        """
    )
    
    st.markdown("#### 2.🍖 Meat Consumption")
    st.write(
        """
        Meat production, especially beef, is highly resource-intensive and generates significant greenhouse gases, particularly methane. 
        Reducing meat consumption can lessen the environmental impact by decreasing methane emissions, deforestation for grazing, 
        and water usage.
        """
    )
    
    st.markdown("#### 3.⛽ Fossil Fuel Usage")
    st.write(
        """
        Burning fossil fuels for energy and transportation releases large amounts of carbon dioxide, a key greenhouse gas. 
        Transitioning to renewable energy sources can significantly reduce these emissions.
        """
    )
    
    st.markdown("#### 4.🌴 Deforestation")
    st.write(
        """
        Forests absorb CO2, but widespread deforestation for agriculture, urban development, and logging is reducing 
        the Earth's ability to naturally offset carbon emissions. Protecting and restoring forests is critical.
        """
    )
    
    st.markdown("#### 5.🏭 Industrial Activity")
    st.write(
        """
        Factories and industries emit significant amounts of CO2, methane, and other pollutants. As economies grow, 
        so does industrial activity, contributing to climate change. Sustainable practices in manufacturing can reduce these impacts.
        """
    )

dashboard.dummyDashboard()

st.markdown("---")
st.markdown("### 💬 We Value Your Feedback")
st.text_area("Share your thoughts or suggestions here:", placeholder="Share your views...")
st.button("Submit Feedback")

# Simple Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 14px; padding: 10px; color: #666;">
    <p><strong>🌿 Sustainability Dashboard</strong></p>
    <p>
        Informing and inspiring change for a sustainable future. 
        Together, we can make a difference. 🌏
    </p>
    <p>© 2024 | Created with ❤️ and responsibility.</p>
</div>
""", unsafe_allow_html=True)