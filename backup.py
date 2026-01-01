import shutil 
import datetime
import os

def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)

source = r"C:\Users\harsh\Desktop\Python-For-Devops\day-01\practice"
destination = r"C:\Users\harsh\Desktop\Python-For-Devops\day-01\practice\backups"
backup_files(source,destination)
