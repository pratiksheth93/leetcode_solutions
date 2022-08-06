# Time Complexity: O(N*Log N)
# Space Complexity: O(N)

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        mapping = defaultdict(int)
        for start, end, colorIdx in segments:
            mapping[start] += colorIdx
            mapping[end] -= colorIdx
        
        res = []
        prev, color = None, 0
        for now in sorted(mapping):
            if color:
                res.append((prev, now, color))
            
            color += mapping[now]
            prev = now
            
        return res