# Concepts

### /proc
- Stored information of the current processes
- This filesystem consists of kernel data that changes in real time
- There is a numbered directory in /proc corresponding to each PID currently on the system

### trap
- Is a bash mechanism which allows to customize a script behavior when it receives a signal
- **Syntaxs**
```bash
trap [actions] [signal]
#example
trap 'echo "Signal detected: SIGINT"' SIGINT
```

### Signal
- SIGTERM(15): This signal send by the kill or pkill command
- SIGSTOP(19), SIGKILL(9): Signals cannot be caught or ignored
