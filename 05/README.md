> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e03-django-rest-api` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` Django: Rest API


Twoim zadaniem jest stworzenie API zarządzającego wydarzeniami, z pełną obsługą operacji CRUD oraz dodatkowym filtrowaniem wydarzeń na podstawie daty.

---

## Zakres zadania

1. Zdefiniuj model `Event` z polami:
   - `name` – nazwa wydarzenia (tekst),
   - `date` – data wydarzenia (DateField),
   - `location` – miejsce wydarzenia (tekst).

2. Utwórz serializer `EventSerializer` (`ModelSerializer`).

3. Zaimplementuj widok `EventViewSet` dziedziczący po `ModelViewSet`.

4. Skonfiguruj `DefaultRouter` tak, aby domyślne endpointy były dostępne pod adresem:
   - **`/api/events/`**
   - **`/api/events/<id>/`**

5. Dodaj własny endpoint `recent`, który:
   - będzie dostępny pod adresem **`/api/events/recent/`**,
   - zwraca tylko wydarzenia, które odbędą się **w ciągu najbliższych 7 dni**.

---

## Wymagania funkcjonalne

- Endpointy wygenerowane automatycznie przez router powinny obsługiwać:
  - `GET`, `POST`, `PUT`, `DELETE` dla `/api/events/` i `/api/events/<id>/`

- Endpoint `/api/events/recent/` powinien zwracać wydarzenia:
  - których `date` mieści się w przedziale od **dzisiaj** do **dzisiaj + 7 dni**

### Przykład odpowiedzi `/api/events/recent/`

```json
[
  {
    "id": 1,
    "name": "Hackathon",
    "date": "2025-01-01",
    "location": "Warszawa"
  },
  {
    "id": 2,
    "name": "Targi pracy IT",
    "date": "2025-01-02",
    "location": "Gdańsk"
  }
]
```

---

## Wskazówki

* Do filtrowania po dacie użyj `datetime.date.today()` i operatora `lte`/`gte` w queryset.
* Upewnij się, że filtr działa niezależnie od danych testowych – możesz dodać wydarzenia z przyszłą i przeszłą datą.

---

## Twoje rozwiązanie powinno zawierać

* Model `Event` z odpowiednimi polami,
* Serializer `EventSerializer`,
* Widok `EventViewSet` z pełnym CRUD i akcją `recent`,
* Rejestrację widoku przez `DefaultRouter`,
* Dostęp do endpointów: `/api/events/` i `/api/events/recent/`.


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-rest-api)*

> :arrow_left: [*poprzednie zadanie*](./../04) | ~~*następne zadanie*~~ :arrow_right:
