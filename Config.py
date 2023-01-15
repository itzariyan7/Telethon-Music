import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5892169342:AAETljNfRPooldtve2NKlbWHGVbq8t-i8FA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBu1LR_Yd_glurY1W7nAZnKDMLCGzFdRMsUAEHX0lJOCEdlTfYTZ3mPIy784r8NEXIKrfDOj9YvlW7KQBIAnrRhEgOJ6bspdKR8RQYyLA5lcznFEfiLSJzcGVPus8ruar1hJiHK2qn-t6qp5OX6dd-QSqymWY28DHk5OqQ4XCZSiFMnbCb1eZVMNGPzsuvIiCaBv3yiwG-uPehqhMG_JGLsp8lHx7pwo6jQWcCd8boD0IOjWXUIFpRfDwVg_fk5CszZUfH064k0Msum2n77vNx2139odhzhr4B9jOTh9xmEZ9bcSceOX1JnPSJxSNwFenw5AYwhBhLGeSi8fMTqrUdi-I=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NottyyXMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "SankiWorldMF") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "NixaWorld") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5688281798")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
