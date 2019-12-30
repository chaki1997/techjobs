form_list=[{'prof_title': 'django developer', 'prof_overview': 'javascript python'},
           {'school': 'pirveli', 'started': '1915', 'ended': '1918', 'degree': 'bachalor', 'area_of_study': 'mathemathics', 'Description': 'management of informational technology'},
           {'language_compatancy': 'Conversational'},{'language_compatancy': 'Conversational'}]

form_list_full = [{'prof_title': 'Django Developer', 'prof_overview': 'Javascript Python', 'repeat': False},
                  {'school': 'pirveli', 'started': '1904', 'ended': '1902', 'degree': 'bachalor','area_of_study': 'mathemathics', 'Description': 'My first degree', 'repeat': True},
                  {'school': 'meore', 'started': '1902', 'ended': '1903', 'degree': 'Master', 'area_of_study': 'Finance','Description': 'my second degree', 'repeat': False},
                  {'company': 'Travel club', 'title': 'content manager', 'location': 'tbilisi', 'role': 'Accounting Director', 'period_sterted': '1906','period_ended': '1909', 'is_current': False, 'description': 'My first job', 'repeat': True},
                  {'company': 'Algorithm', 'title': 'sales manager', 'location': 'tbilisi','role':'Budget Analyst','period_sterted': '1908', 'period_ended': '1905', 'is_current': True, 'description': 'my current job', 'repeat': False},
                  {'language_compatancy': '', 'repeat': False,'hourly_rate': 20},
                  {'language_compatancy': 'Fluent', 'category_industry': 'Accounts Payable/Receivable Clerk', 'repeat': False},
                  {'language_compatancy': '','availability':'Less Then30hr', 'address_1': 'tbilisi machabeli st 14', 'address_2': 'tbilisi machabeli st 14', 'city': 'tbilisi', 'zip_code': '0104', 'country': 'Georgia'}]

def sort_forms_data(form_list):
    form_dict = {}
    form1=[]
    form2=[]
    form3=[]
    for form in form_list:

        if 'prof_title' in form.keys():
            form1.append(form)
            form_dict['form1']=form1
        elif 'school' in form.keys():
            form2.append(form)
            form_dict['form2']=form2
        elif 'language_compatancy' in form.keys():
            form3.append(form)
            form_dict['form3']=form3
    #form_dict['form1':form1,'form2':form2,'form3':form3]
    return form_dict

#print(sort_forms_data(form_list))
dict1 = {'1':1}
dict2 = {'1':1,'2':2,'3':3}
dict3 = {'1':1,'2':4,'3':5}
