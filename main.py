# This is a sample Python script
from Task1 import emp_data,Task1


class ControllerOfMethods:

    task1 = Task1(emp_data)

    list1 = [1, 2, 3, 4, 5, 6, 5, 7, 9]
    list2=[0,0,0,0,0,0,0,0,0]
    print("reverse the braek list")
    task1.reverse_list(list1)
    print("concatinate the two list")
    print(task1.concatenate_list(list1,list2))
    print("all details of employee")
    task1.all_details_of_emp()
    print("store employee")
    task1.store_emp()
    print("sanitise data")
    print(task1.sanitise_data())
    print("search data")
    print(task1.search(101))
    print("update salary")
    task1.update_salary(101,15000)
    print("check the final data")
    task1.all_details_of_emp()
