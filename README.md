## Mako, The SMS Calender Application 

## Description
This is a calender app designed to remind the user about events through SMS. Simply put, your phone's default SMS app will be directly used to update your schedule.

## How It Works
Short Message Service (SMS), or more commonly known as text messaging, uses email addresses associated with your carrier to send short emails back and forth. The emails usually consist of a `.txt` file containing your message which is then automatically formatted by your phone into the text bubbles we know and love. An easy example of this: If the phone number 911 were texting `Good Morning!` to the number 555, the exchage between the two will be +1911@carrier_A.com sending an email with a `.txt` file containing `Good Morning!` to +1555@carrer_B.net. The phone's messaging app would then strip the `.txt` file, and format it into a text bubble on your phone screen.
This program builds off of this concept, and uses a free Gmail account linked to a Google Voice number. The Google Voice number forwards each text message to the gmail account. From there, the script uses `imaplib` to read the information, then uses `smtplib` to send a response. A simple calendar app is sandwiched between the two functions to create a working program that has two-way communication with the user's phone.

This is a basic flowchart of how the program works:
![alt text](https://github.com/maguea/mako/blob/main/images/mako_flowcart.png)

## User Instructions
This program uses a gmail account as a host, and it is best to create a new one since using your main one will result in deleted emails. From there, attach a Google Voice number to your email, and click the "Forward messages to email" option under "Messages" in your settings.
From there, send a quick text to your Google Voice number using your phone, and check your email for the admin address. This address will look like the following: `15556667777.12223334444.letters@txt.voice.google.com`.
After downloading the repo, install `dotenv`
```cmd
pip install python-dotenv
```
Create a file titled `.env` where you will define
```cmd
ADMIN_ADDRESS = "15556667777.12223334444.letters@txt.voice.google.com" #(From previous step)
RECEIVER_EMAIL = "examplehost@gmail.com"
RECEIVER_PASS = "password123"
```
From there, run the program on a server of your choice.
-maguea