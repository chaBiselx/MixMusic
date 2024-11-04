import re
import random
from src.folderExplorer import folderExplorer
from src.musicFile import musicFile

class musicRandomizer:

    musicFileArray = []
    pattern =  r'.*\.mp3$'
    
    def __init__(self) -> None:
        self.musicFileArray = []
        self.generateListMusicFile()
        
    def generateListMusicFile(self):
        fe = folderExplorer()
        listElement = fe.getFolderContent()
        folderPath = fe.getFolderPath() + '/'
        for file in listElement:
            if(re.match(self.pattern, file)):
                self.musicFileArray.append(musicFile(folderPath+file))
    
    def randomise(self) -> bool:
        listRandom = self.getRandomList()
        
        for index,mf in enumerate(self.musicFileArray):
            mf.setNewPostion(str(listRandom[index]))
        
        return True
    
    def getRandomList(self):
        length  = len(self.musicFileArray)
        listRandom = list(range(0,length))
        random.shuffle(listRandom)
        return listRandom
        
            