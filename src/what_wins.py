def beats(task_1, task_2):
    if task_1.choice == 'scissors' and task_2.choice  == 'paper':
        return task_1.choice
    elif task_2.choice == 'scissors' and task_1.choice  == 'paper':
        return task_2.choice

    elif task_1.choice == 'paper' and task_2.choice == 'rock':
        return task_1.choice
    elif task_2.choice == 'paper' and task_1.choice == 'rock':
        return task_2.choice

    elif  task_1.choice == 'rock' and task_2.choice == 'scissors':
        return task_1.choice
    elif  task_2.choice == 'rock' and task_1.choice == 'scissors':
        return task_2.choice