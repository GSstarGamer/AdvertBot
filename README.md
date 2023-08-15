# AdvertBot: Automate Your Discord Messages

**Simplify Your Discord Messaging**

AdvertBot is an easy-to-use solution for automating your Discord messages. Whether you're promoting your community, products, or just sharing information, AdvertBot has you covered. Here's how to get started:

## Installation

1.  Install the required packages:
    -   `discord.py-self`: `pip install discord.py-self`
    -   `requests`: Install it if you don't have it already with `pip install requests`
    -   `Flask`: `pip install flask` if you want 24/7 replit. BUT this should already be there.

## Configuration

1.  Open the configuration file.
2.  Insert your Discord token and channel IDs.

## Customization

-   Adjust the loop delay to control the frequency of message sending.
-   Customize the message content by editing the `message.txt` file.
-   If you prefer to use a different text file, update the `messagePath` in the configuration.

## Understanding Delays

-   `loopDelay`: Set the delay between sending messages, allowing for controlled pacing.
-   `itterDelay`: Define the interval between sending messages to different channels.

## Auto-Reply Feature

-   Utilize the `autoReply` feature for periods when you're unavailable, automatically responding with a preset message.
-   Configure the `autoReplyMessage` to tailor the auto-reply to your preferences.

## Advantages of AdvertBot

-   **Simplicity**: Designed with user-friendliness in mind, AdvertBot streamlines the process of automating Discord messages.
-   **Smart Cooldown**: AdvertBot intelligently manages cooldowns to avoid rate limits, preventing the same channel from receiving messages until the cooldown period ends.
-   **Dynamic Channel Management**: If a channel is no longer available, AdvertBot automatically removes it from the list, further avoiding rate limits.
-   **Auto message update**: When message changed in file. It updates instantly, without having to reload script.

Discover the convenience of AdvertBot – automation made simple. Created with care to elevate your Discord messaging experience.

dawg i hate typing so i used chatGPT sorry lol
if you got any questions add me on discord `gs._` or post a problem
**ALSO THIS IS AGAINST DISCORDS TOS, SO DONT BLAME ME IF YALL GET BANNED**
