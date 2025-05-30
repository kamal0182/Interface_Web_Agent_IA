from google.adk.agents import Agent
from google.adk.tools import google_search
def some_agent_function():
    return "Hello from agent"
match_team = Agent(
    name="match_team", 
    model="gemini-2.0-flash",
    description="an agent can tell the user all the matches in a specific years",
    instruction=""" you can tell the user the who win and who lost with the result.
    example (
        user_input : tell me the matches between Real Madrid and Chelsea form 20020 tell 2021.
        Agent : the matches in 2020
                in chempians league :  Real Madrid : 2 - chelsea : 3 ,
                with back and forth in staduim   and the city   
        )
    give all the matches between them.
    """,
    tools=[google_search]
)