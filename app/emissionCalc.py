import streamlit as st

def calculate_current_emission(user_data):
    """
    Calculate carbon emissions based on real data and research-backed emission factors,
    adjusted for household size.
    """

    # Transportation emissions (Source: EPA and DEFRA reports)
    transport_emissions = 0
    fuel_emission_factors = {
        "Gasoline": 2.31,  # kg CO2 per liter (average)
        "Diesel": 2.68,    # kg CO2 per liter
        "Electric": 0.12,  # kg CO2 per kWh (India average)
        "Hybrid": 1.15     # kg CO2 per liter (hybrid average consumption)
    }
    # Calculate emissions from distance driven
    if user_data.get("fuel_type") and user_data.get("distance_driven"):
        distance = user_data["distance_driven"]
        # Assuming fuel economy based on vehicle type
        fuel_economy = user_data.get("fuel_economy", 15)  # Default 15 km per liter
        fuel_used = distance / fuel_economy
        transport_emissions = fuel_used * fuel_emission_factors.get(user_data["fuel_type"], 2.31)
    
    # Flights emissions (Source: ICAO Carbon Emissions Calculator)
    if user_data.get("flights_per_year"):
        flight_distance = user_data.get("flight_distance", 400)  # Default 1000 km per flight
        flight_emission_factor = 0.255  # kg CO2 per passenger-km
        flight_emissions = user_data["flights_per_year"] * flight_distance * flight_emission_factor
    else:
        flight_emissions = 0

    # Energy emissions (Source: IEA, India-specific emission factors)
    energy_emissions = 0
    if user_data.get("electricity_usage"):
        electricity_emission_factor = 0.82  # kg CO2 per kWh (India-specific average)
        energy_emissions += user_data["electricity_usage"] * electricity_emission_factor
    
    if user_data.get("gas_usage"):
        gas_emission_factor = 2.5  # kg CO2 per cubic meter (natural gas)
        energy_emissions += user_data["gas_usage"] * gas_emission_factor

    # Waste emissions (Source: IPCC Waste Management Guidelines)
    waste_emissions = 0
    if user_data.get("waste_generated"):
        waste_emission_factor = 0.6  # kg CO2 per kg of waste
        recycling_rate = user_data.get("recycling_rate", 0) / 100
        waste_emissions = user_data["waste_generated"] * waste_emission_factor * (1 - recycling_rate)
    
    # Diet emissions (Source: FAO and IPCC Food Sector Reports)
    diet_emissions = 0
    if user_data.get("diet_type"):
        diet_emission_factors = {
            "High": 4.1,
            "Moderate": 3.3,
            "Low": 2.5,  # kg CO2 per day
            "Vegetarian": 1.7,  # kg CO2 per day
            "Vegan": 0.9       # kg CO2 per day
        }
        diet_emissions = diet_emission_factors.get(user_data["diet_type"], 2.5) # Annual emissions
    
    # Water usage emissions (minimal impact, based on average energy for water treatment)
    water_emissions = 0
    if user_data.get("water_usage"):
        water_emission_factor = 0.000298  # kg CO2 per liter of water treated
        water_emissions = user_data["water_usage"] * water_emission_factor
    
    # Shopping frequency emissions (proxy via carbon cost of consumer goods, per annum)
    shopping_emissions = 0
    if user_data.get("shopping_frequency"):
        shopping_emission_factors = {
            "Daily": 2.0,     # kg CO2 per day
            "Weekly": 1.0,    # kg CO2 per day
            "Monthly": 0.5,   # kg CO2 per day
            "Rarely": 0.2     # kg CO2 per day
        }
        shopping_emissions = shopping_emission_factors.get(user_data["shopping_frequency"], 0.5)
    
    # Total emissions calculation
    total_emissions = (
        transport_emissions +
        flight_emissions +
        energy_emissions +
        waste_emissions +
        diet_emissions +
        water_emissions +
        shopping_emissions
    )
    
    # Apply household size scaling factor
    household_size = user_data.get("household_size", 1)  # Default to 1 if not provided
    total_emissions *= household_size
    
    return round(total_emissions, 2)
