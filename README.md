# Sentinel File Monitor

This is a simple Python project that checks if important files were changed.
The program creates three demo files:
- `config.sys`
- `users.db`
- `firewall_rules.txt`

Then it saves the original SHA-256 hash of each file. Every 5 seconds, it checks
the files again. If a file was changed, deleted, or restored, the program prints
an alert and saves it in `incident_report.log`.

## How to run it

```bash
python3 sentinel.py
```
To test it, run the program and then edit one of the demo files.
Press `Ctrl+C` to stop the program.

## What I learned

- How to use file hashes
- How to compare files for changes
- How to write alerts to a log file
- How a basic file integrity monitor works
