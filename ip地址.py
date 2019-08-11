class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self._restoreIpAddresses(0, s, [], result)
        return result

    def _restoreIpAddresses(self, length, s, ips, result):
        if not s:
            if length == 4:
                result.append('.'.join(ips))  # 以.分隔作为字符串返回
            return
        if length == 4:  # 分了4段，结束
            return

        # 取一位
        self._restoreIpAddresses(length + 1, s[1:], ips + [s[:1]], result)

        # 若要取2位及以上，要确保目前的第一位不能为0
        if s[0] != '0':
            if len(s) >= 2:
                self._restoreIpAddresses(length + 1, s[2:], ips + [s[:2]], result)
            if len(s) >= 3 and int(s[:3]) <= 255: # 若要取3位，则要保证小于255
                self._restoreIpAddresses(length + 1, s[3:], ips + [s[:3]], result)

#    或者 ------------------------------------------------------------------------------
def res(s,k,ans,ANS):
    if len(ans)==4 :#列表里有4个就返回，大于4 个的一定不对
        if  k==len(s):
            ANS.append('.'.join(ans))#将列表转换成字符串
        return
    else:
        for i in range(k+1,min(k+4,len(s)+1)): #这里即选区三个数字，i最
                #多取到len(S),即[第k个开始:前len(s)个字母]
            if s[k]=='0' and i>k+1: #遇到0 只能出现一次
                break
            a=s[k:i]
            if int(a) <=255:
                ans.append(a)
                res(s,i,ans,ANS)
                ans.pop() #换下一个数字继续
    ans=[]
    res(s,0,[],ans)
    return ans
