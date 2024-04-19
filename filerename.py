import os

if not os.path.exists("Dest Dir"):
    os.mkdir("Dest Dir")

os.rename("New Dir/renamed.txt", "Dest Dir/renamed-moved.txt")
