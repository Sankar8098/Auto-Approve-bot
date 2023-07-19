from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23990433"))
    API_HASH = getenv("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
    BOT_TOKEN = getenv("BOT_TOKEN", "6324395748:AAGU-qGihOAcRgrxfdccuyySk7ST6hko4MU")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", ""))
    SUDO = list(map(int, getenv("SUDO").split(5821871362)))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sankarbio8098:sankar@cluster0.5gfezqj.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
