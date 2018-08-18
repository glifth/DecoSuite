import os

from src.helper import *
from tests.fact import *

init_log_file = False


def decoSuite(function):
    def wrapper(*args, **kwargs):
        test_list = []
        result_list = []

        with open("../tests/test_" + function.__name__ + ".dcs") as f:
            name = os.path.basename(f.name)
            for test in f:
                if test[len(test) - 1] == '\n':
                    test = test[:-1]
                test_list.append(test)
                if is_int(test):
                    result_list.append(str(function(int(test))) + '\n')
                else:
                    result_list.append(function(test))

        open_status = "a"
        with open("../tests/log.txt", open_status) as log:
            log.write("\n" + "{:-^80}".format(" " + name + " ") + '\n')
            log.write("Test File Input \n")
            if len(test_list) == 0:
                log.write("No test in the file.\n")
                return
            longest = sorted(map(len, test_list))[len(result_list) - 1]

            for i in range(0, len(result_list)):
                log.write("  " + ("{:" + str(longest) + "}").format((test_list[i])) + "  =>  " + result_list[i])

        return

    return wrapper

"""
def genere_test(lst, f):
    entete = "            "

    for i in lst:
        entete += ("{:>" + str(len(i)) + "}  ").format(i)
    f.write(entete + '\n')

    sep = "-" * len(entete) + '\n'
    f.write(sep)

    for i in range(0, len(lst)):
        ligne = "{:>10} |".format(lst[i])
        for j in range(0, len(lst)):
            ligne += ("{:>" + str(len(lst[i])) + "}  ").format(color.green("  OK"))
        f.write(ligne + "\n")

    f.write(sep)
    f.write("{:>10} |\n".format('ratio'))


name = sorted(os.listdir("../tests"))

print(name)

with open("file.txt", 'w') as f:
    genere_test(name, f)

"""