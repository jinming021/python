#编写一个生成凯撒密码的程序
plain_text = input("请输入需要加密的明文（只支持英文字母）：")
shift = int(input("请输入移动的位数："))

crypt_text = ""

for char in plain_text:
    if char.isalpha():
        if char.isupper():
            crypt_text += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.islower():
            crypt_text += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            crypt_text = char
    else:
        crypt_text += char

print(crypt_text)


