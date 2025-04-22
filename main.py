# This python file deals with analysis of data and prediction of the team.


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

global team_data , player_data 




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

    # print(f"Performance statistics for {player_name}:")
    # for key, value in result.items():
    #    print(f"{key}: {value}")
    return(result)


def batting_analysis(player_name):
    # Plotting the performance over the years
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(player_data['Year'], player_data['Runs_Scored'], marker='o', label='Runs Scored')
    ax.bar(player_data['Year'], player_data['Balls_Faced'], alpha=0.5, label='Balls Faced', color='orange')
    ax.set_title(f"Performance of {player_name} Over the Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Performance")
    ax.set_xticks(player_data['Year'])
    ax.legend()
    ax.grid()
    return (fig)


def fours_sixes_analysis(player_name):
    # Plotting the performance over the years
    fig,ax=plt.subplots(figsize=(12, 6))
    ax.plot(player_data['Year'], player_data['Fours'], marker='o', label='Fours')
    ax.plot(player_data['Year'], player_data['Sixes'], marker='o', label='Sixes')
    ax.set_title(f"Performance of {player_name} Over the Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Performance")
    ax.set_xticks(player_data['Year'])
    ax.legend()
    ax.grid()
    return fig

def bowling_analysis(player_name):
    # Plotting the performance over the years
    fig,ax=plt.subplots(figsize=(12, 6))
    ax.plot(player_data['Year'], player_data['Wickets_Taken'], marker='o', label='Wickets Taken')
    ax.bar(player_data['Year'], player_data['Runs_Conceded'], alpha=0.5, label='Runs Conceded', color='orange')
    ax.set_title(f"Performance of {player_name} Over the Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Performance")
    ax.set_xticks(player_data['Year'])
    ax.legend()
    ax.grid()
    return fig

def fielding_analysis(player_name):
    # Plotting the performance over the years
    fig,ax=plt.subplots(figsize=(12, 6))
    ax.plot(player_data['Year'], player_data['Catches_Taken'], marker='o', label='Catches Taken')
    ax.plot(player_data['Year'], player_data['Stumpings'], marker='o', label='Stumpings')
    ax.set_title(f"Performance of {player_name} Over the Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Performance")
    ax.set_xticks(player_data['Year'])
    ax.legend()
    ax.grid()
    return fig





def player_analysis(player_name):
    #importing the data
    df = pd.read_csv("data/cricket_data_2025.csv")

    global player_data
    player_data = df[df['Player_Name'] == player_name]

    if player_data.empty:
        return(None)
    
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
    return(player_performance(player_name))
    batting_analysis(player_name)
    fours_sixes_analysis(player_name)
    bowling_analysis(player_name)
    fielding_analysis(player_name)

    print('-------------------------------------')









def team_performance(team_name):
    """
    This function takes a team's name as input and returns their performance statistics.
    """
    matches_played = 0 
    matches_won = 0
    toss_won = 0
    championships_won = 0
    runner_up = 0
    for i in team_data['team1']:
        if i == team_name:
            matches_played += 1
    for i in team_data['team2']:
        if i == team_name:
            matches_played += 1
    for i in team_data['winner']:
        if i == team_name:
            matches_won += 1
    for i in team_data['toss_winner']:
        if i == team_name:
            toss_won += 1
    for i in team_data[['team1','team2','winner','match_type']].values:
        if i[0] == team_name and i[3] == 'Final' or i[1] == team_name and i[3] == 'Final':
            if i[2] == team_name:
                championships_won += 1
            else:
                runner_up += 1
    
    result = {
        'Matches Played': matches_played,
        'Matches Won': matches_won,
        'Matches Lost': matches_played - matches_won,
        'Win Percentage': matches_won / matches_played * 100 if matches_played > 0 else 0,
        'Toss Won': toss_won,
        'Toss Lost': matches_played - toss_won,
        'Toss Win Percentage': toss_won / matches_played * 100 if matches_played > 0 else 0,
        'Championships Won': championships_won,
        'Runner Up': runner_up
    }

    #print(f"Performance statistics for {team_name}:")
    # for key, value in result.items():
    #     print(f"{key}: {value}")
    return(result)


def venue_performance_analysis(team_name):
    """
    This function takes a team's name as input and returns their performance statistics at different venues.
    """
    venue_performance = team_data.groupby('venue')['winner'].value_counts().unstack().fillna(0)
    venue_performance['Total Matches'] = venue_performance.sum(axis=1)
    venue_performance['Win Percentage'] = (venue_performance[team_name] / venue_performance['Total Matches']) * 100
    venue_performance['Matches Won'] = venue_performance[team_name]

    fig,ax=plt.subplots(figsize=(12, 10))
    sns.barplot(y=venue_performance.index, x=venue_performance['Win Percentage'], data=venue_performance.reset_index())
    for i in ax.containers:
        ax.bar_label(i, label_type='edge', fontsize=10, color='black')
    ax.set_xlim(0, 100)
    ax.set_xticks(np.arange(0, 101, 10))
    ax.set_xticklabels(np.arange(0, 101, 10), fontsize=10)
    ax.set_yticklabels(venue_performance.index, fontsize=10)
    ax.set_title(f"Win Percentage of {team_name} at Different Venues")
    fig.tight_layout()
    ax.set_ylabel("Venue")
    ax.set_xlabel("Matches Won %")
    return fig


def team_analysis(team_name):
    # importing the data
    df = pd.read_csv("data/matches.csv")
    global team_data
    team_data = None
    for i in df['team1'].unique():
        if i == team_name:
            team_data1 = df[df['team1'] == team_name] 
            team_data2 = df[df['team2'] == team_name]
            team_data = pd.concat([team_data1, team_data2], ignore_index=True)
            team_data = team_data.drop_duplicates()
            #team_name = 'Chennai Super Kings'
            return(team_performance(team_name))
        else:
            continue
    
    if team_data is None:
        return(None)





#team_analysis('Chennai Super Kings')
#player_analysis('MS Dhoni')









