import os
import re
from src.musicFile import musicFile

class folderExplorer:

    folderPath = '../../musicFolder'

    # def __init__(self) -> None:
    #     print('construct')
    
    def getFolderContent(self) -> list:
        return os.listdir(self.folderPath)
    
    def getFolderPath(self) -> str:
        return self.folderPath
        
    
    def getMusicFile(self) -> list:
        listElement = self.getFolderContent()
        musicFileArray = []
        pattern = r'.*\.mp3$'
        for file in listElement:
            if(re.match(pattern, file)):
                musicFileArray.append(musicFile((self.folderPath +'/'+file)))
        return musicFileArray
            