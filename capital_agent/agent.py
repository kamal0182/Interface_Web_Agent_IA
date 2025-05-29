from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from capital_agent.sub_agent.calculator_of_teams.agent import calculator_of_teams

def addaMatch(team_against: str, result: str, tool_context: ToolContext) -> dict:
    """
    Args:
        match_history: match history to add
        tool_context: context for accessing and updating session state
    """
    user_team = tool_context.state.get("football_team").lower()
    opponent = team_against.lower()

    if opponent == user_team:
        return {
                "action": "addaMatch",
                "message": f"You cannot add a match where the opponent is your own team ({user_team})."
                }
    match_history = {
        "team_against" : team_against , 
        "result" : result
    }
    print(match_history)
    match_historys = tool_context.state.get("match_history",[])
    match_historys.append(match_history)
    print(match_historys)
    tool_context.state["match_history"] = match_historys

    return {
            "action": "addaMatch",
            "message": f"OK. I've added the match between {user_team} and {team_against} with the result {result} to your match history."
            }
def deleteTeam(team_to_delete :str ,  tool_context : ToolContext)->dict:
    AllTeams = tool_context.state.get("match_history")
    teams = [m for m in AllTeams if m["team_against"].lower() != team_to_delete.lower()]
    tool_context.state["match_history"] = teams
    return {
        "action" : "deleteTeam",
        "message" : f"all the matches against {team_to_delete} is deleted Successfully"
    }
def tellTheUserName(tool_context:ToolContext)->dict :
    user_name  = tool_context.state.get("user_name")
    return {
            "action": "tellTheUserName",
            "message": f"Your name is {user_name}"
            }

def bestTeam(tool_context:ToolContext)->dict :
    mybestTeam = tool_context.state.get("football_team")
    return {
            "action": "bestTeam",
            "message": f"Your favorite football team is {mybestTeam}."
            }

root_agent = Agent(
    name="capital_agent",
    model="gemini-2.0-flash",
    description=(
        "basic-agent."),
    instruction="""You are a helpfull agent that stores Matches scores about user best team.
    and You can tell the user his name.
    - You can add and update and delete and view to database.
    - you can tell the user his best team
    - Full name is stored in `user_name`
    the user informations stored in state:
    Name : 
    {user_name}
    football_team :
    {football_team}
    match History :
    {match_history}
    You can help the user to manage ther team with the following capabilitie :
    1 - add a new History or add match
    2 - tell the user his name 
    GUIDLINES :
    2. if the user about his name you can tell him his name
    """,
    sub_agents=[calculator_of_teams],
    tools=[
        addaMatch,
        tellTheUserName,
        bestTeam,
        deleteTeam,
    ],
)
