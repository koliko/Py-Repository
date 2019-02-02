import os

def load(name):
    '''

    This method crate and load the journal

    :param name: this base name of the journal to load
    :return: a new journal struture
    '''
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entries in fin.readlines():
                data.append(entries.rstrip())
    return data


def save(name, journal_data):

    filname = get_full_pathname(name)

    print("....saving to {}".format(filname))

    with open(filname, "a") as fout:
        for entries in journal_data:
            fout.write(entries + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('./journals/', name + '.jrl'))

    return filename


def add_entries(text, journal_data):
    journal_data.append(text)
