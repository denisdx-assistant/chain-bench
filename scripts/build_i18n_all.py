#!/usr/bin/env python3
"""Build i18n_tasks_all.json: all 17 tasks in ru/en/zh.

Russian blocks come from tasks_final.json; English and Chinese blocks are
reused from i18n_tasks.json where they exist and supplied below for the
remaining tasks (4, 5, 8, 10, 11, 12, 14, 15, 16).

Statement counts are kept identical to Russian so that the shared seed
produces parallel noise across languages.
"""
import json

NEW = {
 4: {
  "en": {
   "statements": [
    "The population of city-11 is 8 thousand greater than that of city-20.",
    "The population of city-30 is 5 thousand less than that of city-20.",
    "The population of city-40 is 7 thousand greater than that of city-30.",
   ],
   "question": "By how many thousand is the population of city-11 greater than that of city-40? Answer with a single integer.",
  },
  "zh": {
   "statements": [
    "11 号城市的人口比 20 号城市多 8 千人。",
    "30 号城市的人口比 20 号城市少 5 千人。",
    "40 号城市的人口比 30 号城市多 7 千人。",
   ],
   "question": "11 号城市的人口比 40 号城市多多少千人？只回答一个整数。",
  },
 },
 5: {
  "en": {
   "statements": [
    "Person-31 is 4 years older than person-44.",
    "Person-44 is 6 years younger than person-52.",
    'Person-52 is also called "old-timer-5".',
   ],
   "question": 'By how many years is "old-timer-5" older than person-31? Answer with a single integer.',
  },
  "zh": {
   "statements": [
    "31 号人比 44 号人大 4 岁。",
    "44 号人比 52 号人小 6 岁。",
    "52 号人也被称为“老居民-5”。",
   ],
   "question": "“老居民-5”比 31 号人大多少岁？只回答一个整数。",
  },
 },
 8: {
  "en": {
   "statements": [
    "The base mileage of a car is 300 kilometres.",
    "Red cars travel 25 kilometres more than the base mileage.",
    "Cars with numbers divisible by four travel 15 kilometres less than the base mileage.",
    "Car-11: red, number 37.",
    "Car-22: blue, number 48.",
   ],
   "question": "By how many kilometres did car-11 travel more than car-22? Answer with a single integer.",
  },
  "zh": {
   "statements": [
    "汽车的基准里程为 300 公里。",
    "红色汽车比基准里程多行驶 25 公里。",
    "编号能被四整除的汽车比基准里程少行驶 15 公里。",
    "11 号汽车：红色，编号 37。",
    "22 号汽车：蓝色，编号 48。",
   ],
   "question": "11 号汽车比 22 号汽车多行驶多少公里？只回答一个整数。",
  },
 },
 10: {
  "en": {
   "statements": [
    "Heron-40 flies at an altitude of 20 metres.",
    "Jay-30 flies 10 metres higher than heron-40.",
    "Raven-21 flies 30 metres higher than jay-30.",
   ],
   "question": "How many times higher does raven-21 fly than heron-40? Answer with a single integer.",
  },
  "zh": {
   "statements": [
    "40 号苍鹭在 20 米的高度飞行。",
    "30 号松鸦比 40 号苍鹭飞得高 10 米。",
    "21 号乌鸦比 30 号松鸦飞得高 30 米。",
   ],
   "question": "21 号乌鸦的飞行高度是 40 号苍鹭的多少倍？只回答一个整数。",
  },
 },
 11: {
  "en": {
   "statements": [
    "The base cargo capacity of a ship is 50 tonnes.",
    "Ships with numbers divisible by five have a capacity 10 tonnes above the base.",
    "Ships with numbers divisible by three have a capacity 4 tonnes below the base.",
    "If a ship matches both rules, only the rule of divisibility by five applies.",
   ],
   "question": "By how many tonnes does ship-15 carry more than ship-18? Answer with a single integer.",
  },
  "zh": {
   "statements": [
    "船舶的基准载重为 50 吨。",
    "编号能被五整除的船，载重比基准高 10 吨。",
    "编号能被三整除的船，载重比基准低 4 吨。",
    "若船舶同时符合两条规则，只适用五的倍数规则。",
   ],
   "question": "15 号船比 18 号船多载多少吨？只回答一个整数。",
  },
 },
 12: {
  "en": {
   "statements": [
    "All jays are 30 grams heavier than all crows.",
    "All crows are 20 grams heavier than all herons.",
    "Jay-07 weighs 150 grams.",
   ],
   "question": "How many grams does heron-09 weigh? Answer with a single integer.",
  },
  "zh": {
   "statements": [
    "所有松鸦都比所有乌鸦重 30 克。",
    "所有乌鸦都比所有苍鹭重 20 克。",
    "07 号松鸦重 150 克。",
   ],
   "question": "09 号苍鹭重多少克？只回答一个整数。",
  },
 },
 14: {
  "en": {
   "statements": [
    "The base flight altitude is 60 metres.",
    'All white birds heavier than 100 grams have the property "silvery".',
    "Silvery birds fly 5 metres above the base altitude.",
    "Bird-11: white, mass 120 grams.",
    "Bird-22: white, mass 90 grams.",
   ],
   "question": "By how many metres does bird-11 fly higher than bird-22? Answer with a single integer.",
  },
  "zh": {
   "statements": [
    "基准飞行高度为 60 米。",
    "所有重于 100 克的白色鸟具有“银色”属性。",
    "银色鸟的飞行高度比基准高 5 米。",
    "11 号鸟：白色，体重 120 克。",
    "22 号鸟：白色，体重 90 克。",
   ],
   "question": "11 号鸟比 22 号鸟飞得高多少米？只回答一个整数。",
  },
 },
 15: {
  "en": {
   "statements": [
    "The black cat Pushok lives together with the person Ivan.",
    "All people were given 100 dollars.",
    "The person Ivan lives in Paris.",
    "All cats were given 20 dollars.",
    "The ginger cat Barsik gave the person Ivan 10 dollars.",
    "Every cat living in Paris receives an additional 10 dollars.",
    "The cat that gave Ivan 10 dollars takes from the cat living with Ivan as much money as needed to triple its own money.",
   ],
   "question": "How many dollars do Ivan and his cat have together? Answer with a single integer.",
  },
  "zh": {
   "statements": [
    "黑猫普肖克与人伊万住在一起。",
    "所有人都获得了 100 美元。",
    "人伊万住在巴黎。",
    "所有猫都获得了 20 美元。",
    "橘猫巴尔西克给了人伊万 10 美元。",
    "每只住在巴黎的猫额外获得 10 美元。",
    "给了伊万 10 美元的猫，从与伊万同住的猫那里拿走让它自己的钱变为三倍所需的金额。",
   ],
   "question": "伊万和他的猫一共有多少美元？只回答一个整数。",
  },
 },
 16: {
  "en": {
   "statements": [
    "x_a17 = 27; bx4 = 7; x_var4 = -99; x_arr = [1, 3, 5, 9].",
    "Executed: x_a17 += bx4; x_arr[0] += x_arr[3].",
    "All variables with the prefix x_ that have an even integer value are halved; for the array the operation is applied element-wise.",
   ],
   "question": "What is the sum of all elements of the array x_arr plus the value of x_a17? Answer with a single integer.",
  },
  "zh": {
   "statements": [
    "x_a17 = 27; bx4 = 7; x_var4 = -99; x_arr = [1, 3, 5, 9]。",
    "已执行：x_a17 += bx4; x_arr[0] += x_arr[3]。",
    "所有以 x_ 为前缀且具有偶数整数值的变量都减半；对数组则逐元素执行该操作。",
   ],
   "question": "数组 x_arr 所有元素之和加上 x_a17 的值等于多少？只回答一个整数。",
  },
 },
}


def main():
    tasks = json.load(open("tasks_final.json"))
    existing = json.load(open("i18n_tasks.json"))
    out = {}
    for t in tasks:
        tid = str(t["id"])
        blocks = {"ru": {"statements": list(t["statements"]), "question": t["question"]}}
        if tid in existing:
            blocks["en"] = existing[tid]["en"]
            blocks["zh"] = existing[tid]["zh"]
        elif t["id"] in NEW:
            blocks["en"] = NEW[t["id"]]["en"]
            blocks["zh"] = NEW[t["id"]]["zh"]
        else:
            raise SystemExit("no translation for task %s" % tid)
        out[tid] = blocks

    # parity fix: the earlier 8-task translation of task 2 omitted the
    # ship-52 distractor present in the Russian original
    ADD = {"2": {"en": "Ship-52 matches neither rule.",
                 "zh": "52 号船不符合任何规则。"}}
    for tid, langs in ADD.items():
        for lang, line in langs.items():
            st = out[tid][lang]["statements"]
            if line not in st:
                st.append(line)

    json.dump(out, open("i18n_tasks_all.json", "w"), ensure_ascii=False, indent=1)

    # sanity: statement counts identical across languages
    bad = []
    for tid, b in out.items():
        n = {k: len(v["statements"]) for k, v in b.items()}
        if len(set(n.values())) != 1:
            bad.append((tid, n))
    print("задач:", len(out), "| несовпадение числа утверждений:", bad or "нет")
    for tid in ("4", "5", "8", "10", "11", "12", "14", "15", "16"):
        print("  %s: en %d / zh %d утверждений" % (tid, len(out[tid]["en"]["statements"]), len(out[tid]["zh"]["statements"])))


if __name__ == "__main__":
    main()
