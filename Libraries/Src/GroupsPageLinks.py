from BaseLink import base_link
import re

expected_groups_page_url = f'{base_link}admin/auth/group/'

links = {
  'home': '/admin/',
  'authentication_and_authorization': '/admin/auth/',
  'add_group': '/admin/auth/group/add/',
   # https://glacial-earth-31542.herokuapp.com/admin/auth/group/168/change/
  'added_group': re.escape('admin/auth/group/') + '(?:\d+)' + re.escape("/change")
}
