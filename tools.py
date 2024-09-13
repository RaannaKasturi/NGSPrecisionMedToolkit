import subprocess

def run_command_out(cmd, dir=None):
    if dir:
        cmd[0] = dir+cmd[0]
    try:
        output = subprocess.check_output(cmd)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print("An error occurred while running the command:", e.output.decode())
        return cmd

def run_command(cmd, dir=None):
    if dir:
        cmd[0] = dir + cmd[0]
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError as e:
        return False