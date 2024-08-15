#
#  _                                _                __          __ _  _    _        _____      _ 
# | |                              (_)               \ \        / /(_)| |  | |      / ____|    | |
# | |      ___   __ _  _ __  _ __   _  _ __    __ _   \ \  /\  / /  _ | |_ | |__   | |         | |
# | |     / _ \ / _` || '__|| '_ \ | || '_ \  / _` |   \ \/  \/ /  | || __|| '_ \  | |     _   | |
# | |____|  __/| (_| || |   | | | || || | | || (_| |    \  /\  /   | || |_ | | | | | |____| |__| |
# |______|\___| \__,_||_|   |_| |_||_||_| |_| \__, |     \/  \/    |_| \__||_| |_|  \_____|\____/ 
#                                              __/ |                                              
#                                             |___/                         -  By CJ
#
# YouTube : www.youtube.com/@LearningWithCJ
# GitHub  : www.github.com/Carl-Johnson1976
# Telegram: t.me/LearningWithCJ
#

import subprocess



cmd_data = subprocess.check_output(["ipconfig", "/all"]).decode("utf-8").split("\n")
keyList = ["Link-local IPv6 Address", "IPv4 Address", "Subnet Mask", "DHCP Server", "DNS Servers"]
windows_keyList= ["Host Name"]
list = []

for a in cmd_data:
    targets = ["Windows IP Configuration\r", "Wireless LAN adapter Wi-Fi:\r", "Ethernet adapter Ethernet:\r"]
    for t in targets:
        if a == t:
            cmd = cmd_data[cmd_data.index(t):]

            result = "\n{}\n\n".format(t.replace("\r", ""))
            list.append(result)

            if t == "Windows IP Configuration\r":
                for i in windows_keyList:
                    data = "".join([b.split(":", 1)[1].strip() for b in cmd if i in b])

                    if data != "":
                        if "(Preferred)" in data:
                            data = data[:-11]
                        result = "\t{:25} : {}\n".format(i, data)
                        list.append(result)
                    else:
                        result = "\t{:25} : \n".format(i)
                        list.append(result)
            else:
                for i in keyList:
                    if i == "DNS Servers":
                        data = "".join([b for b in cmd if i in b])

                        if data != "":
                            dataIndex = cmd.index(data)

                            if ":" in cmd[dataIndex + 1]:
                                data = "".join([b.split(":", 1)[1].strip() for b in cmd if i in b])
                                result = "\t{:25} : Primary : {}\n".format(i, data)
                                list.append(result)
                            else:
                                data = "".join([b.split(":", 1)[1].strip() for b in cmd if i in b])
                                data2 = "".join(cmd[dataIndex + 1].strip())
                                result = "\t{:25} : Primary   : {}\n\t{}Secondary : {}\n".format(i, data, " " * 28, data2)
                                list.append(result)
                        else:
                            result = "\t{:25} : \n".format(i)
                            list.append(result)
                    else:
                        data = "".join([b.split(":", 1)[1].strip() for b in cmd if i in b])

                        if data != "":
                            if "(Preferred)" in data:
                                data = data[:-11]
                            result = "\t{:25} : {}\n".format(i, data)
                            list.append(result)
                        else:
                            result = "\t{:25} : \n".format(i)
                            list.append(result)

print("".join(list))
