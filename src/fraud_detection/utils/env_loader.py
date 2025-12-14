from pathlib import Path
from dotenv import load_dotenv


def load_environment():

    current_file = Path(__file__).resolve()
    root_dir = next(p for p in current_file.parents if (p / ".env").exists())


    load_dotenv(root_dir / ".env")    

