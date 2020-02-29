'''
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
通过次数54,523提交次数112,072

https://leetcode-cn.com/problems/trapping-rain-water/
'''

'''动态规划'''
import queue


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        ans = 0
        for index in range(1, len(height)):
            left_max[index] = max(height[index], left_max[index - 1])

        for index in range(len(height) - 2, -1, -1):
            right_max[index] = max(height[index], right_max[index + 1])

        for index in range(len(height)):
            ans += min(left_max[index], right_max[index]) - height[index]
        return ans


'''双指针'''


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        right_max = 0
        left_max = 0

        right_index = len(height) - 1
        left_index = 0
        ans = 0
        while left_index < right_index:
            if height[left_index] <= height[right_index]:
                left_max = max(left_max, height[left_index])
                ans += (left_max - height[left_index])
                left_index += 1

            if height[right_index] < height[left_index]:
                right_max = max(right_max, height[right_index])
                ans += (right_max - height[right_index])
                right_index -= 1
        return ans

'''2D版本https://leetcode-cn.com/problems/trapping-rain-water-ii/'''


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import queue
        que = queue.PriorityQueue()
        visited = [[1] * len(heightMap[0]) for i in range(len(heightMap))]

        for i in range(len(heightMap[0])):
            que.put([heightMap[0][i], 0, i])
            visited[0][i] = -1
            que.put([heightMap[-1][i], len(heightMap) - 1, i])
            visited[-1][i] = -1

        for i in range(1, len(heightMap) - 1):
            que.put([heightMap[i][0], i, 0])
            visited[i][0] = -1
            que.put([heightMap[i][-1], i, len(heightMap[0]) - 1])
            visited[i][-1] = -1
        ans = 0
        mx = 0
        while que.qsize() != 0:
            current = que.get()
            '''若现在是高为1的点，mx为2，那么说明1的点和mx为2的点想通，积水不会达到3的点'''
            mx = max(current[0], mx)
            if current[1] > 0 and visited[current[1] - 1][current[2]] != -1:
                que.put([heightMap[current[1] - 1][current[2]], current[1] - 1, current[2]])
                visited[current[1] - 1][current[2]] = -1
                if heightMap[current[1] - 1][current[2]] < mx:
                    ans += mx - heightMap[current[1] - 1][current[2]]

            if current[1] < len(heightMap) - 1 and visited[current[1] + 1][current[2]] != -1:
                que.put([heightMap[current[1] + 1][current[2]], current[1] + 1, current[2]])
                visited[current[1] + 1][current[2]] = -1
                if heightMap[current[1] + 1][current[2]] < mx:
                    ans += mx - heightMap[current[1] + 1][current[2]]

            if current[2] > 0 and visited[current[1]][current[2] - 1] != -1:
                que.put([heightMap[current[1]][current[2] - 1], current[1], current[2] - 1])
                visited[current[1]][current[2] - 1] = -1
                if heightMap[current[1]][current[2] - 1] < mx:
                    ans += mx - heightMap[current[1]][current[2] - 1]

            if current[2] < len(heightMap[0]) - 1 and visited[current[1]][current[2] + 1] != -1:
                que.put([heightMap[current[1]][current[2] + 1], current[1], current[2] + 1])
                visited[current[1]][current[2] + 1] = -1
                if heightMap[current[1]][current[2] + 1] < mx:
                    ans += mx - heightMap[current[1]][current[2] + 1]

        return ans

