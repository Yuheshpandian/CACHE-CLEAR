import os
import time as t
from rich.console import Console

console = Console()

file_count = 0
def delete(target):
   console.print(f"Deleting all files in [{target}] ",style="cyan")
   print("\n\n")
   t.sleep(3)
   for file in os.listdir(target):
      try:
         os.unlink(target + file)
         console.print(f"\t File [{file}] deleted",style="bold blue")
         t.sleep(0.2)

      except Exception as e:
         print()
         t.sleep(0.2)
         console.print(f"\t cannot delete file [{file}] due to error \n[{e}]",style="bold red")
         print()
         continue
   t.sleep(3)
   print("\n\n")
   console.print(f"All files in the folder/path [{target}] has been deleted successfully (^-^) ",style="cyan")

