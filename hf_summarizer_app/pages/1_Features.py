import streamlit as st

st.set_page_config(page_title="Features", page_icon="✨", layout="centered")

st.title("✨ Features")

st.markdown("---")

st.markdown("""
### 🧠 AI-Powered Summarization
- **Advanced NLP Models**: Uses state-of-the-art Hugging Face transformers
- **Customizable Length**: Control min and max summary length
- **Multiple Styles**: Choose between stable or creative summarization

### ⚡ Performance
- **Fast Processing**: Optimized for quick text analysis
- **Long Text Support**: Automatically handles long documents by chunking
- **Local Processing**: Runs entirely on your device for privacy

### 🎨 User Experience
- **Clean Interface**: Simple and intuitive design
- **Real-time Feedback**: See progress as your summary is generated
- **Flexible Input**: Paste any text from articles to documents
""")

st.markdown("---")

st.markdown("""
### 📝 How It Works
1. **Paste Your Text**: Enter any text you want to summarize
2. **Adjust Settings**: Set your preferred summary length and style
3. **Generate**: Click summarize and get instant results
4. **Review**: Read your concise summary in seconds
""")
