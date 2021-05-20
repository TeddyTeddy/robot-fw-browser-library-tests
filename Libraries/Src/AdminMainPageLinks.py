from BaseLink import base_link

expected_admin_main_page_url = f'{base_link}admin/'

main_title_link= '/admin/'           			  # on the upper left corner
view_site_link= '/'                               # on the upper right corner
change_password_link= '/admin/password_change/'   # on the upper right corner
logout_link= '/admin/logout/'                     # on the upper right corner
# authentication and authorization section
authentication_and_authorization_link= '/admin/auth/'  # under site_administration_link
groups_link= '/admin/auth/group/'                      # under authentication_and_authorization_link
users_link= '/admin/auth/user/'                        # under groups
add_group_link= '/admin/auth/group/add/'
change_group_link= '/admin/auth/group/'
add_user_link= '/admin/auth/user/add/'
change_user_link= '/admin/auth/user/'
# postings section
postings_link= '/admin/postings/'  					# under users_link
blog_posts_link= '/admin/postings/blogpost/'           # under postings_link
add_blog_post_link= '/admin/postings/blogpost/add/'
change_blog_post_link= '/admin/postings/blogpost/'