ch p# WanderSmart
Creating a Travel agency with CrewAI and Streamlit


# Comprehensive Project Plan for Streamlit & CrewAI Travel Agency Application

## Phase 1: Project Setup and Requirements Analysis

### 1. Define Objectives
- Develop a user-friendly travel agency application using Streamlit for the frontend.
- Use Crewai agents to handle backend tasks like information retrieval, processing, and interaction.
- Implement web scraping to gather travel information (e.g., flight prices, hotel details, tour packages, etc.).
- Ensure scalability and maintainability of the codebase.

### 2. Key Features
- **Search and Booking Interface:** Let users search for flights, hotels, and tour packages.
- **Recommendation System:** Use AI agents to suggest personalized travel options.
- **Web Scraping Automation:** Automate retrieval of travel deals from websites.
- **Chat Support:** Crewai agents to provide a chatbot-like interface for travel queries.

### 3. Tech Stack
- **Frontend:** Streamlit
- **Backend:** Crewai
- **Web Scraping:** `BeautifulSoup`, `Selenium`, or `Playwright`
- **Database:** SQLite (or cloud DB like Firebase if needed)
- **APIs:** Integrate APIs from travel services like Skyscanner, Expedia, etc.
- **Deployment:** Streamlit Cloud, AWS, or Azure.

### 4. Environment Setup
- Install necessary libraries: 
  - Streamlit (`streamlit`)
  - Crewai agents SDK
  - Web scraping tools (`requests`, `BeautifulSoup`, etc.)
  - Database tools (`sqlite3` or SQLAlchemy)

---

## Phase 2: Application Design

### 1. UI/UX Design for Streamlit
- **Homepage:**
  - Search bar for entering travel details (e.g., location, dates, preferences).
  - Sections for featured travel deals, recommendations, and a chatbot.
  
- **Search Results Page:**
  - Display search results dynamically (flights, hotels, tours).
  - Include filters (price range, duration, ratings).

- **Recommendations Page:**
  - Personalized recommendations from AI agents.
  
- **Booking Page:**
  - Form to collect user details for booking.

- **Chat Interface:**
  - Interactive chat panel powered by Crewai agents.

### 2. Backend Workflow with Crewai
- **AI Agent Tasks:**
  - Query processing: Handle natural language queries from users (e.g., "Find a 5-star hotel in Paris").
  - Information retrieval: Interact with web scraping scripts and APIs to fetch results.
  - Data processing: Filter, rank, and organize results for the frontend.

### 3. Web Scraping Design
- Identify target websites to scrape (e.g., airlines, hotel booking platforms).
- Design scraping modules with robust error handling and compliance (e.g., respect for robots.txt, avoiding excessive requests).

---

## Phase 3: Development

### 1. Frontend Development
- Use Streamlit to build an interactive interface:
  - Layout the pages with `st.sidebar`, `st.markdown`, `st.columns`, etc.
  - Add input widgets (`st.text_input`, `st.date_input`, `st.slider`) for travel search.
  - Dynamically display search results with `st.dataframe` or custom visualizations.

### 2. Backend Integration with Crewai
- Set up Crewai agents to:
  - Process user inputs and trigger specific workflows (e.g., querying flights, scraping data).
  - Manage conversation states for the chatbot interface.
  - Recommend options based on AI logic.

### 3. Web Scraping Modules
- Create modular scripts for scraping:
  - Use `BeautifulSoup` for static pages.
  - Use `Selenium` or `Playwright` for dynamic content.
  - Implement caching or rate-limiting to optimize performance.

### 4. Database and APIs
- Set up a database to store user preferences, search history, and scraped data.
- Integrate APIs for supplementary data (e.g., flight status, exchange rates).

---

## Phase 4: Testing

### 1. Unit Testing
- Test individual components (frontend forms, backend workflows, scraping scripts).
- Mock API calls and Crewai responses for testing.

### 2. Integration Testing
- Test communication between Streamlit and Crewai backend.
- Verify scraped data integration into the UI.

### 3. Load Testing
- Simulate high user traffic on both frontend and backend.
- Optimize for performance bottlenecks.

---

## Phase 5: Deployment

### 1. Streamlit Deployment
- Deploy the frontend on Streamlit Cloud or similar platforms.

### 2. Backend Hosting
- Host Crewai agent backend on a cloud platform (AWS Lambda, GCP).

### 3. Continuous Integration/Continuous Deployment (CI/CD)
- Use GitHub Actions or similar tools to automate testing and deployment pipelines.

---

## Phase 6: Future Enhancements

- **Real-Time Notifications:** Add email or SMS alerts for price changes or booking confirmations.
- **User Accounts:** Implement user login and profile management.
- **Advanced Analytics:** Use user data to refine recommendations.
- **Multilingual Support:** Expand chatbot capabilities to handle different languages.

---

# Key Differences Between Python GPT and CrewAI Assistant GPT

## 1. Python GPT
- Focuses on **Python code generation**, debugging, and optimization.
- Assists with modular coding for frontend (Streamlit), backend logic, and integrations (e.g., web scraping, APIs).
- Ideal for developers who want to manually manage code logic and workflows.
- Provides support for troubleshooting and improving code efficiency.

**When to Use:**
- If you want help building individual components step by step.
- For fine-tuning specific tasks like scraping, API integration, and frontend development.

---

## 2. CrewAI Assistant GPT
- Designed to work with **CrewAI**, a framework for AI agents collaborating on tasks.
- Helps structure workflows for agents that operate autonomously.
- Supports creating specialized agents for:
  - Web scraping and data retrieval.
  - Data processing and ranking.
  - User interaction and recommendations.
- Reduces the need for manual backend management by delegating tasks to agents.

**When to Use:**
- If you want a backend powered by autonomous AI agents.
- For complex workflows requiring multiple agents to interact (e.g., scraping, processing, recommending).

---

## 3. Hybrid Approach
- Combine both tools for the best results:
  - Use **Python GPT** to develop the Streamlit frontend and modular scripts.
  - Use **CrewAI** to structure backend workflows where agents collaborate autonomously.

**Recommendation:**
- Start with Python GPT for MVP development.
- Integrate CrewAI later for intelligent and scalable backend processes.

## Original Theme
[theme]
base = "dark"  # Ensures a consistent dark theme
primaryColor = "#1DB954"  # Optional: Accent color (e.g., green for buttons)
backgroundColor = "#121212"  # Optional: Background color for the app
secondaryBackgroundColor = "#191919"  # Optional: Background for widgets
textColor = "#FFFFFF"  # Optional: Text color
