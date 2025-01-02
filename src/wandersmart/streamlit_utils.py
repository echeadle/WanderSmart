import json
from dotenv import load_dotenv
from typing import Any
from crew import Wandersmart

load_dotenv()

import streamlit as st
from typing import Any

def generate_markdown(data):
    """
    Converts a list of vacation recommendations into a formatted Markdown string.

    Parameters:
        data (dict): A dictionary containing vacation recommendations.

    Returns:
        str: A Markdown-formatted string.
    """
    markdown_output = "# Vacation Recommendations\n\n"
    
    for idx, recommendation in enumerate(data.get("recommendations", []), start=1):
        title = recommendation.get("title", "No Title")
        description = recommendation.get("description", "No Description")
        cost = recommendation.get("cost", {})
        tour_price = cost.get("tour_price", "N/A")
        total_estimate = cost.get("total_estimate", "N/A")
        link = recommendation.get("link", "#")
        
        markdown_output += f"## {idx}. {title}\n"
        markdown_output += f"**Description:**  \n{description}\n\n"
        markdown_output += f"**Cost:**  \n- Tour Price: {tour_price}  \n- Total Estimate: {total_estimate}  \n\n"
        markdown_output += f"**[Learn More]({link})**\n\n"
        markdown_output += "---\n\n"

    return markdown_output

def enumerate_dictionary(dictionary):
    """
    Enumerates through a dictionary and prints the index, keys, and values.

    Args:
        dictionary (dict): The input dictionary to enumerate.
    """
    for index, (key, value) in enumerate(dictionary.items(), start=1):
        print(f"{index}. Key: {key}, Value: {value}\n")
        
        
def crew_output_to_json(crew_output: Any) -> dict:
    """
    Transform CrewOutput into a JSON-compatible dictionary while handling circular references.

    Args:
        crew_output (Any): The output object from crew.kickoff.

    Returns:
        dict: A JSON-serializable dictionary representation of the CrewOutput.
    """
    seen = set()

    def serialize(obj):
        """Helper function to serialize objects."""
        if id(obj) in seen:
            return "<circular reference>"
        seen.add(id(obj))
        
        if hasattr(obj, '__dict__'):
            # Handle objects with a __dict__ attribute
            return {key: serialize(value) for key, value in obj.__dict__.items()}
        elif isinstance(obj, list):
            # Handle lists
            return [serialize(item) for item in obj]
        elif isinstance(obj, dict):
            # Handle dictionaries
            return {key: serialize(value) for key, value in obj.items()}
        else:
            # Return primitive types directly
            return obj

    # Start serialization
    return serialize(crew_output)

def extract_recommendations(crew_output):
    """
    Extract recommendations from the 'raw' section of the CrewOutput.

    Args:
        crew_output (CrewOutput): The output object from crew.kickoff.

    Returns:
        list: A list of recommendation dictionaries.
    """
    try:
        # Access the 'raw' field of the CrewOutput object
        if not hasattr(crew_output, 'raw'):
            raise AttributeError("The CrewOutput object does not have a 'raw' attribute.")

        # Parse the 'raw' JSON string
        raw_data = json.loads(crew_output.raw)
        
        # Extract recommendations
        recommendations = raw_data.get('recommendations', [])
        return recommendations
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse 'raw' JSON: {e}")

def clean_json_string(input_string):
    """
    Removes ```json and trailing ``` from a JSON string.

    Args:
        input_string (str): The input string containing the JSON with markdown delimiters.

    Returns:
        str: The cleaned JSON string.
    """
    # Remove ```json from the start and ``` from the end
    cleaned_string = input_string.strip("`").lstrip("json").strip("`").strip()
    #cleaned_string = input_string.strip("`").replace("```json", "").strip("`").strip()
    return cleaned_string

def fetch_itinerary(user_inputs):
    """_
    Args:
        user_inputs (_type_): _description_
    Runs Crew
    """

    crew = Wandersmart().crew()
    crew_output = crew.kickoff(inputs=user_inputs)
    print(50 * "<><>")
    results_clean=clean_json_string(crew_output.raw)
    print(f"Raw Output: {results_clean}")
    print(f" The crew_output.raw type is {type(crew_output.raw)}")
    print(50 * "<><>")
    if crew_output.json_dict:
        print(f"JSON Output: {json.dumps(crew_output.json_dict, indent=2)}")
        print(50 * "<><>")
    if crew_output.pydantic:
        print(f"Pydantic Output: {crew_output.pydantic}")
        print(50 * "<><>")
    print(f"Tasks Output: {crew_output.tasks_output}")
    print(50 * "<><>")
    print(f"Token Usage: {crew_output.token_usage}")
    print(50 * "<><>")
    results = json.loads(results_clean)
    print(f"results_clean type is {type(results_clean)}")
    print(f"results type is {type(results)}")
    print( 20 * "$%#%")
    enumerate_dictionary(results)
    print( 20 * "$%#%")
    return results


def convert_to_python_dict(json_data):
    try:
        python_dict = json.loads(json_data)
        print("Conversion successful!")
        return python_dict
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        
def convert_to_markdown(json_data):
    """
    Convert a JSON object containing recommendations to a Markdown-formatted string.

    Args:
        json_data (dict): JSON object with recommendations.

    Returns:
        str: Markdown-formatted string.
    """
    markdown_output = "# Recommendations\n\n"

    # Iterate over recommendations
    for recommendation in json_data.get("recommendations", []):
        title = recommendation.get("title", "Untitled")
        description = recommendation.get("description", "No description available.")
        cost_details = recommendation.get("cost_details", {})

        markdown_output += f"## {title}\n\n"
        markdown_output += f"{description}\n\n"

        # Add cost details if available
        if "link" in cost_details:
            markdown_output += f"- **More Details**: [Visit Website]({cost_details['link']})\n"
        if "entry_fees" in cost_details:
            markdown_output += f"- **Entry Fees**: {cost_details['entry_fees']}\n"
        if "notes" in cost_details:
            markdown_output += f"- **Notes**: {cost_details['notes']}\n"
        if "additional_notes" in cost_details:
            markdown_output += f"- **Notes**: {cost_details['additional_notes']}\n"

        markdown_output += "\n---\n\n"  # Add a separator between recommendations

    return markdown_output

if __name__ == "__main__":
    # Assume `crew_output` is obtained from crew.kickoff(inputs=user_inputs)
    crew_output = None  # Replace with actual CrewOutput
    
    # Convert CrewOutput to JSON-compatible dictionary
    crew_output_dict = crew_output_to_json(crew_output)
    
