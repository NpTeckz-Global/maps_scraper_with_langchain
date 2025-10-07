from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os, requests, json, re
from config import SERPAPI_URL   # ✅ Import SerpAPI URL from config file

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")  # Get from https://serpapi.com/

def extract_emails_from_url(url):
    try:
        response = requests.get(url, timeout=5)
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text)
        return ", ".join(set(emails)) if emails else "N/A"
    except:
        return "N/A"

# ---------------- Define Google Maps Scraping Tool ----------------
@tool
def scrape_google_maps(query: str) -> str:
    """Scrape Google Maps data (name, address, contact, rating, website, email) using SerpAPI."""
    try:
        params = {
            "engine": "google_maps",
            "q": query,
            "type": "search",
            "api_key": SERPAPI_KEY
        }

        # ✅ Use imported URL
        response = requests.get(SERPAPI_URL, params=params)
        data = response.json()

        results = data.get("local_results", [])
        output = []

        for r in results:
            name = r.get("title", "N/A")
            address = r.get("address", "N/A")
            phone = r.get("phone", "N/A")
            rating = r.get("rating", "N/A")
            website = r.get("website", "N/A")
            email = extract_emails_from_url(website) if website != "N/A" else "N/A"

            info = (
                f"Name: {name}\n"
                f"Address: {address}\n"
                f"Phone: {phone}\n"
                f"Rating: {rating}\n"
                f"Website: {website}\n"
                f"Email: {email}\n"
                "-----------------------------\n"
            )
            output.append(info)

        file_name = query.replace(" ", "_") + ".txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.writelines(output)

        return f"✅ Scraping complete. Results saved to '{file_name}'"

    except Exception as e:
        return f"❌ Error scraping Google Maps: {e}"

# ---------------- Create AI Model and Agent ----------------
def main():
    model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=GROQ_API_KEY
    )

    tools = [scrape_google_maps]
    agent_executor = create_react_agent(model, tools)

    print("🤖 Welcome to Google Maps AI Scraper!")
    print("Type your prompt (e.g. 'Get all software companies in Hyderabad')")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("Goodbye 👋")
            break

        print("\nAssistant: ", end="")
        try:
            for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}
            ):
                if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="", flush=True)
            print()
        except Exception as e:
            print(f"\n[Error] {e}")

# ---------------- Run the Script ----------------
if __name__ == "__main__":
    main()
