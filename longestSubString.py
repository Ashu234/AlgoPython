
class LongestSubString:
	def lengthOfLongestSubstring(self, s):
		
		maxLen = 0
		j = 0
		myDic = {}
		
		if len(s) == 0:
		    return 0
		for i in range(len(s)):
		    if s[i] in myDic:
		        j = max(j,myDic[s[i]] + 1)
		        
		    myDic[s[i]] = i
		    maxLen = max(maxLen,i-j+1)
		return maxLen

if __name__=="__main__":
    f = LongestSubString()
    print f.lengthOfLongestSubstring("dvdf")

