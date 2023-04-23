from download import *
import coloredlogs, logging
import datetime

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

today = time.strftime("%d%m%Y")
downloadDir = str(Path.home() / "Downloads")
datafeedDir = downloadDir+'/'+today

def main():
   menu = True
   while menu:
      print(20*"-","CX Computer Superstore - Automated Invoice Downloader - Version 1.1",20*"-")
      print("1. Download Leader Invoices")
      print("2. Download 4Cabling Invoices")
      print("3. Download Ingram Invoices")
      print("4. Download Dynamic Invoices")
      print("5. Download Powerhouse Invoices")
      print("6. Download DickerData Invoices")
      print("7. Download Hyka Invoices")
      print("8. Download Multimedia Invoices")
      print("9. Download Austronic Invoices")
      print("10. Download Anixter Invoices")
      print("11. Download Force Invoices")
      print("20. Exit")
      print(79*"-")
      choice=int(input("Enter your choice [1-20]:"))

      if choice == 1:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading Leader Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_leader(startDate, endDate)
                subMenu = False
                subMenu2 = False
      
      if choice == 2:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading 4CABLING Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_4cabling(startDate, endDate)
                subMenu = False
                subMenu2 = False

      if choice == 3:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading INGRAM Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_ingram(startDate, endDate)
                subMenu = False
                subMenu2 = False

      if choice == 4:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading DYNAMIC Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_dynamic(startDate, endDate)
                subMenu = False
                subMenu2 = False

      if choice == 5:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading POWERHOUSEPC Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_powerhouse(startDate, endDate)
                subMenu = False
                subMenu2 = False

      if choice == 6:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading DICKERDATA Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_dicker(startDate, endDate)
                subMenu = False
                subMenu2 = False

      if choice == 7:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading HYKA Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_hyka(startDate, endDate)
                subMenu = False
                subMenu2 = False

      if choice == 8:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading MMT Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_mmt(startDate, endDate)
                subMenu = False
                subMenu2 = False

      if choice == 9:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading Austronic Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_austronic(startDate, endDate)
                subMenu = False
                subMenu2 = False

      if choice == 10:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading Anixter Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_anixter(startDate, endDate)
                subMenu = False
                subMenu2 = False

      if choice == 11:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading Force Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_force(startDate, endDate)
                subMenu = False
                subMenu2 = False

      elif choice==20:
         menu = False
      else:
         print("Wrong Choice")

if __name__ == "__main__":
    main()
