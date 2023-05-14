from time import sleep
import pyautogui as pygui
import pyperclip


class ImageGenerator(object):
    '''Generates images using the given prompt and copies them
    to the clipboard.
    '''
    
    def __init__(self, prompt: str = '') -> None:
        self.prompt = prompt

    def generate_image(self, prompt: str) -> None:
        '''The main function for the image generation.
        
        Args:
            prompt: prompt used for the generation. Not modified
            inside the function.
        '''

        # HACK: aidungeon pastes some symbols that stop pyautogui to
        # just write it. Thus, pyperclip is used
        prompt = prompt or self.prompt
        pyperclip.copy(prompt)
        pygui.press('win')
        pygui.sleep(1)
        pygui.write('google chrome', interval=0.05)
        pygui.sleep(1)
        pygui.press('enter')
        pygui.sleep(0.5)
        for _ in range(4):
            pygui.hotkey('win', 'up')
            pygui.sleep(0.01)
        pygui.sleep(4)
        pygui.write('https://www.bing.com/create', interval=0.05)
        pygui.sleep(0.1)
        pygui.press('enter')
        pygui.sleep(7)
        pygui.click(x=401, y=185)
        pygui.write(pyperclip.paste(), interval=0.02)
        pygui.press('enter')
        pygui.sleep(37)
        pygui.leftClick(x=488, y=422)
        pygui.sleep(5)
        pygui.rightClick()
        pygui.sleep(2)
        pygui.leftClick(542, 483)
        sleep(2)
        pygui.hotkey('alt', 'f4', interval=0.5)
