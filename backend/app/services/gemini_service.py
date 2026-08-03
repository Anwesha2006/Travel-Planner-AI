import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
client=genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def generate_itinerary(
    destination,
    budget,
    travel_style,
    start_date,
    end_date,
    number_of_travelers
):
    prompt=f"""
    Create a detailed travel itinerary for a trip to {destination} with a budget of {budget} USD. 
    The trip should be tailored for {number_of_travelers} travelers and should reflect a {travel_style} travel style. 
    The trip will take place from {start_date} to {end_date}. 
    Please provide a day-by-day breakdown of activities, including recommended attractions, dining options, and any other relevant information.
    """
    response = client.models.generate_content(
    model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    contents=prompt
)
    return response.text
