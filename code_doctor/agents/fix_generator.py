from google.adk.agents import LlmAgent
from ..config import get_model
from ..prompts import FIXER_PROMPT

fixer = LlmAgent(
    name="fix_generator",
    model=get_model(),
    instruction=FIXER_PROMPT,
    output_key="fix",
)