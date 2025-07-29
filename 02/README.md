> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e03-django-rest-api` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#02` Django: Rest API

Twoim zadaniem jest stworzenie widoku API, który umożliwia użytkownikowi ocenę filmu. Widok powinien przyjmować dane metodą POST, wykonać prostą walidację i zwrócić odpowiednią odpowiedź JSON.

---

## Zakres zadania

1. Stwórz widok `rate_movie_view`, który:
   - obsługuje tylko zapytania typu **POST**,
   - przyjmuje dane w formacie JSON z polami `movie` i `rating`,
   - sprawdza, czy ocena (`rating`) to liczba całkowita z zakresu od 1 do 10,
   - zwraca odpowiedni komunikat lub błąd.

2. Skonfiguruj URL `/api/rate/`.

---

## Wymagania funkcjonalne

### Przykładowe dane wejściowe:

```json
{
  "movie": "Incepcja",
  "rating": 9
}
```

### Przykładowe odpowiedzi:

* Poprawne dane (Kod HTTP: `201 Created`):

  ```json
  {
    "message": "Oceniono film 'Incepcja' na 9/10"
  }

  ```  

* Niepoprawna ocena (np. 15 lub brak oceny, Kod HTTP: `400 Bad Request`):

  ```json
  {
    "error": "Ocena musi być liczbą od 1 do 10"
  }

  ```


## Wskazówki

* Skorzystaj z `@api_view(['POST'])`.
* Dane z żądania pobieraj przez `request.data`.
* Użyj klasy `Response` oraz odpowiednich kodów statusu (`status=201`, `status=400`).
* Nie twórz modelu ani bazy danych — dane są tymczasowe.

---

## Testowanie

Użyj Postmana lub polecenia `curl`:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"movie": "Incepcja", "rating": 9}' \
  http://localhost:8000/api/rate/

```


## Twoje rozwiązanie powinno zawierać

* Widok `rate_movie_view` w `views.py`,
* wpis w `urls.py`,
* obsługę błędów i walidację danych wejściowych,
* odpowiednie kody statusu HTTP.


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-rest-api)*

> :arrow_left: [*poprzednie zadanie*](./../01) | [*następne zadanie*](./../03) :arrow_right:
