import pytest
from pages.note_page import NotePage

@pytest.mark.ui
def test_sidebar_new_note_button(page):
    """Тест нажатия кнопки 'New note' в боковой панели"""
    print("\n🔄 Запуск test_sidebar_new_note_button")
    note_page = NotePage(page)
    note_page.open()

    # Нажимаем кнопку 'New note'
    assert note_page.click_new_note_button(), "❌ Кнопка 'New note' не нажалась!"
    print("✅ Кнопка 'New note' успешно нажата!")

@pytest.mark.ui
def test_scratchpad_button(page):
    """Тест на проверку работы кнопки 'Scratchpad'"""
    print("\n🔄 Запуск test_scratchpad_button")
    note_page = NotePage(page)
    note_page.open()

    # Нажимаем кнопку Scratchpad
    assert note_page.click_scratchpad_button(), "❌ Не удалось нажать кнопку 'Scratchpad'!"
    print("✅ Кнопка 'Scratchpad' успешно нажата!")

@pytest.mark.ui
def test_notes_button(page):
    """Тест на проверку работы кнопки 'Notes'"""
    print("\n🔄 Запуск test_notes_button")
    note_page = NotePage(page)
    note_page.open()

    # Нажимаем кнопку Notes
    assert note_page.click_notes_button(), "❌ Не удалось нажать кнопку 'Notes'!"
    print("✅ Кнопка 'Notes' успешно нажата!")

@pytest.mark.ui
def test_favorites_button(page):
    """Тест на проверку работы кнопки 'Favorites'"""
    print("\n🔄 Запуск test_favorites_button")
    note_page = NotePage(page)
    note_page.open()

    # Нажимаем кнопку Favorites
    assert note_page.click_favorites_button(), "❌ Не удалось нажать кнопку 'Favorites'!"
    print("✅ Кнопка 'Favorites' успешно нажата!")

@pytest.mark.ui
def test_trash_button(page):
    """Тест на проверку работы кнопки 'Trash'"""
    print("\n🔄 Запуск test_trash_button")
    note_page = NotePage(page)
    note_page.open()

    # Создаем тестовую заметку, чтобы было что удалять
    note_page.add_note("Temporary Note", "This note will be deleted.")

    # Нажимаем кнопку Trash
    assert note_page.click_trash_button(), "❌ Не удалось нажать кнопку 'Trash'!"
    print("✅ Кнопка 'Trash' успешно нажата!")