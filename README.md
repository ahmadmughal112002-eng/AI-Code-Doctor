# AI Code Doctor - 3 Agents (No RAG)

A beginner-friendly Google ADK project using local **Ollama Llama 2 7B**.

## What is included?

1. Code Analyzer + Bug Detector (one agent)
2. Fix Generator (one agent)
3. Report Formatter (one agent)

`SequentialAgent` is the workflow controller, **not** a fourth LLM agent. No RAG, vector database, embeddings, document loader, external API key, Docker, or test-execution tools.

## First run (Windows PowerShell)

Open a terminal in this folder:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
ollama pull llama2:7b
ollama run llama2:7b
```

Type `/bye` to exit the Ollama chat, then:

```powershell
adk web
```

Open http://127.0.0.1:8000 and select **code_doctor**.

If Python 3.11 isn't installed, Python 3.12 or 3.13 can be used, subject to library compatibility: `python -m venv .venv`.

If port 8000 is busy, stop the other `adk web` process with Ctrl+C.

## Sample prompt

```text
Find bugs and fix this Python code:

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print(calculate_average([]))
```

## Model mapping

Hugging Face model ID `meta-llama/Llama-2-7b` refers to the **base** model. This project runs Ollama's `llama2:7b`, which is the **chat/instruction-tuned Llama 2 7B variant**, not the byte-identical Hugging Face base checkpoint. A chat-tuned model is more suitable for conversational agents. For the exact base checkpoint, a separate supported model import/conversion and configuration would be needed.

## Notes

- Only three LLM calls in the fixed workflow per turn; a 7B model may still respond slowly on CPU.
- Reports provide suggested fixes; they do **not** run tests or certify code correctness.
- Don't paste secrets or run generated code blindly.
