from ahk import AHK
from time import sleep

ahk = AHK()

ahk.key_down('alt')
ahk.key_press('tab')
ahk.key_up('alt')