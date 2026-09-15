#Separation of concerns
class JournalV:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
            del self.entries[pos]

    def __str__(self):
         return "\n".join(self.entries)

    def save(self, filename):
         file = open(filename, 'w')
         file.write(str(self))
         file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
            pass

why=""""This code violates the SRP (Single Responsibility Principle)—the "S" in SOLID design principles—because the Journal class has two distinct reasons to change:

Domain Logic: Managing journal entries (add_entry, remove_entry).

Persistence Logic: Saving the journal to disk (save)."""

j = JournalV()
j.add_entry("I cried today")
j.add_entry("I ate a bug")
print(f"Journal entries: \n{j}")

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
            del self.entries[pos]

    def __str__(self):
         return "\n".join(self.entries)


class PersistenceManager:
     @staticmethod
     def save_to_file(journal, filename):
          with open(filename, "w") as file:
               file.write(str(journal))

j = Journal()
j.add_entry("I cried today")
j.add_entry("I ate a bug")
print(f"Journal entries: \n{j}")
PersistenceManager.save_to_file(j, "journal.txt")