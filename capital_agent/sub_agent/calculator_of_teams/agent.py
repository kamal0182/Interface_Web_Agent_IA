from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
def  calculator_of_teams(team_search : str , tool_context : ToolContext) -> dict : 
    counter = 0  
    All_teams = tool_context.state.get("match_history")
    counter = sum(1 for team in All_teams if team["team_against"].lower() == team_search.lower())
    return {
        "action" : "calculator_of_teams" , 
        "message" : f"You have played against {team_search} {counter} times"
        }
calculator_of_teams = Agent(
    name="calculator_of_teams",
    model="gemini-2.0-flash",
    description=(
        "an agent that can calculate how many times you have played against any team."),
    instruction="""
    You are a subagent that can calculate how many times the user played against a team.
    """,
    tools=[
        calculator_of_teams
    ],
)
