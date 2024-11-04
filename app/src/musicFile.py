import os
import re
from mutagen.id3 import ID3, TIT2

class musicFile:
    path = None
    oldName = None

    def __init__(self, path):
        self.path = os.path.realpath(path)
        self.oldName = re.sub(
           r"^temp_", 
           "", 
           self.getName()
       )
        tempName = "temp_"+ self.oldName
        self.renameFile(tempName)
        self.path = os.path.join(self.getDir() , tempName)
        
        
    def getName(self) -> str :
        return os. path. basename(self.path)
    
    def getDir(self) -> str :
        return os. path. dirname(self.path)
    
    def setNewPostion(self, newPosition) -> None:
        metaTitle = newPosition
        
        self.setNewMetaDataTitle(metaTitle)
        self.renameFile(self.oldName)
        
    def setTitleInName(self) -> None:
        self.renameFile(self.getMetaDataTitle() + '.mp3')
        
        
    def renameFile(self, name) -> None:
        newname = os.path.join(self.getDir() , name)
        oldName = os.path.join(self.getDir() , self.getName())
        os.rename(oldName, newname)
        
        
    def setNewMetaDataTitle(self, title) -> None:
        
        audio_file = ID3(self.path)  # Assure-toi que self.filePath contient le chemin du fichier MP3

        # Crée un frame TIT2 pour le titre
        audio_file['TIT2'] = TIT2(encoding=3, text=title)

        # Sauvegarde les changements
        audio_file.save()
        
    def getMetaDataTitle(self) -> str:
        audio_file = ID3(self.path) 
        return audio_file['TIT2'].text[0]

 
        