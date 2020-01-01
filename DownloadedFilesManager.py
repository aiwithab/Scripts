import os
import shutil

path = '/home/aiwithab/Downloads/'
names = os.listdir(path)
folder_name = ['Images', 'Audio', 'Videos', 'Documents', 'Softwares']
       
for x in range(0,5):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for files in  names:
    if ".svg" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
    if ".jpg" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
    if ".jpeg" in files and not os.path.exists(path+'Images/'+files):
        shutil.move(path+files, path+'Images/'+files)
    
    if ".mp3" in files and not os.path.exists(path+'Audio/'+files):
        shutil.move(path+files, path+'Audio/'+files)
    if ".m4a" in files and not os.path.exists(path+'Audio/'+files):
        shutil.move(path+files, path+'Audio/'+files)

    if ".mp4" in files and not os.path.exists(path+'Videos/'+files):
        shutil.move(path+files, path+'Videos/'+files)
    if ".mkv" in files and not os.path.exists(path+'Videos/'+files):
        shutil.move(path+files, path+'Videos/'+files)

    if ".pdf" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".xps" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".doc" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".docx" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".pptx" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)
    if ".xlsx" in files and not os.path.exists(path+'Documents/'+files):
        shutil.move(path+files, path+'Documents/'+files)


    if ".exe" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".deb" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".sh" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".tar.gz" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".tar.xz" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".zip" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".tar.bz2" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
    if ".iso" in files and not os.path.exists(path+'Softwares/'+files):
        shutil.move(path+files, path+'Softwares/'+files)
