from BaseLink import base_link

expected_main_page_url = f'{base_link}admin/'

links = {
	'main_title': '/admin/',           			  # on the upper left corner
	'view_site': '/',                              # on the upper right corner
	'change_password': '/admin/password_change/',   # on the upper right corner
	'logout': '/admin/logout/',                     # on the upper right corner
	# authentication and authorization section
	'authentication_and_authorization': '/admin/auth/',  # under site_administration_link
	'groups': '/admin/auth/group/',                      # under authentication_and_authorization_link
	'users': '/admin/auth/user/',                        # under groups
	'add_group': '/admin/auth/group/add/',
	'change_group': '/admin/auth/group/',
	'add_user': '/admin/auth/user/add/',
	'change_user': '/admin/auth/user/',
	# postings section
	'postings': '/admin/postings/',  					# under users_link
	'blog_posts': '/admin/postings/blogpost/',           # under postings_link
	'add_blog_post': '/admin/postings/blogpost/add/',
	'change_blog_post': '/admin/postings/blogpost/',
}

