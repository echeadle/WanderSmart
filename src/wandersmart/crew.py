from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
import logging

# Uncomment the following line to use an example of a custom tool
# from wandersmart.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

# Create a logger for the crew.py module
logger = logging.getLogger(__name__)

# Configure the logger if it hasn't been configured already
if not logger.hasHandlers():
    logger.setLevel(logging.DEBUG)

    # Create a StreamHandler for console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Define a formatter for logs
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

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
  
def normalize_response(self, response):
    """
    Normalize the CrewAI response into a consistent JSON format.

    Args:
        response (CrewOutput): The raw response from CrewAI.

    Returns:
        dict: A standardized JSON structure.
    """
    try:
        # Convert response to a dictionary if it's a Pydantic object
        if hasattr(response, "dict"):
            response = response.dict()

        # Debug: Log the raw response
        logger.debug(f"Raw response: {response}")

        # Extract fields with validation
        destination = response.get("destination", "Destination not specified")
        travel_details = response.get("travel_details", {})

        # Validate travel_details structure
        flights = travel_details.get("flights", {}).get("service_providers", [])
        accommodations = travel_details.get("accommodations", {}).get("options", [])
        tours = travel_details.get("tours", {}).get("options", [])
        additional_resources = travel_details.get("additional_resources", [])

        # Debug: Log each extracted field
        logger.debug(f"Destination: {destination}")
        logger.debug(f"Flights: {flights}")
        logger.debug(f"Accommodations: {accommodations}")
        logger.debug(f"Tours: {tours}")
        logger.debug(f"Additional Resources: {additional_resources}")

        # Normalize travel details
        normalized_response = {
            "destination": destination,
            "flights": flights,
            "accommodations": accommodations,
            "tours": tours,
            "additional_resources": additional_resources
        }

        # Debug: Log normalized response
        logger.debug(f"Normalized response: {normalized_response}")
        return normalized_response

    except Exception as e:
        # Log the exception
        logger.error(f"Error normalizing CrewAI response: {e}", exc_info=True)
        return {}


my_crew = Wandersmart().crew()
  # Instantiate the Crew object
