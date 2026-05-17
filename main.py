from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""
You are an expert travel assistant.

Create a travel recommendation based on:

Destination: {destination}
Duration: {days} days
Budget: {budget}
Travel Style: {style}

Include:
1. Day-wise itinerary
2. Suggested attractions
3. Food recommendations
4. Transportation tips
5. Estimated budget
""")

chain = prompt | llm


# User input section
destination = input("Enter city/state in India: ")
days = input("Enter trip duration (days): ")
budget = input("Enter budget (Low/Medium/High): ")
style = input("Enter travel style (Adventure/Family/Relaxation/Nature/etc): ")


response = chain.invoke({
    "destination": destination,
    "days": days,
    "budget": budget,
    "style": style
})

print("\n===== YOUR TRAVEL ITINERARY =====\n")
print(response.content)