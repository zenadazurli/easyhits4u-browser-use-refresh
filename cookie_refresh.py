import asyncio
import os
from browser_use_sdk.v3 import AsyncBrowserUse
from supabase import create_client

# LISTA COMPLETA DEGLI ACCOUNT (38)
ACCOUNTS = [
    {"email": "sandrominori50+ulugarecexisa@gmail.com", "password": "DDnmVV45!!", "name": "ulugarecexisa"},
    {"email": "sandrominori50+ukageluli@gmail.com", "password": "DDnmVV45!!", "name": "ukageluli"},
    {"email": "sandrominori50+ukaxiloki@gmail.com", "password": "DDnmVV45!!", "name": "ukaxiloki"},
    {"email": "sandrominori50+uchikilaremu@gmail.com", "password": "DDnmVV45!!", "name": "uchikilaremu"},
    {"email": "sandrominori50+ufrrmncrachinora@gmail.com", "password": "DDnmVV45!!", "name": "ufrrmncrachinora"},
    {"email": "sandrominori50+unenomasagebebe@gmail.com", "password": "DDnmVV45!!", "name": "unenomasagebebe"},
    {"email": "sandrominori50+uisnrnafwttvvceer@gmail.com", "password": "DDnmVV45!!", "name": "uisnrnafwttvvceer"},
    {"email": "sandrominori50+ujuenpaorgl@gmail.com", "password": "DDnmVV45!!", "name": "ujuenpaorgl"},
    {"email": "sandrominori50+uvuoobe@gmail.com", "password": "DDnmVV45!!", "name": "uvuoobe"},
    {"email": "sandrominori50+uoovoge@gmail.com", "password": "DDnmVV45!!", "name": "uoovoge"},
    {"email": "sandrominori50+ukafifoko@gmail.com", "password": "DDnmVV45!!", "name": "ukafifoko"},
    {"email": "sandrominori50+ubozogaza@gmail.com", "password": "DDnmVV45!!", "name": "ubozogaza"},
    {"email": "sandrominori50+udapasa@gmail.com", "password": "DDnmVV45!!", "name": "udapasa"},
    {"email": "sandrominori50+uluglqupgbe@gmail.com", "password": "DDnmVV45!!", "name": "uluglqupgbe"},
    {"email": "sandrominori50+unaglbene@gmail.com", "password": "DDnmVV45!!", "name": "unaglbene"},
    {"email": "sandrominori50+umachizo@gmail.com", "password": "DDnmVV45!!", "name": "umachizo"},
    {"email": "sandrominori50+ulaaacummgl@gmail.com", "password": "DDnmVV45!!", "name": "ulaaacummgl"},
    {"email": "sandrominori50+ufrrageboki@gmail.com", "password": "DDnmVV45!!", "name": "ufrrageboki"},
    {"email": "sandrominori50+unomama@gmail.com", "password": "DDnmVV45!!", "name": "unomama"},
    {"email": "sandrominori50+ucuquaacuge@gmail.com", "password": "DDnmVV45!!", "name": "ucuquaacuge"},
    {"email": "sandrominori50+ukufeno@gmail.com", "password": "DDnmVV45!!", "name": "ukufeno"},
    {"email": "sandrominori50+ukitulobbqu@gmail.com", "password": "DDnmVV45!!", "name": "ukitulobbqu"},
    {"email": "sandrominori50+udaglkilerm@gmail.com", "password": "DDnmVV45!!", "name": "udaglkilerm"},
    {"email": "sandrominori50+usaadgapa@gmail.com", "password": "DDnmVV45!!", "name": "usaadgapa"},
    {"email": "sandrominori50+uqumopgne@gmail.com", "password": "DDnmVV45!!", "name": "uqumopgne"},
    {"email": "sandrominori50+upgximamazo@gmail.com", "password": "DDnmVV45!!", "name": "upgximamazo"},
    {"email": "sandrominori50+uboooggnale@gmail.com", "password": "DDnmVV45!!", "name": "uboooggnale"},
    {"email": "sandrominori50+uenqufetr@gmail.com", "password": "DDnmVV45!!", "name": "uenqufetr"},
    {"email": "sandrominori50+umumure@gmail.com", "password": "DDnmVV45!!", "name": "umumure"},
    {"email": "sandrominori50+udabbpgnc@gmail.com", "password": "DDnmVV45!!", "name": "udabbpgnc"},
    {"email": "sandrominori50+uquliufnemu@gmail.com", "password": "DDnmVV45!!", "name": "uquliufnemu"},
    {"email": "sandrominori50+ukikreazala@gmail.com", "password": "DDnmVV45!!", "name": "ukikreazala"},
    {"email": "sandrominori50+ulibbra@gmail.com", "password": "DDnmVV45!!", "name": "ulibbra"},
    {"email": "sandrominori50+uzarawalita@gmail.com", "password": "DDnmVV45!!", "name": "uzarawalita"},
    {"email": "sandrominori50+ufitamina@gmail.com", "password": "DDnmVV45!!", "name": "ufitamina"},
    {"email": "sandrominori50+utamavocuaa@gmail.com", "password": "DDnmVV45!!", "name": "utamavocuaa"},
    {"email": "sandrominori50+uzomukibobb@gmail.com", "password": "DDnmVV45!!", "name": "uzomukibobb"},
    {"email": "sandrominori50+urepgla@gmail.com", "password": "DDnmVV45!!", "name": "urepgla"},
    {"email": "sandrominori50+ujupgpaoo@gmail.com", "password": "DDnmVV45!!", "name": "ujupgpaoo"},
]

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

async def refresh_one(api_key, email, password, name):
    client = AsyncBrowserUse(api_key=api_key)
    result = await client.run(
        f"Vai su https://www.easyhits4u.com/logon/, "
        f"fai login con email '{email}' e password '{password}', "
        f"attendi il redirect e restituisci i cookie 'sesids' e 'user_id' "
        f"nel formato esatto: sesids=VALORE; user_id=VALORE"
    )
    output = result.output
    try:
        sesids = output.split("sesids=")[1].split(";")[0].strip()
        user_id = output.split("user_id=")[1].strip()
    except:
        raise Exception(f"Formato inaspettato: {output}")
    return sesids, user_id

async def main():
    api_key = os.environ.get("BROWSER_USE_API_KEY")
    if not api_key:
        raise Exception("Manca BROWSER_USE_API_KEY")
    
    while True:
        print("🔄 Avvio ciclo refresh cookie...")
        for acc in ACCOUNTS:
            try:
                sesids, user_id = await refresh_one(api_key, acc["email"], acc["password"], acc["name"])
                cookie_string = f"sesids={sesids}; user_id={user_id}"
                supabase.table("account_cookies").upsert({
                    "email": acc["email"],
                    "account_name": acc["name"],
                    "cookies_string": cookie_string,
                    "status": "active"
                }).execute()
                print(f"✅ {acc['name']} cookie aggiornato")
            except Exception as e:
                print(f"❌ {acc['name']} errore: {e}")
            await asyncio.sleep(2)
        print("✅ Ciclo completato. Attendo 3 ore...")
        await asyncio.sleep(10800)

if __name__ == "__main__":
    asyncio.run(main())
