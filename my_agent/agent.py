 

from google.adk.agents.llm_agent import Agent
from my_agent.tools.time_tool import get_current_time
from my_agent.tools.weather_tool import get_current_weather
from my_agent.tools.expense_tool import (
    get_expense_summary,
    get_expense_by_category,
    get_expense_by_period
)
from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A smart AI assistant that can answer general questions and provide real-time info like weather and time.",
    instruction=(
        "You are a knowledgeable and friendly AI assistant. "
        "Answer general questions conversationally using your own knowledge. "
        "If the question involves time or weather, use the provided tools: "
        "'get_current_time' for city time, and 'get_current_weather' for live weather info."
    ),
    tools=[get_current_time, get_current_weather, get_expense_summary ,get_expense_by_category,
        get_expense_by_period,],
)
