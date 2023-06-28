import json
import os
from datetime import datetime

class Note:
    def __init__(self, id, title, body, created_at):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at

    def __repr__(self):
        return f"Note(id={self.id}, title='{self.title}', body='{self.body}', created_at='{self.created_at}')"

class NoteList:
    def __init__(self):
        self.notes = []

    def add(self, note):
        self.notes.append(note)

    def edit(self, id, title, body):
        note = self.get(id)
        if note:
            note.title = title
            note.body = body
            note.updated_at = datetime.now()

    def delete(self, id):
        note = self.get(id)
        if note:
            self.notes.remove(note)

    def get(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None
    
    def print_by_date(self, date):
        for note in self.notes:
            if note.created_at == date:
                print(note)
        

    def get_all(self):
        return self.notes

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump([vars(note) for note in self.notes], f, indent=4)

    def load(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                self.notes = [Note(**note_data) for note_data in data]

    def print_all(self):
        for note in self.notes:
            print(note)

    def print_by_id(self, id):
        note = self.get(id)
        if note:
            print(note)

if __name__ == '__main__':
    notes = NoteList()
    notes.load('notes.json')

    while True:
        print('Введите команды (add, edit, delete, list, list_by_date, get, exit):')
        command = input()

        if command == 'add':
            id = len(notes.get_all()) + 1
            title = input('Введите заголовок: ')
            body = input('Введите тело заметки: ')
            created_at = datetime.now().strftime("%d-%m-%Y")
            note = Note(id, title, body, created_at)
            notes.add(note)
            notes.save('notes.json')
            print('Заметка сохранена')

        elif command == 'edit':
            id = int(input('Выберете id заметки для редактирования: '))
            title = input('Измените заголовок: ')
            body = input('Измените тело заметки: ')
            notes.edit(id, title, body)
            notes.save('notes.json')
            print('Заметка сохранена')

        elif command == 'delete':
            id = int(input('Выберете id заметки для удаления: '))
            notes.delete(id)

        elif command == 'list':
            notes.print_all()
            
        elif command == 'list_by_date':
            date_notes = input('Введите даты в формате: dd-mm-yyyy, например: 23-07-2022: ')
            notes.print_by_date(date_notes)

        elif command == 'get':
            id = int(input('Введите id заметки: '))
            notes.print_by_id(id)

        elif command == 'exit':
            break

        else:
            print('Команда не распознана')