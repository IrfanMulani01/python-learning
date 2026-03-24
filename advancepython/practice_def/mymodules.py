class calculator:
    def add(self, i,j):
        return i + j
    def sub(self, i,j):
        return i - j
    def mul(self, i,j):
        return i * j
    def div(self, i,j):
        if i == 0 or j == 0:
            print("division in zero not allowed")
        else:
            return i / j
cal = calculator()
