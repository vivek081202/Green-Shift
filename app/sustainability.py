import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Page Title and Intro
st.title("🌍 Sustainability Dashboard: Insights on Carbon Emissions and Environmental Impact")
st.write("""
    Welcome to the **Sustainability Dashboard**! 
    Explore the latest facts and insights related to environmental sustainability, carbon emissions, and how human activities impact the planet. 
    Each section presents detailed, researched facts, with reliable sources to help you learn how to make informed decisions and reduce your carbon footprint.
""")

# Section 1: Environmental Consequences of Childbirth
st.markdown("### 1. The Environmental Consequences of Childbirth")
childFact, chimage = st.columns([12,5])

with childFact:
    st.write("""
        **Fact:** Every additional child born into a family adds about **58.6 tons of carbon emissions** annually. This is due to the combined 
        resource consumption for food, transportation, and energy usage throughout a child's life.

        By understanding these impacts, families and societies can begin to recognize the importance of sustainable population growth.

        **Sources:**
        - [Population Connection](https://populationconnection.org/resources/human-activities-and-climate-change/)
    """)

with chimage:
    # Add Image for child-related emissions from Pexels
    st.image("https://populationconnection.org/wp-content/uploads/2021/09/Untitled-design-26-300x300.png", caption="Childbirth's Environmental Impact")

st.write("---")
# Section 2: Meat and Dairy Consumption

diet, exp, mimage = st.columns([5,4,5])

with diet:
    st.markdown("### 2. Meat and Dairy Consumption: A Major Contributor to Global Emissions")
    st.write("""
        **Fact:** Livestock farming, especially beef and dairy, contributes to **14.5%** of global greenhouse gas emissions. Beef production is the 
        most carbon-intensive, accounting for a significant portion of these emissions due to methane produced by cattle.

        Shifting towards plant-based diets is a critical step in reducing personal and global carbon footprints.

        **Sources:**
        - [CarbonBrief](https://interactive.carbonbrief.org/what-is-the-climate-impact-of-eating-meat-and-dairy/index.html)
    """)

with exp:
    # Add Expander for more details about Meat and Dairy
    with st.expander("Learn More About Meat and Dairy Emissions"):
        st.write("""
            The environmental cost of meat and dairy is staggering, but more and more people are choosing plant-based options as a healthier and more 
            sustainable alternative. In fact, reducing meat consumption can reduce your carbon footprint by up to **73%**!
        """)

with mimage:
    st.image("https://interactive.carbonbrief.org/what-is-the-climate-impact-of-eating-meat-and-dairy/img/prawn-farming.jpg", caption="Massive Deforestation due to Animal Husbandry")

st.write("---")
# Section 3: The Plant-Based Diets

plant, vegimage = st.columns([10,5])

with plant:
    st.markdown("### 3. Plant-Based Diets: A Key to Reducing Emissions")
    st.write("""
        **Fact:** Adopting a **plant-based diet** can reduce your carbon footprint by up to **73%**. A vegan diet has significantly less environmental impact than an omnivorous diet, as animal agriculture is one of the largest sources of methane emissions, deforestation, and water consumption.

        **Sources:**
        - [Environmental Research Letters](https://iopscience.iop.org/journal/1748-9326)
        - [The Guardian](https://www.theguardian.com/environment/2022/jun/04/meat-diets-climate-emissions-plant-based-vegan?ref=refind)
    """)

with vegimage:
    st.image("https://interactive.carbonbrief.org/what-is-the-climate-impact-of-eating-meat-and-dairy/img/planetary-diet.png", caption="Planetary Diet")


st.write("---")
# Section 4: Electric Vehicles

ev, evimg = st.columns([6,4])

with ev:
    st.markdown("### 4. Electric Vehicles: Reducing Carbon Footprints in Transportation")
    st.write("""
        **Fact:** Electric vehicles (EVs) reduce lifetime carbon emissions compared to traditional gasoline-powered vehicles, despite higher emissions 
        from battery production. As renewable energy sources become more prevalent, EVs will further reduce emissions across the transportation sector.

        **Sources:**
        - [International Energy Agency](https://www.iea.org/reports/global-ev-outlook-2024/outlook-for-emissions-reductions)
    """)

with evimg:
    st.image("https://www.carbonbrief.org/wp-content/uploads/2019/05/tesla-transport-electric-vehicles-1349x700.jpg", caption="Electric Vehicle")



# Add Callout for Electric Vehicles Section
st.markdown("""
    > **Tip:** Using public transport, carpooling, or switching to electric vehicles can drastically reduce your transportation-related carbon footprint!
""")

st.write("---")
# Section 5: The Carbon Impact of Air Travel
st.markdown("### 5. The Carbon Impact of Air Travel")

air, airimg = st.columns([8,5])


with air:
    st.write("""
        **Fact:** Air travel is responsible for about **3%** of global carbon emissions. Flying contributes significantly to greenhouse gas emissions, and 
        the environmental cost can be mitigated by avoiding unnecessary air travel and opting for sustainable alternatives.

        **Sources:**
        - [BBC](https://www.bbc.com/future/article/20200218-climate-change-how-to-cut-your-carbon-emissions-when-flying)
    """)

with airimg:
    st.image("https://ichef.bbci.co.uk/images/ic/1024xn/p083t60m.jpg.webp", caption="Carbon Emissions from Aviation")


# Simple Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 14px; padding: 10px; color: #999;">
    <p><strong>🌿 Sustainability Dashboard</strong></p>
    <p>
        Informing and inspiring change for a sustainable future. 
        Together, we can make a difference. 🌏
    </p>
    <p>© 2024 | Created with ❤️ and responsibility.</p>
</div>
""", unsafe_allow_html=True)
