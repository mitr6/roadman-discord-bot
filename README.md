# 🤖 Roadman Bot (Classic)

A complete recreation of the Discord bot used between January and March 2022. This bot features a custom prefix system, moderation tools, music integration, and a classic embed style.

> [!IMPORTANT]  
> **Last Project Update:** March 8, 2022

---

## 📋 Command Overview

### **Moderation**
* `kick` - Remove a member from the server.
* `ban` / `unban` - Manage permanent server bans.
* `mute` / `unmute` - Restrict messaging permissions (via Muted role).
* `purge` - Bulk delete messages from a channel.
* `lock` / `unlock` - Toggle channel write permissions.

### **Music**
* `join` / `leave` - Connect/Disconnect bot from voice.
* `play` - Stream audio into the voice channel.
* `pause` / `resume` - Control audio playback.

### **Others (No Category)**
* `avatar` - Shows a user's profile picture.
* `botinfo` / `serverinfo` - Technical details about the bot and guild.
* `dsay` - Recovers and displays the last deleted message (Snipe).
* `uptime` - Shows how long the bot has been running.
* `ping` - Check API latency.
* `support` - Provides the link to the support server.

---

## 🛠️ Installation & Setup

1. **Requirements:**
   - Python 3.8+
   - `discord.py` library

2. **Install Dependencies:**
   ```bash
   pip install discord.py yt-dlp PyNaCl
