from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
import json

priority_mapper = {1: "Low", 2: "Medium", 3: "High"}

all_tasks = []


def clear_view():
    for slave in tk.grid_slaves():
        slave.destroy()


def render_main_view():
    clear_view()
    Button(tk, text='List ol tasks', bg='Blue', fg='white', command=render_list_tasks_view).grid(row=0, column=0, padx=20, pady=20)
    Button(tk, text='Create all tasks', bg='Green', fg='white', command=render_create_view).grid(row=0, column=1,
                                                                                                 padx=200, pady=20)


def create_task(name, description, priority, is_completed):
    try:
        with open("db.txt", "r") as file:
            tasks = json.loads(file.read())
    except:
        tasks = []
    task = {"name": name, "description": description, "priority": priority_mapper[priority], "is_completed": is_completed}
    tasks.append(task)
    with open("db.txt", "w") as file:
        json.dump(tasks, file)


def delete_task(task):
    task_as_obj = eval(task)
    if task:
        with open("db.txt", "r+") as file:
            all_tasks = json.loads(file.read())
            for index in range(len(all_tasks)):
                if all_tasks[index]['name'] == task_as_obj['name']:
                    break
            del all_tasks[index]
            file.truncate(0)
            file.seek(0)
            json.dump(all_tasks, file)
    render_list_tasks_view()



def render_list_tasks_view():
    clear_view()
    try:
        with open("db.txt", "r") as file:
            tasks = json.loads(file.read())
    except:
        tasks = []

    selected_task = StringVar(tk)
    dropdown = Combobox(tk, width=100, textvariable=selected_task, )
    dropdown["value"] = tasks
    dropdown.grid(row=0, column=0)

    Button(tk, text="Delete", bg="red", fg="white", command=lambda : delete_task(selected_task.get())).grid(row=3, column=0, pady=60)
    Button(tk, text="Cancel", bg="black", fg="white", command=render_main_view).grid(row=3, column=1)

def render_create_view():
    clear_view()

    Label(tk, text="Enter your tasks:").grid(row=0, column=0, padx=20, pady=20)
    task_name = Entry(tk)
    task_name.grid(row=0, column=1, padx=20, pady=20)

    Label(tk, text="Enter your task's description:").grid(row=1, column=0, padx=20, pady=20)
    task_description = ScrolledText(tk, width=30, height=10)
    task_description.grid(row=1, column=1, padx=20, pady=20)

    Label(tk, text="Enter your task's priority:").grid(row=2, column=0, padx=20, pady=20)

    task_priority = IntVar()
    radio_button_1 = Radiobutton(tk, text="Low", value=1, variable=task_priority)
    radio_button_2 = Radiobutton(tk, text="Medium", value=2, variable=task_priority)
    radio_button_3 = Radiobutton(tk, text="High", value=3, variable=task_priority)
    radio_button_1.grid(row=2, column=1, padx=20, pady=20)
    radio_button_2.grid(row=2, column=2, padx=20, pady=20)
    radio_button_3.grid(row=2, column=3, padx=20, pady=20)

    Label(tk, text="Is the task completed ?:").grid(row=3, column=0, padx=20, pady=20)
    task_completed = BooleanVar()
    check_box = Checkbutton(tk, variable=task_completed)
    check_box.grid(row=3, column=1, padx=20, pady=20)

    Button(tk, text="Create tasks", bg="green", fg="white", command=lambda: create_task(task_name.get(), task_description.get("1.0", END), task_priority.get(), task_completed.get())).grid(row=4, column=0)
    Button(tk, text="Cancel", bg="black", fg="white", command=render_main_view).grid(row=4, column=1)


if __name__ == "__main__":
    tk = Tk()
    tk.geometry('700x500')
    tk.title("Hello")
    render_main_view()

    tk.mainloop()
