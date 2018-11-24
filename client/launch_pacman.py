import subprocess
import sys


def launch():
    subprocess.call("start cmd.exe /c capture.exe", cwd=sys.path[0] + "/PacMan", shell=True)


if __name__ == '__main__':
    launch()
