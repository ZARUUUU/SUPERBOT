import sys

from telethon import TelegramClient
from telethon.sessions import StringSession

STRING_SESSION = "BQAxSFWK7SGbivX5vRcnzmxDI5sD09SwImOfB5DBKa_UYwE0o9DNNTzmrubMkOerE_O39VcBj231AMYSSOVTWZgwUM-smdqoseJDWah1xw7VwdM_pmTmo4gMvaVAwhMYDRus1VvzSjdBuTF4-Rjzc8LANJPPmmP5FCI8flN_Ul4mew1WkGzEIVAUBoQvDs9Vqlwx0xtW_Akc07e1Qdhz_n7sb-S5YfWoE4oC8gtXwDIBli-s8MuP0nyarFotea66Aso3tV4yN5J6EAKddAPGC3bJ7TRS6ckjlduNroJvSWL6QJ_neGzmYGv0X4hKLXwPAhGBmFtWx9sEeA1r_qO32Pj4a21KgQA"
API_ID = 4161078
API_HASH = "005968599cf426c7cefe134e1b5a91d6"

ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
try:
    ubot.start()
except BaseException:
    print("Userbot Error ! Have you added a STRING_SESSION in deploying??")
    sys.exit(1)
