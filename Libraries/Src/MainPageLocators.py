from MainPageTexts import texts

locators = {
	'main_title': '//*[@id="site-name"]/a',             # on the upper left corner
	'welcome_user_x': '//*[@id="user-tools"]',          # on the upper right corner the navigation bar for the user
	'view_site': '//*[@id="user-tools"]/a[1]',          # on the upper right corner
	'change_password': '//*[@id="user-tools"]/a[2]',    # on the upper right corner
	'logout': '//*[@id="user-tools"]/a[3]',    			# on the upper right corner
	# TODO: if logout locator below is used, cannot find the element in MainPage.verify_url() method
	# 'logout': f'//*[@id="user-tools"]/a[contains(.,"{texts["logout"]}")]',             # on the upper right corner
	'site_administration': '//*[@id="content"]/h1',      # under main_title
	# authentication and authorization section
	'authentication_and_authorization': '//*[@id="content-main"]/div[1]/table/caption/a',  # under site_administration
	'groups': '//*[@id="content-main"]/div[1]/table/tbody/tr[1]/th/a', # under authentication and authorization
	'users': '//*[@id="content-main"]/div[1]/table/tbody/tr[2]/th/a',  # under groups
	'add_group': '//*[@id="content-main"]/div[1]/table/tbody/tr[1]/td[1]/a',
	'change_group': '//*[@id="content-main"]/div[1]/table/tbody/tr[1]/td[2]/a',
	'add_user': '//*[@id="content-main"]/div[1]/table/tbody/tr[2]/td[1]/a',
	'change_user': '//*[@id="content-main"]/div[1]/table/tbody/tr[2]/td[2]/a',
	# postings section
	'postings': '//*[@id="content-main"]/div[2]/table/caption/a',      # under users
	'blog_posts': '//*[@id="content-main"]/div[2]/table/tbody/tr/th/a',     # under postings
	'add_blog_post': '//*[@id="content-main"]/div[2]/table/tbody/tr/td[1]/a',
	'change_blog_post': '//*[@id="content-main"]/div[2]/table/tbody/tr/td[2]/a',
	# generic add and change buttons
	'add_button': f'//div[@id="content-main"]//a[contains(., {texts["add_button"]})]',    		# in the upper center 3 of them
	'change_button': f'//div[@id="content-main"]//a[contains(., {texts["change_button"]})]',    # in the upper center 3 of them
	# Recent Actions section
	'recent_actions': '//div[@id="recent-actions-module"]/h2',  # right column in the middle
	'my_actions': '//*[@id="recent-actions-module"]/h3',
}
