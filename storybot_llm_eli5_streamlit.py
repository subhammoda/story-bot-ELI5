import streamlit as st
import os
import sys

# Add better error handling for imports
try:
    from storybotcrew import StoryBotCrew
except ImportError as e:
    st.error(f"Import error: {e}")
    st.info("Please check that all dependencies are installed correctly.")
    st.stop()

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #FF8C42 0%, #9B59B6 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
    }
    
    /* Title styling */
    .title-text {
        background: linear-gradient(45deg, #FF8C42, #9B59B6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Subtitle styling */
    .subtitle-text {
        color: #2D3748;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #FF8C42;
        padding: 1rem;
        font-size: 1.1rem;
        background: rgba(255, 255, 255, 0.9);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #FF8C42, #9B59B6);
        border-radius: 25px;
        border: none;
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 1rem 2rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 140, 66, 0.3);
        width: 100%;
        max-width: 300px;
        margin: 0 auto;
        display: block;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 140, 66, 0.4);
    }
    
    /* Center button container */
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
    }
    
    /* Story container styling */
    .story-container {
        background: linear-gradient(135deg, #FFF8F0 0%, #F7FAFC 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border-left: 5px solid #FF8C42;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    /* Success message styling */
    .success-message {
        background: linear-gradient(45deg, #48BB78, #38A169);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
    }
    
    /* Warning message styling */
    .warning-message {
        background: linear-gradient(45deg, #F6AD55, #ED8936);
        color: #2D3748;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
    }
    
    /* Error message styling */
    .error-message {
        background: linear-gradient(45deg, #F56565, #E53E3E);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        color: #718096;
        font-style: italic;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #E2E8F0;
    }
    
    /* Loading animation */
    .loading-container {
        text-align: center;
        padding: 2rem;
    }
    
    /* Emoji decorations */
    .emoji-decoration {
        font-size: 2rem;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Configure page
st.set_page_config(
    page_title="Story Bot LLM - ELI5", 
    page_icon="📚", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Check for API key
if not os.getenv('GEMINI_API_KEY'):
    st.markdown('<div class="error-message">⚠️ GEMINI_API_KEY not found in environment variables!</div>', unsafe_allow_html=True)
    st.info("Please add your Gemini API key to the environment variables.")
    st.stop()

# Main container
with st.container():
    st.markdown('<div class="emoji-decoration">📚✨🧠</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="title-text">Story Bot LLM - Explain Like I\'m 5</h1>', unsafe_allow_html=True)
    
    st.markdown('<p class="subtitle-text">Ever wondered how to explain <span style="background: linear-gradient(45deg, #FF8C42, #9B59B6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: bold;">quantum physics</span>, <span style="background: linear-gradient(45deg, #9B59B6, #FF8C42); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: bold;">machine learning</span>, or even <span style="background: linear-gradient(45deg, #F6AD55, #FF8C42); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: bold;">black holes</span> to a 5-year-old? This app uses a team of intelligent AI agents to do just that. Powered by CrewAI and Gemini-2.0-Flash, it takes any topic you enter, researches it, simplifies it, and transforms it into a fun, age-appropriate story — just like a children\'s book. Whether you\'re a parent, teacher, or just curious, this is the perfect way to make complex ideas beautifully simple.</p>', unsafe_allow_html=True)

# Input section with enhanced styling
st.markdown('<div class="emoji-decoration">🎯</div>', unsafe_allow_html=True)
topic = st.text_input("**Enter a topic you'd like explained as a story for a 5-year-old:**", 
                      placeholder="e.g., photosynthesis, gravity, or how computers work")

# Generate button with enhanced styling - centered
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("🚀 Generate Magical Story", type="primary"):
    st.markdown('</div>', unsafe_allow_html=True)
    
    if not topic.strip():
        st.markdown('<div class="warning-message">Please enter a topic to generate a story!</div>', unsafe_allow_html=True)
    else:
        with st.spinner("🪄 The AI agents are working their magic..."):
            try:
                # call crew class to initiate the agents with user defined topic
                sbc = StoryBotCrew(topic)
                story = sbc.run_crew()
                
                st.markdown('<div class="success-message">🎉 Story generated successfully!</div>', unsafe_allow_html=True)
                
                # Display story in a beautiful container
                st.markdown('<div class="story-container"><h3>📖 Your Story</h3> <p>' + str(story) + '</p></div>', unsafe_allow_html=True)
                
                # Add some decorative elements
                st.markdown('<div class="emoji-decoration">🌟✨🎭</div>', unsafe_allow_html=True)

            except Exception as e:
                st.markdown('<div class="error-message">Something went wrong while generating the story. Please try again.</div>', unsafe_allow_html=True)
                st.exception(e)
                st.info("If this is a deployment issue, please check the logs for more details.")
else:
    st.markdown('</div>', unsafe_allow_html=True)

# Footer with enhanced styling
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("---")
st.markdown("**Built with ❤️ using CrewAI, Gemini-2.0-Flash and Streamlit | © SubhamModa 2025**")
st.markdown("</div>", unsafe_allow_html=True)