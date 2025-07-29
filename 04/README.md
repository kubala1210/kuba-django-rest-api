> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e03-django-rest-api` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#04` Django: Rest API

Twoim zadaniem jest stworzenie API pozwalającego na dodawanie przepisów kulinarnych wraz z listą składników. Każdy przepis może zawierać wiele składników – ćwiczenie wykorzystuje relację jeden-do-wielu.

## Zakres zadania

1. Zdefiniuj dwa modele Django:
   - `Recipe` – reprezentuje przepis (pole `title`),
   - `Ingredient` – reprezentuje składnik (pole `name`, powiązanie z `Recipe` przez `ForeignKey`).

2. Utwórz serializer `RecipeSerializer`, który:
   - zwraca przepis wraz z jego składnikami,
   - umożliwia dodanie nowego przepisu z listą składników przesłanych jako lista nazw.

3. Utwórz klasowy widok `RecipeAPIView` dostępny pod adresem **`/api/recipes/`**, który:
   - obsługuje metodę **GET** – zwraca wszystkie przepisy z ich składnikami,
   - obsługuje metodę **POST** – umożliwia dodanie nowego przepisu oraz składników w jednym żądaniu.

---

## Wymagania funkcjonalne

- Dla `POST` dane wejściowe powinny zawierać:
  - `title`: nazwa przepisu,
  - `ingredients`: lista nazw składników.

### Przykład danych wejściowych (POST)

```json
{
  "title": "Kanapka",
  "ingredients": ["Chleb", "Masło", "Ser"]
}
```

### Przykład odpowiedzi (GET)

```json
[
  {
    "id": 1,
    "title": "Kanapka",
    "ingredients": [
      {"id": 1, "name": "Chleb"},
      {"id": 2, "name": "Masło"},
      {"id": 3, "name": "Ser"}
    ]
  }
]
```

---

## Wskazówki

* W modelu `Ingredient` użyj `ForeignKey` do `Recipe` z `on_delete=models.CASCADE`.
* W serializerze `RecipeSerializer` możesz dodać pole `ingredients` jako zagnieżdżony serializer lub utworzyć składniki ręcznie w `create()`.
* Widok powinien korzystać z `APIView` i obsługiwać metody `get()` oraz `post()`.

---

## Twoje rozwiązanie powinno zawierać

* Modele `Recipe` i `Ingredient`,
* Serializery do obu modeli (`ModelSerializer`),
* Widok `RecipeAPIView` z obsługą `GET` i `POST`,
* Routing pod adresem `/api/recipes/`,
* Możliwość dodania przepisu wraz z listą składników w jednym zapytaniu.


&nbsp;

> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-rest-api)*

> :arrow_left: [*poprzednie zadanie*](./../03) | [*następne zadanie*](./../05) :arrow_right:
