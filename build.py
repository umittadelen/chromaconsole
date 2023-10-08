import os

package_directory = "package"
os.chdir(package_directory)

while True:
    answer = input("1: install library\n2: uninstall library\n3: build\n4: upload to test.pypi.org\n5: upload to pypi.org\n\n>")

    if answer == '1':
        os.system("pip install chromaconsole")
    elif answer == '2':
        os.system("pip uninstall chromaconsole")
    elif answer == '3':
        os.system("py -m build")
    elif answer == '4':
        os.system("py -m twine upload --repository testpypi dist/*")
    elif answer == '5':
        os.system("py -m twine upload --repository pypi dist/*")
    else:
        print("Invalid choice. Please select a valid option.")
