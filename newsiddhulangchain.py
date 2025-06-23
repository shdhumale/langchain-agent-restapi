import requests
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import json # Import json module
from dotenv import load_dotenv



# get_all_objects --- 1. Define your API calling function ---
def get_all_objects(object_id: str) -> str: # Removed objectvalue parameter as it's not used for getting all objects
    """Fetches all objects from the REST API."""
    base_url = "https://api.restful-api.dev/objects"
    params = object_id
    try:
        response = requests.get(base_url)
        print("response get_all_objects =============",response);
        # response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        # object_data = response.json()
        
        return f"{response}"

       
    except requests.exceptions.RequestException as e: # Catch specific request exceptions
        return f"Error fetching all objects: {e}"
    except ValueError: # Catch JSON decoding errors
        return f"Error parsing response for all objects."
    
# --- 2. Create a LangChain Tool from your function ---
get_all_objects_tool = Tool(
    name="get_all_objects",
    func=get_all_objects,
    description="Useful for getting a list of all objects from the REST API"
)    
# get_single_object --- 1. Define your API calling function ---
def get_single_object(object_id: str) -> str: # Renamed objectvalue to object_id for clarity
    base_url = "https://api.restful-api.dev/objects/" # Replace with your weather API endpoint
    params=object_id
    try:
        response = requests.get(base_url+params)
        print("response get_single_object=============",response);
        # response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        # object_data = response.json()
        
        return f"{response}"

       
    except requests.exceptions.RequestException as e: # Catch specific request exceptions
        return f"Error fetching object with ID {object_id}: {e}"
    except ValueError: # Catch JSON decoding errors
        return f"Error parsing response for object with ID {object_id}."

# --- 2. Create a LangChain Tool from your function ---
get_single_object_tool = Tool(
    name="get_single_object",
    func=get_single_object,
    description="Useful for getting the details of a single object from the REST API by providing its ID"
)


# add_object --- 1. Define your API calling function ---
def add_object(object_data_json_str: str) -> str: # Renamed objectvalue for clarity and specified it's a JSON string
    """Adds a new object to the REST API. Input should be a JSON string representing the object data (e.g., '{"name": "New Object", "data": {"year": 2023}}')."""
    base_url = "https://api.restful-api.dev/objects" # Note: no trailing slash for POST to collection
    
    try:
        # Parse the JSON string into a Python dictionary
        object_data = json.loads(object_data_json_str)
        
        response = requests.post(base_url, json=object_data) # Pass data as json argument
        #fetch the id values from the content of response
        
        response_json = response.json()
        print("response add_object=============", response_json['id']) # Print the JSON content
        # response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        # object_data = response.json()
        
        return f"{response_json['id']}"

       
    except json.JSONDecodeError as e: # Catch JSON decoding errors
        return f"Error: Invalid JSON string provided: {e}"
    except requests.exceptions.RequestException as e: # Catch specific request exceptions
        return f"Error adding object with data '{object_data_json_str}': {e}"
    except ValueError: # Catch other parsing errors
        return f"Error parsing response for adding object with data '{object_data_json_str}'."

# --- 2. Create a LangChain Tool from your function ---
add_object_tool = Tool(
    name="add_object",
    func=add_object,
    description="Useful for adding a new object to the REST API by providing its name and data as a JSON string (e.g., '{\"name\": \"New Object\", \"data\": {\"year\": 2023}}')"
)

#     def update_object(self, object_id, data):
#     return requests.put(f"{self.base_url}/objects/{object_id}", json=data).json()

# update_object --- 1. Define your API calling function ---
def update_object(update_details_json_str: str) -> str:
    """Updates an existing object in the REST API. Input should be a JSON string containing the 'id' of the object to update and the 'data' to update with. Example: '{"id": "ff8081818f3d84a4018f3f8b62ea0074", "data": {"name": "Updated Name"}}'"""
    base_url = "https://api.restful-api.dev/objects/" # Replace with your weather API endpoint
    
    try:
        # Parse the JSON string into a Python dictionary
        update_details = json.loads(update_details_json_str)
        object_id = update_details.get("id")
        data = update_details.get("data")

        if not object_id or not data:
            return "Error: The input JSON must contain both 'id' and 'data' keys."
        
        # response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        # object_data = response.json()
        response = requests.put(base_url + object_id, json=data)
        print("response update_object=============", response)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        
        return f"{response}"
       
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON string provided for update: {e}"
    except requests.exceptions.RequestException as e: # Catch specific request exceptions
        return f"Error fetching object with ID {object_id}: {e}"
    except ValueError: # Catch JSON decoding errors
        return f"Error parsing response for object with ID {object_id}."
        return f"Error updating object: {e}"
# --- 2. Create a LangChain Tool from your function ---
update_object_tool = Tool(
    name="update_object",
    func=update_object, # The input must be a JSON string containing the 'id' of the object and the 'data' for the update. Example: '{"id": "some-id", "data": {"name": "New Name"}}'
    description="Useful for updating the details of a single object. The input must be a JSON string containing the 'id' of the object and the 'data' for the update. Example: '{\"id\": \"some-id\", \"data\": {\"name\": \"New Name\"}}'"
)


# def delete_object(self, object_id):
# return requests.delete(f"{self.base_url}/objects/{object_id}").json()
# delete_object --- 1. Define your API calling function ---
def delete_object(object_id: str) -> str: # Renamed objectvalue for clarity and specified it's a JSON string
    """Delete the object to the REST API. Input should be a JSON string representing the ID data (e.g., '{"id": "1234"}')."""
    base_url = "https://api.restful-api.dev/objects/" # Note: no trailing slash for POST to collection
    params=object_id
    try:
        response = requests.delete(base_url+params) # Pass data as json argument
        #fetch the id values from the content of response
        print("response delete_object=============", response) # Print the JSON content
        # response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        # object_data = response.json()
        
        return f"{response}"

       
    except json.JSONDecodeError as e: # Catch JSON decoding errors
        return f"Error: Invalid JSON string provided: {e}"
    except requests.exceptions.RequestException as e: # Catch specific request exceptions
        return f"Error deleting object with data '{object_id}': {e}"
    except ValueError: # Catch other parsing errors
        return f"Error parsing response for deleting object with data '{object_id}'."

# --- 2. Create a LangChain Tool from your function ---
delete_object_tool = Tool(
    name="delete_object",
    func=delete_object,
    description="Useful for deleting a object to the REST API by providing its ID"
)
    
# --- 3. (Optional) Integrate with an Agent ---
# This shows how an agent can decide to use your tool

# Set up your LLM
# llm = ChatOpenAI(model="gpt-4", temperature=0) # Make sure to set your OpenAI API key
from dotenv import load_dotenv

# Load environment variables from .env file if available
load_dotenv()

# Get your Google API key from environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the language model
llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-05-20",
        google_api_key=google_api_key,
        temperature=0.7,
        max_output_tokens=512,  # Corrected parameter name from max_tokens
    )

# Define the tools available to the agent
# For a complete solution, all tools should be available.
# The original code only had add_object_tool enabled. Let's enable all for demonstration.
tools = [get_all_objects_tool, get_single_object_tool, add_object_tool,update_object_tool,delete_object_tool]

# Create an agent prompt (standard ReAct prompt or similar)
prompt = PromptTemplate.from_template("""
You are an AI assistant that can fetch the api call response in json.
You have access to the following tools:
{tools}
Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
Begin!
Question: {input}
Thought:{agent_scratchpad}
""")

# Create the ReAct agent
agent = create_react_agent(llm, tools, prompt)

# Create an AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# --- 4. Make a call through the agent ---
if __name__ == "__main__":
    # Example usage for add_object
    print("--- Adding a new object ---")
    # The input to the agent should be a natural language query that the agent can interpret
    # to call the 'add_object' tool with the correct JSON string.
    add_object_input = '{"name": "MyTestObject", "data": {"year": 2024, "price": 99.99, "color": "blue"}}'
    result_add = agent_executor.invoke({"input": f"Add a new object with data: {add_object_input}"})
    # The add_object tool directly returns the ID as a string, so no splitting is needed.
    created_id = result_add['output']
    print("Result of adding object (ID):", created_id)

    # Example usage for get_single_objects
    print("\n--- Getting single object ---")
    # Prompt the agent to use the 'get_single_object' tool with the extracted ID.
    result_single = agent_executor.invoke({"input": f"Get the details of object with ID: {created_id}"})
    print("Result of getting single objects:", result_single)    
    
     # Example usage for update_objects
    print("\n--- update single object ---")
    # Prompt the agent to use the 'update_object' tool with the extracted ID and update the data.     
    update_object_input = '{"name": "MyTestObject updated", "data": {"year": 2024 , "price": 99.99, "color": "blue updated"}}'
    update_prompt = f"Update the object with ID: '{created_id}' with the following data: {update_object_input}"
    update_result_single = agent_executor.invoke({"input": update_prompt})
    print("Result of getting single objects:", update_result_single)
    
    
    # Example usage for delete_objects
    print("\n--- delete single object ---")
    # Prompt the agent to use the 'get_single_object' tool with the extracted ID.
    result_single = agent_executor.invoke({"input": f"delete the details of object with ID: {created_id}"})
    print("Result of after deleting objects:", result_single)  
    
    
    # Example usage for get_all_objects
    print("\n--- Getting all objects ---")
    result_all = agent_executor.invoke({"input": "Get all objects"})
    print("Result of getting all objects:", result_all)
