import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def run():
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target, exist_ok=True)
    os.chmod(target, 0o755)
    dest = os.path.join(target, "entry.png")
    shutil.copyfile(SRC, dest)
    os.chmod(dest, 0o644)


if __name__ == "__main__":
    run()
