import tkinter as tk

# Debounce function decorator
def debounce(wait):
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)

            if hasattr(debounced, '_timer'):
                debounced._timer.cancel()
            debounced._timer = threading.Timer(wait, call_it)
            debounced._timer.start()

        return debounced
    return decorator

# Function to be debounced
@debounce(0.5)  # 500 milliseconds debounce time
def search_function(query):
    print(f"Searching for: {query}")

# Setting up the GUI
def on_entry_change(event):
    query = entry.get()
    if query:
        search_function(query)

root = tk.Tk()
root.title("Debounce Function Example")

entry = tk.Entry(root)
entry.pack(pady=20)
entry.bind("<KeyRelease>", on_entry_change)

root.mainloop()