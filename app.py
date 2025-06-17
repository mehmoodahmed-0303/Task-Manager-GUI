import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import uuid

TASK_FILE = "tasks.json"

class TaskManagerApp:

	def __init__(self, root):
		self.root = root
		self.root.title("Task Manager")
		self.root.geometry("800x600")
		self.root.configure(bg="#f0f2f5")

		#initialize task file
		if not os.path.exists(TASK_FILE):
			with open(TASK_FILE, "w") as file:
				json.dump([], file)

		# Style configuration
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("TButton", padding=10, font=("Helvetica", 10), background="#4e73df", foreground="white")
		style.map("TButton",  background=[("active", "#3b5bdb")])
		style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="#dfe4ea")
		style.configure("Treeview", rowheight=25, font=("Helvetica", 9))
		style.configure("TLable", font=("Helvetica", 10), background="#f0f2f5")
		style.configure("TEntry", padding=5)

		# Main containerr
		self.container = tk.Frame(self.root, bg="#f0f2f5")
		self.container.pack(padx=20, pady=20, fill="both", expand=True)

		# Header
		header = tk.Label(self.container, text="Task Manager", font=("Helvetica", 18, "bold"), bg="#f0f2f5", fg="#2d3436")
		header.pack(pady=10)

		# Task Treeview
		self.tree = ttk.Treeview(self.container, columns=("ID", "Title", "Status", "Priority", "Assignee", "Deadline"), show="headings")
		self.tree.heading("ID", text="ID")
		self.tree.heading("Title", text="Title")
		self.tree.heading("Status", text="Status")
		self.tree.heading("Priority", text="Priority")
		self.tree.heading("Assignee", text="Assignee")
		self.tree.heading("Deadline", text="Deadline")
		self.tree.column("ID", width=50, anchor="center")
		self.tree.column("Title", width=150)
		self.tree.column("Status", width=100)
		self.tree.column("Priority", width=100)
		self.tree.column("Assignee", width=100)
		self.tree.column("Deadline", width=100)
		self.tree.pack(pady=10, expand=True, fill="both")
		self.tree.bind("<Double-1>", self.edit_task_popup)
		self.refresh_tasks()

		# Input Frame
		input_frame = tk.Frame(self.container, bg="#f0f2f5")
		input_frame.pack(pady=10, fill="x")

		# Input Fields
		tk.Label(input_frame, text="Title:", bg="#f0f2f5").grid(row=0, column=0, padx=5, sticky="e")
		self.title_entry = ttk.Entry(input_frame)
		self.title_entry.grid(row=0, column=1, padx=5, sticky="ew")

		tk.Label(input_frame, text="Description:", bg="#f0f2f5").grid(row=1, column=0, padx=5, sticky="e")
		self.desc_entry = ttk.Entry(input_frame)
		self.desc_entry.grid(row=1, column=1, padx=5, sticky="ew")

		tk.Label(input_frame, text="Deadline (YYYY-MM-DD):", bg="#f0f2f5").grid(row=0, column=2, padx=5, sticky="e")
		self.deadline_entry = ttk.Entry(input_frame)
		self.deadline_entry.grid(row=0, column=3, padx=5, sticky="ew")

		tk.Label(input_frame, text="Priority:", bg="#f0f2f5").grid(row=1, column=2, padx=5, sticky="e")
		self.priority_combo = ttk.Combobox(input_frame, values=["low", "medium", "high"], state="readonly")
		self.priority_combo.set("medium")
		self.priority_combo.grid(row=1, column=3, padx=5, sticky="ew")

		tk.Label(input_frame, text="Assignee:", bg="#f0f2f5").grid(row=0, column=4, padx=5, sticky="e")
		self.assignee_entry= ttk.Entry(input_frame)
		self.assignee_entry.grid(row=0, column=5, padx=5, sticky="ew")

		input_frame.columnconfigure(1, weight=1)
		input_frame.columnconfigure(3, weight=1)
		input_frame.columnconfigure(5, weight=1)

		# Button Frame
		button_frame = tk.Frame(self.container, bg="#f0f2f5")
		button_frame.pack(pady=10)
		ttk.Button(button_frame, text="Add Task", command=self.create_task).pack(side="left", padx=5)
		ttk.Button(button_frame, text="Delete Selected", command=self.delete_task).pack(side="left", padx=5)
		ttk.Button(button_frame, text="Clear Fields", command=self.clear_fields).pack(side="left", padx=5)



	def edit_task_popup(self):
		pass
	def refresh_tasks(self):
		pass
	def create_task(self):
		pass
	def delete_task(self):
		pass
	def clear_fields(self):
		pass

if __name__ == "__main__":
	root = tk.Tk()
	app = TaskManagerApp(root)
	root.mainloop()