import os #метод для роботи з файлами: зміннювати шлях, переменовувати, переmіщати і.т.д
import shutil
import re
import glob


path = input('Enter a path of the folder you want to sort out: ') # будемо водити шлях папки яку хочемо сортувати 

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

    
def normalize(filename):
    filename_new = re.sub(r'\W', '_', filename)  
    return filename_new.translate(TRANS)

    

def sorting_files(path):

    pictures = ['jpeg', 'png', 'jpg', 'svg']
    videos = ['avi', 'mp4', 'mov', 'mkv', 'MOV']
    documents =  ['doc', 'docs', 'txt', 'pdf', 'xlsx', 'pptx', 'ppt']
    music =  ['mp3', 'ogg', 'wav', 'amr','wma']
    archive = ['zip', 'gz', 'tar', 'rar']

    files = os.walk(path) # використовуемо os.walk() щоб у випадку знайденої папки її теж сортувати.
    for file in files:
        filePath = glob.glob(file[0])
        for i in file[2]:

            filename, extension = os.path.splitext(i)

            if extension[1:] in pictures:
                new_name = normalize(filename)
                              
                if os.path.isdir(path):
                    if os.path.exists(path+'/'+"PICTURES"):
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"PICTURES"+'/'+ f"{new_name}{extension}")
                    else:
                        os.makedirs(path + '/'+"PICTURES")
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"PICTURES"+'/'+ f"{new_name}{extension}")


            elif extension[1:] in videos:
                new_name = normalize(filename)
               
                if os.path.isdir(path):
                    if os.path.exists(path+'/'+"VIDEO"):
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"VIDEO"+'/'+ f"{new_name}{extension}")
                    else:
                        os.makedirs(path + '/'+"VIDEO")
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"VIDEO"+'/'+ f"{new_name}{extension}")
                
            elif extension[1:] in documents:
                new_name = normalize(filename)
               
                if os.path.isdir(path):
                    if os.path.exists(path+'/'+"DOCUMENTS"):
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"DOCUMENTS"+'/'+ f"{new_name}{extension}")
                    else:
                        os.makedirs(path + '/'+"DOCUMENTS")
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"DOCUMENTS"+'/'+ f"{new_name}{extension}")

            elif extension[1:] in music:
                new_name = normalize(filename)
               
                if os.path.isdir(path):
                    if os.path.exists(path+'/'+"MUSIC"):
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"MUSIC"+'/'+ f"{new_name}{extension}")
                    else:
                        os.makedirs(path + '/'+"MUSIC")
                        shutil.move(filePath[0]+'/'+ i, path+'/'+"MUSIC"+'/'+ f"{new_name}{extension}")
            
                        
            elif extension[1:] in archive:
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
        
sorting_files(path)