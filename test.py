def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        
        while p2 < n:
            try:
                if nums1[p1] >= nums2[p2]:
                    nums1.insert(p1, nums2[p2])
                    p1 += 2
                    p2 += 1
            except:
                nums1.append(nums2[p2:])
            else:
                p1 += 1

        print nums1
        
merge([0],0,[1],1)