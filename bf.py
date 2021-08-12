import brainfuck
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

i=-1
bf = ["","+", "-", "<", ">", "[", "]","."]

import multiprocessing
from multiprocessing import Value
import time
 
def bf_thread(eval_check,i):
    while True:
        i.value=i.value+1
        code = ""
        for digit in numberToBase(i.value, 8):
            code+=bf[digit]
        try:
            time.sleep(.1)
            print(brainfuck.evaluate(code))
            if brainfuck.evaluate(code)==eval_check:
                print("the following code evaluates to your desired output")
                print(code)

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
    while i.value <(8**code_len):
        print(i.value)
        process = multiprocessing.Process(target=bf_thread, args=(eval_check,i))
        process.start()
        time.sleep(10)
        i=Value('i',i.value)
        process.terminate()
        
    return out
if __name__ == "__main__":
    
    bf = ["","+", "-", "<", ">", "[", "]","."]
        
    code_gen(50,bf,"1")
    x = input()
