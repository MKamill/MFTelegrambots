def search_command(incoming_message):
    if isinstance(incoming_message, str):
        command = ''
        if '(' in incoming_message:
            for i, element in enumerate(incoming_message):
                if element == '(':
                    while incoming_message[i] != ')':
                        command += incoming_message[i]
                        i += 1
                    else:
                        command += incoming_message[i]
        else:
            return 'no valid command'
    return command


def break_into_words(modified_message):
    list_of_words = []
    helping_str = ''
    for i, element in enumerate(modified_message):
        if element != '(' and element != ')':
            helping_str += element
        if element == ' ' or element == ')':
            list_of_words.append(helping_str)
            helping_str = ''
    for iter in range(0, len(list_of_words)):
        list_of_words[iter] = list_of_words[iter].replace(' ', '')
    return list_of_words


def action_check(list):
    if 'mail' in list and 'to' in list:
        return True


def call_all_defs(data):
    return action_check(break_into_words(search_command(data)))
