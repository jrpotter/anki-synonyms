from dataclasses import dataclass
from typing import Optional, Union

import copy
import enum
import random


START_TAG = "'("
END_TAG = ")"
CHOICE_TAG = "|"


class Tag(enum.Enum):
    START = 0
    END = 1
    CHOICE = 2


Token = Union[Tag, str]


@dataclass
class ParserState:
    """Convenience class used when traversing our tokenized stream."""

    starts: int
    pos: int
    tokens: list[Token]


def _matches_at(arg: str, target: str, pos: int = 0) -> bool:
    """Check a substring matches the @target parameter."""
    return arg[pos : pos + len(target)] == target


def _label_tokens(arg: str) -> ParserState:
    """Primary lexing function which traverses our stream and assigns initial
    token labels.

    Note this is a greedy algorithm so it is possible we incorrectly label
    tokens as 'START'. For instance, consider a start tag of "'(". Then running

    >>> _label_tokens(arg="hello'(")

    will yield a token stream like ["hello", START] when we should have just a
    single entry "hello'(". This gets corrected in `_relabel_starts`.
    """
    state = ParserState(starts=0, pos=0, tokens=[])
    while state.pos < len(arg):
        if _matches_at(arg, target=START_TAG, pos=state.pos):
            state.tokens.append(Tag.START)
            state.starts += 1
            state.pos += len(START_TAG)
        elif state.starts and _matches_at(arg, target=END_TAG, pos=state.pos):
            state.tokens.append(Tag.END)
            state.starts -= 1
            state.pos += len(END_TAG)
        elif state.starts and _matches_at(arg, target=CHOICE_TAG, pos=state.pos):
            state.tokens.append(Tag.CHOICE)
            state.pos += 1
        else:
            state.tokens.append(arg[state.pos])
            state.pos += 1
    return state


def _relabel_starts(arg: str, state: ParserState) -> ParserState:
    """Relabels 'START' tags that may have been labeled incorrectly."""
    new_state = copy.copy(state)
    if not new_state.starts:
        return new_state
    for i, token in enumerate(reversed(new_state.tokens)):
        if token != Tag.START:
            continue
        index = len(new_state.tokens) - i - 1
        new_state.tokens[index] = START_TAG
        new_state.starts -= 1
        if not new_state.starts:
            break
    return new_state


def _group_tokens(state: ParserState) -> list[Token]:
    """Aggregate adjacent strings together into a single token."""
    new_tokens: list[Token] = []
    for token in state.tokens:
        if new_tokens and isinstance(token, str) and isinstance(new_tokens[-1], str):
            new_tokens[-1] += token
        else:
            new_tokens.append(token)
    return new_tokens


def _tokenize(arg: str) -> list[Token]:
    """Break string into token stream for easier handling."""
    state = _label_tokens(arg)
    state = _relabel_starts(arg, state)
    return _group_tokens(state)


def run_parser(arg: str) -> str:
    """Find all "choice" selections within the given @arg.

    For instance, assuming a START, END, and CHOICE of "'(", ")", and "|"
    respectively, parsing "'(hello|world)" yields either "hello" or "world".
    """
    tokens = _tokenize(arg)
    stack: list[list[str]] = [[]]
    for token in tokens:
        if token is Tag.START:
            stack.append([])
        elif token is Tag.END:
            ts = stack.pop()
            stack[-1].append(random.choice(ts))
        elif token is Tag.CHOICE:
            pass
        else:
            stack[-1].append(token)
    assert len(stack) == 1, "Stack is larger than a single element"
    return "".join(stack[0])
