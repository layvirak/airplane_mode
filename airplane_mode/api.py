import frappe
import json

@frappe.whitelist(allow_guest=True)
def test_api(**kwargs):
    print('sssssss', kwargs)
    name = kwargs.get('name')
    username = kwargs.get('username')


    # if not frappe.db.exists("User", {'enabled': 1, 'name': name}):
    #     frappe.local.response['http_status_code'] = 404

    #     message = []

    #     return message
    
    response = frappe.db.get_list("User", fields=['name', 'username', 'email', 'full_name'], filters={'enabled': 1, 'name': name}, ignore_permissions=True)

    sql = f"""
            select
                name,
                username, 
                email, 
                full_name
            from `tabUser`
            where enabled = '1'
            and name = '{name}'
            """
    response_sql = frappe.db.sql(sql, as_dict=True)
    return response_sql

@frappe.whitelist(allow_guest=True)

def test_api_form():
    data = frappe.request.form
    name = data.get('name')
    print('ssssssss', data, name)


@frappe.whitelist(allow_guest=True)
def test_api_row():
    form_data = frappe.request.data
    data = json.loads(form_data)
    print('wwwwwwwww', data, type(data))
    name = data.get('name')

    return []


