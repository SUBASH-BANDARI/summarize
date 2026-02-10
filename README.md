# Text Summarizer — Hugging Face & Streamlit

A web app that summarizes long text using Hugging Face transformer models. Built for clarity, local-first use, and recruiter-friendly demonstration of full-stack ML delivery.

---

## What This Project Does

- **Summarization**: Paste any text (articles, docs, notes) and get a shorter summary.
- **Model choice**: Default is `sshleifer/distilbart-cnn-12-6`; you can switch to any Hugging Face summarization model by name.
- **Tunable output**: Min/max length and “Stable” vs “Creative” style (deterministic vs sampling).
- **Long documents**: Input is chunked automatically (e.g. by sentences) so long texts are summarized in parts and combined.
- **Multi-page app**: Main summarizer plus **Features** and **Contact** pages.

---

## Tech Stack

| Layer        | Technology |
|-------------|------------|
| **UI / App** | [Streamlit](https://streamlit.io/) |
| **NLP / ML** | [Hugging Face Transformers](https://huggingface.co/docs/transformers/) (`pipeline("summarization", ...)`) |
| **Backend**  | Python 3.x (script-based; no separate server framework) |
| **Runtime**  | Local (runs on your machine; optional GPU via `device_map="auto"`) |

### Main dependencies

- `streamlit` — web UI and session state
- `transformers` — summarization pipeline and model loading
- `torch` — backend for transformer models (CPU or CUDA/MPS)

---

## Project Structure

```
summarize/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .gitignore
└── hf_summarizer_app/
    ├── app.py                # Main summarizer page and logic
    ├── run.sh                # Convenience script (venv + streamlit)
    └── pages/
        ├── 1_Features.py     # Features overview
        └── 2_Contact.py      # Contact / placeholder form
```

---

## Setup & Run

### Prerequisites

- Python 3.10+ recommended
- (Optional) GPU for faster inference

### Install

```bash
cd hf_summarizer_app
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r ../requirements.txt
```

### Run the app

```bash
# From project root
cd hf_summarizer_app && ./run.sh

# Or manually
cd hf_summarizer_app
source venv/bin/activate
python -m streamlit run app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`).

---

## Design & Implementation Notes

- **Caching**: The summarization pipeline is loaded once per model with `@st.cache_resource` to avoid reloading on every interaction.
- **Chunking**: Long text is split at sentence boundaries (up to ~4000 characters per chunk) to stay within model limits; summaries are concatenated.
- **Device**: `device_map="auto"` uses GPU if available (CUDA / MPS), otherwise CPU.

---

## License

This is a personal project for portfolio and recruitment use. Use and adapt as you like.

---

## Author

Personal project — built to showcase full-stack ML delivery (NLP + web app + deployment-ready structure).
