# Valid Parentheses

## Problem

Given a string `s` that contains only the characters `(`, `)`, `[`, `]`, `{`
and `}`, decide whether the brackets are balanced.

A string is valid when:

- every opening bracket is closed by the same type of bracket,
- brackets close in the correct order,
- every closing bracket has a matching opening bracket.

Return `true` if the string is valid, otherwise return `false`.

## Examples

Input:  `""`
Output: `true`

Input:  `"()[]{}"`
Output: `true`

Input:  `"(]"` 
Output: `false`

Input:  `"([)]"`
Output: `false`

Input:  `"{[]}"`
Output: `true`

## Constraints

- `0 <= s.length <= 10**4`
- `s` only contains the six bracket characters.
