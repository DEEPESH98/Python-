import os
from pywinauto.application import Application

fsv = Application(backend="win32").start("FSViewerSetup46.exe")

fsv.InstallDialog.NextButton.wait('ready', timeout=30).click_input()
fsv.InstallDialog.IAgreeRadioButton.wait('ready', timeout=30).click_input()
fsv.InstallDialog.Edit.Wait('ready', timeout=30).type_keys(os.getcwd() + "\FastStone Image Viewer", with_spaces=True)
fsv.InstallDialog.InstallButton.wait('ready', timeout=30).click_input()
fsv.InstallDialog.FinishButton.wait('ready', timeout=30).click_input()
