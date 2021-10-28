from pyprc import *
import os
import time
import traceback

labels = False
while labels == False:
    try:
        hash.load_labels("ParamLabels.csv")
        labels = True
    except:
        print('no "ParamLabels.csv" file found, are you sure you have it in the same directory as the script with the correct name?')
        time.sleep(2)
        exit()

print('SSBU DOF Editor Script.\nThis will create a new directory called "DOF Mod" next to your stage folder.\nMake sure you have all the stages with the render_param.prc files as they appear in the data.arc.')

stgdir = str(input("Copy and paste your stage directory: "))
dofMode = int(input("DOF Mode (0 = Off, 1 = On): "))
startFocus = int(input("Enter focus start (0 = closest, starts just behind stage): "))
endFocus = int(input("Enter end focus: "))
irisCount = int(input("Enter iris count (Anything over 6 not recommended): "))

with open("log.txt", "w") as log:
    try:
        for root, dir, files in os.walk(stgdir):
            if "render_param.prc" in files:
                currentdir = str(os.path.join(root, "render_param.prc"))
                root = param(os.path.join(root, "render_param.prc"))
                h = root[hash("depth_of_field")]
                h[hash("mode")].value = dofMode
                h[hash(0x0f09c31ed4)].value = irisCount
                h[hash("focus_start")].value = startFocus
                h[hash("focus_end")].value = endFocus
                modDirList = currentdir.split("\\")
                modDirList.pop(len(modDirList) - 1)
                modDirList[len(modDirList) - 5] = "DOF Mod"
                modDir = "/".join(modDirList)
                os.makedirs(modDir)
                modDir = modDir + "/render_param.prc"
                root.save(modDir)
                print("Replaced param at {}".format(modDir))
        stgDirlst = stgdir.split("\\")
        if "stage" in stgDirlst:
            stgDirlst[stgDirlst.index("stage") - 1] = "DOF MOD"
            #stgDirlst[len(stgDirlst) - 2] = "DOF Mod"
        else:
            stgDirlst = modDirList
            for i in range(len(modDirList) - 1, len(modDirList) - 5, -1):
                stgDirlst.pop(i)
        exportDir = "/".join(stgDirlst)
        print("Success! You can find the mod folder at {}.".format(exportDir))
        time.sleep(2)
    except Exception:
        traceback.print_exc(file=log)
        print("Failed to complete mod. Check log for details.")
        time.sleep(3)


        






