import re
from BaseLink import base_link

expected_groups_page_url = f'{base_link}admin/auth/group/'

links = {
    'groups_page': {
        'home_link': '/admin/',
        'authentication_and_authorization_link': '/admin/auth/',
        'add_group_link': '/admin/auth/group/add/',
        # https://glacial-earth-31542.herokuapp.com/admin/auth/group/168/change/
        'added_group_link': re.escape('admin/auth/group/') + '(?:\d+)' + re.escape("/change")
    },
    'confirm_groups_deletions_page': {
        'home_link': '/admin/',
        'authentication_and_authorization_link': '/admin/auth/',
        'groups_link': '/admin/auth/group/',
        'cancel_deletion_button_link': '#',
        'group_to_be_deleted_link': re.escape('admin/auth/group/') + '(?:\d+)' + re.escape("/change")
    }
}
