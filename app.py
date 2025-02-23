#streamlit

import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

st.title("🌱 Growth Mindset Challenge: Build a Positive Mindset with Streamlit")

st.header("🌟 Welcome to the Growth Mindset Challenge!")
st.write("Each day, take on a new challenge to strengthen your mindset and grow beyond your limits.")

# Quotes Section
st.header("💡 Today's Growth Mindset Quote 🚀")
st.write("Difficulties in life are not obstacles, but stepping stones to success.")

# Daily Challenge
st.header("🎯 Today's Challenge") 
user_input = st.text_input("How do you plan to tackle today's challenge?")

# Condition
if user_input:
    st.success(f"💪 You're taking on: {user_input}. Keep moving forward and embrace the journey!")
else:
    st.warning("Share how you'll complete today's challenge to get started!")

# Reflection Section
st.header("📝 Reflect on Your Journey")
reflection = st.text_area("Write your thoughts and insights here:")

if reflection: 
    st.success(f"🌟 Great Reflection! Your insight: {reflection}")
else: 
    st.info("Reflection fuels growth! Take a moment to note your learning.")

# Achievements Section
st.header("🏆 Celebrate Your Progress!")
achievement = st.text_input("Share a recent accomplishment you're proud of:")

if achievement:
    st.success(f"🎉 Fantastic! You achieved: {achievement}")
else:
    st.info("Recognizing small wins leads to big success. Share something you're proud of!")

# Footer
st.write("---")
st.write("💡 Keep believing in yourself and your potential! 🌱")
st.write("© Created by Izma Sadiq")
