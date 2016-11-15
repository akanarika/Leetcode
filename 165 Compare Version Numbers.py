class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        nv1 = []
        nv2 = []
        
        for i in range(max(len(v1), len(v2))):
            try:
                nv1.append(int(v1[i]))
            except:
                nv1.append(0)
            try:
                nv2.append(int(v2[i]))
            except:
                nv2.append(0)
            if nv1[i] > nv2[i]:
                return 1
            elif nv1[i] < nv2[i]:
                return -1
        
        return 0
        