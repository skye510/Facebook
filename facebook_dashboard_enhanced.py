import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from PIL import Image
import requests
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Skye's AI-Enhanced Analytics",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1rem;
    }
    .logo-img {
        max-width: 150px;
        margin-bottom: 1rem;
    }
    .main-header {
        color: #1877f2;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

def load_meta_logo():
    # Load the Meta AI logo
    st.markdown(
        """
        <div class="logo-container">
            <img 
src="https://raw.githubusercontent.com/skye510/facebook-analytics/main/meta_ai_logo.png" 
                 class="logo-img" alt="Meta AI Logo"/>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    # Display logo
    load_meta_logo()
    
    # Main navigation - Fixed the syntax error here
    page = st.sidebar.selectbox(
        "Navigation",
        ["Dashboard", "AI Assistant", "Content Generator", "Performance 
Insights"]
    )

    if page == "Dashboard":
        show_main_dashboard()
    elif page == "AI Assistant":
        show_ai_assistant()
    elif page == "Content Generator":
        show_content_generator()
    elif page == "Performance Insights":
        show_performance_insights()

def show_main_dashboard():
    st.markdown('<h1 class="main-header">📊 Facebook Analytics 
Dashboard</h1>', unsafe_allow_html=True)
    st.caption(f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d 
%H:%M:%S')} UTC")
    st.caption("User: skye510")
    
    # Dashboard metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Reach",
            value="0",
            delta="0%",
            help="Number of unique users who saw any of your content"
        )
    
    with col2:
        st.metric(
            label="Engagement Rate",
            value="0%",
            delta="0%",
            help="(Likes + Comments + Shares) / Reach × 100"
        )
    
    with col3:
        st.metric(
            label="Post Performance",
            value="0",
            delta="0%",
            help="Average engagement per post"
        )
    
    with col4:
        st.metric(
            label="Audience Growth",
            value="0",
            delta="0%",
            help="New followers in selected period"
        )

def show_ai_assistant():
    st.markdown('<h1 class="main-header">🤖 AI Social Media 
Assistant</h1>', unsafe_allow_html=True)
    st.write("Hello skye510! How can I help you today?")
    
    question = st.text_input(
        "Ask me anything about your Facebook data:",
        placeholder="Example: What were my best performing posts last 
month?"
    )
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📈 Analyze Trends"):
            st.info("Analyzing your page trends... (LLM will be connected 
later)")
    with col2:
        if st.button("🎯 Get Recommendations"):
            st.info("Generating personalized recommendations... (LLM will 
be connected later)")
    with col3:
        if st.button("📊 Generate Report"):
            st.info("Creating detailed report... (LLM will be connected 
later)")

def show_content_generator():
    st.markdown('<h1 class="main-header">✍️ AI Content Generator</h1>', 
unsafe_allow_html=True)
    
    content_type = st.selectbox(
        "What type of content do you want to generate?",
        ["Post", "Poll", "Contest", "Story"]
    )
    
    topic = st.text_input("Topic or theme:", placeholder="Enter a topic 
for your content")
    
    tone = st.select_slider(
        "Select content tone:",
        options=["Professional", "Casual", "Humorous", "Inspirational"]
    )
    
    if st.button("Generate Content"):
        st.info("Content generation will be connected to LLM later")
        st.code("""
        Sample Generated Post:
        📢 Exciting news! We're launching something special...
        #Innovation #Technology #Future
        """)

def show_performance_insights():
    st.markdown('<h1 class="main-header">🎯 AI Performance Insights</h1>', 
unsafe_allow_html=True)
    
    period = st.selectbox(
        "Analysis Period",
        ["Last Week", "Last Month", "Last Quarter", "Custom"]
    )
    
    tab1, tab2, tab3 = st.tabs(["Content Analysis", "Audience Insights", 
"Recommendations"])
    
    with tab1:
        st.subheader("Content Performance Analysis")
        st.info("AI will analyze your content performance patterns")
        
    with tab2:
        st.subheader("Audience Behavior Insights")
        st.info("AI will provide detailed audience insights")
        
    with tab3:
        st.subheader("AI Recommendations")
        st.info("Personalized recommendations will appear here")

if __name__ == "__main__":
    main()
