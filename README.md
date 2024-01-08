# New_Music_Compilation
A python program that runs weekly to create a new music playlist

As a music lover, every weekend I have to manually go through different New Music playlists on Spotify to find newly released gems. Using this program, I want to automate this process. 

## Setup
Create a .env file to store your Spotify Client_ID and Client_Secret. To get these, create an app in the Spotify Developer dashboard. 
Run `pip install python-dotenv` if you haven't already. 
Ensure the Redirect URL matches the one in your Spotify app as well. 

In `script.py`:
- Feel free to change the name of the new playlist in line 53.
- I included the playlists I typically go through in the script but this will be updated as I find more in the future. You can modify these playlist IDs to use the playlist IDs you want.

## Automation
To ensure this script runs periodically, every Saturday morning for me, I created a Basic Task in Task Scheduler. The steps were:
1. **Open Task Scheduler:** Search for 'Task Scheduler' in the Start menu and open it
2. **Create a Basic Task:** Click on **Create a Basic Task** in the right panel
3. **Set Trigger:** Choose **Weekly**, select Saturday, and set the start time (e.g. 12:00:00 AM)
4. **Set Action:** Choose **Start a Program**, then browse and select your Python interpreter (python3.11.exe in my case) and the script file
5. **Finish**: Review the settings and click **Finish**

Happy Listening!