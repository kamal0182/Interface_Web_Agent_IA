# main.py (or the file where you run your agent)
from google.adk.tools.tool_context import ToolContext
from capital_agent.agent import root_agent

def main():
    tool_context = ToolContext()
    
    # Initialize state variables here to avoid KeyError
    tool_context.state["user_name"] = tool_context.state.get("user_name")
    tool_context.state["football_team"] = tool_context.state.get("football_team")
    tool_context.state["match_history"] = tool_context.state.get("match_history")

if __name__ == "__main__":
    main()
