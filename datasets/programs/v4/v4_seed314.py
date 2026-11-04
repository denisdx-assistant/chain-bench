"""Тест 2 v4: исполнить программу, назвать массив и сумму."""

import re

def acc(a, n):
    if n <= 0:
        return 0
    return a[n - 1] + acc(a, n - 1)

def bump(a, i, v):
    a[i] += v

def bump_all(a, v):
    for i in range(0, len(a), 2):
        a[i] += v

def mix(a):
    out = []
    for x in a:
        out.append(int(str(x) + '7') % 100)
    return out

def apply_twice(a, i, v):
    bump(a, i, v)
    bump(a, i, v)

MANUAL = """
arr[6] += 57
arr2[0] = 9
arr[3] = 16
arr[4], arr[0] = arr[0], arr[4]
arr[5] += 53
arr[8] *= 48
arr[9] += 42
arr2[8] = 10
"""

TRAP_0 = "arr[7] = 153"
TRAP_1 = "arr[7] = 731"
TRAP_2 = "arr[5] = 644"
TRAP_3 = "arr[3] = 425"
TRAP_4 = "arr[8] = 819"
TRAP_5 = "arr[0] = 907"
TRAP_6 = "arr[1] = 803"
TRAP_7 = "arr[7] = 496"
TRAP_8 = "arr[9] = 594"
TRAP_9 = "arr[8] = 214"
TRAP_10 = "arr[1] = 251"
TRAP_11 = "arr[4] = 580"
TRAP_12 = "arr[8] = 509"
TRAP_13 = "arr[6] = 449"
TRAP_14 = "arr[9] = 514"
TRAP_15 = "arr[3] = 385"
TRAP_16 = "arr[1] = 150"
TRAP_17 = "arr[3] = 303"
TRAP_18 = "arr[0] = 708"
TRAP_19 = "arr[7] = 771"
TRAP_20 = "arr[4] = 304"
TRAP_21 = "arr[5] = 843"
TRAP_22 = "arr[0] = 534"
TRAP_23 = "arr[1] = 990"
TRAP_24 = "arr[7] = 371"
TRAP_25 = "arr[5] = 437"
TRAP_26 = "arr[1] = 512"
TRAP_27 = "arr[9] = 355"
TRAP_28 = "arr[3] = 889"
TRAP_29 = "arr[0] = 454"
TRAP_30 = "arr[9] = 554"
TRAP_31 = "arr[5] = 404"
TRAP_32 = "arr[1] = 104"
TRAP_33 = "arr[8] = 424"
TRAP_34 = "arr[6] = 276"
TRAP_35 = "arr[0] = 968"
TRAP_36 = "arr[6] = 537"
TRAP_37 = "arr[6] = 349"
TRAP_38 = "arr[5] = 114"
TRAP_39 = "arr[1] = 891"
TRAP_40 = "arr[3] = 459"
TRAP_41 = "arr[3] = 344"
TRAP_42 = "arr[7] = 704"
TRAP_43 = "arr[1] = 356"
TRAP_44 = "arr[8] = 107"
TRAP_45 = "arr[5] = 597"
TRAP_46 = "arr[5] = 745"
TRAP_47 = "arr[3] = 522"
TRAP_48 = "arr[2] = 435"
TRAP_49 = "arr[8] = 308"
TRAP_50 = "arr[8] = 124"
TRAP_51 = "arr[2] = 196"
TRAP_52 = "arr[3] = 588"
TRAP_53 = "arr[8] = 764"
TRAP_54 = "arr[5] = 737"
TRAP_55 = "arr[8] = 876"
TRAP_56 = "arr[3] = 285"
TRAP_57 = "arr[2] = 915"
TRAP_58 = "arr[0] = 763"
TRAP_59 = "arr[9] = 666"
TRAP_60 = "arr[5] = 501"
TRAP_61 = "arr[9] = 806"
TRAP_62 = "arr[1] = 939"
TRAP_63 = "arr[6] = 913"
TRAP_64 = "arr[5] = 656"
TRAP_65 = "arr[5] = 832"
TRAP_66 = "arr[0] = 600"
TRAP_67 = "arr[7] = 345"
TRAP_68 = "arr[8] = 845"
TRAP_69 = "arr[9] = 827"
TRAP_70 = "arr[3] = 608"
TRAP_71 = "arr[3] = 531"
TRAP_72 = "arr[9] = 428"
TRAP_73 = "arr[0] = 583"
TRAP_74 = "arr[8] = 618"
TRAP_75 = "arr[5] = 852"
TRAP_76 = "arr[9] = 659"
TRAP_77 = "arr[5] = 461"
TRAP_78 = "arr[4] = 303"
TRAP_79 = "arr[0] = 513"
TRAP_80 = "arr[5] = 235"
TRAP_81 = "arr[9] = 207"
TRAP_82 = "arr[8] = 951"
TRAP_83 = "arr[5] = 317"
TRAP_84 = "arr[5] = 282"
TRAP_85 = "arr[7] = 462"
TRAP_86 = "arr[5] = 834"
TRAP_87 = "arr[1] = 362"
TRAP_88 = "arr[6] = 694"
TRAP_89 = "arr[3] = 914"
TRAP_90 = "arr[3] = 865"
TRAP_91 = "arr[0] = 850"
TRAP_92 = "arr[0] = 766"
TRAP_93 = "arr[6] = 660"
TRAP_94 = "arr[4] = 531"
TRAP_95 = "arr[3] = 601"
TRAP_96 = "arr[7] = 192"
TRAP_97 = "arr[8] = 850"
TRAP_98 = "arr[8] = 177"
TRAP_99 = "arr[0] = 807"
TRAP_100 = "arr[4] = 257"
TRAP_101 = "arr[6] = 268"
TRAP_102 = "arr[0] = 376"
TRAP_103 = "arr[2] = 337"
TRAP_104 = "arr[1] = 718"
TRAP_105 = "arr[7] = 968"
TRAP_106 = "arr[9] = 868"
TRAP_107 = "arr[7] = 966"
TRAP_108 = "arr[0] = 406"
TRAP_109 = "arr[8] = 631"
TRAP_110 = "arr[9] = 588"
TRAP_111 = "arr[0] = 530"
TRAP_112 = "arr[7] = 164"
TRAP_113 = "arr[0] = 125"
TRAP_114 = "arr[2] = 896"
TRAP_115 = "arr[3] = 741"
TRAP_116 = "arr[3] = 170"
TRAP_117 = "arr[4] = 371"
TRAP_118 = "arr[2] = 631"
TRAP_119 = "arr[7] = 596"
TRAP_120 = "arr[2] = 556"
TRAP_121 = "arr[6] = 909"
TRAP_122 = "arr[0] = 546"
TRAP_123 = "arr[5] = 293"
TRAP_124 = "arr[2] = 441"
TRAP_125 = "arr[6] = 570"
TRAP_126 = "arr[0] = 582"
TRAP_127 = "arr[0] = 850"
TRAP_128 = "arr[3] = 785"
TRAP_129 = "arr[3] = 923"
TRAP_130 = "arr[8] = 628"
TRAP_131 = "arr[6] = 997"
TRAP_132 = "arr[0] = 374"
TRAP_133 = "arr[8] = 386"
TRAP_134 = "arr[1] = 222"
TRAP_135 = "arr[7] = 170"
TRAP_136 = "arr[8] = 497"
TRAP_137 = "arr[6] = 267"
TRAP_138 = "arr[5] = 707"
TRAP_139 = "arr[1] = 503"
TRAP_140 = "arr[0] = 399"
TRAP_141 = "arr[4] = 926"
TRAP_142 = "arr[2] = 350"
TRAP_143 = "arr[4] = 273"
TRAP_144 = "arr[0] = 277"
TRAP_145 = "arr[2] = 136"
TRAP_146 = "arr[6] = 820"
TRAP_147 = "arr[6] = 732"
TRAP_148 = "arr[6] = 348"
TRAP_149 = "arr[9] = 662"

arr = [7, 15, 4, 6, 1, 21, 21, 10, 8, 13]

code_0 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_1 = arr[9] + 11
tmp_2 = arr[7] + 36
tmp_3 = arr[5] + 38
tmp_4 = arr[4] + 45
tmp_5 = arr[0] + 7
tmp_6 = arr[8] + 49
copy_7 = arr[3]
note_8 = str(arr[3]) + str(arr[2])
note_9 = str(arr[0]) + str(arr[5])
tmp_10 = arr[5] + 26
label_11 = "запись 11 не применялась"
note_12 = str(arr[8]) + str(arr[2])
note_13 = str(arr[6]) + str(arr[0])
code_14 = re.sub(r'[0-9]', '#', str(arr[9]))
note_15 = str(arr[0]) + str(arr[6])
copy_16 = arr[7]
note_17 = str(arr[5]) + str(arr[3])
tmp_18 = arr[4] + 9
label_19 = "запись 19 не применялась"
copy_20 = arr[1]
copy_21 = arr[9]
tmp_22 = arr[7] + 50
tmp_23 = arr[8] + 27
label_24 = "запись 24 не применялась"
copy_25 = arr[2]
code_26 = re.sub(r'[0-9]', '#', str(arr[6]))
note_27 = str(arr[9]) + str(arr[0])
code_28 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_29 = arr[3]
copy_30 = arr[4]
label_31 = "запись 31 не применялась"
note_32 = str(arr[7]) + str(arr[1])
code_33 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_34 = arr[4]
copy_35 = arr[2]
code_36 = re.sub(r'[0-9]', '#', str(arr[4]))
note_37 = str(arr[2]) + str(arr[8])
code_38 = re.sub(r'[0-9]', '#', str(arr[8]))
note_39 = str(arr[0]) + str(arr[0])
copy_40 = arr[3]
code_41 = re.sub(r'[0-9]', '#', str(arr[1]))
note_42 = str(arr[5]) + str(arr[2])
code_43 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_44 = arr[1] + 26
note_45 = str(arr[7]) + str(arr[2])
tmp_46 = arr[4] + 6
label_47 = "запись 47 не применялась"
label_48 = "запись 48 не применялась"
tmp_49 = arr[9] + 44
tmp_50 = arr[3] + 13
label_51 = "запись 51 не применялась"
code_52 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_53 = arr[8] + 8
tmp_54 = arr[4] + 26
label_55 = "запись 55 не применялась"
copy_56 = arr[0]
tmp_57 = arr[5] + 34
tmp_58 = arr[0] + 27
tmp_59 = arr[7] + 11
copy_60 = arr[1]
tmp_61 = arr[0] + 28
copy_62 = arr[9]
note_63 = str(arr[4]) + str(arr[7])
tmp_64 = arr[1] + 34
label_65 = "запись 65 не применялась"
note_66 = str(arr[5]) + str(arr[7])
copy_67 = arr[3]
code_68 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_69 = arr[8] + 1
tmp_70 = arr[0] + 47
note_71 = str(arr[1]) + str(arr[0])
code_72 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_73 = arr[3] + 14
copy_74 = arr[6]
code_75 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_76 = arr[1]
code_77 = re.sub(r'[0-9]', '#', str(arr[1]))
note_78 = str(arr[2]) + str(arr[4])
copy_79 = arr[1]
note_80 = str(arr[3]) + str(arr[7])
label_81 = "запись 81 не применялась"
note_82 = str(arr[6]) + str(arr[3])
copy_83 = arr[2]
tmp_84 = arr[0] + 44
tmp_85 = arr[2] + 43
code_86 = re.sub(r'[0-9]', '#', str(arr[3]))
code_87 = re.sub(r'[0-9]', '#', str(arr[6]))
label_88 = "запись 88 не применялась"
copy_89 = arr[3]
tmp_90 = arr[9] + 24
tmp_91 = arr[0] + 42
note_92 = str(arr[2]) + str(arr[3])
tmp_93 = arr[7] + 36
note_94 = str(arr[2]) + str(arr[7])
tmp_95 = arr[6] + 22
tmp_96 = arr[2] + 3
tmp_97 = arr[3] + 46
copy_98 = arr[4]
note_99 = str(arr[0]) + str(arr[7])
note_100 = str(arr[8]) + str(arr[0])
note_101 = str(arr[0]) + str(arr[6])
tmp_102 = arr[6] + 22
note_103 = str(arr[0]) + str(arr[4])
note_104 = str(arr[0]) + str(arr[2])
label_105 = "запись 105 не применялась"
label_106 = "запись 106 не применялась"
tmp_107 = arr[4] + 50
copy_108 = arr[2]
tmp_109 = arr[7] + 40
label_110 = "запись 110 не применялась"
tmp_111 = arr[4] + 40
copy_112 = arr[7]
note_113 = str(arr[3]) + str(arr[3])
copy_114 = arr[0]
tmp_115 = arr[3] + 44
code_116 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_117 = arr[8] + 33
code_118 = re.sub(r'[0-9]', '#', str(arr[4]))
code_119 = re.sub(r'[0-9]', '#', str(arr[8]))
note_120 = str(arr[9]) + str(arr[9])
code_121 = re.sub(r'[0-9]', '#', str(arr[8]))
note_122 = str(arr[9]) + str(arr[2])
code_123 = re.sub(r'[0-9]', '#', str(arr[7]))
code_124 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_125 = arr[4] + 43
copy_126 = arr[3]
copy_127 = arr[0]
tmp_128 = arr[8] + 42
code_129 = re.sub(r'[0-9]', '#', str(arr[4]))
note_130 = str(arr[7]) + str(arr[2])
note_131 = str(arr[7]) + str(arr[2])
code_132 = re.sub(r'[0-9]', '#', str(arr[1]))
label_133 = "запись 133 не применялась"
tmp_134 = arr[2] + 33
copy_135 = arr[3]
note_136 = str(arr[0]) + str(arr[4])
label_137 = "запись 137 не применялась"
code_138 = re.sub(r'[0-9]', '#', str(arr[4]))
note_139 = str(arr[4]) + str(arr[1])
tmp_140 = arr[6] + 48
label_141 = "запись 141 не применялась"
label_142 = "запись 142 не применялась"
copy_143 = arr[0]
tmp_144 = arr[2] + 31
note_145 = str(arr[8]) + str(arr[8])
note_146 = str(arr[4]) + str(arr[8])
copy_147 = arr[1]
note_148 = str(arr[0]) + str(arr[4])
copy_149 = arr[5]
label_150 = "запись 150 не применялась"
note_151 = str(arr[7]) + str(arr[5])
copy_152 = arr[0]
tmp_153 = arr[2] + 23
note_154 = str(arr[4]) + str(arr[8])
note_155 = str(arr[2]) + str(arr[2])
copy_156 = arr[5]
copy_157 = arr[2]
tmp_158 = arr[9] + 23
code_159 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_160 = arr[3] + 6
note_161 = str(arr[9]) + str(arr[8])
code_162 = re.sub(r'[0-9]', '#', str(arr[4]))
code_163 = re.sub(r'[0-9]', '#', str(arr[8]))
note_164 = str(arr[2]) + str(arr[0])
note_165 = str(arr[2]) + str(arr[0])
tmp_166 = arr[1] + 35
note_167 = str(arr[6]) + str(arr[1])
note_168 = str(arr[9]) + str(arr[8])
note_169 = str(arr[1]) + str(arr[5])
copy_170 = arr[4]
note_171 = str(arr[7]) + str(arr[5])
note_172 = str(arr[3]) + str(arr[6])
code_173 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_174 = arr[3] + 37
note_175 = str(arr[0]) + str(arr[5])
note_176 = str(arr[9]) + str(arr[7])
tmp_177 = arr[9] + 39
note_178 = str(arr[2]) + str(arr[8])
note_179 = str(arr[9]) + str(arr[7])
code_180 = re.sub(r'[0-9]', '#', str(arr[3]))
label_181 = "запись 181 не применялась"
code_182 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_183 = arr[4] + 17
code_184 = re.sub(r'[0-9]', '#', str(arr[6]))
code_185 = re.sub(r'[0-9]', '#', str(arr[4]))
code_186 = re.sub(r'[0-9]', '#', str(arr[6]))
code_187 = re.sub(r'[0-9]', '#', str(arr[1]))
label_188 = "запись 188 не применялась"
copy_189 = arr[6]
tmp_190 = arr[7] + 3
tmp_191 = arr[2] + 41
label_192 = "запись 192 не применялась"
tmp_193 = arr[0] + 12
tmp_194 = arr[0] + 39
note_195 = str(arr[3]) + str(arr[7])
note_196 = str(arr[4]) + str(arr[7])
note_197 = str(arr[7]) + str(arr[8])
tmp_198 = arr[8] + 22
copy_199 = arr[0]
note_200 = str(arr[9]) + str(arr[5])
tmp_201 = arr[2] + 21
code_202 = re.sub(r'[0-9]', '#', str(arr[5]))
code_203 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_204 = arr[4]
code_205 = re.sub(r'[0-9]', '#', str(arr[4]))
code_206 = re.sub(r'[0-9]', '#', str(arr[9]))
note_207 = str(arr[6]) + str(arr[1])
copy_208 = arr[6]
note_209 = str(arr[9]) + str(arr[6])
copy_210 = arr[1]
label_211 = "запись 211 не применялась"
copy_212 = arr[2]
label_213 = "запись 213 не применялась"
copy_214 = arr[3]
note_215 = str(arr[3]) + str(arr[7])
copy_216 = arr[7]
code_217 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_218 = arr[1] + 4
note_219 = str(arr[3]) + str(arr[4])
note_220 = str(arr[5]) + str(arr[7])
code_221 = re.sub(r'[0-9]', '#', str(arr[2]))
note_222 = str(arr[0]) + str(arr[5])
note_223 = str(arr[2]) + str(arr[7])
note_224 = str(arr[1]) + str(arr[3])
copy_225 = arr[5]
code_226 = re.sub(r'[0-9]', '#', str(arr[5]))
label_227 = "запись 227 не применялась"
tmp_228 = arr[5] + 43
code_229 = re.sub(r'[0-9]', '#', str(arr[6]))
note_230 = str(arr[5]) + str(arr[0])
tmp_231 = arr[6] + 44
note_232 = str(arr[3]) + str(arr[0])
note_233 = str(arr[9]) + str(arr[4])
code_234 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_235 = arr[9]
note_236 = str(arr[6]) + str(arr[5])
code_237 = re.sub(r'[0-9]', '#', str(arr[2]))
note_238 = str(arr[1]) + str(arr[4])
code_239 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_240 = arr[2]
tmp_241 = arr[5] + 41
label_242 = "запись 242 не применялась"
copy_243 = arr[7]
code_244 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_245 = arr[3] + 48
code_246 = re.sub(r'[0-9]', '#', str(arr[8]))
label_247 = "запись 247 не применялась"
copy_248 = arr[7]
tmp_249 = arr[5] + 28
note_250 = str(arr[7]) + str(arr[1])
code_251 = re.sub(r'[0-9]', '#', str(arr[6]))
label_252 = "запись 252 не применялась"
label_253 = "запись 253 не применялась"
code_254 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_255 = arr[8] + 45
copy_256 = arr[7]
tmp_257 = arr[2] + 50
copy_258 = arr[5]
code_259 = re.sub(r'[0-9]', '#', str(arr[3]))
label_260 = "запись 260 не применялась"
note_261 = str(arr[0]) + str(arr[8])
copy_262 = arr[4]
code_263 = re.sub(r'[0-9]', '#', str(arr[3]))
code_264 = re.sub(r'[0-9]', '#', str(arr[1]))
code_265 = re.sub(r'[0-9]', '#', str(arr[3]))
note_266 = str(arr[5]) + str(arr[6])
note_267 = str(arr[0]) + str(arr[4])
label_268 = "запись 268 не применялась"
code_269 = re.sub(r'[0-9]', '#', str(arr[9]))
note_270 = str(arr[9]) + str(arr[2])
note_271 = str(arr[8]) + str(arr[2])
copy_272 = arr[2]
code_273 = re.sub(r'[0-9]', '#', str(arr[2]))
note_274 = str(arr[7]) + str(arr[8])
code_275 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_276 = arr[2] + 35
code_277 = re.sub(r'[0-9]', '#', str(arr[8]))
code_278 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_279 = arr[4]
label_280 = "запись 280 не применялась"
copy_281 = arr[1]
note_282 = str(arr[8]) + str(arr[7])
note_283 = str(arr[9]) + str(arr[2])
note_284 = str(arr[4]) + str(arr[5])
note_285 = str(arr[2]) + str(arr[2])
note_286 = str(arr[2]) + str(arr[3])
note_287 = str(arr[9]) + str(arr[1])
note_288 = str(arr[0]) + str(arr[5])
code_289 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_290 = arr[6] + 46
note_291 = str(arr[2]) + str(arr[0])
copy_292 = arr[2]
label_293 = "запись 293 не применялась"
tmp_294 = arr[3] + 11
tmp_295 = arr[8] + 15
note_296 = str(arr[8]) + str(arr[2])
code_297 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_298 = arr[1]
code_299 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_300 = arr[3] + 13
note_301 = str(arr[6]) + str(arr[8])
note_302 = str(arr[4]) + str(arr[1])
copy_303 = arr[7]
note_304 = str(arr[5]) + str(arr[3])
label_305 = "запись 305 не применялась"
tmp_306 = arr[2] + 37
code_307 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_308 = arr[8]
tmp_309 = arr[2] + 46
code_310 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_311 = arr[6]
label_312 = "запись 312 не применялась"
code_313 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_314 = arr[5] + 4
code_315 = re.sub(r'[0-9]', '#', str(arr[0]))
note_316 = str(arr[2]) + str(arr[9])
tmp_317 = arr[1] + 15
note_318 = str(arr[2]) + str(arr[2])
tmp_319 = arr[5] + 14
code_320 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_321 = arr[6] + 44
tmp_322 = arr[1] + 13
tmp_323 = arr[3] + 37
code_324 = re.sub(r'[0-9]', '#', str(arr[9]))
note_325 = str(arr[5]) + str(arr[3])
tmp_326 = arr[6] + 37
note_327 = str(arr[1]) + str(arr[7])
label_328 = "запись 328 не применялась"
tmp_329 = arr[9] + 8
copy_330 = arr[6]
copy_331 = arr[5]
code_332 = re.sub(r'[0-9]', '#', str(arr[4]))
note_333 = str(arr[1]) + str(arr[4])
note_334 = str(arr[6]) + str(arr[0])
code_335 = re.sub(r'[0-9]', '#', str(arr[7]))
code_336 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_337 = arr[1] + 48
tmp_338 = arr[6] + 44
code_339 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_340 = arr[0] + 40
code_341 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_342 = arr[8]
note_343 = str(arr[0]) + str(arr[6])
note_344 = str(arr[8]) + str(arr[2])
code_345 = re.sub(r'[0-9]', '#', str(arr[2]))
label_346 = "запись 346 не применялась"
code_347 = re.sub(r'[0-9]', '#', str(arr[1]))
note_348 = str(arr[7]) + str(arr[3])
label_349 = "запись 349 не применялась"
code_350 = re.sub(r'[0-9]', '#', str(arr[4]))
code_351 = re.sub(r'[0-9]', '#', str(arr[5]))
note_352 = str(arr[8]) + str(arr[1])
tmp_353 = arr[4] + 49
note_354 = str(arr[5]) + str(arr[5])
code_355 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_356 = arr[6] + 20
code_357 = re.sub(r'[0-9]', '#', str(arr[2]))
code_358 = re.sub(r'[0-9]', '#', str(arr[3]))
code_359 = re.sub(r'[0-9]', '#', str(arr[3]))
note_360 = str(arr[7]) + str(arr[3])
tmp_361 = arr[4] + 32
label_362 = "запись 362 не применялась"
note_363 = str(arr[5]) + str(arr[4])
note_364 = str(arr[7]) + str(arr[6])
note_365 = str(arr[7]) + str(arr[6])
note_366 = str(arr[7]) + str(arr[2])
note_367 = str(arr[9]) + str(arr[2])
note_368 = str(arr[9]) + str(arr[7])
tmp_369 = arr[4] + 17
tmp_370 = arr[2] + 12
tmp_371 = arr[6] + 32
tmp_372 = arr[0] + 17
code_373 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_374 = arr[1] + 32
tmp_375 = arr[6] + 20
note_376 = str(arr[2]) + str(arr[5])
tmp_377 = arr[9] + 19
tmp_378 = arr[0] + 37
tmp_379 = arr[5] + 44
note_380 = str(arr[4]) + str(arr[2])
note_381 = str(arr[2]) + str(arr[8])
code_382 = re.sub(r'[0-9]', '#', str(arr[0]))
code_383 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_384 = arr[4] + 50
copy_385 = arr[5]
note_386 = str(arr[2]) + str(arr[5])
note_387 = str(arr[3]) + str(arr[5])
tmp_388 = arr[0] + 13
tmp_389 = arr[9] + 44
label_390 = "запись 390 не применялась"
note_391 = str(arr[0]) + str(arr[1])
note_392 = str(arr[1]) + str(arr[4])
code_393 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_394 = arr[9] + 46
tmp_395 = arr[1] + 9
label_396 = "запись 396 не применялась"
note_397 = str(arr[4]) + str(arr[0])
note_398 = str(arr[4]) + str(arr[5])
copy_399 = arr[5]
note_400 = str(arr[2]) + str(arr[1])
note_401 = str(arr[4]) + str(arr[3])
note_402 = str(arr[5]) + str(arr[7])
code_403 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_404 = arr[5]
copy_405 = arr[9]
note_406 = str(arr[0]) + str(arr[8])
tmp_407 = arr[2] + 10
tmp_408 = arr[9] + 13
note_409 = str(arr[8]) + str(arr[2])
tmp_410 = arr[3] + 7
code_411 = re.sub(r'[0-9]', '#', str(arr[1]))
note_412 = str(arr[6]) + str(arr[7])
code_413 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_414 = arr[1] + 19
note_415 = str(arr[8]) + str(arr[4])
note_416 = str(arr[8]) + str(arr[4])
tmp_417 = arr[5] + 23
label_418 = "запись 418 не применялась"
note_419 = str(arr[1]) + str(arr[4])
label_420 = "запись 420 не применялась"
tmp_421 = arr[5] + 11
note_422 = str(arr[5]) + str(arr[8])
code_423 = re.sub(r'[0-9]', '#', str(arr[3]))
code_424 = re.sub(r'[0-9]', '#', str(arr[2]))
code_425 = re.sub(r'[0-9]', '#', str(arr[8]))
code_426 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_427 = arr[3]
code_428 = re.sub(r'[0-9]', '#', str(arr[6]))
code_429 = re.sub(r'[0-9]', '#', str(arr[0]))
note_430 = str(arr[8]) + str(arr[7])
tmp_431 = arr[8] + 29
tmp_432 = arr[0] + 15
tmp_433 = arr[9] + 45
tmp_434 = arr[2] + 2
tmp_435 = arr[9] + 17
note_436 = str(arr[1]) + str(arr[3])
tmp_437 = arr[2] + 28
tmp_438 = arr[4] + 38
code_439 = re.sub(r'[0-9]', '#', str(arr[2]))
note_440 = str(arr[1]) + str(arr[7])
tmp_441 = arr[3] + 29
copy_442 = arr[0]
note_443 = str(arr[9]) + str(arr[0])
tmp_444 = arr[1] + 16
copy_445 = arr[7]
tmp_446 = arr[8] + 31
tmp_447 = arr[4] + 20
label_448 = "запись 448 не применялась"
copy_449 = arr[3]
tmp_450 = arr[4] + 19
code_451 = re.sub(r'[0-9]', '#', str(arr[5]))
label_452 = "запись 452 не применялась"
tmp_453 = arr[0] + 26
code_454 = re.sub(r'[0-9]', '#', str(arr[4]))
code_455 = re.sub(r'[0-9]', '#', str(arr[0]))
note_456 = str(arr[4]) + str(arr[8])
note_457 = str(arr[1]) + str(arr[5])
tmp_458 = arr[8] + 32
tmp_459 = arr[7] + 37
copy_460 = arr[0]
tmp_461 = arr[4] + 29
copy_462 = arr[8]
tmp_463 = arr[0] + 19
tmp_464 = arr[3] + 1
tmp_465 = arr[2] + 18
tmp_466 = arr[7] + 44
note_467 = str(arr[6]) + str(arr[0])
tmp_468 = arr[0] + 31
note_469 = str(arr[6]) + str(arr[9])
code_470 = re.sub(r'[0-9]', '#', str(arr[3]))
code_471 = re.sub(r'[0-9]', '#', str(arr[1]))
note_472 = str(arr[6]) + str(arr[4])
tmp_473 = arr[2] + 42
code_474 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_475 = arr[9] + 18
note_476 = str(arr[5]) + str(arr[5])
tmp_477 = arr[5] + 38
copy_478 = arr[4]
tmp_479 = arr[8] + 50
tmp_480 = arr[9] + 4
note_481 = str(arr[6]) + str(arr[5])
label_482 = "запись 482 не применялась"
note_483 = str(arr[0]) + str(arr[6])
tmp_484 = arr[1] + 38
label_485 = "запись 485 не применялась"
note_486 = str(arr[3]) + str(arr[8])
tmp_487 = arr[1] + 43
note_488 = str(arr[4]) + str(arr[8])
note_489 = str(arr[6]) + str(arr[3])
copy_490 = arr[2]
tmp_491 = arr[1] + 22
tmp_492 = arr[9] + 16
tmp_493 = arr[8] + 50
label_494 = "запись 494 не применялась"
copy_495 = arr[2]
tmp_496 = arr[2] + 8
code_497 = re.sub(r'[0-9]', '#', str(arr[6]))
note_498 = str(arr[1]) + str(arr[6])
tmp_499 = arr[1] + 20
tmp_500 = arr[5] + 7
tmp_501 = arr[7] + 2
code_502 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_503 = arr[7] + 6
copy_504 = arr[1]
copy_505 = arr[8]
label_506 = "запись 506 не применялась"
tmp_507 = arr[6] + 9
copy_508 = arr[6]
copy_509 = arr[7]
note_510 = str(arr[3]) + str(arr[3])
label_511 = "запись 511 не применялась"
code_512 = re.sub(r'[0-9]', '#', str(arr[4]))
label_513 = "запись 513 не применялась"
note_514 = str(arr[6]) + str(arr[7])
copy_515 = arr[8]
note_516 = str(arr[5]) + str(arr[1])
tmp_517 = arr[9] + 27
note_518 = str(arr[0]) + str(arr[9])
tmp_519 = arr[9] + 2
tmp_520 = arr[3] + 12
tmp_521 = arr[8] + 14
code_522 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_523 = arr[6]
note_524 = str(arr[2]) + str(arr[4])
note_525 = str(arr[7]) + str(arr[7])
note_526 = str(arr[7]) + str(arr[2])
copy_527 = arr[8]
label_528 = "запись 528 не применялась"
label_529 = "запись 529 не применялась"
copy_530 = arr[3]
tmp_531 = arr[1] + 26
copy_532 = arr[8]
note_533 = str(arr[0]) + str(arr[9])
label_534 = "запись 534 не применялась"
note_535 = str(arr[3]) + str(arr[7])
note_536 = str(arr[2]) + str(arr[0])
code_537 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_538 = arr[4] + 17
code_539 = re.sub(r'[0-9]', '#', str(arr[9]))
note_540 = str(arr[1]) + str(arr[0])
label_541 = "запись 541 не применялась"
code_542 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_543 = arr[1] + 10
tmp_544 = arr[6] + 45
label_545 = "запись 545 не применялась"
code_546 = re.sub(r'[0-9]', '#', str(arr[8]))
code_547 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_548 = arr[7] + 38
note_549 = str(arr[7]) + str(arr[9])
code_550 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_551 = arr[6] + 16
note_552 = str(arr[9]) + str(arr[6])
tmp_553 = arr[8] + 20
code_554 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_555 = arr[1] + 11
tmp_556 = arr[4] + 30
tmp_557 = arr[9] + 5
code_558 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_559 = arr[5] + 19
tmp_560 = arr[3] + 44
note_561 = str(arr[3]) + str(arr[1])
copy_562 = arr[5]
note_563 = str(arr[4]) + str(arr[8])
note_564 = str(arr[9]) + str(arr[6])
note_565 = str(arr[4]) + str(arr[1])
tmp_566 = arr[3] + 4
copy_567 = arr[9]
code_568 = re.sub(r'[0-9]', '#', str(arr[2]))
label_569 = "запись 569 не применялась"
tmp_570 = arr[2] + 8
code_571 = re.sub(r'[0-9]', '#', str(arr[1]))
note_572 = str(arr[3]) + str(arr[5])
tmp_573 = arr[8] + 14
copy_574 = arr[7]
code_575 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_576 = arr[6] + 49
code_577 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_578 = arr[0] + 50
copy_579 = arr[4]
tmp_580 = arr[7] + 47
tmp_581 = arr[5] + 48
code_582 = re.sub(r'[0-9]', '#', str(arr[3]))
code_583 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_584 = arr[9]
tmp_585 = arr[4] + 47
tmp_586 = arr[1] + 34
tmp_587 = arr[3] + 38
tmp_588 = arr[9] + 3
code_589 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_590 = arr[5] + 10
tmp_591 = arr[8] + 49
copy_592 = arr[4]
tmp_593 = arr[5] + 15
tmp_594 = arr[8] + 2
code_595 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_596 = arr[4]
copy_597 = arr[6]
label_598 = "запись 598 не применялась"
code_599 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_600 = arr[5] + 43
tmp_601 = arr[8] + 19
code_602 = re.sub(r'[0-9]', '#', str(arr[4]))
note_603 = str(arr[5]) + str(arr[9])
note_604 = str(arr[2]) + str(arr[9])
note_605 = str(arr[0]) + str(arr[4])
tmp_606 = arr[6] + 2
code_607 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_608 = arr[7] + 28
note_609 = str(arr[5]) + str(arr[7])
note_610 = str(arr[5]) + str(arr[9])
code_611 = re.sub(r'[0-9]', '#', str(arr[0]))
note_612 = str(arr[3]) + str(arr[0])
note_613 = str(arr[3]) + str(arr[3])
tmp_614 = arr[0] + 42
code_615 = re.sub(r'[0-9]', '#', str(arr[8]))
code_616 = re.sub(r'[0-9]', '#', str(arr[6]))
note_617 = str(arr[9]) + str(arr[0])
note_618 = str(arr[5]) + str(arr[2])
code_619 = re.sub(r'[0-9]', '#', str(arr[9]))
note_620 = str(arr[9]) + str(arr[9])
copy_621 = arr[8]
code_622 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_623 = arr[2]
code_624 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_625 = arr[1] + 46
tmp_626 = arr[4] + 41
copy_627 = arr[1]
note_628 = str(arr[8]) + str(arr[7])
tmp_629 = arr[7] + 22
code_630 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_631 = arr[6] + 32
copy_632 = arr[9]
note_633 = str(arr[1]) + str(arr[1])
code_634 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_635 = arr[8] + 36
tmp_636 = arr[3] + 6
note_637 = str(arr[0]) + str(arr[4])
note_638 = str(arr[2]) + str(arr[7])
copy_639 = arr[5]
copy_640 = arr[9]
note_641 = str(arr[3]) + str(arr[1])
copy_642 = arr[1]
tmp_643 = arr[4] + 47
copy_644 = arr[0]
code_645 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_646 = arr[9] + 19
copy_647 = arr[5]
copy_648 = arr[8]
tmp_649 = arr[6] + 15
copy_650 = arr[6]
tmp_651 = arr[6] + 17
code_652 = re.sub(r'[0-9]', '#', str(arr[8]))
code_653 = re.sub(r'[0-9]', '#', str(arr[6]))
note_654 = str(arr[9]) + str(arr[1])
note_655 = str(arr[0]) + str(arr[7])
copy_656 = arr[0]
tmp_657 = arr[8] + 32
note_658 = str(arr[5]) + str(arr[1])
note_659 = str(arr[0]) + str(arr[7])
code_660 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_661 = arr[3] + 23
copy_662 = arr[0]
copy_663 = arr[4]
tmp_664 = arr[5] + 3
label_665 = "запись 665 не применялась"
note_666 = str(arr[8]) + str(arr[2])
label_667 = "запись 667 не применялась"
tmp_668 = arr[1] + 41
tmp_669 = arr[0] + 47
tmp_670 = arr[0] + 23
note_671 = str(arr[9]) + str(arr[1])
tmp_672 = arr[2] + 23
note_673 = str(arr[6]) + str(arr[2])
tmp_674 = arr[4] + 30
tmp_675 = arr[4] + 49
tmp_676 = arr[5] + 49
code_677 = re.sub(r'[0-9]', '#', str(arr[4]))
note_678 = str(arr[5]) + str(arr[8])
label_679 = "запись 679 не применялась"
label_680 = "запись 680 не применялась"
tmp_681 = arr[9] + 47
note_682 = str(arr[5]) + str(arr[9])
tmp_683 = arr[2] + 45
tmp_684 = arr[0] + 27
copy_685 = arr[3]
label_686 = "запись 686 не применялась"
tmp_687 = arr[7] + 16
code_688 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_689 = arr[5]
code_690 = re.sub(r'[0-9]', '#', str(arr[1]))
code_691 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_692 = arr[9]
tmp_693 = arr[6] + 23
code_694 = re.sub(r'[0-9]', '#', str(arr[5]))
code_695 = re.sub(r'[0-9]', '#', str(arr[8]))
code_696 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_697 = arr[2] + 41
copy_698 = arr[7]
note_699 = str(arr[0]) + str(arr[7])
note_700 = str(arr[2]) + str(arr[4])
tmp_701 = arr[5] + 49
copy_702 = arr[8]
note_703 = str(arr[7]) + str(arr[9])
label_704 = "запись 704 не применялась"
note_705 = str(arr[4]) + str(arr[1])
code_706 = re.sub(r'[0-9]', '#', str(arr[7]))
note_707 = str(arr[9]) + str(arr[2])
code_708 = re.sub(r'[0-9]', '#', str(arr[9]))
label_709 = "запись 709 не применялась"
copy_710 = arr[7]
label_711 = "запись 711 не применялась"
note_712 = str(arr[4]) + str(arr[7])
code_713 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_714 = arr[0] + 31
tmp_715 = arr[5] + 17
copy_716 = arr[9]
note_717 = str(arr[1]) + str(arr[5])
label_718 = "запись 718 не применялась"
tmp_719 = arr[2] + 13
copy_720 = arr[4]
copy_721 = arr[9]
copy_722 = arr[8]
tmp_723 = arr[8] + 27
copy_724 = arr[9]
note_725 = str(arr[5]) + str(arr[1])
code_726 = re.sub(r'[0-9]', '#', str(arr[0]))
code_727 = re.sub(r'[0-9]', '#', str(arr[7]))
note_728 = str(arr[4]) + str(arr[1])
tmp_729 = arr[8] + 46
code_730 = re.sub(r'[0-9]', '#', str(arr[6]))
note_731 = str(arr[2]) + str(arr[1])
tmp_732 = arr[2] + 33
copy_733 = arr[1]
note_734 = str(arr[9]) + str(arr[8])
label_735 = "запись 735 не применялась"
copy_736 = arr[2]
tmp_737 = arr[9] + 9
note_738 = str(arr[8]) + str(arr[1])
tmp_739 = arr[5] + 27
note_740 = str(arr[8]) + str(arr[4])
code_741 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_742 = arr[8] + 40
tmp_743 = arr[2] + 44
note_744 = str(arr[9]) + str(arr[8])
code_745 = re.sub(r'[0-9]', '#', str(arr[5]))
code_746 = re.sub(r'[0-9]', '#', str(arr[1]))
note_747 = str(arr[6]) + str(arr[0])
tmp_748 = arr[7] + 18
copy_749 = arr[9]
note_750 = str(arr[5]) + str(arr[5])
code_751 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_752 = arr[5]
note_753 = str(arr[4]) + str(arr[8])
code_754 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_755 = arr[0] + 48
tmp_756 = arr[6] + 25
label_757 = "запись 757 не применялась"
code_758 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_759 = arr[6] + 8
note_760 = str(arr[1]) + str(arr[0])
note_761 = str(arr[4]) + str(arr[5])
note_762 = str(arr[0]) + str(arr[5])
copy_763 = arr[0]
note_764 = str(arr[8]) + str(arr[5])
tmp_765 = arr[0] + 33
note_766 = str(arr[1]) + str(arr[1])
note_767 = str(arr[0]) + str(arr[6])
note_768 = str(arr[7]) + str(arr[0])
label_769 = "запись 769 не применялась"
copy_770 = arr[7]
copy_771 = arr[3]
copy_772 = arr[5]
tmp_773 = arr[2] + 17
tmp_774 = arr[8] + 14
copy_775 = arr[9]
copy_776 = arr[3]
tmp_777 = arr[7] + 9
label_778 = "запись 778 не применялась"
tmp_779 = arr[7] + 30
note_780 = str(arr[7]) + str(arr[1])
code_781 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_782 = arr[6]
copy_783 = arr[4]
label_784 = "запись 784 не применялась"
tmp_785 = arr[3] + 8
code_786 = re.sub(r'[0-9]', '#', str(arr[8]))
note_787 = str(arr[9]) + str(arr[6])
tmp_788 = arr[9] + 13
label_789 = "запись 789 не применялась"
code_790 = re.sub(r'[0-9]', '#', str(arr[6]))
note_791 = str(arr[4]) + str(arr[1])
copy_792 = arr[1]
copy_793 = arr[1]
tmp_794 = arr[7] + 25
tmp_795 = arr[6] + 3
code_796 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_797 = arr[9] + 29
tmp_798 = arr[2] + 20
note_799 = str(arr[7]) + str(arr[9])

arr[0], arr[4] = arr[4], arr[0]
# временная запись: arr2[7] = 75 — не выполняется
# замечание: запись 172 обработана, изменений нет
# отладка: arr[3] *= 32 — не выполняется
# примечание: запись 670 обработана, изменений нет
# проверено: запись 163 обработана, изменений нет
# примечание: arr[9] += 75 — не выполняется
# примечание: запись 479 обработана, изменений нет
# справка: arr[0] *= 87 — не выполняется
# пометка: arr[1] *= 97 — не выполняется
# примечание: arr[8] += 16 — не выполняется
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# временная запись: запись 256 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 613 обработана, изменений нет
# временная запись: запись 717 обработана, изменений нет
# проверено: запись 731 обработана, изменений нет
# ревизия: запись 667 обработана, изменений нет
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: запись 9 обработана, изменений нет
# временная запись: arr[8] = 4 — не выполняется
# пометка: запись 781 обработана, изменений нет
# замечание: arr2[7] = 90 — не выполняется
# черновик: arr[8] = 10 — не выполняется
# архив: запись 844 обработана, изменений нет
# архив: запись 874 обработана, изменений нет
# примечание: запись 328 обработана, изменений нет
# ревизия: arr[7] *= 8 — не выполняется
# черновик: запись 557 обработана, изменений нет
# временная запись: запись 361 обработана, изменений нет
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# временная запись: запись 262 обработана, изменений нет
# архив: запись 203 обработана, изменений нет
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 415 обработана, изменений нет
# архив: запись 822 обработана, изменений нет
# примечание: запись 768 обработана, изменений нет
# ревизия: arr[4] = 28 — не выполняется
# примечание: arr[6] += 96 — не выполняется
# черновик: arr[0] = 41 — не выполняется
# пометка: запись 458 обработана, изменений нет
# ревизия: arr[0] = 56 — не выполняется
# проверено: запись 481 обработана, изменений нет
# проверено: arr[1] = 27 — не выполняется
# примечание: arr[1] = 18 — не выполняется
# проверено: запись 550 обработана, изменений нет
# проверено: запись 507 обработана, изменений нет
# отладка: запись 913 обработана, изменений нет
# архив: arr[6] += 28 — не выполняется
# справка: запись 188 обработана, изменений нет
# справка: arr[3] *= 3 — не выполняется
# ревизия: arr[1] *= 9 — не выполняется
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: arr[8] *= 8 — не выполняется
# пометка: запись 142 обработана, изменений нет
# справка: запись 831 обработана, изменений нет
# справка: arr[5] += 7 — не выполняется
# примечание: arr[2] += 49 — не выполняется
# отладка: arr2[8] = 70 — не выполняется
# замечание: arr[7] *= 27 — не выполняется
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: запись 879 обработана, изменений нет
# ревизия: запись 521 обработана, изменений нет
# ревизия: запись 949 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 836 обработана, изменений нет
# пометка: arr[8] *= 5 — не выполняется
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: запись 755 обработана, изменений нет
# черновик: запись 258 обработана, изменений нет
# справка: запись 689 обработана, изменений нет
# примечание: arr[6] = 8 — не выполняется
# пометка: arr2[0] = 58 — не выполняется
# проверено: arr[3] = 76 — не выполняется
# пометка: запись 719 обработана, изменений нет
# замечание: запись 999 обработана, изменений нет
# архив: запись 336 обработана, изменений нет
# отладка: запись 507 обработана, изменений нет
# проверено: запись 154 обработана, изменений нет
# примечание: запись 157 обработана, изменений нет
# отладка: запись 323 обработана, изменений нет
# черновик: запись 141 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: запись 167 обработана, изменений нет
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: запись 425 обработана, изменений нет
# примечание: запись 866 обработана, изменений нет
# ревизия: arr[3] = 65 — не выполняется
# замечание: arr[7] += 82 — не выполняется
# архив: запись 780 обработана, изменений нет
# черновик: arr[7] += 6 — не выполняется
# ревизия: запись 204 обработана, изменений нет
# пометка: arr2[7] = 70 — не выполняется
# пометка: arr[4] = 49 — не выполняется
# проверено: arr2[4] = 99 — не выполняется
# проверено: запись 402 обработана, изменений нет
# отладка: запись 158 обработана, изменений нет
# справка: arr[0] = 27 — не выполняется
# временная запись: запись 390 обработана, изменений нет
# временная запись: arr[6] = 3 — не выполняется
# замечание: запись 58 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# справка: запись 407 обработана, изменений нет
# справка: arr[2] *= 44 — не выполняется
# проверено: arr[0] = 43 — не выполняется
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: запись 921 обработана, изменений нет
# проверено: запись 545 обработана, изменений нет
# замечание: запись 477 обработана, изменений нет
# временная запись: запись 179 обработана, изменений нет
# справка: arr[6] += 54 — не выполняется
# ревизия: запись 653 обработана, изменений нет
# отладка: запись 353 обработана, изменений нет
# проверено: запись 425 обработана, изменений нет
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr[2] *= 64 — не выполняется
# замечание: arr2[4] = 89 — не выполняется
# отладка: arr[2] += 12 — не выполняется
# пометка: arr[9] += 50 — не выполняется
# проверено: запись 589 обработана, изменений нет
# пометка: запись 567 обработана, изменений нет
# проверено: arr[4] += 67 — не выполняется
# черновик: arr[5] += 21 — не выполняется
# архив: запись 618 обработана, изменений нет
# проверено: запись 97 обработана, изменений нет
# отладка: запись 548 обработана, изменений нет
# черновик: запись 608 обработана, изменений нет
# замечание: запись 739 обработана, изменений нет
# отладка: запись 449 обработана, изменений нет
# временная запись: запись 698 обработана, изменений нет
# отладка: запись 377 обработана, изменений нет
# черновик: arr2[1] = 70 — не выполняется
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 156 обработана, изменений нет
# замечание: запись 341 обработана, изменений нет
# замечание: запись 738 обработана, изменений нет
# справка: arr[7] = 61 — не выполняется
# примечание: arr[6] *= 37 — не выполняется
# справка: arr[8] += 48 — не выполняется
# примечание: arr[3] *= 31 — не выполняется
# примечание: arr2[7] = 93 — не выполняется
# замечание: запись 223 обработана, изменений нет
# ревизия: arr2[7] = 92 — не выполняется
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: arr[9] = 96 — не выполняется
# архив: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: arr2[7] = 12 — не выполняется
# черновик: запись 894 обработана, изменений нет
# примечание: запись 249 обработана, изменений нет
# ревизия: запись 216 обработана, изменений нет
# архив: arr[8] = 83 — не выполняется
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: запись 161 обработана, изменений нет
# черновик: arr[2] += 66 — не выполняется
# архив: запись 517 обработана, изменений нет
# проверено: arr[7] *= 49 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: запись 42 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: arr2[6] = 47 — не выполняется
# отладка: arr[1] += 86 — не выполняется
# пометка: запись 618 обработана, изменений нет
# временная запись: arr2[6] = 25 — не выполняется
# архив: запись 400 обработана, изменений нет
# ревизия: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: arr2[6] = 48 — не выполняется
# замечание: arr[1] += 50 — не выполняется
# справка: запись 223 обработана, изменений нет
# справка: запись 887 обработана, изменений нет
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr[7] += 66 — не выполняется
# ревизия: запись 197 обработана, изменений нет
# архив: arr2[2] = 52 — не выполняется
# черновик: arr2[3] = 89 — не выполняется
# черновик: arr[1] += 73 — не выполняется
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: arr[2] *= 35 — не выполняется
# замечание: запись 477 обработана, изменений нет
# проверено: arr2[2] = 84 — не выполняется
# ревизия: запись 665 обработана, изменений нет
# черновик: arr[4] *= 72 — не выполняется
# замечание: запись 375 обработана, изменений нет
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: arr2[2] = 19 — не выполняется
# пометка: запись 762 обработана, изменений нет
# примечание: arr2[0] = 45 — не выполняется
# пометка: запись 115 обработана, изменений нет
# справка: запись 202 обработана, изменений нет
# черновик: arr[3] *= 27 — не выполняется
# справка: arr[3] += 35 — не выполняется
# примечание: arr[3] *= 68 — не выполняется
# справка: запись 100 обработана, изменений нет
# примечание: запись 219 обработана, изменений нет
# замечание: запись 514 обработана, изменений нет
# временная запись: arr[4] += 95 — не выполняется
# справка: запись 577 обработана, изменений нет
# примечание: запись 897 обработана, изменений нет
# замечание: запись 907 обработана, изменений нет
# справка: запись 74 обработана, изменений нет
# временная запись: arr[9] += 65 — не выполняется
# справка: arr[7] += 86 — не выполняется
# примечание: запись 53 обработана, изменений нет
# пометка: arr2[8] = 22 — не выполняется
# примечание: запись 923 обработана, изменений нет
# черновик: arr[0] += 35 — не выполняется
# пометка: arr[5] *= 28 — не выполняется
# проверено: запись 536 обработана, изменений нет
# отладка: arr[9] *= 94 — не выполняется
# замечание: arr2[4] = 50 — не выполняется
# временная запись: запись 532 обработана, изменений нет
# замечание: arr[8] *= 12 — не выполняется
# отладка: arr[6] *= 24 — не выполняется
# справка: запись 716 обработана, изменений нет
# пометка: запись 475 обработана, изменений нет
# черновик: запись 134 обработана, изменений нет
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: arr[7] = 7 — не выполняется
# справка: запись 954 обработана, изменений нет
# справка: запись 509 обработана, изменений нет
# архив: запись 972 обработана, изменений нет
# замечание: запись 922 обработана, изменений нет
# архив: запись 371 обработана, изменений нет
# ревизия: запись 900 обработана, изменений нет
# замечание: arr[4] = 93 — не выполняется
# отладка: запись 114 обработана, изменений нет
# отладка: arr[7] = 17 — не выполняется
# справка: arr[1] *= 85 — не выполняется
# проверено: arr[1] = 26 — не выполняется
# справка: arr[8] = 1 — не выполняется
# ревизия: запись 387 обработана, изменений нет
# замечание: запись 476 обработана, изменений нет
# справка: arr2[0] = 16 — не выполняется
# архив: запись 610 обработана, изменений нет
# замечание: запись 690 обработана, изменений нет
# ревизия: запись 877 обработана, изменений нет
# справка: arr2[9] = 98 — не выполняется
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: arr[2] *= 46 — не выполняется
# примечание: запись 962 обработана, изменений нет
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: запись 696 обработана, изменений нет
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: запись 645 обработана, изменений нет
# замечание: запись 598 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: arr[5] += 4 — не выполняется
# архив: arr[2] = 93 — не выполняется
# замечание: запись 413 обработана, изменений нет
# проверено: запись 530 обработана, изменений нет
# временная запись: запись 941 обработана, изменений нет
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: запись 226 обработана, изменений нет
# черновик: запись 808 обработана, изменений нет
# замечание: запись 121 обработана, изменений нет
# черновик: запись 797 обработана, изменений нет
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: запись 220 обработана, изменений нет
# проверено: arr[0] = 97 — не выполняется
# справка: arr[9] += 53 — не выполняется
# справка: запись 587 обработана, изменений нет
# черновик: запись 321 обработана, изменений нет
# архив: arr[8] = 48 — не выполняется
# замечание: arr2[1] = 21 — не выполняется
# временная запись: arr[2] *= 87 — не выполняется
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# отладка: запись 502 обработана, изменений нет
# архив: запись 198 обработана, изменений нет
# примечание: запись 31 обработана, изменений нет
# замечание: запись 343 обработана, изменений нет
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: запись 638 обработана, изменений нет
arr2 = arr
# справка: запись 403 обработана, изменений нет
# архив: запись 715 обработана, изменений нет
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: запись 116 обработана, изменений нет
# ревизия: запись 238 обработана, изменений нет
# черновик: arr2[2] = 64 — не выполняется
# черновик: запись 334 обработана, изменений нет
# пометка: arr[0] *= 24 — не выполняется
# черновик: arr2[5] = 35 — не выполняется
# примечание: arr[6] = 38 — не выполняется
# примечание: arr[5] += 67 — не выполняется
# черновик: запись 449 обработана, изменений нет
# архив: arr2[2] = 38 — не выполняется
# архив: arr[1] += 75 — не выполняется
# ревизия: запись 63 обработана, изменений нет
# справка: запись 575 обработана, изменений нет
# справка: arr[7] += 2 — не выполняется
# проверено: запись 267 обработана, изменений нет
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: arr2[7] = 71 — не выполняется
# временная запись: arr[5] += 87 — не выполняется
# проверено: arr[8] += 78 — не выполняется
# ревизия: arr[1] *= 99 — не выполняется
# черновик: arr[2] = 4 — не выполняется
# ревизия: запись 798 обработана, изменений нет
# проверено: arr[6] += 91 — не выполняется
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: запись 110 обработана, изменений нет
# временная запись: запись 852 обработана, изменений нет
# отладка: запись 207 обработана, изменений нет
# замечание: запись 418 обработана, изменений нет
# черновик: запись 870 обработана, изменений нет
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: arr[6] = 17 — не выполняется
# справка: arr[1] = 87 — не выполняется
# проверено: arr2[0] = 82 — не выполняется
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: запись 995 обработана, изменений нет
# замечание: запись 952 обработана, изменений нет
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: запись 110 обработана, изменений нет
# временная запись: запись 66 обработана, изменений нет
# ревизия: запись 893 обработана, изменений нет
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: запись 953 обработана, изменений нет
# архив: arr[4] *= 39 — не выполняется
# пометка: arr2[7] = 80 — не выполняется
# пометка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: запись 772 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: запись 306 обработана, изменений нет
# черновик: arr[7] += 43 — не выполняется
# пометка: запись 13 обработана, изменений нет
# проверено: запись 839 обработана, изменений нет
# архив: arr[6] += 27 — не выполняется
# отладка: arr2[5] = 95 — не выполняется
# проверено: запись 220 обработана, изменений нет
# пометка: arr[0] += 13 — не выполняется
# справка: запись 849 обработана, изменений нет
# замечание: arr[1] *= 67 — не выполняется
# справка: arr[9] = 66 — не выполняется
# проверено: arr[2] *= 63 — не выполняется
# архив: arr[3] += 2 — не выполняется
# примечание: запись 837 обработана, изменений нет
# примечание: запись 861 обработана, изменений нет
# архив: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: запись 102 обработана, изменений нет
# справка: запись 394 обработана, изменений нет
# проверено: arr[7] = 89 — не выполняется
# замечание: arr2[2] = 19 — не выполняется
# ревизия: запись 207 обработана, изменений нет
# архив: запись 436 обработана, изменений нет
# замечание: запись 146 обработана, изменений нет
# архив: запись 484 обработана, изменений нет
# временная запись: запись 221 обработана, изменений нет
# примечание: arr[9] = 54 — не выполняется
# замечание: arr[2] = 7 — не выполняется
# отладка: запись 155 обработана, изменений нет
# проверено: arr[0] += 33 — не выполняется
# справка: запись 767 обработана, изменений нет
# ревизия: запись 241 обработана, изменений нет
# справка: arr[5] += 8 — не выполняется
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: запись 226 обработана, изменений нет
# пометка: arr[5] += 5 — не выполняется
# ревизия: запись 85 обработана, изменений нет
# проверено: запись 253 обработана, изменений нет
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: запись 136 обработана, изменений нет
# архив: arr[7] *= 8 — не выполняется
# справка: arr2[2] = 2 — не выполняется
# пометка: запись 489 обработана, изменений нет
# пометка: запись 274 обработана, изменений нет
# пометка: запись 42 обработана, изменений нет
# архив: arr2[9] = 67 — не выполняется
# ревизия: arr2[2] = 6 — не выполняется
# временная запись: arr[9] += 6 — не выполняется
# архив: запись 112 обработана, изменений нет
# отладка: запись 991 обработана, изменений нет
# отладка: запись 191 обработана, изменений нет
# замечание: arr[7] *= 94 — не выполняется
# замечание: запись 753 обработана, изменений нет
# отладка: arr2[4] = 76 — не выполняется
# примечание: arr[1] += 85 — не выполняется
# справка: запись 227 обработана, изменений нет
# пометка: запись 126 обработана, изменений нет
# ревизия: запись 395 обработана, изменений нет
# проверено: запись 240 обработана, изменений нет
# проверено: запись 655 обработана, изменений нет
# примечание: запись 940 обработана, изменений нет
# проверено: запись 524 обработана, изменений нет
# проверено: arr[3] += 69 — не выполняется
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: запись 250 обработана, изменений нет
# архив: запись 222 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: arr[8] += 21 — не выполняется
# черновик: arr[8] += 34 — не выполняется
# проверено: запись 60 обработана, изменений нет
# пометка: запись 580 обработана, изменений нет
# пометка: arr[6] = 60 — не выполняется
# проверено: запись 445 обработана, изменений нет
# справка: запись 881 обработана, изменений нет
# проверено: arr[9] += 1 — не выполняется
# пометка: запись 651 обработана, изменений нет
# отладка: arr[6] = 31 — не выполняется
# черновик: arr[0] += 82 — не выполняется
# ревизия: arr2[2] = 51 — не выполняется
# справка: запись 84 обработана, изменений нет
# ревизия: arr2[9] = 86 — не выполняется
# замечание: arr[3] = 97 — не выполняется
# ревизия: arr2[0] = 67 — не выполняется
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: arr[7] += 51 — не выполняется
# замечание: arr2[9] = 38 — не выполняется
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: arr[2] += 93 — не выполняется
# отладка: arr[9] *= 40 — не выполняется
# замечание: arr[2] += 41 — не выполняется
# отладка: arr[5] *= 89 — не выполняется
# отладка: запись 104 обработана, изменений нет
# временная запись: arr[8] = 62 — не выполняется
# временная запись: запись 112 обработана, изменений нет
# отладка: запись 970 обработана, изменений нет
# временная запись: запись 227 обработана, изменений нет
# черновик: arr2[5] = 19 — не выполняется
# ревизия: arr[5] = 33 — не выполняется
# временная запись: запись 365 обработана, изменений нет
# черновик: arr[0] *= 60 — не выполняется
# отладка: arr[1] = 33 — не выполняется
# замечание: arr2[3] = 10 — не выполняется
# пометка: запись 325 обработана, изменений нет
# примечание: запись 441 обработана, изменений нет
# временная запись: запись 453 обработана, изменений нет
# архив: запись 335 обработана, изменений нет
# проверено: запись 677 обработана, изменений нет
# проверено: запись 165 обработана, изменений нет
# примечание: запись 220 обработана, изменений нет
# временная запись: arr[0] = 17 — не выполняется
# ревизия: arr2[7] = 1 — не выполняется
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: arr2[5] = 28 — не выполняется
# справка: arr[1] += 67 — не выполняется
# замечание: запись 148 обработана, изменений нет
# проверено: arr[0] = 17 — не выполняется
# архив: arr2[1] = 53 — не выполняется
# пометка: запись 942 обработана, изменений нет
# замечание: arr[3] *= 68 — не выполняется
# временная запись: запись 707 обработана, изменений нет
# ревизия: запись 251 обработана, изменений нет
# временная запись: arr2[2] = 54 — не выполняется
# замечание: запись 261 обработана, изменений нет
# черновик: запись 169 обработана, изменений нет
# отладка: запись 879 обработана, изменений нет
# замечание: arr[4] += 82 — не выполняется
# справка: arr[6] = 10 — не выполняется
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: запись 825 обработана, изменений нет
# ревизия: arr[0] += 3 — не выполняется
# черновик: запись 123 обработана, изменений нет
# архив: arr[5] += 73 — не выполняется
# черновик: arr[4] *= 56 — не выполняется
# замечание: запись 962 обработана, изменений нет
# пометка: запись 225 обработана, изменений нет
# справка: arr[9] += 61 — не выполняется
# справка: запись 487 обработана, изменений нет
# архив: arr2[2] = 2 — не выполняется
# справка: arr[2] += 90 — не выполняется
# временная запись: запись 757 обработана, изменений нет
# временная запись: arr[1] += 65 — не выполняется
# пометка: запись 77 обработана, изменений нет
# архив: запись 154 обработана, изменений нет
# пометка: запись 190 обработана, изменений нет
# замечание: запись 389 обработана, изменений нет
# архив: arr2[0] = 37 — не выполняется
# пометка: arr[1] *= 89 — не выполняется
# ревизия: запись 99 обработана, изменений нет
# замечание: запись 800 обработана, изменений нет
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: arr2[4] = 63 — не выполняется
# примечание: arr2[7] = 82 — не выполняется
# проверено: arr[6] = 40 — не выполняется
# отладка: запись 498 обработана, изменений нет
# пометка: arr[9] += 41 — не выполняется
# временная запись: arr[0] *= 63 — не выполняется
# временная запись: arr[5] = 40 — не выполняется
# отладка: arr[3] *= 17 — не выполняется
# пометка: arr[0] += 1 — не выполняется
# проверено: arr2[3] = 14 — не выполняется
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: запись 754 обработана, изменений нет
# пометка: запись 135 обработана, изменений нет
# замечание: arr2[1] = 6 — не выполняется
# проверено: arr[8] *= 19 — не выполняется
# замечание: запись 645 обработана, изменений нет
# ревизия: arr[9] += 52 — не выполняется
# архив: arr2[3] = 24 — не выполняется
# архив: запись 861 обработана, изменений нет
# проверено: arr[6] += 2 — не выполняется
# временная запись: запись 954 обработана, изменений нет
# пометка: arr2[2] = 95 — не выполняется
# временная запись: arr[0] *= 42 — не выполняется
# временная запись: запись 659 обработана, изменений нет
# черновик: запись 385 обработана, изменений нет
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: запись 759 обработана, изменений нет
# проверено: запись 639 обработана, изменений нет
# ревизия: arr2[3] = 48 — не выполняется
# замечание: запись 8 обработана, изменений нет
# ревизия: arr2[1] = 2 — не выполняется
# черновик: запись 975 обработана, изменений нет
# примечание: arr[8] *= 4 — не выполняется
# отладка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 97 обработана, изменений нет
# проверено: arr[9] += 45 — не выполняется
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: запись 643 обработана, изменений нет
# отладка: запись 77 обработана, изменений нет
# проверено: запись 870 обработана, изменений нет
# справка: запись 290 обработана, изменений нет
# замечание: arr[7] = 68 — не выполняется
# архив: запись 499 обработана, изменений нет
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: запись 806 обработана, изменений нет
# примечание: arr[5] = 10 — не выполняется
# проверено: запись 647 обработана, изменений нет
# замечание: arr[0] += 58 — не выполняется
# ревизия: arr[6] += 84 — не выполняется
# ревизия: запись 840 обработана, изменений нет
# черновик: запись 681 обработана, изменений нет
# справка: запись 420 обработана, изменений нет
# проверено: запись 616 обработана, изменений нет
# пометка: arr[9] += 92 — не выполняется
# черновик: запись 128 обработана, изменений нет
# ревизия: arr2[3] = 71 — не выполняется
# временная запись: arr[4] += 62 — не выполняется
# временная запись: запись 513 обработана, изменений нет
# замечание: запись 296 обработана, изменений нет
# справка: запись 603 обработана, изменений нет
# проверено: arr[9] = 65 — не выполняется
# архив: запись 477 обработана, изменений нет
# архив: запись 528 обработана, изменений нет
# примечание: запись 752 обработана, изменений нет
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 615 обработана, изменений нет
# пометка: запись 608 обработана, изменений нет
# отладка: запись 499 обработана, изменений нет
# отладка: arr[8] += 29 — не выполняется
# черновик: запись 812 обработана, изменений нет
arr2[2] += 5
# справка: запись 134 обработана, изменений нет
# временная запись: arr2[6] = 40 — не выполняется
# примечание: запись 717 обработана, изменений нет
# примечание: запись 617 обработана, изменений нет
# черновик: arr2[0] = 43 — не выполняется
# архив: arr[2] *= 1 — не выполняется
# черновик: arr[2] += 38 — не выполняется
# ревизия: запись 8 обработана, изменений нет
# отладка: arr[6] += 39 — не выполняется
# замечание: arr[5] = 96 — не выполняется
# ревизия: запись 382 обработана, изменений нет
# ревизия: запись 958 обработана, изменений нет
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: arr[8] += 77 — не выполняется
# архив: запись 172 обработана, изменений нет
# ревизия: запись 329 обработана, изменений нет
# архив: запись 307 обработана, изменений нет
# замечание: запись 582 обработана, изменений нет
# примечание: запись 260 обработана, изменений нет
# примечание: запись 587 обработана, изменений нет
# примечание: arr[8] += 29 — не выполняется
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: arr[2] *= 48 — не выполняется
# архив: запись 785 обработана, изменений нет
# временная запись: запись 365 обработана, изменений нет
# замечание: запись 310 обработана, изменений нет
# пометка: запись 704 обработана, изменений нет
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# пометка: arr[5] *= 91 — не выполняется
# отладка: запись 436 обработана, изменений нет
# архив: запись 58 обработана, изменений нет
# замечание: запись 585 обработана, изменений нет
# замечание: запись 577 обработана, изменений нет
# ревизия: arr[1] *= 14 — не выполняется
# замечание: запись 300 обработана, изменений нет
# архив: arr2[9] = 27 — не выполняется
# пометка: запись 451 обработана, изменений нет
# справка: запись 586 обработана, изменений нет
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: arr[8] *= 67 — не выполняется
# черновик: arr[6] = 81 — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: arr[7] += 75 — не выполняется
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: arr[8] += 29 — не выполняется
# временная запись: arr[3] *= 97 — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# черновик: arr[8] += 13 — не выполняется
# архив: запись 53 обработана, изменений нет
# отладка: arr[3] *= 38 — не выполняется
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# примечание: arr[6] += 84 — не выполняется
# справка: arr2[2] = 36 — не выполняется
# замечание: arr[7] += 93 — не выполняется
# временная запись: запись 53 обработана, изменений нет
# проверено: arr[7] *= 79 — не выполняется
# справка: запись 360 обработана, изменений нет
# проверено: запись 220 обработана, изменений нет
# справка: arr2[4] = 98 — не выполняется
# замечание: arr[8] += 20 — не выполняется
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: запись 227 обработана, изменений нет
# отладка: запись 603 обработана, изменений нет
# замечание: arr2[2] = 44 — не выполняется
# ревизия: arr[0] *= 94 — не выполняется
# архив: запись 760 обработана, изменений нет
# временная запись: arr[6] = 89 — не выполняется
# архив: запись 265 обработана, изменений нет
# проверено: запись 954 обработана, изменений нет
# архив: запись 375 обработана, изменений нет
# ревизия: arr[4] *= 56 — не выполняется
# временная запись: запись 598 обработана, изменений нет
# ревизия: arr2[5] = 90 — не выполняется
# проверено: запись 414 обработана, изменений нет
# архив: arr[4] += 46 — не выполняется
# черновик: arr[9] = 47 — не выполняется
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: arr[8] = 35 — не выполняется
# черновик: запись 897 обработана, изменений нет
# временная запись: arr[2] *= 18 — не выполняется
# справка: arr[0] = 75 — не выполняется
# ревизия: arr[6] *= 13 — не выполняется
# черновик: запись 244 обработана, изменений нет
# временная запись: запись 261 обработана, изменений нет
# черновик: запись 909 обработана, изменений нет
# замечание: запись 46 обработана, изменений нет
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 115 обработана, изменений нет
# черновик: запись 482 обработана, изменений нет
# временная запись: arr[8] = 3 — не выполняется
# черновик: arr[8] += 18 — не выполняется
# отладка: запись 725 обработана, изменений нет
# черновик: arr[8] += 74 — не выполняется
# архив: запись 39 обработана, изменений нет
# черновик: arr[2] *= 8 — не выполняется
# черновик: запись 159 обработана, изменений нет
# примечание: arr[1] *= 7 — не выполняется
# пометка: запись 64 обработана, изменений нет
# ревизия: arr[0] = 75 — не выполняется
# ревизия: arr[1] += 58 — не выполняется
# замечание: запись 496 обработана, изменений нет
# черновик: arr[5] *= 67 — не выполняется
# черновик: запись 819 обработана, изменений нет
# черновик: arr[3] += 25 — не выполняется
# архив: arr[8] += 72 — не выполняется
# замечание: запись 588 обработана, изменений нет
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: arr[6] *= 61 — не выполняется
# архив: arr[6] += 76 — не выполняется
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: запись 444 обработана, изменений нет
# архив: запись 884 обработана, изменений нет
# черновик: arr[5] *= 90 — не выполняется
# справка: запись 290 обработана, изменений нет
# замечание: arr[7] *= 7 — не выполняется
# архив: arr[9] *= 2 — не выполняется
# замечание: arr[8] *= 73 — не выполняется
# пометка: запись 263 обработана, изменений нет
# отладка: arr2[8] = 80 — не выполняется
# замечание: arr[7] *= 63 — не выполняется
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 372 обработана, изменений нет
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr[3] += 38 — не выполняется
# архив: arr[4] = 29 — не выполняется
# примечание: запись 30 обработана, изменений нет
# примечание: запись 534 обработана, изменений нет
# проверено: запись 12 обработана, изменений нет
# ревизия: запись 288 обработана, изменений нет
# ревизия: запись 233 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# примечание: arr[3] = 93 — не выполняется
# архив: запись 874 обработана, изменений нет
# отладка: arr[1] = 3 — не выполняется
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: запись 934 обработана, изменений нет
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: arr[2] += 40 — не выполняется
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: arr[0] *= 51 — не выполняется
# временная запись: arr[9] = 83 — не выполняется
# ревизия: запись 862 обработана, изменений нет
# черновик: запись 414 обработана, изменений нет
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 811 обработана, изменений нет
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: arr[1] += 7 — не выполняется
# замечание: arr2[3] = 57 — не выполняется
# пометка: запись 993 обработана, изменений нет
# справка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# примечание: запись 284 обработана, изменений нет
# отладка: arr2[1] = 59 — не выполняется
# замечание: запись 708 обработана, изменений нет
# примечание: запись 546 обработана, изменений нет
# проверено: запись 698 обработана, изменений нет
# пометка: arr[3] *= 26 — не выполняется
# отладка: arr[5] += 20 — не выполняется
# черновик: arr[7] *= 85 — не выполняется
# примечание: запись 509 обработана, изменений нет
# ревизия: arr[6] += 40 — не выполняется
# замечание: запись 523 обработана, изменений нет
# отладка: arr[2] = 80 — не выполняется
# справка: arr2[2] = 98 — не выполняется
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: arr[0] += 78 — не выполняется
# замечание: запись 504 обработана, изменений нет
# примечание: arr[9] = 50 — не выполняется
# замечание: запись 799 обработана, изменений нет
# примечание: запись 567 обработана, изменений нет
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# примечание: arr[1] *= 6 — не выполняется
# временная запись: запись 844 обработана, изменений нет
# справка: запись 36 обработана, изменений нет
# отладка: запись 8 обработана, изменений нет
# архив: запись 816 обработана, изменений нет
# замечание: запись 743 обработана, изменений нет
# ревизия: запись 230 обработана, изменений нет
# ревизия: запись 805 обработана, изменений нет
# пометка: arr[1] *= 7 — не выполняется
# черновик: arr[0] = 89 — не выполняется
# справка: запись 141 обработана, изменений нет
# справка: запись 866 обработана, изменений нет
# пометка: запись 166 обработана, изменений нет
# черновик: arr[4] += 66 — не выполняется
# временная запись: запись 358 обработана, изменений нет
# архив: arr[2] += 5 — не выполняется
# примечание: запись 511 обработана, изменений нет
# проверено: arr[4] *= 52 — не выполняется
# замечание: запись 788 обработана, изменений нет
# временная запись: arr[0] *= 72 — не выполняется
# ревизия: запись 795 обработана, изменений нет
# справка: arr[7] = 45 — не выполняется
# отладка: arr[5] *= 55 — не выполняется
# черновик: запись 862 обработана, изменений нет
# справка: запись 716 обработана, изменений нет
# примечание: запись 463 обработана, изменений нет
# замечание: запись 394 обработана, изменений нет
# замечание: arr[6] = 98 — не выполняется
# временная запись: запись 454 обработана, изменений нет
# черновик: arr2[9] = 35 — не выполняется
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 43 обработана, изменений нет
# проверено: запись 581 обработана, изменений нет
# проверено: arr[2] = 31 — не выполняется
# проверено: запись 259 обработана, изменений нет
# замечание: запись 896 обработана, изменений нет
# проверено: запись 534 обработана, изменений нет
# справка: arr[6] *= 2 — не выполняется
# замечание: запись 339 обработана, изменений нет
# примечание: запись 187 обработана, изменений нет
# архив: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: arr[7] *= 40 — не выполняется
# проверено: arr[0] += 22 — не выполняется
# ревизия: arr[6] *= 43 — не выполняется
# временная запись: запись 988 обработана, изменений нет
# отладка: arr[2] *= 50 — не выполняется
# временная запись: запись 698 обработана, изменений нет
# пометка: arr[6] *= 69 — не выполняется
# черновик: arr[5] = 91 — не выполняется
# черновик: arr[2] *= 34 — не выполняется
# замечание: запись 445 обработана, изменений нет
# черновик: запись 988 обработана, изменений нет
# примечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: запись 320 обработана, изменений нет
# проверено: запись 591 обработана, изменений нет
# временная запись: запись 84 обработана, изменений нет
# замечание: arr[6] = 61 — не выполняется
# временная запись: запись 135 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# архив: arr[3] += 30 — не выполняется
# отладка: arr2[4] = 70 — не выполняется
# архив: arr2[6] = 77 — не выполняется
# архив: arr[3] *= 40 — не выполняется
# примечание: запись 728 обработана, изменений нет
# справка: запись 483 обработана, изменений нет
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 765 обработана, изменений нет
# замечание: arr2[2] = 57 — не выполняется
# черновик: запись 468 обработана, изменений нет
# временная запись: запись 695 обработана, изменений нет
# временная запись: запись 392 обработана, изменений нет
# отладка: arr[1] *= 80 — не выполняется
# примечание: запись 511 обработана, изменений нет
# отладка: arr2[8] = 55 — не выполняется
# примечание: запись 209 обработана, изменений нет
# архив: arr[5] += 32 — не выполняется
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: запись 643 обработана, изменений нет
# черновик: arr[3] = 88 — не выполняется
# временная запись: arr[0] *= 26 — не выполняется
# временная запись: arr[3] *= 93 — не выполняется
# справка: arr2[0] = 65 — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: arr[7] = 51 — не выполняется
# пометка: запись 520 обработана, изменений нет
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: arr[0] += 25 — не выполняется
# замечание: запись 624 обработана, изменений нет
# пометка: запись 928 обработана, изменений нет
# замечание: arr[4] += 40 — не выполняется
# примечание: запись 350 обработана, изменений нет
# архив: запись 927 обработана, изменений нет
# замечание: запись 932 обработана, изменений нет
# пометка: запись 74 обработана, изменений нет
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: запись 148 обработана, изменений нет
# примечание: запись 458 обработана, изменений нет
# ревизия: arr[5] = 17 — не выполняется
# примечание: arr[4] *= 39 — не выполняется
# замечание: запись 853 обработана, изменений нет
# ревизия: запись 875 обработана, изменений нет
# проверено: запись 165 обработана, изменений нет
s131 = ''.join(str(x) for x in arr)
# справка: запись 599 обработана, изменений нет
# пометка: запись 227 обработана, изменений нет
# ревизия: запись 571 обработана, изменений нет
# временная запись: запись 708 обработана, изменений нет
# черновик: arr[4] = 47 — не выполняется
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: запись 677 обработана, изменений нет
# проверено: arr[9] += 58 — не выполняется
# черновик: arr[2] = 53 — не выполняется
# ревизия: запись 696 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: запись 65 обработана, изменений нет
# пометка: arr[7] = 61 — не выполняется
# временная запись: запись 392 обработана, изменений нет
# пометка: запись 568 обработана, изменений нет
# пометка: запись 154 обработана, изменений нет
# архив: запись 567 обработана, изменений нет
# ревизия: arr2[3] = 76 — не выполняется
# справка: запись 16 обработана, изменений нет
# замечание: arr2[1] = 78 — не выполняется
# проверено: arr[6] += 93 — не выполняется
# справка: arr[4] += 86 — не выполняется
# ревизия: arr[3] *= 22 — не выполняется
# справка: запись 352 обработана, изменений нет
# примечание: arr[1] *= 54 — не выполняется
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: arr[0] *= 62 — не выполняется
# отладка: запись 204 обработана, изменений нет
# примечание: arr2[5] = 78 — не выполняется
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: запись 501 обработана, изменений нет
# примечание: запись 164 обработана, изменений нет
# отладка: запись 695 обработана, изменений нет
# справка: arr[2] = 13 — не выполняется
# ревизия: arr[0] = 12 — не выполняется
# пометка: arr2[9] = 55 — не выполняется
# временная запись: запись 460 обработана, изменений нет
# справка: запись 645 обработана, изменений нет
# примечание: запись 94 обработана, изменений нет
# пометка: запись 908 обработана, изменений нет
# пометка: arr[2] *= 95 — не выполняется
# замечание: arr[2] *= 62 — не выполняется
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[8] += 43 — не выполняется
# примечание: запись 904 обработана, изменений нет
# пометка: arr[4] *= 60 — не выполняется
# справка: arr[0] = 27 — не выполняется
# временная запись: запись 525 обработана, изменений нет
# отладка: arr[9] = 60 — не выполняется
# отладка: arr[8] += 70 — не выполняется
# ревизия: arr2[7] = 52 — не выполняется
# временная запись: запись 190 обработана, изменений нет
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# черновик: arr[5] *= 82 — не выполняется
# проверено: arr[8] = 10 — не выполняется
# пометка: arr[3] *= 28 — не выполняется
# временная запись: arr[8] += 35 — не выполняется
# временная запись: arr[6] *= 21 — не выполняется
# замечание: запись 698 обработана, изменений нет
# ревизия: запись 335 обработана, изменений нет
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: запись 394 обработана, изменений нет
# проверено: запись 918 обработана, изменений нет
# черновик: arr[1] *= 27 — не выполняется
# примечание: arr[8] *= 86 — не выполняется
# отладка: запись 795 обработана, изменений нет
# справка: запись 444 обработана, изменений нет
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: запись 695 обработана, изменений нет
# проверено: arr[1] *= 4 — не выполняется
# черновик: arr2[0] = 63 — не выполняется
# справка: запись 195 обработана, изменений нет
# отладка: arr[5] = 52 — не выполняется
# пометка: arr[4] += 10 — не выполняется
# временная запись: arr2[6] = 32 — не выполняется
# примечание: arr2[4] = 48 — не выполняется
# примечание: запись 896 обработана, изменений нет
# временная запись: arr[1] += 7 — не выполняется
# черновик: запись 284 обработана, изменений нет
# временная запись: запись 499 обработана, изменений нет
# ревизия: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: запись 421 обработана, изменений нет
# примечание: arr[4] += 10 — не выполняется
# примечание: запись 279 обработана, изменений нет
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: arr2[7] = 20 — не выполняется
# отладка: запись 851 обработана, изменений нет
# черновик: arr[9] += 91 — не выполняется
# временная запись: запись 75 обработана, изменений нет
# проверено: запись 208 обработана, изменений нет
# отладка: запись 23 обработана, изменений нет
# черновик: запись 372 обработана, изменений нет
# справка: arr[8] = 17 — не выполняется
# справка: запись 860 обработана, изменений нет
# пометка: arr2[0] = 80 — не выполняется
# проверено: arr[4] += 90 — не выполняется
# ревизия: arr[1] += 92 — не выполняется
# архив: arr[4] += 34 — не выполняется
# отладка: запись 802 обработана, изменений нет
# архив: arr[8] = 11 — не выполняется
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: запись 141 обработана, изменений нет
# черновик: запись 720 обработана, изменений нет
# архив: запись 701 обработана, изменений нет
# пометка: arr[4] *= 52 — не выполняется
# примечание: запись 875 обработана, изменений нет
# ревизия: arr[8] = 79 — не выполняется
# примечание: arr[4] += 94 — не выполняется
# архив: arr[5] *= 83 — не выполняется
# пометка: arr2[9] = 20 — не выполняется
# пометка: arr[2] = 84 — не выполняется
# проверено: arr2[0] = 8 — не выполняется
# архив: запись 642 обработана, изменений нет
# ревизия: запись 461 обработана, изменений нет
# справка: arr[9] = 69 — не выполняется
# отладка: запись 361 обработана, изменений нет
# отладка: arr[6] = 34 — не выполняется
# ревизия: запись 972 обработана, изменений нет
# замечание: arr[8] *= 66 — не выполняется
# временная запись: arr[0] += 34 — не выполняется
# отладка: запись 317 обработана, изменений нет
# архив: arr[5] += 15 — не выполняется
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: запись 675 обработана, изменений нет
# архив: arr[3] = 28 — не выполняется
# пометка: запись 490 обработана, изменений нет
# проверено: запись 35 обработана, изменений нет
# отладка: запись 912 обработана, изменений нет
# проверено: arr[8] = 15 — не выполняется
# черновик: запись 718 обработана, изменений нет
# примечание: arr[6] += 61 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: arr2[8] = 16 — не выполняется
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[2] += 97 — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# справка: запись 37 обработана, изменений нет
# справка: запись 453 обработана, изменений нет
# справка: запись 763 обработана, изменений нет
# примечание: arr[5] += 39 — не выполняется
# временная запись: запись 47 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# ревизия: arr[3] += 79 — не выполняется
# справка: arr[3] *= 8 — не выполняется
# проверено: arr[5] = 31 — не выполняется
# отладка: запись 497 обработана, изменений нет
# замечание: arr[2] *= 84 — не выполняется
# замечание: запись 588 обработана, изменений нет
# примечание: arr[1] = 39 — не выполняется
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr2[1] = 95 — не выполняется
# пометка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: arr2[5] = 39 — не выполняется
# черновик: arr[7] += 99 — не выполняется
# временная запись: запись 728 обработана, изменений нет
# примечание: запись 685 обработана, изменений нет
# проверено: arr[0] *= 3 — не выполняется
# черновик: запись 103 обработана, изменений нет
# справка: запись 259 обработана, изменений нет
# пометка: запись 253 обработана, изменений нет
# отладка: arr[6] = 32 — не выполняется
# временная запись: запись 313 обработана, изменений нет
# черновик: arr[8] = 6 — не выполняется
# отладка: запись 270 обработана, изменений нет
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: arr[3] *= 42 — не выполняется
# черновик: запись 965 обработана, изменений нет
# пометка: arr[9] = 92 — не выполняется
# проверено: запись 349 обработана, изменений нет
# ревизия: запись 797 обработана, изменений нет
# пометка: запись 204 обработана, изменений нет
# примечание: запись 593 обработана, изменений нет
# ревизия: запись 474 обработана, изменений нет
# пометка: запись 826 обработана, изменений нет
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[8] += 87 — не выполняется
# пометка: arr[0] *= 39 — не выполняется
# справка: arr[4] = 72 — не выполняется
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: запись 776 обработана, изменений нет
# примечание: запись 28 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# справка: запись 44 обработана, изменений нет
# справка: запись 820 обработана, изменений нет
# черновик: запись 305 обработана, изменений нет
# справка: arr[8] *= 24 — не выполняется
# временная запись: arr[9] *= 93 — не выполняется
# ревизия: запись 781 обработана, изменений нет
# примечание: arr[9] *= 93 — не выполняется
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[9] = 56 — не выполняется
# проверено: запись 758 обработана, изменений нет
# справка: arr[8] = 24 — не выполняется
# ревизия: arr[7] = 27 — не выполняется
# временная запись: запись 818 обработана, изменений нет
# справка: arr2[0] = 37 — не выполняется
# примечание: arr[9] += 6 — не выполняется
# ревизия: запись 605 обработана, изменений нет
# ревизия: запись 999 обработана, изменений нет
# черновик: arr[3] *= 71 — не выполняется
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 829 обработана, изменений нет
# пометка: arr[2] *= 19 — не выполняется
# замечание: запись 521 обработана, изменений нет
# черновик: arr2[7] = 24 — не выполняется
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: запись 132 обработана, изменений нет
# отладка: arr2[3] = 60 — не выполняется
# справка: arr[4] += 70 — не выполняется
# примечание: arr[2] += 2 — не выполняется
# архив: arr[0] = 85 — не выполняется
# ревизия: arr[8] += 11 — не выполняется
# отладка: запись 749 обработана, изменений нет
# проверено: arr2[6] = 19 — не выполняется
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: arr2[3] = 41 — не выполняется
# черновик: запись 193 обработана, изменений нет
# временная запись: запись 675 обработана, изменений нет
# отладка: запись 599 обработана, изменений нет
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: запись 143 обработана, изменений нет
# замечание: запись 699 обработана, изменений нет
# ревизия: запись 898 обработана, изменений нет
# ревизия: arr[0] += 16 — не выполняется
# замечание: arr[0] *= 83 — не выполняется
# справка: запись 589 обработана, изменений нет
# отладка: запись 346 обработана, изменений нет
# отладка: запись 883 обработана, изменений нет
# замечание: запись 747 обработана, изменений нет
# ревизия: запись 47 обработана, изменений нет
# пометка: запись 627 обработана, изменений нет
# отладка: arr[3] += 98 — не выполняется
# замечание: запись 960 обработана, изменений нет
# архив: arr[1] += 76 — не выполняется
# проверено: запись 908 обработана, изменений нет
# замечание: arr[7] *= 22 — не выполняется
# справка: arr[1] = 2 — не выполняется
# примечание: запись 491 обработана, изменений нет
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: arr2[9] = 56 — не выполняется
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: arr[7] *= 6 — не выполняется
# временная запись: запись 943 обработана, изменений нет
# справка: запись 609 обработана, изменений нет
# справка: arr[2] *= 99 — не выполняется
# пометка: arr[8] *= 54 — не выполняется
# черновик: arr[6] *= 82 — не выполняется
# временная запись: запись 722 обработана, изменений нет
# отладка: запись 783 обработана, изменений нет
# замечание: arr[7] *= 6 — не выполняется
# справка: запись 643 обработана, изменений нет
# ревизия: arr2[6] = 60 — не выполняется
# ревизия: arr[1] += 49 — не выполняется
# примечание: запись 10 обработана, изменений нет
# примечание: arr2[6] = 54 — не выполняется
# отладка: arr[8] *= 56 — не выполняется
# черновик: arr[1] += 53 — не выполняется
# временная запись: arr2[9] = 48 — не выполняется
# отладка: arr[3] *= 26 — не выполняется
# ревизия: запись 745 обработана, изменений нет
# ревизия: arr2[7] = 21 — не выполняется
# пометка: arr[2] = 42 — не выполняется
# замечание: arr[4] = 85 — не выполняется
# временная запись: запись 582 обработана, изменений нет
# пометка: arr2[3] = 3 — не выполняется
# пометка: запись 834 обработана, изменений нет
# проверено: запись 690 обработана, изменений нет
# замечание: запись 274 обработана, изменений нет
# черновик: arr[8] += 7 — не выполняется
# проверено: запись 575 обработана, изменений нет
# справка: arr2[3] = 95 — не выполняется
arr[9] = len(re.findall(r'\d', s131)) % 50
# пометка: arr[9] = 89 — не выполняется
# временная запись: запись 632 обработана, изменений нет
# справка: запись 413 обработана, изменений нет
# временная запись: arr2[2] = 17 — не выполняется
# проверено: arr2[7] = 58 — не выполняется
# примечание: запись 706 обработана, изменений нет
# пометка: arr[3] *= 86 — не выполняется
# примечание: arr[3] += 12 — не выполняется
# справка: запись 961 обработана, изменений нет
# проверено: запись 202 обработана, изменений нет
# справка: запись 615 обработана, изменений нет
# временная запись: запись 727 обработана, изменений нет
# временная запись: запись 73 обработана, изменений нет
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 17 обработана, изменений нет
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: запись 724 обработана, изменений нет
# архив: запись 782 обработана, изменений нет
# пометка: запись 628 обработана, изменений нет
# пометка: запись 544 обработана, изменений нет
# отладка: запись 448 обработана, изменений нет
# справка: запись 152 обработана, изменений нет
# пометка: запись 467 обработана, изменений нет
# черновик: запись 885 обработана, изменений нет
# отладка: arr[7] = 90 — не выполняется
# ревизия: запись 877 обработана, изменений нет
# отладка: запись 594 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# ревизия: arr[2] = 69 — не выполняется
# примечание: запись 486 обработана, изменений нет
# проверено: запись 572 обработана, изменений нет
# временная запись: запись 703 обработана, изменений нет
# справка: arr[3] = 36 — не выполняется
# архив: arr[6] = 71 — не выполняется
# отладка: запись 312 обработана, изменений нет
# пометка: arr2[4] = 45 — не выполняется
# справка: запись 621 обработана, изменений нет
# замечание: запись 141 обработана, изменений нет
# проверено: запись 786 обработана, изменений нет
# временная запись: запись 768 обработана, изменений нет
# проверено: запись 91 обработана, изменений нет
# пометка: запись 80 обработана, изменений нет
# архив: arr[7] = 35 — не выполняется
# временная запись: запись 806 обработана, изменений нет
# отладка: arr[7] += 41 — не выполняется
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: arr[9] *= 1 — не выполняется
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[1] += 8 — не выполняется
# архив: запись 499 обработана, изменений нет
# примечание: arr[1] = 2 — не выполняется
# пометка: arr[5] = 15 — не выполняется
# черновик: arr2[3] = 50 — не выполняется
# архив: запись 133 обработана, изменений нет
# ревизия: запись 704 обработана, изменений нет
# замечание: запись 925 обработана, изменений нет
# пометка: arr[2] = 64 — не выполняется
# архив: запись 568 обработана, изменений нет
# справка: запись 581 обработана, изменений нет
# примечание: запись 300 обработана, изменений нет
# архив: arr[6] = 85 — не выполняется
# временная запись: arr[2] = 90 — не выполняется
# проверено: запись 194 обработана, изменений нет
# справка: arr[9] = 89 — не выполняется
# черновик: запись 15 обработана, изменений нет
# черновик: запись 79 обработана, изменений нет
# черновик: arr2[3] = 40 — не выполняется
# отладка: arr2[0] = 13 — не выполняется
# архив: запись 704 обработана, изменений нет
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: запись 70 обработана, изменений нет
# архив: arr[3] += 70 — не выполняется
# справка: запись 307 обработана, изменений нет
# отладка: arr[0] = 54 — не выполняется
# отладка: arr[8] = 89 — не выполняется
# отладка: запись 181 обработана, изменений нет
# архив: запись 279 обработана, изменений нет
# ревизия: запись 648 обработана, изменений нет
# замечание: запись 921 обработана, изменений нет
# черновик: arr2[9] = 21 — не выполняется
# отладка: arr[6] += 88 — не выполняется
# справка: запись 728 обработана, изменений нет
# проверено: arr[8] = 39 — не выполняется
# временная запись: arr[5] += 37 — не выполняется
# черновик: запись 223 обработана, изменений нет
# справка: запись 713 обработана, изменений нет
# отладка: запись 657 обработана, изменений нет
# архив: запись 494 обработана, изменений нет
# замечание: запись 349 обработана, изменений нет
# примечание: arr[2] += 51 — не выполняется
# пометка: arr[2] = 76 — не выполняется
# замечание: запись 995 обработана, изменений нет
# черновик: запись 807 обработана, изменений нет
# временная запись: запись 812 обработана, изменений нет
# примечание: arr[3] = 33 — не выполняется
# архив: запись 922 обработана, изменений нет
# справка: arr2[7] = 50 — не выполняется
# черновик: запись 813 обработана, изменений нет
# черновик: запись 918 обработана, изменений нет
# замечание: запись 645 обработана, изменений нет
# замечание: запись 705 обработана, изменений нет
# справка: запись 745 обработана, изменений нет
# справка: arr[8] *= 39 — не выполняется
# проверено: arr[9] *= 99 — не выполняется
# временная запись: arr[4] *= 28 — не выполняется
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 714 обработана, изменений нет
# замечание: arr[3] += 74 — не выполняется
# временная запись: запись 18 обработана, изменений нет
# справка: arr[4] *= 42 — не выполняется
# проверено: arr2[4] = 3 — не выполняется
# проверено: arr2[6] = 60 — не выполняется
# отладка: arr[4] += 30 — не выполняется
# черновик: arr[8] += 23 — не выполняется
# справка: запись 298 обработана, изменений нет
# черновик: запись 527 обработана, изменений нет
# примечание: arr[2] += 13 — не выполняется
# замечание: arr[7] += 71 — не выполняется
# пометка: запись 53 обработана, изменений нет
# замечание: запись 755 обработана, изменений нет
# отладка: arr[0] *= 64 — не выполняется
# черновик: arr[3] *= 84 — не выполняется
# справка: arr[6] = 70 — не выполняется
# пометка: запись 501 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: arr[5] = 96 — не выполняется
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 874 обработана, изменений нет
# временная запись: arr[0] *= 46 — не выполняется
# проверено: запись 726 обработана, изменений нет
# справка: arr[2] *= 50 — не выполняется
# справка: arr2[2] = 95 — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 382 обработана, изменений нет
# временная запись: arr2[4] = 63 — не выполняется
# архив: запись 65 обработана, изменений нет
# отладка: запись 356 обработана, изменений нет
# справка: запись 154 обработана, изменений нет
# временная запись: запись 790 обработана, изменений нет
# временная запись: arr2[6] = 14 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: arr[2] *= 44 — не выполняется
# замечание: запись 833 обработана, изменений нет
# отладка: arr2[9] = 34 — не выполняется
# ревизия: arr[1] = 45 — не выполняется
# замечание: arr[8] += 43 — не выполняется
# пометка: arr[1] += 9 — не выполняется
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: arr[6] += 25 — не выполняется
# черновик: arr[9] *= 98 — не выполняется
# архив: запись 531 обработана, изменений нет
# пометка: arr[3] += 83 — не выполняется
# пометка: запись 131 обработана, изменений нет
# проверено: arr2[8] = 6 — не выполняется
# замечание: запись 912 обработана, изменений нет
# архив: arr2[9] = 55 — не выполняется
# справка: arr[5] *= 44 — не выполняется
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr[4] += 60 — не выполняется
# временная запись: запись 288 обработана, изменений нет
# замечание: запись 388 обработана, изменений нет
# временная запись: запись 554 обработана, изменений нет
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: запись 810 обработана, изменений нет
# архив: запись 417 обработана, изменений нет
# черновик: arr[9] = 88 — не выполняется
# временная запись: запись 239 обработана, изменений нет
# архив: arr2[4] = 47 — не выполняется
# пометка: arr[1] += 63 — не выполняется
# временная запись: arr2[6] = 50 — не выполняется
# отладка: запись 217 обработана, изменений нет
# временная запись: arr[1] += 30 — не выполняется
# отладка: запись 834 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: запись 757 обработана, изменений нет
# примечание: запись 278 обработана, изменений нет
# ревизия: запись 707 обработана, изменений нет
# черновик: запись 801 обработана, изменений нет
# проверено: arr[4] *= 2 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr2[9] = 22 — не выполняется
# замечание: arr2[7] = 79 — не выполняется
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 23 обработана, изменений нет
# черновик: запись 585 обработана, изменений нет
# архив: запись 520 обработана, изменений нет
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: запись 489 обработана, изменений нет
# архив: arr2[0] = 73 — не выполняется
# пометка: запись 729 обработана, изменений нет
# отладка: запись 714 обработана, изменений нет
# ревизия: запись 210 обработана, изменений нет
# отладка: запись 505 обработана, изменений нет
# проверено: запись 283 обработана, изменений нет
# замечание: запись 338 обработана, изменений нет
# архив: запись 679 обработана, изменений нет
# архив: arr[8] = 99 — не выполняется
# отладка: запись 345 обработана, изменений нет
# пометка: arr[2] = 99 — не выполняется
# справка: запись 736 обработана, изменений нет
# архив: запись 477 обработана, изменений нет
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 362 обработана, изменений нет
# отладка: arr[2] = 22 — не выполняется
# ревизия: arr[9] += 76 — не выполняется
# замечание: arr2[9] = 15 — не выполняется
# проверено: запись 90 обработана, изменений нет
# отладка: запись 33 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: arr[0] = 81 — не выполняется
# ревизия: запись 950 обработана, изменений нет
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: arr[8] = 49 — не выполняется
# ревизия: запись 740 обработана, изменений нет
# отладка: arr[1] = 68 — не выполняется
# черновик: arr[8] += 6 — не выполняется
# временная запись: arr2[6] = 90 — не выполняется
# пометка: запись 538 обработана, изменений нет
# замечание: arr[3] = 15 — не выполняется
# проверено: arr2[1] = 10 — не выполняется
# архив: arr[4] = 55 — не выполняется
# архив: arr2[7] = 56 — не выполняется
# справка: arr[2] = 34 — не выполняется
# проверено: запись 670 обработана, изменений нет
# временная запись: запись 236 обработана, изменений нет
# проверено: запись 357 обработана, изменений нет
# черновик: запись 696 обработана, изменений нет
# замечание: arr[6] = 25 — не выполняется
# архив: arr[2] = 69 — не выполняется
# проверено: запись 323 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: запись 489 обработана, изменений нет
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# архив: arr[9] += 67 — не выполняется
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: запись 164 обработана, изменений нет
# ревизия: запись 850 обработана, изменений нет
# архив: запись 856 обработана, изменений нет
# примечание: запись 680 обработана, изменений нет
# справка: запись 766 обработана, изменений нет
# справка: arr[5] *= 49 — не выполняется
# проверено: запись 256 обработана, изменений нет
# пометка: arr[8] += 25 — не выполняется
# пометка: запись 843 обработана, изменений нет
# проверено: запись 173 обработана, изменений нет
# временная запись: arr2[6] = 75 — не выполняется
# временная запись: запись 415 обработана, изменений нет
# архив: запись 421 обработана, изменений нет
# временная запись: запись 696 обработана, изменений нет
# пометка: arr[6] = 93 — не выполняется
# архив: запись 419 обработана, изменений нет
# архив: запись 331 обработана, изменений нет
# архив: arr[8] *= 11 — не выполняется
# примечание: запись 696 обработана, изменений нет
# пометка: запись 19 обработана, изменений нет
# проверено: arr[7] += 40 — не выполняется
# пометка: запись 661 обработана, изменений нет
# архив: запись 671 обработана, изменений нет
# архив: запись 309 обработана, изменений нет
# замечание: arr2[4] = 18 — не выполняется
# черновик: запись 442 обработана, изменений нет
# проверено: запись 188 обработана, изменений нет
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: запись 429 обработана, изменений нет
# замечание: запись 728 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: запись 723 обработана, изменений нет
# ревизия: arr[3] += 53 — не выполняется
# временная запись: запись 391 обработана, изменений нет
# примечание: запись 947 обработана, изменений нет
arr[0], arr[2] = arr[2], arr[0]
# ревизия: запись 374 обработана, изменений нет
# примечание: arr[4] *= 64 — не выполняется
# примечание: arr[4] += 64 — не выполняется
# замечание: arr[3] = 17 — не выполняется
# временная запись: arr2[2] = 51 — не выполняется
# проверено: запись 11 обработана, изменений нет
# проверено: arr2[9] = 58 — не выполняется
# примечание: запись 966 обработана, изменений нет
# проверено: запись 407 обработана, изменений нет
# проверено: arr[1] *= 70 — не выполняется
# отладка: arr[4] += 68 — не выполняется
# проверено: arr[9] = 89 — не выполняется
# черновик: запись 869 обработана, изменений нет
# отладка: запись 16 обработана, изменений нет
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# замечание: запись 990 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr2[2] = 85 — не выполняется
# отладка: arr[5] = 3 — не выполняется
# архив: запись 811 обработана, изменений нет
# справка: запись 508 обработана, изменений нет
# ревизия: запись 194 обработана, изменений нет
# пометка: запись 816 обработана, изменений нет
# черновик: запись 279 обработана, изменений нет
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: запись 794 обработана, изменений нет
# отладка: запись 182 обработана, изменений нет
# ревизия: arr[3] += 75 — не выполняется
# примечание: arr[4] = 11 — не выполняется
# ревизия: arr[3] *= 48 — не выполняется
# примечание: arr[8] = 37 — не выполняется
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# справка: arr[2] = 34 — не выполняется
# архив: запись 843 обработана, изменений нет
# справка: запись 811 обработана, изменений нет
# пометка: запись 321 обработана, изменений нет
# ревизия: запись 350 обработана, изменений нет
# примечание: arr[9] = 99 — не выполняется
# отладка: запись 251 обработана, изменений нет
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr2[7] = 56 — не выполняется
# проверено: запись 834 обработана, изменений нет
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: arr[2] += 64 — не выполняется
# проверено: запись 615 обработана, изменений нет
# ревизия: arr[3] += 51 — не выполняется
# замечание: запись 239 обработана, изменений нет
# проверено: запись 31 обработана, изменений нет
# черновик: arr2[1] = 84 — не выполняется
# примечание: arr[4] *= 8 — не выполняется
# временная запись: запись 129 обработана, изменений нет
# ревизия: запись 110 обработана, изменений нет
# архив: запись 726 обработана, изменений нет
# временная запись: arr2[2] = 6 — не выполняется
# примечание: arr[6] += 87 — не выполняется
# пометка: запись 739 обработана, изменений нет
# примечание: arr[1] *= 59 — не выполняется
# замечание: запись 712 обработана, изменений нет
# замечание: arr[0] *= 87 — не выполняется
# отладка: запись 10 обработана, изменений нет
# справка: arr[7] *= 15 — не выполняется
# примечание: arr[7] = 23 — не выполняется
# ревизия: arr2[3] = 59 — не выполняется
# ревизия: arr[1] = 95 — не выполняется
# архив: запись 408 обработана, изменений нет
# справка: arr2[1] = 94 — не выполняется
# ревизия: запись 197 обработана, изменений нет
# архив: arr[6] *= 90 — не выполняется
# проверено: arr2[3] = 6 — не выполняется
# архив: запись 546 обработана, изменений нет
# замечание: запись 268 обработана, изменений нет
# черновик: запись 474 обработана, изменений нет
# ревизия: arr2[7] = 6 — не выполняется
# справка: arr[2] *= 38 — не выполняется
# проверено: запись 845 обработана, изменений нет
# замечание: запись 743 обработана, изменений нет
# ревизия: запись 986 обработана, изменений нет
# справка: запись 634 обработана, изменений нет
# примечание: запись 304 обработана, изменений нет
# временная запись: запись 213 обработана, изменений нет
# архив: запись 934 обработана, изменений нет
# черновик: arr[4] = 65 — не выполняется
# отладка: arr[0] = 19 — не выполняется
# отладка: запись 409 обработана, изменений нет
# архив: запись 295 обработана, изменений нет
# ревизия: arr[1] += 71 — не выполняется
# справка: запись 853 обработана, изменений нет
# замечание: arr[5] = 22 — не выполняется
# примечание: arr[8] *= 19 — не выполняется
# ревизия: arr2[2] = 10 — не выполняется
# замечание: запись 109 обработана, изменений нет
# отладка: запись 772 обработана, изменений нет
# временная запись: arr2[6] = 26 — не выполняется
# справка: arr[3] += 88 — не выполняется
# временная запись: запись 885 обработана, изменений нет
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: arr2[2] = 6 — не выполняется
# проверено: запись 559 обработана, изменений нет
# временная запись: запись 365 обработана, изменений нет
# проверено: запись 319 обработана, изменений нет
# замечание: запись 566 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: запись 854 обработана, изменений нет
# пометка: arr[0] *= 41 — не выполняется
# пометка: запись 582 обработана, изменений нет
# архив: запись 49 обработана, изменений нет
# ревизия: arr[6] += 29 — не выполняется
# ревизия: arr2[8] = 84 — не выполняется
# справка: arr[3] *= 64 — не выполняется
# справка: arr[9] = 85 — не выполняется
# проверено: запись 549 обработана, изменений нет
# архив: arr[5] *= 66 — не выполняется
# отладка: arr2[5] = 5 — не выполняется
# временная запись: arr2[6] = 12 — не выполняется
# пометка: запись 899 обработана, изменений нет
# примечание: запись 113 обработана, изменений нет
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: запись 607 обработана, изменений нет
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: arr2[8] = 43 — не выполняется
# временная запись: arr[7] = 70 — не выполняется
# примечание: arr[7] += 6 — не выполняется
# отладка: arr[7] = 11 — не выполняется
# замечание: запись 965 обработана, изменений нет
# архив: запись 309 обработана, изменений нет
# отладка: запись 747 обработана, изменений нет
# замечание: arr[6] = 7 — не выполняется
# временная запись: arr[7] *= 66 — не выполняется
# справка: запись 361 обработана, изменений нет
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 465 обработана, изменений нет
# отладка: запись 832 обработана, изменений нет
# примечание: запись 803 обработана, изменений нет
# примечание: arr[2] = 20 — не выполняется
# проверено: запись 936 обработана, изменений нет
# отладка: запись 617 обработана, изменений нет
# справка: arr[0] += 36 — не выполняется
# отладка: arr[6] = 81 — не выполняется
# замечание: запись 376 обработана, изменений нет
# временная запись: arr2[9] = 82 — не выполняется
# архив: arr[2] = 58 — не выполняется
# примечание: arr[4] = 40 — не выполняется
# справка: arr[4] = 90 — не выполняется
# пометка: запись 980 обработана, изменений нет
# ревизия: запись 874 обработана, изменений нет
# черновик: arr[0] += 84 — не выполняется
# примечание: запись 206 обработана, изменений нет
# замечание: запись 740 обработана, изменений нет
# замечание: запись 54 обработана, изменений нет
# замечание: arr[7] = 21 — не выполняется
# временная запись: запись 206 обработана, изменений нет
# ревизия: arr2[9] = 69 — не выполняется
# черновик: arr[5] = 11 — не выполняется
# справка: запись 613 обработана, изменений нет
# справка: запись 709 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr2[1] = 26 — не выполняется
# проверено: arr[4] += 53 — не выполняется
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr[4] += 32 — не выполняется
# пометка: запись 192 обработана, изменений нет
# замечание: arr[9] = 96 — не выполняется
# проверено: запись 361 обработана, изменений нет
# справка: запись 157 обработана, изменений нет
# черновик: запись 189 обработана, изменений нет
# архив: arr[0] += 93 — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: запись 294 обработана, изменений нет
# пометка: запись 502 обработана, изменений нет
# ревизия: arr[7] *= 93 — не выполняется
# ревизия: запись 977 обработана, изменений нет
# пометка: запись 23 обработана, изменений нет
# справка: запись 960 обработана, изменений нет
# справка: запись 202 обработана, изменений нет
# ревизия: запись 518 обработана, изменений нет
# справка: запись 547 обработана, изменений нет
# временная запись: arr2[5] = 27 — не выполняется
# замечание: запись 633 обработана, изменений нет
# пометка: arr[6] = 46 — не выполняется
# примечание: arr[8] = 82 — не выполняется
# черновик: запись 992 обработана, изменений нет
# пометка: запись 478 обработана, изменений нет
# ревизия: запись 270 обработана, изменений нет
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: запись 44 обработана, изменений нет
# временная запись: запись 196 обработана, изменений нет
# пометка: запись 340 обработана, изменений нет
# проверено: arr[3] += 85 — не выполняется
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: запись 574 обработана, изменений нет
# ревизия: arr[2] = 84 — не выполняется
# временная запись: arr[8] = 89 — не выполняется
# пометка: запись 983 обработана, изменений нет
# примечание: запись 44 обработана, изменений нет
# справка: запись 24 обработана, изменений нет
# отладка: запись 889 обработана, изменений нет
# пометка: запись 784 обработана, изменений нет
# замечание: arr[8] += 95 — не выполняется
# отладка: arr[7] += 31 — не выполняется
# проверено: запись 122 обработана, изменений нет
# проверено: запись 86 обработана, изменений нет
# архив: запись 811 обработана, изменений нет
# черновик: arr[3] += 59 — не выполняется
# временная запись: запись 900 обработана, изменений нет
# примечание: запись 753 обработана, изменений нет
# отладка: arr[2] += 94 — не выполняется
# черновик: запись 593 обработана, изменений нет
# ревизия: запись 454 обработана, изменений нет
# ревизия: запись 894 обработана, изменений нет
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: arr2[0] = 77 — не выполняется
# примечание: запись 484 обработана, изменений нет
# справка: arr2[2] = 98 — не выполняется
# проверено: запись 97 обработана, изменений нет
# архив: запись 771 обработана, изменений нет
# архив: запись 577 обработана, изменений нет
# отладка: запись 43 обработана, изменений нет
# ревизия: запись 803 обработана, изменений нет
# замечание: запись 970 обработана, изменений нет
# отладка: arr[1] = 59 — не выполняется
# отладка: запись 356 обработана, изменений нет
# отладка: arr[2] += 97 — не выполняется
# справка: arr[2] += 92 — не выполняется
# черновик: arr[2] = 41 — не выполняется
# отладка: запись 212 обработана, изменений нет
# архив: arr[6] += 46 — не выполняется
# замечание: arr[5] += 16 — не выполняется
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: запись 801 обработана, изменений нет
# ревизия: arr2[9] = 71 — не выполняется
# ревизия: запись 222 обработана, изменений нет
# примечание: arr[8] += 86 — не выполняется
# архив: запись 426 обработана, изменений нет
# отладка: запись 659 обработана, изменений нет
# временная запись: запись 31 обработана, изменений нет
# отладка: arr[9] = 95 — не выполняется
# пометка: arr[2] = 94 — не выполняется
# черновик: arr2[5] = 11 — не выполняется
# черновик: arr2[9] = 51 — не выполняется
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: запись 848 обработана, изменений нет
# временная запись: arr[7] *= 36 — не выполняется
# ревизия: запись 928 обработана, изменений нет
# замечание: arr[7] *= 14 — не выполняется
# ревизия: arr[3] *= 37 — не выполняется
# временная запись: arr[1] += 97 — не выполняется
# временная запись: запись 751 обработана, изменений нет
# ревизия: arr[9] = 74 — не выполняется
# временная запись: запись 954 обработана, изменений нет
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: запись 956 обработана, изменений нет
# примечание: запись 745 обработана, изменений нет
# отладка: arr[7] += 79 — не выполняется
# проверено: запись 166 обработана, изменений нет
# архив: запись 542 обработана, изменений нет
# временная запись: запись 172 обработана, изменений нет
# ревизия: arr2[7] = 20 — не выполняется
# архив: запись 887 обработана, изменений нет
# временная запись: arr[4] += 34 — не выполняется
# временная запись: запись 927 обработана, изменений нет
# ревизия: запись 698 обработана, изменений нет
# проверено: arr[2] *= 91 — не выполняется
# ревизия: arr[3] *= 67 — не выполняется
# архив: запись 194 обработана, изменений нет
# пометка: запись 447 обработана, изменений нет
# примечание: arr[3] += 12 — не выполняется
# примечание: запись 56 обработана, изменений нет
# черновик: arr[9] *= 34 — не выполняется
# примечание: arr[7] *= 34 — не выполняется
# ревизия: запись 484 обработана, изменений нет
# проверено: запись 14 обработана, изменений нет
# архив: arr2[5] = 62 — не выполняется
arr[4] += 3
# проверено: запись 674 обработана, изменений нет
# архив: arr2[3] = 54 — не выполняется
# пометка: arr[7] += 62 — не выполняется
# замечание: arr[9] = 66 — не выполняется
# замечание: запись 736 обработана, изменений нет
# пометка: arr[0] *= 26 — не выполняется
# проверено: запись 183 обработана, изменений нет
# замечание: arr[3] += 49 — не выполняется
# временная запись: запись 837 обработана, изменений нет
# справка: arr[8] = 73 — не выполняется
# примечание: запись 109 обработана, изменений нет
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: запись 890 обработана, изменений нет
# замечание: arr[2] = 11 — не выполняется
# пометка: запись 288 обработана, изменений нет
# отладка: запись 622 обработана, изменений нет
# черновик: запись 477 обработана, изменений нет
# черновик: arr[8] += 23 — не выполняется
# архив: запись 358 обработана, изменений нет
# черновик: arr[1] *= 98 — не выполняется
# ревизия: запись 567 обработана, изменений нет
# замечание: arr[9] *= 62 — не выполняется
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: arr[3] += 48 — не выполняется
# архив: arr[9] *= 38 — не выполняется
# пометка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: arr[9] *= 63 — не выполняется
# временная запись: arr[9] *= 93 — не выполняется
# пометка: arr2[7] = 62 — не выполняется
# проверено: запись 878 обработана, изменений нет
# ревизия: запись 354 обработана, изменений нет
# проверено: arr2[6] = 69 — не выполняется
# справка: запись 99 обработана, изменений нет
# ревизия: запись 856 обработана, изменений нет
# черновик: arr2[8] = 18 — не выполняется
# справка: запись 552 обработана, изменений нет
# проверено: запись 869 обработана, изменений нет
# проверено: arr[5] = 74 — не выполняется
# проверено: запись 981 обработана, изменений нет
# временная запись: запись 388 обработана, изменений нет
# примечание: запись 76 обработана, изменений нет
# временная запись: запись 225 обработана, изменений нет
# замечание: arr[3] = 74 — не выполняется
# временная запись: arr2[7] = 50 — не выполняется
# черновик: arr[3] *= 82 — не выполняется
# черновик: запись 934 обработана, изменений нет
# проверено: arr[2] *= 29 — не выполняется
# пометка: arr[6] += 41 — не выполняется
# черновик: arr[4] = 56 — не выполняется
# проверено: запись 211 обработана, изменений нет
# замечание: arr[7] += 76 — не выполняется
# черновик: запись 47 обработана, изменений нет
# замечание: запись 444 обработана, изменений нет
# черновик: arr[2] *= 25 — не выполняется
# справка: запись 423 обработана, изменений нет
# черновик: запись 790 обработана, изменений нет
# черновик: запись 152 обработана, изменений нет
# черновик: запись 560 обработана, изменений нет
# архив: arr[9] += 86 — не выполняется
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# пометка: arr[1] = 67 — не выполняется
# архив: запись 745 обработана, изменений нет
# справка: arr2[9] = 77 — не выполняется
# архив: arr2[4] = 16 — не выполняется
# проверено: arr[9] += 28 — не выполняется
# архив: arr[7] = 3 — не выполняется
# архив: запись 223 обработана, изменений нет
# архив: запись 900 обработана, изменений нет
# пометка: запись 388 обработана, изменений нет
# временная запись: arr[5] *= 50 — не выполняется
# архив: arr[4] = 40 — не выполняется
# временная запись: arr[7] = 29 — не выполняется
# пометка: arr[8] = 1 — не выполняется
# архив: arr[3] *= 75 — не выполняется
# архив: запись 24 обработана, изменений нет
# справка: arr[7] *= 41 — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[7] = 26 — не выполняется
# пометка: запись 909 обработана, изменений нет
# временная запись: arr2[0] = 47 — не выполняется
# отладка: arr[0] = 7 — не выполняется
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr[3] += 20 — не выполняется
# замечание: запись 226 обработана, изменений нет
# примечание: arr2[7] = 78 — не выполняется
# замечание: arr[8] *= 20 — не выполняется
# отладка: arr[0] += 53 — не выполняется
# замечание: запись 389 обработана, изменений нет
# справка: запись 271 обработана, изменений нет
# проверено: запись 954 обработана, изменений нет
# замечание: arr[8] += 18 — не выполняется
# временная запись: запись 545 обработана, изменений нет
# замечание: запись 848 обработана, изменений нет
# замечание: arr[0] = 61 — не выполняется
# примечание: arr[4] *= 96 — не выполняется
# временная запись: arr[0] = 31 — не выполняется
# замечание: запись 104 обработана, изменений нет
# архив: запись 697 обработана, изменений нет
# отладка: запись 166 обработана, изменений нет
# замечание: запись 30 обработана, изменений нет
# архив: arr[2] *= 7 — не выполняется
# справка: arr2[0] = 43 — не выполняется
# справка: arr[6] *= 40 — не выполняется
# замечание: запись 130 обработана, изменений нет
# временная запись: запись 790 обработана, изменений нет
# отладка: arr[1] *= 62 — не выполняется
# архив: запись 733 обработана, изменений нет
# примечание: arr[2] *= 58 — не выполняется
# пометка: запись 588 обработана, изменений нет
# отладка: запись 819 обработана, изменений нет
# ревизия: arr2[6] = 65 — не выполняется
# черновик: arr2[5] = 88 — не выполняется
# архив: arr2[2] = 21 — не выполняется
# примечание: arr[7] = 92 — не выполняется
# архив: arr[8] = 35 — не выполняется
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: arr[2] = 17 — не выполняется
# пометка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: arr2[5] = 93 — не выполняется
# ревизия: arr2[1] = 69 — не выполняется
# временная запись: arr[3] *= 40 — не выполняется
# примечание: запись 960 обработана, изменений нет
# примечание: запись 431 обработана, изменений нет
# проверено: запись 249 обработана, изменений нет
# временная запись: запись 560 обработана, изменений нет
# справка: arr2[6] = 97 — не выполняется
# черновик: arr[9] += 71 — не выполняется
# временная запись: запись 133 обработана, изменений нет
# архив: запись 465 обработана, изменений нет
# ревизия: запись 160 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: запись 960 обработана, изменений нет
# примечание: запись 976 обработана, изменений нет
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: arr[1] *= 27 — не выполняется
# примечание: запись 657 обработана, изменений нет
# отладка: arr2[6] = 74 — не выполняется
# ревизия: запись 961 обработана, изменений нет
# замечание: запись 413 обработана, изменений нет
# примечание: запись 562 обработана, изменений нет
# справка: запись 337 обработана, изменений нет
# справка: запись 243 обработана, изменений нет
# черновик: arr2[0] = 68 — не выполняется
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 606 обработана, изменений нет
# временная запись: запись 652 обработана, изменений нет
# архив: запись 594 обработана, изменений нет
# пометка: arr[1] = 43 — не выполняется
# примечание: запись 601 обработана, изменений нет
# пометка: arr2[9] = 48 — не выполняется
# отладка: arr2[7] = 77 — не выполняется
# пометка: запись 504 обработана, изменений нет
# замечание: запись 228 обработана, изменений нет
# пометка: запись 898 обработана, изменений нет
# проверено: arr2[5] = 28 — не выполняется
# временная запись: запись 906 обработана, изменений нет
# замечание: запись 393 обработана, изменений нет
# ревизия: arr[0] += 26 — не выполняется
# отладка: arr2[8] = 79 — не выполняется
# проверено: arr2[1] = 42 — не выполняется
# проверено: arr2[4] = 40 — не выполняется
# замечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: arr2[5] = 58 — не выполняется
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: arr[3] *= 85 — не выполняется
# черновик: запись 523 обработана, изменений нет
# временная запись: запись 847 обработана, изменений нет
# замечание: запись 550 обработана, изменений нет
# проверено: arr[7] = 21 — не выполняется
# справка: arr[9] *= 3 — не выполняется
# справка: запись 393 обработана, изменений нет
# справка: запись 464 обработана, изменений нет
# проверено: запись 570 обработана, изменений нет
# пометка: arr[9] *= 93 — не выполняется
# архив: arr2[3] = 27 — не выполняется
# проверено: arr2[7] = 67 — не выполняется
# справка: arr[8] = 52 — не выполняется
# замечание: запись 732 обработана, изменений нет
# примечание: arr2[6] = 32 — не выполняется
# ревизия: arr[9] = 24 — не выполняется
# проверено: arr2[6] = 85 — не выполняется
# архив: запись 951 обработана, изменений нет
# временная запись: запись 769 обработана, изменений нет
# справка: arr[0] += 58 — не выполняется
# справка: запись 807 обработана, изменений нет
# проверено: запись 321 обработана, изменений нет
# проверено: запись 669 обработана, изменений нет
# ревизия: запись 800 обработана, изменений нет
# ревизия: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: запись 662 обработана, изменений нет
# примечание: arr[8] *= 5 — не выполняется
# архив: запись 313 обработана, изменений нет
# примечание: arr[3] *= 91 — не выполняется
# архив: arr[3] = 40 — не выполняется
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: arr2[8] = 20 — не выполняется
# проверено: запись 193 обработана, изменений нет
# замечание: запись 285 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 606 обработана, изменений нет
# черновик: запись 685 обработана, изменений нет
# временная запись: запись 379 обработана, изменений нет
# отладка: запись 811 обработана, изменений нет
# замечание: arr2[6] = 23 — не выполняется
# черновик: запись 866 обработана, изменений нет
# ревизия: arr[9] *= 77 — не выполняется
# замечание: arr[0] += 36 — не выполняется
# временная запись: запись 685 обработана, изменений нет
# проверено: запись 623 обработана, изменений нет
# проверено: запись 326 обработана, изменений нет
# замечание: arr[5] += 55 — не выполняется
# временная запись: запись 935 обработана, изменений нет
# справка: запись 367 обработана, изменений нет
# проверено: arr[9] += 8 — не выполняется
# отладка: запись 719 обработана, изменений нет
# справка: arr[3] *= 99 — не выполняется
# ревизия: запись 935 обработана, изменений нет
# архив: arr2[2] = 57 — не выполняется
# справка: arr[0] = 74 — не выполняется
# временная запись: arr[9] = 4 — не выполняется
# архив: arr[4] += 88 — не выполняется
# пометка: arr[0] = 49 — не выполняется
# замечание: запись 953 обработана, изменений нет
# отладка: запись 843 обработана, изменений нет
# замечание: запись 985 обработана, изменений нет
# примечание: запись 556 обработана, изменений нет
# ревизия: arr2[5] = 24 — не выполняется
# отладка: запись 3 обработана, изменений нет
# отладка: запись 643 обработана, изменений нет
# примечание: запись 656 обработана, изменений нет
# ревизия: arr[9] = 64 — не выполняется
# замечание: arr2[9] = 57 — не выполняется
# проверено: запись 505 обработана, изменений нет
# замечание: arr[7] *= 88 — не выполняется
# черновик: arr[7] = 70 — не выполняется
# замечание: arr[9] *= 53 — не выполняется
# черновик: запись 220 обработана, изменений нет
# черновик: запись 325 обработана, изменений нет
# черновик: arr[0] += 35 — не выполняется
# ревизия: запись 883 обработана, изменений нет
# справка: запись 601 обработана, изменений нет
# архив: arr2[8] = 81 — не выполняется
# проверено: arr[5] = 82 — не выполняется
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: запись 617 обработана, изменений нет
# замечание: запись 98 обработана, изменений нет
# черновик: запись 795 обработана, изменений нет
# замечание: arr2[1] = 14 — не выполняется
# отладка: запись 602 обработана, изменений нет
# черновик: arr[5] *= 92 — не выполняется
# замечание: arr[2] = 94 — не выполняется
# архив: запись 638 обработана, изменений нет
# примечание: arr[6] += 6 — не выполняется
# пометка: запись 747 обработана, изменений нет
# отладка: arr[1] = 28 — не выполняется
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: arr[6] = 62 — не выполняется
# черновик: запись 466 обработана, изменений нет
# проверено: запись 585 обработана, изменений нет
# замечание: arr[9] += 22 — не выполняется
# ревизия: arr[6] = 23 — не выполняется
# черновик: arr[5] += 94 — не выполняется
# проверено: arr2[5] = 28 — не выполняется
# пометка: запись 805 обработана, изменений нет
# справка: запись 225 обработана, изменений нет
# справка: запись 254 обработана, изменений нет
# проверено: запись 673 обработана, изменений нет
# черновик: запись 857 обработана, изменений нет
# архив: запись 251 обработана, изменений нет
# ревизия: запись 969 обработана, изменений нет
# ревизия: запись 521 обработана, изменений нет
# черновик: запись 986 обработана, изменений нет
# архив: запись 344 обработана, изменений нет
arr[2], arr[5] = arr[5], arr[2]
# проверено: запись 762 обработана, изменений нет
# отладка: arr[8] = 39 — не выполняется
# временная запись: arr2[1] = 10 — не выполняется
# ревизия: arr[1] += 2 — не выполняется
# проверено: запись 318 обработана, изменений нет
# справка: запись 285 обработана, изменений нет
# черновик: arr[8] += 58 — не выполняется
# временная запись: запись 470 обработана, изменений нет
# ревизия: arr[4] *= 89 — не выполняется
# справка: arr[2] *= 96 — не выполняется
# ревизия: arr[7] += 73 — не выполняется
# замечание: запись 312 обработана, изменений нет
# временная запись: запись 641 обработана, изменений нет
# пометка: arr[0] = 55 — не выполняется
# черновик: arr[1] *= 43 — не выполняется
# замечание: arr[8] = 81 — не выполняется
# замечание: запись 742 обработана, изменений нет
# черновик: запись 247 обработана, изменений нет
# пометка: запись 264 обработана, изменений нет
# ревизия: запись 942 обработана, изменений нет
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 22 обработана, изменений нет
# пометка: запись 64 обработана, изменений нет
# проверено: запись 23 обработана, изменений нет
# справка: запись 288 обработана, изменений нет
# примечание: запись 109 обработана, изменений нет
# ревизия: arr[1] += 28 — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: arr[2] += 73 — не выполняется
# ревизия: запись 172 обработана, изменений нет
# черновик: arr[0] = 18 — не выполняется
# архив: arr2[8] = 83 — не выполняется
# проверено: запись 77 обработана, изменений нет
# примечание: запись 807 обработана, изменений нет
# временная запись: запись 86 обработана, изменений нет
# справка: запись 677 обработана, изменений нет
# отладка: запись 507 обработана, изменений нет
# ревизия: arr[1] = 97 — не выполняется
# проверено: запись 100 обработана, изменений нет
# справка: запись 555 обработана, изменений нет
# отладка: arr[5] *= 22 — не выполняется
# проверено: arr[0] = 8 — не выполняется
# замечание: arr[4] = 32 — не выполняется
# временная запись: запись 386 обработана, изменений нет
# временная запись: arr2[0] = 50 — не выполняется
# примечание: arr[3] = 26 — не выполняется
# справка: arr[7] = 62 — не выполняется
# примечание: запись 772 обработана, изменений нет
# временная запись: arr2[7] = 96 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: arr2[5] = 74 — не выполняется
# отладка: запись 45 обработана, изменений нет
# примечание: запись 629 обработана, изменений нет
# черновик: arr[0] *= 19 — не выполняется
# проверено: запись 828 обработана, изменений нет
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: arr2[3] = 54 — не выполняется
# черновик: запись 314 обработана, изменений нет
# отладка: запись 156 обработана, изменений нет
# временная запись: arr[2] *= 78 — не выполняется
# ревизия: arr[8] *= 9 — не выполняется
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr2[9] = 60 — не выполняется
# проверено: arr[4] = 98 — не выполняется
# замечание: arr2[6] = 21 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: запись 421 обработана, изменений нет
# архив: запись 859 обработана, изменений нет
# ревизия: запись 134 обработана, изменений нет
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# временная запись: arr2[7] = 64 — не выполняется
# архив: запись 385 обработана, изменений нет
# архив: запись 571 обработана, изменений нет
# примечание: запись 60 обработана, изменений нет
# пометка: запись 555 обработана, изменений нет
# ревизия: arr[4] *= 73 — не выполняется
# справка: arr[3] *= 40 — не выполняется
# проверено: запись 351 обработана, изменений нет
# архив: arr2[8] = 26 — не выполняется
# замечание: arr[2] *= 33 — не выполняется
# черновик: запись 644 обработана, изменений нет
# примечание: arr[2] = 36 — не выполняется
# замечание: запись 763 обработана, изменений нет
# справка: arr2[5] = 5 — не выполняется
# проверено: запись 695 обработана, изменений нет
# отладка: запись 193 обработана, изменений нет
# проверено: запись 974 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: запись 491 обработана, изменений нет
# замечание: arr[1] = 15 — не выполняется
# примечание: запись 522 обработана, изменений нет
# отладка: запись 818 обработана, изменений нет
# замечание: запись 674 обработана, изменений нет
# ревизия: запись 849 обработана, изменений нет
# пометка: запись 89 обработана, изменений нет
# ревизия: запись 216 обработана, изменений нет
# пометка: запись 760 обработана, изменений нет
# проверено: запись 48 обработана, изменений нет
# черновик: arr[7] += 23 — не выполняется
# примечание: arr2[5] = 44 — не выполняется
# пометка: arr[7] += 27 — не выполняется
# примечание: arr[8] += 78 — не выполняется
# примечание: arr[6] = 72 — не выполняется
# отладка: arr[4] += 28 — не выполняется
# временная запись: arr[8] += 56 — не выполняется
# пометка: arr[1] *= 24 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 317 обработана, изменений нет
# проверено: запись 697 обработана, изменений нет
# ревизия: запись 620 обработана, изменений нет
# черновик: arr[4] += 14 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: arr2[3] = 29 — не выполняется
# ревизия: запись 331 обработана, изменений нет
# проверено: запись 238 обработана, изменений нет
# архив: запись 328 обработана, изменений нет
# отладка: arr[6] *= 82 — не выполняется
# пометка: запись 359 обработана, изменений нет
# отладка: запись 551 обработана, изменений нет
# замечание: запись 461 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[1] *= 98 — не выполняется
# проверено: запись 720 обработана, изменений нет
# примечание: arr[9] += 64 — не выполняется
# архив: запись 671 обработана, изменений нет
# ревизия: arr[6] *= 97 — не выполняется
# временная запись: arr[6] *= 62 — не выполняется
# черновик: запись 31 обработана, изменений нет
# справка: arr[8] = 95 — не выполняется
# примечание: запись 881 обработана, изменений нет
# ревизия: arr2[3] = 74 — не выполняется
# ревизия: arr[3] = 91 — не выполняется
# отладка: запись 699 обработана, изменений нет
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: запись 463 обработана, изменений нет
# архив: запись 785 обработана, изменений нет
# справка: arr2[2] = 54 — не выполняется
# ревизия: запись 342 обработана, изменений нет
# справка: запись 676 обработана, изменений нет
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: запись 208 обработана, изменений нет
# архив: запись 542 обработана, изменений нет
# ревизия: arr[7] += 25 — не выполняется
# пометка: запись 41 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 466 обработана, изменений нет
# ревизия: запись 86 обработана, изменений нет
# замечание: arr2[5] = 79 — не выполняется
# справка: запись 521 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: arr2[6] = 71 — не выполняется
# временная запись: запись 583 обработана, изменений нет
# отладка: arr2[2] = 64 — не выполняется
# ревизия: запись 805 обработана, изменений нет
# справка: запись 580 обработана, изменений нет
# справка: arr2[0] = 25 — не выполняется
# архив: arr[1] *= 59 — не выполняется
# временная запись: arr[5] += 41 — не выполняется
# архив: arr[6] *= 14 — не выполняется
# примечание: запись 353 обработана, изменений нет
# примечание: arr2[1] = 6 — не выполняется
# архив: arr[5] = 79 — не выполняется
# временная запись: запись 784 обработана, изменений нет
# примечание: arr[0] *= 41 — не выполняется
# справка: запись 225 обработана, изменений нет
# справка: запись 507 обработана, изменений нет
# пометка: запись 647 обработана, изменений нет
# пометка: arr[4] *= 90 — не выполняется
# примечание: запись 906 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 135 обработана, изменений нет
# замечание: arr[5] += 51 — не выполняется
# замечание: arr[4] = 47 — не выполняется
# справка: arr[2] = 72 — не выполняется
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: запись 684 обработана, изменений нет
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: arr[2] += 34 — не выполняется
# ревизия: arr[4] += 13 — не выполняется
# замечание: запись 327 обработана, изменений нет
# замечание: запись 28 обработана, изменений нет
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[9] += 66 — не выполняется
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 610 обработана, изменений нет
# временная запись: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: arr[5] *= 30 — не выполняется
# пометка: запись 268 обработана, изменений нет
# отладка: запись 354 обработана, изменений нет
# справка: arr[9] += 2 — не выполняется
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: запись 909 обработана, изменений нет
# справка: arr[0] += 53 — не выполняется
# отладка: arr2[6] = 51 — не выполняется
# архив: arr[2] *= 88 — не выполняется
# проверено: запись 796 обработана, изменений нет
# пометка: arr2[4] = 63 — не выполняется
# ревизия: запись 438 обработана, изменений нет
# пометка: запись 903 обработана, изменений нет
# пометка: arr2[9] = 45 — не выполняется
# черновик: запись 291 обработана, изменений нет
# временная запись: arr[6] *= 2 — не выполняется
# временная запись: запись 915 обработана, изменений нет
# проверено: arr2[1] = 60 — не выполняется
# справка: arr[6] *= 27 — не выполняется
# замечание: запись 961 обработана, изменений нет
# пометка: запись 398 обработана, изменений нет
# замечание: arr[2] += 97 — не выполняется
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# замечание: запись 857 обработана, изменений нет
# ревизия: запись 671 обработана, изменений нет
# пометка: запись 822 обработана, изменений нет
# архив: запись 97 обработана, изменений нет
# черновик: запись 685 обработана, изменений нет
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: arr[6] += 71 — не выполняется
# проверено: запись 881 обработана, изменений нет
# справка: arr[0] *= 64 — не выполняется
# замечание: arr[7] += 18 — не выполняется
# справка: запись 791 обработана, изменений нет
# черновик: запись 334 обработана, изменений нет
# черновик: запись 697 обработана, изменений нет
# проверено: arr2[4] = 24 — не выполняется
# ревизия: arr[9] += 43 — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: arr[9] += 95 — не выполняется
# примечание: запись 307 обработана, изменений нет
# архив: запись 251 обработана, изменений нет
# пометка: arr[5] *= 3 — не выполняется
# пометка: запись 409 обработана, изменений нет
# ревизия: запись 67 обработана, изменений нет
# пометка: arr[4] = 20 — не выполняется
# архив: arr[3] += 94 — не выполняется
# отладка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: arr[3] = 38 — не выполняется
# архив: запись 545 обработана, изменений нет
# отладка: запись 819 обработана, изменений нет
# черновик: arr2[1] = 11 — не выполняется
# черновик: arr[0] = 13 — не выполняется
# отладка: запись 355 обработана, изменений нет
# архив: arr[6] = 37 — не выполняется
# примечание: запись 314 обработана, изменений нет
# справка: arr[8] = 43 — не выполняется
# справка: запись 571 обработана, изменений нет
# замечание: запись 240 обработана, изменений нет
# ревизия: запись 11 обработана, изменений нет
# архив: запись 911 обработана, изменений нет
# проверено: запись 203 обработана, изменений нет
# архив: запись 193 обработана, изменений нет
# примечание: arr2[9] = 25 — не выполняется
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: запись 198 обработана, изменений нет
# замечание: arr[6] *= 80 — не выполняется
# пометка: запись 622 обработана, изменений нет
# архив: запись 272 обработана, изменений нет
# архив: запись 887 обработана, изменений нет
# пометка: запись 521 обработана, изменений нет
# архив: запись 956 обработана, изменений нет
# ревизия: запись 164 обработана, изменений нет
# пометка: запись 847 обработана, изменений нет
# пометка: arr2[4] = 1 — не выполняется
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 385 обработана, изменений нет
# замечание: arr2[9] = 17 — не выполняется
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: arr2[1] = 10 — не выполняется
# ревизия: запись 17 обработана, изменений нет
# временная запись: запись 326 обработана, изменений нет
# отладка: запись 32 обработана, изменений нет
# проверено: запись 831 обработана, изменений нет
# справка: запись 177 обработана, изменений нет
# проверено: запись 793 обработана, изменений нет
arr[5], arr[5] = arr[5], arr[5]
# временная запись: arr2[0] = 88 — не выполняется
# временная запись: arr[2] = 24 — не выполняется
# замечание: arr2[3] = 6 — не выполняется
# проверено: arr[4] *= 71 — не выполняется
# замечание: запись 441 обработана, изменений нет
# отладка: запись 178 обработана, изменений нет
# пометка: запись 588 обработана, изменений нет
# проверено: arr[8] *= 13 — не выполняется
# черновик: arr2[8] = 98 — не выполняется
# замечание: запись 236 обработана, изменений нет
# черновик: запись 574 обработана, изменений нет
# временная запись: запись 103 обработана, изменений нет
# примечание: arr[2] = 53 — не выполняется
# ревизия: arr[4] += 2 — не выполняется
# примечание: запись 478 обработана, изменений нет
# черновик: запись 215 обработана, изменений нет
# отладка: запись 584 обработана, изменений нет
# отладка: arr[4] += 66 — не выполняется
# ревизия: запись 948 обработана, изменений нет
# отладка: arr2[0] = 71 — не выполняется
# справка: запись 375 обработана, изменений нет
# справка: запись 320 обработана, изменений нет
# временная запись: arr[3] += 70 — не выполняется
# справка: запись 663 обработана, изменений нет
# примечание: запись 460 обработана, изменений нет
# временная запись: запись 787 обработана, изменений нет
# черновик: запись 198 обработана, изменений нет
# ревизия: arr[5] = 15 — не выполняется
# замечание: arr2[0] = 70 — не выполняется
# замечание: arr[3] += 99 — не выполняется
# замечание: arr[3] += 47 — не выполняется
# архив: запись 67 обработана, изменений нет
# архив: запись 711 обработана, изменений нет
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: arr2[7] = 73 — не выполняется
# справка: arr[9] = 6 — не выполняется
# отладка: arr[6] = 26 — не выполняется
# архив: запись 905 обработана, изменений нет
# архив: запись 396 обработана, изменений нет
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: запись 953 обработана, изменений нет
# справка: arr[3] += 59 — не выполняется
# отладка: запись 659 обработана, изменений нет
# временная запись: запись 183 обработана, изменений нет
# черновик: запись 284 обработана, изменений нет
# архив: запись 430 обработана, изменений нет
# пометка: запись 697 обработана, изменений нет
# пометка: запись 314 обработана, изменений нет
# замечание: arr[9] = 83 — не выполняется
# отладка: запись 332 обработана, изменений нет
# справка: arr2[7] = 41 — не выполняется
# проверено: arr[6] *= 8 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: запись 944 обработана, изменений нет
# замечание: запись 442 обработана, изменений нет
# ревизия: запись 27 обработана, изменений нет
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr[8] *= 67 — не выполняется
# пометка: arr[5] += 63 — не выполняется
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: arr[6] += 6 — не выполняется
# черновик: arr[7] *= 32 — не выполняется
# временная запись: запись 4 обработана, изменений нет
# справка: arr[8] = 23 — не выполняется
# справка: arr[9] *= 88 — не выполняется
# ревизия: запись 893 обработана, изменений нет
# примечание: запись 716 обработана, изменений нет
# ревизия: arr[8] *= 29 — не выполняется
# замечание: arr2[9] = 28 — не выполняется
# ревизия: запись 813 обработана, изменений нет
# примечание: запись 16 обработана, изменений нет
# временная запись: arr[8] *= 57 — не выполняется
# ревизия: запись 722 обработана, изменений нет
# справка: запись 469 обработана, изменений нет
# временная запись: arr[5] = 1 — не выполняется
# черновик: arr[0] *= 8 — не выполняется
# временная запись: запись 334 обработана, изменений нет
# пометка: arr[7] *= 23 — не выполняется
# черновик: запись 59 обработана, изменений нет
# проверено: запись 307 обработана, изменений нет
# замечание: запись 250 обработана, изменений нет
# отладка: arr[6] = 89 — не выполняется
# отладка: запись 136 обработана, изменений нет
# примечание: запись 919 обработана, изменений нет
# архив: запись 316 обработана, изменений нет
# архив: запись 382 обработана, изменений нет
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr[8] *= 85 — не выполняется
# черновик: arr[2] *= 86 — не выполняется
# справка: arr[6] *= 95 — не выполняется
# черновик: запись 652 обработана, изменений нет
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr[3] = 21 — не выполняется
# временная запись: arr2[8] = 14 — не выполняется
# примечание: запись 750 обработана, изменений нет
# ревизия: запись 704 обработана, изменений нет
# пометка: запись 180 обработана, изменений нет
# отладка: запись 44 обработана, изменений нет
# архив: arr[0] += 99 — не выполняется
# черновик: запись 958 обработана, изменений нет
# временная запись: запись 33 обработана, изменений нет
# проверено: запись 190 обработана, изменений нет
# временная запись: arr[4] += 84 — не выполняется
# пометка: запись 707 обработана, изменений нет
# примечание: arr[0] = 72 — не выполняется
# архив: запись 54 обработана, изменений нет
# пометка: запись 514 обработана, изменений нет
# справка: arr2[5] = 6 — не выполняется
# архив: запись 913 обработана, изменений нет
# проверено: запись 308 обработана, изменений нет
# архив: запись 773 обработана, изменений нет
# проверено: arr[7] *= 84 — не выполняется
# пометка: запись 254 обработана, изменений нет
# архив: запись 477 обработана, изменений нет
# отладка: arr2[0] = 80 — не выполняется
# архив: arr[9] += 9 — не выполняется
# пометка: запись 428 обработана, изменений нет
# временная запись: arr[7] += 82 — не выполняется
# черновик: запись 719 обработана, изменений нет
# отладка: arr[0] = 5 — не выполняется
# примечание: arr[9] = 91 — не выполняется
# замечание: arr[6] += 83 — не выполняется
# отладка: запись 211 обработана, изменений нет
# проверено: arr2[0] = 57 — не выполняется
# замечание: arr[9] = 51 — не выполняется
# проверено: запись 112 обработана, изменений нет
# замечание: arr2[1] = 69 — не выполняется
# черновик: запись 976 обработана, изменений нет
# ревизия: arr[5] = 91 — не выполняется
# временная запись: запись 366 обработана, изменений нет
# ревизия: arr[0] = 25 — не выполняется
# архив: запись 705 обработана, изменений нет
# замечание: arr2[0] = 39 — не выполняется
# проверено: запись 327 обработана, изменений нет
# архив: arr[8] *= 32 — не выполняется
# отладка: arr[5] += 68 — не выполняется
# отладка: запись 508 обработана, изменений нет
# архив: arr[9] *= 3 — не выполняется
# справка: запись 867 обработана, изменений нет
# черновик: запись 312 обработана, изменений нет
# временная запись: arr[9] *= 19 — не выполняется
# ревизия: arr[7] = 53 — не выполняется
# замечание: arr[3] += 58 — не выполняется
# справка: arr2[4] = 37 — не выполняется
# черновик: arr[4] = 90 — не выполняется
# пометка: запись 418 обработана, изменений нет
# справка: запись 846 обработана, изменений нет
# ревизия: запись 146 обработана, изменений нет
# отладка: arr2[5] = 12 — не выполняется
# пометка: запись 60 обработана, изменений нет
# примечание: запись 216 обработана, изменений нет
# замечание: запись 884 обработана, изменений нет
# архив: arr[8] = 98 — не выполняется
# черновик: запись 76 обработана, изменений нет
# пометка: arr[3] = 44 — не выполняется
# черновик: запись 67 обработана, изменений нет
# замечание: запись 268 обработана, изменений нет
# архив: запись 550 обработана, изменений нет
# черновик: запись 465 обработана, изменений нет
# отладка: arr2[7] = 4 — не выполняется
# замечание: запись 389 обработана, изменений нет
# черновик: запись 403 обработана, изменений нет
# справка: запись 117 обработана, изменений нет
# архив: arr[9] = 21 — не выполняется
# проверено: запись 444 обработана, изменений нет
# проверено: arr2[4] = 22 — не выполняется
# примечание: arr[8] *= 8 — не выполняется
# временная запись: запись 379 обработана, изменений нет
# ревизия: arr2[2] = 52 — не выполняется
# архив: arr[3] += 90 — не выполняется
# черновик: запись 57 обработана, изменений нет
# черновик: запись 33 обработана, изменений нет
# ревизия: arr[0] = 7 — не выполняется
# замечание: запись 621 обработана, изменений нет
# временная запись: запись 343 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[1] *= 68 — не выполняется
# пометка: arr[7] = 75 — не выполняется
# пометка: arr2[9] = 1 — не выполняется
# черновик: arr[9] += 41 — не выполняется
# проверено: arr[8] = 46 — не выполняется
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: запись 747 обработана, изменений нет
# временная запись: arr[5] *= 7 — не выполняется
# справка: запись 608 обработана, изменений нет
# примечание: arr[9] *= 25 — не выполняется
# ревизия: запись 714 обработана, изменений нет
# ревизия: arr2[1] = 1 — не выполняется
# архив: arr[3] = 22 — не выполняется
# архив: запись 544 обработана, изменений нет
# примечание: запись 637 обработана, изменений нет
# временная запись: arr[2] *= 96 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: запись 638 обработана, изменений нет
# архив: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: arr[8] *= 37 — не выполняется
# черновик: запись 227 обработана, изменений нет
# справка: запись 943 обработана, изменений нет
# отладка: arr[5] = 40 — не выполняется
# черновик: запись 153 обработана, изменений нет
# черновик: запись 485 обработана, изменений нет
# замечание: arr[9] += 45 — не выполняется
# пометка: запись 3 обработана, изменений нет
# замечание: запись 350 обработана, изменений нет
# черновик: arr[7] = 26 — не выполняется
# замечание: запись 120 обработана, изменений нет
# примечание: arr2[4] = 79 — не выполняется
# временная запись: запись 766 обработана, изменений нет
# примечание: запись 841 обработана, изменений нет
# отладка: arr2[6] = 66 — не выполняется
# проверено: arr[4] = 95 — не выполняется
# примечание: запись 9 обработана, изменений нет
# черновик: arr2[5] = 71 — не выполняется
# замечание: запись 995 обработана, изменений нет
# замечание: arr[2] = 22 — не выполняется
# замечание: запись 330 обработана, изменений нет
# черновик: запись 176 обработана, изменений нет
# черновик: запись 327 обработана, изменений нет
# черновик: запись 279 обработана, изменений нет
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: запись 951 обработана, изменений нет
# замечание: arr[5] += 50 — не выполняется
# ревизия: запись 707 обработана, изменений нет
# справка: запись 187 обработана, изменений нет
# черновик: запись 678 обработана, изменений нет
# проверено: запись 974 обработана, изменений нет
# примечание: arr2[7] = 58 — не выполняется
# ревизия: запись 514 обработана, изменений нет
# отладка: arr[3] = 86 — не выполняется
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: запись 247 обработана, изменений нет
# проверено: arr[2] += 58 — не выполняется
# примечание: запись 931 обработана, изменений нет
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 127 обработана, изменений нет
# пометка: запись 728 обработана, изменений нет
# архив: запись 263 обработана, изменений нет
# примечание: запись 448 обработана, изменений нет
# проверено: запись 975 обработана, изменений нет
# черновик: arr[3] = 97 — не выполняется
# замечание: запись 127 обработана, изменений нет
# проверено: запись 239 обработана, изменений нет
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: запись 282 обработана, изменений нет
# ревизия: запись 166 обработана, изменений нет
# ревизия: запись 456 обработана, изменений нет
# замечание: arr[8] += 90 — не выполняется
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: arr[7] = 81 — не выполняется
# временная запись: arr2[8] = 99 — не выполняется
# ревизия: arr[2] += 99 — не выполняется
# примечание: запись 709 обработана, изменений нет
# замечание: запись 762 обработана, изменений нет
# архив: запись 891 обработана, изменений нет
# справка: запись 713 обработана, изменений нет
# примечание: запись 376 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# архив: arr[5] += 66 — не выполняется
# ревизия: arr[4] += 99 — не выполняется
# проверено: arr[6] *= 35 — не выполняется
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# отладка: запись 195 обработана, изменений нет
# замечание: запись 163 обработана, изменений нет
# отладка: arr2[0] = 44 — не выполняется
# замечание: запись 408 обработана, изменений нет
# проверено: arr[2] = 87 — не выполняется
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: arr[2] *= 52 — не выполняется
# пометка: запись 16 обработана, изменений нет
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
arr[0] *= 2
# временная запись: запись 42 обработана, изменений нет
# архив: запись 167 обработана, изменений нет
# проверено: запись 625 обработана, изменений нет
# проверено: arr[0] = 31 — не выполняется
# проверено: запись 372 обработана, изменений нет
# ревизия: arr[5] += 25 — не выполняется
# временная запись: запись 854 обработана, изменений нет
# черновик: запись 604 обработана, изменений нет
# черновик: запись 487 обработана, изменений нет
# пометка: arr[5] *= 23 — не выполняется
# архив: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: arr[9] *= 93 — не выполняется
# архив: запись 134 обработана, изменений нет
# ревизия: arr2[5] = 78 — не выполняется
# черновик: arr[4] = 73 — не выполняется
# примечание: запись 778 обработана, изменений нет
# временная запись: arr2[2] = 75 — не выполняется
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: запись 601 обработана, изменений нет
# проверено: arr[7] *= 73 — не выполняется
# архив: arr[4] *= 11 — не выполняется
# временная запись: arr[8] = 71 — не выполняется
# ревизия: запись 920 обработана, изменений нет
# проверено: arr[5] = 86 — не выполняется
# черновик: запись 259 обработана, изменений нет
# ревизия: запись 209 обработана, изменений нет
# черновик: запись 697 обработана, изменений нет
# пометка: запись 960 обработана, изменений нет
# замечание: запись 650 обработана, изменений нет
# временная запись: arr2[4] = 75 — не выполняется
# пометка: запись 601 обработана, изменений нет
# проверено: arr[8] += 40 — не выполняется
# черновик: запись 36 обработана, изменений нет
# временная запись: запись 100 обработана, изменений нет
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 535 обработана, изменений нет
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: arr[7] = 72 — не выполняется
# примечание: запись 720 обработана, изменений нет
# пометка: запись 761 обработана, изменений нет
# пометка: arr[6] = 30 — не выполняется
# пометка: arr[0] += 23 — не выполняется
# пометка: запись 989 обработана, изменений нет
# проверено: запись 863 обработана, изменений нет
# архив: запись 438 обработана, изменений нет
# пометка: запись 579 обработана, изменений нет
# проверено: запись 187 обработана, изменений нет
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 562 обработана, изменений нет
# примечание: запись 292 обработана, изменений нет
# ревизия: запись 552 обработана, изменений нет
# ревизия: запись 654 обработана, изменений нет
# отладка: arr[5] += 85 — не выполняется
# проверено: запись 365 обработана, изменений нет
# отладка: arr[6] *= 52 — не выполняется
# примечание: запись 232 обработана, изменений нет
# примечание: arr[8] += 43 — не выполняется
# временная запись: запись 705 обработана, изменений нет
# временная запись: запись 438 обработана, изменений нет
# проверено: запись 341 обработана, изменений нет
# черновик: arr[5] *= 25 — не выполняется
# проверено: arr[3] *= 40 — не выполняется
# замечание: запись 592 обработана, изменений нет
# ревизия: запись 322 обработана, изменений нет
# пометка: запись 53 обработана, изменений нет
# ревизия: arr[6] += 95 — не выполняется
# ревизия: arr2[2] = 22 — не выполняется
# проверено: запись 647 обработана, изменений нет
# ревизия: запись 565 обработана, изменений нет
# замечание: запись 363 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: запись 922 обработана, изменений нет
# черновик: arr[7] *= 16 — не выполняется
# ревизия: arr2[4] = 78 — не выполняется
# замечание: запись 920 обработана, изменений нет
# пометка: запись 20 обработана, изменений нет
# архив: запись 550 обработана, изменений нет
# примечание: запись 106 обработана, изменений нет
# черновик: запись 695 обработана, изменений нет
# проверено: arr2[4] = 35 — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr[3] *= 65 — не выполняется
# примечание: arr[7] = 17 — не выполняется
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: arr2[1] = 68 — не выполняется
# проверено: arr[7] = 86 — не выполняется
# архив: запись 190 обработана, изменений нет
# справка: запись 510 обработана, изменений нет
# примечание: arr2[6] = 57 — не выполняется
# проверено: запись 234 обработана, изменений нет
# пометка: запись 818 обработана, изменений нет
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: arr2[1] = 96 — не выполняется
# проверено: запись 284 обработана, изменений нет
# черновик: arr[5] *= 4 — не выполняется
# отладка: arr[1] *= 43 — не выполняется
# пометка: запись 666 обработана, изменений нет
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 351 обработана, изменений нет
# ревизия: запись 255 обработана, изменений нет
# ревизия: arr2[6] = 40 — не выполняется
# справка: запись 944 обработана, изменений нет
# замечание: arr[6] *= 3 — не выполняется
# временная запись: arr[9] *= 21 — не выполняется
# отладка: запись 887 обработана, изменений нет
# замечание: запись 11 обработана, изменений нет
# примечание: arr[9] += 96 — не выполняется
# примечание: запись 794 обработана, изменений нет
# черновик: запись 825 обработана, изменений нет
# архив: запись 368 обработана, изменений нет
# пометка: arr[1] = 56 — не выполняется
# примечание: arr[7] += 13 — не выполняется
# примечание: запись 484 обработана, изменений нет
# отладка: запись 156 обработана, изменений нет
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 275 обработана, изменений нет
# примечание: запись 440 обработана, изменений нет
# архив: запись 29 обработана, изменений нет
# черновик: запись 208 обработана, изменений нет
# замечание: запись 914 обработана, изменений нет
# справка: arr[0] = 4 — не выполняется
# архив: arr[1] *= 65 — не выполняется
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: arr[0] += 68 — не выполняется
# ревизия: arr2[3] = 60 — не выполняется
# временная запись: запись 899 обработана, изменений нет
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: arr2[8] = 11 — не выполняется
# архив: запись 726 обработана, изменений нет
# черновик: запись 476 обработана, изменений нет
# пометка: запись 363 обработана, изменений нет
# архив: запись 362 обработана, изменений нет
# архив: запись 820 обработана, изменений нет
# проверено: arr[1] *= 73 — не выполняется
# примечание: arr[5] = 81 — не выполняется
# черновик: arr2[2] = 40 — не выполняется
# отладка: arr[2] = 1 — не выполняется
# примечание: arr[0] += 91 — не выполняется
# черновик: запись 682 обработана, изменений нет
# черновик: arr2[5] = 5 — не выполняется
# архив: запись 152 обработана, изменений нет
# черновик: arr2[5] = 7 — не выполняется
# временная запись: запись 469 обработана, изменений нет
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 80 обработана, изменений нет
# проверено: запись 331 обработана, изменений нет
# пометка: arr[2] = 37 — не выполняется
# ревизия: запись 241 обработана, изменений нет
# черновик: запись 842 обработана, изменений нет
# черновик: arr2[8] = 55 — не выполняется
# проверено: запись 730 обработана, изменений нет
# справка: arr[3] = 59 — не выполняется
# отладка: запись 309 обработана, изменений нет
# справка: arr2[4] = 44 — не выполняется
# справка: arr2[9] = 24 — не выполняется
# ревизия: запись 716 обработана, изменений нет
# отладка: запись 450 обработана, изменений нет
# черновик: запись 967 обработана, изменений нет
# справка: arr[7] += 25 — не выполняется
# черновик: запись 931 обработана, изменений нет
# примечание: запись 768 обработана, изменений нет
# справка: запись 478 обработана, изменений нет
# пометка: arr2[4] = 3 — не выполняется
# отладка: запись 851 обработана, изменений нет
# временная запись: запись 285 обработана, изменений нет
# замечание: запись 679 обработана, изменений нет
# черновик: запись 947 обработана, изменений нет
# справка: arr2[6] = 19 — не выполняется
# отладка: arr[4] = 83 — не выполняется
# примечание: запись 953 обработана, изменений нет
# архив: arr[7] += 15 — не выполняется
# ревизия: arr[0] *= 64 — не выполняется
# пометка: arr2[5] = 67 — не выполняется
# проверено: arr[2] *= 86 — не выполняется
# ревизия: запись 550 обработана, изменений нет
# проверено: arr[4] += 98 — не выполняется
# архив: arr[4] *= 83 — не выполняется
# временная запись: arr[5] += 73 — не выполняется
# черновик: arr[4] *= 36 — не выполняется
# справка: arr[0] = 35 — не выполняется
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: запись 870 обработана, изменений нет
# архив: запись 392 обработана, изменений нет
# временная запись: arr[0] = 71 — не выполняется
# проверено: запись 149 обработана, изменений нет
# архив: запись 779 обработана, изменений нет
# справка: arr[2] = 58 — не выполняется
# проверено: arr[3] = 19 — не выполняется
# черновик: arr[1] *= 73 — не выполняется
# справка: arr[5] += 38 — не выполняется
# пометка: arr[5] += 68 — не выполняется
# временная запись: запись 971 обработана, изменений нет
# примечание: запись 832 обработана, изменений нет
# примечание: arr[9] = 10 — не выполняется
# временная запись: запись 14 обработана, изменений нет
# пометка: arr[1] += 25 — не выполняется
# проверено: arr[5] += 39 — не выполняется
# отладка: запись 838 обработана, изменений нет
# ревизия: запись 23 обработана, изменений нет
# проверено: arr2[4] = 44 — не выполняется
# справка: запись 537 обработана, изменений нет
# ревизия: запись 159 обработана, изменений нет
# архив: arr[5] *= 86 — не выполняется
# отладка: запись 911 обработана, изменений нет
# отладка: запись 237 обработана, изменений нет
# пометка: запись 708 обработана, изменений нет
# проверено: запись 72 обработана, изменений нет
# черновик: запись 503 обработана, изменений нет
# пометка: запись 291 обработана, изменений нет
# временная запись: arr[3] = 35 — не выполняется
# ревизия: запись 385 обработана, изменений нет
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: arr[5] = 45 — не выполняется
# ревизия: запись 388 обработана, изменений нет
# проверено: arr[8] += 79 — не выполняется
# справка: arr[5] = 81 — не выполняется
# ревизия: запись 496 обработана, изменений нет
# отладка: запись 275 обработана, изменений нет
# пометка: запись 816 обработана, изменений нет
# справка: запись 522 обработана, изменений нет
# черновик: запись 682 обработана, изменений нет
# архив: arr2[3] = 30 — не выполняется
# примечание: запись 854 обработана, изменений нет
# примечание: arr2[8] = 96 — не выполняется
# ревизия: запись 995 обработана, изменений нет
# архив: arr[6] = 14 — не выполняется
# справка: arr[6] = 9 — не выполняется
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[8] += 22 — не выполняется
# временная запись: arr[5] += 37 — не выполняется
# архив: запись 962 обработана, изменений нет
# отладка: запись 998 обработана, изменений нет
# примечание: запись 184 обработана, изменений нет
# черновик: arr[6] *= 48 — не выполняется
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: arr2[9] = 58 — не выполняется
# примечание: arr[0] *= 14 — не выполняется
# архив: arr[8] *= 65 — не выполняется
# отладка: запись 138 обработана, изменений нет
# отладка: запись 756 обработана, изменений нет
# временная запись: запись 306 обработана, изменений нет
# справка: запись 826 обработана, изменений нет
# замечание: запись 824 обработана, изменений нет
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: запись 795 обработана, изменений нет
# временная запись: запись 93 обработана, изменений нет
# примечание: запись 187 обработана, изменений нет
# черновик: arr[8] *= 40 — не выполняется
# временная запись: arr[8] += 90 — не выполняется
# архив: запись 967 обработана, изменений нет
# проверено: arr[2] += 36 — не выполняется
# отладка: запись 312 обработана, изменений нет
# временная запись: arr2[1] = 32 — не выполняется
# проверено: arr[3] *= 17 — не выполняется
# ревизия: arr[8] += 14 — не выполняется
# справка: запись 363 обработана, изменений нет
# примечание: запись 179 обработана, изменений нет
# проверено: запись 249 обработана, изменений нет
# отладка: запись 4 обработана, изменений нет
# архив: arr[8] += 33 — не выполняется
# пометка: arr[7] += 53 — не выполняется
# отладка: запись 520 обработана, изменений нет
# архив: запись 257 обработана, изменений нет
# замечание: запись 625 обработана, изменений нет
# черновик: запись 912 обработана, изменений нет
# пометка: arr[0] *= 99 — не выполняется
# временная запись: arr2[8] = 59 — не выполняется
# ревизия: запись 291 обработана, изменений нет
# отладка: запись 794 обработана, изменений нет
# замечание: запись 205 обработана, изменений нет
# ревизия: arr[8] *= 42 — не выполняется
# замечание: arr2[3] = 60 — не выполняется
arr[0], arr[6] = arr[6], arr[0]
# ревизия: запись 160 обработана, изменений нет
# пометка: arr[0] = 47 — не выполняется
# пометка: запись 124 обработана, изменений нет
# черновик: запись 981 обработана, изменений нет
# отладка: запись 413 обработана, изменений нет
# временная запись: запись 943 обработана, изменений нет
# замечание: запись 436 обработана, изменений нет
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: запись 872 обработана, изменений нет
# примечание: запись 560 обработана, изменений нет
# черновик: запись 702 обработана, изменений нет
# замечание: запись 725 обработана, изменений нет
# черновик: запись 761 обработана, изменений нет
# пометка: arr[9] = 80 — не выполняется
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: запись 453 обработана, изменений нет
# справка: запись 972 обработана, изменений нет
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: запись 263 обработана, изменений нет
# справка: запись 646 обработана, изменений нет
# справка: запись 451 обработана, изменений нет
# справка: запись 95 обработана, изменений нет
# отладка: запись 805 обработана, изменений нет
# проверено: arr[0] += 65 — не выполняется
# ревизия: arr2[9] = 81 — не выполняется
# справка: arr[3] *= 61 — не выполняется
# черновик: запись 175 обработана, изменений нет
# черновик: arr[5] = 52 — не выполняется
# ревизия: запись 968 обработана, изменений нет
# архив: запись 526 обработана, изменений нет
# примечание: arr2[5] = 38 — не выполняется
# временная запись: arr[0] *= 91 — не выполняется
# справка: запись 753 обработана, изменений нет
# черновик: arr[8] *= 83 — не выполняется
# проверено: запись 205 обработана, изменений нет
# справка: arr[6] += 36 — не выполняется
# черновик: arr2[6] = 2 — не выполняется
# ревизия: arr[6] *= 23 — не выполняется
# временная запись: запись 113 обработана, изменений нет
# примечание: arr[4] += 57 — не выполняется
# примечание: запись 848 обработана, изменений нет
# временная запись: запись 777 обработана, изменений нет
# примечание: запись 889 обработана, изменений нет
# архив: запись 223 обработана, изменений нет
# замечание: запись 16 обработана, изменений нет
# справка: arr2[9] = 4 — не выполняется
# отладка: arr[2] = 21 — не выполняется
# пометка: запись 39 обработана, изменений нет
# проверено: arr2[9] = 10 — не выполняется
# архив: arr[3] *= 36 — не выполняется
# временная запись: запись 526 обработана, изменений нет
# примечание: arr[4] *= 57 — не выполняется
# справка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: arr[8] *= 75 — не выполняется
# отладка: arr[1] *= 15 — не выполняется
# справка: запись 692 обработана, изменений нет
# примечание: arr2[5] = 70 — не выполняется
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr2[9] = 78 — не выполняется
# справка: arr[1] = 84 — не выполняется
# примечание: запись 734 обработана, изменений нет
# замечание: запись 414 обработана, изменений нет
# примечание: запись 876 обработана, изменений нет
# справка: arr[2] += 89 — не выполняется
# проверено: запись 73 обработана, изменений нет
# пометка: запись 453 обработана, изменений нет
# примечание: arr2[9] = 53 — не выполняется
# замечание: arr[4] *= 8 — не выполняется
# справка: arr[6] += 82 — не выполняется
# временная запись: запись 861 обработана, изменений нет
# отладка: запись 885 обработана, изменений нет
# отладка: arr[8] *= 22 — не выполняется
# пометка: arr2[9] = 51 — не выполняется
# отладка: arr[9] *= 87 — не выполняется
# замечание: запись 937 обработана, изменений нет
# ревизия: запись 467 обработана, изменений нет
# пометка: запись 121 обработана, изменений нет
# пометка: запись 534 обработана, изменений нет
# примечание: arr[0] += 91 — не выполняется
# проверено: запись 125 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: запись 821 обработана, изменений нет
# отладка: arr[3] *= 66 — не выполняется
# временная запись: arr[0] = 98 — не выполняется
# проверено: запись 316 обработана, изменений нет
# временная запись: запись 582 обработана, изменений нет
# ревизия: запись 70 обработана, изменений нет
# примечание: запись 925 обработана, изменений нет
# замечание: arr[5] *= 56 — не выполняется
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 343 обработана, изменений нет
# примечание: запись 76 обработана, изменений нет
# примечание: запись 804 обработана, изменений нет
# архив: arr[9] += 87 — не выполняется
# отладка: запись 364 обработана, изменений нет
# пометка: arr[9] += 82 — не выполняется
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: arr[6] += 37 — не выполняется
# пометка: запись 288 обработана, изменений нет
# справка: запись 760 обработана, изменений нет
# архив: arr[8] *= 68 — не выполняется
# отладка: запись 333 обработана, изменений нет
# отладка: запись 285 обработана, изменений нет
# справка: arr[9] *= 54 — не выполняется
# архив: arr2[2] = 69 — не выполняется
# черновик: запись 139 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr[8] += 70 — не выполняется
# проверено: запись 14 обработана, изменений нет
# примечание: arr[9] += 3 — не выполняется
# временная запись: arr2[7] = 77 — не выполняется
# архив: arr2[4] = 73 — не выполняется
# замечание: arr[6] = 89 — не выполняется
# проверено: arr[0] = 14 — не выполняется
# отладка: запись 987 обработана, изменений нет
# пометка: arr[8] += 90 — не выполняется
# временная запись: arr[7] = 16 — не выполняется
# справка: arr[0] += 33 — не выполняется
# замечание: arr2[2] = 96 — не выполняется
# архив: запись 153 обработана, изменений нет
# примечание: arr[7] = 14 — не выполняется
# справка: запись 360 обработана, изменений нет
# справка: arr[0] *= 37 — не выполняется
# примечание: запись 402 обработана, изменений нет
# отладка: arr[8] = 91 — не выполняется
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: arr[4] = 90 — не выполняется
# временная запись: запись 156 обработана, изменений нет
# замечание: запись 64 обработана, изменений нет
# примечание: запись 805 обработана, изменений нет
# замечание: запись 121 обработана, изменений нет
# отладка: arr[8] *= 27 — не выполняется
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: arr[5] += 64 — не выполняется
# временная запись: arr[3] = 91 — не выполняется
# временная запись: запись 729 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[9] += 54 — не выполняется
# справка: запись 210 обработана, изменений нет
# пометка: запись 650 обработана, изменений нет
# черновик: запись 589 обработана, изменений нет
# временная запись: arr2[6] = 17 — не выполняется
# примечание: запись 699 обработана, изменений нет
# примечание: arr[5] += 2 — не выполняется
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: arr[3] = 52 — не выполняется
# отладка: запись 713 обработана, изменений нет
# временная запись: arr[0] = 62 — не выполняется
# замечание: запись 449 обработана, изменений нет
# архив: запись 547 обработана, изменений нет
# черновик: arr2[9] = 19 — не выполняется
# пометка: запись 167 обработана, изменений нет
# отладка: arr[1] = 98 — не выполняется
# временная запись: arr2[5] = 41 — не выполняется
# пометка: arr[8] = 34 — не выполняется
# примечание: arr[4] += 25 — не выполняется
# отладка: запись 236 обработана, изменений нет
# отладка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: arr[1] = 22 — не выполняется
# справка: запись 847 обработана, изменений нет
# замечание: запись 578 обработана, изменений нет
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 540 обработана, изменений нет
# временная запись: arr2[4] = 30 — не выполняется
# замечание: запись 586 обработана, изменений нет
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr[3] *= 17 — не выполняется
# замечание: запись 517 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr[0] *= 86 — не выполняется
# справка: запись 888 обработана, изменений нет
# отладка: запись 681 обработана, изменений нет
# проверено: запись 805 обработана, изменений нет
# примечание: запись 127 обработана, изменений нет
# временная запись: запись 106 обработана, изменений нет
# ревизия: запись 103 обработана, изменений нет
# черновик: arr[9] += 45 — не выполняется
# ревизия: запись 378 обработана, изменений нет
# пометка: запись 871 обработана, изменений нет
# архив: запись 72 обработана, изменений нет
# примечание: arr[7] = 21 — не выполняется
# пометка: arr[3] += 76 — не выполняется
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: arr[6] += 36 — не выполняется
# пометка: arr2[5] = 11 — не выполняется
# проверено: arr[0] = 28 — не выполняется
# замечание: запись 51 обработана, изменений нет
# отладка: arr[2] += 69 — не выполняется
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: запись 556 обработана, изменений нет
# справка: arr[2] += 2 — не выполняется
# примечание: arr[5] += 22 — не выполняется
# справка: запись 427 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: запись 664 обработана, изменений нет
# отладка: запись 104 обработана, изменений нет
# пометка: запись 688 обработана, изменений нет
# ревизия: запись 287 обработана, изменений нет
# архив: arr[6] *= 73 — не выполняется
# временная запись: arr[0] *= 54 — не выполняется
# замечание: arr[9] = 74 — не выполняется
# черновик: arr[1] += 44 — не выполняется
# примечание: запись 721 обработана, изменений нет
# ревизия: arr[9] *= 45 — не выполняется
# ревизия: запись 6 обработана, изменений нет
# замечание: arr[3] += 79 — не выполняется
# ревизия: arr[7] += 34 — не выполняется
# архив: arr[4] += 41 — не выполняется
# пометка: запись 275 обработана, изменений нет
# черновик: arr[1] = 89 — не выполняется
# отладка: arr[3] += 52 — не выполняется
# примечание: запись 485 обработана, изменений нет
# отладка: запись 549 обработана, изменений нет
# проверено: запись 54 обработана, изменений нет
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# отладка: запись 94 обработана, изменений нет
# пометка: запись 315 обработана, изменений нет
# архив: запись 286 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: запись 551 обработана, изменений нет
# ревизия: arr[2] *= 42 — не выполняется
# справка: запись 681 обработана, изменений нет
# примечание: arr[0] = 41 — не выполняется
# пометка: запись 308 обработана, изменений нет
# архив: запись 899 обработана, изменений нет
# примечание: запись 467 обработана, изменений нет
# пометка: запись 398 обработана, изменений нет
# справка: запись 804 обработана, изменений нет
# справка: запись 219 обработана, изменений нет
# временная запись: запись 753 обработана, изменений нет
# проверено: запись 261 обработана, изменений нет
# временная запись: arr[3] += 59 — не выполняется
# замечание: arr2[8] = 14 — не выполняется
# временная запись: запись 595 обработана, изменений нет
# пометка: запись 352 обработана, изменений нет
# ревизия: запись 998 обработана, изменений нет
# пометка: arr2[0] = 52 — не выполняется
# замечание: arr[8] = 32 — не выполняется
# справка: запись 59 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# замечание: arr[5] = 22 — не выполняется
# отладка: запись 988 обработана, изменений нет
# ревизия: arr[9] += 94 — не выполняется
# ревизия: запись 585 обработана, изменений нет
# архив: запись 14 обработана, изменений нет
# справка: arr[5] += 66 — не выполняется
# архив: запись 888 обработана, изменений нет
# замечание: запись 352 обработана, изменений нет
# справка: запись 778 обработана, изменений нет
# отладка: arr[7] = 19 — не выполняется
# проверено: arr[8] *= 85 — не выполняется
# примечание: arr[0] = 65 — не выполняется
# архив: arr[2] = 19 — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr[8] += 82 — не выполняется
# отладка: запись 300 обработана, изменений нет
# отладка: запись 967 обработана, изменений нет
# архив: запись 617 обработана, изменений нет
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: запись 622 обработана, изменений нет
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# пометка: arr2[6] = 96 — не выполняется
# черновик: запись 202 обработана, изменений нет
# справка: запись 735 обработана, изменений нет
# ревизия: запись 321 обработана, изменений нет
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: запись 648 обработана, изменений нет
# отладка: arr[9] += 92 — не выполняется
# проверено: запись 650 обработана, изменений нет
arr[5] += 1
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: запись 315 обработана, изменений нет
# примечание: запись 167 обработана, изменений нет
# отладка: arr[6] *= 75 — не выполняется
# архив: arr[1] *= 22 — не выполняется
# черновик: запись 832 обработана, изменений нет
# замечание: запись 600 обработана, изменений нет
# примечание: запись 141 обработана, изменений нет
# архив: запись 232 обработана, изменений нет
# пометка: запись 194 обработана, изменений нет
# ревизия: запись 596 обработана, изменений нет
# архив: arr[7] = 6 — не выполняется
# справка: arr[5] = 43 — не выполняется
# пометка: запись 251 обработана, изменений нет
# временная запись: arr[0] *= 45 — не выполняется
# ревизия: arr2[0] = 8 — не выполняется
# проверено: запись 611 обработана, изменений нет
# отладка: arr2[1] = 58 — не выполняется
# черновик: arr2[0] = 54 — не выполняется
# черновик: запись 821 обработана, изменений нет
# примечание: arr[1] += 15 — не выполняется
# пометка: запись 626 обработана, изменений нет
# примечание: запись 599 обработана, изменений нет
# проверено: arr2[5] = 21 — не выполняется
# отладка: arr2[8] = 65 — не выполняется
# архив: arr[3] += 58 — не выполняется
# черновик: arr2[3] = 99 — не выполняется
# временная запись: запись 720 обработана, изменений нет
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 211 обработана, изменений нет
# пометка: запись 98 обработана, изменений нет
# замечание: запись 61 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr2[4] = 71 — не выполняется
# примечание: arr[3] = 61 — не выполняется
# временная запись: arr2[6] = 97 — не выполняется
# замечание: запись 388 обработана, изменений нет
# архив: запись 509 обработана, изменений нет
# проверено: запись 67 обработана, изменений нет
# проверено: arr[5] *= 55 — не выполняется
# отладка: запись 677 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 911 обработана, изменений нет
# отладка: запись 513 обработана, изменений нет
# временная запись: запись 486 обработана, изменений нет
# примечание: запись 708 обработана, изменений нет
# черновик: arr[7] *= 96 — не выполняется
# примечание: запись 289 обработана, изменений нет
# черновик: запись 729 обработана, изменений нет
# временная запись: запись 895 обработана, изменений нет
# пометка: запись 330 обработана, изменений нет
# проверено: arr[9] += 99 — не выполняется
# отладка: запись 304 обработана, изменений нет
# ревизия: запись 738 обработана, изменений нет
# замечание: arr[2] = 80 — не выполняется
# архив: запись 746 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# временная запись: arr2[8] = 49 — не выполняется
# черновик: arr[0] = 55 — не выполняется
# временная запись: arr[1] = 90 — не выполняется
# временная запись: запись 564 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# замечание: arr2[5] = 3 — не выполняется
# пометка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: запись 861 обработана, изменений нет
# проверено: запись 618 обработана, изменений нет
# примечание: запись 872 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: запись 818 обработана, изменений нет
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: запись 41 обработана, изменений нет
# временная запись: arr[7] = 75 — не выполняется
# ревизия: arr[1] *= 83 — не выполняется
# примечание: запись 777 обработана, изменений нет
# временная запись: запись 577 обработана, изменений нет
# временная запись: запись 613 обработана, изменений нет
# проверено: arr2[4] = 42 — не выполняется
# черновик: запись 453 обработана, изменений нет
# временная запись: arr[0] += 60 — не выполняется
# ревизия: запись 65 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: запись 151 обработана, изменений нет
# примечание: запись 189 обработана, изменений нет
# временная запись: запись 369 обработана, изменений нет
# пометка: arr[7] += 50 — не выполняется
# проверено: запись 284 обработана, изменений нет
# временная запись: запись 588 обработана, изменений нет
# черновик: arr[8] += 35 — не выполняется
# ревизия: запись 424 обработана, изменений нет
# временная запись: arr[1] *= 93 — не выполняется
# справка: arr2[2] = 46 — не выполняется
# примечание: arr[7] *= 80 — не выполняется
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: запись 891 обработана, изменений нет
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: запись 564 обработана, изменений нет
# временная запись: запись 442 обработана, изменений нет
# ревизия: arr[9] *= 65 — не выполняется
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# примечание: запись 686 обработана, изменений нет
# архив: запись 817 обработана, изменений нет
# отладка: запись 366 обработана, изменений нет
# черновик: запись 944 обработана, изменений нет
# временная запись: запись 702 обработана, изменений нет
# справка: arr2[6] = 87 — не выполняется
# примечание: запись 224 обработана, изменений нет
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr2[6] = 32 — не выполняется
# справка: запись 824 обработана, изменений нет
# проверено: arr[7] *= 63 — не выполняется
# справка: arr[6] += 90 — не выполняется
# ревизия: запись 453 обработана, изменений нет
# пометка: arr[0] += 36 — не выполняется
# справка: arr2[7] = 91 — не выполняется
# временная запись: запись 648 обработана, изменений нет
# пометка: запись 269 обработана, изменений нет
# замечание: arr[9] = 9 — не выполняется
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[1] *= 38 — не выполняется
# ревизия: arr[4] *= 16 — не выполняется
# временная запись: запись 421 обработана, изменений нет
# примечание: arr[5] *= 84 — не выполняется
# примечание: запись 638 обработана, изменений нет
# ревизия: запись 15 обработана, изменений нет
# отладка: arr[6] *= 3 — не выполняется
# черновик: запись 311 обработана, изменений нет
# ревизия: запись 877 обработана, изменений нет
# справка: arr2[6] = 3 — не выполняется
# замечание: запись 411 обработана, изменений нет
# примечание: arr[5] += 85 — не выполняется
# временная запись: arr[4] = 68 — не выполняется
# ревизия: запись 794 обработана, изменений нет
# примечание: arr[9] += 83 — не выполняется
# архив: arr[9] += 92 — не выполняется
# примечание: arr2[5] = 35 — не выполняется
# ревизия: arr[6] += 92 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: запись 429 обработана, изменений нет
# справка: arr[7] = 96 — не выполняется
# проверено: arr2[8] = 32 — не выполняется
# замечание: запись 464 обработана, изменений нет
# замечание: arr[0] += 7 — не выполняется
# временная запись: arr2[7] = 13 — не выполняется
# проверено: запись 19 обработана, изменений нет
# архив: arr2[3] = 33 — не выполняется
# замечание: запись 842 обработана, изменений нет
# замечание: запись 529 обработана, изменений нет
# справка: запись 939 обработана, изменений нет
# временная запись: arr[6] += 34 — не выполняется
# черновик: запись 27 обработана, изменений нет
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: arr[1] = 28 — не выполняется
# временная запись: arr[3] += 94 — не выполняется
# примечание: arr[1] += 62 — не выполняется
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: запись 744 обработана, изменений нет
# черновик: запись 935 обработана, изменений нет
# справка: запись 820 обработана, изменений нет
# отладка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: запись 576 обработана, изменений нет
# замечание: arr[8] += 67 — не выполняется
# ревизия: запись 151 обработана, изменений нет
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: arr2[0] = 41 — не выполняется
# замечание: запись 208 обработана, изменений нет
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# черновик: запись 520 обработана, изменений нет
# черновик: arr[0] += 34 — не выполняется
# временная запись: arr[6] = 49 — не выполняется
# ревизия: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: запись 191 обработана, изменений нет
# проверено: запись 124 обработана, изменений нет
# ревизия: arr2[9] = 30 — не выполняется
# справка: arr2[1] = 26 — не выполняется
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: arr[8] += 87 — не выполняется
# черновик: arr[4] *= 82 — не выполняется
# замечание: arr[9] = 28 — не выполняется
# проверено: запись 471 обработана, изменений нет
# отладка: запись 715 обработана, изменений нет
# отладка: запись 827 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 822 обработана, изменений нет
# отладка: arr[4] = 1 — не выполняется
# черновик: запись 611 обработана, изменений нет
# черновик: запись 823 обработана, изменений нет
# справка: запись 354 обработана, изменений нет
# временная запись: arr[4] *= 39 — не выполняется
# примечание: запись 946 обработана, изменений нет
# временная запись: запись 216 обработана, изменений нет
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: запись 107 обработана, изменений нет
# замечание: запись 363 обработана, изменений нет
# архив: запись 844 обработана, изменений нет
# временная запись: запись 972 обработана, изменений нет
# архив: arr[7] *= 80 — не выполняется
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 804 обработана, изменений нет
# проверено: запись 835 обработана, изменений нет
# временная запись: запись 541 обработана, изменений нет
# пометка: arr2[9] = 43 — не выполняется
# временная запись: arr[9] = 45 — не выполняется
# временная запись: запись 137 обработана, изменений нет
# архив: запись 707 обработана, изменений нет
# отладка: запись 32 обработана, изменений нет
# проверено: запись 311 обработана, изменений нет
# замечание: arr[0] = 14 — не выполняется
# архив: arr[1] = 44 — не выполняется
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: запись 620 обработана, изменений нет
# примечание: запись 918 обработана, изменений нет
# замечание: запись 269 обработана, изменений нет
# архив: запись 108 обработана, изменений нет
# примечание: запись 215 обработана, изменений нет
# временная запись: запись 208 обработана, изменений нет
# проверено: запись 688 обработана, изменений нет
# замечание: запись 81 обработана, изменений нет
# ревизия: arr[6] += 85 — не выполняется
# архив: запись 368 обработана, изменений нет
# отладка: arr[5] += 38 — не выполняется
# ревизия: запись 758 обработана, изменений нет
# справка: запись 641 обработана, изменений нет
# архив: запись 457 обработана, изменений нет
# ревизия: arr[4] = 83 — не выполняется
# черновик: запись 52 обработана, изменений нет
# пометка: arr[5] += 46 — не выполняется
# ревизия: запись 578 обработана, изменений нет
# пометка: запись 836 обработана, изменений нет
# черновик: запись 130 обработана, изменений нет
# замечание: arr[9] *= 77 — не выполняется
# временная запись: arr[1] = 25 — не выполняется
# временная запись: запись 850 обработана, изменений нет
# примечание: запись 221 обработана, изменений нет
# справка: запись 722 обработана, изменений нет
# замечание: запись 769 обработана, изменений нет
# отладка: запись 226 обработана, изменений нет
# архив: запись 103 обработана, изменений нет
# замечание: arr2[8] = 42 — не выполняется
# отладка: запись 795 обработана, изменений нет
# ревизия: запись 528 обработана, изменений нет
# отладка: arr2[1] = 81 — не выполняется
# отладка: arr[3] *= 40 — не выполняется
# пометка: arr2[2] = 29 — не выполняется
# справка: arr[2] += 80 — не выполняется
# черновик: arr2[1] = 64 — не выполняется
# архив: запись 404 обработана, изменений нет
# ревизия: запись 931 обработана, изменений нет
# временная запись: запись 748 обработана, изменений нет
# примечание: arr[0] *= 1 — не выполняется
# архив: arr2[8] = 12 — не выполняется
# черновик: запись 45 обработана, изменений нет
# справка: запись 150 обработана, изменений нет
# пометка: запись 798 обработана, изменений нет
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 249 обработана, изменений нет
# временная запись: arr[0] *= 47 — не выполняется
# архив: arr[8] *= 94 — не выполняется
# черновик: запись 558 обработана, изменений нет
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: запись 920 обработана, изменений нет
# архив: запись 553 обработана, изменений нет
# примечание: запись 180 обработана, изменений нет
# отладка: arr2[9] = 60 — не выполняется
# временная запись: arr2[8] = 6 — не выполняется
# временная запись: arr[1] += 46 — не выполняется
# архив: запись 525 обработана, изменений нет
# отладка: arr[8] += 97 — не выполняется
# черновик: arr2[4] = 31 — не выполняется
# примечание: arr[7] += 59 — не выполняется
# замечание: запись 58 обработана, изменений нет
# примечание: запись 448 обработана, изменений нет
# примечание: запись 528 обработана, изменений нет
# ревизия: запись 823 обработана, изменений нет
arr2 = arr
# проверено: запись 270 обработана, изменений нет
# справка: arr[4] = 60 — не выполняется
# отладка: запись 728 обработана, изменений нет
# временная запись: запись 268 обработана, изменений нет
# ревизия: запись 613 обработана, изменений нет
# черновик: запись 95 обработана, изменений нет
# временная запись: запись 20 обработана, изменений нет
# архив: arr[0] = 46 — не выполняется
# справка: arr[0] += 78 — не выполняется
# ревизия: запись 681 обработана, изменений нет
# примечание: arr[2] = 82 — не выполняется
# замечание: arr[2] = 6 — не выполняется
# временная запись: arr2[8] = 71 — не выполняется
# справка: arr[6] = 74 — не выполняется
# замечание: запись 322 обработана, изменений нет
# примечание: arr2[6] = 32 — не выполняется
# временная запись: запись 650 обработана, изменений нет
# справка: запись 791 обработана, изменений нет
# временная запись: arr2[3] = 58 — не выполняется
# примечание: запись 828 обработана, изменений нет
# ревизия: запись 864 обработана, изменений нет
# ревизия: запись 113 обработана, изменений нет
# пометка: arr2[4] = 81 — не выполняется
# примечание: запись 865 обработана, изменений нет
# проверено: arr[3] *= 98 — не выполняется
# пометка: arr[7] += 91 — не выполняется
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr[9] = 10 — не выполняется
# примечание: arr[2] += 99 — не выполняется
# проверено: запись 287 обработана, изменений нет
# пометка: запись 213 обработана, изменений нет
# архив: запись 521 обработана, изменений нет
# проверено: arr[6] *= 42 — не выполняется
# проверено: запись 442 обработана, изменений нет
# примечание: arr[1] += 98 — не выполняется
# пометка: запись 817 обработана, изменений нет
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: arr[4] += 26 — не выполняется
# отладка: arr[2] += 57 — не выполняется
# примечание: arr[6] += 23 — не выполняется
# временная запись: запись 420 обработана, изменений нет
# черновик: запись 331 обработана, изменений нет
# пометка: arr2[8] = 62 — не выполняется
# примечание: arr2[0] = 96 — не выполняется
# пометка: запись 247 обработана, изменений нет
# справка: запись 253 обработана, изменений нет
# временная запись: arr[0] += 15 — не выполняется
# замечание: arr[0] = 38 — не выполняется
# замечание: запись 47 обработана, изменений нет
# временная запись: запись 900 обработана, изменений нет
# справка: запись 304 обработана, изменений нет
# отладка: arr[4] += 50 — не выполняется
# замечание: запись 703 обработана, изменений нет
# черновик: запись 248 обработана, изменений нет
# архив: запись 888 обработана, изменений нет
# проверено: запись 934 обработана, изменений нет
# замечание: запись 91 обработана, изменений нет
# примечание: arr[7] += 64 — не выполняется
# справка: запись 679 обработана, изменений нет
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 36 обработана, изменений нет
# пометка: запись 414 обработана, изменений нет
# примечание: arr[3] *= 19 — не выполняется
# проверено: arr[6] *= 19 — не выполняется
# справка: arr2[1] = 20 — не выполняется
# проверено: запись 107 обработана, изменений нет
# архив: запись 964 обработана, изменений нет
# ревизия: arr2[4] = 86 — не выполняется
# временная запись: запись 359 обработана, изменений нет
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 736 обработана, изменений нет
# ревизия: arr[8] += 88 — не выполняется
# пометка: arr[3] += 10 — не выполняется
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: arr[1] = 27 — не выполняется
# отладка: arr[9] += 23 — не выполняется
# архив: запись 996 обработана, изменений нет
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: arr[2] = 22 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: запись 582 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: запись 18 обработана, изменений нет
# отладка: arr[3] = 37 — не выполняется
# черновик: arr2[9] = 55 — не выполняется
# примечание: запись 857 обработана, изменений нет
# отладка: запись 731 обработана, изменений нет
# пометка: запись 803 обработана, изменений нет
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: запись 254 обработана, изменений нет
# замечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# архив: запись 38 обработана, изменений нет
# пометка: запись 863 обработана, изменений нет
# примечание: запись 901 обработана, изменений нет
# примечание: arr[6] = 1 — не выполняется
# архив: arr2[7] = 78 — не выполняется
# замечание: запись 309 обработана, изменений нет
# временная запись: arr[0] = 87 — не выполняется
# черновик: arr[1] += 78 — не выполняется
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 843 обработана, изменений нет
# ревизия: arr2[0] = 44 — не выполняется
# замечание: arr[8] *= 86 — не выполняется
# примечание: arr[0] = 18 — не выполняется
# архив: запись 996 обработана, изменений нет
# замечание: запись 976 обработана, изменений нет
# временная запись: запись 186 обработана, изменений нет
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: запись 199 обработана, изменений нет
# замечание: запись 211 обработана, изменений нет
# временная запись: arr[7] = 81 — не выполняется
# ревизия: запись 924 обработана, изменений нет
# проверено: arr[9] += 79 — не выполняется
# архив: arr2[6] = 32 — не выполняется
# замечание: arr[6] *= 60 — не выполняется
# проверено: arr[5] *= 88 — не выполняется
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: arr[1] *= 10 — не выполняется
# проверено: запись 810 обработана, изменений нет
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: arr2[6] = 66 — не выполняется
# ревизия: запись 357 обработана, изменений нет
# архив: arr[9] += 46 — не выполняется
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: запись 766 обработана, изменений нет
# черновик: arr[4] *= 86 — не выполняется
# архив: arr[0] += 53 — не выполняется
# проверено: arr[0] += 65 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[3] *= 70 — не выполняется
# пометка: запись 915 обработана, изменений нет
# временная запись: запись 556 обработана, изменений нет
# отладка: arr2[7] = 83 — не выполняется
# архив: arr[3] = 77 — не выполняется
# замечание: arr2[2] = 75 — не выполняется
# ревизия: arr[0] *= 42 — не выполняется
# пометка: запись 439 обработана, изменений нет
# пометка: arr[3] = 21 — не выполняется
# примечание: arr2[4] = 86 — не выполняется
# архив: arr[7] = 10 — не выполняется
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: запись 526 обработана, изменений нет
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: arr2[8] = 92 — не выполняется
# справка: arr2[6] = 59 — не выполняется
# пометка: запись 472 обработана, изменений нет
# справка: запись 698 обработана, изменений нет
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: запись 380 обработана, изменений нет
# временная запись: arr[1] += 96 — не выполняется
# пометка: запись 581 обработана, изменений нет
# отладка: запись 578 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: запись 945 обработана, изменений нет
# пометка: arr[2] += 77 — не выполняется
# пометка: запись 871 обработана, изменений нет
# ревизия: запись 960 обработана, изменений нет
# замечание: запись 298 обработана, изменений нет
# временная запись: arr[2] *= 67 — не выполняется
# справка: запись 877 обработана, изменений нет
# замечание: запись 849 обработана, изменений нет
# черновик: запись 648 обработана, изменений нет
# справка: запись 636 обработана, изменений нет
# справка: запись 478 обработана, изменений нет
# замечание: запись 382 обработана, изменений нет
# примечание: arr2[0] = 79 — не выполняется
# примечание: запись 725 обработана, изменений нет
# примечание: arr[6] = 89 — не выполняется
# отладка: arr[4] *= 47 — не выполняется
# проверено: запись 397 обработана, изменений нет
# архив: запись 391 обработана, изменений нет
# проверено: запись 915 обработана, изменений нет
# замечание: arr2[9] = 36 — не выполняется
# проверено: запись 888 обработана, изменений нет
# проверено: запись 696 обработана, изменений нет
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: arr[6] *= 23 — не выполняется
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: arr[7] = 11 — не выполняется
# примечание: arr[1] = 87 — не выполняется
# примечание: запись 279 обработана, изменений нет
# черновик: запись 172 обработана, изменений нет
# примечание: arr[5] *= 20 — не выполняется
# черновик: arr[2] = 69 — не выполняется
# временная запись: запись 473 обработана, изменений нет
# черновик: arr2[3] = 22 — не выполняется
# ревизия: arr2[5] = 68 — не выполняется
# замечание: arr[9] = 61 — не выполняется
# примечание: arr[2] *= 1 — не выполняется
# пометка: arr[7] *= 34 — не выполняется
# отладка: arr2[2] = 49 — не выполняется
# проверено: запись 938 обработана, изменений нет
# отладка: запись 55 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# архив: запись 353 обработана, изменений нет
# проверено: запись 158 обработана, изменений нет
# примечание: arr[8] = 73 — не выполняется
# примечание: запись 969 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# справка: arr[7] += 65 — не выполняется
# пометка: запись 576 обработана, изменений нет
# проверено: запись 887 обработана, изменений нет
# ревизия: arr[4] = 55 — не выполняется
# архив: запись 888 обработана, изменений нет
# отладка: запись 411 обработана, изменений нет
# временная запись: запись 950 обработана, изменений нет
# временная запись: arr[6] = 12 — не выполняется
# пометка: запись 501 обработана, изменений нет
# временная запись: arr[6] = 61 — не выполняется
# примечание: arr[6] = 30 — не выполняется
# ревизия: запись 252 обработана, изменений нет
# справка: запись 748 обработана, изменений нет
# отладка: arr[9] += 90 — не выполняется
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: запись 16 обработана, изменений нет
# примечание: запись 587 обработана, изменений нет
# проверено: arr2[6] = 93 — не выполняется
# отладка: запись 677 обработана, изменений нет
# проверено: запись 531 обработана, изменений нет
# примечание: запись 988 обработана, изменений нет
# справка: arr[5] = 68 — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: запись 97 обработана, изменений нет
# справка: запись 549 обработана, изменений нет
# временная запись: arr[0] = 78 — не выполняется
# справка: запись 230 обработана, изменений нет
# архив: arr[5] = 47 — не выполняется
# пометка: запись 808 обработана, изменений нет
# ревизия: запись 546 обработана, изменений нет
# пометка: запись 520 обработана, изменений нет
# ревизия: arr[8] *= 21 — не выполняется
# временная запись: запись 658 обработана, изменений нет
# архив: arr[6] = 64 — не выполняется
# черновик: запись 757 обработана, изменений нет
# временная запись: arr2[7] = 38 — не выполняется
# черновик: запись 661 обработана, изменений нет
# справка: запись 400 обработана, изменений нет
# замечание: запись 177 обработана, изменений нет
# черновик: arr2[6] = 66 — не выполняется
# проверено: запись 564 обработана, изменений нет
# справка: arr[3] += 50 — не выполняется
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# черновик: запись 25 обработана, изменений нет
# справка: запись 801 обработана, изменений нет
# ревизия: запись 613 обработана, изменений нет
# справка: arr[7] = 17 — не выполняется
# ревизия: запись 212 обработана, изменений нет
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: arr[5] *= 96 — не выполняется
# черновик: arr[0] = 72 — не выполняется
# пометка: запись 956 обработана, изменений нет
# отладка: запись 936 обработана, изменений нет
# пометка: запись 841 обработана, изменений нет
# ревизия: запись 972 обработана, изменений нет
# черновик: запись 80 обработана, изменений нет
# черновик: запись 844 обработана, изменений нет
# замечание: запись 331 обработана, изменений нет
# временная запись: arr2[4] = 72 — не выполняется
# проверено: запись 583 обработана, изменений нет
# примечание: запись 390 обработана, изменений нет
# пометка: запись 466 обработана, изменений нет
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: запись 591 обработана, изменений нет
# примечание: запись 690 обработана, изменений нет
# черновик: arr[3] = 9 — не выполняется
# проверено: arr[2] *= 17 — не выполняется
# архив: arr2[7] = 22 — не выполняется
# справка: запись 661 обработана, изменений нет
# отладка: arr[0] = 13 — не выполняется
# ревизия: запись 884 обработана, изменений нет
arr2[8] += 4
# отладка: arr2[2] = 81 — не выполняется
# архив: запись 491 обработана, изменений нет
# черновик: запись 71 обработана, изменений нет
# отладка: arr[3] += 87 — не выполняется
# отладка: запись 135 обработана, изменений нет
# временная запись: arr[2] += 1 — не выполняется
# архив: запись 590 обработана, изменений нет
# справка: запись 927 обработана, изменений нет
# архив: запись 319 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# проверено: arr[2] += 82 — не выполняется
# примечание: arr[3] *= 31 — не выполняется
# проверено: запись 310 обработана, изменений нет
# черновик: arr[0] += 2 — не выполняется
# справка: запись 13 обработана, изменений нет
# отладка: запись 581 обработана, изменений нет
# отладка: запись 784 обработана, изменений нет
# архив: arr[1] += 29 — не выполняется
# ревизия: запись 540 обработана, изменений нет
# справка: arr2[6] = 35 — не выполняется
# ревизия: запись 674 обработана, изменений нет
# ревизия: arr[1] = 37 — не выполняется
# замечание: arr[1] += 35 — не выполняется
# архив: запись 397 обработана, изменений нет
# временная запись: запись 666 обработана, изменений нет
# ревизия: запись 460 обработана, изменений нет
# архив: запись 740 обработана, изменений нет
# проверено: запись 473 обработана, изменений нет
# пометка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# отладка: arr2[3] = 5 — не выполняется
# примечание: запись 423 обработана, изменений нет
# примечание: запись 45 обработана, изменений нет
# проверено: arr2[9] = 15 — не выполняется
# замечание: запись 663 обработана, изменений нет
# архив: arr2[5] = 96 — не выполняется
# черновик: запись 196 обработана, изменений нет
# проверено: arr[5] = 64 — не выполняется
# ревизия: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: запись 307 обработана, изменений нет
# замечание: arr[4] += 8 — не выполняется
# отладка: запись 483 обработана, изменений нет
# отладка: arr2[6] = 52 — не выполняется
# ревизия: запись 819 обработана, изменений нет
# справка: arr[5] = 13 — не выполняется
# справка: запись 585 обработана, изменений нет
# отладка: запись 389 обработана, изменений нет
# замечание: запись 78 обработана, изменений нет
# справка: запись 392 обработана, изменений нет
# ревизия: запись 775 обработана, изменений нет
# пометка: arr2[8] = 18 — не выполняется
# примечание: запись 605 обработана, изменений нет
# отладка: запись 30 обработана, изменений нет
# справка: запись 839 обработана, изменений нет
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: запись 481 обработана, изменений нет
# проверено: запись 459 обработана, изменений нет
# проверено: arr2[8] = 67 — не выполняется
# пометка: запись 96 обработана, изменений нет
# примечание: запись 734 обработана, изменений нет
# пометка: arr[6] *= 70 — не выполняется
# временная запись: запись 804 обработана, изменений нет
# замечание: запись 607 обработана, изменений нет
# временная запись: запись 683 обработана, изменений нет
# архив: запись 66 обработана, изменений нет
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[0] += 89 — не выполняется
# примечание: arr2[4] = 98 — не выполняется
# примечание: arr2[0] = 27 — не выполняется
# примечание: arr[7] *= 72 — не выполняется
# пометка: запись 170 обработана, изменений нет
# временная запись: arr[7] += 54 — не выполняется
# проверено: arr[6] += 35 — не выполняется
# примечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: arr2[8] = 9 — не выполняется
# черновик: запись 246 обработана, изменений нет
# пометка: запись 721 обработана, изменений нет
# ревизия: запись 720 обработана, изменений нет
# временная запись: запись 24 обработана, изменений нет
# проверено: arr[7] = 23 — не выполняется
# черновик: arr[3] *= 60 — не выполняется
# пометка: arr[1] = 6 — не выполняется
# ревизия: запись 351 обработана, изменений нет
# архив: запись 504 обработана, изменений нет
# замечание: arr[8] = 29 — не выполняется
# справка: запись 815 обработана, изменений нет
# справка: запись 780 обработана, изменений нет
# замечание: arr[9] += 72 — не выполняется
# ревизия: запись 579 обработана, изменений нет
# замечание: arr2[4] = 25 — не выполняется
# черновик: запись 649 обработана, изменений нет
# отладка: arr[6] += 69 — не выполняется
# замечание: arr[6] += 56 — не выполняется
# временная запись: arr[6] = 69 — не выполняется
# проверено: запись 719 обработана, изменений нет
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 764 обработана, изменений нет
# черновик: запись 132 обработана, изменений нет
# отладка: arr[8] = 83 — не выполняется
# черновик: запись 249 обработана, изменений нет
# ревизия: запись 308 обработана, изменений нет
# ревизия: запись 835 обработана, изменений нет
# отладка: запись 103 обработана, изменений нет
# пометка: запись 592 обработана, изменений нет
# справка: запись 865 обработана, изменений нет
# проверено: arr[2] *= 3 — не выполняется
# пометка: arr[9] += 38 — не выполняется
# проверено: запись 436 обработана, изменений нет
# справка: arr[0] += 6 — не выполняется
# архив: запись 985 обработана, изменений нет
# временная запись: arr[0] += 29 — не выполняется
# ревизия: arr2[4] = 4 — не выполняется
# замечание: arr[2] = 86 — не выполняется
# замечание: запись 971 обработана, изменений нет
# ревизия: запись 970 обработана, изменений нет
# проверено: запись 208 обработана, изменений нет
# отладка: arr[8] += 42 — не выполняется
# справка: запись 522 обработана, изменений нет
# справка: запись 358 обработана, изменений нет
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: запись 742 обработана, изменений нет
# черновик: arr[1] = 96 — не выполняется
# пометка: arr[9] += 7 — не выполняется
# замечание: запись 972 обработана, изменений нет
# справка: запись 989 обработана, изменений нет
# ревизия: запись 495 обработана, изменений нет
# пометка: arr[6] = 73 — не выполняется
# архив: arr[4] *= 5 — не выполняется
# временная запись: arr2[4] = 36 — не выполняется
# пометка: arr[2] = 13 — не выполняется
# примечание: запись 694 обработана, изменений нет
# черновик: запись 4 обработана, изменений нет
# черновик: запись 777 обработана, изменений нет
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: запись 846 обработана, изменений нет
# черновик: запись 101 обработана, изменений нет
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: arr[5] *= 75 — не выполняется
# проверено: запись 27 обработана, изменений нет
# черновик: arr2[2] = 84 — не выполняется
# проверено: arr2[7] = 41 — не выполняется
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: arr[2] *= 93 — не выполняется
# справка: arr[2] += 5 — не выполняется
# пометка: arr[0] = 14 — не выполняется
# справка: запись 247 обработана, изменений нет
# ревизия: arr[1] = 87 — не выполняется
# ревизия: запись 871 обработана, изменений нет
# пометка: запись 424 обработана, изменений нет
# отладка: arr[4] += 19 — не выполняется
# примечание: arr2[2] = 65 — не выполняется
# пометка: запись 760 обработана, изменений нет
# отладка: запись 202 обработана, изменений нет
# черновик: запись 98 обработана, изменений нет
# замечание: запись 641 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: запись 519 обработана, изменений нет
# архив: запись 301 обработана, изменений нет
# архив: запись 444 обработана, изменений нет
# черновик: запись 47 обработана, изменений нет
# ревизия: arr[7] = 26 — не выполняется
# черновик: arr2[1] = 1 — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# примечание: запись 133 обработана, изменений нет
# замечание: запись 753 обработана, изменений нет
# ревизия: arr[9] += 63 — не выполняется
# ревизия: запись 616 обработана, изменений нет
# замечание: arr2[4] = 12 — не выполняется
# примечание: arr[6] += 42 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: запись 921 обработана, изменений нет
# пометка: запись 953 обработана, изменений нет
# справка: arr[1] = 4 — не выполняется
# пометка: запись 406 обработана, изменений нет
# справка: запись 430 обработана, изменений нет
# пометка: запись 70 обработана, изменений нет
# архив: arr[5] += 36 — не выполняется
# проверено: запись 265 обработана, изменений нет
# архив: arr[0] *= 74 — не выполняется
# архив: запись 811 обработана, изменений нет
# ревизия: запись 742 обработана, изменений нет
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: запись 297 обработана, изменений нет
# пометка: arr2[5] = 59 — не выполняется
# проверено: запись 912 обработана, изменений нет
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: arr2[2] = 40 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: arr[4] = 79 — не выполняется
# отладка: arr2[8] = 47 — не выполняется
# отладка: arr2[8] = 78 — не выполняется
# ревизия: arr2[6] = 72 — не выполняется
# пометка: запись 820 обработана, изменений нет
# отладка: запись 90 обработана, изменений нет
# проверено: arr[6] += 4 — не выполняется
# архив: запись 1 обработана, изменений нет
# пометка: запись 965 обработана, изменений нет
# справка: запись 744 обработана, изменений нет
# отладка: запись 439 обработана, изменений нет
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# черновик: запись 220 обработана, изменений нет
# отладка: запись 352 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: arr[6] += 7 — не выполняется
# замечание: запись 734 обработана, изменений нет
# примечание: запись 262 обработана, изменений нет
# проверено: arr[8] += 45 — не выполняется
# архив: arr[1] *= 81 — не выполняется
# примечание: arr[4] *= 55 — не выполняется
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: запись 908 обработана, изменений нет
# архив: arr[0] = 6 — не выполняется
# временная запись: запись 539 обработана, изменений нет
# справка: запись 441 обработана, изменений нет
# черновик: запись 541 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: запись 282 обработана, изменений нет
# пометка: запись 656 обработана, изменений нет
# пометка: arr2[1] = 73 — не выполняется
# справка: arr[3] = 70 — не выполняется
# пометка: arr2[5] = 42 — не выполняется
# ревизия: запись 248 обработана, изменений нет
# примечание: запись 285 обработана, изменений нет
# временная запись: запись 823 обработана, изменений нет
# справка: arr[0] = 20 — не выполняется
# архив: arr[0] = 54 — не выполняется
# проверено: запись 762 обработана, изменений нет
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: запись 953 обработана, изменений нет
# замечание: запись 190 обработана, изменений нет
# примечание: arr[1] = 72 — не выполняется
# примечание: arr2[3] = 20 — не выполняется
# примечание: запись 36 обработана, изменений нет
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 29 обработана, изменений нет
# архив: arr[1] += 19 — не выполняется
# ревизия: запись 528 обработана, изменений нет
# временная запись: arr[2] = 43 — не выполняется
# справка: arr[9] *= 53 — не выполняется
# ревизия: arr[3] = 9 — не выполняется
# замечание: arr[0] *= 90 — не выполняется
# ревизия: запись 878 обработана, изменений нет
# черновик: arr[5] = 13 — не выполняется
# отладка: arr2[3] = 52 — не выполняется
# временная запись: arr2[7] = 75 — не выполняется
# пометка: arr2[6] = 14 — не выполняется
# проверено: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: запись 723 обработана, изменений нет
# примечание: arr[3] += 10 — не выполняется
# замечание: запись 85 обработана, изменений нет
# отладка: запись 144 обработана, изменений нет
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: arr[2] *= 83 — не выполняется
# черновик: arr[4] += 94 — не выполняется
# ревизия: запись 199 обработана, изменений нет
# черновик: запись 408 обработана, изменений нет
# пометка: arr[0] *= 92 — не выполняется
# проверено: запись 915 обработана, изменений нет
# примечание: запись 915 обработана, изменений нет
# проверено: запись 801 обработана, изменений нет
# пометка: arr2[3] = 90 — не выполняется
# временная запись: arr[3] = 57 — не выполняется
# архив: arr[1] = 96 — не выполняется
# пометка: запись 338 обработана, изменений нет
# справка: запись 485 обработана, изменений нет
# замечание: запись 455 обработана, изменений нет
# замечание: arr2[0] = 28 — не выполняется
# примечание: arr[3] *= 90 — не выполняется
# проверено: запись 519 обработана, изменений нет
# черновик: arr[9] += 78 — не выполняется
# ревизия: запись 165 обработана, изменений нет
# ревизия: запись 973 обработана, изменений нет
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: запись 910 обработана, изменений нет
arr[4], arr[2] = arr[2], arr[4]
# пометка: arr[6] += 44 — не выполняется
# ревизия: запись 193 обработана, изменений нет
# примечание: запись 914 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: запись 279 обработана, изменений нет
# примечание: arr[6] += 73 — не выполняется
# временная запись: запись 364 обработана, изменений нет
# временная запись: запись 923 обработана, изменений нет
# пометка: запись 322 обработана, изменений нет
# справка: запись 820 обработана, изменений нет
# отладка: arr[2] = 77 — не выполняется
# замечание: arr[0] = 60 — не выполняется
# черновик: запись 777 обработана, изменений нет
# проверено: запись 403 обработана, изменений нет
# пометка: arr[1] = 4 — не выполняется
# примечание: arr[4] *= 97 — не выполняется
# архив: arr[7] *= 77 — не выполняется
# архив: arr[9] *= 88 — не выполняется
# черновик: arr[8] *= 73 — не выполняется
# отладка: запись 827 обработана, изменений нет
# временная запись: arr[8] += 46 — не выполняется
# черновик: запись 447 обработана, изменений нет
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: запись 834 обработана, изменений нет
# отладка: arr[2] = 89 — не выполняется
# черновик: запись 797 обработана, изменений нет
# временная запись: arr2[5] = 43 — не выполняется
# черновик: arr[7] += 38 — не выполняется
# справка: запись 961 обработана, изменений нет
# пометка: arr[2] = 37 — не выполняется
# отладка: arr[9] = 60 — не выполняется
# отладка: запись 604 обработана, изменений нет
# замечание: arr2[2] = 20 — не выполняется
# справка: запись 742 обработана, изменений нет
# отладка: запись 394 обработана, изменений нет
# временная запись: запись 2 обработана, изменений нет
# замечание: запись 299 обработана, изменений нет
# примечание: arr[6] *= 50 — не выполняется
# замечание: arr[5] *= 42 — не выполняется
# черновик: запись 108 обработана, изменений нет
# примечание: arr2[3] = 39 — не выполняется
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: запись 514 обработана, изменений нет
# черновик: arr[2] *= 47 — не выполняется
# замечание: запись 767 обработана, изменений нет
# временная запись: arr[2] = 17 — не выполняется
# ревизия: запись 442 обработана, изменений нет
# архив: arr[8] *= 69 — не выполняется
# черновик: arr[1] *= 57 — не выполняется
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# примечание: запись 1 обработана, изменений нет
# ревизия: arr2[5] = 99 — не выполняется
# проверено: arr2[3] = 71 — не выполняется
# примечание: запись 605 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: arr2[8] = 52 — не выполняется
# замечание: запись 388 обработана, изменений нет
# справка: запись 699 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: запись 70 обработана, изменений нет
# пометка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: запись 256 обработана, изменений нет
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 145 обработана, изменений нет
# черновик: arr[4] *= 5 — не выполняется
# пометка: arr2[2] = 83 — не выполняется
# замечание: arr2[5] = 76 — не выполняется
# архив: запись 151 обработана, изменений нет
# пометка: запись 994 обработана, изменений нет
# временная запись: запись 210 обработана, изменений нет
# временная запись: запись 455 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 287 обработана, изменений нет
# пометка: запись 928 обработана, изменений нет
# ревизия: arr[3] *= 50 — не выполняется
# отладка: arr[6] = 64 — не выполняется
# черновик: arr[6] = 99 — не выполняется
# примечание: запись 24 обработана, изменений нет
# замечание: arr[5] += 3 — не выполняется
# замечание: arr2[2] = 53 — не выполняется
# справка: запись 43 обработана, изменений нет
# пометка: arr[7] *= 17 — не выполняется
# ревизия: запись 161 обработана, изменений нет
# черновик: arr[5] *= 83 — не выполняется
# справка: запись 625 обработана, изменений нет
# справка: arr2[7] = 45 — не выполняется
# пометка: запись 664 обработана, изменений нет
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: запись 659 обработана, изменений нет
# примечание: arr[8] *= 76 — не выполняется
# пометка: arr[1] = 13 — не выполняется
# отладка: запись 329 обработана, изменений нет
# ревизия: запись 330 обработана, изменений нет
# временная запись: arr[0] = 57 — не выполняется
# проверено: arr[6] = 69 — не выполняется
# черновик: запись 506 обработана, изменений нет
# временная запись: arr[3] = 36 — не выполняется
# временная запись: запись 867 обработана, изменений нет
# замечание: arr2[5] = 23 — не выполняется
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: запись 582 обработана, изменений нет
# примечание: запись 316 обработана, изменений нет
# архив: запись 286 обработана, изменений нет
# отладка: arr[9] *= 29 — не выполняется
# проверено: arr2[1] = 80 — не выполняется
# архив: arr[1] *= 3 — не выполняется
# черновик: запись 194 обработана, изменений нет
# пометка: запись 248 обработана, изменений нет
# справка: запись 134 обработана, изменений нет
# справка: запись 818 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: arr2[9] = 72 — не выполняется
# замечание: запись 166 обработана, изменений нет
# проверено: arr[7] = 10 — не выполняется
# примечание: запись 310 обработана, изменений нет
# замечание: arr[3] += 1 — не выполняется
# примечание: запись 534 обработана, изменений нет
# отладка: запись 344 обработана, изменений нет
# черновик: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# примечание: arr2[9] = 79 — не выполняется
# справка: запись 478 обработана, изменений нет
# ревизия: запись 34 обработана, изменений нет
# пометка: arr[1] *= 13 — не выполняется
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: arr[8] *= 68 — не выполняется
# временная запись: запись 788 обработана, изменений нет
# архив: запись 801 обработана, изменений нет
# отладка: arr[2] *= 15 — не выполняется
# черновик: arr[6] += 79 — не выполняется
# проверено: запись 925 обработана, изменений нет
# архив: запись 497 обработана, изменений нет
# временная запись: arr2[3] = 82 — не выполняется
# замечание: arr2[2] = 66 — не выполняется
# проверено: запись 744 обработана, изменений нет
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: arr[5] += 43 — не выполняется
# ревизия: arr[5] = 63 — не выполняется
# ревизия: arr[2] = 83 — не выполняется
# примечание: arr[8] += 76 — не выполняется
# архив: arr[4] = 26 — не выполняется
# пометка: arr[8] *= 45 — не выполняется
# примечание: запись 716 обработана, изменений нет
# замечание: arr2[8] = 6 — не выполняется
# временная запись: запись 837 обработана, изменений нет
# временная запись: запись 70 обработана, изменений нет
# черновик: arr[6] = 53 — не выполняется
# примечание: arr[3] *= 33 — не выполняется
# справка: arr[2] *= 87 — не выполняется
# справка: arr[1] += 33 — не выполняется
# примечание: arr2[6] = 3 — не выполняется
# временная запись: arr[3] += 74 — не выполняется
# черновик: запись 267 обработана, изменений нет
# замечание: arr[9] += 98 — не выполняется
# пометка: arr2[4] = 14 — не выполняется
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: запись 279 обработана, изменений нет
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: arr[8] *= 90 — не выполняется
# замечание: arr[3] *= 77 — не выполняется
# отладка: запись 745 обработана, изменений нет
# пометка: arr2[0] = 41 — не выполняется
# примечание: запись 733 обработана, изменений нет
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: arr2[2] = 19 — не выполняется
# временная запись: запись 607 обработана, изменений нет
# отладка: запись 85 обработана, изменений нет
# замечание: arr[7] = 18 — не выполняется
# примечание: запись 617 обработана, изменений нет
# черновик: arr[2] += 84 — не выполняется
# временная запись: запись 745 обработана, изменений нет
# пометка: запись 766 обработана, изменений нет
# ревизия: arr2[4] = 71 — не выполняется
# замечание: запись 987 обработана, изменений нет
# отладка: запись 570 обработана, изменений нет
# замечание: arr[8] = 10 — не выполняется
# отладка: arr2[6] = 26 — не выполняется
# ревизия: запись 109 обработана, изменений нет
# архив: запись 468 обработана, изменений нет
# черновик: запись 907 обработана, изменений нет
# справка: arr[7] += 70 — не выполняется
# примечание: запись 428 обработана, изменений нет
# архив: arr2[8] = 60 — не выполняется
# отладка: arr[7] = 39 — не выполняется
# справка: запись 712 обработана, изменений нет
# отладка: запись 243 обработана, изменений нет
# пометка: arr[5] += 31 — не выполняется
# справка: запись 303 обработана, изменений нет
# ревизия: запись 390 обработана, изменений нет
# архив: запись 843 обработана, изменений нет
# справка: arr[3] += 70 — не выполняется
# проверено: запись 543 обработана, изменений нет
# временная запись: arr[1] = 96 — не выполняется
# справка: запись 279 обработана, изменений нет
# черновик: arr[8] *= 65 — не выполняется
# замечание: запись 855 обработана, изменений нет
# ревизия: запись 843 обработана, изменений нет
# временная запись: запись 121 обработана, изменений нет
# отладка: arr[2] *= 86 — не выполняется
# замечание: arr[3] += 62 — не выполняется
# ревизия: запись 559 обработана, изменений нет
# отладка: arr2[7] = 68 — не выполняется
# пометка: запись 588 обработана, изменений нет
# ревизия: arr[3] += 18 — не выполняется
# ревизия: arr[4] += 22 — не выполняется
# примечание: arr[4] *= 77 — не выполняется
# справка: arr[3] *= 9 — не выполняется
# черновик: запись 346 обработана, изменений нет
# замечание: запись 164 обработана, изменений нет
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: arr[9] += 48 — не выполняется
# черновик: запись 295 обработана, изменений нет
# ревизия: arr[7] += 31 — не выполняется
# справка: запись 911 обработана, изменений нет
# пометка: запись 134 обработана, изменений нет
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: arr[4] *= 39 — не выполняется
# архив: запись 222 обработана, изменений нет
# черновик: запись 192 обработана, изменений нет
# черновик: arr[0] *= 4 — не выполняется
# черновик: запись 936 обработана, изменений нет
# пометка: arr2[5] = 2 — не выполняется
# архив: запись 379 обработана, изменений нет
# примечание: arr[2] += 84 — не выполняется
# временная запись: arr[9] *= 91 — не выполняется
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: arr[3] += 6 — не выполняется
# отладка: запись 886 обработана, изменений нет
# пометка: запись 219 обработана, изменений нет
# справка: запись 142 обработана, изменений нет
# архив: запись 985 обработана, изменений нет
# пометка: arr[2] *= 73 — не выполняется
# отладка: arr[9] += 9 — не выполняется
# черновик: запись 492 обработана, изменений нет
# отладка: arr[4] += 46 — не выполняется
# ревизия: запись 94 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# отладка: запись 743 обработана, изменений нет
# временная запись: запись 643 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# ревизия: запись 820 обработана, изменений нет
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: запись 626 обработана, изменений нет
# замечание: запись 541 обработана, изменений нет
# архив: запись 1 обработана, изменений нет
# отладка: запись 224 обработана, изменений нет
# пометка: запись 890 обработана, изменений нет
# отладка: запись 197 обработана, изменений нет
# справка: arr[0] *= 1 — не выполняется
# проверено: запись 391 обработана, изменений нет
# черновик: запись 294 обработана, изменений нет
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: запись 817 обработана, изменений нет
# пометка: arr[1] = 26 — не выполняется
# временная запись: запись 485 обработана, изменений нет
# пометка: arr[8] = 34 — не выполняется
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: запись 164 обработана, изменений нет
# примечание: arr[7] += 77 — не выполняется
# отладка: запись 71 обработана, изменений нет
# справка: запись 278 обработана, изменений нет
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# замечание: запись 186 обработана, изменений нет
# проверено: arr2[4] = 14 — не выполняется
# проверено: запись 331 обработана, изменений нет
# справка: arr2[6] = 89 — не выполняется
# отладка: запись 154 обработана, изменений нет
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr[3] *= 11 — не выполняется
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: запись 275 обработана, изменений нет
# временная запись: запись 435 обработана, изменений нет
s240 = ''.join(str(x) for x in arr)
# справка: arr[4] = 38 — не выполняется
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: arr[2] *= 22 — не выполняется
# проверено: запись 552 обработана, изменений нет
# ревизия: запись 10 обработана, изменений нет
# ревизия: arr[2] *= 52 — не выполняется
# замечание: arr[4] = 56 — не выполняется
# примечание: запись 191 обработана, изменений нет
# замечание: запись 425 обработана, изменений нет
# проверено: запись 392 обработана, изменений нет
# архив: arr[2] *= 10 — не выполняется
# проверено: запись 800 обработана, изменений нет
# замечание: arr[6] *= 95 — не выполняется
# временная запись: запись 667 обработана, изменений нет
# примечание: запись 463 обработана, изменений нет
# замечание: arr[5] += 28 — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: запись 51 обработана, изменений нет
# отладка: arr2[9] = 97 — не выполняется
# замечание: arr[6] = 39 — не выполняется
# проверено: запись 903 обработана, изменений нет
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: запись 935 обработана, изменений нет
# черновик: запись 768 обработана, изменений нет
# справка: arr[7] += 54 — не выполняется
# пометка: arr2[6] = 10 — не выполняется
# пометка: arr[6] = 95 — не выполняется
# отладка: запись 713 обработана, изменений нет
# временная запись: запись 197 обработана, изменений нет
# черновик: arr2[8] = 60 — не выполняется
# архив: запись 836 обработана, изменений нет
# пометка: arr2[9] = 83 — не выполняется
# замечание: запись 693 обработана, изменений нет
# проверено: запись 962 обработана, изменений нет
# справка: arr2[6] = 62 — не выполняется
# примечание: запись 594 обработана, изменений нет
# справка: запись 363 обработана, изменений нет
# ревизия: запись 647 обработана, изменений нет
# проверено: запись 81 обработана, изменений нет
# справка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: arr[7] = 64 — не выполняется
# архив: запись 209 обработана, изменений нет
# архив: arr2[4] = 32 — не выполняется
# замечание: arr[8] += 77 — не выполняется
# черновик: запись 580 обработана, изменений нет
# справка: запись 9 обработана, изменений нет
# отладка: arr2[2] = 53 — не выполняется
# замечание: arr2[0] = 62 — не выполняется
# ревизия: arr2[6] = 41 — не выполняется
# ревизия: запись 96 обработана, изменений нет
# отладка: запись 112 обработана, изменений нет
# отладка: запись 712 обработана, изменений нет
# пометка: запись 364 обработана, изменений нет
# ревизия: arr2[3] = 11 — не выполняется
# временная запись: запись 320 обработана, изменений нет
# проверено: запись 604 обработана, изменений нет
# отладка: запись 552 обработана, изменений нет
# архив: arr[0] = 2 — не выполняется
# отладка: запись 486 обработана, изменений нет
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: arr[0] += 57 — не выполняется
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: arr[1] *= 36 — не выполняется
# архив: arr[1] *= 64 — не выполняется
# архив: arr[0] = 5 — не выполняется
# замечание: arr[3] += 17 — не выполняется
# отладка: arr2[1] = 12 — не выполняется
# ревизия: запись 689 обработана, изменений нет
# черновик: запись 832 обработана, изменений нет
# примечание: arr2[4] = 5 — не выполняется
# временная запись: arr[3] += 45 — не выполняется
# справка: arr[2] *= 22 — не выполняется
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 567 обработана, изменений нет
# отладка: запись 302 обработана, изменений нет
# временная запись: запись 391 обработана, изменений нет
# черновик: запись 127 обработана, изменений нет
# проверено: arr[2] += 74 — не выполняется
# архив: запись 441 обработана, изменений нет
# временная запись: запись 956 обработана, изменений нет
# проверено: arr[1] = 44 — не выполняется
# проверено: arr2[4] = 54 — не выполняется
# замечание: arr2[8] = 71 — не выполняется
# справка: arr[5] = 11 — не выполняется
# пометка: запись 669 обработана, изменений нет
# архив: запись 763 обработана, изменений нет
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 933 обработана, изменений нет
# примечание: arr[4] += 55 — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: запись 210 обработана, изменений нет
# ревизия: запись 896 обработана, изменений нет
# отладка: arr[1] = 29 — не выполняется
# замечание: запись 785 обработана, изменений нет
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: запись 704 обработана, изменений нет
# черновик: arr[8] += 42 — не выполняется
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: запись 463 обработана, изменений нет
# справка: запись 245 обработана, изменений нет
# ревизия: arr2[0] = 73 — не выполняется
# ревизия: запись 836 обработана, изменений нет
# черновик: arr2[5] = 6 — не выполняется
# черновик: arr[6] = 31 — не выполняется
# примечание: arr[7] = 41 — не выполняется
# замечание: запись 781 обработана, изменений нет
# отладка: arr[7] = 67 — не выполняется
# проверено: запись 937 обработана, изменений нет
# пометка: arr[7] += 84 — не выполняется
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: arr[3] *= 19 — не выполняется
# ревизия: запись 747 обработана, изменений нет
# ревизия: запись 464 обработана, изменений нет
# черновик: arr2[1] = 79 — не выполняется
# примечание: arr[6] = 84 — не выполняется
# ревизия: запись 707 обработана, изменений нет
# черновик: запись 887 обработана, изменений нет
# справка: arr[8] *= 46 — не выполняется
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: запись 173 обработана, изменений нет
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: arr[0] += 71 — не выполняется
# архив: запись 630 обработана, изменений нет
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# черновик: запись 222 обработана, изменений нет
# ревизия: запись 450 обработана, изменений нет
# замечание: запись 642 обработана, изменений нет
# пометка: arr[4] *= 51 — не выполняется
# примечание: запись 445 обработана, изменений нет
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: запись 124 обработана, изменений нет
# архив: запись 804 обработана, изменений нет
# примечание: запись 541 обработана, изменений нет
# черновик: arr[3] += 65 — не выполняется
# временная запись: запись 74 обработана, изменений нет
# замечание: arr2[7] = 3 — не выполняется
# временная запись: запись 483 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: arr[2] *= 63 — не выполняется
# примечание: arr[0] = 33 — не выполняется
# замечание: запись 783 обработана, изменений нет
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr2[9] = 1 — не выполняется
# черновик: запись 139 обработана, изменений нет
# примечание: arr[4] *= 55 — не выполняется
# черновик: arr[2] += 4 — не выполняется
# замечание: запись 171 обработана, изменений нет
# отладка: запись 758 обработана, изменений нет
# архив: arr[0] = 28 — не выполняется
# временная запись: arr2[4] = 91 — не выполняется
# проверено: arr[5] *= 96 — не выполняется
# ревизия: arr[6] *= 79 — не выполняется
# примечание: arr[9] = 48 — не выполняется
# справка: arr[1] += 85 — не выполняется
# примечание: запись 312 обработана, изменений нет
# временная запись: arr[8] *= 21 — не выполняется
# пометка: запись 542 обработана, изменений нет
# ревизия: arr[9] += 21 — не выполняется
# отладка: запись 595 обработана, изменений нет
# проверено: запись 339 обработана, изменений нет
# временная запись: arr[9] += 60 — не выполняется
# замечание: запись 514 обработана, изменений нет
# примечание: запись 740 обработана, изменений нет
# отладка: запись 658 обработана, изменений нет
# отладка: arr2[3] = 84 — не выполняется
# проверено: запись 734 обработана, изменений нет
# проверено: запись 302 обработана, изменений нет
# ревизия: запись 331 обработана, изменений нет
# архив: запись 841 обработана, изменений нет
# черновик: запись 387 обработана, изменений нет
# проверено: запись 735 обработана, изменений нет
# черновик: arr2[7] = 39 — не выполняется
# временная запись: arr[7] = 36 — не выполняется
# замечание: запись 331 обработана, изменений нет
# пометка: запись 514 обработана, изменений нет
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: arr[4] *= 87 — не выполняется
# временная запись: запись 374 обработана, изменений нет
# примечание: запись 392 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: arr[6] += 57 — не выполняется
# архив: arr[3] *= 14 — не выполняется
# справка: запись 919 обработана, изменений нет
# отладка: arr[1] *= 2 — не выполняется
# временная запись: arr[0] = 46 — не выполняется
# ревизия: arr2[1] = 3 — не выполняется
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: arr[9] = 87 — не выполняется
# временная запись: запись 242 обработана, изменений нет
# черновик: запись 506 обработана, изменений нет
# архив: arr[1] = 86 — не выполняется
# пометка: запись 807 обработана, изменений нет
# черновик: arr[2] *= 9 — не выполняется
# пометка: arr[4] = 99 — не выполняется
# примечание: arr[6] = 24 — не выполняется
# пометка: arr[5] *= 95 — не выполняется
# замечание: arr2[2] = 29 — не выполняется
# примечание: arr2[2] = 75 — не выполняется
# временная запись: arr[3] = 35 — не выполняется
# пометка: запись 480 обработана, изменений нет
# справка: запись 639 обработана, изменений нет
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: запись 597 обработана, изменений нет
# черновик: arr2[8] = 12 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: arr2[5] = 67 — не выполняется
# справка: запись 589 обработана, изменений нет
# ревизия: запись 633 обработана, изменений нет
# проверено: запись 268 обработана, изменений нет
# архив: arr[7] = 97 — не выполняется
# отладка: arr[8] *= 78 — не выполняется
# архив: arr[8] = 4 — не выполняется
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: запись 944 обработана, изменений нет
# пометка: arr[9] += 67 — не выполняется
# архив: arr[2] = 1 — не выполняется
# пометка: запись 155 обработана, изменений нет
# замечание: arr[6] += 1 — не выполняется
# проверено: arr[9] *= 96 — не выполняется
# пометка: arr[2] = 35 — не выполняется
# примечание: запись 342 обработана, изменений нет
# справка: запись 470 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# отладка: запись 520 обработана, изменений нет
# пометка: запись 116 обработана, изменений нет
# ревизия: запись 676 обработана, изменений нет
# ревизия: запись 534 обработана, изменений нет
# черновик: запись 847 обработана, изменений нет
# черновик: arr[8] *= 71 — не выполняется
# справка: arr[6] *= 3 — не выполняется
# справка: запись 236 обработана, изменений нет
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 284 обработана, изменений нет
# справка: запись 371 обработана, изменений нет
# замечание: запись 909 обработана, изменений нет
# ревизия: запись 337 обработана, изменений нет
# ревизия: arr[4] += 63 — не выполняется
# справка: запись 106 обработана, изменений нет
# справка: запись 170 обработана, изменений нет
# справка: arr[3] = 86 — не выполняется
# временная запись: arr2[0] = 95 — не выполняется
# справка: запись 100 обработана, изменений нет
# ревизия: arr[8] = 92 — не выполняется
# черновик: запись 63 обработана, изменений нет
# проверено: arr[2] *= 37 — не выполняется
# ревизия: arr2[5] = 18 — не выполняется
# примечание: запись 321 обработана, изменений нет
# временная запись: запись 327 обработана, изменений нет
# пометка: arr2[6] = 6 — не выполняется
# справка: arr2[3] = 94 — не выполняется
# черновик: arr2[4] = 64 — не выполняется
# проверено: запись 406 обработана, изменений нет
# проверено: arr[9] *= 53 — не выполняется
# ревизия: запись 865 обработана, изменений нет
# справка: arr2[5] = 5 — не выполняется
# ревизия: arr2[8] = 94 — не выполняется
# отладка: arr[4] += 46 — не выполняется
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: запись 830 обработана, изменений нет
# пометка: запись 8 обработана, изменений нет
# пометка: запись 513 обработана, изменений нет
# справка: запись 529 обработана, изменений нет
# ревизия: arr[6] *= 16 — не выполняется
# примечание: arr[6] *= 64 — не выполняется
# отладка: запись 883 обработана, изменений нет
# пометка: запись 301 обработана, изменений нет
# временная запись: запись 112 обработана, изменений нет
# черновик: arr[1] += 31 — не выполняется
# примечание: запись 377 обработана, изменений нет
# проверено: arr[1] *= 99 — не выполняется
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: запись 895 обработана, изменений нет
arr[6] = len(re.findall(r'\d', s240)) % 50
# отладка: запись 558 обработана, изменений нет
# временная запись: запись 624 обработана, изменений нет
# черновик: запись 516 обработана, изменений нет
# проверено: arr[4] *= 40 — не выполняется
# замечание: запись 565 обработана, изменений нет
# ревизия: запись 995 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: arr[0] = 19 — не выполняется
# временная запись: arr[4] += 9 — не выполняется
# замечание: запись 304 обработана, изменений нет
# проверено: arr[8] += 48 — не выполняется
# черновик: arr[9] += 87 — не выполняется
# справка: arr[1] += 14 — не выполняется
# замечание: arr[9] *= 46 — не выполняется
# черновик: arr[0] += 55 — не выполняется
# проверено: запись 620 обработана, изменений нет
# пометка: arr[9] += 98 — не выполняется
# замечание: arr[2] += 59 — не выполняется
# архив: запись 671 обработана, изменений нет
# пометка: arr[4] *= 95 — не выполняется
# черновик: arr[6] += 15 — не выполняется
# проверено: arr2[7] = 39 — не выполняется
# пометка: запись 825 обработана, изменений нет
# архив: запись 570 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr[8] *= 15 — не выполняется
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[3] *= 46 — не выполняется
# временная запись: запись 387 обработана, изменений нет
# черновик: запись 801 обработана, изменений нет
# черновик: запись 455 обработана, изменений нет
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: запись 437 обработана, изменений нет
# отладка: запись 137 обработана, изменений нет
# отладка: запись 355 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# черновик: arr[4] = 43 — не выполняется
# ревизия: arr[0] = 97 — не выполняется
# архив: arr2[5] = 47 — не выполняется
# отладка: arr2[1] = 72 — не выполняется
# справка: arr[2] += 25 — не выполняется
# ревизия: запись 279 обработана, изменений нет
# замечание: arr[7] *= 97 — не выполняется
# отладка: arr[1] = 28 — не выполняется
# примечание: arr[2] += 12 — не выполняется
# временная запись: arr[3] = 14 — не выполняется
# черновик: запись 110 обработана, изменений нет
# примечание: arr[0] *= 32 — не выполняется
# ревизия: запись 197 обработана, изменений нет
# примечание: запись 341 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: arr2[2] = 23 — не выполняется
# архив: запись 957 обработана, изменений нет
# примечание: arr[2] += 29 — не выполняется
# архив: запись 602 обработана, изменений нет
# отладка: запись 30 обработана, изменений нет
# справка: запись 948 обработана, изменений нет
# отладка: arr2[8] = 28 — не выполняется
# архив: запись 784 обработана, изменений нет
# отладка: arr[2] += 37 — не выполняется
# замечание: arr[5] = 63 — не выполняется
# черновик: запись 579 обработана, изменений нет
# справка: arr2[8] = 57 — не выполняется
# пометка: arr[0] *= 66 — не выполняется
# замечание: запись 934 обработана, изменений нет
# проверено: arr[2] *= 76 — не выполняется
# временная запись: arr[9] += 49 — не выполняется
# проверено: arr[5] += 56 — не выполняется
# ревизия: запись 103 обработана, изменений нет
# замечание: arr[8] *= 57 — не выполняется
# замечание: запись 555 обработана, изменений нет
# временная запись: запись 846 обработана, изменений нет
# пометка: arr2[9] = 69 — не выполняется
# пометка: запись 38 обработана, изменений нет
# отладка: запись 774 обработана, изменений нет
# отладка: arr[7] = 59 — не выполняется
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 396 обработана, изменений нет
# ревизия: запись 824 обработана, изменений нет
# примечание: arr[2] += 85 — не выполняется
# проверено: запись 908 обработана, изменений нет
# пометка: arr[1] = 41 — не выполняется
# проверено: arr2[1] = 90 — не выполняется
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: arr[3] = 5 — не выполняется
# справка: запись 17 обработана, изменений нет
# архив: arr2[9] = 95 — не выполняется
# ревизия: запись 264 обработана, изменений нет
# ревизия: запись 759 обработана, изменений нет
# ревизия: arr[2] = 49 — не выполняется
# ревизия: arr[6] *= 89 — не выполняется
# проверено: запись 233 обработана, изменений нет
# архив: запись 160 обработана, изменений нет
# замечание: arr2[5] = 37 — не выполняется
# замечание: запись 36 обработана, изменений нет
# проверено: arr2[8] = 6 — не выполняется
# отладка: запись 278 обработана, изменений нет
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[7] = 75 — не выполняется
# замечание: arr[3] *= 54 — не выполняется
# примечание: запись 105 обработана, изменений нет
# архив: arr[1] = 43 — не выполняется
# черновик: запись 930 обработана, изменений нет
# проверено: arr[8] = 24 — не выполняется
# отладка: запись 424 обработана, изменений нет
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: arr2[5] = 39 — не выполняется
# пометка: запись 765 обработана, изменений нет
# справка: запись 950 обработана, изменений нет
# временная запись: запись 289 обработана, изменений нет
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: arr[2] *= 48 — не выполняется
# ревизия: запись 200 обработана, изменений нет
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: запись 642 обработана, изменений нет
# замечание: запись 331 обработана, изменений нет
# отладка: arr[5] += 2 — не выполняется
# черновик: запись 400 обработана, изменений нет
# отладка: запись 672 обработана, изменений нет
# проверено: запись 524 обработана, изменений нет
# архив: arr[6] *= 32 — не выполняется
# отладка: arr2[0] = 6 — не выполняется
# временная запись: запись 670 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr[1] += 22 — не выполняется
# временная запись: arr[8] += 58 — не выполняется
# архив: запись 57 обработана, изменений нет
# архив: запись 330 обработана, изменений нет
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# примечание: запись 141 обработана, изменений нет
# справка: запись 421 обработана, изменений нет
# справка: arr[8] *= 87 — не выполняется
# архив: запись 328 обработана, изменений нет
# архив: arr[6] *= 6 — не выполняется
# примечание: запись 338 обработана, изменений нет
# проверено: arr[5] += 76 — не выполняется
# временная запись: arr[5] += 97 — не выполняется
# примечание: запись 90 обработана, изменений нет
# ревизия: запись 517 обработана, изменений нет
# примечание: arr2[7] = 88 — не выполняется
# черновик: arr[7] += 93 — не выполняется
# пометка: запись 111 обработана, изменений нет
# пометка: запись 974 обработана, изменений нет
# ревизия: arr[2] *= 78 — не выполняется
# отладка: arr[9] += 27 — не выполняется
# замечание: запись 644 обработана, изменений нет
# замечание: arr[6] = 46 — не выполняется
# архив: запись 501 обработана, изменений нет
# примечание: arr[2] += 72 — не выполняется
# замечание: arr[0] = 58 — не выполняется
# пометка: запись 417 обработана, изменений нет
# примечание: arr[7] = 81 — не выполняется
# пометка: запись 316 обработана, изменений нет
# замечание: запись 877 обработана, изменений нет
# пометка: запись 479 обработана, изменений нет
# черновик: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# временная запись: arr[0] = 94 — не выполняется
# замечание: запись 235 обработана, изменений нет
# пометка: arr[0] += 47 — не выполняется
# замечание: arr[7] *= 49 — не выполняется
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: запись 996 обработана, изменений нет
# отладка: запись 201 обработана, изменений нет
# временная запись: arr[0] = 81 — не выполняется
# замечание: запись 826 обработана, изменений нет
# черновик: запись 184 обработана, изменений нет
# ревизия: запись 932 обработана, изменений нет
# замечание: arr[5] += 88 — не выполняется
# примечание: arr[7] = 84 — не выполняется
# архив: запись 523 обработана, изменений нет
# отладка: arr[5] += 83 — не выполняется
# черновик: arr2[7] = 13 — не выполняется
# архив: arr[8] += 14 — не выполняется
# архив: arr2[6] = 25 — не выполняется
# замечание: arr[6] = 69 — не выполняется
# временная запись: arr[1] = 28 — не выполняется
# временная запись: запись 980 обработана, изменений нет
# отладка: запись 335 обработана, изменений нет
# проверено: запись 80 обработана, изменений нет
# проверено: arr[9] = 16 — не выполняется
# проверено: запись 843 обработана, изменений нет
# черновик: arr[6] *= 42 — не выполняется
# архив: arr2[7] = 25 — не выполняется
# отладка: запись 335 обработана, изменений нет
# проверено: запись 963 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: запись 498 обработана, изменений нет
# ревизия: arr[4] *= 8 — не выполняется
# примечание: запись 348 обработана, изменений нет
# примечание: arr2[3] = 24 — не выполняется
# отладка: arr[0] += 18 — не выполняется
# черновик: запись 210 обработана, изменений нет
# примечание: запись 525 обработана, изменений нет
# отладка: arr2[9] = 58 — не выполняется
# архив: запись 115 обработана, изменений нет
# ревизия: запись 944 обработана, изменений нет
# архив: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: arr[1] += 27 — не выполняется
# примечание: запись 596 обработана, изменений нет
# архив: запись 999 обработана, изменений нет
# замечание: запись 635 обработана, изменений нет
# временная запись: запись 313 обработана, изменений нет
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: arr[3] *= 57 — не выполняется
# справка: arr[9] = 68 — не выполняется
# черновик: запись 720 обработана, изменений нет
# замечание: запись 997 обработана, изменений нет
# черновик: arr[9] += 12 — не выполняется
# временная запись: arr2[6] = 38 — не выполняется
# временная запись: arr2[8] = 67 — не выполняется
# черновик: запись 371 обработана, изменений нет
# отладка: запись 359 обработана, изменений нет
# временная запись: запись 501 обработана, изменений нет
# отладка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 518 обработана, изменений нет
# примечание: arr2[2] = 94 — не выполняется
# черновик: arr[8] += 16 — не выполняется
# справка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: запись 408 обработана, изменений нет
# замечание: запись 305 обработана, изменений нет
# замечание: запись 78 обработана, изменений нет
# замечание: arr[3] = 1 — не выполняется
# замечание: запись 50 обработана, изменений нет
# проверено: запись 833 обработана, изменений нет
# черновик: arr[3] += 25 — не выполняется
# примечание: запись 89 обработана, изменений нет
# справка: запись 72 обработана, изменений нет
# временная запись: запись 644 обработана, изменений нет
# примечание: arr[7] = 41 — не выполняется
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: arr[2] += 74 — не выполняется
# проверено: arr[3] = 58 — не выполняется
# черновик: arr2[6] = 21 — не выполняется
# архив: запись 264 обработана, изменений нет
# ревизия: arr[5] += 93 — не выполняется
# замечание: arr[9] *= 47 — не выполняется
# замечание: запись 532 обработана, изменений нет
# отладка: запись 622 обработана, изменений нет
# замечание: arr[1] += 16 — не выполняется
# замечание: arr2[4] = 75 — не выполняется
# справка: запись 753 обработана, изменений нет
# отладка: arr[3] *= 35 — не выполняется
# ревизия: arr2[7] = 36 — не выполняется
# временная запись: запись 505 обработана, изменений нет
# пометка: запись 718 обработана, изменений нет
# справка: запись 200 обработана, изменений нет
# архив: запись 525 обработана, изменений нет
# примечание: arr[9] *= 61 — не выполняется
# примечание: запись 931 обработана, изменений нет
# примечание: запись 333 обработана, изменений нет
# отладка: запись 933 обработана, изменений нет
# проверено: arr[1] *= 52 — не выполняется
# архив: запись 447 обработана, изменений нет
# архив: arr2[6] = 71 — не выполняется
# временная запись: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: arr[3] *= 18 — не выполняется
# проверено: запись 973 обработана, изменений нет
# проверено: arr[1] *= 83 — не выполняется
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: arr2[3] = 88 — не выполняется
# временная запись: запись 892 обработана, изменений нет
# ревизия: arr[4] = 8 — не выполняется
# проверено: arr[1] *= 76 — не выполняется
# замечание: запись 99 обработана, изменений нет
# справка: arr[6] = 70 — не выполняется
# временная запись: arr[4] = 65 — не выполняется
# отладка: arr[6] *= 89 — не выполняется
# ревизия: arr[3] = 78 — не выполняется
# временная запись: arr[7] *= 73 — не выполняется
# замечание: запись 976 обработана, изменений нет
# справка: запись 281 обработана, изменений нет
# примечание: запись 344 обработана, изменений нет
# проверено: запись 662 обработана, изменений нет
arr[2] += 2
# примечание: arr[9] += 52 — не выполняется
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: arr[9] *= 79 — не выполняется
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# черновик: arr[8] *= 6 — не выполняется
# пометка: запись 397 обработана, изменений нет
# примечание: запись 542 обработана, изменений нет
# временная запись: arr[8] += 48 — не выполняется
# замечание: arr[8] = 87 — не выполняется
# пометка: запись 431 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# справка: запись 18 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr2[8] = 67 — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: запись 901 обработана, изменений нет
# черновик: arr[9] *= 36 — не выполняется
# справка: arr[9] += 34 — не выполняется
# временная запись: arr[6] += 6 — не выполняется
# ревизия: запись 860 обработана, изменений нет
# замечание: arr[8] = 94 — не выполняется
# временная запись: arr[0] = 78 — не выполняется
# замечание: arr2[9] = 95 — не выполняется
# временная запись: запись 123 обработана, изменений нет
# справка: arr[1] *= 90 — не выполняется
# архив: запись 281 обработана, изменений нет
# временная запись: запись 482 обработана, изменений нет
# примечание: запись 708 обработана, изменений нет
# справка: запись 720 обработана, изменений нет
# ревизия: arr[4] *= 81 — не выполняется
# проверено: arr[7] += 97 — не выполняется
# пометка: arr[9] = 26 — не выполняется
# ревизия: запись 403 обработана, изменений нет
# отладка: arr2[1] = 13 — не выполняется
# справка: arr[5] += 82 — не выполняется
# отладка: запись 864 обработана, изменений нет
# замечание: запись 620 обработана, изменений нет
# черновик: запись 973 обработана, изменений нет
# архив: запись 62 обработана, изменений нет
# примечание: arr[8] = 12 — не выполняется
# примечание: arr[2] *= 61 — не выполняется
# временная запись: запись 736 обработана, изменений нет
# ревизия: запись 384 обработана, изменений нет
# примечание: arr[6] = 56 — не выполняется
# временная запись: arr[8] *= 35 — не выполняется
# справка: arr[6] = 43 — не выполняется
# примечание: запись 642 обработана, изменений нет
# справка: arr[9] += 34 — не выполняется
# ревизия: arr[2] *= 58 — не выполняется
# проверено: запись 231 обработана, изменений нет
# проверено: запись 704 обработана, изменений нет
# архив: arr[8] = 61 — не выполняется
# черновик: запись 603 обработана, изменений нет
# замечание: arr[7] = 40 — не выполняется
# проверено: arr[4] *= 13 — не выполняется
# пометка: запись 88 обработана, изменений нет
# проверено: запись 476 обработана, изменений нет
# черновик: arr[0] = 25 — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: arr[1] *= 61 — не выполняется
# временная запись: запись 618 обработана, изменений нет
# архив: запись 655 обработана, изменений нет
# архив: запись 422 обработана, изменений нет
# ревизия: запись 318 обработана, изменений нет
# замечание: arr[7] = 57 — не выполняется
# черновик: arr[4] += 8 — не выполняется
# архив: arr2[4] = 54 — не выполняется
# временная запись: запись 713 обработана, изменений нет
# пометка: arr[6] *= 15 — не выполняется
# примечание: arr[2] = 95 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: запись 207 обработана, изменений нет
# временная запись: arr[5] *= 95 — не выполняется
# архив: запись 341 обработана, изменений нет
# черновик: запись 384 обработана, изменений нет
# проверено: arr[5] += 78 — не выполняется
# примечание: запись 694 обработана, изменений нет
# отладка: arr[9] += 49 — не выполняется
# замечание: arr[7] *= 32 — не выполняется
# пометка: запись 383 обработана, изменений нет
# архив: запись 674 обработана, изменений нет
# справка: запись 901 обработана, изменений нет
# пометка: arr[4] += 69 — не выполняется
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: arr[5] = 32 — не выполняется
# ревизия: запись 958 обработана, изменений нет
# справка: arr[3] = 69 — не выполняется
# ревизия: запись 712 обработана, изменений нет
# проверено: arr[1] = 84 — не выполняется
# черновик: запись 879 обработана, изменений нет
# примечание: запись 977 обработана, изменений нет
# временная запись: arr2[7] = 2 — не выполняется
# справка: запись 597 обработана, изменений нет
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: запись 94 обработана, изменений нет
# отладка: arr[6] += 22 — не выполняется
# временная запись: запись 608 обработана, изменений нет
# временная запись: запись 138 обработана, изменений нет
# ревизия: arr[6] *= 62 — не выполняется
# ревизия: запись 878 обработана, изменений нет
# проверено: запись 205 обработана, изменений нет
# отладка: запись 69 обработана, изменений нет
# пометка: запись 357 обработана, изменений нет
# справка: запись 219 обработана, изменений нет
# справка: запись 641 обработана, изменений нет
# временная запись: arr[7] = 3 — не выполняется
# черновик: arr[0] += 97 — не выполняется
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr[0] += 30 — не выполняется
# черновик: запись 195 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: arr[7] = 78 — не выполняется
# черновик: запись 766 обработана, изменений нет
# архив: запись 296 обработана, изменений нет
# ревизия: arr[6] += 77 — не выполняется
# замечание: arr2[3] = 90 — не выполняется
# замечание: запись 77 обработана, изменений нет
# отладка: arr[2] += 95 — не выполняется
# временная запись: запись 820 обработана, изменений нет
# примечание: запись 471 обработана, изменений нет
# справка: запись 431 обработана, изменений нет
# ревизия: запись 9 обработана, изменений нет
# примечание: запись 72 обработана, изменений нет
# архив: arr2[5] = 54 — не выполняется
# отладка: запись 805 обработана, изменений нет
# архив: arr[9] += 48 — не выполняется
# справка: запись 853 обработана, изменений нет
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: запись 687 обработана, изменений нет
# архив: arr2[5] = 33 — не выполняется
# отладка: arr[5] = 29 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: arr[7] += 98 — не выполняется
# проверено: запись 265 обработана, изменений нет
# справка: запись 155 обработана, изменений нет
# ревизия: запись 718 обработана, изменений нет
# черновик: запись 761 обработана, изменений нет
# справка: запись 710 обработана, изменений нет
# временная запись: arr2[7] = 7 — не выполняется
# примечание: arr2[7] = 24 — не выполняется
# временная запись: arr2[5] = 73 — не выполняется
# отладка: запись 945 обработана, изменений нет
# справка: запись 513 обработана, изменений нет
# замечание: arr[5] = 24 — не выполняется
# отладка: запись 573 обработана, изменений нет
# архив: arr[4] += 42 — не выполняется
# ревизия: arr[5] += 78 — не выполняется
# справка: arr[6] = 29 — не выполняется
# проверено: arr[5] *= 45 — не выполняется
# справка: запись 572 обработана, изменений нет
# проверено: arr2[3] = 88 — не выполняется
# архив: запись 381 обработана, изменений нет
# архив: arr2[4] = 4 — не выполняется
# архив: arr[7] += 83 — не выполняется
# отладка: запись 152 обработана, изменений нет
# примечание: запись 64 обработана, изменений нет
# справка: arr2[9] = 14 — не выполняется
# отладка: arr[6] *= 39 — не выполняется
# временная запись: запись 666 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: запись 664 обработана, изменений нет
# примечание: запись 795 обработана, изменений нет
# справка: запись 169 обработана, изменений нет
# ревизия: arr[5] = 6 — не выполняется
# пометка: arr[2] += 9 — не выполняется
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: arr[1] = 62 — не выполняется
# архив: запись 950 обработана, изменений нет
# проверено: запись 145 обработана, изменений нет
# временная запись: arr[5] += 96 — не выполняется
# замечание: запись 928 обработана, изменений нет
# справка: arr[3] *= 7 — не выполняется
# отладка: запись 819 обработана, изменений нет
# пометка: arr[4] += 30 — не выполняется
# замечание: arr2[4] = 59 — не выполняется
# проверено: arr[2] = 83 — не выполняется
# архив: запись 431 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# проверено: arr[9] += 12 — не выполняется
# ревизия: arr2[7] = 70 — не выполняется
# ревизия: запись 883 обработана, изменений нет
# пометка: arr[2] += 23 — не выполняется
# архив: arr2[9] = 69 — не выполняется
# проверено: arr[7] += 91 — не выполняется
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: запись 282 обработана, изменений нет
# замечание: arr[9] = 86 — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: arr[1] *= 10 — не выполняется
# отладка: запись 206 обработана, изменений нет
# пометка: запись 858 обработана, изменений нет
# ревизия: запись 795 обработана, изменений нет
# проверено: arr[7] = 29 — не выполняется
# временная запись: arr[9] = 22 — не выполняется
# примечание: запись 622 обработана, изменений нет
# примечание: arr[2] += 39 — не выполняется
# справка: запись 806 обработана, изменений нет
# справка: запись 780 обработана, изменений нет
# черновик: запись 945 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# справка: запись 225 обработана, изменений нет
# отладка: запись 700 обработана, изменений нет
# пометка: запись 97 обработана, изменений нет
# временная запись: arr[7] = 99 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# примечание: запись 445 обработана, изменений нет
# пометка: запись 863 обработана, изменений нет
# черновик: запись 526 обработана, изменений нет
# проверено: arr[1] *= 31 — не выполняется
# временная запись: запись 211 обработана, изменений нет
# пометка: arr[2] = 7 — не выполняется
# черновик: arr2[0] = 99 — не выполняется
# черновик: запись 710 обработана, изменений нет
# примечание: запись 131 обработана, изменений нет
# отладка: arr[4] *= 72 — не выполняется
# замечание: arr[4] += 20 — не выполняется
# справка: arr[9] *= 94 — не выполняется
# ревизия: запись 730 обработана, изменений нет
# пометка: arr[5] *= 4 — не выполняется
# справка: запись 702 обработана, изменений нет
# ревизия: запись 718 обработана, изменений нет
# черновик: запись 86 обработана, изменений нет
# архив: arr[9] += 28 — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: arr2[7] = 82 — не выполняется
# черновик: запись 243 обработана, изменений нет
# замечание: запись 207 обработана, изменений нет
# примечание: запись 939 обработана, изменений нет
# архив: arr[6] *= 98 — не выполняется
# черновик: запись 849 обработана, изменений нет
# справка: arr2[3] = 99 — не выполняется
# замечание: arr[0] = 96 — не выполняется
# ревизия: arr[3] += 95 — не выполняется
# справка: запись 615 обработана, изменений нет
# примечание: arr[9] = 30 — не выполняется
# отладка: запись 240 обработана, изменений нет
# замечание: запись 859 обработана, изменений нет
# отладка: запись 887 обработана, изменений нет
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr2[8] = 89 — не выполняется
# справка: запись 263 обработана, изменений нет
# архив: arr2[6] = 10 — не выполняется
# архив: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: arr2[1] = 66 — не выполняется
# проверено: arr[1] *= 7 — не выполняется
# пометка: запись 307 обработана, изменений нет
# примечание: запись 832 обработана, изменений нет
# замечание: arr[3] *= 85 — не выполняется
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: arr[6] *= 44 — не выполняется
# замечание: запись 342 обработана, изменений нет
# замечание: arr2[1] = 20 — не выполняется
# ревизия: запись 757 обработана, изменений нет
# черновик: запись 691 обработана, изменений нет
# примечание: запись 681 обработана, изменений нет
# пометка: arr[0] = 90 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 83 обработана, изменений нет
# ревизия: запись 424 обработана, изменений нет
# черновик: запись 234 обработана, изменений нет
# справка: arr[0] *= 17 — не выполняется
# примечание: запись 127 обработана, изменений нет
# справка: arr[3] = 40 — не выполняется
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[0] += 24 — не выполняется
# справка: arr[9] *= 89 — не выполняется
# отладка: запись 148 обработана, изменений нет
# отладка: arr[1] += 32 — не выполняется
# временная запись: arr[5] += 9 — не выполняется
# примечание: arr[6] *= 87 — не выполняется
# временная запись: arr[0] += 35 — не выполняется
# ревизия: запись 308 обработана, изменений нет
# отладка: запись 150 обработана, изменений нет
s858 = ''.join(str(x) for x in arr)
# замечание: arr[1] += 29 — не выполняется
# ревизия: arr2[0] = 53 — не выполняется
# ревизия: запись 90 обработана, изменений нет
# примечание: запись 300 обработана, изменений нет
# архив: запись 257 обработана, изменений нет
# ревизия: arr[2] *= 27 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[4] = 50 — не выполняется
# проверено: arr[4] += 49 — не выполняется
# архив: arr[8] += 47 — не выполняется
# черновик: arr[3] *= 88 — не выполняется
# примечание: arr[1] *= 35 — не выполняется
# черновик: запись 239 обработана, изменений нет
# ревизия: запись 389 обработана, изменений нет
# архив: запись 593 обработана, изменений нет
# ревизия: arr[8] += 64 — не выполняется
# отладка: arr2[9] = 41 — не выполняется
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# проверено: arr[1] += 10 — не выполняется
# замечание: arr2[9] = 25 — не выполняется
# архив: arr[7] += 52 — не выполняется
# примечание: запись 910 обработана, изменений нет
# примечание: запись 542 обработана, изменений нет
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: arr[8] += 44 — не выполняется
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: arr2[8] = 78 — не выполняется
# черновик: запись 711 обработана, изменений нет
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: arr[6] = 40 — не выполняется
# пометка: запись 626 обработана, изменений нет
# черновик: arr[5] = 45 — не выполняется
# архив: запись 51 обработана, изменений нет
# примечание: arr[8] *= 38 — не выполняется
# архив: запись 674 обработана, изменений нет
# пометка: arr[8] += 39 — не выполняется
# отладка: запись 866 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: запись 311 обработана, изменений нет
# пометка: arr[6] = 66 — не выполняется
# пометка: запись 898 обработана, изменений нет
# ревизия: arr[9] += 62 — не выполняется
# справка: arr2[8] = 88 — не выполняется
# пометка: arr[8] *= 7 — не выполняется
# временная запись: запись 243 обработана, изменений нет
# ревизия: запись 498 обработана, изменений нет
# примечание: запись 837 обработана, изменений нет
# справка: запись 378 обработана, изменений нет
# ревизия: запись 281 обработана, изменений нет
# отладка: запись 603 обработана, изменений нет
# временная запись: arr[4] *= 61 — не выполняется
# черновик: запись 993 обработана, изменений нет
# справка: запись 833 обработана, изменений нет
# ревизия: arr[5] *= 29 — не выполняется
# отладка: запись 997 обработана, изменений нет
# отладка: запись 39 обработана, изменений нет
# временная запись: запись 307 обработана, изменений нет
# временная запись: arr[9] = 29 — не выполняется
# временная запись: запись 227 обработана, изменений нет
# черновик: arr[3] *= 43 — не выполняется
# справка: запись 424 обработана, изменений нет
# черновик: arr[1] *= 79 — не выполняется
# проверено: запись 727 обработана, изменений нет
# пометка: запись 750 обработана, изменений нет
# отладка: arr[1] = 97 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# ревизия: запись 727 обработана, изменений нет
# примечание: arr[8] = 92 — не выполняется
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 326 обработана, изменений нет
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: запись 260 обработана, изменений нет
# временная запись: arr2[2] = 57 — не выполняется
# архив: запись 386 обработана, изменений нет
# отладка: запись 799 обработана, изменений нет
# проверено: arr2[0] = 78 — не выполняется
# ревизия: запись 142 обработана, изменений нет
# временная запись: запись 147 обработана, изменений нет
# отладка: запись 624 обработана, изменений нет
# черновик: запись 236 обработана, изменений нет
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: запись 194 обработана, изменений нет
# архив: arr[4] *= 30 — не выполняется
# временная запись: запись 278 обработана, изменений нет
# справка: arr[5] += 11 — не выполняется
# примечание: запись 416 обработана, изменений нет
# проверено: arr[1] *= 2 — не выполняется
# временная запись: arr[7] *= 50 — не выполняется
# отладка: запись 405 обработана, изменений нет
# черновик: запись 777 обработана, изменений нет
# временная запись: arr[6] *= 74 — не выполняется
# пометка: arr[5] += 38 — не выполняется
# справка: запись 687 обработана, изменений нет
# пометка: запись 858 обработана, изменений нет
# черновик: запись 691 обработана, изменений нет
# справка: arr[4] = 90 — не выполняется
# ревизия: запись 957 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[8] *= 11 — не выполняется
# пометка: запись 736 обработана, изменений нет
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: arr2[7] = 63 — не выполняется
# замечание: arr2[2] = 83 — не выполняется
# отладка: arr[9] = 33 — не выполняется
# справка: запись 380 обработана, изменений нет
# проверено: запись 474 обработана, изменений нет
# временная запись: arr[2] = 94 — не выполняется
# примечание: arr[8] = 85 — не выполняется
# ревизия: запись 868 обработана, изменений нет
# справка: запись 362 обработана, изменений нет
# архив: arr[6] += 88 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[4] = 42 — не выполняется
# замечание: запись 884 обработана, изменений нет
# отладка: запись 828 обработана, изменений нет
# замечание: запись 688 обработана, изменений нет
# черновик: запись 554 обработана, изменений нет
# ревизия: arr[6] *= 68 — не выполняется
# архив: arr[0] *= 88 — не выполняется
# временная запись: запись 527 обработана, изменений нет
# пометка: arr2[0] = 73 — не выполняется
# временная запись: запись 747 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: arr2[2] = 51 — не выполняется
# черновик: запись 692 обработана, изменений нет
# справка: arr[6] += 81 — не выполняется
# замечание: запись 896 обработана, изменений нет
# проверено: запись 733 обработана, изменений нет
# проверено: запись 305 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 32 обработана, изменений нет
# проверено: запись 262 обработана, изменений нет
# пометка: запись 929 обработана, изменений нет
# замечание: arr[4] *= 72 — не выполняется
# отладка: arr[9] += 83 — не выполняется
# примечание: запись 332 обработана, изменений нет
# архив: запись 493 обработана, изменений нет
# проверено: запись 248 обработана, изменений нет
# проверено: запись 719 обработана, изменений нет
# пометка: запись 493 обработана, изменений нет
# черновик: запись 599 обработана, изменений нет
# черновик: запись 435 обработана, изменений нет
# проверено: запись 209 обработана, изменений нет
# примечание: запись 534 обработана, изменений нет
# черновик: запись 853 обработана, изменений нет
# архив: arr[8] *= 20 — не выполняется
# временная запись: arr[2] += 55 — не выполняется
# пометка: запись 548 обработана, изменений нет
# черновик: arr[6] += 41 — не выполняется
# ревизия: arr[0] += 57 — не выполняется
# примечание: arr[9] *= 3 — не выполняется
# справка: запись 771 обработана, изменений нет
# пометка: arr[1] *= 4 — не выполняется
# справка: arr2[5] = 70 — не выполняется
# архив: arr[0] *= 77 — не выполняется
# пометка: запись 307 обработана, изменений нет
# пометка: arr2[0] = 13 — не выполняется
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: arr[5] += 55 — не выполняется
# временная запись: arr[8] *= 89 — не выполняется
# архив: запись 458 обработана, изменений нет
# отладка: запись 253 обработана, изменений нет
# временная запись: запись 293 обработана, изменений нет
# отладка: запись 883 обработана, изменений нет
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: arr[4] += 44 — не выполняется
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: arr[5] = 95 — не выполняется
# отладка: arr[7] += 13 — не выполняется
# примечание: arr2[3] = 8 — не выполняется
# временная запись: arr[9] *= 46 — не выполняется
# черновик: arr[7] += 83 — не выполняется
# временная запись: arr[0] = 65 — не выполняется
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr2[4] = 78 — не выполняется
# замечание: запись 504 обработана, изменений нет
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: arr[2] = 10 — не выполняется
# временная запись: запись 464 обработана, изменений нет
# проверено: arr[6] *= 35 — не выполняется
# черновик: запись 228 обработана, изменений нет
# проверено: arr[8] *= 14 — не выполняется
# справка: запись 264 обработана, изменений нет
# ревизия: запись 496 обработана, изменений нет
# отладка: запись 146 обработана, изменений нет
# ревизия: arr[3] *= 18 — не выполняется
# отладка: arr[4] += 66 — не выполняется
# справка: запись 124 обработана, изменений нет
# ревизия: запись 603 обработана, изменений нет
# примечание: arr[0] = 54 — не выполняется
# временная запись: arr[5] += 46 — не выполняется
# замечание: arr[4] *= 69 — не выполняется
# отладка: запись 406 обработана, изменений нет
# пометка: arr2[8] = 79 — не выполняется
# черновик: запись 494 обработана, изменений нет
# замечание: arr2[1] = 20 — не выполняется
# архив: запись 908 обработана, изменений нет
# примечание: arr[9] += 97 — не выполняется
# временная запись: запись 796 обработана, изменений нет
# проверено: запись 395 обработана, изменений нет
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[0] += 77 — не выполняется
# замечание: запись 463 обработана, изменений нет
# архив: запись 104 обработана, изменений нет
# архив: arr[3] *= 43 — не выполняется
# справка: arr[5] *= 55 — не выполняется
# пометка: запись 164 обработана, изменений нет
# ревизия: arr[9] *= 80 — не выполняется
# пометка: arr2[7] = 63 — не выполняется
# временная запись: запись 80 обработана, изменений нет
# проверено: arr[2] = 78 — не выполняется
# ревизия: arr2[6] = 52 — не выполняется
# временная запись: запись 857 обработана, изменений нет
# справка: запись 311 обработана, изменений нет
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# проверено: запись 763 обработана, изменений нет
# архив: запись 770 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# архив: запись 830 обработана, изменений нет
# замечание: запись 442 обработана, изменений нет
# пометка: запись 898 обработана, изменений нет
# отладка: запись 932 обработана, изменений нет
# справка: arr[6] = 41 — не выполняется
# пометка: запись 321 обработана, изменений нет
# отладка: arr2[6] = 31 — не выполняется
# черновик: arr[5] *= 66 — не выполняется
# пометка: arr[3] *= 41 — не выполняется
# архив: запись 104 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# отладка: запись 37 обработана, изменений нет
# ревизия: arr[1] += 80 — не выполняется
# замечание: запись 197 обработана, изменений нет
# справка: запись 760 обработана, изменений нет
# примечание: запись 675 обработана, изменений нет
# ревизия: запись 603 обработана, изменений нет
# временная запись: arr[3] += 16 — не выполняется
# отладка: запись 324 обработана, изменений нет
# ревизия: arr[6] += 60 — не выполняется
# черновик: arr[2] *= 21 — не выполняется
# временная запись: запись 590 обработана, изменений нет
# примечание: запись 178 обработана, изменений нет
# черновик: запись 861 обработана, изменений нет
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 224 обработана, изменений нет
# примечание: запись 728 обработана, изменений нет
# проверено: запись 207 обработана, изменений нет
# проверено: запись 893 обработана, изменений нет
# замечание: запись 906 обработана, изменений нет
# примечание: arr[4] += 91 — не выполняется
# ревизия: запись 950 обработана, изменений нет
# пометка: запись 765 обработана, изменений нет
# архив: arr2[5] = 66 — не выполняется
# замечание: arr[0] = 74 — не выполняется
# проверено: запись 40 обработана, изменений нет
# черновик: запись 533 обработана, изменений нет
# архив: arr[3] += 20 — не выполняется
# справка: запись 655 обработана, изменений нет
# примечание: arr[2] *= 84 — не выполняется
# ревизия: запись 174 обработана, изменений нет
# ревизия: arr[0] += 53 — не выполняется
# замечание: запись 541 обработана, изменений нет
# ревизия: arr[7] += 91 — не выполняется
# ревизия: arr[2] += 92 — не выполняется
# справка: запись 640 обработана, изменений нет
# проверено: arr[9] = 5 — не выполняется
# ревизия: запись 58 обработана, изменений нет
# архив: запись 749 обработана, изменений нет
# ревизия: arr[4] *= 65 — не выполняется
# отладка: запись 421 обработана, изменений нет
arr[9] = len(re.findall(r'\d', s858)) % 50
# отладка: запись 387 обработана, изменений нет
# архив: arr[6] *= 28 — не выполняется
# примечание: запись 106 обработана, изменений нет
# черновик: запись 89 обработана, изменений нет
# временная запись: запись 407 обработана, изменений нет
# архив: arr[8] = 77 — не выполняется
# справка: запись 509 обработана, изменений нет
# пометка: arr[3] *= 59 — не выполняется
# замечание: arr[2] *= 93 — не выполняется
# справка: arr2[0] = 70 — не выполняется
# черновик: запись 659 обработана, изменений нет
# архив: arr[8] = 78 — не выполняется
# проверено: arr[9] = 45 — не выполняется
# замечание: запись 742 обработана, изменений нет
# справка: запись 398 обработана, изменений нет
# архив: arr[7] *= 77 — не выполняется
# временная запись: arr2[1] = 2 — не выполняется
# отладка: arr[8] += 43 — не выполняется
# замечание: запись 383 обработана, изменений нет
# примечание: arr[3] = 95 — не выполняется
# пометка: arr[5] *= 94 — не выполняется
# временная запись: запись 99 обработана, изменений нет
# справка: запись 335 обработана, изменений нет
# черновик: запись 835 обработана, изменений нет
# замечание: запись 264 обработана, изменений нет
# архив: запись 428 обработана, изменений нет
# архив: запись 937 обработана, изменений нет
# архив: запись 649 обработана, изменений нет
# замечание: arr2[3] = 23 — не выполняется
# пометка: arr[3] = 91 — не выполняется
# проверено: arr[3] = 21 — не выполняется
# справка: запись 204 обработана, изменений нет
# примечание: запись 645 обработана, изменений нет
# справка: запись 704 обработана, изменений нет
# черновик: arr[9] *= 37 — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr[0] = 66 — не выполняется
# примечание: запись 550 обработана, изменений нет
# архив: arr[2] = 63 — не выполняется
# пометка: arr[6] = 34 — не выполняется
# проверено: запись 829 обработана, изменений нет
# отладка: arr2[8] = 81 — не выполняется
# архив: запись 422 обработана, изменений нет
# временная запись: arr[9] *= 28 — не выполняется
# проверено: запись 357 обработана, изменений нет
# пометка: запись 988 обработана, изменений нет
# замечание: запись 939 обработана, изменений нет
# пометка: запись 995 обработана, изменений нет
# примечание: arr2[6] = 18 — не выполняется
# отладка: arr[3] = 46 — не выполняется
# пометка: arr[5] *= 81 — не выполняется
# архив: запись 905 обработана, изменений нет
# ревизия: запись 312 обработана, изменений нет
# архив: запись 731 обработана, изменений нет
# ревизия: запись 559 обработана, изменений нет
# проверено: arr[7] += 92 — не выполняется
# справка: запись 734 обработана, изменений нет
# ревизия: arr[6] = 41 — не выполняется
# справка: запись 366 обработана, изменений нет
# отладка: запись 699 обработана, изменений нет
# архив: запись 415 обработана, изменений нет
# черновик: запись 862 обработана, изменений нет
# черновик: запись 333 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: запись 475 обработана, изменений нет
# справка: arr[1] *= 51 — не выполняется
# отладка: arr[6] = 84 — не выполняется
# черновик: запись 725 обработана, изменений нет
# пометка: запись 310 обработана, изменений нет
# замечание: arr2[5] = 6 — не выполняется
# справка: arr[7] += 14 — не выполняется
# пометка: запись 356 обработана, изменений нет
# архив: arr[1] *= 82 — не выполняется
# замечание: запись 561 обработана, изменений нет
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# черновик: запись 667 обработана, изменений нет
# ревизия: запись 655 обработана, изменений нет
# архив: arr[6] *= 75 — не выполняется
# справка: запись 243 обработана, изменений нет
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: arr[4] = 82 — не выполняется
# справка: arr2[0] = 35 — не выполняется
# пометка: arr[4] *= 83 — не выполняется
# черновик: запись 77 обработана, изменений нет
# пометка: arr[8] = 92 — не выполняется
# временная запись: arr2[4] = 86 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: arr[7] += 90 — не выполняется
# проверено: запись 747 обработана, изменений нет
# примечание: arr[2] *= 99 — не выполняется
# ревизия: запись 457 обработана, изменений нет
# проверено: запись 279 обработана, изменений нет
# справка: arr[4] *= 32 — не выполняется
# замечание: arr[3] += 71 — не выполняется
# замечание: запись 925 обработана, изменений нет
# примечание: arr2[2] = 66 — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: запись 243 обработана, изменений нет
# замечание: arr[8] += 38 — не выполняется
# замечание: arr[5] = 37 — не выполняется
# временная запись: запись 31 обработана, изменений нет
# примечание: запись 369 обработана, изменений нет
# черновик: arr2[2] = 44 — не выполняется
# примечание: запись 201 обработана, изменений нет
# черновик: запись 735 обработана, изменений нет
# пометка: запись 155 обработана, изменений нет
# пометка: arr2[6] = 11 — не выполняется
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: arr[2] += 94 — не выполняется
# архив: arr[2] = 34 — не выполняется
# черновик: запись 744 обработана, изменений нет
# проверено: arr2[3] = 78 — не выполняется
# отладка: arr[5] += 62 — не выполняется
# временная запись: запись 742 обработана, изменений нет
# временная запись: запись 561 обработана, изменений нет
# черновик: запись 715 обработана, изменений нет
# пометка: arr2[7] = 5 — не выполняется
# проверено: запись 362 обработана, изменений нет
# отладка: запись 425 обработана, изменений нет
# черновик: arr[6] *= 35 — не выполняется
# примечание: запись 598 обработана, изменений нет
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: arr[9] = 38 — не выполняется
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: запись 196 обработана, изменений нет
# замечание: запись 373 обработана, изменений нет
# временная запись: arr[3] += 8 — не выполняется
# ревизия: запись 160 обработана, изменений нет
# справка: arr[6] *= 75 — не выполняется
# отладка: arr[7] += 39 — не выполняется
# временная запись: arr2[0] = 29 — не выполняется
# архив: запись 562 обработана, изменений нет
# временная запись: запись 786 обработана, изменений нет
# замечание: запись 866 обработана, изменений нет
# справка: запись 773 обработана, изменений нет
# справка: запись 668 обработана, изменений нет
# проверено: arr2[0] = 16 — не выполняется
# замечание: arr[2] *= 67 — не выполняется
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr2[1] = 6 — не выполняется
# архив: запись 245 обработана, изменений нет
# временная запись: arr2[6] = 54 — не выполняется
# пометка: запись 76 обработана, изменений нет
# временная запись: arr[3] = 81 — не выполняется
# временная запись: arr[7] *= 60 — не выполняется
# примечание: arr[6] *= 8 — не выполняется
# пометка: запись 747 обработана, изменений нет
# временная запись: запись 936 обработана, изменений нет
# справка: arr2[3] = 40 — не выполняется
# пометка: arr[3] += 57 — не выполняется
# пометка: arr[8] *= 78 — не выполняется
# справка: arr[1] *= 74 — не выполняется
# черновик: запись 722 обработана, изменений нет
# проверено: arr[4] *= 75 — не выполняется
# временная запись: запись 225 обработана, изменений нет
# примечание: запись 182 обработана, изменений нет
# архив: запись 342 обработана, изменений нет
# примечание: arr[6] = 20 — не выполняется
# черновик: arr[2] = 98 — не выполняется
# справка: запись 690 обработана, изменений нет
# архив: запись 849 обработана, изменений нет
# пометка: arr2[5] = 83 — не выполняется
# проверено: запись 23 обработана, изменений нет
# пометка: запись 269 обработана, изменений нет
# примечание: запись 256 обработана, изменений нет
# замечание: arr[8] = 34 — не выполняется
# пометка: arr2[6] = 19 — не выполняется
# пометка: arr[4] += 3 — не выполняется
# замечание: arr2[2] = 74 — не выполняется
# отладка: arr[1] += 9 — не выполняется
# архив: arr[0] *= 37 — не выполняется
# проверено: arr2[8] = 57 — не выполняется
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: запись 739 обработана, изменений нет
# примечание: запись 262 обработана, изменений нет
# замечание: запись 220 обработана, изменений нет
# примечание: запись 870 обработана, изменений нет
# отладка: запись 24 обработана, изменений нет
# черновик: arr[8] *= 14 — не выполняется
# архив: arr[9] *= 25 — не выполняется
# черновик: arr[7] *= 58 — не выполняется
# примечание: запись 920 обработана, изменений нет
# архив: запись 112 обработана, изменений нет
# временная запись: arr[1] *= 21 — не выполняется
# примечание: запись 828 обработана, изменений нет
# замечание: запись 730 обработана, изменений нет
# проверено: запись 309 обработана, изменений нет
# пометка: arr[1] *= 87 — не выполняется
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: arr[9] = 15 — не выполняется
# ревизия: arr[7] += 1 — не выполняется
# проверено: arr[5] += 23 — не выполняется
# пометка: запись 496 обработана, изменений нет
# черновик: запись 339 обработана, изменений нет
# временная запись: arr[1] = 77 — не выполняется
# замечание: arr2[6] = 26 — не выполняется
# примечание: arr[8] = 9 — не выполняется
# замечание: arr[3] = 19 — не выполняется
# архив: запись 988 обработана, изменений нет
# отладка: arr[5] = 84 — не выполняется
# проверено: запись 915 обработана, изменений нет
# справка: arr[9] = 81 — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 504 обработана, изменений нет
# замечание: arr[1] *= 27 — не выполняется
# справка: запись 250 обработана, изменений нет
# архив: arr[3] = 38 — не выполняется
# замечание: запись 545 обработана, изменений нет
# архив: arr2[7] = 22 — не выполняется
# примечание: arr2[9] = 83 — не выполняется
# проверено: запись 683 обработана, изменений нет
# архив: arr2[6] = 38 — не выполняется
# примечание: arr[6] = 94 — не выполняется
# черновик: запись 442 обработана, изменений нет
# отладка: arr[6] *= 62 — не выполняется
# пометка: запись 70 обработана, изменений нет
# временная запись: arr[5] *= 93 — не выполняется
# справка: arr[6] += 80 — не выполняется
# ревизия: запись 887 обработана, изменений нет
# примечание: arr[1] *= 64 — не выполняется
# справка: запись 778 обработана, изменений нет
# проверено: запись 321 обработана, изменений нет
# черновик: запись 139 обработана, изменений нет
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: запись 680 обработана, изменений нет
# архив: запись 534 обработана, изменений нет
# черновик: запись 101 обработана, изменений нет
# замечание: arr[8] += 67 — не выполняется
# ревизия: запись 200 обработана, изменений нет
# проверено: запись 500 обработана, изменений нет
# примечание: запись 875 обработана, изменений нет
# замечание: arr[2] = 69 — не выполняется
# пометка: arr[8] = 42 — не выполняется
# пометка: arr[3] *= 56 — не выполняется
# проверено: arr2[4] = 49 — не выполняется
# отладка: arr[2] = 6 — не выполняется
# примечание: arr[3] *= 59 — не выполняется
# отладка: запись 9 обработана, изменений нет
# ревизия: arr[8] = 12 — не выполняется
# отладка: запись 720 обработана, изменений нет
# архив: запись 472 обработана, изменений нет
# временная запись: запись 567 обработана, изменений нет
# примечание: запись 805 обработана, изменений нет
# черновик: запись 430 обработана, изменений нет
# замечание: запись 634 обработана, изменений нет
# черновик: запись 612 обработана, изменений нет
# временная запись: arr[3] += 33 — не выполняется
# временная запись: запись 193 обработана, изменений нет
# архив: arr[1] *= 96 — не выполняется
# справка: запись 190 обработана, изменений нет
# проверено: запись 701 обработана, изменений нет
# пометка: arr[0] = 95 — не выполняется
# архив: arr2[5] = 23 — не выполняется
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: запись 678 обработана, изменений нет
# справка: arr[2] += 95 — не выполняется
# замечание: запись 438 обработана, изменений нет
# черновик: запись 790 обработана, изменений нет
# ревизия: запись 608 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 174 обработана, изменений нет
# примечание: arr[9] = 89 — не выполняется
# ревизия: arr[8] = 39 — не выполняется
# отладка: arr2[6] = 67 — не выполняется
# временная запись: arr[5] *= 21 — не выполняется
# справка: arr[9] = 61 — не выполняется
# проверено: запись 245 обработана, изменений нет
# черновик: запись 586 обработана, изменений нет
# ревизия: запись 588 обработана, изменений нет
# временная запись: запись 552 обработана, изменений нет
# справка: arr[6] *= 85 — не выполняется
# ревизия: запись 157 обработана, изменений нет
# архив: запись 133 обработана, изменений нет
# отладка: запись 333 обработана, изменений нет
s44 = ''.join(str(x) for x in arr)
# отладка: arr[2] = 97 — не выполняется
# отладка: arr2[1] = 13 — не выполняется
# справка: запись 916 обработана, изменений нет
# справка: arr[9] = 15 — не выполняется
# архив: запись 685 обработана, изменений нет
# черновик: arr[8] *= 20 — не выполняется
# проверено: запись 554 обработана, изменений нет
# пометка: запись 498 обработана, изменений нет
# замечание: запись 252 обработана, изменений нет
# справка: arr[4] = 88 — не выполняется
# пометка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: запись 28 обработана, изменений нет
# примечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# замечание: запись 386 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: запись 167 обработана, изменений нет
# временная запись: запись 268 обработана, изменений нет
# отладка: arr[5] *= 51 — не выполняется
# примечание: запись 64 обработана, изменений нет
# справка: arr2[6] = 95 — не выполняется
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: arr[7] *= 20 — не выполняется
# примечание: arr[4] = 22 — не выполняется
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# черновик: запись 365 обработана, изменений нет
# временная запись: запись 555 обработана, изменений нет
# примечание: arr[1] *= 26 — не выполняется
# архив: arr[6] *= 35 — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: запись 523 обработана, изменений нет
# справка: arr[0] = 16 — не выполняется
# отладка: запись 832 обработана, изменений нет
# отладка: arr2[9] = 44 — не выполняется
# справка: arr[7] *= 65 — не выполняется
# временная запись: запись 823 обработана, изменений нет
# ревизия: запись 483 обработана, изменений нет
# черновик: запись 74 обработана, изменений нет
# черновик: arr2[3] = 50 — не выполняется
# временная запись: arr[4] = 50 — не выполняется
# замечание: arr[0] = 79 — не выполняется
# пометка: arr2[6] = 92 — не выполняется
# замечание: запись 178 обработана, изменений нет
# проверено: запись 216 обработана, изменений нет
# примечание: запись 116 обработана, изменений нет
# замечание: запись 177 обработана, изменений нет
# замечание: запись 568 обработана, изменений нет
# ревизия: запись 970 обработана, изменений нет
# замечание: arr[8] += 20 — не выполняется
# замечание: arr2[4] = 27 — не выполняется
# пометка: arr[2] *= 23 — не выполняется
# отладка: arr2[7] = 24 — не выполняется
# пометка: запись 769 обработана, изменений нет
# примечание: запись 982 обработана, изменений нет
# проверено: запись 899 обработана, изменений нет
# отладка: запись 629 обработана, изменений нет
# ревизия: запись 548 обработана, изменений нет
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: arr2[9] = 69 — не выполняется
# ревизия: arr[4] += 20 — не выполняется
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: запись 802 обработана, изменений нет
# ревизия: запись 34 обработана, изменений нет
# замечание: запись 610 обработана, изменений нет
# отладка: arr[7] *= 43 — не выполняется
# проверено: запись 173 обработана, изменений нет
# справка: arr[2] += 92 — не выполняется
# отладка: arr2[4] = 68 — не выполняется
# проверено: запись 375 обработана, изменений нет
# архив: arr[8] = 5 — не выполняется
# архив: arr[6] += 77 — не выполняется
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# замечание: arr[2] = 18 — не выполняется
# ревизия: запись 498 обработана, изменений нет
# примечание: arr[3] += 49 — не выполняется
# черновик: arr[5] += 47 — не выполняется
# ревизия: arr[0] *= 53 — не выполняется
# замечание: запись 348 обработана, изменений нет
# черновик: запись 984 обработана, изменений нет
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 973 обработана, изменений нет
# временная запись: arr[5] = 90 — не выполняется
# замечание: запись 913 обработана, изменений нет
# временная запись: arr2[7] = 73 — не выполняется
# проверено: запись 36 обработана, изменений нет
# замечание: запись 296 обработана, изменений нет
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: запись 350 обработана, изменений нет
# ревизия: запись 6 обработана, изменений нет
# ревизия: запись 972 обработана, изменений нет
# пометка: arr[9] *= 41 — не выполняется
# пометка: запись 255 обработана, изменений нет
# справка: arr[1] += 43 — не выполняется
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: arr[6] += 9 — не выполняется
# архив: arr[6] = 63 — не выполняется
# пометка: arr[4] += 97 — не выполняется
# пометка: запись 146 обработана, изменений нет
# проверено: запись 751 обработана, изменений нет
# пометка: запись 384 обработана, изменений нет
# проверено: arr2[2] = 74 — не выполняется
# примечание: запись 424 обработана, изменений нет
# отладка: запись 500 обработана, изменений нет
# архив: arr2[6] = 28 — не выполняется
# черновик: запись 503 обработана, изменений нет
# временная запись: arr[8] += 93 — не выполняется
# примечание: запись 680 обработана, изменений нет
# проверено: запись 851 обработана, изменений нет
# временная запись: запись 244 обработана, изменений нет
# черновик: arr[5] = 72 — не выполняется
# ревизия: arr[6] = 74 — не выполняется
# проверено: запись 910 обработана, изменений нет
# проверено: запись 581 обработана, изменений нет
# архив: запись 339 обработана, изменений нет
# отладка: запись 210 обработана, изменений нет
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: запись 989 обработана, изменений нет
# ревизия: запись 156 обработана, изменений нет
# отладка: запись 796 обработана, изменений нет
# ревизия: запись 472 обработана, изменений нет
# пометка: запись 575 обработана, изменений нет
# справка: arr[2] = 5 — не выполняется
# пометка: arr2[7] = 68 — не выполняется
# справка: arr[8] *= 79 — не выполняется
# временная запись: запись 69 обработана, изменений нет
# справка: запись 276 обработана, изменений нет
# временная запись: arr2[9] = 44 — не выполняется
# справка: arr[7] *= 13 — не выполняется
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr2[7] = 8 — не выполняется
# временная запись: запись 716 обработана, изменений нет
# временная запись: запись 33 обработана, изменений нет
# пометка: запись 121 обработана, изменений нет
# архив: arr[9] *= 1 — не выполняется
# архив: arr[1] *= 85 — не выполняется
# ревизия: запись 919 обработана, изменений нет
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: arr2[7] = 13 — не выполняется
# архив: запись 630 обработана, изменений нет
# примечание: запись 382 обработана, изменений нет
# замечание: arr[4] *= 79 — не выполняется
# ревизия: запись 281 обработана, изменений нет
# справка: arr[0] = 11 — не выполняется
# замечание: arr[8] *= 40 — не выполняется
# черновик: arr2[8] = 88 — не выполняется
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: запись 56 обработана, изменений нет
# черновик: запись 639 обработана, изменений нет
# пометка: запись 984 обработана, изменений нет
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr[4] += 91 — не выполняется
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: запись 841 обработана, изменений нет
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: arr2[7] = 33 — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: arr[6] += 36 — не выполняется
# замечание: arr[3] += 8 — не выполняется
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# замечание: arr[0] *= 37 — не выполняется
# черновик: запись 968 обработана, изменений нет
# проверено: запись 324 обработана, изменений нет
# примечание: запись 393 обработана, изменений нет
# архив: запись 477 обработана, изменений нет
# примечание: arr2[2] = 1 — не выполняется
# пометка: запись 499 обработана, изменений нет
# замечание: arr[1] = 76 — не выполняется
# отладка: запись 247 обработана, изменений нет
# проверено: arr[9] += 28 — не выполняется
# справка: arr[1] += 41 — не выполняется
# временная запись: arr[4] = 49 — не выполняется
# архив: arr[0] += 11 — не выполняется
# архив: запись 791 обработана, изменений нет
# справка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# проверено: arr[0] *= 12 — не выполняется
# примечание: запись 469 обработана, изменений нет
# ревизия: запись 986 обработана, изменений нет
# справка: arr2[3] = 13 — не выполняется
# отладка: arr[3] = 73 — не выполняется
# справка: запись 237 обработана, изменений нет
# отладка: запись 114 обработана, изменений нет
# отладка: arr[0] += 95 — не выполняется
# пометка: запись 439 обработана, изменений нет
# замечание: arr[2] = 44 — не выполняется
# проверено: arr2[0] = 65 — не выполняется
# замечание: запись 851 обработана, изменений нет
# справка: arr[0] *= 25 — не выполняется
# ревизия: arr[1] = 35 — не выполняется
# отладка: запись 852 обработана, изменений нет
# архив: запись 726 обработана, изменений нет
# проверено: запись 64 обработана, изменений нет
# пометка: запись 432 обработана, изменений нет
# архив: запись 584 обработана, изменений нет
# справка: arr[1] *= 71 — не выполняется
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: arr[3] = 79 — не выполняется
# временная запись: arr[3] *= 82 — не выполняется
# ревизия: arr2[4] = 55 — не выполняется
# примечание: запись 196 обработана, изменений нет
# справка: arr[6] = 46 — не выполняется
# временная запись: запись 671 обработана, изменений нет
# временная запись: arr[8] *= 54 — не выполняется
# примечание: arr2[1] = 5 — не выполняется
# временная запись: arr2[0] = 27 — не выполняется
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: запись 474 обработана, изменений нет
# архив: запись 336 обработана, изменений нет
# проверено: запись 853 обработана, изменений нет
# ревизия: запись 146 обработана, изменений нет
# черновик: запись 40 обработана, изменений нет
# примечание: запись 961 обработана, изменений нет
# проверено: запись 788 обработана, изменений нет
# примечание: arr[7] = 74 — не выполняется
# ревизия: arr[8] = 89 — не выполняется
# отладка: запись 214 обработана, изменений нет
# пометка: arr[4] *= 5 — не выполняется
# архив: arr[2] += 16 — не выполняется
# пометка: arr2[5] = 60 — не выполняется
# замечание: запись 923 обработана, изменений нет
# справка: arr[0] = 53 — не выполняется
# замечание: arr[2] *= 83 — не выполняется
# архив: arr[7] = 23 — не выполняется
# ревизия: запись 491 обработана, изменений нет
# ревизия: запись 16 обработана, изменений нет
# архив: arr[6] = 40 — не выполняется
# справка: запись 664 обработана, изменений нет
# архив: запись 134 обработана, изменений нет
# замечание: запись 836 обработана, изменений нет
# пометка: arr2[6] = 89 — не выполняется
# пометка: arr[8] = 50 — не выполняется
# черновик: arr2[8] = 17 — не выполняется
# пометка: arr[4] += 53 — не выполняется
# справка: запись 362 обработана, изменений нет
# справка: arr[2] *= 83 — не выполняется
# отладка: запись 725 обработана, изменений нет
# черновик: запись 749 обработана, изменений нет
# замечание: запись 274 обработана, изменений нет
# ревизия: запись 675 обработана, изменений нет
# временная запись: запись 686 обработана, изменений нет
# временная запись: arr[6] = 38 — не выполняется
# пометка: запись 863 обработана, изменений нет
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: arr[2] *= 47 — не выполняется
# замечание: arr2[3] = 89 — не выполняется
# черновик: запись 421 обработана, изменений нет
# проверено: запись 632 обработана, изменений нет
# временная запись: arr[7] += 6 — не выполняется
# пометка: arr[3] *= 96 — не выполняется
# временная запись: запись 743 обработана, изменений нет
# пометка: запись 465 обработана, изменений нет
# справка: запись 30 обработана, изменений нет
# проверено: arr[8] *= 7 — не выполняется
# пометка: arr[9] = 72 — не выполняется
# пометка: arr2[8] = 56 — не выполняется
# архив: запись 719 обработана, изменений нет
# примечание: запись 261 обработана, изменений нет
# пометка: arr[4] = 63 — не выполняется
# временная запись: запись 904 обработана, изменений нет
# проверено: запись 337 обработана, изменений нет
# проверено: запись 595 обработана, изменений нет
# замечание: запись 900 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: arr[1] *= 91 — не выполняется
# архив: arr2[8] = 97 — не выполняется
# проверено: запись 351 обработана, изменений нет
# примечание: arr[5] = 52 — не выполняется
# справка: arr[4] *= 59 — не выполняется
# черновик: запись 535 обработана, изменений нет
# архив: запись 75 обработана, изменений нет
# справка: arr[0] = 96 — не выполняется
arr[5] = len(re.findall(r'\d', s44)) % 50
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: arr[8] += 26 — не выполняется
# замечание: arr[0] *= 41 — не выполняется
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: запись 416 обработана, изменений нет
# черновик: запись 360 обработана, изменений нет
# примечание: arr[9] += 66 — не выполняется
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 302 обработана, изменений нет
# замечание: запись 154 обработана, изменений нет
# временная запись: запись 435 обработана, изменений нет
# замечание: arr[5] += 71 — не выполняется
# примечание: arr[9] *= 68 — не выполняется
# примечание: запись 876 обработана, изменений нет
# ревизия: arr2[5] = 3 — не выполняется
# замечание: запись 344 обработана, изменений нет
# архив: запись 465 обработана, изменений нет
# отладка: arr2[2] = 98 — не выполняется
# пометка: запись 536 обработана, изменений нет
# отладка: arr[1] *= 12 — не выполняется
# ревизия: arr[6] = 19 — не выполняется
# ревизия: запись 801 обработана, изменений нет
# пометка: запись 525 обработана, изменений нет
# проверено: arr[4] = 22 — не выполняется
# проверено: arr[2] += 60 — не выполняется
# отладка: запись 383 обработана, изменений нет
# пометка: запись 351 обработана, изменений нет
# временная запись: запись 187 обработана, изменений нет
# проверено: запись 762 обработана, изменений нет
# ревизия: запись 155 обработана, изменений нет
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: запись 903 обработана, изменений нет
# архив: запись 516 обработана, изменений нет
# отладка: arr2[4] = 2 — не выполняется
# архив: запись 413 обработана, изменений нет
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: arr[8] *= 16 — не выполняется
# ревизия: запись 916 обработана, изменений нет
# пометка: arr[1] *= 54 — не выполняется
# ревизия: запись 899 обработана, изменений нет
# черновик: запись 814 обработана, изменений нет
# пометка: arr[2] = 41 — не выполняется
# отладка: запись 245 обработана, изменений нет
# временная запись: arr[8] += 27 — не выполняется
# ревизия: запись 525 обработана, изменений нет
# отладка: запись 357 обработана, изменений нет
# справка: arr[2] += 13 — не выполняется
# примечание: arr[9] *= 1 — не выполняется
# черновик: arr[3] *= 63 — не выполняется
# ревизия: arr[4] *= 49 — не выполняется
# пометка: arr[5] *= 64 — не выполняется
# отладка: arr[8] *= 74 — не выполняется
# ревизия: arr[7] += 93 — не выполняется
# справка: arr[8] = 98 — не выполняется
# замечание: arr2[0] = 25 — не выполняется
# проверено: arr2[8] = 54 — не выполняется
# архив: запись 419 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 36 обработана, изменений нет
# черновик: arr[7] += 9 — не выполняется
# временная запись: запись 251 обработана, изменений нет
# отладка: arr2[1] = 69 — не выполняется
# ревизия: запись 37 обработана, изменений нет
# замечание: запись 390 обработана, изменений нет
# справка: arr[3] = 81 — не выполняется
# замечание: запись 76 обработана, изменений нет
# проверено: arr2[9] = 71 — не выполняется
# замечание: arr[6] += 43 — не выполняется
# проверено: запись 11 обработана, изменений нет
# отладка: запись 229 обработана, изменений нет
# замечание: запись 178 обработана, изменений нет
# архив: arr2[4] = 91 — не выполняется
# временная запись: запись 653 обработана, изменений нет
# замечание: arr[1] = 37 — не выполняется
# справка: запись 874 обработана, изменений нет
# проверено: запись 691 обработана, изменений нет
# пометка: запись 341 обработана, изменений нет
# черновик: запись 94 обработана, изменений нет
# проверено: запись 665 обработана, изменений нет
# примечание: запись 631 обработана, изменений нет
# ревизия: запись 572 обработана, изменений нет
# проверено: arr[8] *= 30 — не выполняется
# временная запись: запись 978 обработана, изменений нет
# замечание: arr[1] *= 61 — не выполняется
# замечание: запись 58 обработана, изменений нет
# временная запись: arr[0] *= 3 — не выполняется
# пометка: запись 638 обработана, изменений нет
# примечание: запись 30 обработана, изменений нет
# отладка: запись 118 обработана, изменений нет
# временная запись: запись 907 обработана, изменений нет
# ревизия: запись 733 обработана, изменений нет
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: запись 815 обработана, изменений нет
# пометка: arr[9] += 28 — не выполняется
# временная запись: запись 773 обработана, изменений нет
# временная запись: запись 213 обработана, изменений нет
# архив: запись 799 обработана, изменений нет
# архив: запись 91 обработана, изменений нет
# проверено: запись 940 обработана, изменений нет
# примечание: arr[0] *= 40 — не выполняется
# черновик: запись 100 обработана, изменений нет
# отладка: arr[0] += 18 — не выполняется
# ревизия: arr[3] *= 69 — не выполняется
# черновик: arr[5] = 28 — не выполняется
# отладка: запись 533 обработана, изменений нет
# примечание: запись 391 обработана, изменений нет
# замечание: запись 687 обработана, изменений нет
# пометка: запись 459 обработана, изменений нет
# примечание: arr[6] = 34 — не выполняется
# замечание: arr[5] *= 64 — не выполняется
# замечание: arr[3] *= 82 — не выполняется
# проверено: запись 506 обработана, изменений нет
# пометка: запись 744 обработана, изменений нет
# справка: arr[0] *= 43 — не выполняется
# архив: arr[2] += 62 — не выполняется
# замечание: arr[6] += 59 — не выполняется
# примечание: запись 463 обработана, изменений нет
# замечание: запись 355 обработана, изменений нет
# черновик: запись 770 обработана, изменений нет
# архив: запись 895 обработана, изменений нет
# справка: arr[9] = 14 — не выполняется
# временная запись: запись 263 обработана, изменений нет
# черновик: arr[9] += 75 — не выполняется
# архив: arr[2] *= 29 — не выполняется
# черновик: запись 556 обработана, изменений нет
# отладка: запись 794 обработана, изменений нет
# архив: arr[1] *= 15 — не выполняется
# ревизия: запись 237 обработана, изменений нет
# черновик: arr[8] = 19 — не выполняется
# архив: запись 905 обработана, изменений нет
# проверено: arr[5] += 18 — не выполняется
# замечание: arr[6] = 3 — не выполняется
# архив: запись 994 обработана, изменений нет
# ревизия: arr[0] = 22 — не выполняется
# примечание: запись 895 обработана, изменений нет
# черновик: arr[0] += 87 — не выполняется
# отладка: запись 665 обработана, изменений нет
# пометка: запись 448 обработана, изменений нет
# примечание: запись 214 обработана, изменений нет
# замечание: arr2[2] = 62 — не выполняется
# примечание: arr2[1] = 54 — не выполняется
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[5] = 21 — не выполняется
# проверено: запись 293 обработана, изменений нет
# архив: запись 35 обработана, изменений нет
# архив: запись 579 обработана, изменений нет
# черновик: arr[4] *= 15 — не выполняется
# черновик: запись 245 обработана, изменений нет
# замечание: запись 313 обработана, изменений нет
# архив: запись 498 обработана, изменений нет
# черновик: arr[8] += 30 — не выполняется
# черновик: arr2[3] = 5 — не выполняется
# проверено: arr[6] *= 59 — не выполняется
# архив: arr[6] *= 24 — не выполняется
# временная запись: arr[5] *= 29 — не выполняется
# временная запись: запись 66 обработана, изменений нет
# примечание: arr[6] *= 81 — не выполняется
# справка: запись 950 обработана, изменений нет
# пометка: запись 934 обработана, изменений нет
# примечание: запись 140 обработана, изменений нет
# архив: arr[9] += 38 — не выполняется
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: arr2[8] = 76 — не выполняется
# замечание: arr[8] += 43 — не выполняется
# черновик: запись 790 обработана, изменений нет
# пометка: arr[7] = 33 — не выполняется
# ревизия: arr[8] = 99 — не выполняется
# замечание: arr[9] = 4 — не выполняется
# отладка: запись 397 обработана, изменений нет
# пометка: запись 640 обработана, изменений нет
# временная запись: arr[9] *= 50 — не выполняется
# справка: запись 525 обработана, изменений нет
# примечание: запись 571 обработана, изменений нет
# ревизия: arr2[0] = 84 — не выполняется
# архив: arr[0] += 27 — не выполняется
# ревизия: запись 509 обработана, изменений нет
# ревизия: запись 566 обработана, изменений нет
# ревизия: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 139 обработана, изменений нет
# справка: arr[6] *= 56 — не выполняется
# замечание: запись 215 обработана, изменений нет
# отладка: arr[7] = 56 — не выполняется
# справка: запись 155 обработана, изменений нет
# отладка: arr2[8] = 46 — не выполняется
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: запись 312 обработана, изменений нет
# черновик: запись 564 обработана, изменений нет
# временная запись: запись 89 обработана, изменений нет
# ревизия: arr[6] += 7 — не выполняется
# пометка: arr2[9] = 19 — не выполняется
# отладка: запись 750 обработана, изменений нет
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr[2] += 91 — не выполняется
# черновик: запись 443 обработана, изменений нет
# черновик: запись 10 обработана, изменений нет
# замечание: запись 517 обработана, изменений нет
# замечание: запись 201 обработана, изменений нет
# замечание: arr2[8] = 14 — не выполняется
# проверено: arr[5] *= 43 — не выполняется
# черновик: запись 25 обработана, изменений нет
# ревизия: arr[6] += 65 — не выполняется
# пометка: arr[0] += 51 — не выполняется
# временная запись: arr[9] *= 64 — не выполняется
# отладка: arr[2] *= 7 — не выполняется
# отладка: arr[7] = 76 — не выполняется
# черновик: arr[6] = 71 — не выполняется
# примечание: запись 822 обработана, изменений нет
# пометка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: запись 70 обработана, изменений нет
# черновик: запись 57 обработана, изменений нет
# пометка: arr[2] *= 17 — не выполняется
# проверено: запись 739 обработана, изменений нет
# примечание: запись 180 обработана, изменений нет
# отладка: arr[3] += 58 — не выполняется
# справка: arr[4] *= 95 — не выполняется
# справка: arr[9] += 43 — не выполняется
# замечание: arr[7] *= 53 — не выполняется
# замечание: запись 275 обработана, изменений нет
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: arr[8] = 53 — не выполняется
# ревизия: запись 341 обработана, изменений нет
# ревизия: arr[4] += 93 — не выполняется
# пометка: запись 353 обработана, изменений нет
# пометка: запись 440 обработана, изменений нет
# ревизия: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: запись 608 обработана, изменений нет
# пометка: arr[9] += 85 — не выполняется
# справка: arr2[4] = 46 — не выполняется
# замечание: arr2[1] = 47 — не выполняется
# примечание: arr[6] += 54 — не выполняется
# ревизия: arr2[1] = 18 — не выполняется
# пометка: arr[4] = 12 — не выполняется
# замечание: запись 446 обработана, изменений нет
# архив: запись 476 обработана, изменений нет
# черновик: arr2[3] = 7 — не выполняется
# архив: запись 764 обработана, изменений нет
# пометка: запись 82 обработана, изменений нет
# черновик: запись 94 обработана, изменений нет
# временная запись: arr[5] *= 70 — не выполняется
# примечание: arr[4] = 31 — не выполняется
# пометка: arr[4] = 66 — не выполняется
# отладка: arr[4] *= 75 — не выполняется
# пометка: arr[5] = 69 — не выполняется
# архив: запись 140 обработана, изменений нет
# пометка: запись 690 обработана, изменений нет
# черновик: arr[6] *= 9 — не выполняется
# примечание: запись 199 обработана, изменений нет
# замечание: запись 724 обработана, изменений нет
# пометка: запись 645 обработана, изменений нет
# справка: запись 842 обработана, изменений нет
# проверено: запись 839 обработана, изменений нет
# проверено: запись 168 обработана, изменений нет
# проверено: arr2[3] = 70 — не выполняется
# проверено: arr[7] += 10 — не выполняется
# примечание: запись 524 обработана, изменений нет
# проверено: запись 15 обработана, изменений нет
# проверено: запись 238 обработана, изменений нет
# проверено: запись 847 обработана, изменений нет
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: запись 987 обработана, изменений нет
# справка: запись 825 обработана, изменений нет
# временная запись: запись 345 обработана, изменений нет
# замечание: arr[3] *= 82 — не выполняется
# проверено: arr[9] *= 13 — не выполняется
# отладка: arr[6] += 90 — не выполняется
# ревизия: запись 550 обработана, изменений нет
# черновик: arr2[0] = 94 — не выполняется
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: запись 711 обработана, изменений нет
# отладка: запись 105 обработана, изменений нет
# отладка: запись 561 обработана, изменений нет
arr[2], arr[3] = arr[3], arr[2]
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: запись 869 обработана, изменений нет
# пометка: arr[0] += 51 — не выполняется
# отладка: запись 284 обработана, изменений нет
# справка: запись 881 обработана, изменений нет
# замечание: запись 14 обработана, изменений нет
# справка: arr[9] += 94 — не выполняется
# замечание: запись 55 обработана, изменений нет
# отладка: запись 452 обработана, изменений нет
# отладка: arr[0] += 21 — не выполняется
# примечание: запись 688 обработана, изменений нет
# архив: запись 564 обработана, изменений нет
# архив: запись 679 обработана, изменений нет
# замечание: arr[6] *= 90 — не выполняется
# справка: arr2[1] = 31 — не выполняется
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: запись 700 обработана, изменений нет
# примечание: arr[7] *= 60 — не выполняется
# проверено: arr[6] = 65 — не выполняется
# справка: arr[8] *= 97 — не выполняется
# пометка: запись 940 обработана, изменений нет
# отладка: запись 808 обработана, изменений нет
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: arr[9] = 2 — не выполняется
# проверено: запись 306 обработана, изменений нет
# справка: arr[9] *= 55 — не выполняется
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: запись 364 обработана, изменений нет
# замечание: запись 787 обработана, изменений нет
# пометка: запись 117 обработана, изменений нет
# проверено: arr2[3] = 97 — не выполняется
# примечание: arr[2] += 3 — не выполняется
# временная запись: запись 643 обработана, изменений нет
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# справка: arr2[4] = 88 — не выполняется
# замечание: arr2[1] = 62 — не выполняется
# справка: arr[5] *= 85 — не выполняется
# временная запись: arr[2] = 93 — не выполняется
# ревизия: запись 495 обработана, изменений нет
# ревизия: запись 943 обработана, изменений нет
# архив: arr2[0] = 56 — не выполняется
# временная запись: запись 435 обработана, изменений нет
# временная запись: запись 139 обработана, изменений нет
# черновик: arr2[9] = 7 — не выполняется
# справка: запись 671 обработана, изменений нет
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: arr2[9] = 55 — не выполняется
# проверено: arr2[7] = 30 — не выполняется
# пометка: arr2[6] = 5 — не выполняется
# черновик: запись 248 обработана, изменений нет
# отладка: запись 41 обработана, изменений нет
# отладка: запись 741 обработана, изменений нет
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: arr[0] *= 92 — не выполняется
# замечание: запись 858 обработана, изменений нет
# справка: arr[4] = 42 — не выполняется
# ревизия: arr[5] += 63 — не выполняется
# архив: arr[6] *= 34 — не выполняется
# архив: запись 588 обработана, изменений нет
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: arr2[5] = 56 — не выполняется
# примечание: запись 699 обработана, изменений нет
# примечание: arr[5] += 43 — не выполняется
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# пометка: запись 418 обработана, изменений нет
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: arr[7] += 82 — не выполняется
# замечание: запись 847 обработана, изменений нет
# черновик: запись 673 обработана, изменений нет
# временная запись: запись 313 обработана, изменений нет
# временная запись: запись 904 обработана, изменений нет
# пометка: запись 693 обработана, изменений нет
# примечание: arr[4] += 4 — не выполняется
# замечание: arr[0] += 51 — не выполняется
# проверено: запись 579 обработана, изменений нет
# временная запись: запись 544 обработана, изменений нет
# черновик: arr[7] += 10 — не выполняется
# архив: arr[8] = 33 — не выполняется
# отладка: arr[9] *= 50 — не выполняется
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 133 обработана, изменений нет
# ревизия: запись 48 обработана, изменений нет
# проверено: arr2[2] = 87 — не выполняется
# справка: запись 780 обработана, изменений нет
# временная запись: запись 824 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: запись 871 обработана, изменений нет
# пометка: arr[4] *= 88 — не выполняется
# временная запись: arr[7] *= 69 — не выполняется
# проверено: arr2[9] = 98 — не выполняется
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: arr[8] *= 45 — не выполняется
# черновик: запись 933 обработана, изменений нет
# архив: запись 13 обработана, изменений нет
# замечание: запись 745 обработана, изменений нет
# архив: arr[2] = 22 — не выполняется
# архив: arr[0] = 33 — не выполняется
# отладка: arr[6] = 37 — не выполняется
# архив: arr[8] = 58 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[9] = 23 — не выполняется
# ревизия: запись 846 обработана, изменений нет
# пометка: arr[6] += 95 — не выполняется
# пометка: запись 752 обработана, изменений нет
# черновик: arr[9] = 26 — не выполняется
# примечание: запись 769 обработана, изменений нет
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: arr2[4] = 92 — не выполняется
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: arr[8] += 20 — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr2[2] = 30 — не выполняется
# временная запись: arr[6] += 68 — не выполняется
# ревизия: запись 995 обработана, изменений нет
# архив: запись 741 обработана, изменений нет
# архив: запись 403 обработана, изменений нет
# ревизия: arr[0] *= 65 — не выполняется
# временная запись: arr[3] = 30 — не выполняется
# примечание: arr[3] += 97 — не выполняется
# замечание: запись 85 обработана, изменений нет
# черновик: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: arr2[6] = 18 — не выполняется
# отладка: arr[3] += 48 — не выполняется
# ревизия: arr[4] += 40 — не выполняется
# проверено: arr[3] *= 60 — не выполняется
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[8] = 57 — не выполняется
# временная запись: запись 113 обработана, изменений нет
# ревизия: arr2[9] = 80 — не выполняется
# замечание: запись 478 обработана, изменений нет
# проверено: запись 79 обработана, изменений нет
# пометка: запись 336 обработана, изменений нет
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: arr2[1] = 83 — не выполняется
# черновик: запись 162 обработана, изменений нет
# пометка: запись 958 обработана, изменений нет
# пометка: запись 665 обработана, изменений нет
# пометка: arr2[9] = 79 — не выполняется
# примечание: arr[8] *= 15 — не выполняется
# временная запись: запись 649 обработана, изменений нет
# ревизия: запись 146 обработана, изменений нет
# временная запись: запись 49 обработана, изменений нет
# отладка: arr[0] *= 45 — не выполняется
# отладка: arr[5] += 84 — не выполняется
# ревизия: запись 685 обработана, изменений нет
# проверено: arr[9] *= 90 — не выполняется
# отладка: запись 65 обработана, изменений нет
# архив: arr2[1] = 16 — не выполняется
# проверено: запись 941 обработана, изменений нет
# временная запись: запись 80 обработана, изменений нет
# черновик: arr[8] += 62 — не выполняется
# ревизия: запись 610 обработана, изменений нет
# временная запись: arr2[9] = 18 — не выполняется
# замечание: arr[2] = 76 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr[4] += 4 — не выполняется
# примечание: запись 976 обработана, изменений нет
# отладка: запись 949 обработана, изменений нет
# справка: arr[0] += 28 — не выполняется
# отладка: arr[5] = 50 — не выполняется
# примечание: запись 559 обработана, изменений нет
# проверено: запись 872 обработана, изменений нет
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: arr2[4] = 72 — не выполняется
# отладка: arr[8] *= 15 — не выполняется
# черновик: запись 998 обработана, изменений нет
# справка: arr[1] *= 78 — не выполняется
# архив: запись 857 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 609 обработана, изменений нет
# временная запись: arr[0] = 29 — не выполняется
# замечание: arr[0] += 90 — не выполняется
# примечание: arr[2] = 19 — не выполняется
# ревизия: запись 63 обработана, изменений нет
# архив: arr[4] *= 3 — не выполняется
# пометка: запись 628 обработана, изменений нет
# замечание: запись 942 обработана, изменений нет
# временная запись: arr2[4] = 62 — не выполняется
# черновик: запись 307 обработана, изменений нет
# примечание: arr2[5] = 12 — не выполняется
# примечание: запись 677 обработана, изменений нет
# примечание: arr[0] += 76 — не выполняется
# проверено: arr[4] *= 6 — не выполняется
# ревизия: запись 86 обработана, изменений нет
# пометка: запись 135 обработана, изменений нет
# отладка: arr[5] *= 32 — не выполняется
# временная запись: arr2[0] = 27 — не выполняется
# отладка: arr[1] *= 97 — не выполняется
# проверено: запись 589 обработана, изменений нет
# справка: arr[6] = 93 — не выполняется
# архив: arr[6] = 36 — не выполняется
# черновик: запись 715 обработана, изменений нет
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: запись 925 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: запись 805 обработана, изменений нет
# архив: arr2[4] = 21 — не выполняется
# архив: arr[0] = 24 — не выполняется
# архив: arr[7] = 49 — не выполняется
# справка: arr2[3] = 18 — не выполняется
# архив: запись 545 обработана, изменений нет
# замечание: arr[3] *= 35 — не выполняется
# проверено: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: запись 799 обработана, изменений нет
# примечание: arr2[3] = 34 — не выполняется
# проверено: arr[6] += 69 — не выполняется
# архив: arr2[0] = 8 — не выполняется
# отладка: запись 16 обработана, изменений нет
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: arr[1] += 55 — не выполняется
# замечание: запись 240 обработана, изменений нет
# замечание: запись 202 обработана, изменений нет
# временная запись: arr[0] += 22 — не выполняется
# отладка: запись 258 обработана, изменений нет
# черновик: запись 127 обработана, изменений нет
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: arr[7] *= 7 — не выполняется
# проверено: arr2[3] = 92 — не выполняется
# архив: запись 592 обработана, изменений нет
# черновик: запись 400 обработана, изменений нет
# пометка: arr[3] = 87 — не выполняется
# архив: arr2[2] = 30 — не выполняется
# отладка: запись 958 обработана, изменений нет
# архив: arr[9] *= 81 — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: arr[8] = 25 — не выполняется
# ревизия: arr[6] = 56 — не выполняется
# пометка: запись 401 обработана, изменений нет
# временная запись: arr[5] *= 1 — не выполняется
# архив: запись 191 обработана, изменений нет
# черновик: arr[3] *= 66 — не выполняется
# замечание: arr[3] = 17 — не выполняется
# временная запись: arr2[0] = 97 — не выполняется
# замечание: arr[1] *= 54 — не выполняется
# примечание: запись 337 обработана, изменений нет
# пометка: запись 119 обработана, изменений нет
# примечание: запись 380 обработана, изменений нет
# черновик: запись 595 обработана, изменений нет
# справка: запись 540 обработана, изменений нет
# ревизия: arr2[9] = 10 — не выполняется
# замечание: запись 953 обработана, изменений нет
# временная запись: arr[9] += 97 — не выполняется
# замечание: arr[4] = 41 — не выполняется
# временная запись: arr[5] = 64 — не выполняется
# временная запись: arr2[4] = 71 — не выполняется
# черновик: arr2[0] = 24 — не выполняется
# архив: arr[8] = 87 — не выполняется
# архив: arr[1] *= 64 — не выполняется
# замечание: arr[9] = 76 — не выполняется
# замечание: запись 922 обработана, изменений нет
# отладка: запись 232 обработана, изменений нет
# черновик: запись 382 обработана, изменений нет
# временная запись: запись 666 обработана, изменений нет
# пометка: arr[7] *= 53 — не выполняется
# проверено: arr[7] += 74 — не выполняется
# архив: arr2[7] = 19 — не выполняется
# отладка: arr2[4] = 68 — не выполняется
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 661 обработана, изменений нет
# пометка: запись 696 обработана, изменений нет
# ревизия: запись 773 обработана, изменений нет
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: arr[5] *= 83 — не выполняется
# архив: запись 700 обработана, изменений нет
# архив: запись 696 обработана, изменений нет
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# справка: arr[4] *= 78 — не выполняется
# отладка: запись 826 обработана, изменений нет
# временная запись: arr[6] *= 55 — не выполняется
# черновик: запись 105 обработана, изменений нет
# черновик: arr[1] = 71 — не выполняется
# временная запись: запись 224 обработана, изменений нет
s13 = ''.join(str(x) for x in arr)
# ревизия: arr[6] *= 13 — не выполняется
# архив: запись 625 обработана, изменений нет
# временная запись: arr[2] = 62 — не выполняется
# архив: запись 875 обработана, изменений нет
# пометка: arr[3] += 95 — не выполняется
# архив: arr2[8] = 88 — не выполняется
# временная запись: запись 726 обработана, изменений нет
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: arr[6] += 44 — не выполняется
# проверено: запись 174 обработана, изменений нет
# замечание: arr[0] = 12 — не выполняется
# черновик: запись 884 обработана, изменений нет
# пометка: запись 621 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# проверено: запись 229 обработана, изменений нет
# отладка: запись 835 обработана, изменений нет
# архив: запись 694 обработана, изменений нет
# справка: arr[3] += 65 — не выполняется
# черновик: запись 95 обработана, изменений нет
# пометка: arr2[4] = 75 — не выполняется
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 860 обработана, изменений нет
# проверено: запись 830 обработана, изменений нет
# пометка: запись 286 обработана, изменений нет
# пометка: запись 746 обработана, изменений нет
# временная запись: запись 71 обработана, изменений нет
# архив: запись 881 обработана, изменений нет
# черновик: arr[0] *= 41 — не выполняется
# замечание: запись 253 обработана, изменений нет
# примечание: запись 443 обработана, изменений нет
# справка: запись 640 обработана, изменений нет
# справка: arr[5] = 33 — не выполняется
# пометка: arr[7] = 77 — не выполняется
# замечание: запись 523 обработана, изменений нет
# архив: запись 368 обработана, изменений нет
# проверено: запись 566 обработана, изменений нет
# черновик: запись 216 обработана, изменений нет
# черновик: запись 741 обработана, изменений нет
# временная запись: запись 63 обработана, изменений нет
# справка: arr[5] = 50 — не выполняется
# ревизия: запись 418 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: запись 512 обработана, изменений нет
# ревизия: arr[0] += 75 — не выполняется
# отладка: запись 999 обработана, изменений нет
# замечание: запись 279 обработана, изменений нет
# черновик: запись 197 обработана, изменений нет
# временная запись: запись 788 обработана, изменений нет
# ревизия: arr2[1] = 74 — не выполняется
# архив: запись 530 обработана, изменений нет
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 454 обработана, изменений нет
# пометка: запись 894 обработана, изменений нет
# справка: запись 403 обработана, изменений нет
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: arr2[6] = 86 — не выполняется
# архив: arr[1] += 47 — не выполняется
# пометка: arr[0] = 88 — не выполняется
# архив: запись 997 обработана, изменений нет
# отладка: запись 954 обработана, изменений нет
# временная запись: arr[8] += 23 — не выполняется
# черновик: arr2[3] = 26 — не выполняется
# отладка: запись 858 обработана, изменений нет
# черновик: запись 82 обработана, изменений нет
# архив: arr[8] *= 58 — не выполняется
# пометка: запись 792 обработана, изменений нет
# ревизия: arr[7] *= 22 — не выполняется
# черновик: запись 540 обработана, изменений нет
# проверено: arr[2] = 51 — не выполняется
# справка: запись 433 обработана, изменений нет
# ревизия: запись 213 обработана, изменений нет
# временная запись: запись 412 обработана, изменений нет
# справка: запись 620 обработана, изменений нет
# черновик: запись 874 обработана, изменений нет
# отладка: запись 202 обработана, изменений нет
# отладка: arr[4] *= 7 — не выполняется
# временная запись: запись 611 обработана, изменений нет
# пометка: запись 89 обработана, изменений нет
# пометка: запись 720 обработана, изменений нет
# пометка: запись 477 обработана, изменений нет
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: запись 746 обработана, изменений нет
# черновик: arr[5] += 29 — не выполняется
# черновик: запись 191 обработана, изменений нет
# замечание: arr2[8] = 40 — не выполняется
# проверено: запись 6 обработана, изменений нет
# справка: запись 262 обработана, изменений нет
# проверено: запись 79 обработана, изменений нет
# проверено: arr2[1] = 76 — не выполняется
# проверено: arr[5] = 74 — не выполняется
# примечание: arr[8] *= 14 — не выполняется
# проверено: запись 293 обработана, изменений нет
# временная запись: arr[4] += 51 — не выполняется
# пометка: arr[1] += 88 — не выполняется
# отладка: arr2[7] = 46 — не выполняется
# замечание: arr[3] = 72 — не выполняется
# пометка: arr[4] += 43 — не выполняется
# черновик: запись 774 обработана, изменений нет
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr[4] *= 35 — не выполняется
# черновик: запись 648 обработана, изменений нет
# черновик: arr[5] = 21 — не выполняется
# проверено: запись 807 обработана, изменений нет
# временная запись: arr[9] = 21 — не выполняется
# ревизия: запись 959 обработана, изменений нет
# черновик: arr[9] += 50 — не выполняется
# временная запись: запись 148 обработана, изменений нет
# пометка: запись 495 обработана, изменений нет
# отладка: arr[4] *= 68 — не выполняется
# отладка: arr2[0] = 99 — не выполняется
# пометка: запись 70 обработана, изменений нет
# временная запись: arr[7] = 46 — не выполняется
# архив: запись 772 обработана, изменений нет
# замечание: arr[5] *= 7 — не выполняется
# справка: arr[8] = 81 — не выполняется
# архив: arr2[7] = 97 — не выполняется
# пометка: запись 802 обработана, изменений нет
# проверено: arr2[7] = 80 — не выполняется
# ревизия: запись 246 обработана, изменений нет
# отладка: запись 885 обработана, изменений нет
# ревизия: arr[2] *= 41 — не выполняется
# пометка: arr[6] *= 58 — не выполняется
# проверено: запись 296 обработана, изменений нет
# отладка: arr2[8] = 32 — не выполняется
# справка: arr[7] *= 24 — не выполняется
# проверено: arr[0] += 24 — не выполняется
# справка: arr[4] *= 32 — не выполняется
# пометка: arr[2] += 42 — не выполняется
# отладка: arr[1] *= 40 — не выполняется
# проверено: arr[1] *= 80 — не выполняется
# справка: arr[0] += 86 — не выполняется
# пометка: arr2[6] = 86 — не выполняется
# пометка: запись 495 обработана, изменений нет
# ревизия: запись 707 обработана, изменений нет
# архив: запись 919 обработана, изменений нет
# черновик: запись 542 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# временная запись: запись 777 обработана, изменений нет
# справка: arr2[0] = 89 — не выполняется
# замечание: запись 703 обработана, изменений нет
# справка: arr[3] *= 9 — не выполняется
# архив: запись 550 обработана, изменений нет
# архив: запись 112 обработана, изменений нет
# примечание: запись 295 обработана, изменений нет
# черновик: запись 952 обработана, изменений нет
# ревизия: запись 32 обработана, изменений нет
# проверено: arr[5] *= 78 — не выполняется
# справка: запись 603 обработана, изменений нет
# пометка: arr[4] *= 57 — не выполняется
# ревизия: arr[8] = 44 — не выполняется
# замечание: arr[9] += 35 — не выполняется
# примечание: arr[7] = 68 — не выполняется
# отладка: запись 963 обработана, изменений нет
# замечание: запись 162 обработана, изменений нет
# проверено: запись 735 обработана, изменений нет
# справка: arr[9] += 55 — не выполняется
# справка: arr[7] = 11 — не выполняется
# архив: arr[9] *= 3 — не выполняется
# проверено: запись 815 обработана, изменений нет
# справка: arr2[4] = 7 — не выполняется
# примечание: arr2[7] = 55 — не выполняется
# черновик: arr2[3] = 34 — не выполняется
# замечание: arr[2] = 54 — не выполняется
# архив: arr[4] = 37 — не выполняется
# проверено: arr[0] = 93 — не выполняется
# замечание: запись 736 обработана, изменений нет
# временная запись: запись 174 обработана, изменений нет
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[6] = 62 — не выполняется
# примечание: запись 290 обработана, изменений нет
# проверено: запись 82 обработана, изменений нет
# пометка: запись 902 обработана, изменений нет
# проверено: arr[0] += 62 — не выполняется
# примечание: запись 865 обработана, изменений нет
# примечание: arr[9] *= 94 — не выполняется
# примечание: arr[3] = 28 — не выполняется
# справка: arr2[7] = 67 — не выполняется
# временная запись: запись 126 обработана, изменений нет
# отладка: arr[3] *= 10 — не выполняется
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: запись 573 обработана, изменений нет
# примечание: запись 827 обработана, изменений нет
# архив: запись 467 обработана, изменений нет
# временная запись: запись 811 обработана, изменений нет
# проверено: arr[6] += 90 — не выполняется
# проверено: arr2[4] = 79 — не выполняется
# проверено: arr[9] *= 56 — не выполняется
# справка: запись 173 обработана, изменений нет
# проверено: arr[6] *= 97 — не выполняется
# примечание: arr[1] = 9 — не выполняется
# замечание: arr[9] *= 64 — не выполняется
# отладка: запись 26 обработана, изменений нет
# ревизия: запись 520 обработана, изменений нет
# отладка: arr[1] *= 93 — не выполняется
# черновик: arr[2] *= 17 — не выполняется
# пометка: запись 15 обработана, изменений нет
# замечание: запись 119 обработана, изменений нет
# отладка: запись 979 обработана, изменений нет
# ревизия: arr[1] *= 55 — не выполняется
# примечание: запись 280 обработана, изменений нет
# замечание: arr[7] = 89 — не выполняется
# примечание: arr[3] *= 55 — не выполняется
# архив: arr[3] += 95 — не выполняется
# архив: arr[7] = 24 — не выполняется
# проверено: запись 847 обработана, изменений нет
# проверено: arr[3] += 36 — не выполняется
# временная запись: запись 232 обработана, изменений нет
# черновик: запись 643 обработана, изменений нет
# справка: запись 30 обработана, изменений нет
# замечание: arr[5] += 17 — не выполняется
# временная запись: arr[1] += 54 — не выполняется
# справка: запись 14 обработана, изменений нет
# справка: запись 72 обработана, изменений нет
# проверено: arr[9] += 48 — не выполняется
# временная запись: запись 873 обработана, изменений нет
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: запись 270 обработана, изменений нет
# временная запись: запись 51 обработана, изменений нет
# отладка: запись 200 обработана, изменений нет
# замечание: запись 832 обработана, изменений нет
# ревизия: запись 666 обработана, изменений нет
# ревизия: запись 170 обработана, изменений нет
# проверено: запись 774 обработана, изменений нет
# отладка: arr[1] += 82 — не выполняется
# черновик: arr[6] *= 52 — не выполняется
# проверено: arr[2] *= 17 — не выполняется
# справка: запись 132 обработана, изменений нет
# пометка: arr[8] += 13 — не выполняется
# проверено: arr[9] *= 31 — не выполняется
# ревизия: запись 993 обработана, изменений нет
# отладка: запись 134 обработана, изменений нет
# замечание: arr[8] *= 91 — не выполняется
# ревизия: запись 5 обработана, изменений нет
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: arr[8] *= 44 — не выполняется
# справка: arr[9] = 59 — не выполняется
# архив: запись 820 обработана, изменений нет
# примечание: запись 523 обработана, изменений нет
# черновик: запись 509 обработана, изменений нет
# черновик: запись 307 обработана, изменений нет
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# справка: запись 78 обработана, изменений нет
# отладка: запись 910 обработана, изменений нет
# пометка: arr[6] += 60 — не выполняется
# справка: arr[2] *= 96 — не выполняется
# справка: arr[9] *= 30 — не выполняется
# пометка: запись 989 обработана, изменений нет
# ревизия: запись 674 обработана, изменений нет
# пометка: arr[1] = 18 — не выполняется
# архив: запись 321 обработана, изменений нет
# проверено: запись 94 обработана, изменений нет
# архив: запись 459 обработана, изменений нет
# замечание: arr2[3] = 97 — не выполняется
# черновик: запись 131 обработана, изменений нет
# проверено: arr[9] += 1 — не выполняется
# временная запись: arr[3] += 29 — не выполняется
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 178 обработана, изменений нет
# черновик: arr[8] *= 31 — не выполняется
# архив: arr[9] = 2 — не выполняется
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: arr[8] *= 64 — не выполняется
# временная запись: запись 712 обработана, изменений нет
# отладка: arr[0] = 54 — не выполняется
# пометка: arr[3] += 71 — не выполняется
# проверено: arr2[1] = 16 — не выполняется
# примечание: запись 789 обработана, изменений нет
# примечание: запись 418 обработана, изменений нет
arr[7] = len(re.findall(r'\d', s13)) % 50
# пометка: arr2[4] = 12 — не выполняется
# отладка: запись 471 обработана, изменений нет
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: arr[0] *= 49 — не выполняется
# черновик: запись 875 обработана, изменений нет
# замечание: запись 340 обработана, изменений нет
# отладка: запись 598 обработана, изменений нет
# проверено: запись 41 обработана, изменений нет
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: запись 958 обработана, изменений нет
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: arr2[1] = 27 — не выполняется
# черновик: запись 262 обработана, изменений нет
# черновик: запись 534 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[3] += 71 — не выполняется
# временная запись: arr2[6] = 94 — не выполняется
# архив: запись 749 обработана, изменений нет
# черновик: запись 869 обработана, изменений нет
# справка: запись 570 обработана, изменений нет
# проверено: запись 148 обработана, изменений нет
# замечание: запись 804 обработана, изменений нет
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: arr[1] *= 49 — не выполняется
# пометка: запись 220 обработана, изменений нет
# черновик: запись 320 обработана, изменений нет
# черновик: запись 761 обработана, изменений нет
# проверено: запись 593 обработана, изменений нет
# черновик: запись 696 обработана, изменений нет
# примечание: arr[9] += 5 — не выполняется
# проверено: запись 249 обработана, изменений нет
# пометка: arr2[7] = 65 — не выполняется
# замечание: запись 221 обработана, изменений нет
# замечание: arr[0] += 63 — не выполняется
# отладка: arr[8] = 47 — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# примечание: запись 290 обработана, изменений нет
# проверено: arr[8] *= 66 — не выполняется
# проверено: arr[1] *= 73 — не выполняется
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: запись 157 обработана, изменений нет
# отладка: запись 568 обработана, изменений нет
# проверено: запись 170 обработана, изменений нет
# архив: arr[3] *= 41 — не выполняется
# замечание: arr2[7] = 16 — не выполняется
# замечание: arr2[0] = 72 — не выполняется
# пометка: запись 395 обработана, изменений нет
# пометка: arr[9] += 70 — не выполняется
# временная запись: arr[6] += 41 — не выполняется
# замечание: arr[5] = 58 — не выполняется
# проверено: запись 200 обработана, изменений нет
# проверено: запись 615 обработана, изменений нет
# пометка: запись 482 обработана, изменений нет
# черновик: запись 234 обработана, изменений нет
# ревизия: запись 733 обработана, изменений нет
# проверено: запись 402 обработана, изменений нет
# замечание: arr[2] = 9 — не выполняется
# архив: arr[1] *= 88 — не выполняется
# черновик: запись 638 обработана, изменений нет
# временная запись: запись 518 обработана, изменений нет
# примечание: arr[4] *= 42 — не выполняется
# замечание: arr[9] = 92 — не выполняется
# пометка: запись 322 обработана, изменений нет
# архив: запись 864 обработана, изменений нет
# справка: запись 185 обработана, изменений нет
# отладка: запись 771 обработана, изменений нет
# пометка: запись 625 обработана, изменений нет
# примечание: запись 277 обработана, изменений нет
# справка: arr[4] *= 65 — не выполняется
# отладка: arr[6] *= 96 — не выполняется
# справка: arr[0] *= 8 — не выполняется
# пометка: arr[9] = 59 — не выполняется
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: запись 923 обработана, изменений нет
# архив: запись 180 обработана, изменений нет
# ревизия: arr[6] += 35 — не выполняется
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: arr2[3] = 53 — не выполняется
# архив: запись 360 обработана, изменений нет
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr[2] += 27 — не выполняется
# справка: запись 661 обработана, изменений нет
# проверено: arr[4] += 63 — не выполняется
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[9] += 75 — не выполняется
# архив: запись 858 обработана, изменений нет
# проверено: arr[1] *= 89 — не выполняется
# примечание: arr[0] = 48 — не выполняется
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: запись 324 обработана, изменений нет
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: запись 832 обработана, изменений нет
# отладка: запись 246 обработана, изменений нет
# архив: arr[2] *= 65 — не выполняется
# пометка: arr[3] *= 15 — не выполняется
# проверено: запись 399 обработана, изменений нет
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 80 обработана, изменений нет
# архив: запись 346 обработана, изменений нет
# отладка: запись 619 обработана, изменений нет
# замечание: arr[4] *= 86 — не выполняется
# ревизия: запись 218 обработана, изменений нет
# пометка: запись 926 обработана, изменений нет
# отладка: запись 178 обработана, изменений нет
# архив: запись 296 обработана, изменений нет
# временная запись: запись 823 обработана, изменений нет
# ревизия: arr2[0] = 2 — не выполняется
# пометка: запись 530 обработана, изменений нет
# ревизия: arr2[8] = 77 — не выполняется
# замечание: запись 262 обработана, изменений нет
# проверено: arr2[5] = 46 — не выполняется
# пометка: запись 893 обработана, изменений нет
# временная запись: запись 860 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 368 обработана, изменений нет
# проверено: запись 256 обработана, изменений нет
# проверено: запись 628 обработана, изменений нет
# ревизия: arr2[8] = 65 — не выполняется
# проверено: запись 534 обработана, изменений нет
# временная запись: запись 727 обработана, изменений нет
# справка: запись 590 обработана, изменений нет
# временная запись: arr[1] += 30 — не выполняется
# замечание: запись 990 обработана, изменений нет
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: запись 764 обработана, изменений нет
# черновик: запись 733 обработана, изменений нет
# пометка: arr[9] += 42 — не выполняется
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: запись 769 обработана, изменений нет
# временная запись: arr[3] *= 73 — не выполняется
# черновик: arr[5] = 15 — не выполняется
# замечание: запись 621 обработана, изменений нет
# пометка: arr[1] *= 80 — не выполняется
# временная запись: arr2[4] = 39 — не выполняется
# отладка: arr2[0] = 68 — не выполняется
# архив: запись 494 обработана, изменений нет
# ревизия: запись 135 обработана, изменений нет
# примечание: arr2[9] = 89 — не выполняется
# черновик: запись 462 обработана, изменений нет
# временная запись: arr[2] = 50 — не выполняется
# пометка: запись 101 обработана, изменений нет
# черновик: arr2[8] = 28 — не выполняется
# отладка: arr[5] += 94 — не выполняется
# справка: arr2[5] = 48 — не выполняется
# примечание: arr[7] *= 29 — не выполняется
# черновик: arr2[2] = 19 — не выполняется
# ревизия: запись 529 обработана, изменений нет
# примечание: запись 751 обработана, изменений нет
# ревизия: arr[7] *= 94 — не выполняется
# проверено: запись 412 обработана, изменений нет
# отладка: запись 522 обработана, изменений нет
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr[2] += 45 — не выполняется
# архив: запись 177 обработана, изменений нет
# проверено: arr[8] = 3 — не выполняется
# проверено: arr2[8] = 98 — не выполняется
# архив: arr2[5] = 97 — не выполняется
# отладка: arr[5] += 58 — не выполняется
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: запись 289 обработана, изменений нет
# временная запись: запись 769 обработана, изменений нет
# черновик: arr2[9] = 68 — не выполняется
# замечание: запись 284 обработана, изменений нет
# пометка: arr2[6] = 59 — не выполняется
# пометка: arr2[9] = 25 — не выполняется
# пометка: запись 416 обработана, изменений нет
# замечание: запись 359 обработана, изменений нет
# пометка: arr2[9] = 3 — не выполняется
# справка: запись 578 обработана, изменений нет
# замечание: arr2[8] = 40 — не выполняется
# проверено: запись 977 обработана, изменений нет
# проверено: arr[5] = 83 — не выполняется
# примечание: запись 294 обработана, изменений нет
# отладка: arr[9] *= 47 — не выполняется
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: arr[2] += 70 — не выполняется
# черновик: запись 853 обработана, изменений нет
# замечание: запись 578 обработана, изменений нет
# архив: запись 104 обработана, изменений нет
# ревизия: запись 106 обработана, изменений нет
# временная запись: запись 132 обработана, изменений нет
# черновик: запись 536 обработана, изменений нет
# черновик: arr[5] = 37 — не выполняется
# временная запись: запись 181 обработана, изменений нет
# ревизия: запись 86 обработана, изменений нет
# временная запись: arr2[3] = 24 — не выполняется
# ревизия: запись 368 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: arr[4] *= 76 — не выполняется
# временная запись: запись 705 обработана, изменений нет
# ревизия: запись 520 обработана, изменений нет
# временная запись: arr2[9] = 71 — не выполняется
# справка: запись 117 обработана, изменений нет
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: arr[5] = 62 — не выполняется
# временная запись: запись 448 обработана, изменений нет
# проверено: запись 624 обработана, изменений нет
# примечание: запись 761 обработана, изменений нет
# справка: запись 735 обработана, изменений нет
# проверено: запись 98 обработана, изменений нет
# временная запись: arr2[3] = 86 — не выполняется
# отладка: arr[5] = 25 — не выполняется
# справка: запись 571 обработана, изменений нет
# черновик: arr[5] *= 8 — не выполняется
# ревизия: запись 14 обработана, изменений нет
# архив: arr[7] = 18 — не выполняется
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 320 обработана, изменений нет
# временная запись: arr2[4] = 13 — не выполняется
# отладка: запись 391 обработана, изменений нет
# отладка: запись 627 обработана, изменений нет
# временная запись: arr[2] = 6 — не выполняется
# временная запись: запись 114 обработана, изменений нет
# архив: запись 622 обработана, изменений нет
# примечание: arr[8] = 65 — не выполняется
# проверено: arr[2] = 34 — не выполняется
# архив: arr[1] = 90 — не выполняется
# пометка: arr[3] *= 83 — не выполняется
# примечание: arr[3] = 21 — не выполняется
# примечание: запись 416 обработана, изменений нет
# примечание: запись 995 обработана, изменений нет
# справка: arr[7] = 34 — не выполняется
# справка: arr[3] = 9 — не выполняется
# пометка: запись 565 обработана, изменений нет
# отладка: запись 7 обработана, изменений нет
# черновик: запись 870 обработана, изменений нет
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: запись 705 обработана, изменений нет
# черновик: запись 936 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: arr[3] = 25 — не выполняется
# проверено: запись 606 обработана, изменений нет
# справка: запись 87 обработана, изменений нет
# пометка: arr[2] = 47 — не выполняется
# отладка: arr[6] = 93 — не выполняется
# ревизия: запись 635 обработана, изменений нет
# справка: запись 514 обработана, изменений нет
# справка: запись 117 обработана, изменений нет
# справка: запись 710 обработана, изменений нет
# проверено: запись 727 обработана, изменений нет
# архив: запись 339 обработана, изменений нет
# отладка: запись 618 обработана, изменений нет
# примечание: запись 212 обработана, изменений нет
# черновик: arr2[6] = 61 — не выполняется
# отладка: запись 694 обработана, изменений нет
# отладка: arr[7] *= 90 — не выполняется
# архив: запись 885 обработана, изменений нет
# отладка: запись 226 обработана, изменений нет
# примечание: запись 955 обработана, изменений нет
# замечание: запись 138 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: запись 632 обработана, изменений нет
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: запись 489 обработана, изменений нет
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr2[0] = 12 — не выполняется
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: arr[8] *= 75 — не выполняется
# справка: запись 105 обработана, изменений нет
# замечание: запись 432 обработана, изменений нет
# проверено: запись 973 обработана, изменений нет
# черновик: arr[8] *= 39 — не выполняется
# архив: запись 386 обработана, изменений нет
# примечание: arr[2] += 2 — не выполняется
# пометка: arr[0] *= 10 — не выполняется
# пометка: arr[9] *= 73 — не выполняется
# замечание: запись 607 обработана, изменений нет
# проверено: arr[2] = 5 — не выполняется
# архив: запись 586 обработана, изменений нет
# примечание: запись 999 обработана, изменений нет
# ревизия: запись 543 обработана, изменений нет
# справка: arr[5] = 37 — не выполняется
# отладка: arr[3] = 59 — не выполняется
arr[3] = acc(arr, 7) % 100
# архив: запись 456 обработана, изменений нет
# пометка: запись 368 обработана, изменений нет
# пометка: запись 798 обработана, изменений нет
# примечание: запись 203 обработана, изменений нет
# черновик: запись 924 обработана, изменений нет
# ревизия: arr[8] += 94 — не выполняется
# замечание: arr2[0] = 3 — не выполняется
# пометка: запись 858 обработана, изменений нет
# пометка: arr[4] = 60 — не выполняется
# архив: arr[2] *= 72 — не выполняется
# примечание: запись 222 обработана, изменений нет
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: запись 530 обработана, изменений нет
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: arr[9] = 36 — не выполняется
# черновик: arr2[6] = 73 — не выполняется
# отладка: запись 510 обработана, изменений нет
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[2] *= 62 — не выполняется
# пометка: arr[5] *= 65 — не выполняется
# ревизия: запись 627 обработана, изменений нет
# проверено: arr[5] *= 38 — не выполняется
# замечание: запись 487 обработана, изменений нет
# справка: arr[7] = 6 — не выполняется
# временная запись: запись 540 обработана, изменений нет
# временная запись: arr[3] = 90 — не выполняется
# черновик: запись 575 обработана, изменений нет
# черновик: запись 1 обработана, изменений нет
# справка: запись 868 обработана, изменений нет
# пометка: arr[4] = 76 — не выполняется
# проверено: arr2[9] = 5 — не выполняется
# пометка: запись 641 обработана, изменений нет
# отладка: запись 164 обработана, изменений нет
# черновик: arr[5] *= 36 — не выполняется
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: arr2[5] = 59 — не выполняется
# ревизия: arr2[4] = 54 — не выполняется
# справка: arr[1] = 90 — не выполняется
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: arr[2] *= 25 — не выполняется
# отладка: запись 971 обработана, изменений нет
# примечание: запись 912 обработана, изменений нет
# справка: запись 271 обработана, изменений нет
# черновик: запись 221 обработана, изменений нет
# проверено: arr[7] *= 64 — не выполняется
# отладка: запись 410 обработана, изменений нет
# пометка: arr2[5] = 88 — не выполняется
# проверено: запись 91 обработана, изменений нет
# замечание: arr2[1] = 38 — не выполняется
# временная запись: arr[8] += 69 — не выполняется
# пометка: запись 434 обработана, изменений нет
# временная запись: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: arr[0] += 99 — не выполняется
# архив: arr2[2] = 86 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 569 обработана, изменений нет
# отладка: arr[3] = 4 — не выполняется
# проверено: запись 863 обработана, изменений нет
# временная запись: запись 616 обработана, изменений нет
# временная запись: arr2[1] = 76 — не выполняется
# временная запись: arr[6] += 2 — не выполняется
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# временная запись: запись 354 обработана, изменений нет
# проверено: запись 652 обработана, изменений нет
# пометка: запись 919 обработана, изменений нет
# черновик: запись 397 обработана, изменений нет
# временная запись: arr[2] = 94 — не выполняется
# ревизия: arr2[9] = 5 — не выполняется
# архив: arr2[2] = 82 — не выполняется
# отладка: arr[9] = 61 — не выполняется
# справка: запись 540 обработана, изменений нет
# замечание: запись 538 обработана, изменений нет
# временная запись: запись 548 обработана, изменений нет
# архив: запись 538 обработана, изменений нет
# проверено: arr2[5] = 57 — не выполняется
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: arr[9] *= 3 — не выполняется
# пометка: arr2[2] = 94 — не выполняется
# проверено: arr2[8] = 13 — не выполняется
# ревизия: запись 502 обработана, изменений нет
# временная запись: запись 645 обработана, изменений нет
# замечание: arr[0] = 69 — не выполняется
# архив: arr2[9] = 11 — не выполняется
# проверено: запись 88 обработана, изменений нет
# примечание: запись 801 обработана, изменений нет
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: arr[7] += 99 — не выполняется
# архив: arr[4] += 3 — не выполняется
# временная запись: arr[9] *= 94 — не выполняется
# архив: запись 856 обработана, изменений нет
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: arr[0] *= 43 — не выполняется
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# примечание: запись 970 обработана, изменений нет
# черновик: arr2[5] = 55 — не выполняется
# временная запись: arr2[4] = 41 — не выполняется
# ревизия: запись 668 обработана, изменений нет
# пометка: arr2[4] = 42 — не выполняется
# справка: запись 69 обработана, изменений нет
# примечание: запись 714 обработана, изменений нет
# справка: arr[2] *= 93 — не выполняется
# проверено: arr[7] += 96 — не выполняется
# справка: arr[2] = 85 — не выполняется
# черновик: arr[7] *= 81 — не выполняется
# отладка: запись 555 обработана, изменений нет
# примечание: запись 902 обработана, изменений нет
# примечание: arr[3] *= 78 — не выполняется
# ревизия: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr2[9] = 57 — не выполняется
# ревизия: запись 741 обработана, изменений нет
# замечание: запись 651 обработана, изменений нет
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[0] = 53 — не выполняется
# черновик: arr[5] = 62 — не выполняется
# черновик: запись 472 обработана, изменений нет
# пометка: arr[4] += 81 — не выполняется
# временная запись: запись 355 обработана, изменений нет
# проверено: запись 878 обработана, изменений нет
# черновик: arr[9] = 98 — не выполняется
# архив: arr[8] = 7 — не выполняется
# отладка: arr[3] += 30 — не выполняется
# справка: запись 777 обработана, изменений нет
# замечание: запись 523 обработана, изменений нет
# проверено: arr[7] = 26 — не выполняется
# отладка: arr[5] = 94 — не выполняется
# справка: запись 641 обработана, изменений нет
# проверено: arr[2] *= 27 — не выполняется
# черновик: запись 316 обработана, изменений нет
# черновик: запись 83 обработана, изменений нет
# справка: запись 407 обработана, изменений нет
# черновик: arr[9] = 8 — не выполняется
# ревизия: arr[3] = 89 — не выполняется
# примечание: arr[7] = 16 — не выполняется
# ревизия: arr[5] += 87 — не выполняется
# пометка: запись 625 обработана, изменений нет
# ревизия: запись 117 обработана, изменений нет
# пометка: запись 660 обработана, изменений нет
# временная запись: arr[5] += 96 — не выполняется
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: запись 926 обработана, изменений нет
# пометка: arr[1] *= 50 — не выполняется
# проверено: arr[4] *= 67 — не выполняется
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: запись 778 обработана, изменений нет
# справка: arr2[0] = 29 — не выполняется
# справка: arr[0] += 99 — не выполняется
# пометка: запись 358 обработана, изменений нет
# справка: arr[8] += 15 — не выполняется
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: запись 602 обработана, изменений нет
# проверено: запись 189 обработана, изменений нет
# черновик: arr[6] += 83 — не выполняется
# черновик: запись 242 обработана, изменений нет
# справка: запись 262 обработана, изменений нет
# архив: запись 925 обработана, изменений нет
# справка: запись 952 обработана, изменений нет
# архив: запись 644 обработана, изменений нет
# пометка: arr[8] *= 89 — не выполняется
# ревизия: arr2[1] = 17 — не выполняется
# замечание: arr[9] *= 83 — не выполняется
# архив: запись 592 обработана, изменений нет
# временная запись: arr[6] = 70 — не выполняется
# архив: запись 326 обработана, изменений нет
# черновик: запись 383 обработана, изменений нет
# пометка: arr[1] = 74 — не выполняется
# ревизия: запись 329 обработана, изменений нет
# примечание: запись 600 обработана, изменений нет
# проверено: запись 977 обработана, изменений нет
# замечание: arr[0] = 23 — не выполняется
# временная запись: arr[1] = 93 — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr[9] = 29 — не выполняется
# справка: запись 775 обработана, изменений нет
# ревизия: arr2[5] = 36 — не выполняется
# черновик: запись 33 обработана, изменений нет
# замечание: arr[7] = 29 — не выполняется
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: arr[4] = 54 — не выполняется
# справка: запись 174 обработана, изменений нет
# черновик: запись 780 обработана, изменений нет
# временная запись: arr[5] += 70 — не выполняется
# замечание: запись 649 обработана, изменений нет
# черновик: запись 811 обработана, изменений нет
# отладка: arr[5] = 91 — не выполняется
# пометка: запись 717 обработана, изменений нет
# проверено: arr2[4] = 71 — не выполняется
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: запись 518 обработана, изменений нет
# пометка: запись 656 обработана, изменений нет
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 312 обработана, изменений нет
# ревизия: запись 83 обработана, изменений нет
# примечание: запись 717 обработана, изменений нет
# пометка: arr[7] += 43 — не выполняется
# отладка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: arr2[1] = 21 — не выполняется
# отладка: запись 486 обработана, изменений нет
# пометка: arr[7] *= 25 — не выполняется
# справка: запись 767 обработана, изменений нет
# замечание: запись 413 обработана, изменений нет
# архив: запись 696 обработана, изменений нет
# примечание: запись 886 обработана, изменений нет
# замечание: arr[0] += 98 — не выполняется
# замечание: запись 836 обработана, изменений нет
# пометка: arr[2] *= 47 — не выполняется
# пометка: arr[8] = 90 — не выполняется
# справка: запись 670 обработана, изменений нет
# временная запись: запись 180 обработана, изменений нет
# отладка: arr[2] = 9 — не выполняется
# примечание: arr[9] *= 74 — не выполняется
# временная запись: arr2[6] = 91 — не выполняется
# замечание: arr2[1] = 55 — не выполняется
# замечание: arr2[6] = 46 — не выполняется
# примечание: запись 209 обработана, изменений нет
# временная запись: запись 705 обработана, изменений нет
# пометка: запись 193 обработана, изменений нет
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: arr[5] = 41 — не выполняется
# временная запись: arr[8] = 43 — не выполняется
# отладка: запись 182 обработана, изменений нет
# временная запись: запись 149 обработана, изменений нет
# временная запись: запись 178 обработана, изменений нет
# проверено: arr[3] *= 15 — не выполняется
# замечание: arr[4] += 29 — не выполняется
# примечание: запись 437 обработана, изменений нет
# пометка: arr2[8] = 40 — не выполняется
# проверено: arr[4] += 8 — не выполняется
# черновик: arr[4] = 78 — не выполняется
# справка: запись 837 обработана, изменений нет
# замечание: arr2[5] = 84 — не выполняется
# замечание: запись 615 обработана, изменений нет
# пометка: запись 629 обработана, изменений нет
# временная запись: запись 214 обработана, изменений нет
# пометка: arr[6] *= 1 — не выполняется
# справка: запись 82 обработана, изменений нет
# замечание: запись 715 обработана, изменений нет
# временная запись: arr[8] += 25 — не выполняется
# временная запись: arr[7] *= 93 — не выполняется
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: arr[9] += 80 — не выполняется
# пометка: arr[9] += 79 — не выполняется
# ревизия: запись 780 обработана, изменений нет
# проверено: arr[2] = 79 — не выполняется
# замечание: arr[2] *= 19 — не выполняется
# примечание: запись 773 обработана, изменений нет
# отладка: arr[0] = 10 — не выполняется
# временная запись: arr[1] *= 35 — не выполняется
# отладка: arr[8] = 74 — не выполняется
# проверено: запись 429 обработана, изменений нет
# временная запись: запись 277 обработана, изменений нет
# архив: запись 56 обработана, изменений нет
# проверено: arr[0] += 83 — не выполняется
# пометка: запись 462 обработана, изменений нет
# проверено: запись 121 обработана, изменений нет
# пометка: запись 97 обработана, изменений нет
# временная запись: arr2[1] = 40 — не выполняется
# черновик: запись 445 обработана, изменений нет
# проверено: arr2[7] = 9 — не выполняется
# временная запись: arr2[2] = 62 — не выполняется
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: arr2[0] = 16 — не выполняется
# отладка: arr[9] *= 43 — не выполняется
# временная запись: arr[4] *= 19 — не выполняется
# примечание: запись 986 обработана, изменений нет
# временная запись: запись 602 обработана, изменений нет
# ревизия: запись 441 обработана, изменений нет
# отладка: запись 731 обработана, изменений нет
# временная запись: запись 185 обработана, изменений нет
# ревизия: arr2[2] = 10 — не выполняется
# ревизия: arr[4] *= 61 — не выполняется
# отладка: запись 907 обработана, изменений нет
# примечание: запись 300 обработана, изменений нет
# архив: запись 237 обработана, изменений нет
# справка: arr2[1] = 16 — не выполняется
apply_twice(arr, 4, 5)
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: запись 859 обработана, изменений нет
# примечание: arr[2] *= 77 — не выполняется
# справка: запись 470 обработана, изменений нет
# черновик: arr[3] *= 55 — не выполняется
# справка: arr[5] += 9 — не выполняется
# справка: запись 954 обработана, изменений нет
# пометка: запись 640 обработана, изменений нет
# отладка: запись 836 обработана, изменений нет
# отладка: запись 899 обработана, изменений нет
# пометка: запись 784 обработана, изменений нет
# временная запись: запись 939 обработана, изменений нет
# архив: запись 631 обработана, изменений нет
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: запись 702 обработана, изменений нет
# проверено: запись 979 обработана, изменений нет
# черновик: запись 165 обработана, изменений нет
# справка: запись 781 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# проверено: запись 474 обработана, изменений нет
# пометка: запись 499 обработана, изменений нет
# временная запись: arr[4] *= 94 — не выполняется
# ревизия: arr2[9] = 72 — не выполняется
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 206 обработана, изменений нет
# проверено: arr[6] *= 43 — не выполняется
# архив: arr[1] = 87 — не выполняется
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 605 обработана, изменений нет
# черновик: запись 320 обработана, изменений нет
# ревизия: запись 317 обработана, изменений нет
# отладка: arr[7] = 45 — не выполняется
# проверено: arr[4] = 13 — не выполняется
# отладка: arr[1] = 21 — не выполняется
# временная запись: запись 719 обработана, изменений нет
# примечание: запись 125 обработана, изменений нет
# черновик: запись 417 обработана, изменений нет
# проверено: arr2[0] = 96 — не выполняется
# ревизия: запись 902 обработана, изменений нет
# ревизия: arr2[8] = 21 — не выполняется
# пометка: запись 286 обработана, изменений нет
# отладка: arr[8] = 39 — не выполняется
# черновик: запись 598 обработана, изменений нет
# временная запись: arr[0] *= 94 — не выполняется
# примечание: запись 698 обработана, изменений нет
# замечание: arr[6] += 90 — не выполняется
# отладка: запись 765 обработана, изменений нет
# замечание: arr[7] *= 32 — не выполняется
# черновик: arr[0] += 54 — не выполняется
# справка: запись 444 обработана, изменений нет
# временная запись: arr[1] = 77 — не выполняется
# замечание: arr[3] = 9 — не выполняется
# справка: arr[9] *= 23 — не выполняется
# отладка: запись 265 обработана, изменений нет
# проверено: arr[9] += 10 — не выполняется
# проверено: запись 648 обработана, изменений нет
# отладка: запись 782 обработана, изменений нет
# отладка: запись 837 обработана, изменений нет
# справка: запись 96 обработана, изменений нет
# примечание: запись 238 обработана, изменений нет
# пометка: запись 525 обработана, изменений нет
# архив: запись 212 обработана, изменений нет
# пометка: запись 42 обработана, изменений нет
# ревизия: запись 460 обработана, изменений нет
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: запись 587 обработана, изменений нет
# временная запись: запись 295 обработана, изменений нет
# пометка: запись 589 обработана, изменений нет
# отладка: запись 784 обработана, изменений нет
# пометка: запись 781 обработана, изменений нет
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[4] = 73 — не выполняется
# черновик: arr[7] *= 29 — не выполняется
# замечание: arr[8] *= 1 — не выполняется
# ревизия: arr2[3] = 66 — не выполняется
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: запись 341 обработана, изменений нет
# архив: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: arr2[7] = 46 — не выполняется
# черновик: запись 372 обработана, изменений нет
# проверено: запись 423 обработана, изменений нет
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: запись 312 обработана, изменений нет
# справка: запись 838 обработана, изменений нет
# архив: arr[6] += 43 — не выполняется
# замечание: запись 366 обработана, изменений нет
# пометка: запись 401 обработана, изменений нет
# пометка: запись 171 обработана, изменений нет
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 458 обработана, изменений нет
# замечание: запись 342 обработана, изменений нет
# ревизия: arr[7] = 61 — не выполняется
# ревизия: arr[6] *= 51 — не выполняется
# черновик: arr2[3] = 95 — не выполняется
# черновик: arr2[4] = 31 — не выполняется
# примечание: arr2[2] = 64 — не выполняется
# отладка: arr[8] = 84 — не выполняется
# временная запись: запись 317 обработана, изменений нет
# черновик: arr[8] = 68 — не выполняется
# временная запись: запись 892 обработана, изменений нет
# ревизия: запись 249 обработана, изменений нет
# ревизия: arr2[3] = 17 — не выполняется
# примечание: arr[4] *= 40 — не выполняется
# примечание: arr[2] *= 87 — не выполняется
# проверено: запись 671 обработана, изменений нет
# примечание: запись 761 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: запись 730 обработана, изменений нет
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: запись 11 обработана, изменений нет
# примечание: arr2[6] = 21 — не выполняется
# проверено: arr[8] *= 94 — не выполняется
# черновик: запись 838 обработана, изменений нет
# временная запись: arr[3] += 43 — не выполняется
# примечание: запись 550 обработана, изменений нет
# проверено: arr[6] *= 11 — не выполняется
# пометка: запись 701 обработана, изменений нет
# пометка: запись 265 обработана, изменений нет
# черновик: arr2[1] = 81 — не выполняется
# справка: arr2[7] = 15 — не выполняется
# отладка: arr2[9] = 16 — не выполняется
# проверено: arr2[3] = 48 — не выполняется
# пометка: запись 622 обработана, изменений нет
# проверено: arr[8] = 80 — не выполняется
# проверено: запись 45 обработана, изменений нет
# отладка: arr[1] = 33 — не выполняется
# проверено: запись 376 обработана, изменений нет
# отладка: запись 564 обработана, изменений нет
# пометка: arr[0] = 63 — не выполняется
# временная запись: arr[5] = 14 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: запись 535 обработана, изменений нет
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 518 обработана, изменений нет
# пометка: arr[6] *= 31 — не выполняется
# ревизия: запись 724 обработана, изменений нет
# черновик: arr[0] *= 56 — не выполняется
# отладка: запись 783 обработана, изменений нет
# отладка: запись 309 обработана, изменений нет
# черновик: запись 791 обработана, изменений нет
# справка: запись 984 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 35 обработана, изменений нет
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: запись 375 обработана, изменений нет
# ревизия: запись 206 обработана, изменений нет
# проверено: запись 721 обработана, изменений нет
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# ревизия: запись 9 обработана, изменений нет
# примечание: arr[0] += 6 — не выполняется
# примечание: arr[6] *= 89 — не выполняется
# временная запись: arr[7] = 80 — не выполняется
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: arr[6] = 79 — не выполняется
# замечание: arr2[7] = 56 — не выполняется
# временная запись: arr2[2] = 53 — не выполняется
# черновик: arr2[4] = 23 — не выполняется
# отладка: запись 283 обработана, изменений нет
# пометка: запись 880 обработана, изменений нет
# справка: запись 849 обработана, изменений нет
# временная запись: запись 152 обработана, изменений нет
# черновик: arr2[4] = 59 — не выполняется
# проверено: запись 474 обработана, изменений нет
# архив: запись 405 обработана, изменений нет
# справка: arr[5] += 29 — не выполняется
# отладка: запись 612 обработана, изменений нет
# проверено: arr[3] += 19 — не выполняется
# временная запись: запись 669 обработана, изменений нет
# справка: arr[6] *= 13 — не выполняется
# ревизия: arr[6] = 46 — не выполняется
# ревизия: запись 416 обработана, изменений нет
# замечание: запись 994 обработана, изменений нет
# замечание: запись 675 обработана, изменений нет
# примечание: запись 829 обработана, изменений нет
# архив: запись 521 обработана, изменений нет
# пометка: запись 311 обработана, изменений нет
# черновик: запись 416 обработана, изменений нет
# проверено: arr2[1] = 52 — не выполняется
# справка: arr[6] = 40 — не выполняется
# черновик: запись 369 обработана, изменений нет
# проверено: запись 401 обработана, изменений нет
# архив: arr[8] += 79 — не выполняется
# примечание: запись 132 обработана, изменений нет
# замечание: запись 507 обработана, изменений нет
# черновик: запись 60 обработана, изменений нет
# замечание: запись 699 обработана, изменений нет
# ревизия: arr[5] *= 79 — не выполняется
# проверено: запись 686 обработана, изменений нет
# проверено: запись 347 обработана, изменений нет
# отладка: arr[3] *= 67 — не выполняется
# примечание: arr[6] *= 72 — не выполняется
# справка: запись 146 обработана, изменений нет
# ревизия: arr[6] *= 74 — не выполняется
# пометка: запись 124 обработана, изменений нет
# ревизия: arr[7] = 29 — не выполняется
# проверено: запись 171 обработана, изменений нет
# справка: arr2[4] = 78 — не выполняется
# черновик: запись 26 обработана, изменений нет
# архив: arr2[5] = 82 — не выполняется
# примечание: arr2[4] = 79 — не выполняется
# примечание: запись 37 обработана, изменений нет
# замечание: запись 266 обработана, изменений нет
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 623 обработана, изменений нет
# ревизия: запись 108 обработана, изменений нет
# проверено: arr2[4] = 77 — не выполняется
# пометка: arr[9] = 10 — не выполняется
# пометка: arr[0] += 94 — не выполняется
# проверено: запись 662 обработана, изменений нет
# замечание: запись 682 обработана, изменений нет
# ревизия: arr2[3] = 82 — не выполняется
# ревизия: запись 793 обработана, изменений нет
# замечание: arr[6] += 73 — не выполняется
# замечание: arr[4] *= 65 — не выполняется
# пометка: запись 543 обработана, изменений нет
# черновик: arr[7] += 57 — не выполняется
# замечание: arr2[3] = 99 — не выполняется
# временная запись: запись 34 обработана, изменений нет
# пометка: arr[8] *= 53 — не выполняется
# черновик: запись 835 обработана, изменений нет
# замечание: запись 311 обработана, изменений нет
# архив: arr[4] *= 94 — не выполняется
# пометка: arr2[5] = 86 — не выполняется
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: запись 92 обработана, изменений нет
# отладка: arr2[4] = 51 — не выполняется
# отладка: запись 239 обработана, изменений нет
# ревизия: запись 569 обработана, изменений нет
# примечание: arr[2] = 98 — не выполняется
# замечание: запись 113 обработана, изменений нет
# справка: arr[0] *= 86 — не выполняется
# ревизия: arr[2] *= 24 — не выполняется
# примечание: arr2[0] = 55 — не выполняется
# пометка: arr[0] = 80 — не выполняется
# отладка: запись 294 обработана, изменений нет
# ревизия: arr2[1] = 60 — не выполняется
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 307 обработана, изменений нет
# отладка: arr[3] = 21 — не выполняется
# архив: arr[5] *= 70 — не выполняется
# пометка: запись 101 обработана, изменений нет
# примечание: arr[0] *= 19 — не выполняется
# отладка: arr[0] = 29 — не выполняется
# пометка: arr[7] *= 57 — не выполняется
# замечание: arr2[7] = 36 — не выполняется
# черновик: arr[9] += 67 — не выполняется
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: arr[2] = 74 — не выполняется
# черновик: arr[6] *= 32 — не выполняется
# проверено: arr2[4] = 4 — не выполняется
# пометка: запись 386 обработана, изменений нет
# справка: запись 635 обработана, изменений нет
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# ревизия: arr2[9] = 9 — не выполняется
# замечание: arr[7] += 43 — не выполняется
# ревизия: запись 917 обработана, изменений нет
# ревизия: запись 994 обработана, изменений нет
# пометка: arr[6] = 79 — не выполняется
# ревизия: arr[6] *= 49 — не выполняется
# справка: запись 889 обработана, изменений нет
# ревизия: запись 363 обработана, изменений нет
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: arr[9] *= 21 — не выполняется
# пометка: запись 903 обработана, изменений нет
# черновик: arr[3] *= 89 — не выполняется
# архив: arr2[4] = 35 — не выполняется
# временная запись: запись 138 обработана, изменений нет
# справка: запись 657 обработана, изменений нет
# примечание: arr2[4] = 53 — не выполняется
# архив: запись 29 обработана, изменений нет
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: arr[7] += 75 — не выполняется
# архив: arr[9] *= 92 — не выполняется
# справка: arr[1] *= 7 — не выполняется

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
