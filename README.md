# maps_scraper_with_langchain
The Google Maps AI Scraper uses LangChain, Groq’s Llama 3.1, and SerpAPI to collect business listings from Google Maps. It extracts name, address, phone, rating, website, and email, saving results in clean text files ideal for data analysts, marketers, and AI developers automating web data extraction.
## 🧠 GitHub Repository Overview
## 🏷️ Repository Name
      google-maps-ai-scraper
## 📄 Detailed Description 
The Google Maps AI Scraper is an intelligent data collection tool that uses LangChain, Groq’s Llama 3.1, and SerpAPI to fetch business listings directly from Google Maps.
It automatically extracts key details such as name, address, phone, rating, website, and email, then saves them to neatly formatted text files.
Designed for data analysts, marketers, and AI developers, this project demonstrates how to integrate LLMs and APIs for smart web automation.
## 🧩 Key Features
🧠 AI-powered agent using LangChain + Groq

🔍 Google Maps scraping via SerpAPI

📧 Automatic email extraction from websites

🗂️ Organized output with one file per query

⚙️ Modular design (config.py, queries.py, main.py) for easy collaboration

🌍 Ready to extend with Playwright or Excel integration
## 🧰 Technologies Used
* Python 3.10+
* LangChain Core
* LangGraph
* Groq Llama 3.1
* SerpAPI
* dotenv
* Requests + Regex
## 📦 Installation Steps

 ### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/google-maps-ai-scraper.git
cd google-maps-ai-scraper
### 2️⃣ Create a virtual environment (recommended)
     python -m venv venv
     # Windows
     venv\Scripts\activate
     # macOS/Linux
     source venv/bin/activate
3️⃣ Install required packages
    # Install core packages
       pip install langchain-core langchain-groq langgraph python-dotenv requests
    # (Optional) If using Playwright
        pip install playwright
        playwright install
4️⃣ Setup environment variables
    cp .env.example .env  # macOS/Linux
    copy .env.example .env  # Windows
Add your keys:
  GROQ_API_KEY=your_groq_api_key
  SERPAPI_KEY=your_serpapi_key
⚡ Usage
   1️⃣ Run the scraper
       python google_maps_ai_scraper.py run
   2️⃣ Example commands
       Get all software companies in Hyderabad
🧩 Folder Structure
     google-maps-ai-scraper/
      │
      ├── config.py                  # API URLs and constants
      ├── google_maps_ai_scraper.py  # Main script
      ├── requirements.txt           # All dependencies
      ├── .env.example               # Example environment variables
      ├── README.md                  # Project documentation
      └── output/                    # Folder where scraped text files are saved
🧠 Example Output
   software_companies_in_Hyderabad.txt
    Name: Infosys Limited
Address: Cyber Towers, Hitech City, Hyderabad
Phone: +91 40 3980 2000
Rating: 4.5
Website: https://www.infosys.com
Email: contact@infosys.com
-----------------------------

Name: Tata Consultancy Services (TCS)
Address: TCS Synergy Building, Hitech City, Hyderabad
Phone: +91 40 6601 1000
Rating: 4.4
Website: https://www.tcs.com
Email: info@tcs.com
-----------------------------

Name: Tech Mahindra Ltd
Address: Mindspace IT Park, Hitech City, Hyderabad
Phone: +91 40 6653 3000
Rating: 4.3
Website: https://www.techmahindra.com
Email: enquiry@techmahindra.com
-----------------------------

Name: Cognizant Technology Solutions
Address: Cognizant Park, Gachibowli, Hyderabad
Phone: +91 40 4434 0000
Rating: 4.2
Website: https://www.cognizant.com
Email: contact@cognizant.com
-----------------------------

Name: Capgemini India
Address: Capgemini Technology Services, Hitech City, Hyderabad
Phone: +91 40 4430 0000
Rating: 4.3
Website: https://www.capgemini.com
Email: info@capgemini.com
-----------------------------
👨‍💻 Author

SrinivasaGupta R K
Built with ❤️ for developers to easily integrate AI with Google Maps scraping.
    * Project description 
    * Features (bullet points)  
    * Technologies used  
    * Step-by-step installation instructions with package installation  
    * Usage instructions 
    * Folder structure
    * Example output 
 


       
         



        

  







