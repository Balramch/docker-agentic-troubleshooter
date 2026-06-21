# docker_streamlit.py
import subprocess
import json
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
#from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent as create_react_agent
from langchain_core.messages import SystemMessage

# ---------------------------------------------------------
# Docker Tools
# ---------------------------------------------------------

@tool
def docker_version() -> str:
    """Show Docker version."""
    result = subprocess.run(["docker", "version"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def docker_info() -> str:
    """Show Docker info."""
    result = subprocess.run(["docker", "info"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def pull_image(image_name: str) -> str:
    """Pull a Docker image."""
    result = subprocess.run(["docker", "pull", image_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def list_images() -> str:
    """List Docker images."""
    result = subprocess.run(["docker", "images"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def list_unused_images() -> str:
    """Show unused Docker images (dangling)."""
    result = subprocess.run(["docker", "images", "-f", "dangling=true"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def remove_images(image_names: list[str]) -> str:
    """Remove Docker images."""
    result = subprocess.run(["docker", "rmi", "-f"] + image_names, capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def remove_unused_images() -> str:
    """Remove unused Docker images."""
    result = subprocess.run(["docker", "image", "prune", "-af"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def run_container_detach(image_name: str, container_name: str, ports: list[str], volumes: list[str]) -> str:
    """Run a Docker container in detached mode."""
    cmd = ["docker", "run", "-d", "--name", container_name]
    for port in ports:
        cmd.extend(["-p", port])
    for volume in volumes:
        cmd.extend(["-v", volume])
    cmd.append(image_name)
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def list_running_containers() -> str:
    """List running Docker containers."""
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def list_all_containers() -> str:
    """List all Docker containers."""
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def restart_container(container_name: str) -> str:
    """Restart a Docker container."""
    result = subprocess.run(["docker", "restart", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def stop_container(container_name: str) -> str:
    """Stop a Docker container."""
    result = subprocess.run(["docker", "stop", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def start_container(container_name: str) -> str:
    """Start a Docker container."""
    result = subprocess.run(["docker", "start", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def remove_container(container_name: str) -> str:
    """Remove a Docker container."""
    result = subprocess.run(["docker", "rm", "-f", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def logs_container(container_name: str) -> str:
    """Get logs for a container (last 100 lines)."""
    result = subprocess.run(["docker", "logs", "--tail", "100", container_name], capture_output=True, text=True)
    return result.stdout + result.stderr

@tool
def inspect_container(container_name: str) -> str:
    """Inspect a Docker container."""
    result = subprocess.run(["docker", "inspect", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def docker_stats() -> str:
    """Show Docker container stats."""
    result = subprocess.run(["docker", "stats", "--no-stream"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def docker_top(container_name: str) -> str:
    """Show processes in a container."""
    result = subprocess.run(["docker", "top", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def list_networks() -> str:
    """List Docker networks."""
    result = subprocess.run(["docker", "network", "ls"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def create_network(network_name: str) -> str:
    """Create a Docker network."""
    result = subprocess.run(["docker", "network", "create", network_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def inspect_network(network_name: str) -> str:
    """Inspect a Docker network."""
    result = subprocess.run(["docker", "network", "inspect", network_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def remove_network(network_name: str) -> str:
    """Remove a Docker network."""
    result = subprocess.run(["docker", "network", "rm", network_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def prune_network() -> str:
    """Prune unused Docker networks."""
    result = subprocess.run(["docker", "network", "prune", "-f"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def list_volumes() -> str:
    """List Docker volumes."""
    result = subprocess.run(["docker", "volume", "ls"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def create_volume(volume_name: str) -> str:
    """Create a Docker volume."""
    result = subprocess.run(["docker", "volume", "create", volume_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def inspect_volume(volume_name: str) -> str:
    """Inspect a Docker volume."""
    result = subprocess.run(["docker", "volume", "inspect", volume_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def remove_volume(volume_name: str) -> str:
    """Remove a Docker volume."""
    result = subprocess.run(["docker", "volume", "rm", volume_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def prune_volumes() -> str:
    """Prune unused Docker volumes."""
    result = subprocess.run(["docker", "volume", "prune", "-f"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def show_disk_usage() -> str:
    """Show Docker disk usage."""
    result = subprocess.run(["docker", "system", "df"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def docker_prune() -> str:
    """Prune Docker system (containers, images, networks, volumes)."""
    result = subprocess.run(["docker", "system", "prune", "-f"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def image_history(image_name: str) -> str:
    """Show Docker image history."""
    result = subprocess.run(["docker", "history", image_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def docker_events() -> str:
    """Show Docker events from the last hour."""
    result = subprocess.run(["docker", "events", "--since", "1h"], capture_output=True, text=True)
    return result.stdout or result.stderr

# ---------------------------------------------------------
# System Prompt
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

1. DISCOVER - List all containers, images, networks, and volumes if relevant. Identify the scope.
2. INSPECT - Inspect suspicious containers (config, environment, health, restart policy). Gather runtime metadata.
3. OBSERVE - Read logs thoroughly (include recent and historical logs). Identify errors, crash loops, misconfigurations.
4. DIAGNOSE - Correlate logs + container state + configuration. Identify the most likely root cause with evidence.
5. ACT - Suggest or execute the safest corrective action (restart, rebuild, fix config, adjust compose, etc.). Prefer minimal, reversible changes.
6. VERIFY - Re-check container status and logs after changes. Confirm resolution.

## Tool Usage Rules
- You MUST use tools whenever available (do not simulate outputs).
- If tool output is insufficient, request additional data instead of guessing.
- Prefer multiple small tool calls over one large assumption.

## Decision Style
- Be precise, technical, and evidence-driven.
- Clearly separate: Observations, Inference, Action, Result.

## Failure Handling
- If the issue cannot be resolved, clearly state: what was checked, what was found, what is still unknown, and next recommended debugging step.

You are operating in a production environment. Reliability and correctness matter more than speed.
"""

# ---------------------------------------------------------
# Agent creation (cached)
# ---------------------------------------------------------
@st.cache_resource
def get_agent():
    llm = ChatOllama(model="gemma4", temperature=0.7)
    tools = [
        docker_version, docker_info, pull_image, list_images, list_unused_images,
        remove_images, remove_unused_images, run_container_detach,
        list_running_containers, list_all_containers, restart_container,
        stop_container, start_container, remove_container, logs_container,
        inspect_container, docker_stats, docker_top, list_networks,
        create_network, inspect_network, remove_network, prune_network,
        list_volumes, create_volume, inspect_volume, remove_volume, prune_volumes,
        show_disk_usage, docker_prune, image_history, docker_events,
    ]
    return create_react_agent(
        model=llm,
        tools=tools,
        system_prompt=SystemMessage(content=SYSTEM_PROMPT),   # <-- correct parameter
    )

# ---------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------
st.set_page_config(page_title="Balram's Docker Troubleshooter", page_icon="🐳")
st.title("🐳 Balram's Docker Troubleshooter Agent")
st.markdown("Ask anything about your Docker environment – the agent will use tools to investigate.")

# Initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Sidebar
with st.sidebar:
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.caption("Agent uses tools to list containers, inspect, read logs, restart, and more.")

# React to user input
if prompt := st.chat_input("Ask a Docker question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Balram's Docker Agent thinking..."):
            try:
                agent = get_agent()
                result = agent.invoke({"messages": [("user", prompt)]})
                answer = result["messages"][-1].content
            except Exception as e:
                answer = f"❌ Error: {e}"
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})