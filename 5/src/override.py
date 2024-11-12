class AObj:
    def display(self, title, content = None):
        print(f"A title = {title}, content = {content}")

class BObj(AObj):
    def display(self, title):
        print(f"B title = {title}")

b: BObj = BObj()
# b.display("bbbb", "CCC")
a: AObj = BObj()
a.display("aaaa")
