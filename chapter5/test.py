from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyautogui
import tkinter as tk
driver = webdriver.Edge()
driver.get("file:///E:/NIKLEARNING/projects/monday/python_for_hack_shanbe/chapter5/index.html")


def set_score():
    score = entry.get()
    driver.execute_script(f"score = {score};document.getElementById('score').innerText = 'Score:' + score")


window = tk.Tk()
entry = tk.Entry(window)
entry.pack()
btn = tk.Button(window, text="تنظیم امتیاز", command=set_score)
btn.pack()
window.mainloop()





# score =  driver.find_element(By.CSS_SELECTOR, '#score')
# print("****************",score.text)
