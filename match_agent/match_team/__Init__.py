
def my_function_in_match_team():
    from . import agent  # Import inside function to avoid circular import
    # Now you can use things from agent.py safely here
    result = agent.some_agent_function()
    return result