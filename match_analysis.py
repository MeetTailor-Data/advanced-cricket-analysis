import pandas as pd
import numpy as np

data = {
    "Match_ID": [1,1,1,1,2,2,2,2,3,3,3,3],
    "Team": ["India","India","Australia","Australia",
             "India","India","Australia","Australia",
             "India","India","Australia","Australia"],
    "Player": ["A","B","C","D","E","F","G","H","I","J","K","L"],
    "Runs": [50, np.nan, 70, 30, 100, 20, 60, np.nan, 80, 40, 10, 90],
    "Balls": [30, 25, 40, 35, 60, 15, 45, 20, 50, 30, 10, 55]
}

df = pd.DataFrame(data)
print(df)
#phase-1
miss=df.isna().sum()
print(miss)

df = df.fillna(0)
print(df)

df['Strike_Rate'] = (df['Runs'] / df['Balls']) * 100

#phase-2
conditions = [
    df["Runs"] >= 80,
    (df["Runs"] >= 40) & (df["Runs"] < 80),
    df["Runs"] < 40
]
choices = ["Excellent", "Good", "Low"]

df["Performance"] = np.select(conditions, choices,default="none")
print(df)

#phase-3
truns=df.groupby("Team")["Runs"].sum()
print(truns)

team_strike_rate=df.groupby("Team")["Strike_Rate"].mean()
print(team_strike_rate)

tb=df.groupby("Team")["Balls"].sum()
print(tb)

if team_strike_rate['India'] > team_strike_rate['Australia']:
  print("Indian team is more aggressive")
else:
  print("Australia team is more aggressive")

#phase-4
top_scorers = df.loc[df.groupby("Player")["Runs"].idxmax().head(1)]
print(top_scorers)

top_scorers_team = df.loc[df.groupby("Team")["Runs"].idxmax().head(1)]
print(top_scorers_team)

hst = df.loc[df.groupby("Player")["Strike_Rate"].idxmax().head(1)]
print(hst)

print("Count of Excellent Performances per Team:")
print(pd.crosstab(df["Team"], df["Performance"])["Excellent"])

#phase-5
total_runs_per_match = df.groupby('Match_ID')['Runs'].sum()
print("Total Runs Scored Per Match:\n", total_runs_per_match)
best_player_per_match = df.loc[df.groupby('Match_ID')['Runs'].idxmax()]
print("\nBest Player in Each Match:\n", best_player_per_match[['Match_ID', 'Player', 'Runs']])

highest_run_match_id = total_runs_per_match.idxmax()
highest_run_match_value = total_runs_per_match.max()
print(f"\nMatch with the Highest Total Runs: Match ID {highest_run_match_id} with {highest_run_match_value} runs.")
print("Consistent players")
consistent_players = df[df['Runs']>=40]
print(consistent_players)

