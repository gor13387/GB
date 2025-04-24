import os

# Функция для отображения меню
def display_menu():
    print("\nМеню:")
    print("1. Создать заметку")
    print("2. Просмотреть заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выход")

# Функция для создания заметки
def create_note():
    note = input("Введите текст заметки: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Заметка сохранена.")

# Функция для просмотра заметок
def view_notes():
    if not os.path.exists("notes.txt"):
        print("Нет сохраненных заметок.")
        return
    with open("notes.txt", "r") as file:
        notes = file.readlines()
        if not notes:
            print("Нет сохраненных заметок.")
        else:
            print("\nСписок заметок:")
            for index, note in enumerate(notes):
                print(f"{index + 1}. {note.strip()}")

# Функция для редактирования заметки
def edit_note():
    view_notes()
    note_number = int(input("Введите номер заметки для редактирования: ")) - 1
    with open("notes.txt", "r") as file:
        notes = file.readlines()
    if 0 <= note_number < len(notes):
        new_note = input("Введите новый текст заметки: ")
        notes[note_number] = new_note + "\n"
        with open("notes.txt", "w") as file:
            file.writelines(notes)
        print("Заметка обновлена.")
    else:
        print("Неверный номер заметки.")

# Функция для удаления заметки
def delete_note():
    view_notes()
    note_number = int(input("Введите номер заметки для удаления: ")) - 1
    with open("notes.txt", "r") as file:
        notes = file.readlines()
    if 0 <= note_number < len(notes):
        del notes[note_number]
        with open("notes.txt", "w") as file:
            file.writelines(notes)
        print("Заметка удалена.")
    else:
        print("Неверный номер заметки.")

# Основная функция программы
def main():
    while True:
        display_menu()
        choice = input("Выберите действие (1-5): ")
        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
