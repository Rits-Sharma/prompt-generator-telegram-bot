import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
    .main {
        background-color: #fcfdfe;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 14px 28px;
        font-weight: 600;
        font-size: 16px;
        width: 100%;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%);
        box-shadow: 0 8px 20px rgba(124, 58, 237, 0.3);
        transform: translateY(-1px);
    }
    
    .stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        transition: all 0.2s ease;
    }
    .stTextArea textarea:focus {
        border-color: #7c3aed !important;
        box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1);
    }
    
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 10px;
    }
    
    .success-box {
        background: #f0fdf4;
        color: #166534;
        padding: 16px 20px;
        border-radius: 12px;
        border: 1px solid #bbf7d0;
        border-left: 5px solid #22c55e;
        font-weight: 500;
    }
    
    .prompt-box {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #f1f5f9;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e1b4b 0%, #311042 100%) !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label {
        color: #f8fafc !important;
    }

    code {
        white-space: pre-wrap !important;
        word-break: break-word !important;
    }
    </style>
    """, unsafe_allow_html=True)

def display_footer():
    st.markdown("""
    <div style='text-align: center; margin-top: 50px; padding-top: 20px;'>
        <p style='color: #4A5568; font-weight: 500; font-family: sans-serif; letter-spacing: 0.5px; margin-bottom: 4px;'>
            SmartPrompt AI <span style='color: #a0aec0;'>|</span> Powered by Gemini API
        </p>
        <p style='font-size: 13px; color: #718096; font-style: italic;'>
            Crafted with ❤️ by Ritesh
        </p>
    </div>
    """, unsafe_allow_html=True)
