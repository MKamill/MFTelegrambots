from string import punctuation as punct
import random as rnd


def search_words(incoming_message):
    if isinstance(incoming_message, str):
        helping_str, helping_list = '', []
        for i, element in enumerate(incoming_message):
            helping_str += element
            if element in punct or element == ' ':
                helping_str[i].replace(element,'')
                helping_list.append(helping_str)
                helping_str = ''
        else:
            helping_list.append(helping_str)
            del helping_str
    for iter in range(0, len(helping_list)):
        helping_list[iter] = helping_list[iter].replace(' ', '')
    while '' in helping_list:
        helping_list.remove('')
    return helping_list



print(search_words(
    'Всякая   записанная речь (литературное произведение, сочинение, документ и т. п., а также часть, отрывок из них).'))

def random_delete(helping_list):
    new_list = list(range(len(helping_list)))
    while len(new_list) != 0:
        s = rnd.randrange(len(helping_list))
        if s in new_list:
            new_list.remove(s)
            print(new_list)

random_delete()


