Feature: Simple Intersection Number

Scenario Outline: Intersection Number
    Given   This Number for <input> to Intersection Function
    When    Asked to Find the Intersection for <number>
    Then    The Intersections Are <output>
    Examples: Intersection Number Sample
        | input          | number          | output   |
        | 1, 3, 2, 4, 5  | 1, 3, 5, 7, 9   | 1, 3  |
        | 1, 3, 5, 7, 9  | 1, 3, 5, 7, 9   | 1, 3, 5, 7  |
        | 1, 3, 3, 3, 3  | 1, 3, 5, 7, 9   | 1, 3  |
