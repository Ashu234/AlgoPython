import sys
import time
from itertools import permutations


class Node:

     def __init__(self):
           self.data = None
           self.word = False
           self.nodes = {}


     def insertWord(self,word,indexPos):
           currentLetter = word[indexPos]
           if currentLetter not in self.nodes:
                 self.nodes[currentLetter] = Node()

           if len(word) == indexPos+1:
                 self.nodes[currentLetter].data = word
                 self.nodes[currentLetter].word = True
           else:
                 self.nodes[currentLetter].insertWord(word, indexPos + 1)


     def insertWordSuffix(self,word,indexPos):
           currentLetter = word[indexPos]
           if currentLetter not in self.nodes:
                 self.nodes[currentLetter] = Node()

           if len(word) == indexPos+1:
                 self.nodes[currentLetter].data = word[::-1]
                 self.nodes[currentLetter].word = True
           else:
                 self.nodes[currentLetter].insertWordSuffix(word, indexPos + 1)


                

class Trie:

      def __init__(self):
           self.root = Node()
           self.rootSuffix = Node()

      def insert(self,word):
           self.root.insertWord(word,0)

      def hasWord(self, word):
           currentNode = self.root
           found = True
           for letter in word:
                if letter in currentNode.nodes:
                    currentNode = currentNode.nodes[letter]
                else:
                    found = False
                    break

           if found:
                if  currentNode.word == False:
                      found = False
           return found

      def insertSuffix(self,word):
           self.rootSuffix.insertWordSuffix(word,0)


      def get_all_with_prefix(self, prefix, string_pos = 0):
        words = []
        
        top_node = self.root
        for letter in prefix:
            if letter in top_node.nodes:
                top_node = top_node.nodes[letter]
            else:
                return words
        
        if top_node == self.root:
            queue = [node for key, node in self.top_node.iteritems()]
        else:
            queue = [top_node]

        while queue:
            current_node = queue.pop()
            if current_node.word != False:
                words.append(current_node.data)
            
            queue = [node for key,node in current_node.nodes.iteritems()] + queue
        
        return words

      def get_all_with_suffix(self, suffix, string_pos = 0):
        words = []
        
        top_node = self.rootSuffix
        for letter in suffix:
            if letter in top_node.nodes:
                top_node = top_node.nodes[letter]
            else:
                return words
        
        if top_node == self.rootSuffix:
            queue = [node for key, node in self.top_node.iteritems()]
        else:
            queue = [top_node]

        while queue:
            current_node = queue.pop()
            if current_node.word != False:
                words.append(current_node.data)
            
            queue = [node for key,node in current_node.nodes.iteritems()] + queue
        
        return words

      def buildIndexedDic(self,filePath):
             dicFile=open(filePath,'r')
             doc=[]
             for line in dicFile:
                line = line.strip()
                self.insert(line)

      def buildIndexedDicSuffix(self,filePath):
             dicFile=open(filePath,'r')
             doc=[]
             for line in dicFile:
                line = line.strip()
                line = line[::-1]
                self.insertSuffix(line)



                

class Scrabbler:

     def __init__(self):
        self.index={}
        self.reducedIndex = {}
     

     def buildIndexedDic(self,filePath):
             dicFile=open(filePath,'r')
             doc=[]
             for line in dicFile:
                key = line[0]
                line = line.strip()
                if key in self.reducedIndex:
                  if len(line) not in self.reducedIndex[key]:
                      self.reducedIndex[key][len(line)] = [line]
                  else:
                      self.reducedIndex[key][len(line)].append(line)
                else:
                  self.reducedIndex[key] = {}
                  self.reducedIndex[key][len(line)] = [line]
             
             

     def findScrabbleWords(self,scrabbleWord):
         
         scrabbleDic = {}
         scrabbleDicUnique = {}
         for letter in scrabbleWord:
               scrabbleDicUnique[letter] = 0
               if letter in scrabbleDic:
                 scrabbleDic[letter] += 1
               else:
                 scrabbleDic[letter] = 1
         resultList = []
         for scrabbleKey in scrabbleDicUnique:
               for i in range(2, len(scrabbleWord)+1):
                    if i in self.reducedIndex[scrabbleKey]:
                          x = self.reducedIndex[scrabbleKey][i]
                          for word in x:
                             flag = True
                             for letter in word:
	                                   value = scrabbleDic.get(letter)
	                                   if value == 0:
                                             flag = False
                                             break   
	                                   elif value == None:
	                                      flag = False
	                                      break
	                                   else: 
	                                      scrabbleDic[letter] -= 1
	                     if flag == True:
	                        resultList.append(word)
		             scrabbleDic.clear()
		             for letter in scrabbleWord:
			        if letter in scrabbleDic:
			           scrabbleDic[letter] += 1
			        else:
			           scrabbleDic[letter] = 1
         
         resultList = sorted(resultList)
         printResult(resultList)

def printResult(wordList):
          if wordList == []:
            print 'word not found'
          else:
            for word in wordList:
              print word

class FindTask:

    def __init__(self):
        self.filePath = 'words.txt'
        self.scrabbler = Scrabbler()

    
    def unique_permutations(self,iterable, r=None):
	    previous = tuple()
	    for p in permutations(sorted(iterable), r):
		if p > previous:
		    previous = p
		    yield p

    

    def printError(self):
         print 'pass argument as --prefix "word" for prefix search'
         print 'pass argument as --suffix "word" for suffix search'
         print 'pass argument as "word/letter" for word generation'
         sys.exit()


    def findTask(self): 
         if len(sys.argv) <= 1:
             self.printError()
         param=sys.argv
         task = param[1]
         if len(sys.argv) == 3 and param[2].isalpha():
		 if task == '--prefix':
		     self.prefix = param[2]
		     trie = Trie()
		     trie.buildIndexedDic(self.filePath)
		     printResult(sorted(trie.get_all_with_prefix(self.prefix)))
		 elif task == '--suffix':
		     self.suffix = param[2]
		     trie = Trie()
		     trie.buildIndexedDicSuffix(self.filePath)
		     self.suffix = self.suffix[::-1]
		     printResult(sorted(trie.get_all_with_suffix(self.suffix)))
                 else:
                     self.printError()
         else:
             if task.isalpha():
	             self.scrabbleWord = param[1]
	     	     start = int(round(time.time() * 1000))
	     	     if len(self.scrabbleWord) > 7:
	     	         self.scrabbler.buildIndexedDic(self.filePath)
	     	         self.scrabbler.findScrabbleWords(self.scrabbleWord)
	     	     else:
                         resultList = []
	     	         trie = Trie()
	     	         trie.buildIndexedDic(self.filePath)
	     	         for k in range(2,len(self.scrabbleWord)+1):
	      	               for p in self.unique_permutations(self.scrabbleWord, k):
	     	                    s = ''.join(p)
                                    if trie.hasWord(s):
	      		 	       resultList.append(s)
                         resultList = sorted(resultList)
                         printResult(resultList)
	      	     
             else:
                   self.printError()
	 

if __name__=="__main__":
    f = FindTask()
    f.findTask()





























