import subprocess

def get_devices():
    broadcast_address = subprocess.check_output(["ifconfig", "en0"]).decode("utf-8").split("inet")[1].split("/")[0]

    return broadcast_address

print(get_devices())
