class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        """Переход на нужную страницу"""
        self.page.goto(url)

    def wait_for_element(self, selector):
        """Ожидание появления элемента"""
        self.page.wait_for_selector(selector)
