import os
import psutil
import subprocess
import threading
import sys

# Function to trace a PID and save the trace to a file
def trace_pid(pid):
    output_file = f"trace_pid_{pid}.log"
    # Execute strace as a subprocess, redirecting the output to the log file
    subprocess.run(["strace", "-T", "-ttt", "-o", output_file, "-f", "-p", str(pid)])

def main(target_process_name):
    # Find all matching processes by name
    matching_pids = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == target_process_name:
            matching_pids.append(process.info['pid'])

    if not matching_pids:
        print(f"No processes with the name {target_process_name} found.")
    else:
        print(f"Found {len(matching_pids)} processes with the name {target_process_name}:")
        threads = []
        for pid in matching_pids:
            print(f"  - PID: {pid}")
            # Create a thread to trace each PID
            thread = threading.Thread(target=trace_pid, args=(pid,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    # Wait for the traced processes to exit
    for pid in matching_pids:
        while True:
            try:
                os.kill(pid, 0)  # Check if the process is still running
            except ProcessLookupError:
                print(f"Process with PID {pid} has exited.")
                break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 pypidtrace.py <target_process_name>")
        sys.exit(1)

    target_process_name = sys.argv[1]
    main(target_process_name)
