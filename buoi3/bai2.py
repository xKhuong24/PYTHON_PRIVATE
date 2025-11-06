s=input("Input: ")
words=""
for ch in s.lower():
    if ch.isalpha() or ch==" ":
        words+=ch
print("→ Chuẩn hóa:",words)
letters=[ch for ch in words if ch.isalpha()]
vowels="ueoai"
v=sum(ch in vowels for ch in letters)
c=len(letters)-v
print("→ Nguyên âm:",v,"Phụ âm:",c)
wlist=words.split()
rev=[w[::-1] for w in wlist]
print("→ Đảo từng từ:",rev)
plain=words.replace(" ","")
is_palindrome=plain==plain[::-1]
print("→ Palindrome:",is_palindrome)