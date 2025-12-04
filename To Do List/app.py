import tkinter as tk
from tkinter import messagebox
import json
import os


FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task = task_entry.get()
    if task != "":
        tasks_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_current_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task")


def delete_task():
    try:
        selected = tasks_list.curselection()[0]
        tasks_list.delete(selected)
        save_current_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task")


def save_current_tasks():
    tasks = list(tasks_list.get(0, tk.END))
    save_tasks(tasks)


def load_to_list():
    tasks = load_tasks()
    for task in tasks:
        tasks_list.insert(tk.END, task)


# App Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("350x450")
root.config(bg="#fff6f6")

title = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#fff6f6", fg="#d93a2a")
title.pack(pady=10)

tasks_frame = tk.Frame(root)
tasks_frame.pack()

tasks_list = tk.Listbox(tasks_frame, width=35, height=15, font=("Arial", 12))
tasks_list.pack(side=tk.LEFT, fill=tk.BOTH)

scroll_bar = tk.Scrollbar(tasks_frame)
scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

tasks_list.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=tasks_list.yview)

task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=10, command=add_task, bg="#d93a2a", fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task, bg="#222", fg="white")
delete_button.pack(pady=5)

load_to_list()

root.mainloop()
