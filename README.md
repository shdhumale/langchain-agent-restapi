# langchain-agent-restapi
This repo shows the use of langchain frame work using Google Gemini LLM to interact with external RESTAPI

Langchain Agent with REST API
This project demonstrates the creation of a Langchain agent integrated with the Google Gemini Large Language Model (LLM) to interact with external REST APIs. It provides a robust framework for building intelligent agents capable of performing actions by calling various API endpoints based on natural language prompts.

🌟 Features
Langchain Framework: Leverages the powerful Langchain library for agent orchestration, tool management, and prompt engineering.

Google Gemini LLM Integration: Utilizes the Google Gemini model for advanced natural language understanding and generation, enabling the agent to interpret user requests and formulate API calls.

REST API Interaction: Designed to seamlessly connect with and execute requests on external REST APIs.

Modular Design: The agent structure allows for easy extension and integration of new tools (API endpoints).

Environment Variable Configuration: Securely manages API keys and other sensitive information using .env files.

🚀 Getting Started
Follow these steps to set up and run the Langchain Agent locally.

Prerequisites
Python 3.8+

pip (Python package installer)

Installation
Clone the repository:

git clone https://github.com/shdhumale/langchain-agent-restapi.git
cd langchain-agent-restapi

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:

pip install -r requirements.txt

Configure environment variables:
Create a .env file in the root directory of the project and add your Google Gemini API key:

GOOGLE_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"

Replace "YOUR_GOOGLE_GEMINI_API_KEY" with your actual API key obtained from Google AI Studio or Google Cloud.

Usage
To run the agent and interact with it, execute the langchain_agent.py script. The specific interaction method (e.g., command-line input, web interface) will depend on how the langchain_agent.py is implemented. Assuming a basic command-line interface:

python langchain_agent.py

Once the script is running, you can provide natural language prompts to the agent, and it will attempt to use its defined tools (REST API endpoints) to fulfill your requests.

Example Prompts (depending on integrated APIs):

"Get the current weather in London."

"Book a flight from New York to San Francisco for tomorrow."

"Create a new task with the description 'Finish project report'."

🛠️ Technologies Used
Python: The core programming language.

Langchain: Framework for building LLM-powered applications.

Google Gemini: Large Language Model for natural language processing.

Dotenv: For managing environment variables.

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details (if a LICENSE file exists in the original repo, otherwise a placeholder).
