# anki-synonyms

A simple [Anki plugin](https://ankiweb.net/shared/info/492653825) that allows
randomly choosing different options for parts of prompts. This was designed to
handle synonyms in a clean way.

## Motivation

Consider a [total order](https://en.wikipedia.org/wiki/Total_order). What this
is does not matter; other names it may have does. What some people call a
"total order", others call a "linear order". Though this example is simple, it
highlights an important issue - remembering the various synonyms used to
describe a concept is necessary for fluency.

As of now, to handle this situation, it is probably suggested to use two
flashcards, one with prompt "Total Order" and another with prompt "Linear Order".
In some cases though, it'd be nice if the flashcard could *choose* which term it
shows when it shows it. That is, it'd be nice to have a single card and allow
Anki to randomly choose to show "Total Order" *or* "Linear Order".

To do so, we can install this plugin and write the following:

```
'(Total|Linear) Order
```

Here, `'(` is used to indicate the start of a set of choices Anki can display,
`|` is used to separate the different options, and `)` is used to indicate the
end of the set. The result is either "Total Order" or "Linear Order" at time
of prompting.

You can also nest choices if need be:

```
'('(Logical|Valid) Consequence|Entailment)
```

will yield either "Logical Consequence", "Valid Consequence", or "Entailment".

## Configuration

From "Tools > Add-ons", select the `anki-synonyms` entry and select "Config"
to reveal a dialog with contents:

```json
{
    "CHOICE_TAG": "|",
    "END_TAG": ")",
    "START_TAG": "'("
}
```

Update these accordingly if the default `'(|)` set of operators do not mesh with
the text in your questions and answers.
