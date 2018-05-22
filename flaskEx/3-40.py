class SiteItem(object):
    def __init__(self, href="", title="", children=[]):
        self.href = href
        self.title = title
        self.children = children

about = SiteItem("/about", "AboutUs")
contact_us = SiteItem("/contact", "ContactUs")

main_page = SiteItem("/", "MainPage", [about, contact_us])
second_page = SiteItem("/second", "SecondPage")

sitemap = [main_page, second_page]