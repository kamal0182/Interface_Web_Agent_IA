from google.genai import types

async def call_agent(runner, user_id, session_id, query):
    new_message = types.Content(
        role="user", parts=[types.Part(text=query)]
    )
    try:
        finale_response_text = None
        async for event in runner.run_async(
            user_id=user_id, session_id=session_id, new_message=new_message
        ):
            response_text = finale_response_basic_generate(event)
            if response_text:
                finale_response_text = response_text
        return finale_response_text or "No response from agent."
    except Exception as e:
        print(f"error {e}")
        return f"Error occurred: {e}"

def finale_response_basic_generate(event):
    # Check if event content exists
    if event.content:
        # Loop through parts to concatenate any text parts
        texts = []
        for part in event.content.parts:
            if part.text:
                texts.append(part.text)
        if texts:
            return " ".join(texts)
    # No text found
    return None
