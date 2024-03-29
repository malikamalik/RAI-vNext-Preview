# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import json


def prompt_yes_no(prompt: str) -> bool:
    response = "INVALID"
    while response not in ["y", "n"]:
        response = input(prompt + " (y/n)")
        response = response.lower()
    return response == "y"


def create_workspace_config():
    JSON_FILE = "config.json"
    config_dict = dict()
    config_dict["subscription_id"] = input("Enter subscription id: ")
    config_dict["resource_group"] = input("Enter resource group name: ")
    config_dict["workspace_name"] = input("Enter workspace name: ")

    with open(JSON_FILE, "w") as jf:
        json.dump(config_dict, jf)
    print("Written {0}".format(JSON_FILE))


def create_component_config():
    JSON_FILE = "component_config.json"
    config_dict = dict()
    config_dict["version"] = int(input("Enter version: "))

    with open(JSON_FILE, "w") as jf:
        json.dump(config_dict, jf)
    print("Written {0}".format(JSON_FILE))


def main():
    if prompt_yes_no("Create workspace config.json? "):
        create_workspace_config()
    if prompt_yes_no("Create component_config.json? "):
        create_component_config()
    print("Completed")


if __name__ == "__main__":
    main()
