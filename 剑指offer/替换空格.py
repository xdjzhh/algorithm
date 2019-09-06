

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        string_list = s.split(' ')
        new_string = '%20'.join(i for i in string_list)
        print(new_string)


if __name__ == '__main__':
    string = 'we are family'
    solution = Solution()
    solution.replaceSpace(string)