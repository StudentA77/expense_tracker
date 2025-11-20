
# Expense Tracker

Dit is een command line applicatie die een kleine SQLite database gebruikt.
Je kan categorieën toevoegen, uitgaven toevoegen en een rapport exporteren in CSV of Excel.

## Hoe gebruiken?

1. Maak een virtual environment:
   venv\Scripts\activate

2. Installeer de benodigde packages:
   pip install -r requirements.txt

3. Maak een bestand "settings.json" (niet in Git) met:
   {
       "database_path": "database/expenses.db"
   }

4. Initialiseer de database:
   python app.py init-db

5. Voeg een categorie toe:
   python app.py add-category --name "School"

6. Voeg een uitgave toe:
   python app.py add-expense --category_id 1 --amount 12.5 --description "Pen gekocht"

7. Exporteer CSV:
   python app.py export-csv

8. Exporteer Excel:
   python app.py export-excel

## Structuur van het project

database/
models/
utils/
exports/
app.py
settings_example.json
requirements.txt
.gitignore

## Klassen

Category  
Expense
