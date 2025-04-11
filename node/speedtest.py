import subprocess
import json

def run_speedtest():
    try:
        result = subprocess.run(["speedtest-cli", "--json"], capture_output=True, text=True)
        return json.loads(result.stdout)
    except Exception as e:
        return {"error": str(e)}