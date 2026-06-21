================================================================================
                    DOCKER CONTAINERIZATION AI AGENT
================================================================================

PROJECT OVERVIEW
================================================================================
This project provides an AI-powered Docker troubleshooting and management agent
with both CLI (Command-Line Interface) and GUI (Graphical User Interface) modes.
The agent uses Ollama and LangChain to provide expert-level Docker assistance.

It can help with:
  • Docker image management (pull, list, remove)
  • Container operations
  • Docker troubleshooting and diagnostics
  • Docker Compose guidance
  • Container security and optimization
  • Best practices for containerization


REQUIREMENTS
================================================================================
Before running the project, ensure you have:

1. Python 3.8 or higher
2. Docker installed and running
3. Ollama installed and running (Download from: https://ollama.ai)

Required Python packages (see requirements.txt):
  • ollama
  • langchain
  • langchain-core
  • langchain-ollama
  • langgraph
  • streamlit

Install dependencies:
  pip install -r requirements.txt


SETUP & INSTALLATION
================================================================================

1. Create/Activate Virtual Environment (Recommended):
   python -m venv gemma_env
   source gemma_env/bin/activate  # On macOS/Linux
   # or
   gemma_env\Scripts\activate      # On Windows

2. Install Dependencies:
   pip install -r requirements.txt

3. Start Ollama Service:
   Open a terminal and run:
   ollama serve

   This keeps Ollama running in the background, which is required for the agent
   to communicate with the language model.


CLI USAGE (COMMAND-LINE INTERFACE)
================================================================================

The CLI version provides an interactive command-line experience for Docker
assistance.

FILES:
  • docker_agent.py - Core agent implementation with Docker tools

RUNNING THE CLI:

Step 1: Ensure Ollama is running (in separate terminal):
        ollama serve

Step 2: Run the CLI agent:
        python docker_agent.py

Step 3: Interact with the agent:
        • The agent will greet you with: "Hello, How Can I Help You?"
        • Type your Docker-related questions or commands
        • Example questions:
          - "What Docker images do I have?"
          - "How do I create a production-ready Dockerfile?"
          - "Pull the Ubuntu 20.04 image"
          - "Show me Docker version and system info"
          - "What are best practices for Docker Compose?"

Step 4: Exit the CLI:
        Type: quit
        Press: Enter


CLI FEATURES:
  ✓ Interactive conversation with Docker expert AI
  ✓ Docker version and system information
  ✓ Image management (list, pull, remove)
  ✓ Container troubleshooting
  ✓ Production-ready solutions
  ✓ Best practices guidance
  ✓ Real-time Docker command execution


GUI USAGE (GRAPHICAL USER INTERFACE)
================================================================================

The GUI version provides a web-based interface using Streamlit for a more
user-friendly experience.

FILES:
  • streamlit_dockerAgent.py - Web-based GUI using Streamlit

RUNNING THE GUI:

Step 1: Ensure Ollama is running (in separate terminal):
        ollama serve

Step 2: Start the Streamlit application:
        streamlit run streamlit_dockerAgent.py

Step 3: Access the Web Interface:
        • A browser window will automatically open
        • If not, navigate to: http://localhost:8501
        • The GUI loads in your default web browser

Step 4: Using the Interface:
        • You'll see a clean, user-friendly interface
        • Type your Docker questions in the chat input box
        • The AI agent responds with helpful information
        • View Docker operations results in real-time
        • Example queries same as CLI mode

Step 5: Stop the GUI:
        Press: Ctrl+C in the terminal running Streamlit


GUI FEATURES:
  ✓ Web-based interface (accessible from browser)
  ✓ Clean, intuitive chat interface
  ✓ Real-time responses
  ✓ Docker operations execution
  ✓ Responsive design
  ✓ Same Docker expertise as CLI
  ✓ Easy to use for non-technical users


EXAMPLE INTERACTIONS
================================================================================

EXAMPLE 1: Get Docker Information
  User: "Show me Docker version and info"
  Agent: Executes docker version and docker info commands
  Response: Returns complete Docker environment details

EXAMPLE 2: Manage Images
  User: "List all Docker images"
  Agent: Executes docker images command
  Response: Shows all images with sizes and creation dates

EXAMPLE 3: Pull an Image
  User: "Pull the official Python 3.11 image"
  Agent: Executes docker pull python:3.11
  Response: Downloads and confirms successful pull

EXAMPLE 4: Troubleshooting
  User: "How do I remove dangling images?"
  Agent: Explains the concept and provides the command
  Response: Offers multiple approaches with pros/cons


TROUBLESHOOTING
================================================================================

Issue: "Connection refused" or "Cannot connect to Ollama"
Solution: 
  1. Verify Ollama is running: ollama serve
  2. Check if Ollama is properly installed
  3. Ensure default port (11434) is not blocked

Issue: "ModuleNotFoundError" for any package
Solution:
  1. Activate your virtual environment
  2. Run: pip install -r requirements.txt
  3. Verify installation: pip list

Issue: Streamlit won't open browser
Solution:
  1. The server is still running
  2. Manually open: http://localhost:8501
  3. Check firewall settings

Issue: Docker commands not executing
Solution:
  1. Ensure Docker daemon is running
  2. Check user permissions: sudo usermod -aG docker $USER
  3. Verify Docker installation: docker --version


FILE STRUCTURE
================================================================================

AI-Practice/
├── README.txt                    # This file
├── requirements.txt              # Python dependencies
├── docker_agent.py              # Core agent with Docker tools
├── streamlit_dockerAgent.py     # GUI Streamlit application
└── gemma_env/                   # Virtual environment directory
    ├── bin/
    ├── lib/
    └── etc/


DOCKER TOOLS AVAILABLE
================================================================================

The agent has access to these Docker tools:

1. docker_version() - Get Docker version information
2. docker_info() - Get Docker system information
3. pull_image(image_name) - Pull Docker image from registry
4. list_images() - List all local Docker images
5. list_unused_images() - Show dangling/unused images
6. remove_images(image_names) - Remove specific images
7. remove_unused_images() - Clean up all unused images

Plus many container management and troubleshooting capabilities.


TIPS & BEST PRACTICES
================================================================================

1. Always keep Ollama running in a separate terminal
2. Use specific image tags (not 'latest') in production
3. The agent provides multi-stage Dockerfile best practices
4. Leverage the agent for security recommendations
5. Use the CLI for automation scripts
6. Use the GUI for exploration and learning
7. Check agent responses for production-ready solutions


ADVANCED USAGE
================================================================================

Creating Custom Queries:
  The agent understands context and can handle complex questions:
  • "Create a Dockerfile for a Node.js Express app with best practices"
  • "Show me how to set up Docker Compose for a microservices architecture"
  • "Explain container networking and when to use bridge vs host"

Integration:
  • CLI mode can be integrated into scripts
  • GUI mode works on any device with a web browser
  • Both modes execute real Docker commands on your system


GETTING HELP
================================================================================

If you encounter issues:
1. Check the Troubleshooting section above
2. Verify all dependencies are installed
3. Ensure both Ollama and Docker are running
4. Check Python version compatibility (3.8+)
5. Review error messages from the terminal output


================================================================================
For more information about Docker: https://docs.docker.com
For more information about Ollama: https://ollama.ai
For LangChain documentation: https://python.langchain.com
================================================================================
