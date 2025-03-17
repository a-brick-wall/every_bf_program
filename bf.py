import sys
sys.path.append('./')
import brainfuck
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

i=-1
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
            #time.sleep(0.1)
            if brainfuck.evaluate(code)==eval_check:
                print("the following code evaluates to your desired output")
                print(code)
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
    i=Value('i',0)
    end=Value('i',0)
    while i.value <(7**code_len):
        print(i.value)
        process = multiprocessing.Process(target=bf_thread, args=(eval_check,i), daemon=True)
        process.start()
        time.sleep(10)
        i=Value('i',i.value)
        if i.value<-10:
            sys.exit()
        process.terminate()
        
    return None
if __name__ == "__main__":
    
    bf = ["+", "-", "<", ">", "[", "]","."]
        
    code_gen(5,bf,"=")
