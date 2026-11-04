# Final task set — 17 items

> Answers are recomputed by code (`build_tasks.py`); no discrepancies.
> Machine-readable form: `tasks_final.json`.

## 1. Birds: altitude, linear chain

1. Falcon-14 flies 6 metres higher than crow-33.
2. Crow-33 flies 4 metres higher than jay-08.
3. Jay-08 flies 3 metres higher than heron-51.
4. Heron-51 is also called "super-flyer-1".

**Question:** by how many metres does falcon-14 fly higher than heron-51? Answer with a single integer.
**Answer:** `13`
**Check:** 6 + 4 + 3 = 13.

---

## 2. Ships: group rules by divisibility

1. The base cargo capacity of a ship is 40 tonnes.
2. Ships with numbers divisible by five have a capacity 6 tonnes above the base.
3. Ships with numbers divisible by seven have a capacity 4 tonnes below the base.
4. Ship-25 is also called "heavylift-2".
5. Ship-33 matches neither rule.
6. Ship-52 matches neither rule.

**Question:** by how many tonnes does "heavylift-2" carry more than ship-33? Answer with a single integer.
**Answer:** `6`
**Check:** 25 is divisible by 5 → 46 t; 33 has no rule → 40 t; 46 − 40 = 6.

---

## 3. Turbines: star, minimum and maximum

1. Turbine-70 produces 120 MW.
2. Turbine-71 produces 15 MW more than turbine-70.
3. Turbine-72 produces 25 MW less than turbine-70.
4. Turbine-73 produces 5 MW more than turbine-70.

**Question:** by how many megawatts is the maximum output among these four turbines greater than the minimum? Answer with a single integer.
**Answer:** `40`
**Check:** max 135 (71), min 95 (72); 135 − 95 = 40.

---

## 4. Cities: branching

1. The population of city-11 is 8 thousand greater than that of city-20.
2. The population of city-30 is 5 thousand less than that of city-20.
3. The population of city-40 is 7 thousand greater than that of city-30.

**Question:** by how many thousand is the population of city-11 greater than that of city-40? Answer with a single integer.
**Answer:** `6`
**Check:** 11 = 20 + 8; 40 = 20 − 5 + 7 = 20 + 2; 8 − 2 = 6.

---

## 5. People: age and alias

1. Person-31 is 4 years older than person-44.
2. Person-44 is 6 years younger than person-52.
3. Person-52 is also called "elder-5".

**Question:** by how many years is "elder-5" older than person-31? Answer with a single integer.
**Answer:** `2`
**Check:** 52 = 44 + 6; 31 = 44 + 4; 52 − 31 = 2.

---

## 6. Prices: sequential discounts

1. The price of item-60 is 2500 roubles.
2. Item-60 has a 12 percent discount.
3. After the first discount another 20 percent discount applies.

**Question:** how many roubles does item-60 cost after both discounts? Answer with a single integer.
**Answer:** `1760`
**Check:** 2500 × 0.88 = 2200; 2200 × 0.8 = 1760.

---

## 7. Birds: mass, colour and base altitude

1. The base flight altitude is 100 metres.
2. All birds heavier than 150 grams fly 12 metres above the base altitude.
3. All white birds fly 7 metres below the base altitude.
4. Bird-11: mass 180 grams, colour white.
5. Bird-22: mass 140 grams, colour grey.
6. Bird-33: mass 180 grams, colour grey.

**Question:** by how many metres does bird-11 fly higher than bird-22? Answer with a single integer.
**Answer:** `5`
**Check:** 11: 100 + 12 − 7 = 105; 22: 100; 105 − 100 = 5.

---

## 8. Cars: mileage, colour, plate number

1. The base mileage of a car is 300 kilometres.
2. Red cars travel 25 kilometres more than the base mileage.
3. Cars with numbers divisible by four travel 15 kilometres less than the base mileage.
4. Car-11: red, number 37.
5. Car-22: blue, number 48.

**Question:** by how many kilometres did car-11 travel more than car-22? Answer with a single integer.
**Answer:** `40`
**Check:** 11: 325; 22: 300 − 15 = 285; 325 − 285 = 40.

---

## 9. Counting by two features

1. Jay-12: mass 200 grams, colour white.
2. Jay-13: mass 170 grams, colour white.
3. Jay-14: mass 190 grams, colour grey.
4. Jay-15: mass 160 grams, colour white.
5. Jay-16: mass 150 grams, colour white.
6. Jay-17: mass 180 grams, colour black.
7. Count birds that are both heavier than 160 grams and white.

**Question:** how many birds satisfy both conditions? Answer with a single integer.
**Answer:** `2`
**Check:** 12 (200, white) and 13 (170, white); 14 is grey; 15 and 16 are not heavier than 160.

---

## 10. Ratio instead of difference

1. Heron-40 flies at an altitude of 20 metres.
2. Jay-30 flies 10 metres higher than heron-40.
3. Crow-21 flies 30 metres higher than jay-30.

**Question:** how many times higher does crow-21 fly compared with heron-40? Answer with a single integer.
**Answer:** `3`
**Check:** heron 20; jay 30; crow 60; 60 ÷ 20 = 3.

---

## 11. Rule priority

1. The base cargo capacity of a ship is 50 tonnes.
2. Ships with numbers divisible by five have a capacity 10 tonnes above the base.
3. Ships with numbers divisible by three have a capacity 4 tonnes below the base.
4. If a ship matches both rules, only the divisibility-by-five rule applies.

**Question:** by how many tonnes does ship-15 carry more than ship-18? Answer with a single integer.
**Answer:** `14`
**Check:** 15 is divisible by both 5 and 3 → only the first rule: 60; 18 is divisible by 3 → 46; 60 − 46 = 14.

---

## 12. Group versus group

1. All jays are 30 grams heavier than all crows.
2. All crows are 20 grams heavier than all herons.
3. Jay-07 weighs 150 grams.

**Question:** how many grams does heron-09 weigh? Answer with a single integer.
**Answer:** `100`
**Check:** crow = 150 − 30 = 120; heron = 120 − 20 = 100.

---

## 13. Ability and size

1. The base flight altitude is 80 metres.
2. Birds that can dive fly 15 metres below the base altitude.
3. Birds with a wingspan greater than 120 centimetres fly 10 metres above the base altitude.
4. Bird-11: can dive, wingspan 130 centimetres.
5. Bird-22: cannot dive, wingspan 110 centimetres.

**Question:** by how many metres does bird-11 fly lower than bird-22? Answer with a single integer as "bird-11 minus bird-22".
**Answer:** `-5`
**Check:** 11: 80 − 15 + 10 = 75; 22: 80; 75 − 80 = −5.

---

## 14. Derived property

1. The base flight altitude is 60 metres.
2. All white birds heavier than 100 grams possess the property "silvery".
3. Silvery birds fly 5 metres above the base altitude.
4. Bird-11: white, mass 120 grams.
5. Bird-22: white, mass 90 grams.

**Question:** by how many metres does bird-11 fly higher than bird-22? Answer with a single integer.
**Answer:** `5`
**Check:** 11 is white and heavier than 100 → silvery → 65; 22 is white but lighter → 60; 65 − 60 = 5.

---

## 15. Cats and money: trap with similar entities

1. The black cat Pushok lives with the human Ivan.
2. Every human was given 100 dollars.
3. The human Ivan lives in Paris.
4. Every cat was given 20 dollars.
5. The ginger cat Barsik gave the human Ivan 10 dollars.
6. Every cat living in Paris receives an additional 10 dollars.
7. The cat that gave Ivan 10 dollars takes from the cat living with Ivan as much money as needed to triple his own money.

**Question:** how many dollars do Ivan and his cat have together? Answer with a single integer.
**Answer:** `120`
**Check:** Ivan 100 + 10 = 110; Pushok 20 + 10 = 30, gives 20 → 10; Barsik 20 − 10 = 10, receives 20 → 30. Ivan + his cat = 120.

---

## 16. Variables and an array: state mutation

1. `x_a17 = 27; bx4 = 7; x_var4 = -99; x_arr = [1, 3, 5, 9].`
2. Executed: `x_a17 += bx4; x_arr[0] += x_arr[3].`
3. All variables with the `x_` prefix that hold an even integer value are halved; for the array the operation is applied element-wise.

**Question:** what is the sum of all elements of `x_arr` plus the value of `x_a17`? Answer with a single integer.
**Answer:** `39`
**Check:** `x_a17` = 34 → 17; `x_arr` = [10,3,5,9] → [5,3,5,9]; sum 22 + 17 = 39.

---

## 17. Land: order of events and a cancelled record

1. On 20 June 2016 John14 acquired 30 acres of land.
2. In the penultimate record of this document John14 is mistakenly called Johan15.
3. The last record in order of mention (not by date) about John14's land operations is erroneous and must not be counted.
4. In 1999 John14 had 100 acres of land.
5. On 8 March 2008 John14 sold half of his land.
6. All land operations performed by John14 are listed in this document.
7. At the end of 2004 Johan15 acquired 60 acres of land.
8. In 2010 John sold 40 acres of land.

**Question:** how many acres of land does John14 have in 2026? Answer with a single integer.
**Answer:** `110`
**Check:** 1999: 100. 2004: "Johan15" is John14 (penultimate record), +60 → 160. 2008: sold half → 80. 2010: last record by mention — cancelled. 2016: +30 → 110. If the 2010 record were counted, the answer would be 70.

---

## Summary

| # | Move type | Answer |
|---|---|---|
1 | linear chain, sum of offsets | 13 |
2 | group rules by divisibility | 6 |
3 | star, max minus min | 40 |
4 | branching, two paths | 6 |
5 | age and alias | 2 |
6 | sequential percentages | 1760 |
7 | mass + colour thresholds | 5 |
8 | mileage + colour + divisibility | 40 |
9 | counting by two features | 2 |
10 | ratio | 3 |
11 | rule priority | 14 |
12 | group versus group | 100 |
13 | ability and size | -5 |
14 | derived property | 5 |
15 | money trap | 120 |
16 | state mutation | 39 |
17 | cancellation by order of mention | 110 |
