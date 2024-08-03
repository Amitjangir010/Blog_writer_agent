from crewai import Agent
from langchain_groq import ChatGroq
import os

class BlogWritingAgents():
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768"
        )

    def topic_research_agent(self):
        return Agent(
            role="Topic Researcher",
            goal="""
                Research topics thoroughly and provide comprehensive and up-to-date information.
                """,
            backstory="""
                As a Topic Researcher, your responsibility is to gather the most accurate and recent data on the assigned topics.
                """,
            verbose=True,
            llm=self.llm,
            max_iter=5,
        )

    def blog_writer_agent(self):
        return Agent(
            role="Blog Writer",
            goal="""
                Write engaging, informative, and authentic blog posts based on the researched information.
                The content should include interesting facts, high-quality recommendations, and reference links.
                """,
            backstory="""
                As a Blog Writer, you are a top-tier content creator renowned for crafting captivating and well-researched blog posts. 
                Your writing is celebrated for its authenticity, engagement, and inclusion of detailed insights and references.
                You are known worldwide for creating content that resonates with readers and provides genuine value.
                """,
            verbose=True,
            llm=self.llm,
            max_iter=5,
        )
