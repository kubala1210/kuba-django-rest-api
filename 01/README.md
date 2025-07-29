> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e03-django-rest-api` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#01` Django: Rest API

Twoim zadaniem jest stworzenie prostego endpointu API, który przyjmuje parametr zapytania (`query param`) i na jego podstawie zwraca komunikat powitalny w odpowiednim języku.

To ćwiczenie pozwoli Ci przećwiczyć:
- pracę z widokiem funkcyjnym w Django REST Framework (`@api_view`),
- obsługę parametrów w adresie URL (`request.query_params`),
- przygotowanie odpowiedzi w formacie JSON (`Response`).

---

## Zakres zadania

1. Stwórz plik `views.py` (jeśli go jeszcze nie masz) w swojej aplikacji Django.
2. Zaimplementuj funkcję `hello_view`, która:
   - przyjmuje tylko zapytanie typu **GET**,
   - odczytuje parametr `lang` z adresu URL,
   - zwraca odpowiedni komunikat w formacie JSON.

3. Skonfiguruj routing:
   - dodaj wpis do pliku `urls.py`, tak aby widok był dostępny pod adresem:  
     **`/api/hello/`**

---

## Wymagania funkcjonalne

### Przykładowe wywołania:

| Zapytanie                            | Odpowiedź JSON                   |
|-------------------------------------|----------------------------------|
| `/api/hello/?lang=pl`              | `{"message": "Cześć!"}`         |
| `/api/hello/?lang=en`              | `{"message": "Hello!"}`         |
| `/api/hello/?lang=de`              | `{"message": "Hallo!"}`         |
| `/api/hello/` (brak parametru)     | `{"message": "Hej!"}`           |

Możesz obsłużyć inne języki lub ustawić domyślne `"Hej!"`.

---

## Wskazówki

- Skorzystaj z dekoratora `@api_view(['GET'])`.
- Parametry zapytania odczytujemy przez `request.query_params.get("lang")`.
- Użyj klasy `Response` z `rest_framework.response`.
- Przygotuj mapę język → komunikat w postaci słownika Pythonowego.

---

## Testowanie

Możesz przetestować ten endpoint w przeglądarce, Postmanie lub wpisując URL bezpośrednio:


http://localhost:8000/api/hello/?lang=en


## Twoje rozwiązanie powinno zawierać

* Widok `hello_view` w `views.py`,
* wpis w `urls.py`,
* poprawną obsługę parametrów query i odpowiedzi JSON.



&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-rest-api)*

> :arrow_left: ~~*poprzednie zadanie*~~ | [*następne zadanie*](./../02) :arrow_right:
