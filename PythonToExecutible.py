# Program to convert .py file into .exe (useful as if the project we made is really great and we want to share it with people, so it will be a necessity for them to download python interpreter first, to overcome that, this program will help us to convert the .py file into .exe file)


# Method 1
# open powershell and type > python -m PyInstaller [Script Name or Path]
# this will create all the necessary and extra files in the current directory but we only need the .exe file, so to get that only we will type (the executable is in dist folder)
# python -m PyInstaller --onefile [Script Name or Path]
# this will also create necessary and some extra files, but the single exe file will be located in dist folder, and now we can share it with our friends 
# this method is good, but what if we want to customise the build, adding icon, combining multiple .py files to create one .exe, for that we will use method 2

# Method 2
# install > pip install auto-py-to-exe --user
# open powershell > python -m auto-py-to-exe
# now browse the file(s), add icon and check other settings and finally click on convert
# it will convert the .py file(s) to a single .exe file