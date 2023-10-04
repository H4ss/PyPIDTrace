# Multi Process Tracing with Strace

This Python script allows you to trace one or more running processes using the `strace` command-line tool from a single application. It finds processes by their PID from the application name and creates a log file for each traced process.

## Prerequisites

- Python 3.x
- `strace` tool (available on most Linux distributions)
- `psutil` Python library (install it using `pip install psutil`)

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Run the script with the following command:

   ```bash
   python3 pypidtrace.py <target_process_name>
   ```

   Replace `<target_process_name>` with the name of the process you want to trace.

4. The script will create log files for each traced process with the format `trace_pid_<pid>.log`, where `<pid>` is the process ID of the traced process.

5. Once the tracing is complete, the script will check if the traced processes have exited and report their status.

## Example

To trace a process named "myapp," run the following command:

```bash
python3 pypidtrace.py myapp
```

The script will start tracing all processes named "myapp" and create log files for each traced process.
