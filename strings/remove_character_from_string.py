class StrRecursion:
    def print_str(self, s : str) -> None:
        a = s
        if len(s)==1:
            print(s)
            return
        
        #print(s[0]) # print normal
        self.print_str(s[1:])
        print(s[0]) # Print reverse

    def removeWord(self, s: str, a: str) -> str:
        if len(s) == 0:
            return ""
        
        if s.startswith(a):
            return self.removeWord(s[len(a):], a)
        else:
            return s[0] + self.removeWord(s[1:], a)
a = StrRecursion()

#a.print_str("ABVCFAHAH")

print(a.removeWord("sfappledjfhf", "apple"))
