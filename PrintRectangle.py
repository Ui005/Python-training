class Programm:
    def PrintRectangle(file):
        # печать в файл с именем file прямоугольника из символов * со сторонами a и b
        a, b = int(open(file).readline().split()[0]), int(open(file).readline().split()[1])
        file = open(file).read().split("\n")[1]
        f = open(file, "w")
        f.write(a * "* " + "\n")
        for i in range(b - 2):
            f.write("*" + (" " * (2 * a - 3)) + "*" + "\n")
        f.write(a * "* " + "\n")
        f.close()

    def PrintSquare(file):
        # печать в файл с именем file квадрата из символов * со стороной a.
        a = b = int(open(file).readline())
        file1 = open(file).read().split("\n")[1]
        f = open(file1, "w")
        f.write(a * "* " + "\n")
        for i in range(b - 2):
            f.write("*" + (" " * (2 * a - 3)) + "*" + "\n")
        f.write(a * "* " + "\n")
        f.close()