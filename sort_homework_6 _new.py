import os 
import shutil
import re
import glob

category = {
    'jpeg':"pictures",
    'png':"pictures",
    'jpg':"pictures",
    'svg':"pictures",
    'avi':"videos",
    'mp4':"videos",
    'mov':"videos",
    'mkv':"videos",
    'doc':"documents",
    'docs':"documents",
    'txt':"documents",
    'pdf':"documents",
    'xlsx':"documents",
    'pptx':"documents", 
    'ppt':"documents",
    'mp3':"music", 
    'ogg':"music", 
    'wav':"music", 
    'amr':"music",
    'wma':"music"
}

archive = ['zip', 'gz', 'tar', 'rar']

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

    
def normalize(filename):
    filename_new = re.sub(r'\W', '_', filename)  
    return filename_new.translate(TRANS)

def category_file(filename, path, filePath, extension,i):
    new_name = normalize(filename)                              
    if os.path.isdir(path):
        if os.path.exists(path+'/'+ category[extension[1:].lower()].upper()):
            shutil.move(filePath[0]+'/'+ i, path+'/'+category[extension[1:].lower()].upper()+'/'+ f"{new_name}{extension}")
        else:
            os.makedirs(path + '/'+category[extension[1:].lower()].upper())
            shutil.move(filePath[0]+'/'+ i, path+'/'+category[extension[1:].lower()].upper()+'/'+ f"{new_name}{extension}")
    return

def sorting_files(path):
    files = os.walk(path) # використовуемо os.walk() щоб у випадку знайденої папки її теж сортувати.
    for file in files:
        filePath = glob.glob(file[0])
        for i in file[2]:
    
            filename, extension = os.path.splitext(i)

            if extension[1:].lower() in category:
                category_file(filename, path, filePath, extension,i)             
            elif extension[1:].lower() in archive:
                
                new_name = normalize(filename)               
                if os.path.isdir(path):
                    if os.path.exists(path+'/'+"ARCHIVE"):
                        os.makedirs(path + '/'+"ARCHIVE"+'/'+ new_name)
                        shutil.unpack_archive(filePath[0]+'/'+ i, path+'/'+"ARCHIVE"+'/'+ new_name)
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"ARCHIVE"+'/'+ f"{new_name}{extension}")
                    else:
                        os.makedirs(path + '/'+"ARCHIVE")
                        os.makedirs(path + '/'+"ARCHIVE"+'/'+ new_name)
                        shutil.unpack_archive(filePath[0]+'/'+ i, path+'/'+"ARCHIVE"+'/'+ new_name)
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"ARCHIVE"+'/'+ f"{new_name}{extension}")
            else:               
                new_name = normalize(filename)
                if os.path.isdir(path):
                    if os.path.exists(path+'/'+"UNKNOW"):
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"UNKNOW"+'/'+ f"{new_name}{extension}")
                    else:
                        os.makedirs(path + '/'+"UNKNOW")
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"UNKNOW"+'/'+ f"{new_name}{extension}")
                        
        if len(os.listdir(filePath[0])) == 0: # Check if the folder is empty
            shutil.rmtree(filePath[0])# If so, delete it  
        
if __name__ == "__main__": sorting_files(path = input('Enter a path of the folder you want to sort out: ')) 