from langgraph.graph import StateGraph, END
from langchain.chat_models import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from config import TAVILY_API_KEY
from typing import TypedDict, List, Optional, Dict

# ✅ Define state structure
class AgentState(TypedDict):
    question: str
    search_text: Optional[str]
    source_links: List[Dict[str, str]]  # Each dict has {"title": ..., "url": ...}
    answer: Optional[str]
    insights: Optional[str]

# ✅ Tools
llm = ChatOpenAI(model="gpt-4", temperature=0)
search_tool = TavilySearchResults(k=3, tavily_api_key=TAVILY_API_KEY)

# ✅ Search Node: fetch content and links
def search_node(state: AgentState) -> AgentState:
    query = state["question"]
    results = search_tool.run(query)

    search_text = ""
    source_links = []

    for r in results:
        if isinstance(r, dict):
            content = r.get("content", "")
            url = r.get("url", "")
            title = r.get("title", url)
        else:
            content = str(r)
            url = ""
            title = url

        if content:
            search_text += f"- {content.strip()}\n"
        if url:
            source_links.append({"title": title.strip(), "url": url.strip()})

    return {
        "question": query,
        "search_text": search_text,
        "source_links": source_links,
        "answer": None,
        "insights": None
    }

# ✅ Summarize Node: generate clear and complete answer
def summarize_node(state: AgentState) -> AgentState:
    prompt = PromptTemplate.from_template(
        "You are a Nigerian data assistant. Use the web search results below to provide a comprehensive answer "
        "to the user's question.\n\n"
        "Question: {question}\n\n"
        "Search Results:\n{search_text}\n\n"
        "Answer:"
    )
    chain = prompt | llm
    answer = chain.invoke({
        "question": state["question"],
        "search_text": state["search_text"]
    })

    return {
        **state,
        "answer": answer
    }

# ✅ Insight Node: extract patterns, trends, suggest chart/summary
def insight_node(state: AgentState) -> AgentState:
    prompt = PromptTemplate.from_template(
        "Based on the information and answer below, identify any patterns, trends, or insights related to Nigeria. "
        "If relevant, suggest types of visualizations (e.g. line chart, bar chart, map). Use bullet points for clarity.\n\n"
        "Question: {question}\n\n"
        "Answer: {answer}\n\n"
        "Insights:"
    )
    chain = prompt | llm
    insights = chain.invoke({
        "question": state["question"],
        "answer": state["answer"]
    })

    return {
        **state,
        "insights": insights
    }

# ✅ Build LangGraph flow
def build_graph():
    builder = StateGraph(AgentState)
    builder.add_node("search", RunnableLambda(search_node))
    builder.add_node("summarize", RunnableLambda(summarize_node))
    builder.add_node("insight", RunnableLambda(insight_node))

    builder.set_entry_point("search")
    builder.add_edge("search", "summarize")
    builder.add_edge("summarize", "insight")
    builder.add_edge("insight", END)

    return builder.compile()
