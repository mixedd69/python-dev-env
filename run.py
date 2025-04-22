import time
import os
import subprocess
import signal
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_app()

    def start_app(self):
        if self.process:
            print("Restarting application...")
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
        else:
            print("Starting application...")

        # Start the Flask application
        self.process = subprocess.Popen(
            ["python", "app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            preexec_fn=os.setsid,
        )

    def on_modified(self, event):
        if event.src_path.endswith(".py") and not event.src_path.endswith("run.py"):
            print(f"Change detected in {event.src_path}")
            self.start_app()


if __name__ == "__main__":
    path = "."
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            line = event_handler.process.stdout.readline()
            if line:
                print(line.decode("utf-8").strip())
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            os.killpg(os.getpgid(event_handler.process.pid), signal.SIGTERM)

    observer.join()