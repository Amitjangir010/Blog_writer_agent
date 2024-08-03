import os
import time
import csv
from dotenv import load_dotenv
from crewai import Crew
from langchain_groq import ChatGroq
from agents import BlogWritingAgents
from tasks import WriteBlogTask
from logger import logger  # Importing the custom logger

load_dotenv()

# Blog content template
blog_template = """
## [Title]

### Introduction
[Introduction content]

### Main Content
[Main content]

### Conclusion
[Conclusion content]

### References
[References]
"""

# 1. Create agents
agents = BlogWritingAgents()
topic_researcher = agents.topic_research_agent()
blog_writer = agents.blog_writer_agent()

# 2. Create tasks
tasks = WriteBlogTask()

research_tasks = []
write_blog_tasks = []

# Path to the CSV file containing topic information
csv_file_path = 'data/topics.csv'

try:
    # Open the CSV file
    with open(csv_file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            topic_info = {
                'topic': row['topic'],
                'keywords': row['keywords'],
                'audience': row['audience']
            }

            # Create a research task for each topic
            research_task = tasks.research_topic(
                agent=topic_researcher,
                topic_info=topic_info
            )

            cleaned_topic = "".join(c if c.isalnum() else "_" for c in topic_info['topic'])

            # Create a write_blog task for each topic with a placeholder path
            write_blog_task = tasks.write_blog(
                agent=blog_writer,
                research_task=research_task,
                blog_template=blog_template,
                output_file_path=os.path.join("output", f"{cleaned_topic}_blog.txt")
            )

            # Add the task to the crew
            research_tasks.append(research_task)
            write_blog_tasks.append(write_blog_task)

except FileNotFoundError:
    logger.error(f"CSV file not found: {csv_file_path}")
    exit(1)
except Exception as e:
    logger.error(f"An error occurred while reading the CSV file: {e}")
    exit(1)

# Ensure output directory exists
output_directory = 'output'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Setup Crew
crew = Crew(
    agents=[topic_researcher, blog_writer],
    tasks=[*research_tasks, *write_blog_tasks],
    max_rpm=29
)

# Kick off the crew
try:
    start_time = time.time()
    results = crew.kickoff()
    end_time = time.time()
    elapsed_time = end_time - start_time

    logger.info(f"Crew kickoff took {elapsed_time:.2f} seconds.")
    logger.info(f"Crew usage: {crew.usage_metrics}")
except Exception as e:
    logger.error(f"An error occurred during crew kickoff: {e}")
    exit(1)
