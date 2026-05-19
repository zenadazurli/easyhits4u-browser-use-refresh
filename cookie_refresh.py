import asyncio
import os
from browser_use_sdk.v3 import AsyncBrowserUse

async def main():
    api_key = os.environ.get("BROWSER_USE_API_KEY")
    if not api_key:
        raise Exception("Manca BROWSER_USE_API_KEY nell'ambiente")

    client = AsyncBrowserUse(api_key=api_key)
    result = await client.run(
        "Vai su https://www.easyhits4u.com/logon/, "
        "inserisci l'email 'sandrominori50+ulugarecexisa@gmail.com' e la password 'DDnmVV45!!', "
        "clicca login, attendi il redirect e poi restituisci i cookie sesids e user_id."
    )
    print("🎉 Cookie ottenuti:", result.output)

if __name__ == "__main__":
    asyncio.run(main())