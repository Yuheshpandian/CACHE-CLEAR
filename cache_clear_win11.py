#This program clears all useless cache in your windows pc

#impoting the requiered modules/libraries

from delete import delete
import time as t
from rich.console import Console
import winshell


#targets/paths

target_1 = "C:\\Windows\\Temp\\"
target_2 = "C:\\Users\\User\\AppData\\Local\\Temp\\"
target_3 = "C:\\Windows\\Prefetch\\"
target_4 ="Recycle Bin\\"


console = Console()

console.print("CACHE-CLEAR-WIN11",style="bold magenta")

print("\n\n\n")
console.print("clearing cache in the 'temp' folder!",style="bold yellow")
t.sleep(0.5)
print("\n")
delete(target_1)
print("\n")
console.print("cleared cache in 'temp' folder [✓]",style="bold yellow")
print("\n")
t.sleep(0.5)

print("\n\n\n")
console.print("clearing cache in the '%temp%' folder!",style="bold yellow")
t.sleep(0.5)
print("\n")
delete(target_2)
print("\n")
console.print("cleared cache in '%temp%' folder [✓]",style="bold yellow")
print("\n")
t.sleep(0.5)

print("\n\n\n")
console.print("clearing cache in the 'prefetch' folder!",style="bold yellow")
t.sleep(0.5)
print("\n")
delete(target_3)
print("\n")
console.print("cleared cache in 'prefetch' folder [✓]",style="bold yellow")
print("\n")
t.sleep(0.5)

print("\n\n\n")

console.print("Clearing 'RECYCLE BIN' ",style="bold yellow")
try:
    winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
    console.print("Recycle Bin is emptied now! [✓]",style="bold blue")
except:
    console.print("Recycle Bin is already empty! [✓]",style="bold cyan")

t.sleep(0.5)


print("")
console.print("Every possible cache and useless files has been deleted. Hope you enjoy your fast laptop (^_~) ", style="bold green ")
print("")

