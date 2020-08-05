import argparse
from pathlib import Path
import json
import matplotlib.pyplot as plt
import numpy as np
from heapq import nlargest
from collections import defaultdict

# messages/inbox
#  |- DylanSteele (folder)
#  |   |- file1.json (file)
#  |   |- file2.json (file, opened = 'convo')
#  |   |- Photos (file)
#  |   |   |- photo1.jpg
#  |   |- files (file)
#  |   |   |- file1.txt
#  |- AnwellWang (folder)


def nlargest_dict(n, d):
    nlargest_keys = nlargest(n, d, key=d.get)
    nlargest_values = [d[key] for key in nlargest_keys]
    return (nlargest_keys, nlargest_values)


def analyze_messages(inbox_path):
    # Create dictionary that will store chat title/volume as key/value pairing
    # Each key will be initialized with a value of 0
    fb_conversations = defaultdict(lambda: 0)

    # Access the first level of subfolder from "inbox"
    # (e.g. "folder" == DylanSteele in the example above)
    for folder in inbox_path.iterdir():
        # Access the individuals .json files in each conversations "folder"
        for message_file in folder.glob("*.json"):
            with message_file.open() as f:
                data = json.load(f)

            # Check if the message is with an active Facebook user and add the
            # new number of messages to the existing number of messages
            if data["title"] != "Facebook User" and "messages" in data:
                fb_conversations[data["title"]] += len(data["messages"])

    nlargest_messages = nlargest_dict(10, fb_conversations)
    plt.ylabel("Number of Messages")
    plt.xlabel("Name")
    plt.title("Top 10 Most Messaged Recipients on Facebook", fontweight="bold")
    plt.yticks(size=8)
    plt.xticks(size=8, rotation=25, ha="right")
    plt.bar(
        nlargest_messages[0],
        nlargest_messages[1],
        width=0.7,
        color=(0.1, 0.1, 0.1, 0.1),
        edgecolor="blue",
    )
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description="Analyze Facebook Messenger message counts."
    )
    parser.add_argument(
        "inbox",
        help="path to inbox directory",
        # Resolve to an absolute path
        type=lambda p: Path(p).resolve(),
    )
    args = parser.parse_args()
    print(f"Analyzing messages from {args.inbox}")
    analyze_messages(args.inbox)


if __name__ == "__main__":
    main()
