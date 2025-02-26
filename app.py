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

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ Error: Missing API key. Please check your .env file.")

# Configure API
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
    # Only focus on conversion-related queries
    if is_invalid_conversion(user_input):
        return "❌ Error: You cannot convert temperature into weight. Please enter a valid question about conversions."
    
    # Filter out non-conversion topics
    if not any(unit in user_input.lower() for unit in ["meter", "kilometer", "centimeter", "mile", "kilogram", "gram", "pound", "celsius", "fahrenheit", "kelvin"]):
        return "❌ Please ask a question related to unit or currency conversions. For example, ask about converting meters to kilometers or kilograms to pounds."
    
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
        
        # Input Fields
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
                
        # Display chat history (latest message on top)
        for chat in reversed(st.session_state.chat_history):
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
