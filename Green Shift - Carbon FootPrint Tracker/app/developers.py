import streamlit as st

@st.cache_data
def circular_image(image_path, width=140):
    # Display the image using Streamlit
    st.image(image_path, width=width, use_column_width=False)

st.logo("../Images/team.png")
st.image("../Images/team.png",width=145)
st.title("Meet the Team Behind the Suite")
st.write("""
    This project was developed by a team of dedicated students from the JIIT Noida campus, with a passion for creating tools that improve academic experiences.
    Our team consists of:
    """)

st.write("---")
# Display each developer's profile picture and details
circular_image("../Images/vivek.jpg")  # Replace with your image path
st.subheader("Vivek Kumar Singh")
st.write("Role: Lead Developer | Specializes in backend development and Machine Learning Algorithms.")

st.markdown("""
I am a results-oriented individual with a strong work ethic. I'm also a team player and have excellent communication skills and passionate about software development, data science, machine learning and have a strong foundation in Java, Python, data structures & algorithms, software engineering principles and practical statistics.
""")

st.write("""Reach out through:""")
st.write("""📧 Email: vihixi50@gmail.com""")
st.write("""GitHub: https://github.com/vivek081202""")
st.write("""LinkedIn: https://www.linkedin.com/in/vivek-singh-858941201""")
            
st.markdown("""
I'm constantly exploring the latest advancements in AI and technology. This proactive approach keeps me ahead of the curve, eager to contribute to what's next.
""")

st.write('---')

circular_image("../Images/Hamza.jpg")  # Replace with your image path
st.subheader("Mohd. Hamza")
st.write("Role: Data Analysis | Responsible for data processing and ensuring accurate analytics.")

st.write("Each member has contributed to the success of this suite by bringing their expertise to the project, creating a comprehensive and user-friendly experience.")

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