from google.adk.agents import Agent

def generate_script(topic: str, feature: str) -> dict:
    """
    Generates a YouTube Shorts-style Hinglish script about a tech feature.

    Args:
        topic (str): The general tech topic (e.g., WhatsApp, GitHub).
        feature (str): The specific feature to explain (e.g., Pull Request).

    Returns:
        dict: Contains status and the script text.
    """
    prompt = f"""
Write a YouTube Shorts-style script (under 60 seconds) with two Delhi college students, Nik & Sid, casually discussing "{feature}" in "{topic}".

Instructions:
🗣️ Use chill Hinglish tone (e.g., "bhai", "scene kya hai", "sach me?", "mast chiz hai").
💬 Only dialog between Nik and Sid — no narration.
🎭 Show emotion in lines (e.g., *excited*, *confused*).
📹 Format into timestamps like: (0-5 sec), (5-15 sec), etc.
😂 Make it funny, casual, and relatable to college students.
"""

    return {
        "status": "success",
        "script": prompt  # The agent will fill in the Gemini LLM response
    }

# Root Agent definition (model handles tool prompts)
root_agent = Agent(
    name="Delhi_Tech_Dost",
    model="gemini-1.5-flash",  # This is all you need to define the model
    description="An AI agent that explains tech features in a Hinglish YouTube Shorts format.",
    instruction="You're Nik and Sid — chill Delhi students. Create funny, Hinglish YouTube Shorts-style convos about tech topics.",
    tools=[generate_script],  # ADK will auto-handle LLM prompting from tool output
)

# import datetime
# from zoneinfo import ZoneInfo
# from google.adk.agents import Agent

# def get_weather(city: str) -> dict:
#     """Retrieves the current weather report for a specified city.

#     Args:
#         city (str): The name of the city for which to retrieve the weather report.

#     Returns:
#         dict: status and result or error msg.
#     """
#     if city.lower() == "new york":
#         return {
#             "status": "success",
#             "report": (
#                 "The weather in New York is sunny with a temperature of 25 degrees"
#                 " Celsius (77 degrees Fahrenheit)."
#             ),
#         }
#     else:
#         return {
#             "status": "error",
#             "error_message": f"Weather information for '{city}' is not available.",
#         }


# def get_current_time(city: str) -> dict:
#     """Returns the current time in a specified city.

#     Args:
#         city (str): The name of the city for which to retrieve the current time.

#     Returns:
#         dict: status and result or error msg.
#     """

#     if city.lower() == "new york":
#         tz_identifier = "America/New_York"
#     else:
#         return {
#             "status": "error",
#             "error_message": (
#                 f"Sorry, I don't have timezone information for {city}."
#             ),
#         }

#     tz = ZoneInfo(tz_identifier)
#     now = datetime.datetime.now(tz)
#     report = (
#         f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
#     )
#     return {"status": "success", "report": report}


# root_agent = Agent(
#     name="weather_time_agent",
#     model="gemini-2.0-flash",
#     description=(
#         "Agent to answer questions about the time and weather in a city."
#     ),
#     instruction=(
#         "You are a helpful agent who can answer user questions about the time and weather in a city."
#     ),
#     tools=[get_weather, get_current_time],
# )