import streamlit as st
from graph.agent_graph import build_graph
from langchain_core.messages import AIMessage

# Streamlit page config
st.set_page_config(page_title="Naija Data Intelligence Assistant", page_icon="🇳🇬")
st.title("🇳🇬 Naija Data Intelligence Assistant")

# Build the LangGraph workflow
graph = build_graph()

# Input field
question = st.text_input("Ask your question about Nigeria (e.g. economy, health, education)...")

# On button click
if st.button("Ask"):
    if question:
        with st.spinner("🔍 Searching the web and analyzing..."):
            try:
                result = graph.invoke({"question": question})

                # Handle the answer (AIMessage or str)
                answer = result.get("answer")
                if isinstance(answer, AIMessage):
                    answer = answer.content
                elif hasattr(answer, "content"):
                    answer = answer.content

                # Display the main answer
                st.markdown("### 📄 Answer:")
                st.markdown(answer or "*No answer generated.*")

                # Display additional insights or patterns
                insights = result.get("insights")
                if insights:
                    if isinstance(insights, AIMessage):
                        insights = insights.content
                    elif hasattr(insights, "content"):
                        insights = insights.content

                    st.markdown("### 📊 Insights / Trends:")
                    st.markdown(insights)
                else:
                    st.info("No additional insights were generated.")

                # Display source links with titles
                source_links = result.get("source_links", [])
                if source_links:
                    st.markdown("### 🔗 Sources:")
                    for idx, link in enumerate(source_links, 1):
                        title = link.get("title", f"Source {idx}")
                        url = link.get("url")
                        if url:
                            st.markdown(f"- [{title}]({url})")
                else:
                    st.info("No sources were found for this query.")

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a question.")
