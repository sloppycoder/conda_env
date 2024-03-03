import os
import sys
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print(sys.version)
    print(os.environ["SOME_VAR"])
