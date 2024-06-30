#Python

#python一行实现动态百分比进度条

import sys, time
for i in range(101): sys.stdout.write(f"\r{i}% [{'=' * i}{' ' * (100 - i)}]"); sys.stdout.flush(); time.sleep(0.1)