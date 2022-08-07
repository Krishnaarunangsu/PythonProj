import json

employee_dict = [
    {
        'emp_id': 'emp_1',
        'emp_name': 'John',
        'dob': '18/12/90',
        'emp_address': {
            'perm_address': 'Howrah',
            'corr_address': 'Saltlake'
        }
    },
    {
        'emp_id': 'emp_2',
        'emp_name': 'Tom',
        'dob': '17/12/91',
        'emp_address': {
            'perm_address': 'Midnapur',
            'corr_address': 'Gariahut'
        }
    }
]

employee_dict_2 = {
    'emp_1': {

        'emp_name': 'John',
        'dob': '18/12/90',
        'emp_address': {
            'perm_address': 'Howrah',
            'corr_address': 'Saltlake'
        }
    },
    'emp_2': {
        'emp_name': 'Tom',
        'dob': '17/12/91',
        'emp_address': {
            'perm_address': 'Midnapur',
            'corr_address': 'Gariahut'
        }
    }
}

print(json.dumps(employee_dict[0], sort_keys=False, indent=4))
