from AddGroupPageTexts import texts

BLOG_EDITORS_PERMISSIONS = [texts['postings_blog_post_can_add_blog_post'],
                            texts['postings_blog_post_can_change_blog_post'],
                            texts['postings_blog_post_can_delete_blog_post']]

GROUP_EDITORS_PERMISSIONS = [texts['auth_group_can_add_group'],
                             texts['auth_group_can_change_group'],
                             texts['auth_group_can_delete_group']]


def get_variables():
    variables = {
        'BROWSER': 'ff',
        'CREDENTIALS': {
                'valid_admin': {
                    'username': 'hakan',
                    'password': 'h1a2k3a4',
                },
        },
        'BLOG_EDITORS_PERMISSIONS': BLOG_EDITORS_PERMISSIONS,
        'GROUP_EDITORS_PERMISSIONS': GROUP_EDITORS_PERMISSIONS,
        'BLOG_EDITORS_GROUP_NAME': 'blog_editors',
        'GROUP_EDITORS_GROUP_NAME': 'group_editors'
    }
    return variables

