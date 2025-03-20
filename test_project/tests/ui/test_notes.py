import pytest
from pages.note_page import NotePage

@pytest.mark.ui
def test_add_note(page):
    """Тест на создание новой заметки"""
    print("\n🔄 Запуск test_add_note")
    note_page = NotePage(page)
    note_page.open()
    note_page.add_note("Test note", "This is a test note.")

    # Проверяем, появилась ли заметка
    notes_list = note_page.get_notes()
    assert any("Test note" in note for note in notes_list), "❌ Заметка не была создана!"

@pytest.mark.ui
def test_delete_note(page):
    """Тест на удаление заметки"""
    print("\n🔄 Запуск test_delete_note")
    note_page = NotePage(page)
    note_page.open()

    # Проверяем, что заметка еще не существует, чтобы не дублировать её
    notes_list = note_page.get_notes()
    if "Note to delete" in notes_list:
        print("⚠️ Заметка 'Note to delete' уже есть, пропускаем создание.")
    else:
        note_page.add_note("Note to delete", "This note will be deleted.")

    # Проверяем, что заметка появилась
    notes_list = note_page.get_notes()
    assert any("Note to delete" in note for note in notes_list), "❌ Заметка не была создана перед удалением!"

    # Удаляем заметку
    assert note_page.delete_note("Note to delete"), "❌ Не удалось удалить заметку!"

    # Проверяем, что заметка исчезла
    notes_list_after = note_page.get_notes()
    assert not any("Note to delete" in note for note in notes_list_after), "❌ Заметка осталась после удаления!"


@pytest.mark.ui
def test_download_note(page):
    """Тест на проверку работы кнопки загрузки заметки"""
    print("\n🔄 Запуск test_download_note")
    note_page = NotePage(page)
    note_page.open()

    # Убедимся, что есть хотя бы одна заметка, чтобы было что загружать
    notes_list = note_page.get_notes()
    assert notes_list, "❌ Нет заметок для загрузки!"

    # Выбираем первую заметку
    first_note_title = notes_list[0]

    # Нажимаем кнопку загрузки
    download_button = page.locator("#root > div > div > div.Pane.vertical.Pane2 > div > div.Pane.vertical.Pane2 > main > section > nav:nth-child(1) > button:nth-child(4) > span")
    assert download_button.is_visible(), "❌ Кнопка загрузки не найдена!"
    download_button.click()

    # Проверяем, что загрузка произошла (например, появление файла или изменение интерфейса)
    # Если приложение дает какой-то индикатор загрузки, сюда можно добавить проверку
    print(f"✅ Успешно нажата кнопка загрузки для заметки: {first_note_title}")



@pytest.mark.ui
def test_add_note_to_favorites(page):
    """Тест на добавление заметки в избранное (нижняя панель)"""
    print("\n🔄 Запуск test_add_note_to_favorites")
    note_page = NotePage(page)
    note_page.open()

    # Создаем тестовую заметку
    note_title = "Favorite Note"
    note_content = "This note should be favorited."
    note_page.add_note(note_title, note_content)

    # Проверяем, что заметка появилась
    notes_list = note_page.get_notes()
    assert any(note_title in note for note in notes_list), "❌ Заметка не была создана!"

    # Открываем заметку
    assert note_page.open_note(note_title), "❌ Не удалось открыть заметку!"

    # Добавляем в избранное
    assert note_page.add_to_favorites(), "❌ Не удалось добавить заметку в избранное!"

@pytest.mark.ui
def test_edit_note(page):
    """Тест на проверку работы кнопки редактирования заметки (нижняя панель)"""
    print("\n🔄 Запуск test_edit_note")
    note_page = NotePage(page)
    note_page.open()

    # Создаем тестовую заметку
    note_title = "Editable Note"
    note_content = "This is a test note for editing."
    note_page.add_note(note_title, note_content)

    # Проверяем, что заметка появилась
    notes_list = note_page.get_notes()
    assert any(note_title in note for note in notes_list), "❌ Заметка не была создана!"

    # Открываем заметку
    assert note_page.open_note(note_title), "❌ Не удалось открыть заметку!"

    # Нажимаем кнопку редактирования
    edit_button_selector = "#root > div > div > div.Pane.vertical.Pane2 > div > div.Pane.vertical.Pane2 > main > section > nav:nth-child(1) > button:nth-child(1)"
    edit_button = page.locator(edit_button_selector)
    assert edit_button.is_visible(), "❌ Кнопка редактирования не найдена!"
    edit_button.click()

    # Вносим изменения в заметку
    updated_content = "This note has been edited successfully!"
    note_page.page.keyboard.insert_text(updated_content)
    note_page.page.wait_for_timeout(1000)

    # Проверяем, что изменения сохранены
    note_page.page.click("text=Notes")  # Переключаемся на список заметок
    note_page.page.wait_for_timeout(2000)

    opened_note = note_page.open_note(note_title)
    assert opened_note, "❌ Не удалось открыть отредактированную заметку!"

import pytest
from pages.note_page import NotePage

@pytest.mark.ui
def test_copy_note_button(page):
    """Тест на проверку работы кнопки 'Copy Note'"""
    print("\n🔄 Запуск test_copy_note_button")
    note_page = NotePage(page)
    note_page.open()

    # Создаем тестовую заметку
    note_title = "Copy Note Test"
    note_content = "This note will be copied."
    note_page.add_note(note_title, note_content)

    # Проверяем, что заметка появилась
    notes_list = note_page.get_notes()
    assert any(note_title in note for note in notes_list), "❌ Заметка не была создана!"

    # Нажимаем кнопку 'Copy Note'
    assert note_page.click_copy_note_button(), "❌ Не удалось нажать кнопку 'Copy Note'!"
