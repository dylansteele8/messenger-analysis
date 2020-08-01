import os
import json
import matplotlib.pyplot as plt
import numpy as np
from heapq import nlargest

# messages/inbox
#  |- DylanSteele (folder)
#  |   |- file1.json (file)
#  |   |- file2.json (file, opened = 'convo')
#  |   |- Photos (file)
#  |   |   |- photo1.jpg
#  |   |- files (file)
#  |   |   |- file1.txt
#  |- AnwellWang (folder)

def analyze_messages():
	# Create dictionary that will store chat title/volume as key/value pairing
	fb_conversations = {}

	# Define root path
	# TODO: User needs to replace root with their own file path
	root = r'C:\Users\Jerry\Documents\Programming\Python\Personal Projects\FB Messenger Analyzer\facebook-jerrysun123\messages\inbox'
	dir_list = os.listdir(root)

	# Access the first level of subfolder from "inbox"
	# (e.g. "folder" == DylanSteele in the example above)
	for folder in dir_list:
		count_values = 0
		temp = root + "\\" + folder
		convo_dir = os.listdir(temp)

		# Access the individuals .json files in each conversations "folder"
		# (e.g. "json_file" == file1.json in the example above)
		# and sum volume of all messages sent
		for json_file in convo_dir:
			if json_file.endswith(".json"):
				convo = open(temp+"\\"+json_file,"r")
				data = json.load(convo)
				if 'messages' in data:
					count_values += len(data['messages'])
					convo.close()

		# Populates the fb_conversations dictionary with an active Facebook
		# conversation. If a key representing conversations with users already
		# exists, sum all values together for that key
		if (data['title']) != 'Facebook User':
			if (data['title']) not in fb_conversations:
					fb_conversations[data['title']] = count_values
			else:
				fb_conversations[data['title']] = fb_conversations.get(data['title']) + count_values

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

if __name__ == "__main__":
	analyze_messages()
