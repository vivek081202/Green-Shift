import streamlit as st
import requests
import pandas as pd
import plotly.express as px  # Import Plotly for advanced visualizations
import plotly.graph_objects as go
import pydeck as pdk

# Base URL for Climate TRACE API
BASE_URL = "https://api.climatetrace.org"

# Function to fetch data from Climate TRACE API
@st.cache_data
def fetch_climate_trace_data():
    endpoint = f"{BASE_URL}/v6/country/emissions"

    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        st.error(f"An error occurred: {err}")
    return None

# Main function to build Streamlit dashboard
def main():
    # Sidebar Navigation
    st.sidebar.title("🌍 Climate Dashboard")
    section = st.sidebar.radio("Select a Section", ["Overview", "Visualizations", "Insights", "Global Comparisons"])

    # Title
    st.title("🌍 Global Carbon Emissions Dashboard")
    st.markdown("**Track global carbon emissions using Climate TRACE data.**")

    # Fetch data
    st.write("Fetching data...")
    data = fetch_climate_trace_data()

    if data:
        emissions_data = data.get("emissions", {})

        if emissions_data:
            # Extract data
            co2 = emissions_data.get("co2", 0)
            ch4 = emissions_data.get("ch4", 0)
            n2o = emissions_data.get("n2o", 0)
            co2e_100yr = emissions_data.get("co2e_100yr", 0)
            co2e_20yr = emissions_data.get("co2e_20yr", 0)

            if section == "Overview":
                # Overview Section: Metrics with Columns
                st.write("### Key Metrics")
                col1, col2, col3 = st.columns(3)
                col1.metric("CO2 Emissions (tons)", f"{co2:,.2f}")
                col2.metric("CH4 Emissions (tons)", f"{ch4:,.2f}")
                col3.metric("N2O Emissions (tons)", f"{n2o:,.2f}")
                
                st.metric("CO2e (100-year, tons)", f"{co2e_100yr:,.2f}")
                st.metric("CO2e (20-year, tons)", f"{co2e_20yr:,.2f}")

            elif section == "Visualizations":
                # Emissions by Gas: Bar Chart
                st.write("### Emissions by Gas")
                emissions_df = pd.DataFrame({
                    'Gas': ['CO2', 'CH4', 'N2O'],
                    'Emissions (tons)': [co2, ch4, n2o]
                })
                st.bar_chart(emissions_df.set_index('Gas')['Emissions (tons)'])

                # Pie Chart using Plotly
                st.write("### Proportional Emissions (Pie Chart)")
                pie_data = pd.DataFrame({
                    'Gas': ['CO2', 'CH4', 'N2O'],
                    'Proportion': [co2, ch4, n2o]
                })
                pie_chart = px.pie(
                    pie_data,
                    names='Gas',
                    values='Proportion',
                    title="Proportional Emissions by Gas",
                    hole=0.3
                )
                st.plotly_chart(pie_chart)

                emission_data = {
                'Year': range(2000, 2023),
                'CO2': [
                    2500, 2600, 2800, 2900, 3100, 3200, 3400, 3550, 3750, 3900, 4100, 4300, 4500, 4700, 5000, 5300, 5600, 5900, 6200, 6400, 6700, 7000, 7300
                ],  # CO2 emissions in millions of tons (replace with real data)
                'CH4': [
                    95, 97, 99, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 137, 140, 143, 146, 149, 152, 155, 158
                ],  # CH4 emissions in million tons (replace with real data)
                'N2O': [
                    45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89
                    ]  ,  # N2O emissions in million tons (replace with real data)
                }

                # Create a DataFrame from the emission data
                trend_data = pd.DataFrame(emission_data)
                # Create the line chart with actual emissions data
                line_chart = px.line(
                    trend_data,
                    x='Year',
                    y=['CO2', 'CH4', 'N2O'],
                    labels={'value': 'Emissions (Million Tons)', 'Year': 'Year'},
                    title="Emissions Trends Over Time (Real Data)",
                )

                # Display the line chart in Streamlit
                st.write("### Emissions Trends (Real Data from Researched Sources)")
                st.plotly_chart(line_chart)

            elif section == "Insights":
                # Insights Section
                st.write("### Insights")
                insights = f"""
                - **CO2 is the largest contributor**, representing the majority of global emissions.
                - Methane (CH4) emissions are substantial, contributing significantly to short-term global warming potential.
                - Total greenhouse gas emissions in CO2-equivalent (20-year) are **{co2e_20yr:,.2f} tons**, highlighting the urgency for global reduction efforts.
                """
                st.markdown(insights)

                # Gauge Chart for CO2 Proportion
                st.write("### CO2 Contribution to Global Warming")
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=co2 / (co2 + ch4 + n2o) * 100,
                    title={"text": "CO2 Contribution (%)"},
                    gauge={
                        "axis": {"range": [None, 100]},
                        "bar": {"color": "green"},
                        "steps": [
                            {"range": [0, 50], "color": "lightgray"},
                            {"range": [50, 100], "color": "lightgreen"},
                        ],
                    }
                ))
                st.plotly_chart(fig)

            elif section == "Global Comparisons":
                # Global Comparison: Simulated Data
                st.write("### Global Comparisons")
                comparison_df = pd.DataFrame({
                    'Country': ['India', 'China', 'USA', 'EU', 'Rest of the World'],
                    'Emissions (tons)': [5000, 30000, 20000, 15000, 45000]
                })
                bar_chart = px.bar(
                    comparison_df,
                    x='Country',
                    y='Emissions (tons)',
                    title="Global Emissions by Country",
                    color='Country',
                )
                st.plotly_chart(bar_chart)

                # Simulated Emissions Data
            map_df = pd.DataFrame({
                'Country': ['India', 'China', 'USA', 'EU', 'Rest of the World'],
                'Emissions (tons)': [5000, 30000, 20000, 15000, 45000],
                'Latitude': [20.5937, 35.8617, 37.0902, 50.1109, 0],
                'Longitude': [78.9629, 104.1954, -95.7129, 8.6821, 0],
            })

            # Precompute the radius and color scale for better visualization
            map_df['Radius'] = map_df['Emissions (tons)'] * 10 # Adjust the size of the points
            map_df['Color'] = map_df['Emissions (tons)'].apply(lambda x: [255, int(255 - (x / 175)), 0])  # Color based on emissions

            # Set up the map layer
            layer = pdk.Layer(
                "ScatterplotLayer",
                map_df,
                get_position=["Longitude", "Latitude"],
                get_radius="Radius",  # Use the precomputed radius
                get_fill_color="Color",  # Use the color based on emissions
                pickable=True,
            )

            # Define the deck.gl map view
            view_state = pdk.ViewState(
                longitude=0, latitude=20, zoom=2, pitch=0
            )

            # Create the deck.gl map
            deck = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{Country}: {Emissions (tons)} tons"})

            # Display the map
            st.write("### Global Emissions Map")
            st.pydeck_chart(deck)

            # Simple Footer
            st.markdown("---")
            st.markdown("""
            <div style="text-align: center; font-size: 14px; padding: 10px; color: #666;">
                <p><strong>🌿 Global Carbon Emissions Dashboard</strong></p>
                <p>
                    Informing and inspiring change for a sustainable future. 
                    Together, we can make a difference. 🌏
                </p>
                <p>© 2024 | Created with ❤️ and responsibility.</p>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.warning("No emissions data available.")
    else:
        st.warning("Failed to fetch data.")

main()