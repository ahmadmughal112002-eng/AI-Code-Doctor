from google.adk.agents import SequentialAgent

from .code_analyzer import analyzer
from .fix_generator import fixer
from .report_formatter import reporter

main_agent = SequentialAgent(
    name="code_doctor",
    sub_agents=[analyzer, fixer, reporter],
)