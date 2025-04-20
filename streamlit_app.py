import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openai

st.set_page_config(page_title="Dream11 IPL Predictor", layout="wide")

# Sidebar
st.sidebar.title("🏏 IPL Dream11 Predictor")
menu_option = st.sidebar.radio("Navigate", ["Home", "Team Predictor", "Player Analysis", "Match Insights"])

# Title
st.title("🏆 IPL Fantasy Assistant")
st.markdown("Make smarter Dream11 picks with real-time analysis and predictions.")

# Main sections
if menu_option == "Home":
    st.subheader("Welcome to the ultimate Dream11 IPL assistant!")
    st.write("""
    🔍 Get data-driven suggestions for your Dream11 team  
    📊 Explore player performance stats  
    💡 Make better choices for Captain/Vice-captain  
    """)
    st.image("https://upload.wikimedia.org/wikipedia/en/2/2d/Dream11_Logo.png", width=200)

elif menu_option == "Team Predictor":
    st.subheader("🧠 Team Predictor")
    # --- Inside the Team Predictor section ---
    # --- Match Details ---
    st.markdown("### 🏟️ Match Setup")
    col1, col2, col3 = st.columns(3)
    with col1:
        team1 = st.selectbox("Select Team 1", ["CSK", "MI", "RCB", "KKR", "GT", "SRH", "DC", "RR", "PBKS", "LSG"])
    with col2:
        team2 = st.selectbox("Select Team 2", ["MI", "CSK", "RCB", "KKR", "GT", "SRH", "DC", "RR", "PBKS", "LSG"])
    with col3:
        venue = st.selectbox("Venue", ["Wankhede", "Chepauk", "Eden Gardens", "Narendra Modi", "Chinnaswamy"])

    # --- Match Conditions ---
    st.markdown("### 🌦️ Match Conditions")
    col4, col5 = st.columns(2)
    with col4:
        pitch_type = st.selectbox("Pitch Type", ["Batting Friendly", "Bowling Friendly", "Balanced"])
    with col5:
        weather = st.selectbox("Weather", ["Clear", "Humid", "Rainy", "Overcast"])

    # --- Predict Button ---
    if st.button("🚀 Generate Dream11 Team"):
        st.success(f"Generated Dream11 team for {team1} vs {team2} at {venue}!")

        # TODO: Replace with model/backend API
        sample_team = [
            {"Name": "Virat Kohli", "Role": "Batsman", "Team": team1},
            {"Name": "MS Dhoni", "Role": "Wicket Keeper", "Team": team1},
            {"Name": "Hardik Pandya", "Role": "All-Rounder", "Team": team2},
            {"Name": "Jasprit Bumrah", "Role": "Bowler", "Team": team2},
            # Add more mock players...
        ]
        
        st.markdown("### 🧩 Suggested Team")
        for player in sample_team:
            st.write(f"**{player['Name']}** - {player['Role']} ({player['Team']})")
        
        st.markdown("### 👑 Captain & Vice-Captain Picks")
        st.write("**Captain**: Virat Kohli")
        st.write("**Vice-Captain**: Hardik Pandya")

    st.info("This feature will suggest your ideal Dream11 team based on the latest data.")
    st.write("Coming soon...")

elif menu_option == "Player Analysis":
    st.subheader("📈 Player Analysis")
    st.write("Upload or fetch player data to analyze form, consistency, and points.")
    #adding selectbox to select bowler

    bowler_list = ('a','bbb','bbaaa','asdf','asdqawed')
    selected_bowler = st.selectbox("Select a Bowler", bowler_list)


elif menu_option == "Match Insights":
    st.subheader("📊 Match Insights")
    st.write("See historical stats, venue records, and team matchups.")

