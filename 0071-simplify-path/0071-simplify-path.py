class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for i in path.split('/'):
            if i in ('','.'):
                continue
            if i == '..':
                if res:
                    res.pop()
            else:
                res.append(i)
        return '/' + '/'.join(res)
        