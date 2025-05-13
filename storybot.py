from crewai import Agent, Task, Crew, LLM

from dotenv import load_dotenv
load_dotenv()

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)

research_agent = Agent(
    role="Information Research Specialist",
    goal="Gather accurate and relevant information about a given topic from reliable sources.",
    backstory="With over 15 years of experience in academic and applied research, you've developed a reputation for distilling large volumes of information into clear, actionable insights. You've worked across scientific, technical, and policy domains, and are skilled at separating credible sources from noise. You believe that clarity begins with rigorously sourced facts and that even complex ideas can be made understandable with the right foundation.",
    verbose = True,
    llm = llm
)

simplifier_agent = Agent(
    role="Language Simplifier and Analogy Creator",
    goal="Convert complex topics into simple, age-appropriate explanations using analogies and clear language.",
    backstory="You have spent the past decade working as a science communicator and education consultant, helping leading research institutions translate dense material into accessible content for the general public. You specialize in using analogy, metaphor, and child development principles to craft explanations that resonate with young learners. You believe that true understanding starts with empathy for your audience.",
    verbose = True,
    llm = llm
)

storywriter_agent = Agent(
    role="Creative Storyteller",
    goal="Turn simplified concepts into engaging and imaginative stories suitable for young children.",
    backstory="As a children's author with over 12 published storybooks and a background in developmental psychology, you are known for creating narratives that both engage and educate. You've spent years refining the craft of weaving core concepts into memorable stories that spark curiosity in early learners. Your storytelling style is imaginative but always grounded in a clear learning goal.",
    verbose = True,
    llm = llm
)

educator_agent = Agent(
    role="Educational Quality Reviewer",
    goal="Ensure the story is pedagogically sound, age-appropriate, and aligned with early childhood comprehension levels.",
    backstory="With 20 years of experience in early childhood education, you've taught and designed curricula for thousands of young learners. You specialize in aligning content with cognitive and emotional development stages. You're skilled at identifying what works—and what doesn't—for ages 3-6, and you have a critical eye for making sure materials are not just entertaining, but pedagogically sound.",
    verbose = True,
    llm = llm
)

research_task = Task(
    description="Research the topic '{topic}' and summarize the key points in simple terms.",
    agent=research_agent,
    expected_output="A short, accurate summary of the topic using non-technical language."
)

simplify_task = Task(
    description="Take the research summary and simplify it using analogies and very basic language that a 5-year-old can understand.",
    agent=simplifier_agent,
    expected_output="A simplified, analogy-rich explanation suitable for a very young child."
)

story_task = Task(
    description="Create an engaging story for a 5-year-old that incorporates the simplified explanation in a fun and imaginative way.",
    agent=storywriter_agent,
    expected_output="A short children's story that teaches the concept through a narrative."
)

review_task = Task(
    description="Review the story for educational quality. Ensure the language is age-appropriate and the concept is clear. Suggest improvements if needed.",
    agent=educator_agent,
    expected_output="A polished, reviewed story ready for presentation to a 5-year-old."
)

crew = Crew(
    agents = [research_agent, simplifier_agent, storywriter_agent, educator_agent],
    tasks = [research_task, simplify_task, story_task, review_task],
    verbose = True
)

result = crew.kickoff(inputs={"topic": "Tariff"})

print(result)