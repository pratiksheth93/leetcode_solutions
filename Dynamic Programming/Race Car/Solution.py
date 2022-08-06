# Time Complexity: O(T Log T)
# Space Complexity: O(T)
# T: Target

class DynamicProgrammingQueue:
    def racecar(self, target: int) -> int:
        frontier = deque([(0, 0, 1)]) # step, pos, spd
        while frontier:
            step, pos, spd = frontier.popleft()
            
            if pos == target:
                return step
            
            frontier.append((step + 1, pos + spd, spd * 2))
            
            if pos + spd > target and spd > 0:
                frontier.append((step + 1, pos, -1))
            if pos + spd < target and spd < 0:
                frontier.append((step + 1, pos, 1))

 # Time Complexity: O(T Log T)
# Space Complexity: O(T)
# T: Target
     
class DynamicProgramming(object):
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target
        for t in xrange(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in xrange(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]

 # Time Complexity: O(T Log T)
# Space Complexity: O(T)
# T: Target

class DijkstraAlgorithm(object):
    def racecar(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps: continue

            for k in xrange(K+1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ: steps2 -= 1

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]
