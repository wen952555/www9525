import subprocess
import time
import threading
from pathlib import Path

LOG_FILE = Path("logs/shell_connections.log")

def execute_shell_command(command: str, user_id: int) -> str:
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        output = result.stdout or result.stderr
        log_connection(user_id, command, output)
        return output if output else "Command executed successfully with no output."
    except Exception as e:
        log_connection(user_id, command, f"Error: {e}")
        return f"Error executing command: {e}"

def schedule_shell_command(command: str, delay: int, user_id: int) -> None:
    def task():
        time.sleep(delay)
        execute_shell_command(command, user_id)

    threading.Thread(target=task, daemon=True).start()

def log_connection(user_id: int, command: str, result: str) -> None:
    with LOG_FILE.open("a") as log_file:
        log_file.write(f"User: {user_id}, Command: {command}, Result: {result}\n")