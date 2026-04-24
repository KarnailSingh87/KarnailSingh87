import os
import subprocess
from datetime import datetime, timedelta
import random

def boost(count):
    print(f"Starting {count} commits...")
    
    for i in range(1, count + 1):
        # Create or update a log file to ensure there's a change
        with open("activity_log.txt", "a") as f:
            f.write(f"Contribution update {i}: {datetime.now().isoformat()}\n")
        
        # Add and commit
        subprocess.run(["git", "add", "activity_log.txt"], capture_output=True)
        
        # You can customize the commit messages here
        msg = f"chore: update activity log increment {i}"
        subprocess.run(["git", "commit", "-m", msg], capture_output=True)
        
        if i % 100 == 0:
            print(f"Progress: {i}/{count} commits done.")

    print("\nFinished!")
    print("Next step: Run 'git push' to see the changes on GitHub.")

if __name__ == "__main__":
    # Change this number to however many commits you want
    # Recommendation: Start with 500 or 1000. 100,000 will take hours.
    num_commits = 500 
    boost(num_commits)
