from google.adk.agents import LlmAgent
from ..config import get_model
from ..prompts import REPORTER_PROMPT

reporter = LlmAgent(
    name="report_formatter",
    model=get_model(),
    instruction=REPORTER_PROMPT,
)