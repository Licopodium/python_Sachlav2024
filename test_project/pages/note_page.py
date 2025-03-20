from pages.base_page import BasePage
from playwright.sync_api import Page

class NotePage(BasePage):
    URL = "https://takenote.dev/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def open(self):
        """Открывает главную страницу и переходит в приложение"""
        self.navigate(self.URL)
        self.wait_for_element("text=View Demo")
        self.page.click("text=View Demo")
        self.wait_for_element("button:has-text('New note')")

    def get_notes(self):
        """Возвращает список всех заметок"""
        self.page.wait_for_timeout(2000)
        notes_list = self.page.locator("div.note-list-outer")
        return notes_list.all_inner_texts()

    def add_note(self, title, content):
        """Создает новую заметку"""
        self.page.click("button:has-text('New note')")
        self.page.wait_for_selector(".CodeMirror", timeout=5000)

        editor = self.page.locator(".CodeMirror")
        editor.click()
        self.page.keyboard.insert_text(title)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(500)
        self.page.keyboard.insert_text(content)

        self.page.wait_for_timeout(3000)
        self.page.click("text=Notes")
        self.page.wait_for_selector("div.note-list-outer", timeout=10000)

    def _open_context_menu(self, note_title):
        """Открывает контекстное меню заметки"""
        note_item = self.page.locator(f"div.note-list-outer:has-text('{note_title}')")
        if note_item.count() == 0:
            print(f"❌ Заметка '{note_title}' не найдена!")
            return False

        note_item.click()
        self.page.wait_for_timeout(1000)
        three_dots_selector = "#root > div > div > div.Pane.vertical.Pane2 > div > div.Pane.vertical.Pane1 > aside > div.note-list > div.note-list-each.selected > div.note-list-outer > div.note-options"
        self.page.locator(three_dots_selector).hover()
        self.page.wait_for_timeout(500)
        self.page.locator(three_dots_selector).click(force=True)
        self.page.wait_for_timeout(1000)

        context_menu_selector = "#context-menu > div > div"
        if not self.page.locator(context_menu_selector).is_visible():
            print("❌ Контекстное меню не появилось!")
            return False

        print(f"✅ Контекстное меню открыто для заметки '{note_title}'!")
        return True

    def click_first_context_menu_button(self, note_title):
        """Нажимает первую кнопку в контекстном меню для заметки"""
        self._open_context_menu(note_title)
        self.page.click("#context-menu > div > div > nav > div:nth-child(1)")
        self.page.wait_for_timeout(1000)
        print(f"✅ Первая кнопка в контекстном меню успешно нажата для заметки '{note_title}'!")
        return True

    def click_delete_context_menu_button(self, note_title):
        """Нажимает кнопку удаления в контекстном меню"""
        self._open_context_menu(note_title)
        self.page.click("#context-menu > div > div > nav > div.nav-item.delete-option")
        self.page.wait_for_timeout(1000)
        print(f"✅ Заметка '{note_title}' успешно удалена через контекстное меню!")
        return True

    def click_download_context_menu_button(self, note_title):
        """Нажимает кнопку загрузки в контекстном меню"""
        self._open_context_menu(note_title)
        self.page.click("#context-menu > div > div > nav > div:nth-child(3)")
        self.page.wait_for_timeout(1000)
        print(f"✅ Файл заметки '{note_title}' успешно скачан через контекстное меню!")
        return True

    def click_copy_reference_context_menu_button(self, note_title):
        """Нажимает кнопку копирования референса в контекстном меню"""
        self._open_context_menu(note_title)
        self.page.click("#context-menu > div > div > nav > div:nth-child(4)")
        self.page.wait_for_timeout(1000)
        print(f"✅ Кнопка копирования референса успешно нажата для заметки '{note_title}'!")
        return True

    def delete_note(self, title):
        """Удаляет заметку по названию"""
        self.page.wait_for_timeout(2000)
        notes_list = self.get_notes()

        if not any(title in note for note in notes_list):
            print(f"❌ Заметка '{title}' не найдена для удаления!")
            return False

        note_item = self.page.locator(f"div.note-list-outer:has-text('{title}')")
        note_item.click()
        self.page.wait_for_timeout(1500)

        delete_button = self.page.locator("button.note-menu-bar-button.trash")
        if not delete_button.is_visible():
            print("❌ Кнопка удаления не найдена!")
            return False

        delete_button.hover()
        self.page.wait_for_timeout(1500)
        delete_button.click()
        self.page.wait_for_timeout(2000)

        remaining_notes = self.get_notes()
        if any(title in note for note in remaining_notes):
            print(f"❌ Ошибка! Заметка '{title}' осталась после удаления!")
            return False

        print(f"✅ Заметка '{title}' успешно удалена.")
        return True

    def open_note(self, title):
        """Открывает заметку по заголовку"""
        self.page.wait_for_selector("div.note-list-outer", timeout=5000)
        note_item = self.page.locator(f"div.note-list-outer:has-text('{title}')")

        if note_item.count() == 0:
            print(f"❌ Заметка '{title}' не найдена!")
            return False

        note_item.click()
        self.page.wait_for_timeout(1000)
        print(f"✅ Заметка '{title}' открыта.")
        return True

    def add_to_favorites(self):
        """Добавляет текущую открытую заметку в избранное (нижняя панель)"""
        favorite_button_selector = "#root > div > div > div.Pane.vertical.Pane2 > div > div.Pane.vertical.Pane2 > main > section > nav:nth-child(1) > button:nth-child(2)"

        self.page.wait_for_selector(favorite_button_selector, state="visible", timeout=5000)
        self.page.click(favorite_button_selector)
        self.page.wait_for_timeout(1000)

        print("✅ Заметка успешно добавлена в избранное!")
        return True

    def click_copy_note_button(self):
        """Нажимает кнопку 'Copy Note'"""
        copy_button_selector = "#root > div > div > div.Pane.vertical.Pane2 > div > div.Pane.vertical.Pane2 > main > section > nav:nth-child(1) > button.note-menu-bar-button.uuid"

        self.page.wait_for_selector(copy_button_selector, state="visible", timeout=5000)
        self.page.click(copy_button_selector)
        self.page.wait_for_timeout(1000)

        print("✅ Кнопка 'Copy Note' успешно нажата!")
        return True

    def click_new_note_button(self):
        """Нажимает кнопку 'New note' в боковой панели"""
        new_note_button = "#root > div > div > div.Pane.vertical.Pane1 > aside > button"
        self.page.wait_for_selector(new_note_button, state="visible", timeout=5000)
        self.page.click(new_note_button)
        self.page.wait_for_timeout(1000)
        print("✅ Кнопка 'New note' успешно нажата!")
        return True

    def click_scratchpad_button(self):
        """Нажимает кнопку 'Scratchpad' в боковой панели"""
        scratchpad_button = "#root > div > div > div.Pane.vertical.Pane1 > aside > section > button:nth-child(1)"
        self.page.wait_for_selector(scratchpad_button, state="visible", timeout=5000)
        self.page.click(scratchpad_button)
        self.page.wait_for_timeout(1000)
        print("✅ Кнопка 'Scratchpad' успешно нажата!")
        return True
    def click_notes_button(self):
        """Нажимает кнопку 'Notes' в боковой панели"""
        notes_button = "#root > div > div > div.Pane.vertical.Pane1 > aside > section > button:nth-child(2)"
        self.page.wait_for_selector(notes_button, state="visible", timeout=5000)
        self.page.click(notes_button)
        self.page.wait_for_timeout(1000)
        print("✅ Кнопка 'Notes' успешно нажата!")
        return True

    def click_favorites_button(self):
        """Нажимает кнопку 'Favorites' в боковой панели"""
        favorites_button = "#root > div > div > div.Pane.vertical.Pane1 > aside > section > button:nth-child(3)"
        self.page.wait_for_selector(favorites_button, state="visible", timeout=5000)
        self.page.click(favorites_button)
        self.page.wait_for_timeout(1000)
        print("✅ Кнопка 'Favorites' успешно нажата!")
        return True

    def click_trash_button(self):
        """Нажимает кнопку 'Trash' в боковой панели"""
        trash_button = "#root > div > div > div.Pane.vertical.Pane1 > aside > section > button:nth-child(4)"
        self.page.wait_for_selector(trash_button, state="visible", timeout=5000)
        self.page.click(trash_button)
        self.page.wait_for_timeout(2000)

        print("✅ Кнопка 'Trash' успешно нажата!")
        return True









