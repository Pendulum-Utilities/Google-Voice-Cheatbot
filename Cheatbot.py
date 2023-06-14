from time import sleep
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.remote.webdriver import By
from Bard import Chatbot
from colorama import init, Fore, Style
import undetected_chromedriver as uc
import configparser
import logging
import sys
import threading

# Settings
config = configparser.ConfigParser()
config.read('settings.ini')

Email = config.get('DEFAULT', 'Email')
Password = config.get('DEFAULT', 'Password')
BardCookie = config.get('DEFAULT', 'BardCookie')
PhoneNumber = config.get('DEFAULT', 'PhoneNumber')
#check if any of the variables are empty
if Email == '' or Password == '' or BardCookie == '' or PhoneNumber == '':
    input(Fore.RED + 'ERROR: Please fill in the settings.ini file. See README.txt for a guide on how set it up. Press enter to continue...' + Fore.RESET)
    sys.exit()

config.clear()
# Logging
logging.basicConfig(level=logging.ERROR)
LOGGER.setLevel(logging.ERROR)

# Chrome options
options = uc.ChromeOptions()
options.add_argument("--headless=chrome")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--log-level=3')

# Start everything.
driver = uc.Chrome(options=options)
driver.get("https://voice.google.com/")
bard = Chatbot(BardCookie)

# Functions
def click_xpath(xpath):
    driver.find_element(By.XPATH, xpath).click()
def keys_xpath(xpath, keys):
    driver.find_element(By.XPATH, xpath).send_keys(keys)
def typewriter_effect(text, delay=0.04):
    init()  # Initialize colorama
    sys.stdout.write(Fore.LIGHTGREEN_EX)  # Set text color to green

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Flush the output buffer
        sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.write(Style.RESET_ALL)  # Reset text color to default
    sys.stdout.flush()  # Flush the output bufferdef typewriter_effect(text, delay=0.04):
def T_Print(text, delay=0.05):
    threading.Thread(target=typewriter_effect, args=(text, delay)).start()

# Main program
T_Print("Welcome to the CheatBot!\n\nCreated by CROAXER#8683\n\nLogging into google... Please wait...")
click_xpath('//*[@id="header"]/div[2]/a[2]')
# Input email:
keys_xpath('//*[@id="identifierId"]', Email)
# Next:
sleep(2) # doesnt detect for some reason
click_xpath('//*[@id="identifierNext"]/div/button/span')
sleep(5)
# Input password:
keys_xpath('//*[@id="password"]/div[1]/div/div[1]/input', Password)
sleep(5)
# next:
click_xpath('//*[@id="passwordNext"]/div/button/span')
T_Print("Sucessfully logged into google. Connecting to google voice...")
# next:
sleep(5)
try:
    click_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[4]/div[1]/button/span')
except:
    ...
# Go to messages to start the main process.
sleep(1)
click_xpath('//*[@id="gvPageRoot"]/div[2]/gv-side-panel/mat-sidenav-container/mat-sidenav-content/div/div[2]/gv-side-nav/div/div/gmat-nav-list/a[2]/div')
sleep(2)
T_Print("Connected! Almost done...")
click_xpath("//*[contains(text(), '" + PhoneNumber + "')]")
sleep(2)

# Main loop:
elements = driver.find_elements(By.XPATH, '//gv-annotation[@aria-hidden="true" and @class="content ng-star-inserted"]')
old_text = ""
for element in elements:
    old_text += element.text + "\n"
T_Print("""
Cheatbot has been activated! You can now send a text to cheatbot. However, here are some useful tips you should ALWAYS keep in mind whenever using it.

1. Wait for cheatbot to respond to the question. Don't send any other messages because that will cause an error. 
No matter how long it takes, it will answer the question. If it doesn't, reload the script using a remote access software.

2. Cheatbot is a valuable asset outside of being a 'cheatbot'. It could technically be used as a someone you can text on the go.

3. Cheatbot may get noticeably slower responses if you ask a lot of questions. This is a google voice problem and is out of our control.

4. Cheatbot is currently in open beta and may not work as intended.

5. Cheatbot will be recieving further updates in the future and nothing is finalized until Cheatbot is rolled out of public beta.

6. Cheatbot is not affiliated with google, or any other outside coorperations.

7. Cheatbot is a last resort if the internet cannot be accessed by any other means. Its very hard for voice recognition softwares to hear whispering, so do not have high hopes that its perfect.

8. Have fun, and share your friends cheatbot. They'll like it and you'll be better friends with them (Unless they don't have the balls to cheat or just enjoy learning.)

9. Do not spam messages to cheatbot. Cheatbot will not be able to respond to your own messages and will get overwhelemed with the amount of messages you've sent.

10. For the best results, pretend like its ChatGPT. Wait until Cheatbot is done talking then send back a response. There is no actual way to prevent this.

Thank you once again for using cheatbot. I really hope you enjoy it :).

https://discord.gg/4nk2xMfdtm
""", .0001)
while True:
    try:
        elements = driver.find_elements(By.XPATH, '//gv-annotation[@aria-hidden="true" and @class="content ng-star-inserted"]')
        new_text = ""

        # Construct the new text
        for element in elements:
            new_text += element.text + "\n"

        if new_text != old_text:
            BardQuestion = new_text.replace(old_text, "")
            T_Print(BardQuestion, 0.001)
            BardAnswer = bard.ask("Keep your answers as short as possible. Also do not show steps to math problems and just say the answer and absolutely nothing else. It is being read aloud by a TTS engine, so the user must hear it correctly! The TTS engine cannot interpret symbols. . Example: 'the answer is x = 5. Repeat, the answer is x = 5. If the user asks you to repeat your answer, repeat the answer with each repetition being seperated with periods. Also, keep your answers extremely short. Make them as short as you can possibly make them. Don't give any extra info if the user didn't ask for any, espically if it makes your responses long. With all that being said, here is the users question. Remember don't bring up anything I said before.: " + BardQuestion)["content"].replace("\n", " ").replace("-", " negative ")
            T_Print(BardAnswer, 0.001)
            driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/gv-side-panel/mat-sidenav-container/mat-sidenav-content/div/div[2]/div/gv-messaging-view/div/div/md-content/gv-thread-details/div/div[2]/gv-message-entry/div/div[2]/md-input-container/textarea').send_keys(BardAnswer)
            click_xpath('//*[@id="ib2"]')
            sleep(3)
            T_Print("Message sent successfully.")
            elements = driver.find_elements(By.XPATH, '//gv-annotation[@aria-hidden="true" and @class="content ng-star-inserted"]')
            old_text = ""
            for element in elements:
                old_text += element.text + "\n"
    except:
        T_Print("Something went wrong. Retrying in 3 seconds...")
        sleep(3)
        continue

    sleep(1)
