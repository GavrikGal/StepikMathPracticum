from typing import List
import os.path

event = "git fetch origin"
file_name = "Base_python/tmp/git.log"

def get_log_lines(file_name: str) -> List[str]:
    current_log_lines = []
    if os.path.isfile(file_name):
        with open(file_name, encoding='utf-8') as f:
            current_log_lines = f.readlines()
    return current_log_lines

def get_next_event_number(log_lines: List[str]) -> int:
    lines_with_events = [line for line in log_lines if line != '\n']
    return len(lines_with_events) + 1

def prepare_event_str(event: str, n: int):
    return f"event {n} - '{event}'\n"

def add_event(event: str, log_lines: List[str]):
    log_lines.insert(0, event)

def write_log(log_lines: List[str], file_name: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(log_lines)

log_lines = get_log_lines(file_name)
next_event_n = get_next_event_number(log_lines)
event_str = prepare_event_str(event, next_event_n)
add_event(event_str, log_lines)
write_log(log_lines, file_name)
