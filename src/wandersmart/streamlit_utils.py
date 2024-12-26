import logging
from crew import my_crew
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    filename='wandersmart.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_itinerary(inputs):
    """
    Fetch travel itinerary using CrewAI.
    Args:
        inputs (dict): User-provided inputs for the trip.
    Returns:
        dict: Response from CrewAI or error details.
    """
    print(inputs)
    # logging.info(f"Fetching itinerary with inputs: {inputs}")
    try:
        response =  my_crew.kickoff(inputs=inputs)
        # logging.info(f"Received response: {response}")
        print(response)
        return response
    except Exception as e:
        # logging.error(f"Error fetching itinerary: {e}", exc_info=True)
        return {"error": str(e)}
if __name__ == '__main__':
    itenerary=fetch_itinerary({"destination":"Paris"})
    print(itenerary)