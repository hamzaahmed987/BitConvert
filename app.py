# import streamlit as st
# import google.generativeai as genai

# # Set the page configuration as the very first Streamlit command
# st.set_page_config(page_title="Smart Bit Converter & AI Chatbot", page_icon="⚡", layout="centered")

# # Custom CSS for a modern, professional look
# st.markdown("""
# <style>
# /* Import Google Fonts */
# @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

# body {
#     background: linear-gradient(135deg, #74ABE2, #5563DE);
#     font-family: 'Poppins', sans-serif;
#     color: #FFFFFF;
# }

# /* Make the main app background transparent */
# .stApp {
#     background: transparent;
# }

# /* Title Styling */
# h1 {
#     text-align: center;
#     font-size: 3em;
#     font-weight: 700;
#     margin-bottom: 20px;
#     text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
# }

# /* Tab Navigation Styling */
# div[data-baseweb="tab-list"] button {
#     background-color: #FFFFFF;
#     color: #333333;
#     border: none;
#     padding: 10px 20px;
#     border-radius: 5px 5px 0 0;
#     font-size: 1.1em;
#     font-weight: 600;
#     margin-right: 2px;
# }
# div[data-baseweb="tab-list"] button:hover {
#     background-color: #E0E0E0;
# }
# div[data-baseweb="tab-list"] button[aria-selected="true"] {
#     background-color: #5563DE;
#     color: #FFFFFF;
#     border-bottom: 3px solid #74ABE2;
# }

# /* Input elements */
# .stTextInput input, .stNumberInput input, .stSelectbox select {
#     border: 2px solid #FFFFFF;
#     border-radius: 8px;
#     padding: 10px;
#     background: rgba(255, 255, 255, 0.2);

#     transition: background 0.3s ease, color 0.3s ease;
# }

# /* Prevent input field color change after interaction */
# .stTextInput input:focus {
#     background: rgba(255, 255, 255, 0.3);
  
# }

# /* Button styling */
# div.stButton > button {
#     background: linear-gradient(90deg, #74ABE2, #5563DE);
#     color: #FFFFFF;
#     padding: 10px 25px;
#     border-radius: 8px;
#     border: none;
#     font-size: 1em;
#     font-weight: 600;
#     box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
#     transition: transform 0.2s;
# }
# div.stButton > button:hover {
#     transform: scale(1.05);
# }

# /* Output text styling */
# .markdown-text-container p {
#     font-size: 1.2em;
# }
# </style>
# """, unsafe_allow_html=True)

# # Configure Gemini API
# GEMINI_API_KEY = "AIzaSyCZjDMBkTr8fB2SLwUvcpQKbbcwGbENyKE"  # Replace with your actual API key
# genai.configure(api_key=GEMINI_API_KEY)

# # Set a valid model name. Options include "gemini-2.0-flash", "gemini-2.0-flash-lite", etc.
# MODEL_NAME = "gemini-2.0-flash"

# # Function to check for invalid conversion requests (e.g., converting temperature to weight)
# def is_invalid_conversion(user_input):
#     weight_units = ["kilogram", "kilograms", "gram", "grams", "pound", "pounds"]
#     temp_units = ["fahrenheit", "celsius", "kelvin"]
#     contains_weight = any(unit in user_input.lower() for unit in weight_units)
#     contains_temp = any(unit in user_input.lower() for unit in temp_units)
#     return contains_weight and contains_temp

# # AI Chatbot function using the Gemini API
# def chatbot_response(user_input):
#     if is_invalid_conversion(user_input):
#         return "❌ Error: You cannot convert temperature (e.g., Fahrenheit) into weight (e.g., Kilograms). Please enter a valid question."
#     try:
#         model = genai.GenerativeModel(model_name=MODEL_NAME)
#         response = model.generate_content(user_input)
#         return response.text
#     except Exception as e:
#         return f"❌ Error: {str(e)}"

# # Unit conversion function
# def convert_units(value, from_unit, to_unit):
#     conversion_rates = {
#         "meters": {"kilometers": 0.001, "centimeters": 100, "miles": 0.000621371},
#         "kilograms": {"grams": 1000, "pounds": 2.20462},
#         "celsius": {"fahrenheit": lambda c: (c * 9/5) + 32, "kelvin": lambda c: c + 273.15},
#     }
#     if from_unit in conversion_rates and to_unit in conversion_rates[from_unit]:
#         conversion = conversion_rates[from_unit][to_unit]
#         return conversion(value) if callable(conversion) else value * conversion
#     else:
#         return "Invalid Conversion"

# # Build the Streamlit UI
# st.title("🔄 Smart Bit Converter & AI Chatbot ⚡")
# tab1, tab2 = st.tabs(["📏 Unit Converter", "🤖 AI Chatbot"])

# # Unit Converter Tab
# with tab1:
#     st.markdown("### 🚀 Unit Converter")
#     value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
#     col1, col2 = st.columns(2)
#     with col1:
#         from_unit = st.selectbox("From Unit", ["meters", "kilograms", "celsius"], index=0)
#     with col2:
#         to_unit = st.selectbox("To Unit", ["kilometers", "centimeters", "miles", "grams", "pounds", "fahrenheit", "kelvin"], index=1)
#     if st.button("Convert"):
#         result = convert_units(value, from_unit, to_unit)
#         st.markdown(f"**✅ Converted Value:** {result} {to_unit}")

# # AI Chatbot Tab
# with tab2:
#     st.markdown("### 🤖 Chat with AI")
#     user_input = st.text_input("Ask me anything:", placeholder="Type your question here...")
#     if st.button("Chat"):
#         ai_response = chatbot_response(user_input)
#         st.markdown(f"**🤖 AI:** {ai_response}")














# -------------------------------
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv 

# Configure Page
st.set_page_config(
    page_title="SmartBit Pro - AI-Powered Conversion Suite",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS Styles
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        }
        .stTextInput input, .stNumberInput input {
            border: 1px solid #dee2e6 !important;
            border-radius: 8px !important;
            padding: 12px !important;
        }
        .stSelectbox div[data-baseweb="select"] {
            border-radius: 8px !important;
        }
        .stButton button {
            background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 12px 24px !important;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stMarkdown h1, h2, h3 {
            color: #1e293b !important;
        }
        .chat-response {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# Configure Gemini API
load_dotenv()

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Ensure API key is not missing
if not GEMINI_API_KEY:
    st.error("❌ Error: Missing API key. Please set GEMINI_API_KEY in your .env file.")
else:
    genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-2.0-flash"

# Function to check for invalid conversion requests
def is_invalid_conversion(user_input):
    weight_units = ["kilogram", "kilograms", "gram", "grams", "pound", "pounds"]
    temp_units = ["fahrenheit", "celsius", "kelvin"]
    contains_weight = any(unit in user_input.lower() for unit in weight_units)
    contains_temp = any(unit in user_input.lower() for unit in temp_units)
    return contains_weight and contains_temp

# AI Chatbot function
def chatbot_response(user_input):
    if is_invalid_conversion(user_input):
        return "❌ Error: You cannot convert temperature into weight. Please enter a valid question."
    try:
        model = genai.GenerativeModel(model_name=MODEL_NAME)
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Unit conversion function
def convert_units(value, from_unit, to_unit):
    conversion_rates = {
        "meters": {"kilometers": 0.001, "centimeters": 100, "miles": 0.000621371},
        "kilograms": {"grams": 1000, "pounds": 2.20462},
        "celsius": {"fahrenheit": lambda c: (c * 9/5) + 32, "kelvin": lambda c: c + 273.15},
        "kilometers": {"meters": 1000},
        "centimeters": {"meters": 0.01},
        "miles": {"meters": 1609.34},
        "grams": {"kilograms": 0.001},
        "pounds": {"kilograms": 0.453592},
        "fahrenheit": {"celsius": lambda f: (f - 32) * 5/9},
        "kelvin": {"celsius": lambda k: k - 273.15},
    }
    if from_unit in conversion_rates and to_unit in conversion_rates[from_unit]:
        conversion = conversion_rates[from_unit][to_unit]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return None

# Build the Streamlit UI
st.title("🚀 SmartBit Pro")
st.markdown("### AI-Powered Conversion Suite")
st.divider()

# Tabs
tab1, tab2 = st.tabs(["📏 Unit Converter", "💬 AI Assistant"])

all_units = ["meters", "kilometers", "centimeters", "miles", 
            "kilograms", "grams", "pounds", "celsius", 
            "fahrenheit", "kelvin"]

# Unit Converter Tab
with tab1:
    with st.container():
        col_head = st.columns([3, 1])
        with col_head[0]:
            st.markdown("### 🔄 Unit Conversion")
            st.markdown("*Precision conversions made simple*")
        with col_head[1]:
            st.image("https://cdn-icons-png.flaticon.com/512/3203/3203883.png", width=80)
        
        st.divider()
        
        # Input Fields (outside form)
        col_input = st.columns(3)
        with col_input[0]:
            value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
        with col_input[1]:
            from_unit = st.selectbox("From Unit", all_units, index=0)
        with col_input[2]:
            to_unit = st.selectbox("To Unit", all_units, index=1)
        
        # Submit Button inside Form (prevents auto-submit message)
        with st.form("conversion_form"):
            submitted = st.form_submit_button("🚀 Convert Now", use_container_width=True)
        
        if submitted:
            result = convert_units(value, from_unit, to_unit)
            if result is not None:
                st.success(f"""
                    **Conversion Result:**  
                    **{value:.2f} {from_unit}** = **{result:.4f} {to_unit}**
                """)
            else:
                st.error("⚠️ Invalid conversion request. Please check unit compatibility.")

# AI Chatbot Tab
with tab2:
    with st.container():
        col_head = st.columns([3, 1])
        with col_head[0]:
            st.markdown("### 💬 AI Assistant")
            st.markdown("*Your smart conversion companion*")
        with col_head[1]:
            st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=80)
        
        st.divider()
        
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
            
        user_input = st.chat_input("Ask me anything about conversions...")
        
        if user_input:
            with st.spinner("💡 Thinking..."):
                ai_response = chatbot_response(user_input)
                st.session_state.chat_history.append({
                    "user": user_input,
                    "ai": ai_response
                })
                
        for chat in st.session_state.chat_history:
            with st.container():
                st.markdown(f"""
                    <div class="chat-response">
                        <strong>👤 You:</strong><br>
                        {chat['user']}
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="chat-response" style="background: #f3f4f6;">
                        <strong>🤖 SmartBit:</strong><br>
                        {chat['ai']}
                    </div>
                """, unsafe_allow_html=True)
