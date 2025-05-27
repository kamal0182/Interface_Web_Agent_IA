from dotenv  import load_dotenv
from google.adk.sessions import DatabaseSessionService
import capital_agent
import asyncio
import os
from google.adk.runners  import Runner
from utils import call_agent
from capital_agent.agent import root_agent
base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)
# Example using a local SQLite file:
db_url = "sqlite:///./MyTeamHistoryMatches.db"
session_service = DatabaseSessionService(db_url=db_url)
initial_state = {
    "user_name" : "Younes Kamal", 
    "football_team" : "Real madrid"  , 
    "match_history" : []
    
}
async def main_async() :
    APP_NAME="MyTeam Agent"
    USER_ID="youneskamal"
    exesting_session = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID
    )
    if exesting_session and len(exesting_session.sessions) > 0 :
        SESSION_ID = exesting_session.sessions[0].id
        print("continue with existing session : ")
    else : 
        session = session_service.create_session(
            app_name=APP_NAME ,
            user_id=USER_ID ,
            state=initial_state
        )
        SESSION_ID = session.id 
    runner = Runner(
        agent=root_agent ,
        app_name=APP_NAME,
        session_service=session_service
    )
    print("welcome to your Team History Agent")
    print("if you heat quit or exit the agent will end")
    while True:
        print("welcome to Your Team History!")
        user_input = input("You : ")
        if user_input.lower()  in ["exit", "quit"] :
            break
        response = await call_agent(runner,USER_ID ,SESSION_ID , user_input)
        print ("Agent : ",response )

asyncio.run(main_async())    
