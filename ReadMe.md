# Wordle Scoring Algorithm

This algorithm uses a two pass solution to complete the
scoring.

## The Basic Algorithm

The basic process used to score is:

- do words differ in length? yes - raise an exception
- are words the same? yes - return [2,2,2,2,2]
- presume all letters are wrong, score 0 for each letter
- locate letters in correct place and score 2 for each correct letter
- locate letters in incorrect place and score 1 for each letter
- return the score

# The Algorithm (Pseudocode)

- get the length of the word
- get the length of the guess
- check if the word and guess are the same length
- if they are not, raise a ValueError
    - if the word and guess are the same,
    - return a list of 2s
- initialise the result list to scores of 0
- convert the word and guess to lists
- check for exact matches
- for each letter in the word
    - check if the letter in the word is the same as the letter in the guess and if it is, set
      the result to 2
    - and remove the letter from the word and guess
- check for partial matches
    - check if the letter in the word is in the guess
        - if it is, check if it is in the guess
            - if it is, set the result to 1
            - and remove the letter from the word and guess
            - end the for loop early
- return the resulting list of scores

## The Algorithm (Flowchart)

```mermaid

flowchart TD
    subgraph Main Code
        A0((start)) --> A
        A([calculate length of word]) --> B
        B([calculate length of guess]) --> C
        C{are word and guess are the same length?}
        C -- NO --> D
        D([raise a ValueError]) --> Z
        C -- YES --> E
        E{are word and guess are the same?}
        E -- YES --> F
        F([return a list of 2s]) --> Z
        E -- NO --> G
        G([create result list of 0 score]) --> H
        H([convert the word to list]) --> I
        I([convert the guess to list]) --> J
        J[[Score Matched Letters]]
        J --> N
        N[[Score Mismatched Words]]

        N --> S
        S([return the resulting list of scores]) --> Z
        Z((end))
    end
```

```mermaid
flowchart TD

    subgraph Score Matched Letters
        J0((start)) --> J1
        J1([for each letter in the word]) --> K1
        K1{is letter in word same as letter in guess?} -- YES --> L1
        K1 -- NO --> J1
        L1([set the result to 2]) --> M1
        M1([remove letter from the word and guess]) --> J1
        J2((end))
    end
```

```mermaid
flowchart TD

    subgraph Score Mismatched Words
        N0(("start")) --> N1
        N1([for each letter in the word]) --> O1
        O1{letter in the word is in the guess?} -- YES --> Q1
        Q1([result is 1]) --> R1
        R1([remove the letter from the word and guess]) --> N1
        O1 -- NO --> N1
    end
```
