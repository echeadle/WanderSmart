from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff


# Uncomment the following line to use an example of a custom tool
# from wandersmart.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

@CrewBase
class Wandersmart():
	"""Wandersmart crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@before_kickoff # Optional hook to be executed before the crew starts
	def pull_data_example(self, inputs):
		# Example of pulling data from an external API, dynamically changing the inputs
		inputs['extra_data'] = "This is extra data"
		return inputs

	@after_kickoff # Optional hook to be executed after the crew has finished
	def log_results(self, output):
		# Example of logging results, dynamically changing the output
		print(f"Results: {output}")
		return output

	@agent
	def research_specialist(self) -> Agent:
		return Agent(
            config=self.agents_config['research_specialist'],
            tools=[SerperDevTool()],
            verbose=True
            
        )
  
	@task
	def search_task(self) -> Task:
		return Task(
            config=self.tasks_config['search_task'],
        )

	@crew
	def crew(self) -> Crew:
		"""Creates the Wandersmart crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

my_crew = Wandersmart().crew()
  # Instantiate the Crew object
