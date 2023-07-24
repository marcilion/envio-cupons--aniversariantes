import os
import dotenv
dotenv.load_dotenv()

def get_env(chave:str) -> str | None:
    return os.getenv("chave")