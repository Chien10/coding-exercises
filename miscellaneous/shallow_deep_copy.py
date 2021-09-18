import copy

"""
	Shallow copy
"""
### Only affect the new_list ###
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

new_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

new_list[0] = [4, 4, 4]
print("Old list:", old_list)
print("New list:", new_list)

### Affect both ###
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

new_list[0][0] = 0
print("Old list:", old_list)
print("New list:", new_list)

################################################
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

print(id(old_list))
print(id(new_list))

print(id(old_list[0]))
print(id(new_list[0]))

print(id(old_list[0][0]))
print(id(new_list[0][0]))

"""
	If the id of the `old_list[0]` and the `new_list[0]` is the same, then why changing
	the `new_list[0]`'s value does not affect the value of the `old_list[0]`?
"""

import copy

"""
	Deep copy
"""
### Only affect the new_list ###
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

new_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

new_list[0] = [4, 4, 4]
print("Old list:", old_list)
print("New list:", new_list)

### Affect both ###
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

new_list[0][0] = 0
print("Old list:", old_list)
print("New list:", new_list)

################################################
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print(id(old_list))
print(id(new_list))

print(id(old_list[0]))
print(id(new_list[0]))

print(id(old_list[0][0]))
print(id(new_list[0][0]))

"""
	If the id of the `old_list[0][0]` and the `new_list[0][0]` is the same, then why changing
	the `new_list[0][0]`'s value does not affect the value of the `old_list[0][0]`?
"""

"""
	List within dictionary
"""
question_template = {
    "title": "default title",
    "question": "default question",
    "answer": "default answer",
    "hints": []
}

def make_new_question(title, question: str, answer: str, hints=None):
	new_q = question_template.copy()
    # always require title, question, answer
    new_q["title"] = title
    new_q["question"] = question
    new_q["answer"] = answer
    # sometimes there aren't hints, that's fine. Otherwise, add them:
    if hints is not None:
        new_q["hints"].extend(hints)
    return new_q

question_1 = make_new_question("title1", "question1", "answer1", ["q1 hint1", "q1 hint2"])
question_2 = make_new_question("title2", "question2", "answer2")
question_3 = make_new_question("title3", "question3", "answer3", ["q3 hint1"])

"""
	https://docs.python.org/3/library/copy.html
"""