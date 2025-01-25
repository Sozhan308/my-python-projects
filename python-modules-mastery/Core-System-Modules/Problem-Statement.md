# Problem Statements with Elaboration

## Problem 1: Directory Traversal and File Size Summary
**Task:** Write a script that:
- Traverses a given directory (including subdirectories).
- Lists all files with their sizes and last modified times.
- Outputs a summary of the total number of files, directories, and total size.

**Modules:** `os`, `sys`

**Key Concepts:**
- Use `os.walk` for traversing directories.
- Use `os.stat` or `os.path.getsize` for file information.
- Accept the directory path as a command-line argument using `sys.argv`.

**Bonus:**
- Add an option to save the output as a CSV or JSON.

---

## Problem 2: System Information Dashboard
**Task:** Build a Python script that:
- Displays detailed information about the system (e.g., OS type, version, architecture, processor, and Python version).
- Shows uptime, CPU usage, memory usage, and disk usage.

**Modules:** `platform`, `sys`, `psutil`

**Key Concepts:**
- Use `platform` for OS details and `sys.version` for Python version.
- Use `psutil` for monitoring CPU, memory, and disk usage.
- Format the output into a readable report (e.g., table or JSON).

**Bonus:**
- Add options to write the output to a file or display it in real-time with periodic updates.

---

## Problem 3: File Organizer Script
**Task:** Create a script that organizes files in a directory based on their type (e.g., `.txt`, `.jpg`, `.pdf`).
- Automatically create subdirectories for each file type (e.g., `Documents`, `Images`).
- Move files into the appropriate subdirectories.

**Modules:** `os`, `sys`

**Key Concepts:**
- Use `os.listdir` to list directory contents.
- Use `os.path.splitext` to determine file extensions.
- Use `os.makedirs` to create directories dynamically.

**Bonus:**
- Add a log file to record which files were moved and where.

---

## Problem 4: Process Monitor
**Task:** Write a Python script that:
- Lists all running processes with their process IDs (PIDs), names, and memory usage.
- Allows the user to search for a specific process by name or PID.
- Optionally kills a process by PID.

**Modules:** `psutil`, `sys`

**Key Concepts:**
- Use `psutil.process_iter` to iterate over running processes.
- Retrieve process details such as `name()`, `pid`, and `memory_info()`.
- Use `sys.argv` or user input to accept search criteria or PID to kill.

**Bonus:**
- Add options to monitor real-time CPU and memory usage of a specific process.

---

## Problem 5: Platform Compatibility Check
**Task:** Build a script that:
- Detects the current operating system and architecture (e.g., Windows 64-bit, Linux 32-bit).
- Checks whether a given software is compatible with the system.
- Logs compatibility results.

**Modules:** `platform`, `logging`

**Key Concepts:**
- Use `platform.system()` and `platform.architecture()` for OS and architecture details.
- Use `logging` to create a compatibility log.

**Bonus:**
- Add a database of software compatibility (e.g., in JSON format) to validate multiple software items.

---

## Problem 6: Disk Space Analyzer
**Task:** Create a script that:
- Scans all drives or a specific directory.
- Shows the total, used, and available disk space.
- Alerts the user if disk space usage exceeds a threshold (e.g., 90%).

**Modules:** `psutil`, `sys`

**Key Concepts:**
- Use `psutil.disk_partitions` to list all mounted partitions.
- Use `psutil.disk_usage` to fetch disk space stats.
- Accept the threshold as a command-line argument or user input.

**Bonus:**
- Send email alerts for critical thresholds using `smtplib`.

---

# Key Concepts for Each Module

## `os`
- Navigating and manipulating the file system.
- Interacting with environment variables.
- Fetching metadata like file size and modification time.

## `sys`
- Accessing command-line arguments.
- System-specific configurations and error handling.

## `platform`
- Identifying OS details like type, version, and architecture.

## `psutil`
- Monitoring system health (CPU, memory, disk, network).
- Fetching process-related information.
