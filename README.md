

\# Expense Tracker



Dit is een command line applicatie die een kleine SQLite database gebruikt.

Je kan categorieën toevoegen, uitgaven toevoegen en een rapport exporteren in CSV of Excel.



\## Hoe gebruiken?



1\. Maak een virtual environment:

&nbsp;  venv\\Scripts\\activate



2\. Installeer de benodigde packages:

&nbsp;  pip install -r requirements.txt



3\. Maak een bestand "settings.json" (niet in Git) met:

&nbsp;  {

&nbsp;      "database\_path": "database/expenses.db"

&nbsp;  }



4\. Initialiseer de database:

&nbsp;  python app.py init-db



5\. Voeg een categorie toe:

&nbsp;  python app.py add-category --name "School"



6\. Voeg een uitgave toe:

&nbsp;  python app.py add-expense --category\_id 1 --amount 12.5 --description "Pen gekocht"



7\. Exporteer CSV:

&nbsp;  python app.py export-csv



8\. Exporteer Excel:

&nbsp;  python app.py export-excel



\## Structuur van het project



database/

models/

utils/

exports/

app.py

settings\_example.json

requirements.txt

.gitignore



\## Klassen



Category  

Expense  



\## Rapporten



CSV en Excel worden opgeslagen in de map "exports".





