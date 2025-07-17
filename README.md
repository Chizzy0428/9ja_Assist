
# 🇳🇬 9ja_Assist — Naija Data Intelligence Assistant

**9ja_Assist** is a Nigerian-focused, AI-powered web assistant that helps users ask questions about national data, trends, and statistics—covering topics like health, education, economy, demographics, and more. The assistant fetches real-time web data, summarizes answers using GPT-4, and generates intelligent insights such as trends and patterns with potential chart suggestions.



##  Key Features

- **Natural Language Question Answering**: Ask questions like “What is the maternal mortality rate in Nigeria?” or “How has Nigeria’s economy grown in the last 5 years?”
- **Web Search Integration**: Uses the Tavily API to perform up-to-date and relevant web searches.
- **GPT-4 Summarization**: Summarizes multiple web sources into a single, concise, human-readable response.
- **Insight Agent**: Extracts patterns and trends and suggests possible data visualizations or statistical interpretations.
- **Streamlit Interface**: Clean, user-friendly interface for interacting with the assistant.
- **Citations & Sources**: Displays clickable, titled links to the data sources used.



##  How It Works

```

┌────────────┐     ┌──────────────┐     ┌────────────────┐     ┌─────────────────┐
│ User Input │ →→  │ Search Agent │ →→  │ Summary Agent  │ →→  │ Insight Agent    │
└────────────┘     └──────────────┘     └────────────────┘     └─────────────────┘
↓                                                    ↓
Tavily API                                         Trends, Patterns, Charts

```

- **Search Agent**: Uses Tavily to fetch relevant results.
- **Summarize Agent**: Uses GPT-4 to generate concise answers from search data.
- **Insight Agent**: Detects trends, patterns, and chart suggestions for deeper understanding.



## Demo

Ask questions like:

- “What is Nigeria’s current inflation rate?”
- “Trends in Nigeria’s education budget over the last decade”
- “Maternal mortality rate in Nigeria and what’s driving it”
- “Unemployment trends in Nigeria between 2010 and 2024”



## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)
- **LLM**: OpenAI GPT-4 via `langchain`
- **Search API**: [Tavily](https://tavily.com/)
- **Agent Framework**: LangGraph (multi-agent orchestration)
- **Language**: Python 3.10+



## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Chizzy0428/9ja_Assist.git
   cd 9ja_Assist


2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your `TAVILY_API_KEY`**
   Create a `config.py` file:

   ```python
   TAVILY_API_KEY = "your_tavily_api_key"
   ```

5. **Run the app**

   ```bash
   streamlit run app.py
   ```



## Project Structure

```
9ja_Assist/
│
├── app.py                      # Streamlit app interface
├── config.py                   # Tavily API key config
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── graph/
    └── agent_graph.py          # Multi-agent LangGraph logic
```



## Future Improvements

* Add visualization rendering (charts inside Streamlit)
* Integrate Nigerian open data repositories (NBS, FMH, etc.)
* Add offline caching for frequently asked questions
* Support voice-to-text input for accessibility
* Add authentication and usage tracking for multiple users



## Acknowledgments

* [OpenAI](https://openai.com/)
* [LangGraph](https://docs.langchain.com/langgraph/)
* [Tavily](https://www.tavily.com/)
* [Streamlit](https://streamlit.io)


## Contact

**Chizzy Nwabuisi**
[GitHub: Chizzy0428](https://github.com/Chizzy0428)



## License

This project is open-source and available under the [MIT License](LICENSE).


