numero_puerto = int(input("Dime numero de puerto: "))


match numero_puerto:
    class "21":
        print("FTP")
    class "22":
        print("SSH")
    class "53":
        print("DNS")
    class "80":
        print("HTTP")
    class "443":
        print("HTTPS")
