import pandas as pd
import numpy as np
import sqlite3


df = pd.read_csv('olx_surowe_dane.csv', encoding='utf-8-sig')

#Price
df['Cena'] = df['Cena_Surowa'].astype(str).str.replace(' zł', '', regex=False).str.replace(' ', '', regex=False)
df['Cena'] = pd.to_numeric(df['Cena'], errors='coerce')

#flat type
warunek = df['Tytul'].str.lower().str.contains('kawalerka|studio', na=False)
df['Liczba_pokoi'] = np.where(warunek, 'Kawalerka', 'Więcej pokoi')

#Promoted?
df['Promowanie'] = df['Link'].astype(str).str.contains('promoted', na=False)

#dataframe
tabela_koncowa = df[['Cena', 'Liczba_pokoi', 'Promowanie']]

print(tabela_koncowa.to_string())

tabela_koncowa.to_csv('olx_gotowe_do_powerbi.csv', index=False, encoding='utf-8-sig')

#SQL

conn = sqlite3.connect('baza_olx.db')

tabela_koncowa.to_sql('mieszkania', conn, if_exists='replace', index=False)
print("Dane zrzucone do bazy danych SQL!")

zapytanie_sql = """
SELECT 
    Liczba_pokoi, 
    ROUND(AVG(Cena), 0) AS Srednia_Cena,
    COUNT(*) AS Liczba_Ofert
FROM mieszkania
GROUP BY Liczba_pokoi;
"""

wynik_sql = pd.read_sql_query(zapytanie_sql, conn)

print("\nWynik zapytania SQL:")
print(wynik_sql.to_string())

conn.close()

print("\nDane zostały wyczyszczone i zapisane!")