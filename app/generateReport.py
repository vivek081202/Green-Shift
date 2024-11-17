import io
import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

def generate_pdf(user_data, current_emission, savings_messages, total_household_emissions, emission_savings):
    """
    Generate a PDF report for the user's carbon footprint and household emissions.
    """
    # Calculate household and scaled emissions
    household_size = user_data.get('household_size', 1)  # Default to 1 if not provided
    total_household_emissions = current_emission * household_size * 365 / 1000  # Convert kg to tons annually
    emission_savings = total_household_emissions * 0.2  # Assume a 20% potential savings

    # PDF generation setup
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("Personalized Carbon Footprint Dashboard Report", styles['Title']))
    elements.append(Spacer(1, 12))

    # User details
    elements.append(Paragraph(f"User Name: {user_data['user_name']}", styles['Normal']))
    elements.append(Paragraph(f"Household Size: {household_size}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Emission metrics
    elements.append(Paragraph(f"Total Current Emission: {current_emission:.2f} kg CO2/day", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Savings messages
    if savings_messages:
        elements.append(Paragraph("Savings Opportunities:", styles['Heading2']))
        for msg in savings_messages:
            elements.append(Paragraph(f"• {msg}", styles['Normal']))
        elements.append(Spacer(1, 12))

    # Household emissions and potential savings
    elements.append(Paragraph(f"Total Household Emissions: {total_household_emissions:.2f} tons CO2/year", styles['Normal']))
    elements.append(Paragraph(f"Potential Savings with Sustainable Practices: {emission_savings:.2f} tons CO2/year", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Footer
    elements.append(Paragraph("🌍 Together, we can make a difference in reducing carbon emissions!", styles['Italic']))

    # Build the document
    doc.build(elements)
    buffer.seek(0)
    return buffer
