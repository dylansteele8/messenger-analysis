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
			if data['title'] != 'Facebook User' and 'messages' in data:
				fb_conversations[data['title']] += len(data['messages'])

	# extract the top 10 most messaged keys and place them in a new dictionary
	ten_largest = nlargest(10, fb_conversations, key = fb_conversations.get)
	graph = {}
	for val in ten_largest:
		graph[val] = fb_conversations.get(val)

	# Put the top 10 most messaged individuals in a bar graph
	n_groups = 10
	index = np.arange(n_groups)
	x_axis = graph.keys()
	y_axis = graph.values()
	plt.ylabel("Number of Messages")
	plt.xlabel("Name")
	plt.title("Top 10 Most Messaged Recipients on Facebook", fontweight="bold")
	plt.yticks(size = 8)
	plt.xticks(index, size=8, rotation=25)
	plt.bar(x_axis, y_axis,width = 0.7, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')
	plt.show()

def main():
	parser = argparse.ArgumentParser(
		description='Analyze Facebook Messenger message counts.'
	)
	parser.add_argument(
		'inbox',
		help='path to inbox directory',
		# Resolve to an absolute path
		type=lambda p: Path(p).resolve()
	)
	args = parser.parse_args()
	print(f"Analyzing messages from {args.inbox}")
	analyze_messages(args.inbox)


if __name__ == "__main__":
	main()

