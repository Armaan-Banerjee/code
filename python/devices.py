import subprocess

def get_devices():
    broadcast_address = subprocess.check_output(["ifconfig", "en0"]).decode("utf-8").split("inet")[1].split("/")[0]


    ping_output = subprocess.check_output(["ping", "-c1", broadcast_address]).decode("utf-8")

    devices = []

    for line in ping_output.splitlines():
        if line.startswith("PING"):
            continue

        ip_address = line.split("(")[1].split(")")[0]

        mac_address = line.split("(")[0].split(":"")")[5]

        devices.append({
            "ip address": ip_address,
            "mac_address": mac_address
        })

    return devices

if __name__ == "__main__":
    devoces = get_devices()
    for device in devices:
        print(f'ip address: {device["ip_address"]} \n MAC address: {device["mac_address"]}')
