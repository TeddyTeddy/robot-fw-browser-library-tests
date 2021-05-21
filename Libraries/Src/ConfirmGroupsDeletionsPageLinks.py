import re
from BaseLink import base_link

expected_confirmation_page_url = f'{base_link}admin/auth/group/'

links = {
   'home': '/admin/',
   'authentication_and_authorization': '/admin/auth/',
   'groups': '/admin/auth/group/',
   'cancel_deletion_button': '#',
   'group_to_be_deleted': re.escape('admin/auth/group/') + '(?:\d+)' + re.escape("/change")
}
