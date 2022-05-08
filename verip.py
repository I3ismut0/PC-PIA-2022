import subprocess

def ipleef():
    comando = 'arp -a'
    lineaPS = "powershell -Executionpolicy ByPass -Command "+ comando
    runningProcesses = subprocess.check_output(lineaPS)
    print(runningProcesses.decode(encoding= 'unicode_escape'))
