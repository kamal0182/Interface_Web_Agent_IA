from google.adk.agents import Agent
from google.adk.tools import google_search

agent  = Agent (
    name="history_Against_a_Team_In_Specific_Year",
    model="gemini-2.0-flash",
    description="an agent that can give the history against a team in a specific team",
    instruction= """ You can tell the user the matches that his {football_team} played against the team hes asked for in a specific year.
    """,
    tools=[google_search],
)