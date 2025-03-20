import pytest
from pages.note_page import NotePage

@pytest.mark.ui
def test_first_button_in_context_menu(page):
    """Тест на проверку работы первой кнопки в контекстном меню"""
    print("\n🔄 Запуск test_first_button_in_context_menu")
    note_page = NotePage(page)
    note_page.open()

    # Создаем тестовую заметку
    note_title = "Context Menu Test Note"
    note_content = "This is a test note for context menu."
    note_page.add_note(note_title, note_content)

    # Проверяем, что заметка появилась
    notes_list = note_page.get_notes()
    assert any(note_title in note for note in notes_list), "❌ Заметка не была создана!"

    # Нажимаем первую кнопку в контекстном меню
    assert note_page.click_first_context_menu_button(note_title), "❌ Не удалось нажать первую кнопку в контекстном меню!"

    print(f"✅ Первая кнопка в контекстном меню успешно нажата для заметки '{note_title}'!")

@pytest.mark.ui
def test_delete_button_in_context_menu(page):
    """Тест на проверку работы кнопки удаления в контекстном меню"""
    print("\n🔄 Запуск test_delete_button_in_context_menu")
    note_page = NotePage(page)
    note_page.open()

    # Создаем тестовую заметку
    note_title = "Context Menu Delete Test"
    note_content = "This note will be deleted via context menu."
    note_page.add_note(note_title, note_content)

    # Проверяем, что заметка появилась
    notes_list = note_page.get_notes()
    assert any(note_title in note for note in notes_list), "❌ Заметка не была создана!"

    # Нажимаем кнопку удаления в контекстном меню
    assert note_page.click_delete_context_menu_button(note_title), "❌ Не удалось удалить заметку через контекстное меню!"


@pytest.mark.ui
def test_download_button_in_context_menu(page):
    """Тест на проверку работы кнопки загрузки в контекстном меню"""
    print("\n🔄 Запуск test_download_button_in_context_menu")
    note_page = NotePage(page)
    note_page.open()

    # Создаем тестовую заметку
    note_title = "Context Menu Download Test"
    note_content = "This note will be downloaded via context menu."
    note_page.add_note(note_title, note_content)

    # Проверяем, что заметка появилась
    notes_list = note_page.get_notes()
    assert any(note_title in note for note in notes_list), "❌ Заметка не была создана!"

    # Нажимаем кнопку загрузки в контекстном меню
    assert note_page.click_download_context_menu_button(note_title), "❌ Не удалось скачать заметку через контекстное меню!"


@pytest.mark.ui
def test_copy_reference_button_in_context_menu(page):
    """Тест на проверку работы кнопки копирования референса в контекстном меню"""
    print("\n🔄 Запуск test_copy_reference_button_in_context_menu")
    note_page = NotePage(page)
    note_page.open()

    # Создаем тестовую заметку
    note_title = "Context Menu Copy Reference Test"
    note_content = "This note will be used for testing the copy reference button."
    note_page.add_note(note_title, note_content)

    # Проверяем, что заметка появилась
    notes_list = note_page.get_notes()
    assert any(note_title in note for note in notes_list), "❌ Заметка не была создана!"

    # Нажимаем кнопку копирования референса в контекстном меню
    assert note_page.click_copy_reference_context_menu_button(note_title), "❌ Не удалось скопировать референс через контекстное меню!"
