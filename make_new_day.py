from pathlib import Path

def make_new_day(day_number):
    folder_name = f"day{day_number}"
    
    Path(folder_name).mkdir(exist_ok=True)
    
    files = ["sol.py", "input.in", "test.in"]
    for file in files:
        file_path = Path(folder_name) / file
        file_path.touch()
    
    print(f"Created folder '{folder_name}' with 3 empty files")


day = input("Enter day number: ")
make_new_day(day)