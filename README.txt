Analiza Rynku Najmu Mieszkań w Łodzi (OLX)

## Cel projektu
Celem projektu było zbadanie korelacji między promowaniem ogłoszeń na portalu OLX a ceną najmu mieszkań. Projekt obejmuje pełną ścieżkę analityczną: od pozyskania danych, przez ich czyszczenie i analizę SQL, aż po wizualizację biznesową.

## Stos technologiczny
* **Python**: BeautifulSoup (Web Scraping), Pandas (ETL & Data Cleaning)
* **SQL (SQLite)**: Agregacja danych i weryfikacja hipotez
* **Power BI**: Budowa interaktywnego dashboardu i analiza outlierów

## Etapy prac
1.  **Pozyskanie danych**: Skrypt Python pobierający dane z ponad 500 ogłoszeń (Tytuł, Cena, Link).
2.  **Czyszczenie**: Usunięcie znaków specjalnych, konwersja typów danych, obsługa brakujących wartości (NaN).
3.  **Analiza SQL**: Przeniesienie danych do bazy SQLite i wykonanie zapytań sprawdzających średnie ceny w grupach (Kawalerki vs Pozostałe).
4.  **Wizualizacja**: Stworzenie raportu w Power BI z dynamicznymi filtrami.

## Kluczowe wnioski (Data Insights)
* **Obalenie hipotezy**: Wbrew początkowym założeniom, oferty promowane są średnio o X PLN tańsze od ofert zwykłych.
* **Segmentacja**: Najczęściej promowane są mieszkania z niższego segmentu cenowego (wysoka konkurencja rynkowa).
* **Wykrycie anomalii**: Zidentyfikowano oferty o nierealnych cenach (powyżej 20 tys. PLN), które bez odpowiedniej filtracji zniekształcały obraz rynku o 15%.