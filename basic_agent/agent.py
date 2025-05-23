from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime
import random
import os
from pydantic import BaseModel, Field, validator
from google.adk.models.lite_llm import LiteLlm


class DetailFootballTeam(BaseModel) : 
    name: str = Field(description="the name of the FootballTeam")   
    city: str = Field(description="the City of the FootballTeam")
    country: str = Field(description="the The Country of the FootballTeam")
    continent_leagues_total : int  = Field(description="The Total  continent leagues total")
    country_championships_total : int  = Field(description="The Total  country championships \total")
@validator('city', 'country')
def reject_unknown(cls, v):
    if v == "Unknown":
        raise ValueError("there is no team with that name")
    
model = LiteLlm(
    model="openrouter/openai/gpt-4.1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    max_tokens=4000
)
  
def get_current_time() -> dict:
    return   {
        "current_time " : datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    }
def tell_arandom_tory() -> str:
    stories = [
            "The Rise of the Machines",
            "Lost in the Data Stream",
            "Echoes of Code",
            "Desert of Firewalls",
            "Children of the Cloud"
            ];
    return random.choices(stories)
root_agent = Agent(
    name="basic_agent",
    model=model,
    description=(
        "basic-agent."),
    instruction="""You are a helpful agent that gives details about footbal teams.
    Your task to generate a aspecific informations about a team based on user request .
    GUIDELINES :
    -Identify the team name.
    - Current squad
    - Recent match results
    - Tactics or formations
    - League standing
    - History and trophies
    - Stadium and coach
    - Upcoming fixtures
    IMPORTANT : Your response Must be a valid JSON matching this structure : 
    {
    "name": "The Team name here",
    "city": "The City  of the team  here",
    "country": "The Country of the team  here",
    "continent_leagues_total": "The total of the continent leuagues that the team has" ,
    "country_championships_total": "The total of the country leagues that the team has"  
    }
    if the name is unknown  Your response Must be .
    {
    "name": "Unknown",
    "city": "Unknown",
    "country": "Unknown",
    "continent_leagues_total": 0,
    "country_championships_total": 0
    }
    """,
#    tools=[google_search],
   
    output_schema=DetailFootballTeam,
    output_key="teamdetails"

)