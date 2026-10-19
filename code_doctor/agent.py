
"""AI Code Doctor - Three simple Google ADK agents."""

import os

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm

from .prompts import ANALYZER_PROMPT, FIXER_PROMPT, REPORTER_PROMPT


# Ollama configuration
os.environ.setdefault("OLLAMA_API_BASE", "http://localhost:11434")
MODEL = "ollama_chat/qwen2.5-coder:7b"


# Agent 1: Code Analyzer + Bug Detector
analyzer = LlmAgent(
    name="code_analyzer",
    model=LiteLlm(model=MODEL),
    instruction=ANALYZER_PROMPT,
    output_key="analysis",
)


# Agent 2: Fix Generator
fixer = LlmAgent(
    name="fix_generator",
    model=LiteLlm(model=MODEL),
    instruction=FIXER_PROMPT,
    output_key="fix",
)


# Agent 3: Report Formatter
reporter = LlmAgent(
    name="report_formatter",
    model=LiteLlm(model=MODEL),
    instruction=REPORTER_PROMPT,
)


# Root Workflow
root_agent = SequentialAgent(
    name="code_doctor",
    sub_agents=[
        analyzer,
        fixer,
        reporter,
    ],
)
