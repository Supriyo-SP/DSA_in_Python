class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        components = path.split('/')
        stack = []
        for component in components:
            if component == "" or component == ".":
                continue
            elif component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        return "/" + "/".join(stack)                     
        