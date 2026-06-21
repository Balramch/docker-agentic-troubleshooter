"""
Docker Troubleshooter Agent

Requirements:
pip install langchain langchain-core langchain-ollama

Start Ollama first:
ollama serve

Run:
python docker_troubleshooter.py
"""
import subprocess
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent as create_react_agent
# ---------------------------------------------------------
# Docker Tools
# ---------------------------------------------------------
# ---------------------------------------------------------
# Docker Version and Info
# --------------------------------------------------------
## Docker Version 
@tool
def docker_version() -> str:
    """Show Docker version."""
    result = subprocess.run(
        ["docker", "version"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Docker info 
@tool
def docker_info() -> str:
    """Show Docker info."""
    result = subprocess.run(
        ["docker", "info"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr 


# ---------------------------------------------------------
# Docker image management
# --------------------------------------------------------
### docker pull image
@tool
def pull_image(image_name: str) -> str:
    """Pull a Docker image."""
    result = subprocess.run(
        ["docker", "pull", image_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Docker image listing
@tool
def list_images() -> str:
    """List Docker images."""
    result = subprocess.run(
        ["docker", "images"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## List unused images
@tool
def list_unused_images() -> str:
    """Show unused Docker images."""
    result = subprocess.run(
        ["docker", "images", "-f", "dangling=true"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Remove images
@tool
def remove_images(image_names: list[str]) -> str:
    """Remove Docker images."""
    result = subprocess.run(
        ["docker", "rmi", "-f"] + image_names,
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Remove unused images
@tool
def remove_unused_images() -> str:
    """Remove unused Docker images."""
    result = subprocess.run(
        ["docker", "image", "prune", "-af"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

# ---------------------------------------------------------
# Docker Container management
# --------------------------------------------------------

## Run Containers in detach mode
@tool
def run_container_detach(image_name: str, container_name: str, ports: list[str], volumes: list[str]) -> str:
    """Run a Docker container."""
    cmd = ["docker", "run", "-d", "--name", container_name]
    for port in ports:
        cmd.extend(["-p", port])
    for volume in volumes:
        cmd.extend(["-v", volume])
    cmd.append(image_name)
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## List Running Containers
@tool
def list_running_containers() -> str:
    """List running Docker containers."""
    result = subprocess.run(
        ["docker", "ps"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## List all Containers
@tool
def list_all_containers() -> str:
    """List all Docker containers."""
    result = subprocess.run(
        ["docker", "ps", "-a"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Restart Container
@tool
def restart_container(container_name: str) -> str:
    """Restart a Docker container."""
    result = subprocess.run(
        ["docker", "restart", container_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Stop Container
@tool
def stop_container(container_name: str) -> str:
    """Stop a Docker container."""
    result = subprocess.run(
        ["docker", "stop", container_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

### Start Container
@tool
def start_container(container_name: str) -> str:
    """Start a Docker container."""
    result = subprocess.run(
        ["docker", "start", container_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

### Remove container
@tool
def remove_container(container_name: str) -> str:
    """Remove a Docker container."""
    result = subprocess.run(
        ["docker", "rm", "-f", container_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr


# ---------------------------------------------------------
# Docker Inspection and Logs
# --------------------------------------------------------

## check logs of the container
@tool
def logs_container(container_name: str) -> str:
    """Get logs for a container."""
    result = subprocess.run(
        ["docker", "logs", "--tail", "100", container_name],
        capture_output=True,
        text=True,
    )
    return result.stdout + result.stderr

## Inspect Container
@tool
def inspect_container(container_name: str) -> str:
    """Inspect a Docker container."""
    result = subprocess.run(
        ["docker", "inspect", container_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Docker stats
@tool
def docker_stats() -> str:
    """Show Docker container stats."""
    result = subprocess.run(
        ["docker", "stats", "--no-stream"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Docker top
@tool
def docker_top(container_name: str) -> str:
    """Show processes in a container."""
    result = subprocess.run(
        ["docker", "top", container_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

# ---------------------------------------------------------
# Docker Network management
# --------------------------------------------------------
@tool
def list_networks() -> str:
    """List Docker networks."""
    result = subprocess.run(
        ["docker", "network", "ls"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

@tool
def create_network(network_name: str) -> str:
    """Create a Docker network."""
    result = subprocess.run(
        ["docker", "network", "create", network_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

@tool
def inspect_network(network_name: str) -> str:
    """Inspect a Docker network."""
    result = subprocess.run(
        ["docker", "network", "inspect", network_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

@tool
def remove_network(network_name: str) -> str:
    """Remove a Docker network."""
    result = subprocess.run(
        ["docker", "network", "rm", network_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

@tool
def prune_network(network_name: str) -> str:
    """Prune unused Docker networks."""
    result = subprocess.run(
        ["docker", "network", "prune"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr
# ---------------------------------------------------------
# Docker Volume management
# --------------------------------------------------------
## Docker volume listing
@tool
def list_volumes() -> str:
    """List Docker volumes."""
    result = subprocess.run(
        ["docker", "volume", "ls"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Docker Create Volume
@tool
def create_volume(volume_name: str) -> str:
    """Create a Docker volume."""
    result = subprocess.run(
        ["docker", "volume", "create", volume_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Docker Volume Inspect
@tool
def inspect_volume(volume_name: str) -> str:
    """Inspect a Docker volume."""
    result = subprocess.run(
        ["docker", "volume", "inspect", volume_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Remove Docker Volume
@tool
def remove_volume(volume_name: str) -> str:
    """Remove a Docker volume."""
    result = subprocess.run(
        ["docker", "volume", "rm", volume_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

@tool
def prune_volumes() -> str:
    """Prune unused Docker volumes."""
    result = subprocess.run(
        ["docker", "volume", "prune"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

# ---------------------------------------------------------
# Docker System cleanup
# ---------------------------------------------------------
## show disk usage
@tool
def show_disk_usage() -> str:
    """Show Docker disk usage."""
    result = subprocess.run(
        ["docker", "system", "df"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Docker system prune
@tool
def docker_prune() -> str:
    """Prune Docker system."""
    result = subprocess.run(
        ["docker", "system", "prune"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Docker image history
@tool
def image_history(image_name: str) -> str:
    """Show Docker image history."""
    result = subprocess.run(
        ["docker", "history", image_name],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

# ---------------------------------------------------------
# Docker Monitoring
# ---------------------------------------------------------

## Docker events since 1 hr.
@tool
def docker_events() -> str:
    """Show Docker events."""
    result = subprocess.run(
        ["docker", "events", "--since", "1h"],
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr

## Check image vulnerabilities
# @tool
# def check_image_vulnerabilities(image_name: str) -> str:
#     """Check for vulnerabilities in a Docker image."""
#     try:
#         # Try Trivy first
#         result = subprocess.run(
#             ["trivy", "image", image_name],
#             capture_output=True,
#             text=True,
#             timeout=120  # 2 minute timeout
#         )
#         return result.stdout or result.stderr
#     except subprocess.TimeoutExpired:
#         return "Scan timed out. Please try again."
#     except FileNotFoundError:
#         return "Trivy or Docker Scan not found. Please install one of them."

# ---------------------------------------------------------
# LLM
# ---------------------------------------------------------

llm = ChatOllama(
    model="gemma4",  # change if needed
    temperature=0.7,
)

tools = [
    docker_version,
    docker_info,
    pull_image,
    list_images,
    list_unused_images,
    remove_images,
    remove_unused_images,
    run_container_detach,
    list_running_containers,
    list_all_containers,
    restart_container,
    stop_container,
    start_container,
    remove_container,
    logs_container,
    inspect_container,
    docker_stats,
    docker_top,
    list_networks,
    create_network,
    inspect_network,
    remove_network,
    list_volumes,
    create_volume,
    inspect_volume,
    remove_volume,
    show_disk_usage,
    docker_prune,
    image_history,
    prune_network,
    prune_volumes,
    docker_events,
    # check_image_vulnerabilities,





]

# ---------------------------------------------------------
# ReAct Prompt
# ---------------------------------------------------------

SYSTEM_PROMPT = """
You are an autonomous DevOps agent specialized in Docker debugging, container orchestration, and production incident resolution.

Your primary goal is to diagnose and resolve Docker-related issues using tools, not assumptions.

## Core Operating Principles
- NEVER guess the state of the system.
- ALWAYS use available tools before drawing conclusions.
- Treat every issue as an incident requiring investigation and verification.
- Work iteratively: observe → analyze → act → verify.

## Standard Investigation Loop
Follow this loop until the issue is resolved:

1. DISCOVER
   - List all containers, images, networks, and volumes if relevant.
   - Identify the scope of the issue.

2. INSPECT
   - Inspect suspicious containers (config, environment, health, restart policy).
   - Gather detailed runtime metadata.

3. OBSERVE
   - Read logs thoroughly (include recent and historical logs if needed).
   - Identify errors, crash loops, or misconfigurations.

4. DIAGNOSE
   - Correlate logs + container state + configuration.
   - Identify the most likely root cause (be explicit about evidence).

5. ACT
   - Suggest or execute the safest corrective action (restart, rebuild, fix config, adjust compose, etc.).
   - Prefer minimal, reversible changes.

6. VERIFY
   - Re-check container status and logs after changes.
   - Confirm whether the issue is resolved.

## Tool Usage Rules
- You MUST use tools whenever available (do not simulate outputs).
- If tool output is insufficient, request additional data instead of guessing.
- Prefer multiple small tool calls over one large assumption.

## Decision Style
- Be precise, technical, and evidence-driven.
- Clearly separate:
  - Observations
  - Inference
  - Action
  - Result

## Failure Handling
- If the issue cannot be resolved, clearly state:
  - What was checked
  - What was found
  - What is still unknown
  - Next recommended debugging step

You are operating in a production environment. Reliability and correctness matter more than speed.
"""

##prompt = PromptTemplate.from_template(template)
# ---------------------------------------------------------
# Agent
# ---------------------------------------------------------

agent = create_react_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)

# ---------------------------------------------------------
# Main Loop
# ---------------------------------------------------------

print("\n🐳 Docker Troubleshooter Agent")
print("-" * 40)

while True:
    print("Ask me anything about Docker troubleshooting!")
    print("Type 'quit' to exit.\n")
    question = input("\nQuestion > ").strip()

    if question.lower() in ["quit", "exit", "q"]:
        break
    try:
        result = agent.invoke({"messages": [("user", question)]})
        print(result["messages"][-1].content)

    except Exception as e:
        print(f"\nError: {e}")
