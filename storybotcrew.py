from crewai import Crew, LLM
from storybot import StoryBot

from dotenv import load_dotenv
load_dotenv()

class StoryBotCrew():

    def __init__(self, topic: str) -> None:
        self.topic = topic

    def run_crew(self) -> str:
        sb = StoryBot()

        crew = Crew(
            agents = [sb.research_agent, sb.simplifier_agent, sb.storywriter_agent, sb.educator_agent],
            tasks = [sb.research_task, sb.simplify_task, sb.story_task, sb.review_task],
            verbose = False
        )

        result = crew.kickoff(inputs={"topic": self.topic})

        return result

if __name__ == "__main__":
    topic = input("Enter a topic you would like a story about: ")
    sbc = StoryBotCrew(topic)
    print(sbc.run_crew())