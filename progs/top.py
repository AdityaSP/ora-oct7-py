import subprocess
output = subprocess.check_output('tasklist', shell=True).decode().split("\r\n")[3:-1]
#print(output[:3])
#print(output[-2:])
#[
#'cmd.exe                      29764 Console                    1      3,692 K', #'tasklist.exe                 29716 Console                    1      7,712 K'
#]

#"3,692"
#line.split()[-2].replace(',','')
#"3692"
#
#3692
# inplace sorting
output.sort(key= lambda line: int(line.split()[-2].replace(',','')), reverse=True)
for item in output[:5]:
    print(item)