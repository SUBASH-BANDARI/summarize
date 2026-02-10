import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📧", layout="centered")

st.title("📧 Contact")

st.markdown("---")

st.markdown("""
### Get in Touch

Have questions, suggestions, or feedback? We'd love to hear from you!
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📬 Email
    support@example.com
    
    ### 📱 Phone
    +1 (555) 123-4567
    """)

with col2:
    st.markdown("""
    ### 🌐 Social Media
    - Twitter: @example
    - LinkedIn: /company/example
    - GitHub: /example
    """)

st.markdown("---")

st.markdown("""
### 💬 Send us a Message
""")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message", height=150)
    submitted = st.form_submit_button("Send Message", type="primary")
    
    if submitted:
        st.success("Thank you for your message! We'll get back to you soon.")
