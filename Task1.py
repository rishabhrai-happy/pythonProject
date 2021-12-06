# This is a sample Python script
class Task1:
    def __init__(self, emp_data):
        self.emp_data = emp_data

    dummy_db = {}


    def split_list(self,passedlist):
        for i in range(0, len (passedlist), len (passedlist) // 3):
            yield passedlist[i:i + len(passedlist) // 3]
    def reverse_list(self,passed_list):
        passed_list=list((Task1.split_list(self,passed_list)))
        reversedlist =[]
        for i in  passed_list:
            reversedlist.append(i[::-1])
        print(reversedlist)


    def concatenate_list(self,first_li, second_li):
        res = []
        for i in range(len(first_li)):
            res.append(str(first_li[i]) +""+ str(second_li[i]))
        return res


    def all_details_of_emp(self):
        sorted_list = sorted(emp_data, key=lambda emp: emp[2], reverse=True)
        for sorted_emp in sorted_list:
            print(sorted_emp)


    def store_emp(self):
        for emp in emp_data:
            self.dummy_db[emp[0]] = dict(zip(["EmpID", "EmpName", "Salary"], emp))
        print(self.dummy_db)


    def sanitise_data(self):
        map = {}
        for index, emp in enumerate(emp_data):
            if emp[0] in map:
                emp_data.pop(index)
            else:
                map[emp[0]] = True


    def update_salary(self,emp_id, new_salary):
        for emp in emp_data:
            if emp[0] == emp_id:
                emp[2] = new_salary


    def search(self,emp_id):
        search_data = list(filter(lambda emp: emp[0] == emp_id, emp_data))
        return search_data


    def update_db_data(self):
        dummy_name_split = {}
        for i in range(len(emp_data)):
            dummy_name_split["EmpId"] = emp_data[i][0]
            fname, lname = (emp_data[i][1].split())
            dummy_name_split["Fname"] = fname
            dummy_name_split["Lname"] = lname
            dummy_name_split["Salary"] = emp_data[i][2]
            print(dummy_name_split)
emp_data = [
    [101, "ABC abc", 10000],
    [102, "XYZ xyz", 20000],
    [103, "XYZ xyz", 20000],
    [103, "xcb ncb", 5000]
]


