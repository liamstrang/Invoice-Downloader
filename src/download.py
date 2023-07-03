import os
import traceback
import time
from imap_tools import MailBox, A
import datetime
from pathlib import Path
import coloredlogs, logging
import re

import getenv

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

today = time.strftime("%d%m%Y")
downloadDir = str(Path.home() / "Downloads")

host = getenv.EMAIL_HOST

username_receiving = getenv.EMAIL_USER_RECEIVING
password_receiving = getenv.EMAIL_PASS_RECEIVING

username_receivable = getenv.EMAIL_USER_RECEIVABLE
password_receivable = getenv.EMAIL_PASS_RECEIVABLE

download_folder = downloadDir+'/'+today

if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)
    
    
#ADD NEWMAGIC, BLUECHIP, COMSOL

def download_leader(startDate, endDate):
    print(30*"-")
    logger.critical("LEADER INVOICES")
    print(30*"-")

    query = A(from_='ar@leadersystems.com.au', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/leader"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_4cabling(startDate, endDate):
    print(30*"-")
    logger.critical("4CABLING INVOICES")
    print(30*"-")

    query = A(from_='invoices@4cabling.com.au', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/4cabling"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_ingram(startDate, endDate):
    print(30*"-")
    logger.critical("INGRAM INVOICES")
    print(30*"-")

    query = A(from_='Maricar.Adem@ingrammicro.com', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/ingram"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_dynamic(startDate, endDate):
    print(30*"-")
    logger.critical("DYNAMIC INVOICES")
    print(30*"-")

    query = A(from_='notifications@ds.net.au', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/octet-stream"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/dynamic"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_powerhouse(startDate, endDate):
    print(30*"-")
    logger.critical("POWERHOUSE INVOICES")
    print(30*"-")

    query = A(from_='henry@powerhousepc.com.au', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = re.search(r'P\d{7}$', msg.subject).group(0)
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/powerhouse"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail+".pdf", 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_dicker(startDate, endDate):
    print(30*"-")
    logger.critical("DICKERDATA INVOICES")
    print(30*"-")

    query = A(from_='noreply@dickerdata.com.au', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/octet-stream"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/dicker"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_hyka(startDate, endDate):
    print(30*"-")
    logger.critical("HYKA INVOICES")
    print(30*"-")

    query = A(text='invoice from hyka', from_='groupaccounts@cx.com.au', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/hyka"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_mmt(startDate, endDate):
    print(30*"-")
    logger.critical("MULTIMEDIA INVOICES")
    print(30*"-")

    query = A(from_='cs@mmt.com.au', subject='MMT Invoice', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/multimedia"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_mmt(startDate, endDate):
    print(30*"-")
    logger.critical("MULTIMEDIA INVOICES")
    print(30*"-")

    query = A(from_='cs@mmt.com.au', subject='MMT Invoice', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/multimedia"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_austronic(startDate, endDate):
    print(30*"-")
    logger.critical("AUSTRONIC INVOICES")
    print(30*"-")

    query = A(from_='dispatch@computercables.com.au', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/austronic"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_anixter(startDate, endDate):
    print(30*"-")
    logger.critical("ANIXTER INVOICES")
    print(30*"-")

    query = A(from_='eInvoice_Notification@anixter.com', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/anixter"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_force(startDate, endDate):
    print(30*"-")
    logger.critical("FORCE INVOICES")
    print(30*"-")

    query = A(from_='accounts@forcetechnology.com.au', subject='Force Technology International Invoices', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/octet-stream"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/force"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_alloys(startDate, endDate):
    print(30*"-")
    logger.critical("ALLOYS INVOICES")
    print(30*"-")

    query = A(from_='orders@alloys.com.au', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receivable, password_receivable, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receivable)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/alloys"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_bluechip(startDate, endDate):
    print(30*"-")
    logger.critical("BLUECHIP INVOICES")
    print(30*"-")

    query = A(from_='statements@bluechipit.com.au', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/octet-stream"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/bluechip"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_comsol(startDate, endDate):
    print(30*"-")
    logger.critical("COMSOL INVOICES")
    print(30*"-")

    query = A(from_='system@sent-via.netsuite.com', subject='Comsol Invoice', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/comsol"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_streakwave(startDate, endDate):
    print(30*"-")
    logger.critical("STREAKWAVE INVOICES")
    print(30*"-")

    query = A(subject='Streakwave Pty Ltd Invoice', date_gte=datetime.date(startDate.year, startDate.month, startDate.day), date_lt=datetime.date(endDate.year, endDate.month, endDate.day), seen=False)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/streakwave"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

def download_manual(input):
    print(30*"-")
    logger.critical("MANUAL INVOICE DOWNLOAD")
    print(30*"-")

    query = A(text=input)
    with MailBox(host).login(username_receiving, password_receiving, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receiving)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf" or att.content_type == "application/octet-stream"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/manual"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())

    with MailBox(host).login(username_receivable, password_receivable, 'Inbox') as mailbox:
        logger.warning("Logged Into: "+username_receivable)
        for msg in mailbox.fetch(query, mark_seen=True):
            for att in msg.attachments:
                if(att.content_type == "application/pdf" or att.content_type == "application/octet-stream"):
                    subjectEmail = att.filename
                    logger.debug("Downloading: "+subjectEmail+" Date: "+msg.date_str)
                    try:
                        download_path = f"{download_folder}/manual"
                        if not os.path.isdir(download_path):
                            os.makedirs(download_path, exist_ok=True)
                        open(download_path+"/"+subjectEmail, 'wb').write(att.payload)
                    except:
                        print(traceback.print_exc())