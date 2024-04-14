"""
Description: Update the ports in the configuration file
Author: Daniel Diamont
"""


import json
import sys
import os


def update_ports(ports, config_file):
    """
    Update the ports in the configuration file

    :param ports: list of ports to update
    :param config_file: configuration file path
    :return: None
    """
    with open(config_file, "r", encoding="utf-8") as file:
        config = json.load(file)

        prefix = "/dev/pts/"

        print("Current ports:")
        print(f"{config['serial-loopback']['TX']['port'] = }")
        print(f"{config['serial-loopback']['RX']['port'] = }")

        config["serial-loopback"]["TX"]["port"] = f"{prefix}{ports[0]}"
        config["serial-loopback"]["RX"]["port"] = f"{prefix}{ports[1]}"

        print("Updated ports:")
        print(f"{config['serial-loopback']['TX']['port'] = }")
        print(f"{config['serial-loopback']['RX']['port'] = }")

    with open(config_file, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


if __name__ == "__main__":
    config_path = os.path.join(
        os.path.dirname(__file__),
        "tests",
        "config.json")

    assert len(
        sys.argv) == 3, "Usage: python3 demo_update_ports.py <tx_port> <rx_port>"

    update_ports(sys.argv[1:], config_path)
