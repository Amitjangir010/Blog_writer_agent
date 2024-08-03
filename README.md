# Blog Writing Automation with CrewAI 🚀

Welcome to the **Blog Writing Automation** project! This project leverages the power of the CrewAI library and the LangChain Groq model to create high-quality, engaging blog posts based on user-provided topics, keywords, and audience specifications. Whether you're a seasoned blogger or just starting, our automated agents are here to help you craft content that's informative, authentic, and enjoyable to read.

## What's Inside? 📦

- **Agents**: Meet our Topic Researcher and Blog Writer agents, each with a unique backstory and skill set. They're designed to work together to gather information and create compelling blog content.
- **Tasks**: From researching a topic to writing a complete blog post, our tasks ensure that each piece of content is well-researched, engaging, and tailored to your target audience.
- **Customization**: Provide your own topics, keywords, and audience details through a CSV file, and watch as our agents turn them into polished blog posts.

## How It Works 💡

1. **Setup Your Environment**: 
   - Make sure to have your environment variables set up. You can use a `.env` file to store sensitive information like API keys.

2. **Define Your Topics**:
   - Create a CSV file (`data/topics.csv`) with the columns: `topic`, `keywords`, and `audience`. This file will guide our agents on what to research and write about.

3. **Run the Script**:
   - Simply execute `main.py` to kick off the process. The script will:
     - Load environment variables.
     - Create the agents and tasks.
     - Process the CSV file to generate research and writing tasks.
     - Output the final blog posts into the `output` directory.

## Getting Started 🛠️

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/blog-writing-automation.git
   cd blog-writing-automation
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then install the necessary packages:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up Your .env File**:
   Create a `.env` file in the root directory and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Prepare Your Data**:
   Create a `data/topics.csv` file with the topics you want to explore.

5. **Run the Script**:
   ```sh
   python main.py
   ```

## Example CSV Format 📄

Your `topics.csv` should look something like this:

| topic             | keywords                   | audience          |
|-------------------|----------------------------|-------------------|
| AI in Healthcare  | AI, healthcare, technology | Medical professionals, tech enthusiasts |
| Sustainable Living| sustainability, eco-friendly| Environmentally conscious individuals |

## Output 📂

The generated blog posts will be saved in the `output` directory. Each file will be named based on the topic, making it easy to find and review the content.

## Contributing 🤝

Got an idea to make this project even better? Feel free to fork the repository and submit a pull request. We welcome contributions from everyone!


# Sample Blog output

## How Rural Housewives in India Can Earn Money Using AI

### Introduction
In today's digital age, artificial intelligence (AI) has made significant strides in various industries, offering numerous opportunities for people to earn money. Even rural housewives in India can benefit from AI and earn a steady income. In this blog post, we will explore five AI-based earning opportunities for rural housewives in India.

### Main Content

1. **AI-based Content Writing:**
    With the rise of artificial intelligence, content writing has taken a new turn. AI-based content writing platforms like Articoolo, Quill, and Wordsmith use machine learning algorithms to generate articles, blogs, and reports. These platforms can help rural housewives to earn money by creating content on various topics. They don't require any prior experience in writing, just a basic understanding of the language and the subject.
    Interesting Fact: Did you know that AI can generate up to 2,000 words in just a few seconds? This opens up a world of possibilities for rural housewives who want to earn money through content writing.

2. **AI-powered Transcription Services:**
    AI-powered transcription services like Trint, Sonix, and Descript are revolutionizing the transcription industry. These platforms use speech recognition technology to convert audio and video files into text. Rural housewives can use these platforms to transcribe audio and video files and earn money. They don't require any special skills, just a good command of the language and accuracy in typing.
    Engaging Content: Imagine being able to transcribe an hour-long audio file while cooking lunch for your family. With AI-powered transcription services, this is now possible!

3. **AI-based Data Entry Jobs:**
    AI-based data entry jobs are becoming increasingly popular. Platforms like Amazon Mechanical Turk, Clickworker, and Appen use AI to automate data entry tasks. However, they still require human intervention to review and verify the data. Rural housewives can use these platforms to earn money by completing data entry tasks. They require basic computer skills and accuracy in typing.
    Recommendation: Consider practicing your typing skills to increase your earning potential in data entry jobs.

4. **AI-powered Online Tutoring:**
    AI-powered online tutoring platforms like Carnegie Learning, Content Technologies, and DreamBox Learning are changing the way education is delivered. These platforms use AI to personalize learning and provide customized instruction to students. Rural housewives can use these platforms to earn money by teaching students online. They require a good command of the subject and excellent communication skills.
    Insight: AI-powered online tutoring can be a rewarding experience, as you get to help students learn and grow while earning money.

5. **AI-powered Virtual Assistant Jobs:**
    AI-powered virtual assistant jobs are becoming increasingly popular. Platforms like Zirtual, Redbutler, and Time etc. use AI to automate administrative tasks. However, they still require human intervention to perform complex tasks. Rural housewives can use these platforms to earn money by providing virtual assistant services. They require good organizational skills, basic computer skills, and excellent communication skills.
    Real Data Value: Virtual assistant jobs pay an average of $15-$20 per hour, making them a lucrative option for rural housewives.

### Conclusion
AI has opened up numerous earning opportunities for rural housewives in India. By leveraging these AI-based platforms, rural housewives can earn a steady income and contribute to their family's financial stability. With the right skills and resources, rural housewives can turn these opportunities into a successful career.

### References
- [The Future of Content Creation: How AI is Changing the Game](https://www.forbes.com/sites/forbestechcouncil/2018/10/17/the-future-of-content-creation-how-ai-is-changing-the-game/?sh=6b80a2e17d6f)
- [The State of AI in 2021](https://www.cbinsights.com/research/report/ai-trends-2021/)
- [The Impact of Artificial Intelligence on Data Entry Jobs](https://analyticssteps.com/blogs/the-impact-of-artificial-intelligence-on-data-entry-jobs/)
- [AI in Education: 7 Ways Artificial Intelligence Can Transform Learning](https://elearningindustry.com/ai-in-education-7-ways-artificial-intelligence-can-transform-learning)
- [How AI Is Changing Customer Service](https://www.forbes.com/sites/forbestechcouncil/2018/04/12/how-ai-is-changing-customer-service/?sh=5a9344e17f6a)
```
Photo Recommendations:
1. A rural housewife working on a laptop, with a content writing platform open on the screen.
2. A close-up of a smartphone displaying an AI-powered transcription service.
3. A rural housewife typing on a computer, with a data entry platform open on the screen.
4. A rural housewife teaching a student online, with an AI-powered tutoring platform displayed on the screen.
5. A rural housewife answering emails on a computer, with a virtual assistant platform open on the screen.