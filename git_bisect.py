#!/usr/bin/env python3

# 119cb8fdb041990253cfacbdc828c4c8d3354f55 last made commit
# 7317be75cd6d04c43bd9bd0c444687310449d169 init commit

import os
import subprocess as sb


def checkout_command(hash: str):
    return ["git", "checkout", hash, "-q"]

# path = input("Enter path: ")
# start = input("Enter first commit: ")
# end = input("Enter second commit: ")
# test_command = input("Enter test command: ").split()


path = "/Users/rustamsalimov/Documents/GitHub/ALGs/git_bisect"
start = "7317be75cd6d04c43bd9bd0c444687310449d169"
end = "119cb8fdb041990253cfacbdc828c4c8d3354f55"
test_command = ["./checkfile.py"]

if len(start) < 40:
    format = "%h"
else:
    format = "%H"

log_command = ["git", "log", f'--format="{format}"']

os.chdir(path)
all_commits = sb.run(log_command, capture_output=True)
all_commits = [i.strip('"') for i in all_commits.stdout.decode().split()]
all_commits = all_commits[::-1]

print(all_commits)

if start not in all_commits or end not in all_commits:
    print("Wrong start or(and) end commits")
    exit(1)

l = all_commits.index(start)
r = all_commits.index(end)

while l <= r:
    c = (l + r) // 2

    sb.run(checkout_command(all_commits[c]))
    test_out = sb.run(test_command, capture_output=True)

    print(f"check commit {c}, return code is {test_out.returncode}")

    if test_out.returncode == 0:
        sb.run(checkout_command(all_commits[c + 1]))
        print(f"check commit {c + 1} in case it is the broken")

        if sb.run(test_command, capture_output=True).returncode != 0:
            print(f"The broken commit is: {all_commits[c + 1]}")
            sb.run(checkout_command("master"))
            exit(0)
        else:
            l = c + 1
    else:
        sb.run(checkout_command(all_commits[c - 1]))
        print(f"check commit {c - 1} in case {c} is the broken")

        if sb.run(test_command, capture_output=True).returncode == 0:
            print(f"The broken commit is: {all_commits[c]}")
            sb.run(checkout_command("master"))
            exit(0)
        else:
            r = c - 1

sb.run(checkout_command("master"))
print("OH No something goes wrong")
exit(2)
