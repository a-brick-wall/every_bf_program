import sys
sys.path.append('./')
import brainfuck
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

start_i=-1

# you can start at a number close to a known solution to see it work
# start_i=1675637653546986400

bf = ["+", "-", "<", ">", "[", "]","."]

import multiprocessing
from multiprocessing import Value
import time
 
def bf_thread(eval_check,i):
    test = 1
    while True:
        test+=1
        i.value=i.value+1
        code = ""
        for digit in numberToBase(i.value, 7):
            code+=bf[digit]
        try:
            if brainfuck.evaluate(code)==eval_check:
                print(code + ' evaluates to ' + brainfuck.evaluate(code))
                i.value=-1000
                break

        except:
            pass
 
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def code_gen(code_len,bf,eval_check):
    global start_i
    # uses long long so there is a size limit to the bf code, but it would take essentially forever to get that far
    i=Value('q',start_i)
    while i.value <(7**code_len):
        print(i.value)
        process = multiprocessing.Process(target=bf_thread, args=(eval_check,i), daemon=True)
        process.start()
        time.sleep(10)
        i=Value('q',i.value)
        if i.value<-10:
            sys.exit()
        process.terminate()
        
    return None
if __name__ == "__main__":
    
    bf = ["+", "-", "<", ">", "[", "]","."]
        
    code_gen(25,bf,"0")
