import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="HF Summarizer", page_icon="🧠", layout="centered")

@st.cache_resource
def load_summarizer(model_name: str):
    return pipeline(
        "summarization",
        model=model_name,
        device_map="auto"
    )

st.title("🧠 Text Summarizer")
st.markdown("---")

# Model selection
MODEL_DEFAULT = "sshleifer/distilbart-cnn-12-6"
model_name = st.text_input("Model name", value=MODEL_DEFAULT)
summarizer = load_summarizer(model_name)

# Text input area with good spacing
st.markdown("### Enter your text:")
text = st.text_area(
    "Your text", 
    height=300, 
    placeholder="Paste your text here to summarize...",
    label_visibility="collapsed"
)

# Parameters
col1, col2, col3 = st.columns(3)
with col1:
    min_len = st.number_input("Min length", min_value=10, max_value=400, value=60, step=10)
with col2:
    max_len = st.number_input("Max length", min_value=20, max_value=800, value=150, step=10)
with col3:
    do_sample = st.selectbox("Style", ["Stable", "Creative"], index=0) == "Creative"

# Summarize button
if st.button("Summarize", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            # Chunk long text
            chunks = []
            max_chars = 4000
            t = text.strip()
            while len(t) > max_chars:
                split_at = t.rfind(".", 0, max_chars)
                if split_at == -1:
                    split_at = max_chars
                chunks.append(t[:split_at+1])
                t = t[split_at+1:].strip()
            if t:
                chunks.append(t)

            summaries = []
            for c in chunks:
                out = summarizer(
                    c,
                    min_length=int(min_len),
                    max_length=int(max_len),
                    do_sample=do_sample,
                )
                summaries.append(out[0]["summary_text"])

            final_summary = "\n\n".join(summaries)
            st.session_state.summary = final_summary

# Display summary with good spacing
if "summary" in st.session_state:
    st.markdown("---")
    st.markdown("### Summary:")
    st.info(st.session_state.summary)
