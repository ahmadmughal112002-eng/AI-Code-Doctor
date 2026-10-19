from google.adk.agents import LlmAgent
from ..config import get_model
from ..prompts import ANALYZER_PROMPT

analyzer = LlmAgent(
    name="code_analyzer",
    model=get_model(),
    instruction=ANALYZER_PROMPT,
    output_key="analysis",
)