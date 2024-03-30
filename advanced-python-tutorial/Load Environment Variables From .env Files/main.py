# pip install python-dotenv

import os
from dotenv import load_dotenv, dotenv_values

load_dotenv(override=True)

print(os.getenv("MY_SECRET_KEY"))
print(dotenv_values(".env"))
