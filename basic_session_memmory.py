from dotenv  import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.runners  import Runner
from google.genai import types 
import basic_agent
import uuid
from basic_agent.agent import root_agent
from utils import my_function
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_dir, '.env')

print(f"Loading .env from: {dotenv_path}")
load_dotenv(dotenv_path)

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Missing GOOGLE_API_KEY environment variable")

import google.generativeai as genai
genai.configure(api_key=api_key)
first_state = InMemorySessionService()
initial_state = {
    "user_name" : "younes kamal" ,
    "user_preference" : """
    i like to play football. 
    my favorite  Tv show  is Game  Of Thrones.
    My best team is Real Madrid , Raja Casablanca. 
    MY best best player ever is  Ronaldo.
    i am 20 years old
    """
}
APP_NAME = "Younes Bot"
USER_ID = "youness_kamal"
SESSION_ID = str(uuid.uuid4())
statefule_state =  first_state.create_session(
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
    app_name=APP_NAME
)
print("Created new session  : ")
print(f"\tSession Id  : {SESSION_ID} ")
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=first_state
)
new_message = types.Content(
    role="user" , parts=[types.Part(text="what year i was born?")]
)
for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message
):
    if event.is_final_response():
        if event.content and event.content.parts :
            print(f"Final Response : {event.content.parts[0].text}")
    else :
        print("hohohohohhoho")
print("===Session Event Exploration ===")
session = first_state.get_session(
    app_name=APP_NAME , user_id=USER_ID,session_id=SESSION_ID
)

for key,value in session.state.items() :
    print(f"{key} : {value}")
