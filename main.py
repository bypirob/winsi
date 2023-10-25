import win32gui

new_width = 1920
new_height = 1080
ctx = { "window": 0, "count": 0 }

def printWindowInfo(window):
    print(window, " - ", win32gui.GetWindowText(window))

def getPreviousActiveWindow( w, ctx ):
    if ctx["count"] < 2 and win32gui.IsWindowVisible( w ) and win32gui.GetWindowText(w) != "":
        ctx["window"] = w
        ctx["count"] += 1

win32gui.EnumWindows( getPreviousActiveWindow, ctx)

if ctx["window"] == 0:
    print("Window not found!!")
    exit()

printWindowInfo(ctx["window"])

x0, y0, x1, y1 = win32gui.GetWindowRect(ctx["window"])
print("width: ", x1 - x0)
print("height: ", y1 - y0)
win32gui.MoveWindow(ctx["window"], x0, y0, new_width, new_height, False)
