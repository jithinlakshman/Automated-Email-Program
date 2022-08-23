# Automated-Email-Program
Simple Python program to send emails to different people without much effort

1. Turn On 2-Step Verification
    Before we start writing code, we need to set up our Gmail account to be able to use it with Python.
    In the past, we could easily connect to Gmail with Python by turning on “Less secure app access” but that option isn’t available anymore. 
    What we have to do now is turn on 2-step verification to get a 16-character password that we can use to log in to Gmail using Python.
        -First, go to your Google account, choose the account you want to use for this tutorial, and on the left panel select the option “Security.”
        -Then scroll down until you find the section “Signing in to Google.” Here we need to click on “2-Step Verification.”
        -After this, we’ll see a new page. We have to click on “Get Started”
        -Google will ask to log in again. Then we have to introduce a phone number and click on “Next.” 
        -We’ll get a code to verify our phone number. After we introduce the code.
        -We need to click on “Turn On.”
        -If everything was set up correctly, we’ll see a new page with the message “2-Step Verification is On.”
        -Finally, we need to go to the “App Passwords” section, so go to your Google account again, click on “Security,” scroll down until you find the section “Signing in to Google” and select “App Passwords.”
        -We need to log in again.
        -In the “Select app” dropdown, select “Other (Custom name)” and type any name you want. I’ll name mine “Python” and then click on “Generate”
        -After this, we should see a new page with the 16-character password inside a yellow box.
        -It’s all set! We’ll use this 16-character password to log into our Gmail account with Python.
        -Now you can either copy this password and paste it inside a variable in your Python script or hide the password using environment variables (which I highly recommend you).


2.Creating Environment Variables
    -On Windows, we can hide secret keys using the control panel. To do that, we click on the windows icon and search for the control panel.
    -Then we have to select “System and Security,” click on “System” and select the option “Advanced system settings” that is on the left.
    -The window below will pop up. We need to click on “Environment Variables”
    -Then a new window will pop up. Here we can add any user variable we want by clicking on the “New” button.
    -First, Add the username and then add the password.
    -Then we click “OK” to save. Note that we might need to restart our text editor to get the changes to take effect.

3.Install the requirements.txt ( pip install -r requirements.txt )
4.Add the List of mails to send in the MailingList.xlxs "EMAIL_ID" column.
5.Edit the Subject in Subject.txt
6.Edit the Message in Body.txt
7.Add the attachments (img/pdf) in the same folder.
8.The code is ready to run.
