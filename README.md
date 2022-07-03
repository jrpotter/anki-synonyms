# anki-synonyms

A simple [Anki](https://apps.ankiweb.net/) plugin that allows randomly choosing
different options for parts of prompts. This was designed to handle synonyms in
a clean way.

Consider a [total order](https://en.wikipedia.org/wiki/Total_order). What this
is does not matter; what it could also be called does. What some people call a
"total order", others call a "linear order". Though this example is simple, it
does highlight an issue - remembering the various synonyms used to describe
a concept is important for fluency.

As of now, to handle this situation, it is probably best to use two flashcards,
one with prompt "Total Order" and another with prompt "Linear Order". In some
cases though, it'd be nice if the flashcard could *choose* which term it shows
when it shows it. That is, it'd be nice to have a single card and allow Anki to
randomly choose to show "Total Order" *or* "Linear Order".

To do so, we can install this plugin and write the following:

```
'(Total|Linear) Order
```

Here, `'(` is used to indicate the start of a set of choices Anki can display,
`|` is used to separate the different options, and `)` is used to indicate the
end of the set. The result is either "Total Order" or "Linear Order" at time
of prompting.

## Configuration

TODO

## Nesting

TODO
