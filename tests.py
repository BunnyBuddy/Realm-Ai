# from functions.get_file_content import get_file_content
# from functions.get_files_info import get_files_info
# from functions.write_file import write_file
from functions.run_python import run_python_file


def test():
    ### FOR TESTING GET_FILES_INFO FUNCTION
    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(result)
    # print("")

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)

    # result = get_files_info("calculator", "/bin")
    # print("Result for '/bin' directory:")
    # print(result)

    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(result)

    ### FOR TESTING GET_FILE_CONTENT FUNCTION
    # result = get_file_content("calculator", "main.py")
    # print("Result for 'main.py' file:")
    # print(result)

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for 'main.py' file:")
    # print(result)
    
    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for 'main.py' file:")
    # print(result)
    
    # result = get_file_content("calculator", "pkg/does_not_exist.py")
    # print("Result for 'main.py' file:")
    # print(result)
    
    ### FOR TESTING WRITE_FILE FUNCTION
    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print(result)
    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print(result)
    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print(result)
    
    ### FOR TESTING RUN_PYTHON FUNCTION
    result = run_python_file("calculator", "main.py")
    print(result)
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    result = run_python_file("calculator", "tests.py")
    print(result)
    result = run_python_file("calculator", "../main.py")
    print(result)
    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    
if __name__ == "__main__":
    test()
