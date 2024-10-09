class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        output=[]
        linelength=0
        line = []
        for word in words:
            print(linelength,len(line),len(word))
            if(linelength+len(line)+len(word)>maxWidth):
                spaces_needed = maxWidth-linelength
                if(len(line)==1):
                    output.append(line[0]+' '*spaces_needed)
                else:
                    spaces_btw_words, extra_spaces = spaces_needed//(len(line)-1),spaces_needed%(len(line)-1)
                    for i in range(extra_spaces):
                        line[i]+=' '
                    output.append((' '*spaces_btw_words).join(line))
                line=[]
                linelength=0
            line.append(word)
            linelength+=len(word)
            print(line,linelength)
        lastLine = ' '.join(line)
        output.append(lastLine+ ' '*(maxWidth-len(lastLine)))
        return output
    
