import json
import random
import numpy as np
from tabulate import tabulate


# Reading name and surname data from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

first_names = data['first_names']
last_names = data['last_names']


""" GENERATING DATA AND THE TABLE"""
# Generating 150 full names using random name-surname combinations
full_names = []
for name in first_names:
    for surname in random.sample(last_names, 3):
        full_name = name + ' ' + surname
        full_names.append(full_name)

random.shuffle(full_names)

topics = ['ქართული', 'მათემატიკა', 'ინგლისური', 'ფიზიკა', 'ბიოლოგია']

# Generating random scores matrix with size 150x5 (number of students x number of topics)
scores_matrix = np.random.randint(0, 101, size=(len(full_names), len(topics)))

# Create a column stack of names and data
names_column = np.array(full_names).reshape(-1, 1)  # Reshape names to a column vector
stacked_data = np.column_stack((names_column, scores_matrix))

topics.insert(0, '')
# Create a row stack of topics and stacked data
topics_row = np.array([topics])  # Convert topics list to a row vector
table = np.row_stack((topics_row, stacked_data))

output = 'ცხრილის პირველი 5 ჩანაწერი:\n\n'
output += tabulate(table[:5], tablefmt='grid') + '\n\n'


""" DATA ANALYSIS """
# 1. Calculating the average score for each student and finding the best
avg_scores = {}
for name, scores in zip(table[1:, :1], scores_matrix[1:]):
    avg_scores[name[0]] = np.mean(scores)

best_avg_score = avg_scores.get(max(avg_scores, key=avg_scores.get))
# get the name of the students with the highest average score
best_avg_scorer = [name for name, score in avg_scores.items() if score == best_avg_score][0]
output += f'საუკეთესო სტუდენტია: {best_avg_scorer} საშუალო ქულით - {best_avg_score}\n\n'

# 2. Finding best and worst students in math
math_scores = scores_matrix[:, 1]
best_math_students, worst_math_students = [], []
for name, math_score in zip(table[1:, :1], math_scores):
    if math_score == max(math_scores):
        best_math_students.append(name[0])
    if math_score == min(math_scores):
        worst_math_students.append(name[0])

output += 'საუკეთესო სტუდენტი(ები) მათემატიკაში:\n'
output += f"{', '.join(best_math_students)} - {max(math_scores)} ქულით\n"
output += 'ყველაზე სუსტი სტუდენტი(ები) მათემატიკაში:\n'
output += f"{', '.join(worst_math_students)} - {min(math_scores)} ქულით\n"
output += '\n' * 2

# 3. Finding students with better-than-average English scores
english_scores = scores_matrix[:, 2]
avg_english_score = np.mean(english_scores)
output += 'სტუდენტები საშუალოზე უკეთესი ინგლისურის ქულით:\n'
for name, english_score in zip(table[1:, :1], english_scores):
    if english_score > avg_english_score:
        output += f'{name[0]} - {english_score} ქულა\n'

# Writing output to a file
with open('output.txt', 'w', newline='', encoding='utf-8') as f:
    f.write(output)
