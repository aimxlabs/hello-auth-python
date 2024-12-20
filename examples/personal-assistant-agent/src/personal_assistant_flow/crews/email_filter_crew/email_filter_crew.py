from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from hello_message.tools.hello_create_draft import CreateDraftTool


@CrewBase
class EmailFilterCrew:
    """Email Filter Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    llm = None #ChatOpenAI(model="gpt-4o")

    @agent
    def email_response_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["email_response_writer"],
            llm=self.llm,
            verbose=True,
            tools=[
                CreateDraftTool.create_draft,
            ],
        )

    @task
    def draft_responses_task(self) -> Task:
        return Task(config=self.tasks_config["draft_responses"])

    @crew
    def crew(self) -> Crew:
        """Creates the Email Filter Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )