import streamlit as st
from storybotcrew import StoryBotCrew

st.set_page_config(page_title="Story Bot LLM - ELI5", page_icon="📚", layout="centered")

st.title("Story Bot LLM")
st.markdown("Ever wondered how to explain quantum physics, machine learning, or even black holes to a 5-year-old? This app uses a team of intelligent AI agents to do just that. Powered by CrewAI and Gemini-2.0-Flask, it takes any topic you enter, researches it, simplifies it, and transforms it into a fun, age-appropriate story — just like a children's book. Whether you're a parent, teacher, or just curious, this is the perfect way to make complex ideas beautifully simple.")

topic = st.text_input("Enter a topic you'd like explained as a story for a 5-year-old: ")

if st.button("Generate Story"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("The agents are researching, simplifying, and storytelling..."):
            try:
                # Set topic as input if needed (depends on how your agents/tasks are designed)
                
                sbc = StoryBotCrew(topic)
                story = sbc.run_crew()
                
                st.success("Story generated successfully!")

                st.markdown(story)

            except Exception as e:
                st.error("Something went wrong while generating the story. Please try again.")
                st.exception(e)

st.markdown("---")
st.caption("Built using CrewAI, Gemini-2.0-Flash and Streamlit | © SubhamModa 2025")