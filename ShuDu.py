import random
import os, sys
import traceback
import time
import gc

class ShuDu:
    '''
    每一个ShuDu实例会自动生成一个完整且合法的9x9数独方阵，平均用时10-20秒左右
    应该还有可以优化的地方，比如先遍历所有空节点，优先填充可能性最少的位置
    '''
    
    def __init__(self):
        '''
        初始化类实例
        '''
        self.data = []
        self.num = [1,2,3,4,5,6,7,8,9]
        self.init_data()
        self.create()
        self.show()
        gc.set_threshold(500,20,5)
        
    def init_data(self):
        '''
        初始化9x9方阵至self.data里面，其中左上、中间、右下的3x3方阵都由1-9随机填充
        '''
        self.data = []
        for i in range(9):
            self.data.append([0]*9)
        for i in range(3):
            j = i
            l = [1,2,3,4,5,6,7,8,9]
            random.shuffle(l)
            for i0 in range(3):
                for j0 in range(3):
                    self.data[i*3+i0][j*3+j0] = l[i0*3+j0]
        # self.show()
        # time.sleep(99999)
        
        
    def create(self):
        '''
        新建一个合法的9x9方阵
        '''
        gc.disable()
        ok = True
        k = 0
        k2 = 0
        start = time.time()
        while 1:
            ok = True
            self.init_data()
            for i in range(9):
                if ok == False:
                    break
                for j in range(9):
                    if ok == False:
                        break
                    if self.data[i][j] != 0:
                        continue
                    l = self.enable(i, j)
                    if len(l) == 0:
                        ok = False
                        break
                    self.data[i][j] = l[random.randint(0,len(l)-1)]
            if ok == True:
                break
            else:
                k += 1
                if k%10000 == 0:
                    k = 0
                    k2 += 1
                    print(k2, "    ", time.time() - start)
                    self.show()
                    gc.collect()
        gc.enable()
        os.system("cls")
        print(k2 * 10000 + k + 1, "    ", time.time()-start)
        return self.data
            
    def legal(self):
        '''
        检测方阵本身是否合法
        '''
        c = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            if not self.legal9(self.data[i]):
                return False
        for i in range(9):
            if not self.legal9(self.data[:][i]):
                return False
        for i in range(3):
            for j in range(3):
                l = self.data[i*3:i*3+3][j*3:j*3+3]
                print(len(l))
                if not self.legal9(l):
                    return False
        return True
        
    def legal9(self, l):
        '''
        检测该行/列是否合法，合法则返回合法的数组，不合法则返回空数组
        '''
        #_l = [0,0,0,0,0,0,0,0,0,0]
        c = [1,2,3,4,5,6,7,8,9]
        for r in l:
            #_l[r] += 1
            if r in c:
                c.remove(r)
            #if (r != 0) and (_l[r] >= 2):
            elif r != 0:
                return []
        return c
        
    def enable(self, x, y):
        '''
        获取坐标(x, y)处可能可以获取的值
        '''
        c = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            if self.data[x][i] in c:
                c.remove(self.data[x][i])
        for i in range(9):
            if self.data[i][y] in c:
                c.remove(self.data[i][y])
        for i in range(3):
            for j in range(3):
                l = self.data[i*3:i*3+3][j*3:j*3+3]
                for z in l:
                    if z in c:
                        c.remove(z)
        return c
            
            
    def show(self):
        '''
        输出当前9x9矩阵
        '''
        for i in range(9):
            print(self.data[i])
        
            
            
         
# try:          
    # ShuDu()
# except:
    # traceback.print_exc()
# os.system("pause")
start = time.time()
for i in range(100):
    ShuDu()
    print("count: ", i+1 ,"total time: ", time.time() - start)
            