## Mako, The SMS Calender Application 

## Description
This is a calender app designed to remind the user about events through SMS. Simply put, your phone's default SMS app will be directly used to update your schedule.

## How It Works
Short Message Service (SMS), or more commonly known as text messaging, uses email addresses associated with your carrier to send short emails back and forth. The emails usually consist of a `.txt` file containing your message which is then automatically formatted by your phone into the text bubbles on your screen. An easy example of this: If the phone number 911 were texting `Good Morning!` to the number 555, the exchage between the two will be 911@carrier.com sending an email with a `.txt` file containing `Good Morning!` to 555@carrer.net. The phone's messaging app would then strip the `.txt` file for the message, and format it into a text bubble on your phone screen.
This program builds off of this concept, and uses a free Gmail account linked to a Google Voice number. The Google Voice number forwards each text message to the gmail account. From there, the script uses `imaplib` to read the information, then uses `smtplib` to send a response. A simple calendar app is sandwiched between the two functions to create a working program that has two-way communication with the user's phone.

This is a basic flowchart of how the program works:
![alt text](https://github.com/maguea/mako/blob/main/images/mako_flowcart.png)

Admin commands include:
```cmd
"add": intended to add an event
"remove": intended to remove an event
"get": intended to get a .jpg of detailed schedule
"block": intended to block a user with given address
"name": intended to change name of user with given address
```
Guest commands include
```cmd
"request": intended for a guest to request a meeting time (Confirmation from admin requried)
"cancel": intended for a guest to cancel a meeting time
"see": intended to send a .jpg schedule to show just available and unavailable time
```
To add to any of these lists, add to the function dictionary (No `switch` or `elif` statements used).

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

## Important
THIS PROGRAM CAN NOT BE USED TO INITIATE FIRST CONTACT. You must have someone text it with their first and last name for two-way communication to work. For official use, link a proper consent form in `commands.py` in `def new_number`.

## References
YouTube @NeuralNine: https://www.youtube.com/watch?v=4iMZUhkpWAc&t=695s
