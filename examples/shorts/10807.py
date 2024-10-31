import contextlib

@contextlib.contextmanager
def open_file(filename):
    f = open(filename, 'r')
    try:
        yield f
    finally:
        f.close()

@contextlib.contextmanager
def connect_to_db(db_name):
    connection = f"Connection to {db_name}"
    try:
        yield connection
    finally:
        print(f"Closed connection to {db_name}")

def process_data():
    with contextlib.ExitStack() as stack:
        file = stack.enter_context(open_file('data.txt'))
        db = stack.enter_context(connect_to_db('my_database'))
        
        # Process file and database
        data = file.read()
        print("Processing data:", data)
        print("Using database:", db)

process_data()