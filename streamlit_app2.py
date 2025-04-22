# import streamlit as st
# from main import player_analysis,batting_analysis,team_analysis,fours_sixes_analysis,bowling_analysis,fielding_analysis,venue_performance_analysis


# st.title("🏏 IPL Analyzer & Live Match Predictor")
# st.image("https://tse4.mm.bing.net/th/id/OIP.ApSe1JqN2PS3VsO2D2hr5wHaDy?rs=1&pid=ImgDetMain", width=200)
# # Sidebar navigation
# option = st.sidebar.radio("Navigate", ["Player Analysis", "Team Analysis"])


# if option == "Player Analysis":
#     player_name = st.text_input("Enter Player Name", "Virat Kohli")
#     if st.button("Get Stats"):
#         stats = player_analysis(player_name)
#         if stats is None:
#             st.error("Player not found or no data available.")
#         else:
#             for i in stats:
#                 st.write(f"**{i}**: {stats[i]}")
#             fig1 = batting_analysis(player_name)
#             st.pyplot(fig1)
#             fig2 = fours_sixes_analysis(player_name)
#             st.pyplot(fig2)
#             fig3 = bowling_analysis(player_name)
#             st.pyplot(fig3)
#             fig4 = fielding_analysis(player_name)
#             st.pyplot(fig4)
            

# elif option == "Team Analysis":
#     team_name = st.text_input("Enter Team Name", "Chennai Super Kings")
#     if st.button("Get Match Stats"):
#         match_data = team_analysis(team_name)
#         if match_data is None:
#             st.error("Team not found or no data available.")
#         else:
#             for i in match_data:
#                 st.write(f"**{i}**: {match_data[i]}")
#             fig5 = venue_performance_analysis(team_name)
#             st.pyplot(fig5)







import streamlit as st
from main import (
    player_analysis, batting_analysis, fours_sixes_analysis,
    bowling_analysis, fielding_analysis,team_analysis, venue_performance_analysis
)

st.set_page_config(page_title="IPL Analyzer", layout="wide")

# Header
st.image("https://tse4.mm.bing.net/th/id/OIP.ApSe1JqN2PS3VsO2D2hr5wHaDy?rs=1&pid=ImgDetMain", width=150)
st.markdown("""
    <h1 style="text-align:center; color:#1f77b4;">🏏 IPL Analyzer & Live Match Predictor</h1>
""", unsafe_allow_html=True)



# Sidebar navigation
option = st.sidebar.radio("📂 Navigate", ["Player Analysis", "Team Analysis"])

# Main content
st.markdown("---")

if option == "Player Analysis":
    st.subheader("🔍 Player Performance Breakdown")


    player_name = st.text_input("Enter Player Name", "Virat Kohli")

    if st.button("Get Player Stats"):
        stats = player_analysis(player_name)

        if not stats:
            st.error("Player not found or no data available.")
        else:
            st.success(f"Showing stats for {player_name}")
            with st.expander("📊 Player Summary Stats", expanded=True):
                st.dataframe(stats, use_container_width=True)

            st.markdown("### 🧠 Insights and Visualizations")

            # Use columns for a responsive layout
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Batting Over Years**")
                fig1 = batting_analysis(player_name)
                st.pyplot(fig1)

                st.markdown("**Fielding Performance**")
                fig4 = fielding_analysis(player_name)
                st.pyplot(fig4)

            with col2:
                st.markdown("**Fours and Sixes Analysis**")
                fig2 = fours_sixes_analysis(player_name)
                st.pyplot(fig2)

                st.markdown("**Bowling Contributions**")
                fig3 = bowling_analysis(player_name)
                st.pyplot(fig3)

elif option == "Team Analysis":
    st.subheader("🏟️ Team Performance Insights")

    team_name = st.text_input("Enter Team Name", "Chennai Super Kings")

    if st.button("Get Team Stats"):
        match_data = team_analysis(team_name)

        if not match_data:
            st.error("Team not found or no data available.")
        else:
            st.success(f"Performance data for {team_name}")
            with st.expander("📊 Team Summary Stats", expanded=True):
                st.dataframe(match_data, use_container_width=True)

            st.markdown("### 📍 Venue-Based Analysis")
            fig5 = venue_performance_analysis(team_name)
            st.pyplot(fig5)
st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #000000;  /* Dark background for footer */
            color: #ffffff;  /* White text for contrast */
            text-align: center;
            padding: 10px 0;
            font-size: 15px;
            font-weight: 500;
            font-family: 'Arial', sans-serif;
            box-shadow: 0 -1px 5px rgba(0,0,0,0.1);
        }
        .footer a {
            color: #1f77b4;  /* Blue link color */
            text-decoration: underline;
            text-decoration: none;
            font-weight: bold;
        }
    </style>

    <div class="footer">
        🏏Copyright © 2025 | Powered by <b>Streamlit</b> ⚡ | 🔎Analysis by 
        <a href="mailto:abdulraqeeb437@gmail.com" target="_blank">Abdul Raqeeb </a>
    </div>
""", unsafe_allow_html=True)























