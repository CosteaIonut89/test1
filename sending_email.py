import glob
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import shutil
import zipfile
import os

root_path = "D:\Python Projects\StackField"

def clean_folder():
    dir_path = root_path + "/Report/screenshot"
    print(dir_path)
    folder_path = root_path +  "\Report"
    isFolder = os.path.isdir(dir_path)
    if isFolder == True:
        for files in os.listdir(folder_path):
            path = os.path.join(folder_path, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
        print("The specific folder was deleted")
    else:
        print("No folder found")


def create_folder():
    raport_foler_path =root_path +"\Report"
    directory = "screenshot"
    path = os.path.join(raport_foler_path, directory)
    os.mkdir(path)


def move_html():
    testpath = root_path + '/*.html'
    targetpath =root_path + '/Report'
    files = glob.glob(testpath, recursive=True)
    i = 0
    while i < len(files):
        i = i + 1
    for i in files:
        shutil.copy2(i, targetpath)


def move_img():
    testpath = root_path + '\screenshot'
    targetpath = root_path + '/Report/screenshot'
    files = os.listdir(testpath)
    for fname in files:
        # copying the files to the
        # destination directory
        shutil.copy2(os.path.join(testpath, fname), targetpath)


def zipfiletest():
    folder_to_be_zip = "Report"

    with zipfile.ZipFile('report.zip', 'w', zipfile.ZIP_DEFLATED) as newzip:
        for dirpath, dirnames, files in os.walk(folder_to_be_zip):
            for file in files:
                newzip.write(os.path.join(dirpath, file))



def sending_email():
    fromaddr = "inboundtest@stackfield.de"
    toe = ''
    toaddr = " 84e9ba88-6a9c-4c8b-ad1a-e741f71f2691@mail-stackfield.com"
    t = '77bc5afb-dba5-485b-92a8-a10d8ee7fe9a@mail-stackfield.com'
    dt_object = date.today()
    date1 = dt_object.strftime("%d/%m/%Y")
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr
    # storing the subject
    msg['Subject'] = " Test Report " + date1

    # string to store the body of the mail
    body = "Automation Report"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = "report.zip"
    attachment = open(root_path + '/report.zip', "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtps.udag.de', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, '09395a03*')
    # s.login(fromaddr, 'fenhxczljalvpbqz' )

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def delete_folder():
    dir = root_path + '/Report'
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


def delete_screenshots():
    dir = root_path +'\screenshot'
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


if __name__ == "__main__":
    clean_folder()
    create_folder()
    move_html()
    move_img()
    zipfiletest()
    sending_email()
    delete_folder()
    delete_screenshots()
