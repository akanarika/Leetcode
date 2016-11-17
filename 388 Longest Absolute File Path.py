import re
from collections import defaultdict

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
		return ""

    	p = re.compile(r'\n[\t]*')
    	names = p.split(input)
    
    	gaps = []
    	for m in p.finditer(input):
    		gaps.append(len(m.group()))
    	
    	curr_path = []
    	curr_path.append(names[0])
    
    	last_gap = 0
    
    	final_path = []
        
        if re.match(r'[\w|\s]*[[\w]*[\s]*]*\.[\w]*', names[0]):
            max = len(names[0])
            final_path.append(names[0])
        else:
    	    max = 0
    
    	for i in range(len(gaps)):
    		gap = gaps[i] - 1
    		name = names[i+1]
    		
    		if gap > last_gap:
    			curr_path.append(name)
    		elif gap == last_gap:
    			curr_path[gap] = name
    		elif gap < last_gap:
    			curr_path[gap] = name
    			curr_path[:] = curr_path[:gap+1]
    
    		last_gap = gap
    
    		if re.match(r'[\w|\s]*[[\w]*[\s]*]*\.[\w]*', name):
    			curr_max = sum(len(item) for item in curr_path) + len(curr_path) - 1
    			if curr_max >= max:
    			    final_path[:] = curr_path
    			    max = curr_max
    
        final = ""
    	for item in final_path:
            final += "/" + item
            
        return len(final[1:]) if len(final) > 0 else 0
        