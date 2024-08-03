from crewai import Task

class WriteBlogTask():
    def research_topic(self, agent, topic_info):
        return Task(
            description=f"""
                Research the given topic using reliable sources.

                - Topic: {topic_info['topic']}
                - Keywords: {topic_info['keywords']}
                - Target Audience: {topic_info['audience']}

                Important Info to consider:
                - Gather data, facts, and the latest information on the topic.
                - Ensure that the information is credible and up-to-date.
                - Include interesting facts, reference links, and recommendations for photos.
                - The content should be accessible and engaging for all age groups.
            """,
            agent=agent,
            expected_output="Research document containing facts, references, and photo recommendations.",
            async_execution=True,
        )

    def write_blog(self, agent, research_task, blog_template, output_file_path):
        return Task(
            description=f"""
                Write a blog post using the researched information.

                Writing Style:
                - Informal, engaging, and authentic, resembling popular blog writers.
                - Include real data values, engaging content, and high-quality recommendations.
                - The blog should feature interesting facts, references, and links to photos or additional resources.
                - Content should be easily understandable by all age groups.

                Blog Structure:
                - Title
                - Introduction
                - Main Content with engaging details, facts, and photos
                - Conclusion
                - References with links to sources

                The blog template is as follows:

                ```
                {blog_template}
                ```
            """,
            agent=agent,
            context=[research_task],
            expected_output="Completed blog post with engaging content and references.",
            output_file=output_file_path,
        )
