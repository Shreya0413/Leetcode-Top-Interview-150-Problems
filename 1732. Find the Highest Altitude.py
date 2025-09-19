class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0    # current altitude
        best = 0   # highest altitude seen

        for g in gain:
            alt += g           # move up or down
            best = max(best, alt)  # update if new high

        return best  # done
        
