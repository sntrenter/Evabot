import asyncio
from twikit import Client
from account_info import username, password, email
from GetImages import Videos, Video

USERNAME = username
EMAIL = email
PASSWORD = password

# Initialize client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD,
        cookies_file='cookies.json'
    )

    ############################
    media_ids = [
        await client.upload_media("test_images/1.jpg"),
        await client.upload_media("test_images/2.PNG"),
        await client.upload_media("test_images/3.jpg"),
        await client.upload_media("test_images/4.jpg"),
    ]
    await client.create_tweet("maymay",media_ids=media_ids)

asyncio.run(main())