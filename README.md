# Lab: Web Scraping

## Feature Tasks and Requirements

- Scrape a Wikipedia page and record which passages need citations.
    - E.g. History of Mexico has a few “citations needed”.
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant    passage.
    - E.g. Citation needed for “lorem spam and impsum eggs”
    - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

## Implementation
- create function called get_citations_needed_count that accept url and returns an integer
- create function called get_citations_needed_report that accept url and returns a string, the string should be formatted with each citation needed on own line, in order found.
