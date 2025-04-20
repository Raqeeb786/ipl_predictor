# This python file deals with analysis of data and prediction of the team.


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# importing the data
df = pd.read_csv("data/cricket_data_2025.csv")



# Function to find the best figure from a list of strings
def find(x):
    """
    This function takes a list of strings and returns the best figure from the list.   
    """
    best = None
    best_wickets = 0
    best_runs = 9999

    for fig in x:
        if fig == 0 or fig==0.0 or fig=='0' :
            fig='0/0'
        if fig == 'No stats':
            fig = '0/0'
        parts = fig.split('/')
        wickets = int(parts[0])
        runs = int(parts[1])

        if wickets > best_wickets:
            best = fig
            best_wickets = wickets
            best_runs = runs
        elif wickets == best_wickets and runs < best_runs:
            best = fig
            best_runs = runs
    return best


def player_performance(player_name):
    """
    This function takes a player's name as input and returns their performance statistics.
    """
    a= player_data['Matches_Batted'].sum()
    b= player_data['Not_Outs'].sum()
    c= player_data['Runs_Scored'].sum()
    d= player_data['Highest_Score'].max()
    e= player_data['Batting_Average'].mean()
    f= player_data['Balls_Faced'].sum()
    g= player_data['Batting_Strike_Rate'].mean()
    h= player_data['Centuries'].sum()
    i= player_data['Half_Centuries'].sum()
    j= player_data['Fours'].sum()
    k= player_data['Sixes'].sum()
    l= player_data['Catches_Taken'].sum()
    m= player_data['Stumpings'].sum()
    n= player_data['Matches_Bowled'].sum()
    o= player_data['Balls_Bowled'].sum()
    p= player_data['Runs_Conceded'].sum()
    q= player_data['Wickets_Taken'].sum()
    r= player_data['Best_Bowling_Match'].tolist()
    s= player_data['Bowling_Average'].mean()
    t= player_data['Economy_Rate'].mean()
    u= player_data['Bowling_Strike_Rate'].mean()
    v= player_data['Four_Wicket_Hauls'].sum()
    w= player_data['Five_Wicket_Hauls'].sum()

    result= {
        'Matches Batted': a,
        'Not Outs': b,
        'Runs Scored': c,
        'Highest Score': d,
        'Batting Average': e,
        'Balls Faced': f,
        'Batting Strike Rate': g,
        'Centuries': h,
        'Half Centuries': i,
        'Fours': j,
        'Sixes': k,
        'Catches Taken': l,
        'Stumpings': m,
        'Matches Bowled': n,
        'Balls Bowled': o,
        'Runs Conceded': p,
        'Wickets Taken': q,
        'Best Bowling Match': find(r),
        'Bowling Average': s,
        'Economy Rate': t,
        'Bowling Strike Rate': u,
        'Four Wicket Hauls': v,
        'Five Wicket Hauls': w
    }

    print(f"Performance statistics for {player_name}:")
    for key, value in result.items():
       print(f"{key}: {value}")
    #return(result)


def batting_analysis(player_name):
    # Plotting the performance over the years
    plt.figure(figsize=(12, 6))
    plt.plot(player_data['Year'], player_data['Runs_Scored'], marker='o', label='Runs Scored')
    plt.bar(player_data['Year'], player_data['Balls_Faced'], alpha=0.5, label='Balls Faced', color='orange')
    plt.title(f"Performance of {player_name} Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Performance")
    plt.xticks(player_data['Year'])
    plt.legend()
    plt.grid()
    plt.show()

def fours_sixes_analysis(player_name):
    # Plotting the performance over the years
    plt.figure(figsize=(12, 6))
    plt.plot(player_data['Year'], player_data['Fours'], marker='o', label='Fours')
    plt.plot(player_data['Year'], player_data['Sixes'], marker='o', label='Sixes')
    plt.title(f"Performance of {player_name} Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Performance")
    plt.xticks(player_data['Year'])
    plt.legend()
    plt.grid()
    plt.show()

def bowling_analysis(player_name):
    # Plotting the performance over the years
    plt.figure(figsize=(12, 6))
    plt.plot(player_data['Year'], player_data['Wickets_Taken'], marker='o', label='Wickets Taken')
    plt.bar(player_data['Year'], player_data['Runs_Conceded'], alpha=0.5, label='Runs Conceded', color='orange')
    plt.title(f"Performance of {player_name} Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Performance")
    plt.xticks(player_data['Year'])
    plt.legend()
    plt.grid()
    plt.show()

def fielding_analysis(player_name):
    # Plotting the performance over the years
    plt.figure(figsize=(12, 6))
    plt.plot(player_data['Year'], player_data['Catches_Taken'], marker='o', label='Catches Taken')
    plt.plot(player_data['Year'], player_data['Stumpings'], marker='o', label='Stumpings')
    plt.title(f"Performance of {player_name} Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Performance")
    plt.xticks(player_data['Year'])
    plt.legend()
    plt.grid()
    plt.show()





while True:
    player_name = input("Enter the name of the player: ")

    player_data = df[df['Player_Name'] == player_name]
    if player_data.empty:
        print( f"No data found for player: {player_name}" )
    
    #print(player_data.columns)
    for i in player_data:
        if i == 'Player_Name':
            continue
        elif i == "Year":
            player_data[i] = player_data[i].astype(int)
        else:
            try:
                player_data[i] = player_data[i].astype(str)
                player_data[i] = player_data[i].str.replace('No stats', '0')
                player_data[i] = player_data[i].str.replace('*', '')
                player_data[i] = player_data[i].astype(float)
            except:
                pass
    #player_data.info()
    player_performance(player_name)
    batting_analysis(player_name)
    fours_sixes_analysis(player_name)
    bowling_analysis(player_name)
    fielding_analysis(player_name)

    print('-------------------------------------')













