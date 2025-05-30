from google.adk.agents import Agent
root_agent = Agent(
    name="basic_agent",
    model="gemini-2.0-flash",
    description=(
        "basic-agent."),
    instruction="""You are a helpfull agent that give informations about the user.
    the user informations stored in state:
    Name : 
    {user_name}
    preferences :
    {user_preference}   
    """,
#    tools=[google_search],

)