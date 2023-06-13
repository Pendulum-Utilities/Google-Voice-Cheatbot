# How to install Cheatbot (step by step guide)
### Dependencies:
 - You will first need a [Gmail](https://www.gmail.com) account. It is recommended you create a special email dedicated to Cheatbot.
 - You will need a phone number to get a google voice phone number [here](https://voice.google.com).
 - You need to have the unextracted zip file of Cheatbot on your drive. Get the ZIP [here](https://github.com/Pendulum-Utilities/Google-Voice-Cheatbot/releases/download/Open-Beta/Cheatbot.zip).
 - You will need a phone with a phone number.
 - You will need a bard account. Get one [here](https://bard.google.com).
---
### How to install:

1. Go to google voice [here](https://voice.google.com). Make an account, get a number and contact  
2. Open developer tools by pressing ctrl + shift + i or F12.  **Make sure you're in the elements tab of the dev tools.**
3. In the chat section google voice, find your number.
4. Find this button and click it.
![](https://lh3.googleusercontent.com/pw/AJFCJaXxM97j4DRYGOv0Jp7LJQhaCshFxzsNAVK6-o-r7ZzkxIAZxR-7P7XHloPNui91zb5JpEqPfOnSP-RR6NjTsoeAkaYwGa05zjW_R1QjssGUpL5l_d2i5meFJY0XiGrBRUXZ6N4MVkmZs79cCh3_HKk=w220-h123-s-no)
5.  Hover your mouse on the bottom right corner of the contact it will look something like this if done correctly. **Make sure it looks similar to this and the "Role" says "button."**
![](https://lh3.googleusercontent.com/pw/AJFCJaVNB9Kxqw92FIBK-dHcpz6L07yXjDao-8doweHXImqkFD94iRJ9lSHQT7kaWGCFUpfoFkl3CekffG963GF-dT7Y1uQST_wfg5IFbbg8I-V4_9LMLiyiMm49q3WzJxdUJc7M3pZUJm8tOxOalWuor3c=w319-h283-s-no?authuser=1)
6. In the dev tools, find the text highlighted in blue, then right click it, then find the copy dropdown then copy the full XPATH.
7. Open cheatbot_settings and paste the full XPATH into the empty "" next to PhoneNumberXPATH.
8. Input your Email and Password for your Gmail account associated to the phone number into the empty quotes to each corresponding item in the json.
9. Go back to Bard and open the Developer tools using F12 or ctrl + shift + i.
10. Go to the application tab and then find the cookies dropdown. and find "https://bard.google.com" in the cookies dropdown.
11. Find the __Secure_1PSID cookie value and copy and paste it into the empty quotes next to BardCookie
12. Save the JSON file.
# How to use Bard to cheat.
1. Run the executable inside the extracted ZIP file. (May lag due to PyInstaller)
2. Keep note of the tips printed into the console.
3. Text Bard with your number.
4. Connect a pair of AirPods or Beats to your iphone.
	* If you have an android phone, find something can be used to contact google voice assistant via mini earpiece.
5. Make sure Siri is enabled, and you have set Siris listen time to longest.
6. Disable the PIN on your phone. This is so Siri can read messages aloud and in case the message is too long Siri will not have require you to unlock your phone.
7. Take the AirPod/Beat out of your ear, and then ask Siri to text your bard contact. You can then tell Siri what you want to say.
	* Make sure announce notifications are on or else Siri will not read the message out loud to you.

You're done! If you have followed all these steps correctly, it should work. If you'd like to report any bugs, create an issue.
