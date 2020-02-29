"""
判断两个IP是否属于同一子网, 需要判断网络地址是否相同
网络地址：IP地址的二进制与子网掩码的二进制地址逻辑“与”得到
主机地址: IP地址的二进制与子网掩码的二进制取反地址逻辑“与”得到
"""


class IpAddrConverter(object):

    def __init__(self, ip_addr, net_mask):
        self.ip_addr = ip_addr
        self.net_mask = net_mask

    @staticmethod
    def _get_bin(target):
        if not target.isdigit():
            raise Exception('bad ip address')
        target = int(target)
        assert target < 256, 'bad ip address'
        res = ''
        temp = target
        for t in range(8):
            a, b = divmod(temp, 2)
            temp = a
            res += str(b)
            if temp == 0:
                res += '0' * (7 - t)
                break
        return res[::-1]

    def _to_32_bin(self, ip_address):
        temp_list = ip_address.split('.')
        assert len(temp_list) == 4, 'bad ip address'
        return ''.join(list(map(self._get_bin, temp_list)))

    @property
    def ip_32_bin(self):
        return self._to_32_bin(self.ip_addr)

    @property
    def mask_32_bin(self):
        return self._to_32_bin(self.net_mask)

    @property
    def net_address(self):
        ip_list = self.ip_addr.split('.')
        mask_list = self.net_mask.split('.')
        and_result_list = list(map(lambda x: str(int(x[0]) & int(x[1])), list(zip(ip_list, mask_list))))
        return '.'.join(and_result_list)

    @property
    def host_address(self):
        ip_list = self.ip_addr.split('.')
        mask_list = self.net_mask.split('.')
        rever_mask = list(map(lambda x: abs(255 - int(x)), mask_list))
        and_result_list = list(map(lambda x: str(int(x[0]) & int(x[1])), list(zip(ip_list, rever_mask))))
        return '.'.join(and_result_list)


if __name__ == '__main__':
    ip01 = IpAddrConverter("211.95.165.24", "255.255.254.0")
    ip02 = IpAddrConverter("211.95.164.78", "255.255.254.0")
    print(ip01.net_address == ip02.net_address)