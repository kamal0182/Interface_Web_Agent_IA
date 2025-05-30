from match_agent.match_team.agent import match_team
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

root_agent = Agent(
    name= "match_agent", 
    model= "gemini-2.0-flash" , 
    description="An agent that can use a Toool agent offre the user to see the infromation between two teams",
    instruction="""
    You are an agent that use a tool agent that tell the user result aginst another team 
    """ , 
    tools= [AgentTool(match_team)]
)
