import pyautogui
import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

while True:
	finished = pyautogui.locateOnScreen('imagem_render/tela_renderFinished.png', confidence=0.95, grayscale = 'true')
if finished is not None:
    	pyautogui.click('btn_chrome.png')
time.sleep(2)
pyautogui.click('btn_bruna.png')
time.sleep(2)
pyautogui.click('tela_pesquisaGoogle.png')
time.sleep(1)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(10)
chatOpen = pyautogui.locateOnScreen('imagem_render/tela_chatWpp.png', confidence=0.95, grayscale = 'true')
while chatOpen is None:
        sleep(15)
        chatOpen = pyautogui.locateOnScreen('imagem_render/tela_chatWpp.png', confidence=0.95, grayscale = 'true')
contato = pyautogui.locateOnScreen('imagem_render/tela_contatoRegis.png', confidence=0.95, grayscale = 'true')
if contato is not None:
        pyautogui.click('btn_contatoRegis.png')
        sleep(1)
        pyautogui.click('tela_chatRegis.png')
        pyautogui.write('Render Finalizado')
        pyautogui.press('enter')
        pyautogui.keyDown('alt')
        time.sleep(.2)
        pyautogui.press('tab')
        time.sleep(.2)
        pyautogui.keyUp('alt')



	
