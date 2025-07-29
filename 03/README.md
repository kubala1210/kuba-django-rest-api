> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e03-django-rest-api` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#03` Django: Rest API


Twoim zadaniem jest stworzenie klasowego widoku API, który pozwoli użytkownikowi zapisywać i odczytywać pomysły. Dane mają być przechowywane tymczasowo w pamięci – nie tworzysz modelu ani bazy danych.


## Zakres zadania

1. Utwórz klasę `IdeaAPIView`, która dziedziczy po `APIView`.
2. Widok powinien być dostępny pod adresem **`/api/ideas/`**.
3. Widok powinien:
   - obsługiwać metodę **GET** – zwraca wszystkie zapisane pomysły w formacie JSON,
   - obsługiwać metodę **POST** – przyjmuje jeden klucz `description`, dodaje nowy pomysł do listy i zwraca go z unikalnym `id`.

---

## Wymagania funkcjonalne

- Dane mają być przechowywane w liście `ideas` w pliku `views.py`.
- Każdy pomysł powinien mieć automatycznie nadane pole `id` (np. rosnące liczby).
- Widok powinien zwracać odpowiedni kod statusu:
  - `201 Created` po dodaniu nowego pomysłu,
  - `400 Bad Request` jeśli brakuje pola `description`.

### Przykład danych wejściowych (POST)

```json
{
  "description": "Zbudować aplikację do zarządzania budżetem"
}
```

### Przykład odpowiedzi (GET)

```json
[
  {"id": 1, "description": "Zbudować aplikację do zarządzania budżetem"},
  {"id": 2, "description": "Stworzyć kurs Django po polsku"}
]
```

---

## Wskazówki

* W pliku `views.py` utwórz globalne zmienne `ideas = []` i `next_id = 1`.
* Użyj `request.data.get('description')`, aby pobrać dane z żądania POST.
* W metodzie `get()` po prostu zwróć całą listę `ideas`.
* W metodzie `post()` dodaj nowy słownik z kluczami `id` i `description`, a następnie zwiększ `next_id`.

---

## Twoje rozwiązanie powinno zawierać

* Klasę `IdeaAPIView` z metodami `get()` i `post()`,
* Rejestrację widoku w pliku `urls.py` pod ścieżką `/api/ideas/`,
* Poprawną logikę przypisywania `id` oraz przechowywania danych w liście `ideas`,
* Obsługę kodów HTTP: `201`, `400`.


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-rest-api)*

> :arrow_left: [*poprzednie zadanie*](./../02) | [*następne zadanie*](./../04) :arrow_right:
