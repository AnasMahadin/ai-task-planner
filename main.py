import json
import requests

def generate_tasks(context, api_token=None):
    """Generate tasks using Hugging Face Inference API."""
    try:
        # Use a small model like distilgpt2
        api_url = "https://api-inference.huggingface.co/models/distilgpt2"
        headers = {"Authorization": f"Bearer {api_token}" if api_token else {}}
        prompt = f"Generate a list of 3 tasks for a {context} schedule, each with a task name and time slot (e.g., 'Task: Cook dinner, Time: 18:00-19:00')."
        payload = {"inputs": prompt, "parameters": {"max_length": 100}}
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            generated_text = response.json()[0]["generated_text"]
            # Parse generated text into tasks
            tasks = []
            lines = generated_text.split("\n")
            for line in lines:
                if "Task:" in line and "Time:" in line:
                    task_name = line.split("Task:")[1].split(", Time:")[0].strip()
                    time_slot = line.split("Time:")[1].strip()
                    tasks.append({"task": task_name, "time": time_slot})
            return tasks[:3]  # Limit to 3 tasks
        else:
            return [
                {"task": f"{context} activity 1", "time": "09:00-10:00"},
                {"task": f"{context} activity 2", "time": "10:30-11:30"},
                {"task": f"{context} activity 3", "time": "12:00-12:30"}
            ]
    except Exception:
        return [
            {"task": f"{context} activity 1", "time": "09:00-10:00"},
            {"task": f"{context} activity 2", "time": "10:30-11:30"},
            {"task": f"{context} activity 3", "time": "12:00-12:30"}
        ]

def generate_task_plan(user_input):
    try:
        # Extract number of days and context
        days = 1
        words = user_input.lower().split()
        for word in words:
            if word.isdigit():
                days = int(word)
                break
        # Extract context (e.g., "gym" from "Plan a gym schedule")
        context = "general"
        for word in words:
            if word in ["gym", "cooking", "playing", "study", "work"]:
                context = word
                break
        # Generate tasks using AI
        tasks = generate_tasks(context)
        # Create schedule
        schedule = {f"Day {i+1}": tasks for i in range(days)}
        return json.dumps(schedule, indent=4)
    except Exception:
        return "Error: Please specify a valid input (e.g., 'Plan a cooking schedule for 3 days')."

def print_table(schedule_json):
    try:
        schedule = json.loads(schedule_json)
        print("\nSchedule Table:")
        print("-" * 50)
        for day, tasks in schedule.items():
            print(f"{day}:")
            for task in tasks:
                print(f"  {task['time']} | {task['task']}")
            print("-" * 50)
    except:
        print("Error: Cannot display table for invalid schedule.")

def main():
    print("=== AI Task Planner ===")
    print("Enter your plan request (e.g., 'Plan a cooking schedule for 3 days')")
    user_input = input("> ")
    plan = generate_task_plan(user_input)
    print("\nYour Schedule (JSON):")
    print(plan)
    if "Error" not in plan:
        print_table(plan)

if __name__ == "__main__":
    main()