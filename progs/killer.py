import subprocess

output = subprocess.check_output('tasklist', shell=True)
print(type(output))
output = output.decode()
print(type(output))
print(output[:500])
print(len(output))

output_lines = output.split("\r\n")
print(type(output_lines))
print(output_lines[:5])
print(len(output_lines))

chrome_lines = list(filter(lambda x : 'chrome.exe' in x , output_lines))
print(len(chrome_lines))
print(chrome_lines)
chrome_lines = [ line for line in output_lines if 'chrome.exe' in line]
print(len(chrome_lines))
print(chrome_lines)

pids = list(map(lambda x : x.split()[1], chrome_lines))
print(pids)
pids = [line.split()[1] for line in chrome_lines]
print(pids)

for pid in pids:
    subprocess.call('taskkill /f /pid ' + pid)
    



##tasklist  ( mac or linux : ps -ef)
##taskkill /f /pid <pid> ( mac or linux : kill -9 <pid> )
#
#import subprocess
## fire and forget
##subprocess.call('tasklist', shell=True)
#
## capture the stdout/stderr
#output = subprocess.check_output('dir', shell=True)
#print(output.decode())
##print(type(output))

