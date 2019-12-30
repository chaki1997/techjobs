import re




data = {'starter': {'prof_title': 'Djaaango Developer asdasdadadasd', 'prof_overview': '', 'profile_image': None, 'status': 'Freelancer'},
        'education': {'school': 'pirveli', 'started': '2014', 'ended': '2014','degree': '', 'area_of_study': '', 'Description': '', 'repeat': False},
        'first_education': None,
        'second_education': None,
        'employment': {'company': 'Travel club', 'title': '', 'location': '', 'role': 'Accountancy', 'period_sterted': '', 'period_ended': '', 'is_current': False, 'description': '', 'repeat': False},
        'first_employment': None,
        'second_employment': None,
        'hour_rate': {'language_compatancy': 'zxc', 'availability': 'More Then 30hr', 'hourly_rate': 123}, 'proficiency': {'language_compatancy': 'Conversational', 'category_industry': 'FMCG'},
        'location': {'language_compatancy': '', 'phone': '<phone_field.phone_number.PhoneNumber object at 0x000000000522DF98>', 'address_1': '', 'address_2': '', 'city': '', 'zip_code': '', 'country':'', 'phone_number': ''}}


job_data = {'Status': 'freelancer',
            'job_title': 'Project Manager',
            'prof_description': 'asd',
            'country': 'aaa',
            'budjet': 200,
            'category': 'Accountancy'}

def job_moderation(job_data):
    pass
    pattern = {'3l': r'(\w)\1\1', 'asd': 'asd', 'zxc': 'zxc'}
    n_number_of_empty = 0
    regex_count = 0
    k_number_of_fields = 0

    for key in job_data.keys():
        #print (key)
        k_number_of_fields+=1
        if job_data[key] == '' or job_data[key] == None:
            n_number_of_empty += 1
        for pat in pattern.keys():
            #print (job_data[key])
            #print (pattern[pat])
            #print (job_data[key])
            try:
                if re.search(pattern[pat], job_data[key]):
                    regex_count += 1
                    #print(job_data[key])
                    #print(regex_count)
            except:
                TypeError


    print ('number of fields {}'.format(k_number_of_fields))
    print ('number of empty fileds {}'.format(n_number_of_empty))
    print ('number of wrong matches {}'.format(regex_count))

    if n_number_of_empty >1:
        return False
    if regex_count >0:
        return False
    return True

job_moderation(job_data)


def moderation(data):
    pattern={'3l':r'(\w)\1\1','asd':'asd','zxc':'zxc','hjk':'hjk','tyu':'tyu'}
    regex_count = 0
    n_number_of_empty=0
    k_number_of_fields=0
    #print(data)
    for key in data.keys():

        #print (data[key])
        try:
            for key_in in data[key].keys():
                #print (data[key][key_in])
                #print('i')
                k_number_of_fields+=1
                if data[key][key_in] == '' or data[key][key_in] == None:
                    n_number_of_empty+=1
                for pat in pattern.keys():

                    if re.search(pattern[pat], data[key][key_in]):
                        print(data[key][key_in])
                        regex_count+=1
                '''
                MONITOR
                regex = re.compile(r"((?:asd){1})")
                match = regex.search(data[key][key_in])
                print(match.group())
                '''
        except:
            AttributeError
    #MONITOR
    #empty_share = (n_number_of_empty / k_number_of_fields) * 100

    print ('number of empty fields is {}'.format(n_number_of_empty))
    print('number of fields is {}'.format(k_number_of_fields))

    #print('Percent of empty fields are {}'.format((n_number_of_empty / k_number_of_fields) * 100))
    print ('number of wrong matches are {}'.format(regex_count))
    if regex_count > 2:
        return False
    if k_number_of_fields != 0:
        print('Percent of empty fields are {}'.format((n_number_of_empty / k_number_of_fields) * 100))
        if (n_number_of_empty/k_number_of_fields)*100 >50:
            return False
    return True


#moderation(data)

word = 'asdaaasd'

if re.search(r'(\w)\1\1', ''):
    print('regex')

asd=re.compile(r"((?:asd){1})")
search = asd.search('assasdasd')
#print (search.group())