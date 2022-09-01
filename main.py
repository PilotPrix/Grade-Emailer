import emailer
from time import sleep

with open("Grade-Emailer/data.txt", "r") as f:
    data = f.read().split("\n")

# remove whitespace
alias = data[0].split(":")[1].strip()
fmEmail = data[1].split(":")[1].strip()
password = data[2].split(":")[1].strip()

emailSubject = data[4].split(":")[1].strip()
emailBody = ""
for i in range(6, len(data)):
    emailBody += data[i] + "\n"
emailBody = emailBody.strip()

print("Welcome to the Grade-Emailer program! Make sure to check out the README.md file if you haven't already.\n")
sleep(3)
print("Please confirm the following information below is accurate")
print("Alias: " + alias)
print("From email: " + fmEmail)
print("Password: " + password)
print("Subject: " + emailSubject)
print("Body:")
print("------------------------------------------------------")
print(emailBody)
print("------------------------------------------------------")
input("Press enter to continue or press ctrl+c to exit: ")

# Get spreadsheet input
userInput = None
spreadsheetData = []
print("\nFrom the spreadsheet, copy the contents and paste them here in the console (without the headings), then press enter twice:")
while True:
    userInput = input()
    if userInput != "":
        spreadsheetData.append(userInput.split("\t"))
    else:
        break

# Send emails
print("Sending emails...")
for spreadsheetRow in spreadsheetData:
    # Get email and signature
    toEmail = spreadsheetRow[1]
    # Replace placeholders
    emailBodytmp = emailBody.replace("$STUDENT", spreadsheetRow[0])
    emailBodytmp = emailBodytmp.replace("$MARK", spreadsheetRow[2])
    # Send email
    sleep(5)
    emailer.sendEmail(fromaddr=fmEmail, name=alias, password=password, to=toEmail, subject=emailSubject, content=emailBodytmp)
    print(f"Email sent to {toEmail}")