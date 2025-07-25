 ### AI Task Planner

     A vibe-coded Python tool that generates dynamic task schedules from natural language inputs using Windsurf and Hugging Face’s free-tier Inference API. Built to showcase AI-driven automation for the Vibe Coder role at HUMAIN.

     ## Features

     - Takes natural language input (e.g., "Plan a cooking schedule for 3 days")
     - Generates context-specific tasks (e.g., cooking, gym, playing) using AI
     - Outputs structured JSON schedules and a formatted table for user-friendliness
     - Developed with Windsurf for creative, AI-assisted coding

     ## Setup

     1. Install Python 3.8 or higher
     2. Install dependencies: `pip install requests`
     3. Run: `python main.py`

     ## Vibe Coding Process

     Used Windsurf’s chat in VS Code to integrate Hugging Face’s Inference API, generating dynamic tasks via natural language prompts. Iterated to ensure intuitive output for diverse contexts like cooking, gym, or playing.

     ## API Usage

     This project currently uses **Hugging Face’s free-tier Inference API** (`distilgpt2` model) for task generation, suitable for prototyping but limited by rate limits and basic context understanding. The script extracts context from a predefined list of keywords (e.g., “cooking,” “gym”), which may not capture all user inputs. A paid API (e.g., Hugging Face’s Pro tier or xAI’s Grok API) would significantly improve performance by offering more powerful models, better natural language processing for context extraction, higher request quotas, and faster response times, resulting in more relevant and accurate task generation for any user-defined schedule.