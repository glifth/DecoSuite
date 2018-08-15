import color as color

from Misc.fact import *


def test_entry(files):
    file = open(files, 'r')
    lst = []
    for i in file:
        if is_int(i):
            lst.append(1)
        else:
            lst.append(0)
    file.close()
    return lst


def get_files_name(f):
    l = []
    with open(f) as names:
        for name in names:
            l.append(name[:len(name)-1])
    return l


def genere_test(name, f):
    lst = get_files_name(name)
    entete = "      "
    for i in range(0, len(lst)):
        entete += ("{:>" + str(len(lst[i])) + "}  ").format(i)
    f.write(entete + '\n')

    f.write("-" * sum([len(i) for i in lst]) + 6 * "-" + '\n')

    for i in range(0, len(lst)):
        ligne = "{:>10} |".format(lst[i])
        for j in range(1, len(lst)):
            ligne += "{:3}  ".format(color.green("  OK"))
        f.write(ligne + "\n")

    f.write("-" * ((len(lst)) * 7) + '\n')
    f.write("{:>10} |\n".format('ratio'))


name = "name_tests.txt"

with open("file.txt", 'w') as f:
    genere_test(name, f)

