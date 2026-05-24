import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9"
}

LICZBA_STRON_DO_POBRANIA = 10
zebrane_oferty = []

print("Rozpoczynam pobieranie danych...")

for strona in range(1, LICZBA_STRON_DO_POBRANIA + 1):
    print(f"Pobieram stronę {strona}...")
    
    url = f"https://www.olx.pl/nieruchomosci/mieszkania/wynajem/lodz/?page={strona}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Błąd! Serwer zwrócił kod: {response.status_code}.")
        break
        
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # KROK 1: Znajdujemy wszystkie kafelki na danej stronie
    karty_ogloszen = soup.find_all('div', {'data-cy': 'l-card'})
    
    # KROK 2: Analizujemy KAŻDY kafelek z osobna
    for karta in karty_ogloszen:
        try:
            tytul_div = karta.find('div', {'data-cy': 'ad-card-title'})
            if tytul_div:
                tytul = tytul_div.text.strip()
            else:
                tytul = "Brak tytułu"
            
            # Szukamy ceny
            cena_element = karta.find('p', {'data-testid': 'ad-price'})
            cena = cena_element.text.strip() if cena_element else "Brak ceny"
            
            # Szukamy linku
            link_element = karta.find('a')
            if link_element and 'href' in link_element.attrs:
                link = link_element['href']
                # OLX czasem daje linki względne, czasem bezwzględne
                if not link.startswith('http'):
                    link = "https://www.olx.pl" + link
            else:
                link = "Brak linku"
            
            # Dodajemy tylko te ogłoszenia, które mają chociaż cenę i tytuł
            if tytul != "Brak tytułu" and cena != "Brak ceny":
                zebrane_oferty.append({
                    'Tytul': tytul,
                    'Cena_Surowa': cena,
                    'Link': link
                })
            
        except Exception as e:
            continue
            
    # Czekamy chwilę, żeby nie dostać bana
    time.sleep(random.uniform(2.0, 4.0))

# Zapisujemy do pliku z odpowiednim kodowaniem, żeby Excel to dobrze przeczytał
if zebrane_oferty:
    df = pd.DataFrame(zebrane_oferty)
    df.to_csv('olx_surowe_dane.csv', index=False, encoding='utf-8-sig')
    print(f"\nSukces! Zapisano {len(zebrane_oferty)} ofert do pliku 'olx_surowe_dane.csv'.")
else:
    print("\nNie udało się pobrać żadnych ofert.")