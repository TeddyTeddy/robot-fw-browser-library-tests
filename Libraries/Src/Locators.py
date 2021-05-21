from ExpectedTexts import expected

locator = {
    'groups_page': {
        'breadcrumbs': '//*[@id="container"]/div[2]',
        'home_link': '//*[@id="container"]/div[2]/a[1]',
        'authentication_and_authorization_link': '//*[@id="container"]/div[2]/a[2]',
        'group_x_added_successfully': '//*[@id="container"]/ul/li[@class="success"]',
        'select_group_to_change': '//*[@id="content"]/h1',
        'add_group': '//*[@id="content-main"]/ul/li/a',
        'search_button': '//*[@id="changelist-search"]/div/input[2]',
        'action': '//*[@id="changelist-form"]/div[1]/label',
        'default_option':'//*[@id="changelist-form"]/div[1]/label/select',
        'delete_selected_groups_option': f'//*[@id="changelist-form"]/div[1]/label/select/option[contains(.,"{expected["groups_page"]["delete_selected_groups_option_text"]}")]',
        'delete_selected_groups_option_2': '//select[@name="action"]',
        'go_button': '//*[@id="changelist-form"]/div[1]/button',
        'x_of_y_selected': '//*[@id="changelist-form"]/div[1]/span',
        'select_all_groups': '//*[@id="result_list"]/thead/tr/th[2]/div[1]/span',
        'generic_group_element_checkbox': '//*[@id="result_list"]/tbody/tr[contains(.,"%s")]/td/input[@type="checkbox"]',
        'generic_group_element': '//table[@id="result_list"]/tbody/tr/th/a[contains(.,"%s")]',
        'y_groups': '//*[@id="changelist-form"]/p',
    },
    'confirm_groups_deletions_page': {
        'breadcrumbs': '//*[@id="container"]/div[2]',
        'home': '//*[@id="container"]/div[2]/a[1]',
        'authentication_and_authorization': '//*[@id="container"]/div[2]/a[2]',
        'groups': '//*[@id="container"]/div[2]/a[3]',
        'are_you_sure_headline': '//*[@id="content"]/h1',
        'are_you_sure_question': '//*[@id="content"]/p',
        'summary': '//*[@id="content"]/h2[1]',
        'objects': '//*[@id="content"]/h2[2]',
        'generic_group_element': '//*[@id="content"]/ul[2]/li/a[contains(.,"%s")]',
        'confirm_deletion_button': '//*[@id="content"]/form/div/input[4]',
        'cancel_deletion_button': '//*[@id="content"]/form/div/a',
    }
}