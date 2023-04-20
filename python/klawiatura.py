import ctypes
VK_LSHIFT = 0xa0
GetAsyncKeyState = ctypes.windll.user32.GetAsyncKeyState
x = GetAsyncKeyState(VK_LSHIFT)
if x&0x8000:
    print("Shift clicked")
else:
    print("Shift nie wcisniety")