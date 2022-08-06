# Time Complexity: O(N)
# Space Complexity: O(N)

class HashMap:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        seen = {}
        work_log = []
        for start, end in paint:
            work = 0
            
            while start < end:
                if start in seen:
                    start = seen[start]
                else:
                    seen[start] = end
                    work += 1
                    start += 1
                    
            work_log.append(work)

        return work_log
