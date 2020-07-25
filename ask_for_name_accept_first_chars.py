def present_group_names(groups):
    for group in sorted(groups):
        print(group)


def prompt_for_group_name():
    return input("Type group name: ")


def no_matching_groups(result):
    return bool(not result)


def more_than_one_matching_group(result):
    return bool(len(result) > 1)


def get_groups_starting_with(user_input, groups):
    return [group for group in groups if group.lower().startswith(user_input.lower())]


def check_input(user_input, groups):
    user_input = user_input.strip()
    matching_groups = get_groups_starting_with(user_input, groups)

    if no_matching_groups(matching_groups):
        print()
        present_group_names(groups)
        return check_input(prompt_for_group_name(), groups)

    if more_than_one_matching_group(matching_groups):
        print()
        present_group_names(matching_groups)
        return check_input(prompt_for_group_name(), matching_groups)

    return matching_groups[0]


def main():
    groups = [
        "Audit",
        "Domain Controller",
        "Protect",
        "Server",
        "Triage",
        "Trusted",
        "Technician"
    ]

    present_group_names(groups)
    chosen_group = check_input(prompt_for_group_name(), groups)
    print("\nYou chose:", chosen_group)


if __name__ == "__main__":
    main()
