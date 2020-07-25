def present_group_names(groups):
    for group in sorted(groups):
        print(group)


def prompt_for_group_name():
    return input("Type first character(s) of group name: ")


def no_matching_groups(result):
    return bool(not result)


def more_than_one_matching_group(result):
    return bool(len(result) > 1)


def get_groups_starting_with(user_input, groups):
    '''Return list of group names that start with the characters provided
    '''
    return [group for group in groups if group.lower().startswith(user_input.lower())]


def check_input(user_input, groups, origional_goups):
    '''Check user input against group names matching on the first characters of the group name
    If more than one name starts with the characters provided, present a list of matching names
    If no group name starts with the characters provided, present the full list
    '''
    user_input = user_input.strip()
    matching_groups = get_groups_starting_with(user_input, groups)

    if no_matching_groups(matching_groups):
        print()
        present_group_names(origional_goups)
        return check_input(prompt_for_group_name(), origional_goups, origional_goups)

    if more_than_one_matching_group(matching_groups):
        print()
        present_group_names(matching_groups)
        return check_input(prompt_for_group_name(), matching_groups, origional_goups)

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
    chosen_group = check_input(prompt_for_group_name(), groups, groups)
    print("\nYou chose:", chosen_group)


if __name__ == "__main__":
    main()
