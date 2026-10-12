# AI-Infused Learning II

A hands-on Python project exploring **LLM applications, AI agents, conversational memory, and website summarization** using modern AI development tools.

## Features

- **AI Agent:** Implements tool calling using Groq-hosted `openai/gpt-oss-120b`.
- **Smart Shop Assistant:** Interactive chatbot built with Gradio that retrieves product prices.
- **Conversational Memory:** Experiments with maintaining chat history using LangChain.
- **Website Summarization:** Extracts website content and generates AI-powered summaries.

## Tech Stack

- Python
- Groq API and GPT-OSS-120B
- LangChain
- Gradio
- BeautifulSoup
- Python-dotenv

## Project Structure

```text
AI-Infused-Learning-II/
├── agent.py
├── app.py
├── memory_chat.py
├── memory_demo.py
├── scraper.py
├── summarizer_langchain.py
└── .gitignore
```

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/pr9je/AI-Infused-Learning-II.git
cd AI-Infused-Learning-II
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**3. Install dependencies**

```bash
pip install openai python-dotenv gradio langchain-openai langchain-core requests beautifulsoup4
```

**4. Configure environment variables**

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Obtain your API key from [Groq Console](https://console.groq.com/).

**5. Run the application**

```bash
python app.py
```

## Learning Objectives

- Build LLM-powered agents with function calling.
- Integrate language models with external tools.
- Manage conversational context using LangChain.
- Develop AI chat interfaces and website summarization workflows.

## Author

**Mitesh Prajapati**

[GitHub Profile](https://github.com/pr9je) · [Project Repository](https://github.com/pr9je/AI-Infused-Learning-II)
