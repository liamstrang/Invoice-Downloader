from download import *
from merge import *
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
      print("12. Download Alloys Invoices")
      print("13. Download Bluechip Invoices")
      print("14. Download Comsol Invoices")
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/leader", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/4cabling", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/ingram", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/dynamic", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/powerhouse", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/dicker", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/hyka", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/multimedia", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/austronic", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/anixter", mergeChoice)
                   mergeMenu = False
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
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/force", mergeChoice)
                   mergeMenu = False
                subMenu = False
                subMenu2 = False
      
      if choice == 12:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading Alloys Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_alloys(startDate, endDate)
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/alloys", mergeChoice)
                   mergeMenu = False
                subMenu = False
                subMenu2 = False

      if choice == 13:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading Bluechip Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_bluechip(startDate, endDate)
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/bluechip", mergeChoice)
                   mergeMenu = False
                subMenu = False
                subMenu2 = False

      if choice == 14:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading Comsol Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_comsol(startDate, endDate)
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/comsol", mergeChoice)
                   mergeMenu = False
                subMenu = False
                subMenu2 = False

      if choice == 15:
         subMenu = True
         while subMenu:
            subChoice=input("Enter the START date for the download (eg: 18/04/2022): ")
            subMenu2 = True
            while subMenu2:
                subChoice2=input("Enter the END date for the download (eg: 25/04/2022): ")
                startDate = datetime.datetime.strptime(subChoice, "%d/%m/%Y")
                endDate = datetime.datetime.strptime(subChoice2, "%d/%m/%Y")
                logger.debug("Downloading Streakwave Invoices - Starting: "+subChoice+" Ending: "+subChoice2)
                download_streakwave(startDate, endDate)
                mergeMenu = True
                while mergeMenu:
                   mergeChoice=input("Do you want to merge the downloaded invoices (Y or N): ")
                   merge(datafeedDir+"/streakwave", mergeChoice)
                   mergeMenu = False
                subMenu = False
                subMenu2 = False

      elif choice==20:
         menu = False
      else:
         print("Wrong Choice")

if __name__ == "__main__":
    main()
