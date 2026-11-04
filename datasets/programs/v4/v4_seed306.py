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
arr2[8] = 39
arr[0], arr[5] = arr[5], arr[0]
arr[9], arr[8] = arr[8], arr[9]
arr[4] *= 13
arr2[0] = 17
arr[0], arr[9] = arr[9], arr[0]
arr[4], arr[5] = arr[5], arr[4]
arr2[4] = 29
"""

TRAP_0 = "arr[9] = 818"
TRAP_1 = "arr[8] = 426"
TRAP_2 = "arr[8] = 108"
TRAP_3 = "arr[7] = 956"
TRAP_4 = "arr[4] = 630"
TRAP_5 = "arr[4] = 301"
TRAP_6 = "arr[8] = 161"
TRAP_7 = "arr[6] = 616"
TRAP_8 = "arr[3] = 142"
TRAP_9 = "arr[2] = 380"
TRAP_10 = "arr[4] = 691"
TRAP_11 = "arr[6] = 267"
TRAP_12 = "arr[6] = 741"
TRAP_13 = "arr[4] = 289"
TRAP_14 = "arr[5] = 621"
TRAP_15 = "arr[5] = 783"
TRAP_16 = "arr[1] = 136"
TRAP_17 = "arr[8] = 777"
TRAP_18 = "arr[3] = 332"
TRAP_19 = "arr[2] = 338"
TRAP_20 = "arr[7] = 329"
TRAP_21 = "arr[0] = 225"
TRAP_22 = "arr[3] = 621"
TRAP_23 = "arr[9] = 331"
TRAP_24 = "arr[9] = 152"
TRAP_25 = "arr[5] = 316"
TRAP_26 = "arr[1] = 388"
TRAP_27 = "arr[5] = 776"
TRAP_28 = "arr[2] = 920"
TRAP_29 = "arr[5] = 401"
TRAP_30 = "arr[8] = 285"
TRAP_31 = "arr[3] = 511"
TRAP_32 = "arr[1] = 984"
TRAP_33 = "arr[1] = 382"
TRAP_34 = "arr[1] = 360"
TRAP_35 = "arr[0] = 199"
TRAP_36 = "arr[5] = 681"
TRAP_37 = "arr[8] = 512"
TRAP_38 = "arr[5] = 729"
TRAP_39 = "arr[8] = 384"
TRAP_40 = "arr[6] = 172"
TRAP_41 = "arr[8] = 455"
TRAP_42 = "arr[7] = 681"
TRAP_43 = "arr[9] = 989"
TRAP_44 = "arr[5] = 920"
TRAP_45 = "arr[5] = 561"
TRAP_46 = "arr[6] = 513"
TRAP_47 = "arr[1] = 565"
TRAP_48 = "arr[8] = 192"
TRAP_49 = "arr[4] = 365"
TRAP_50 = "arr[6] = 680"
TRAP_51 = "arr[6] = 222"
TRAP_52 = "arr[7] = 887"
TRAP_53 = "arr[1] = 404"
TRAP_54 = "arr[7] = 172"
TRAP_55 = "arr[4] = 481"
TRAP_56 = "arr[8] = 695"
TRAP_57 = "arr[9] = 194"
TRAP_58 = "arr[8] = 609"
TRAP_59 = "arr[5] = 665"
TRAP_60 = "arr[0] = 102"
TRAP_61 = "arr[7] = 284"
TRAP_62 = "arr[8] = 482"
TRAP_63 = "arr[4] = 950"
TRAP_64 = "arr[7] = 773"
TRAP_65 = "arr[2] = 736"
TRAP_66 = "arr[4] = 658"
TRAP_67 = "arr[1] = 550"
TRAP_68 = "arr[7] = 941"
TRAP_69 = "arr[7] = 934"
TRAP_70 = "arr[3] = 532"
TRAP_71 = "arr[0] = 630"
TRAP_72 = "arr[3] = 965"
TRAP_73 = "arr[8] = 585"
TRAP_74 = "arr[9] = 846"
TRAP_75 = "arr[3] = 428"
TRAP_76 = "arr[8] = 556"
TRAP_77 = "arr[7] = 855"
TRAP_78 = "arr[7] = 496"
TRAP_79 = "arr[8] = 536"
TRAP_80 = "arr[2] = 865"
TRAP_81 = "arr[3] = 615"
TRAP_82 = "arr[4] = 461"
TRAP_83 = "arr[0] = 812"
TRAP_84 = "arr[2] = 958"
TRAP_85 = "arr[9] = 629"
TRAP_86 = "arr[0] = 225"
TRAP_87 = "arr[4] = 913"
TRAP_88 = "arr[6] = 215"
TRAP_89 = "arr[5] = 863"
TRAP_90 = "arr[8] = 865"
TRAP_91 = "arr[1] = 587"
TRAP_92 = "arr[3] = 240"
TRAP_93 = "arr[0] = 100"
TRAP_94 = "arr[6] = 691"
TRAP_95 = "arr[1] = 673"
TRAP_96 = "arr[3] = 150"
TRAP_97 = "arr[8] = 708"
TRAP_98 = "arr[5] = 238"
TRAP_99 = "arr[4] = 334"
TRAP_100 = "arr[1] = 877"
TRAP_101 = "arr[2] = 693"
TRAP_102 = "arr[1] = 701"
TRAP_103 = "arr[3] = 956"
TRAP_104 = "arr[8] = 592"
TRAP_105 = "arr[4] = 170"
TRAP_106 = "arr[2] = 478"
TRAP_107 = "arr[5] = 655"
TRAP_108 = "arr[0] = 112"
TRAP_109 = "arr[2] = 890"
TRAP_110 = "arr[1] = 771"
TRAP_111 = "arr[8] = 861"
TRAP_112 = "arr[3] = 705"
TRAP_113 = "arr[3] = 140"
TRAP_114 = "arr[4] = 119"
TRAP_115 = "arr[4] = 263"
TRAP_116 = "arr[7] = 995"
TRAP_117 = "arr[0] = 194"
TRAP_118 = "arr[8] = 602"
TRAP_119 = "arr[0] = 626"
TRAP_120 = "arr[1] = 339"
TRAP_121 = "arr[0] = 558"
TRAP_122 = "arr[0] = 590"
TRAP_123 = "arr[6] = 271"
TRAP_124 = "arr[9] = 607"
TRAP_125 = "arr[0] = 386"
TRAP_126 = "arr[3] = 787"
TRAP_127 = "arr[0] = 361"
TRAP_128 = "arr[8] = 358"
TRAP_129 = "arr[7] = 242"
TRAP_130 = "arr[4] = 774"
TRAP_131 = "arr[7] = 291"
TRAP_132 = "arr[2] = 577"
TRAP_133 = "arr[1] = 145"
TRAP_134 = "arr[3] = 989"
TRAP_135 = "arr[9] = 973"
TRAP_136 = "arr[7] = 779"
TRAP_137 = "arr[1] = 339"
TRAP_138 = "arr[6] = 620"
TRAP_139 = "arr[7] = 839"
TRAP_140 = "arr[4] = 831"
TRAP_141 = "arr[6] = 653"
TRAP_142 = "arr[8] = 996"
TRAP_143 = "arr[0] = 898"
TRAP_144 = "arr[0] = 543"
TRAP_145 = "arr[2] = 689"
TRAP_146 = "arr[4] = 206"
TRAP_147 = "arr[9] = 928"
TRAP_148 = "arr[5] = 775"
TRAP_149 = "arr[9] = 196"

arr = [14, 30, 17, 26, 7, 9, 25, 20, 7, 14]

tmp_0 = arr[7] + 4
label_1 = "запись 1 не применялась"
label_2 = "запись 2 не применялась"
note_3 = str(arr[4]) + str(arr[3])
tmp_4 = arr[5] + 25
note_5 = str(arr[3]) + str(arr[2])
tmp_6 = arr[3] + 37
note_7 = str(arr[5]) + str(arr[8])
note_8 = str(arr[6]) + str(arr[7])
tmp_9 = arr[5] + 49
code_10 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_11 = arr[8] + 48
code_12 = re.sub(r'[0-9]', '#', str(arr[9]))
code_13 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_14 = arr[6]
code_15 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_16 = arr[8] + 7
code_17 = re.sub(r'[0-9]', '#', str(arr[8]))
code_18 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_19 = arr[1] + 7
tmp_20 = arr[4] + 10
note_21 = str(arr[6]) + str(arr[2])
tmp_22 = arr[2] + 32
tmp_23 = arr[6] + 4
copy_24 = arr[0]
label_25 = "запись 25 не применялась"
label_26 = "запись 26 не применялась"
code_27 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_28 = arr[6]
copy_29 = arr[6]
tmp_30 = arr[7] + 20
note_31 = str(arr[3]) + str(arr[1])
tmp_32 = arr[1] + 17
code_33 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_34 = arr[3] + 27
tmp_35 = arr[5] + 18
tmp_36 = arr[2] + 48
tmp_37 = arr[7] + 37
note_38 = str(arr[4]) + str(arr[6])
label_39 = "запись 39 не применялась"
copy_40 = arr[9]
copy_41 = arr[1]
label_42 = "запись 42 не применялась"
tmp_43 = arr[7] + 40
note_44 = str(arr[1]) + str(arr[3])
code_45 = re.sub(r'[0-9]', '#', str(arr[4]))
note_46 = str(arr[2]) + str(arr[2])
note_47 = str(arr[4]) + str(arr[1])
code_48 = re.sub(r'[0-9]', '#', str(arr[8]))
label_49 = "запись 49 не применялась"
code_50 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_51 = arr[2]
label_52 = "запись 52 не применялась"
code_53 = re.sub(r'[0-9]', '#', str(arr[0]))
note_54 = str(arr[4]) + str(arr[5])
tmp_55 = arr[7] + 22
copy_56 = arr[9]
copy_57 = arr[4]
label_58 = "запись 58 не применялась"
label_59 = "запись 59 не применялась"
code_60 = re.sub(r'[0-9]', '#', str(arr[7]))
code_61 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_62 = arr[4]
note_63 = str(arr[4]) + str(arr[9])
tmp_64 = arr[5] + 8
note_65 = str(arr[2]) + str(arr[6])
tmp_66 = arr[0] + 13
code_67 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_68 = arr[2] + 30
label_69 = "запись 69 не применялась"
note_70 = str(arr[2]) + str(arr[4])
tmp_71 = arr[6] + 20
label_72 = "запись 72 не применялась"
note_73 = str(arr[8]) + str(arr[9])
tmp_74 = arr[8] + 47
tmp_75 = arr[1] + 50
label_76 = "запись 76 не применялась"
label_77 = "запись 77 не применялась"
code_78 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_79 = arr[8] + 24
copy_80 = arr[5]
note_81 = str(arr[7]) + str(arr[2])
copy_82 = arr[9]
copy_83 = arr[2]
code_84 = re.sub(r'[0-9]', '#', str(arr[8]))
note_85 = str(arr[7]) + str(arr[2])
copy_86 = arr[6]
note_87 = str(arr[4]) + str(arr[5])
tmp_88 = arr[7] + 16
note_89 = str(arr[9]) + str(arr[4])
copy_90 = arr[0]
code_91 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_92 = arr[0]
note_93 = str(arr[3]) + str(arr[3])
note_94 = str(arr[4]) + str(arr[1])
copy_95 = arr[2]
note_96 = str(arr[6]) + str(arr[0])
label_97 = "запись 97 не применялась"
tmp_98 = arr[5] + 35
code_99 = re.sub(r'[0-9]', '#', str(arr[2]))
code_100 = re.sub(r'[0-9]', '#', str(arr[4]))
note_101 = str(arr[3]) + str(arr[4])
note_102 = str(arr[2]) + str(arr[2])
label_103 = "запись 103 не применялась"
note_104 = str(arr[3]) + str(arr[7])
code_105 = re.sub(r'[0-9]', '#', str(arr[7]))
label_106 = "запись 106 не применялась"
note_107 = str(arr[7]) + str(arr[5])
tmp_108 = arr[7] + 12
tmp_109 = arr[5] + 31
tmp_110 = arr[1] + 34
label_111 = "запись 111 не применялась"
code_112 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_113 = arr[5]
note_114 = str(arr[1]) + str(arr[8])
note_115 = str(arr[3]) + str(arr[8])
code_116 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_117 = arr[3] + 5
note_118 = str(arr[6]) + str(arr[6])
note_119 = str(arr[3]) + str(arr[2])
label_120 = "запись 120 не применялась"
tmp_121 = arr[0] + 28
code_122 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_123 = arr[0]
tmp_124 = arr[1] + 18
label_125 = "запись 125 не применялась"
code_126 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_127 = arr[0] + 41
code_128 = re.sub(r'[0-9]', '#', str(arr[5]))
code_129 = re.sub(r'[0-9]', '#', str(arr[1]))
note_130 = str(arr[4]) + str(arr[4])
note_131 = str(arr[1]) + str(arr[7])
copy_132 = arr[0]
code_133 = re.sub(r'[0-9]', '#', str(arr[9]))
code_134 = re.sub(r'[0-9]', '#', str(arr[7]))
note_135 = str(arr[6]) + str(arr[0])
note_136 = str(arr[0]) + str(arr[0])
note_137 = str(arr[3]) + str(arr[4])
copy_138 = arr[1]
note_139 = str(arr[6]) + str(arr[9])
note_140 = str(arr[3]) + str(arr[6])
copy_141 = arr[5]
code_142 = re.sub(r'[0-9]', '#', str(arr[6]))
code_143 = re.sub(r'[0-9]', '#', str(arr[3]))
label_144 = "запись 144 не применялась"
code_145 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_146 = arr[5]
code_147 = re.sub(r'[0-9]', '#', str(arr[8]))
label_148 = "запись 148 не применялась"
label_149 = "запись 149 не применялась"
copy_150 = arr[4]
code_151 = re.sub(r'[0-9]', '#', str(arr[6]))
label_152 = "запись 152 не применялась"
code_153 = re.sub(r'[0-9]', '#', str(arr[4]))
code_154 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_155 = arr[9]
copy_156 = arr[2]
copy_157 = arr[2]
tmp_158 = arr[6] + 13
label_159 = "запись 159 не применялась"
copy_160 = arr[1]
note_161 = str(arr[2]) + str(arr[6])
label_162 = "запись 162 не применялась"
note_163 = str(arr[3]) + str(arr[5])
tmp_164 = arr[2] + 36
note_165 = str(arr[0]) + str(arr[5])
tmp_166 = arr[4] + 18
code_167 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_168 = arr[6] + 23
note_169 = str(arr[6]) + str(arr[3])
copy_170 = arr[3]
note_171 = str(arr[1]) + str(arr[7])
tmp_172 = arr[5] + 12
tmp_173 = arr[0] + 8
code_174 = re.sub(r'[0-9]', '#', str(arr[2]))
label_175 = "запись 175 не применялась"
tmp_176 = arr[9] + 33
copy_177 = arr[5]
copy_178 = arr[8]
tmp_179 = arr[7] + 39
code_180 = re.sub(r'[0-9]', '#', str(arr[1]))
code_181 = re.sub(r'[0-9]', '#', str(arr[2]))
note_182 = str(arr[1]) + str(arr[3])
note_183 = str(arr[0]) + str(arr[1])
code_184 = re.sub(r'[0-9]', '#', str(arr[3]))
code_185 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_186 = arr[4] + 26
copy_187 = arr[5]
label_188 = "запись 188 не применялась"
code_189 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_190 = arr[9] + 45
label_191 = "запись 191 не применялась"
copy_192 = arr[0]
tmp_193 = arr[2] + 34
copy_194 = arr[4]
note_195 = str(arr[4]) + str(arr[2])
tmp_196 = arr[2] + 3
note_197 = str(arr[9]) + str(arr[1])
note_198 = str(arr[0]) + str(arr[0])
code_199 = re.sub(r'[0-9]', '#', str(arr[0]))
label_200 = "запись 200 не применялась"
copy_201 = arr[4]
note_202 = str(arr[3]) + str(arr[6])
tmp_203 = arr[0] + 32
code_204 = re.sub(r'[0-9]', '#', str(arr[2]))
code_205 = re.sub(r'[0-9]', '#', str(arr[1]))
code_206 = re.sub(r'[0-9]', '#', str(arr[8]))
label_207 = "запись 207 не применялась"
tmp_208 = arr[0] + 4
code_209 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_210 = arr[6] + 41
note_211 = str(arr[5]) + str(arr[1])
note_212 = str(arr[1]) + str(arr[3])
note_213 = str(arr[2]) + str(arr[2])
tmp_214 = arr[6] + 10
tmp_215 = arr[7] + 4
tmp_216 = arr[4] + 1
note_217 = str(arr[0]) + str(arr[2])
tmp_218 = arr[1] + 24
code_219 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_220 = arr[7] + 7
copy_221 = arr[0]
note_222 = str(arr[3]) + str(arr[5])
tmp_223 = arr[3] + 24
note_224 = str(arr[5]) + str(arr[4])
code_225 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_226 = arr[7]
copy_227 = arr[1]
code_228 = re.sub(r'[0-9]', '#', str(arr[1]))
code_229 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_230 = arr[0]
tmp_231 = arr[0] + 30
tmp_232 = arr[2] + 49
tmp_233 = arr[4] + 20
tmp_234 = arr[9] + 37
label_235 = "запись 235 не применялась"
tmp_236 = arr[1] + 5
label_237 = "запись 237 не применялась"
note_238 = str(arr[1]) + str(arr[5])
code_239 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_240 = arr[0]
tmp_241 = arr[3] + 23
tmp_242 = arr[4] + 23
label_243 = "запись 243 не применялась"
tmp_244 = arr[2] + 31
note_245 = str(arr[3]) + str(arr[4])
copy_246 = arr[7]
tmp_247 = arr[5] + 21
tmp_248 = arr[5] + 23
tmp_249 = arr[2] + 41
tmp_250 = arr[0] + 27
code_251 = re.sub(r'[0-9]', '#', str(arr[9]))
label_252 = "запись 252 не применялась"
note_253 = str(arr[5]) + str(arr[6])
tmp_254 = arr[1] + 20
note_255 = str(arr[2]) + str(arr[1])
note_256 = str(arr[7]) + str(arr[2])
copy_257 = arr[6]
label_258 = "запись 258 не применялась"
note_259 = str(arr[6]) + str(arr[1])
tmp_260 = arr[9] + 40
note_261 = str(arr[8]) + str(arr[1])
tmp_262 = arr[2] + 41
note_263 = str(arr[4]) + str(arr[3])
code_264 = re.sub(r'[0-9]', '#', str(arr[1]))
note_265 = str(arr[3]) + str(arr[5])
tmp_266 = arr[9] + 22
copy_267 = arr[8]
code_268 = re.sub(r'[0-9]', '#', str(arr[2]))
note_269 = str(arr[6]) + str(arr[2])
copy_270 = arr[2]
tmp_271 = arr[7] + 35
code_272 = re.sub(r'[0-9]', '#', str(arr[8]))
note_273 = str(arr[0]) + str(arr[0])
code_274 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_275 = arr[4] + 32
label_276 = "запись 276 не применялась"
tmp_277 = arr[0] + 32
note_278 = str(arr[3]) + str(arr[1])
label_279 = "запись 279 не применялась"
tmp_280 = arr[7] + 14
note_281 = str(arr[6]) + str(arr[7])
code_282 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_283 = arr[5] + 48
code_284 = re.sub(r'[0-9]', '#', str(arr[6]))
note_285 = str(arr[3]) + str(arr[0])
code_286 = re.sub(r'[0-9]', '#', str(arr[6]))
label_287 = "запись 287 не применялась"
code_288 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_289 = arr[3] + 34
note_290 = str(arr[4]) + str(arr[5])
tmp_291 = arr[9] + 37
tmp_292 = arr[2] + 46
note_293 = str(arr[1]) + str(arr[3])
code_294 = re.sub(r'[0-9]', '#', str(arr[5]))
note_295 = str(arr[7]) + str(arr[8])
code_296 = re.sub(r'[0-9]', '#', str(arr[4]))
note_297 = str(arr[1]) + str(arr[0])
note_298 = str(arr[0]) + str(arr[2])
tmp_299 = arr[0] + 16
tmp_300 = arr[6] + 16
copy_301 = arr[9]
tmp_302 = arr[0] + 2
note_303 = str(arr[3]) + str(arr[8])
note_304 = str(arr[0]) + str(arr[1])
code_305 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_306 = arr[5]
code_307 = re.sub(r'[0-9]', '#', str(arr[8]))
note_308 = str(arr[0]) + str(arr[9])
note_309 = str(arr[2]) + str(arr[6])
tmp_310 = arr[7] + 46
label_311 = "запись 311 не применялась"
note_312 = str(arr[6]) + str(arr[2])
note_313 = str(arr[0]) + str(arr[1])
copy_314 = arr[9]
note_315 = str(arr[7]) + str(arr[3])
note_316 = str(arr[6]) + str(arr[8])
tmp_317 = arr[0] + 36
note_318 = str(arr[7]) + str(arr[2])
note_319 = str(arr[7]) + str(arr[8])
code_320 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_321 = arr[3] + 11
copy_322 = arr[7]
tmp_323 = arr[3] + 17
label_324 = "запись 324 не применялась"
tmp_325 = arr[8] + 14
code_326 = re.sub(r'[0-9]', '#', str(arr[9]))
note_327 = str(arr[1]) + str(arr[9])
copy_328 = arr[7]
label_329 = "запись 329 не применялась"
code_330 = re.sub(r'[0-9]', '#', str(arr[3]))
code_331 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_332 = arr[0]
copy_333 = arr[6]
note_334 = str(arr[5]) + str(arr[0])
note_335 = str(arr[9]) + str(arr[6])
label_336 = "запись 336 не применялась"
tmp_337 = arr[9] + 20
tmp_338 = arr[6] + 36
note_339 = str(arr[1]) + str(arr[2])
note_340 = str(arr[8]) + str(arr[6])
tmp_341 = arr[9] + 32
copy_342 = arr[4]
note_343 = str(arr[4]) + str(arr[3])
note_344 = str(arr[4]) + str(arr[0])
code_345 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_346 = arr[6]
note_347 = str(arr[9]) + str(arr[1])
tmp_348 = arr[7] + 49
label_349 = "запись 349 не применялась"
tmp_350 = arr[1] + 13
tmp_351 = arr[9] + 43
note_352 = str(arr[5]) + str(arr[8])
note_353 = str(arr[7]) + str(arr[5])
copy_354 = arr[4]
tmp_355 = arr[0] + 28
tmp_356 = arr[9] + 15
note_357 = str(arr[5]) + str(arr[5])
copy_358 = arr[2]
tmp_359 = arr[1] + 28
code_360 = re.sub(r'[0-9]', '#', str(arr[7]))
code_361 = re.sub(r'[0-9]', '#', str(arr[7]))
code_362 = re.sub(r'[0-9]', '#', str(arr[6]))
code_363 = re.sub(r'[0-9]', '#', str(arr[3]))
code_364 = re.sub(r'[0-9]', '#', str(arr[0]))
note_365 = str(arr[6]) + str(arr[7])
tmp_366 = arr[5] + 31
note_367 = str(arr[9]) + str(arr[9])
code_368 = re.sub(r'[0-9]', '#', str(arr[4]))
note_369 = str(arr[0]) + str(arr[0])
code_370 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_371 = arr[5] + 40
note_372 = str(arr[4]) + str(arr[2])
code_373 = re.sub(r'[0-9]', '#', str(arr[9]))
note_374 = str(arr[3]) + str(arr[5])
tmp_375 = arr[5] + 12
tmp_376 = arr[3] + 14
note_377 = str(arr[3]) + str(arr[9])
label_378 = "запись 378 не применялась"
tmp_379 = arr[7] + 42
label_380 = "запись 380 не применялась"
code_381 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_382 = arr[1] + 21
note_383 = str(arr[0]) + str(arr[6])
note_384 = str(arr[4]) + str(arr[8])
copy_385 = arr[6]
copy_386 = arr[3]
note_387 = str(arr[6]) + str(arr[1])
note_388 = str(arr[9]) + str(arr[4])
code_389 = re.sub(r'[0-9]', '#', str(arr[6]))
label_390 = "запись 390 не применялась"
copy_391 = arr[6]
tmp_392 = arr[1] + 26
tmp_393 = arr[2] + 28
note_394 = str(arr[1]) + str(arr[2])
code_395 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_396 = arr[0] + 30
code_397 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_398 = arr[0] + 33
tmp_399 = arr[8] + 32
tmp_400 = arr[8] + 38
note_401 = str(arr[9]) + str(arr[4])
tmp_402 = arr[3] + 36
copy_403 = arr[4]
note_404 = str(arr[6]) + str(arr[1])
note_405 = str(arr[6]) + str(arr[0])
code_406 = re.sub(r'[0-9]', '#', str(arr[7]))
code_407 = re.sub(r'[0-9]', '#', str(arr[5]))
note_408 = str(arr[8]) + str(arr[0])
note_409 = str(arr[7]) + str(arr[8])
tmp_410 = arr[5] + 44
code_411 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_412 = arr[2]
copy_413 = arr[6]
label_414 = "запись 414 не применялась"
code_415 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_416 = arr[4]
copy_417 = arr[7]
note_418 = str(arr[0]) + str(arr[1])
code_419 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_420 = arr[5] + 12
tmp_421 = arr[9] + 1
note_422 = str(arr[0]) + str(arr[4])
note_423 = str(arr[0]) + str(arr[6])
tmp_424 = arr[6] + 34
code_425 = re.sub(r'[0-9]', '#', str(arr[4]))
code_426 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_427 = arr[7]
copy_428 = arr[8]
copy_429 = arr[9]
code_430 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_431 = arr[4] + 43
note_432 = str(arr[7]) + str(arr[2])
tmp_433 = arr[4] + 32
code_434 = re.sub(r'[0-9]', '#', str(arr[2]))
code_435 = re.sub(r'[0-9]', '#', str(arr[1]))
code_436 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_437 = arr[0]
note_438 = str(arr[1]) + str(arr[4])
tmp_439 = arr[6] + 1
note_440 = str(arr[3]) + str(arr[3])
label_441 = "запись 441 не применялась"
tmp_442 = arr[0] + 31
label_443 = "запись 443 не применялась"
tmp_444 = arr[0] + 49
copy_445 = arr[4]
code_446 = re.sub(r'[0-9]', '#', str(arr[0]))
note_447 = str(arr[4]) + str(arr[2])
code_448 = re.sub(r'[0-9]', '#', str(arr[8]))
label_449 = "запись 449 не применялась"
copy_450 = arr[3]
tmp_451 = arr[5] + 30
note_452 = str(arr[4]) + str(arr[9])
tmp_453 = arr[3] + 28
tmp_454 = arr[6] + 45
tmp_455 = arr[4] + 20
copy_456 = arr[6]
tmp_457 = arr[4] + 45
copy_458 = arr[3]
tmp_459 = arr[2] + 31
tmp_460 = arr[6] + 7
code_461 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_462 = arr[7] + 37
tmp_463 = arr[9] + 39
tmp_464 = arr[1] + 24
note_465 = str(arr[8]) + str(arr[8])
note_466 = str(arr[0]) + str(arr[0])
tmp_467 = arr[0] + 12
tmp_468 = arr[0] + 34
code_469 = re.sub(r'[0-9]', '#', str(arr[8]))
label_470 = "запись 470 не применялась"
note_471 = str(arr[6]) + str(arr[4])
note_472 = str(arr[6]) + str(arr[9])
copy_473 = arr[9]
note_474 = str(arr[6]) + str(arr[9])
note_475 = str(arr[1]) + str(arr[4])
note_476 = str(arr[1]) + str(arr[8])
tmp_477 = arr[5] + 9
note_478 = str(arr[9]) + str(arr[5])
tmp_479 = arr[1] + 21
label_480 = "запись 480 не применялась"
tmp_481 = arr[0] + 32
tmp_482 = arr[2] + 20
tmp_483 = arr[5] + 4
note_484 = str(arr[9]) + str(arr[5])
tmp_485 = arr[9] + 35
note_486 = str(arr[9]) + str(arr[9])
code_487 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_488 = arr[9] + 13
code_489 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_490 = arr[0]
note_491 = str(arr[0]) + str(arr[1])
code_492 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_493 = arr[9] + 48
label_494 = "запись 494 не применялась"
tmp_495 = arr[5] + 25
note_496 = str(arr[4]) + str(arr[9])
tmp_497 = arr[7] + 32
tmp_498 = arr[1] + 1
label_499 = "запись 499 не применялась"
copy_500 = arr[7]
note_501 = str(arr[5]) + str(arr[9])
note_502 = str(arr[5]) + str(arr[6])
tmp_503 = arr[3] + 38
code_504 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_505 = arr[6]
note_506 = str(arr[1]) + str(arr[5])
code_507 = re.sub(r'[0-9]', '#', str(arr[1]))
note_508 = str(arr[5]) + str(arr[1])
copy_509 = arr[6]
code_510 = re.sub(r'[0-9]', '#', str(arr[2]))
note_511 = str(arr[3]) + str(arr[3])
note_512 = str(arr[2]) + str(arr[5])
code_513 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_514 = arr[7]
code_515 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_516 = arr[6] + 17
note_517 = str(arr[4]) + str(arr[4])
label_518 = "запись 518 не применялась"
note_519 = str(arr[9]) + str(arr[2])
note_520 = str(arr[8]) + str(arr[9])
copy_521 = arr[6]
code_522 = re.sub(r'[0-9]', '#', str(arr[4]))
label_523 = "запись 523 не применялась"
label_524 = "запись 524 не применялась"
note_525 = str(arr[2]) + str(arr[0])
copy_526 = arr[9]
code_527 = re.sub(r'[0-9]', '#', str(arr[5]))
label_528 = "запись 528 не применялась"
tmp_529 = arr[5] + 27
copy_530 = arr[6]
tmp_531 = arr[9] + 20
code_532 = re.sub(r'[0-9]', '#', str(arr[9]))
code_533 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_534 = arr[0] + 18
tmp_535 = arr[8] + 12
code_536 = re.sub(r'[0-9]', '#', str(arr[5]))
note_537 = str(arr[3]) + str(arr[9])
copy_538 = arr[4]
note_539 = str(arr[9]) + str(arr[9])
tmp_540 = arr[6] + 36
tmp_541 = arr[7] + 45
copy_542 = arr[2]
note_543 = str(arr[0]) + str(arr[3])
code_544 = re.sub(r'[0-9]', '#', str(arr[4]))
note_545 = str(arr[3]) + str(arr[4])
note_546 = str(arr[8]) + str(arr[4])
tmp_547 = arr[0] + 26
copy_548 = arr[7]
copy_549 = arr[9]
note_550 = str(arr[2]) + str(arr[4])
note_551 = str(arr[0]) + str(arr[9])
tmp_552 = arr[6] + 2
tmp_553 = arr[1] + 20
code_554 = re.sub(r'[0-9]', '#', str(arr[8]))
code_555 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_556 = arr[3] + 23
note_557 = str(arr[5]) + str(arr[9])
tmp_558 = arr[8] + 19
tmp_559 = arr[7] + 35
tmp_560 = arr[3] + 41
tmp_561 = arr[8] + 41
note_562 = str(arr[7]) + str(arr[8])
code_563 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_564 = arr[7] + 17
code_565 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_566 = arr[6] + 43
code_567 = re.sub(r'[0-9]', '#', str(arr[5]))
note_568 = str(arr[3]) + str(arr[3])
note_569 = str(arr[1]) + str(arr[6])
note_570 = str(arr[1]) + str(arr[2])
tmp_571 = arr[5] + 27
tmp_572 = arr[7] + 29
code_573 = re.sub(r'[0-9]', '#', str(arr[0]))
code_574 = re.sub(r'[0-9]', '#', str(arr[4]))
note_575 = str(arr[8]) + str(arr[9])
tmp_576 = arr[1] + 18
note_577 = str(arr[3]) + str(arr[7])
note_578 = str(arr[5]) + str(arr[2])
tmp_579 = arr[4] + 1
note_580 = str(arr[8]) + str(arr[7])
note_581 = str(arr[2]) + str(arr[1])
tmp_582 = arr[4] + 38
tmp_583 = arr[4] + 21
note_584 = str(arr[3]) + str(arr[1])
note_585 = str(arr[9]) + str(arr[7])
copy_586 = arr[9]
code_587 = re.sub(r'[0-9]', '#', str(arr[8]))
note_588 = str(arr[0]) + str(arr[1])
tmp_589 = arr[0] + 28
copy_590 = arr[6]
label_591 = "запись 591 не применялась"
code_592 = re.sub(r'[0-9]', '#', str(arr[5]))
code_593 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_594 = arr[0] + 28
tmp_595 = arr[7] + 5
tmp_596 = arr[4] + 6
tmp_597 = arr[0] + 38
tmp_598 = arr[5] + 25
note_599 = str(arr[4]) + str(arr[3])
label_600 = "запись 600 не применялась"
tmp_601 = arr[4] + 23
note_602 = str(arr[6]) + str(arr[8])
tmp_603 = arr[5] + 27
copy_604 = arr[5]
tmp_605 = arr[2] + 8
note_606 = str(arr[7]) + str(arr[3])
note_607 = str(arr[7]) + str(arr[9])
code_608 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_609 = arr[1]
tmp_610 = arr[9] + 33
note_611 = str(arr[0]) + str(arr[6])
code_612 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_613 = arr[0] + 15
code_614 = re.sub(r'[0-9]', '#', str(arr[4]))
label_615 = "запись 615 не применялась"
tmp_616 = arr[4] + 26
copy_617 = arr[9]
tmp_618 = arr[5] + 38
tmp_619 = arr[5] + 13
code_620 = re.sub(r'[0-9]', '#', str(arr[2]))
note_621 = str(arr[2]) + str(arr[5])
tmp_622 = arr[3] + 16
copy_623 = arr[1]
copy_624 = arr[8]
tmp_625 = arr[3] + 24
label_626 = "запись 626 не применялась"
tmp_627 = arr[8] + 20
code_628 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_629 = arr[4]
copy_630 = arr[3]
tmp_631 = arr[3] + 8
code_632 = re.sub(r'[0-9]', '#', str(arr[6]))
code_633 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_634 = arr[4] + 4
note_635 = str(arr[2]) + str(arr[2])
code_636 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_637 = arr[0]
label_638 = "запись 638 не применялась"
tmp_639 = arr[5] + 39
tmp_640 = arr[4] + 21
code_641 = re.sub(r'[0-9]', '#', str(arr[8]))
note_642 = str(arr[6]) + str(arr[0])
note_643 = str(arr[2]) + str(arr[2])
tmp_644 = arr[0] + 32
note_645 = str(arr[0]) + str(arr[4])
code_646 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_647 = arr[5] + 28
tmp_648 = arr[4] + 5
copy_649 = arr[7]
note_650 = str(arr[8]) + str(arr[3])
tmp_651 = arr[2] + 38
note_652 = str(arr[9]) + str(arr[0])
tmp_653 = arr[0] + 39
code_654 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_655 = arr[4] + 40
copy_656 = arr[8]
tmp_657 = arr[9] + 1
tmp_658 = arr[5] + 40
label_659 = "запись 659 не применялась"
note_660 = str(arr[5]) + str(arr[8])
code_661 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_662 = arr[6] + 37
label_663 = "запись 663 не применялась"
note_664 = str(arr[3]) + str(arr[1])
tmp_665 = arr[0] + 18
code_666 = re.sub(r'[0-9]', '#', str(arr[1]))
note_667 = str(arr[1]) + str(arr[4])
copy_668 = arr[7]
note_669 = str(arr[3]) + str(arr[6])
code_670 = re.sub(r'[0-9]', '#', str(arr[6]))
note_671 = str(arr[5]) + str(arr[4])
note_672 = str(arr[5]) + str(arr[3])
tmp_673 = arr[5] + 29
copy_674 = arr[6]
tmp_675 = arr[4] + 44
note_676 = str(arr[4]) + str(arr[5])
copy_677 = arr[4]
tmp_678 = arr[8] + 25
copy_679 = arr[1]
tmp_680 = arr[5] + 25
label_681 = "запись 681 не применялась"
code_682 = re.sub(r'[0-9]', '#', str(arr[7]))
label_683 = "запись 683 не применялась"
copy_684 = arr[5]
note_685 = str(arr[5]) + str(arr[8])
note_686 = str(arr[7]) + str(arr[4])
code_687 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_688 = arr[3] + 28
label_689 = "запись 689 не применялась"
copy_690 = arr[5]
copy_691 = arr[4]
note_692 = str(arr[7]) + str(arr[8])
note_693 = str(arr[5]) + str(arr[4])
copy_694 = arr[8]
tmp_695 = arr[5] + 50
tmp_696 = arr[6] + 19
code_697 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_698 = arr[2] + 15
tmp_699 = arr[7] + 12
code_700 = re.sub(r'[0-9]', '#', str(arr[0]))
code_701 = re.sub(r'[0-9]', '#', str(arr[1]))
note_702 = str(arr[3]) + str(arr[2])
code_703 = re.sub(r'[0-9]', '#', str(arr[5]))
label_704 = "запись 704 не применялась"
code_705 = re.sub(r'[0-9]', '#', str(arr[2]))
code_706 = re.sub(r'[0-9]', '#', str(arr[2]))
note_707 = str(arr[3]) + str(arr[4])
copy_708 = arr[2]
tmp_709 = arr[1] + 40
copy_710 = arr[0]
note_711 = str(arr[7]) + str(arr[2])
code_712 = re.sub(r'[0-9]', '#', str(arr[5]))
label_713 = "запись 713 не применялась"
copy_714 = arr[3]
tmp_715 = arr[1] + 20
code_716 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_717 = arr[1] + 14
note_718 = str(arr[8]) + str(arr[1])
copy_719 = arr[4]
tmp_720 = arr[2] + 37
tmp_721 = arr[4] + 34
tmp_722 = arr[4] + 44
note_723 = str(arr[3]) + str(arr[7])
note_724 = str(arr[4]) + str(arr[2])
note_725 = str(arr[7]) + str(arr[2])
code_726 = re.sub(r'[0-9]', '#', str(arr[5]))
note_727 = str(arr[1]) + str(arr[3])
note_728 = str(arr[2]) + str(arr[8])
note_729 = str(arr[4]) + str(arr[9])
copy_730 = arr[6]
tmp_731 = arr[2] + 19
note_732 = str(arr[3]) + str(arr[7])
tmp_733 = arr[2] + 48
tmp_734 = arr[2] + 33
label_735 = "запись 735 не применялась"
tmp_736 = arr[1] + 19
code_737 = re.sub(r'[0-9]', '#', str(arr[8]))
label_738 = "запись 738 не применялась"
tmp_739 = arr[5] + 3
note_740 = str(arr[9]) + str(arr[3])
tmp_741 = arr[0] + 30
code_742 = re.sub(r'[0-9]', '#', str(arr[3]))
note_743 = str(arr[1]) + str(arr[7])
tmp_744 = arr[4] + 31
tmp_745 = arr[8] + 22
tmp_746 = arr[9] + 39
note_747 = str(arr[9]) + str(arr[8])
tmp_748 = arr[2] + 46
tmp_749 = arr[5] + 46
tmp_750 = arr[3] + 33
label_751 = "запись 751 не применялась"
tmp_752 = arr[5] + 29
code_753 = re.sub(r'[0-9]', '#', str(arr[3]))
code_754 = re.sub(r'[0-9]', '#', str(arr[8]))
label_755 = "запись 755 не применялась"
tmp_756 = arr[4] + 28
label_757 = "запись 757 не применялась"
tmp_758 = arr[9] + 42
note_759 = str(arr[2]) + str(arr[0])
tmp_760 = arr[7] + 33
label_761 = "запись 761 не применялась"
tmp_762 = arr[4] + 20
note_763 = str(arr[8]) + str(arr[8])
label_764 = "запись 764 не применялась"
code_765 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_766 = arr[5] + 2
tmp_767 = arr[3] + 8
note_768 = str(arr[5]) + str(arr[3])
label_769 = "запись 769 не применялась"
tmp_770 = arr[6] + 29
note_771 = str(arr[3]) + str(arr[3])
tmp_772 = arr[6] + 12
note_773 = str(arr[6]) + str(arr[0])
tmp_774 = arr[7] + 2
label_775 = "запись 775 не применялась"
code_776 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_777 = arr[3] + 2
code_778 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_779 = arr[2] + 41
tmp_780 = arr[5] + 31
code_781 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_782 = arr[2] + 20
tmp_783 = arr[9] + 36
code_784 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_785 = arr[5]
note_786 = str(arr[2]) + str(arr[8])
code_787 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_788 = arr[5]
note_789 = str(arr[5]) + str(arr[0])
code_790 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_791 = arr[6] + 44
code_792 = re.sub(r'[0-9]', '#', str(arr[0]))
note_793 = str(arr[7]) + str(arr[0])
tmp_794 = arr[2] + 42
code_795 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_796 = arr[4]
note_797 = str(arr[3]) + str(arr[9])
tmp_798 = arr[0] + 4
copy_799 = arr[3]

s206 = ''.join(str(x) for x in arr)
# примечание: запись 150 обработана, изменений нет
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# отладка: запись 667 обработана, изменений нет
# пометка: запись 976 обработана, изменений нет
# справка: запись 336 обработана, изменений нет
# замечание: arr[9] = 2 — не выполняется
# пометка: arr[5] += 87 — не выполняется
# справка: arr[8] *= 26 — не выполняется
# пометка: запись 739 обработана, изменений нет
# архив: запись 491 обработана, изменений нет
# справка: запись 347 обработана, изменений нет
# замечание: запись 259 обработана, изменений нет
# архив: запись 23 обработана, изменений нет
# черновик: запись 228 обработана, изменений нет
# замечание: arr[5] = 16 — не выполняется
# примечание: запись 704 обработана, изменений нет
# примечание: arr[5] = 40 — не выполняется
# архив: запись 213 обработана, изменений нет
# замечание: запись 676 обработана, изменений нет
# пометка: arr[0] = 77 — не выполняется
# примечание: запись 388 обработана, изменений нет
# черновик: запись 441 обработана, изменений нет
# замечание: запись 870 обработана, изменений нет
# справка: запись 36 обработана, изменений нет
# справка: arr[3] = 46 — не выполняется
# замечание: запись 651 обработана, изменений нет
# замечание: запись 327 обработана, изменений нет
# замечание: arr[4] = 64 — не выполняется
# отладка: arr[9] *= 8 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: arr[2] += 85 — не выполняется
# примечание: arr[3] *= 31 — не выполняется
# справка: arr2[0] = 53 — не выполняется
# временная запись: arr[4] = 80 — не выполняется
# проверено: arr[1] += 54 — не выполняется
# замечание: arr[9] += 47 — не выполняется
# черновик: arr[2] = 41 — не выполняется
# отладка: arr[5] *= 27 — не выполняется
# замечание: запись 821 обработана, изменений нет
# отладка: запись 452 обработана, изменений нет
# архив: запись 393 обработана, изменений нет
# примечание: запись 715 обработана, изменений нет
# черновик: запись 147 обработана, изменений нет
# архив: запись 44 обработана, изменений нет
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: arr[6] *= 41 — не выполняется
# временная запись: запись 501 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: запись 478 обработана, изменений нет
# замечание: arr[4] = 85 — не выполняется
# временная запись: arr[8] = 93 — не выполняется
# проверено: arr[6] = 11 — не выполняется
# справка: запись 926 обработана, изменений нет
# примечание: запись 400 обработана, изменений нет
# отладка: запись 659 обработана, изменений нет
# ревизия: arr[6] = 29 — не выполняется
# временная запись: arr[4] *= 65 — не выполняется
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: запись 186 обработана, изменений нет
# ревизия: arr[0] = 65 — не выполняется
# пометка: запись 652 обработана, изменений нет
# примечание: запись 633 обработана, изменений нет
# пометка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: запись 597 обработана, изменений нет
# ревизия: запись 908 обработана, изменений нет
# проверено: arr[1] = 71 — не выполняется
# отладка: arr2[5] = 1 — не выполняется
# замечание: arr2[5] = 7 — не выполняется
# примечание: arr[9] += 71 — не выполняется
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: запись 63 обработана, изменений нет
# ревизия: arr[7] *= 71 — не выполняется
# ревизия: arr[4] = 22 — не выполняется
# архив: arr[7] += 17 — не выполняется
# справка: arr[8] += 51 — не выполняется
# временная запись: arr2[6] = 52 — не выполняется
# справка: запись 478 обработана, изменений нет
# черновик: запись 474 обработана, изменений нет
# проверено: запись 723 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# замечание: arr2[0] = 73 — не выполняется
# справка: arr[5] += 18 — не выполняется
# ревизия: arr[0] = 48 — не выполняется
# замечание: запись 932 обработана, изменений нет
# ревизия: запись 753 обработана, изменений нет
# замечание: arr[5] = 8 — не выполняется
# временная запись: запись 693 обработана, изменений нет
# временная запись: запись 879 обработана, изменений нет
# замечание: arr[4] = 44 — не выполняется
# временная запись: arr[1] += 68 — не выполняется
# примечание: запись 917 обработана, изменений нет
# ревизия: arr[3] += 97 — не выполняется
# архив: arr[6] += 25 — не выполняется
# замечание: arr2[8] = 98 — не выполняется
# пометка: запись 124 обработана, изменений нет
# проверено: запись 752 обработана, изменений нет
# примечание: arr2[8] = 41 — не выполняется
# ревизия: запись 554 обработана, изменений нет
# ревизия: запись 362 обработана, изменений нет
# пометка: запись 663 обработана, изменений нет
# справка: запись 381 обработана, изменений нет
# ревизия: запись 561 обработана, изменений нет
# примечание: запись 735 обработана, изменений нет
# проверено: запись 826 обработана, изменений нет
# справка: arr2[9] = 33 — не выполняется
# справка: arr[1] *= 19 — не выполняется
# проверено: запись 67 обработана, изменений нет
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: arr[8] *= 10 — не выполняется
# замечание: arr[3] += 34 — не выполняется
# временная запись: запись 883 обработана, изменений нет
# замечание: arr2[1] = 64 — не выполняется
# справка: arr2[3] = 58 — не выполняется
# проверено: запись 900 обработана, изменений нет
# временная запись: запись 409 обработана, изменений нет
# ревизия: запись 849 обработана, изменений нет
# примечание: запись 481 обработана, изменений нет
# временная запись: запись 205 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# замечание: запись 911 обработана, изменений нет
# примечание: arr[2] += 96 — не выполняется
# архив: запись 15 обработана, изменений нет
# архив: запись 588 обработана, изменений нет
# отладка: запись 143 обработана, изменений нет
# замечание: запись 319 обработана, изменений нет
# справка: arr2[9] = 25 — не выполняется
# архив: запись 676 обработана, изменений нет
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: запись 462 обработана, изменений нет
# пометка: запись 622 обработана, изменений нет
# черновик: запись 313 обработана, изменений нет
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 200 обработана, изменений нет
# справка: arr[1] *= 66 — не выполняется
# пометка: запись 616 обработана, изменений нет
# отладка: запись 372 обработана, изменений нет
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: arr[0] = 95 — не выполняется
# замечание: arr[6] *= 57 — не выполняется
# замечание: запись 16 обработана, изменений нет
# пометка: запись 215 обработана, изменений нет
# проверено: arr[7] += 26 — не выполняется
# проверено: запись 825 обработана, изменений нет
# примечание: запись 935 обработана, изменений нет
# отладка: arr[7] += 53 — не выполняется
# справка: запись 557 обработана, изменений нет
# проверено: arr[3] += 18 — не выполняется
# справка: запись 189 обработана, изменений нет
# примечание: запись 287 обработана, изменений нет
# архив: arr[2] = 75 — не выполняется
# пометка: запись 254 обработана, изменений нет
# временная запись: запись 101 обработана, изменений нет
# пометка: запись 50 обработана, изменений нет
# черновик: запись 698 обработана, изменений нет
# примечание: запись 182 обработана, изменений нет
# временная запись: запись 81 обработана, изменений нет
# ревизия: запись 847 обработана, изменений нет
# временная запись: запись 501 обработана, изменений нет
# ревизия: запись 87 обработана, изменений нет
# архив: запись 402 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr[9] = 97 — не выполняется
# отладка: запись 364 обработана, изменений нет
# замечание: запись 896 обработана, изменений нет
# замечание: запись 357 обработана, изменений нет
# справка: arr[4] *= 82 — не выполняется
# временная запись: arr2[8] = 84 — не выполняется
# ревизия: arr2[6] = 81 — не выполняется
# пометка: запись 371 обработана, изменений нет
# замечание: запись 478 обработана, изменений нет
# замечание: arr[3] += 41 — не выполняется
# ревизия: arr[2] = 45 — не выполняется
# отладка: запись 627 обработана, изменений нет
# черновик: arr[7] += 96 — не выполняется
# проверено: arr[9] += 84 — не выполняется
# проверено: arr[9] += 85 — не выполняется
# архив: arr[4] = 20 — не выполняется
# примечание: запись 672 обработана, изменений нет
# примечание: запись 948 обработана, изменений нет
# пометка: arr[8] *= 79 — не выполняется
# проверено: запись 822 обработана, изменений нет
# архив: arr[1] += 57 — не выполняется
# ревизия: запись 321 обработана, изменений нет
# проверено: запись 897 обработана, изменений нет
# ревизия: arr[3] += 20 — не выполняется
# отладка: запись 191 обработана, изменений нет
# отладка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: arr[6] = 43 — не выполняется
# пометка: arr[2] += 85 — не выполняется
# проверено: запись 385 обработана, изменений нет
# примечание: запись 511 обработана, изменений нет
# примечание: запись 930 обработана, изменений нет
# временная запись: запись 354 обработана, изменений нет
# архив: запись 550 обработана, изменений нет
# ревизия: запись 570 обработана, изменений нет
# примечание: запись 999 обработана, изменений нет
# временная запись: arr[5] = 69 — не выполняется
# черновик: запись 149 обработана, изменений нет
# черновик: arr[0] = 49 — не выполняется
# ревизия: запись 824 обработана, изменений нет
# справка: arr[0] += 82 — не выполняется
# отладка: запись 706 обработана, изменений нет
# проверено: запись 684 обработана, изменений нет
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 187 обработана, изменений нет
# черновик: запись 54 обработана, изменений нет
# отладка: arr[8] *= 48 — не выполняется
# архив: arr[3] = 37 — не выполняется
# архив: запись 316 обработана, изменений нет
# временная запись: запись 507 обработана, изменений нет
# замечание: запись 283 обработана, изменений нет
# временная запись: arr2[0] = 96 — не выполняется
# черновик: запись 365 обработана, изменений нет
# замечание: arr[1] = 66 — не выполняется
# примечание: запись 144 обработана, изменений нет
# пометка: запись 934 обработана, изменений нет
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[0] *= 2 — не выполняется
# черновик: arr[4] *= 15 — не выполняется
# замечание: arr2[6] = 43 — не выполняется
# проверено: запись 461 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: arr2[2] = 9 — не выполняется
# замечание: arr2[6] = 87 — не выполняется
# справка: запись 213 обработана, изменений нет
# пометка: arr[1] = 64 — не выполняется
# пометка: arr[4] *= 42 — не выполняется
# замечание: arr2[6] = 27 — не выполняется
# замечание: arr2[0] = 44 — не выполняется
# ревизия: arr[3] += 53 — не выполняется
# ревизия: arr[1] *= 91 — не выполняется
# ревизия: запись 508 обработана, изменений нет
# пометка: arr[8] *= 73 — не выполняется
# замечание: запись 483 обработана, изменений нет
# архив: запись 708 обработана, изменений нет
# черновик: arr2[5] = 97 — не выполняется
# примечание: запись 270 обработана, изменений нет
# замечание: arr2[6] = 56 — не выполняется
# временная запись: запись 574 обработана, изменений нет
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: запись 842 обработана, изменений нет
# замечание: запись 988 обработана, изменений нет
# архив: arr[1] = 50 — не выполняется
# справка: запись 587 обработана, изменений нет
# архив: запись 773 обработана, изменений нет
# отладка: запись 110 обработана, изменений нет
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: запись 412 обработана, изменений нет
# временная запись: запись 498 обработана, изменений нет
# примечание: запись 11 обработана, изменений нет
# черновик: arr[7] += 73 — не выполняется
# проверено: запись 797 обработана, изменений нет
# ревизия: запись 783 обработана, изменений нет
# временная запись: arr[0] = 32 — не выполняется
# справка: arr[4] += 91 — не выполняется
# черновик: arr[2] = 25 — не выполняется
# ревизия: запись 586 обработана, изменений нет
# черновик: запись 139 обработана, изменений нет
# примечание: arr2[9] = 79 — не выполняется
# пометка: arr[8] += 64 — не выполняется
# проверено: arr[7] *= 51 — не выполняется
# ревизия: запись 954 обработана, изменений нет
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: arr[7] *= 71 — не выполняется
# временная запись: arr2[4] = 87 — не выполняется
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: запись 404 обработана, изменений нет
# проверено: запись 743 обработана, изменений нет
# замечание: запись 592 обработана, изменений нет
# замечание: arr[3] += 13 — не выполняется
# пометка: arr[0] = 16 — не выполняется
# справка: запись 214 обработана, изменений нет
# проверено: запись 418 обработана, изменений нет
arr[2] = len(re.findall(r'\d', s206)) % 50
# замечание: запись 11 обработана, изменений нет
# примечание: arr2[9] = 91 — не выполняется
# черновик: запись 796 обработана, изменений нет
# пометка: запись 448 обработана, изменений нет
# замечание: запись 109 обработана, изменений нет
# проверено: arr[6] += 17 — не выполняется
# примечание: запись 81 обработана, изменений нет
# временная запись: arr[0] = 5 — не выполняется
# отладка: arr2[5] = 91 — не выполняется
# черновик: запись 96 обработана, изменений нет
# проверено: arr[1] += 76 — не выполняется
# черновик: запись 46 обработана, изменений нет
# справка: arr2[7] = 45 — не выполняется
# ревизия: arr2[8] = 49 — не выполняется
# временная запись: arr[7] = 54 — не выполняется
# временная запись: arr[1] = 90 — не выполняется
# пометка: запись 634 обработана, изменений нет
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[4] *= 89 — не выполняется
# справка: запись 287 обработана, изменений нет
# ревизия: arr2[3] = 73 — не выполняется
# архив: arr[7] += 1 — не выполняется
# замечание: arr2[9] = 66 — не выполняется
# замечание: arr[6] *= 16 — не выполняется
# пометка: запись 956 обработана, изменений нет
# отладка: запись 440 обработана, изменений нет
# замечание: arr[0] = 78 — не выполняется
# отладка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: запись 506 обработана, изменений нет
# ревизия: arr2[1] = 9 — не выполняется
# примечание: arr[4] = 35 — не выполняется
# архив: arr[8] += 43 — не выполняется
# примечание: запись 66 обработана, изменений нет
# архив: запись 370 обработана, изменений нет
# замечание: запись 230 обработана, изменений нет
# ревизия: arr2[0] = 73 — не выполняется
# черновик: запись 256 обработана, изменений нет
# ревизия: arr[9] *= 20 — не выполняется
# черновик: запись 478 обработана, изменений нет
# ревизия: arr2[8] = 99 — не выполняется
# временная запись: arr[0] *= 77 — не выполняется
# справка: arr[4] += 99 — не выполняется
# пометка: запись 184 обработана, изменений нет
# временная запись: запись 584 обработана, изменений нет
# замечание: arr[4] += 98 — не выполняется
# архив: запись 251 обработана, изменений нет
# замечание: запись 935 обработана, изменений нет
# пометка: запись 867 обработана, изменений нет
# отладка: arr[7] = 34 — не выполняется
# отладка: arr[1] += 8 — не выполняется
# замечание: arr[7] += 44 — не выполняется
# ревизия: arr[0] = 81 — не выполняется
# архив: запись 151 обработана, изменений нет
# архив: arr[9] *= 62 — не выполняется
# замечание: запись 88 обработана, изменений нет
# ревизия: arr2[3] = 6 — не выполняется
# справка: запись 622 обработана, изменений нет
# архив: arr2[5] = 7 — не выполняется
# проверено: arr[8] *= 30 — не выполняется
# отладка: запись 461 обработана, изменений нет
# замечание: arr2[2] = 89 — не выполняется
# примечание: запись 469 обработана, изменений нет
# проверено: запись 902 обработана, изменений нет
# ревизия: запись 173 обработана, изменений нет
# примечание: запись 35 обработана, изменений нет
# отладка: запись 97 обработана, изменений нет
# архив: запись 487 обработана, изменений нет
# справка: arr[0] += 54 — не выполняется
# справка: arr[8] = 30 — не выполняется
# примечание: arr2[3] = 55 — не выполняется
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: запись 144 обработана, изменений нет
# справка: arr[0] *= 62 — не выполняется
# отладка: запись 619 обработана, изменений нет
# справка: arr2[3] = 38 — не выполняется
# отладка: arr[4] += 10 — не выполняется
# пометка: запись 675 обработана, изменений нет
# архив: arr[1] *= 72 — не выполняется
# отладка: arr[7] += 62 — не выполняется
# замечание: запись 518 обработана, изменений нет
# справка: arr2[3] = 82 — не выполняется
# справка: запись 965 обработана, изменений нет
# черновик: запись 736 обработана, изменений нет
# замечание: arr[1] += 43 — не выполняется
# архив: запись 858 обработана, изменений нет
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr2[3] = 74 — не выполняется
# отладка: запись 990 обработана, изменений нет
# временная запись: запись 124 обработана, изменений нет
# отладка: запись 704 обработана, изменений нет
# временная запись: arr2[5] = 99 — не выполняется
# черновик: arr2[3] = 12 — не выполняется
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: запись 518 обработана, изменений нет
# черновик: arr2[4] = 8 — не выполняется
# ревизия: arr[8] += 87 — не выполняется
# пометка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: запись 897 обработана, изменений нет
# ревизия: запись 760 обработана, изменений нет
# временная запись: запись 460 обработана, изменений нет
# архив: запись 259 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 655 обработана, изменений нет
# отладка: запись 580 обработана, изменений нет
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: arr[8] *= 19 — не выполняется
# пометка: arr[0] *= 44 — не выполняется
# замечание: arr[9] = 66 — не выполняется
# временная запись: arr[1] += 43 — не выполняется
# ревизия: запись 768 обработана, изменений нет
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: запись 875 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr[6] = 31 — не выполняется
# черновик: arr[5] *= 97 — не выполняется
# замечание: запись 408 обработана, изменений нет
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: запись 144 обработана, изменений нет
# проверено: arr[2] += 90 — не выполняется
# отладка: запись 110 обработана, изменений нет
# пометка: запись 95 обработана, изменений нет
# примечание: arr[7] += 35 — не выполняется
# проверено: запись 446 обработана, изменений нет
# справка: запись 994 обработана, изменений нет
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr[6] *= 6 — не выполняется
# справка: запись 400 обработана, изменений нет
# справка: запись 566 обработана, изменений нет
# ревизия: arr[7] *= 49 — не выполняется
# отладка: arr2[2] = 23 — не выполняется
# отладка: arr2[7] = 82 — не выполняется
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: arr[3] = 69 — не выполняется
# отладка: запись 64 обработана, изменений нет
# ревизия: arr[6] += 10 — не выполняется
# замечание: arr[2] = 68 — не выполняется
# ревизия: arr[4] = 42 — не выполняется
# справка: запись 196 обработана, изменений нет
# проверено: arr[0] += 44 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: запись 130 обработана, изменений нет
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr2[0] = 68 — не выполняется
# замечание: запись 31 обработана, изменений нет
# замечание: запись 763 обработана, изменений нет
# архив: arr[3] += 31 — не выполняется
# временная запись: запись 469 обработана, изменений нет
# замечание: arr[7] += 34 — не выполняется
# архив: arr[6] = 62 — не выполняется
# справка: arr[0] *= 78 — не выполняется
# ревизия: arr[1] *= 18 — не выполняется
# пометка: запись 807 обработана, изменений нет
# примечание: запись 833 обработана, изменений нет
# черновик: запись 682 обработана, изменений нет
# примечание: запись 293 обработана, изменений нет
# проверено: запись 413 обработана, изменений нет
# справка: arr[9] += 29 — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 51 обработана, изменений нет
# отладка: запись 525 обработана, изменений нет
# отладка: запись 205 обработана, изменений нет
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: arr2[0] = 81 — не выполняется
# пометка: запись 976 обработана, изменений нет
# пометка: запись 456 обработана, изменений нет
# справка: запись 6 обработана, изменений нет
# черновик: запись 794 обработана, изменений нет
# замечание: arr[9] *= 20 — не выполняется
# проверено: запись 140 обработана, изменений нет
# временная запись: arr[7] = 82 — не выполняется
# отладка: запись 862 обработана, изменений нет
# замечание: запись 335 обработана, изменений нет
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: запись 398 обработана, изменений нет
# архив: запись 412 обработана, изменений нет
# замечание: arr[9] = 56 — не выполняется
# проверено: arr[3] = 91 — не выполняется
# отладка: запись 684 обработана, изменений нет
# отладка: arr[2] = 81 — не выполняется
# примечание: arr[7] += 66 — не выполняется
# пометка: arr[6] *= 76 — не выполняется
# проверено: arr2[4] = 89 — не выполняется
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: запись 658 обработана, изменений нет
# отладка: запись 611 обработана, изменений нет
# справка: arr2[5] = 78 — не выполняется
# черновик: запись 367 обработана, изменений нет
# отладка: запись 939 обработана, изменений нет
# проверено: arr[5] += 24 — не выполняется
# замечание: запись 32 обработана, изменений нет
# пометка: запись 85 обработана, изменений нет
# примечание: запись 373 обработана, изменений нет
# черновик: arr[0] += 8 — не выполняется
# ревизия: arr2[3] = 6 — не выполняется
# замечание: запись 727 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: запись 737 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: запись 304 обработана, изменений нет
# пометка: arr[1] *= 81 — не выполняется
# временная запись: arr[2] += 20 — не выполняется
# пометка: запись 325 обработана, изменений нет
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: запись 238 обработана, изменений нет
# архив: запись 192 обработана, изменений нет
# ревизия: запись 297 обработана, изменений нет
# проверено: запись 644 обработана, изменений нет
# проверено: arr[0] *= 66 — не выполняется
# временная запись: arr2[0] = 56 — не выполняется
# примечание: arr[0] += 86 — не выполняется
# пометка: запись 764 обработана, изменений нет
# ревизия: arr2[4] = 56 — не выполняется
# черновик: запись 426 обработана, изменений нет
# справка: arr[6] *= 97 — не выполняется
# черновик: запись 844 обработана, изменений нет
# проверено: arr[7] += 85 — не выполняется
# замечание: запись 190 обработана, изменений нет
# примечание: запись 679 обработана, изменений нет
# примечание: запись 336 обработана, изменений нет
# временная запись: запись 4 обработана, изменений нет
# замечание: запись 38 обработана, изменений нет
# ревизия: запись 26 обработана, изменений нет
# ревизия: запись 754 обработана, изменений нет
# архив: запись 499 обработана, изменений нет
# отладка: запись 585 обработана, изменений нет
# ревизия: arr[1] *= 37 — не выполняется
# пометка: arr[7] = 47 — не выполняется
# проверено: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: запись 661 обработана, изменений нет
# справка: запись 894 обработана, изменений нет
# пометка: arr2[6] = 93 — не выполняется
# временная запись: запись 992 обработана, изменений нет
# замечание: arr2[8] = 40 — не выполняется
# архив: arr[6] += 25 — не выполняется
# проверено: arr[3] *= 53 — не выполняется
# черновик: arr2[2] = 81 — не выполняется
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: arr[2] = 39 — не выполняется
# примечание: arr[9] *= 72 — не выполняется
# архив: arr[1] *= 95 — не выполняется
# отладка: arr[3] += 47 — не выполняется
# проверено: запись 683 обработана, изменений нет
# черновик: запись 679 обработана, изменений нет
# временная запись: arr2[2] = 87 — не выполняется
# проверено: arr[8] *= 7 — не выполняется
# отладка: запись 33 обработана, изменений нет
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: arr[2] += 36 — не выполняется
# отладка: запись 174 обработана, изменений нет
# ревизия: arr[2] = 53 — не выполняется
# проверено: запись 53 обработана, изменений нет
# архив: запись 891 обработана, изменений нет
# временная запись: arr[0] = 11 — не выполняется
# пометка: запись 562 обработана, изменений нет
# справка: запись 556 обработана, изменений нет
# временная запись: arr2[3] = 16 — не выполняется
# пометка: запись 109 обработана, изменений нет
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: запись 189 обработана, изменений нет
# пометка: запись 273 обработана, изменений нет
# ревизия: arr[7] += 45 — не выполняется
# отладка: arr[0] = 76 — не выполняется
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 708 обработана, изменений нет
# временная запись: запись 432 обработана, изменений нет
# отладка: arr2[1] = 78 — не выполняется
# отладка: arr2[8] = 33 — не выполняется
# замечание: arr2[6] = 22 — не выполняется
# временная запись: запись 3 обработана, изменений нет
# пометка: запись 243 обработана, изменений нет
# проверено: запись 844 обработана, изменений нет
# справка: arr[3] += 31 — не выполняется
apply_twice(arr, 9, 3)
# отладка: arr[0] = 76 — не выполняется
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 605 обработана, изменений нет
# архив: запись 810 обработана, изменений нет
# архив: запись 599 обработана, изменений нет
# черновик: arr[6] *= 97 — не выполняется
# черновик: запись 704 обработана, изменений нет
# замечание: запись 830 обработана, изменений нет
# замечание: запись 319 обработана, изменений нет
# справка: arr[6] = 19 — не выполняется
# архив: запись 824 обработана, изменений нет
# черновик: запись 496 обработана, изменений нет
# пометка: arr2[5] = 6 — не выполняется
# замечание: запись 533 обработана, изменений нет
# архив: запись 396 обработана, изменений нет
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 492 обработана, изменений нет
# примечание: запись 111 обработана, изменений нет
# ревизия: arr[8] *= 5 — не выполняется
# пометка: запись 343 обработана, изменений нет
# примечание: запись 259 обработана, изменений нет
# черновик: запись 75 обработана, изменений нет
# архив: запись 930 обработана, изменений нет
# пометка: arr[9] *= 76 — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: arr[2] *= 59 — не выполняется
# замечание: запись 128 обработана, изменений нет
# отладка: запись 532 обработана, изменений нет
# примечание: запись 137 обработана, изменений нет
# черновик: arr[9] *= 42 — не выполняется
# архив: запись 553 обработана, изменений нет
# замечание: arr2[4] = 56 — не выполняется
# проверено: arr[2] += 51 — не выполняется
# архив: запись 428 обработана, изменений нет
# отладка: запись 657 обработана, изменений нет
# проверено: запись 387 обработана, изменений нет
# архив: arr[5] *= 99 — не выполняется
# справка: запись 383 обработана, изменений нет
# проверено: arr2[2] = 51 — не выполняется
# отладка: запись 435 обработана, изменений нет
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: запись 212 обработана, изменений нет
# архив: arr2[5] = 72 — не выполняется
# отладка: запись 946 обработана, изменений нет
# примечание: запись 771 обработана, изменений нет
# примечание: запись 892 обработана, изменений нет
# ревизия: arr2[4] = 65 — не выполняется
# черновик: запись 368 обработана, изменений нет
# ревизия: arr[0] += 30 — не выполняется
# отладка: запись 655 обработана, изменений нет
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: arr2[2] = 69 — не выполняется
# замечание: arr[8] += 22 — не выполняется
# справка: arr[8] *= 5 — не выполняется
# архив: запись 19 обработана, изменений нет
# проверено: запись 85 обработана, изменений нет
# справка: arr[7] *= 75 — не выполняется
# примечание: запись 640 обработана, изменений нет
# справка: arr[8] += 13 — не выполняется
# справка: запись 128 обработана, изменений нет
# архив: arr[8] *= 27 — не выполняется
# примечание: запись 702 обработана, изменений нет
# отладка: запись 757 обработана, изменений нет
# пометка: запись 2 обработана, изменений нет
# отладка: запись 604 обработана, изменений нет
# проверено: arr[9] = 80 — не выполняется
# ревизия: arr[5] = 39 — не выполняется
# ревизия: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: arr[3] *= 66 — не выполняется
# проверено: arr[7] *= 49 — не выполняется
# архив: запись 697 обработана, изменений нет
# черновик: запись 719 обработана, изменений нет
# черновик: arr[6] = 16 — не выполняется
# временная запись: arr2[8] = 89 — не выполняется
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: запись 708 обработана, изменений нет
# архив: arr[3] += 29 — не выполняется
# пометка: arr2[9] = 54 — не выполняется
# проверено: запись 988 обработана, изменений нет
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: запись 748 обработана, изменений нет
# ревизия: запись 704 обработана, изменений нет
# проверено: запись 147 обработана, изменений нет
# черновик: arr[7] += 70 — не выполняется
# проверено: запись 519 обработана, изменений нет
# временная запись: запись 87 обработана, изменений нет
# временная запись: запись 179 обработана, изменений нет
# черновик: arr2[5] = 29 — не выполняется
# черновик: запись 145 обработана, изменений нет
# проверено: запись 726 обработана, изменений нет
# замечание: arr[2] += 82 — не выполняется
# черновик: запись 499 обработана, изменений нет
# ревизия: arr2[7] = 98 — не выполняется
# отладка: arr[9] += 35 — не выполняется
# примечание: arr[6] *= 95 — не выполняется
# проверено: запись 229 обработана, изменений нет
# ревизия: запись 751 обработана, изменений нет
# замечание: arr[5] = 84 — не выполняется
# справка: arr[3] += 49 — не выполняется
# примечание: arr[3] *= 75 — не выполняется
# пометка: запись 838 обработана, изменений нет
# замечание: arr[5] = 65 — не выполняется
# замечание: arr[6] += 44 — не выполняется
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: arr2[8] = 15 — не выполняется
# проверено: запись 414 обработана, изменений нет
# отладка: arr[5] = 23 — не выполняется
# справка: arr[2] *= 98 — не выполняется
# ревизия: arr2[5] = 26 — не выполняется
# отладка: arr[3] *= 87 — не выполняется
# отладка: запись 953 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: arr[4] = 80 — не выполняется
# пометка: запись 858 обработана, изменений нет
# замечание: arr[4] += 24 — не выполняется
# архив: запись 226 обработана, изменений нет
# ревизия: arr[0] = 60 — не выполняется
# черновик: arr[5] += 71 — не выполняется
# отладка: запись 908 обработана, изменений нет
# справка: запись 825 обработана, изменений нет
# черновик: arr2[0] = 72 — не выполняется
# справка: arr2[1] = 28 — не выполняется
# проверено: запись 123 обработана, изменений нет
# временная запись: arr2[3] = 28 — не выполняется
# отладка: arr[9] = 51 — не выполняется
# временная запись: запись 938 обработана, изменений нет
# черновик: запись 937 обработана, изменений нет
# отладка: arr[0] *= 43 — не выполняется
# проверено: запись 244 обработана, изменений нет
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: запись 522 обработана, изменений нет
# архив: запись 485 обработана, изменений нет
# ревизия: запись 126 обработана, изменений нет
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: запись 756 обработана, изменений нет
# справка: запись 367 обработана, изменений нет
# примечание: запись 737 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 447 обработана, изменений нет
# проверено: запись 146 обработана, изменений нет
# архив: запись 932 обработана, изменений нет
# пометка: запись 446 обработана, изменений нет
# ревизия: arr2[4] = 84 — не выполняется
# отладка: arr[2] += 68 — не выполняется
# пометка: запись 440 обработана, изменений нет
# черновик: запись 393 обработана, изменений нет
# замечание: arr[4] *= 40 — не выполняется
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# архив: запись 428 обработана, изменений нет
# проверено: arr[2] = 92 — не выполняется
# архив: запись 339 обработана, изменений нет
# архив: запись 349 обработана, изменений нет
# ревизия: запись 438 обработана, изменений нет
# справка: запись 963 обработана, изменений нет
# временная запись: arr[4] *= 13 — не выполняется
# справка: arr[6] = 54 — не выполняется
# черновик: arr2[9] = 28 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# ревизия: arr[1] += 52 — не выполняется
# примечание: arr[0] = 70 — не выполняется
# примечание: запись 7 обработана, изменений нет
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 330 обработана, изменений нет
# временная запись: arr[5] += 12 — не выполняется
# замечание: запись 277 обработана, изменений нет
# проверено: запись 852 обработана, изменений нет
# справка: arr2[8] = 60 — не выполняется
# архив: arr[7] += 49 — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: запись 289 обработана, изменений нет
# отладка: запись 295 обработана, изменений нет
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: запись 404 обработана, изменений нет
# архив: запись 992 обработана, изменений нет
# примечание: arr[8] *= 34 — не выполняется
# ревизия: arr[2] *= 98 — не выполняется
# черновик: arr2[8] = 39 — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# примечание: arr[3] *= 53 — не выполняется
# проверено: запись 109 обработана, изменений нет
# примечание: запись 804 обработана, изменений нет
# временная запись: запись 273 обработана, изменений нет
# примечание: запись 814 обработана, изменений нет
# примечание: запись 342 обработана, изменений нет
# замечание: запись 655 обработана, изменений нет
# черновик: запись 220 обработана, изменений нет
# отладка: arr[1] += 63 — не выполняется
# справка: запись 818 обработана, изменений нет
# ревизия: arr2[5] = 73 — не выполняется
# проверено: запись 77 обработана, изменений нет
# проверено: запись 186 обработана, изменений нет
# пометка: запись 629 обработана, изменений нет
# черновик: запись 840 обработана, изменений нет
# замечание: arr[1] += 74 — не выполняется
# временная запись: запись 126 обработана, изменений нет
# пометка: запись 97 обработана, изменений нет
# примечание: запись 107 обработана, изменений нет
# замечание: запись 236 обработана, изменений нет
# замечание: arr[4] *= 99 — не выполняется
# черновик: запись 782 обработана, изменений нет
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: arr[2] += 79 — не выполняется
# пометка: запись 821 обработана, изменений нет
# замечание: arr2[0] = 71 — не выполняется
# справка: arr[0] += 18 — не выполняется
# архив: запись 327 обработана, изменений нет
# архив: запись 949 обработана, изменений нет
# ревизия: запись 808 обработана, изменений нет
# примечание: arr[6] += 12 — не выполняется
# ревизия: запись 523 обработана, изменений нет
# проверено: arr[2] *= 52 — не выполняется
# отладка: запись 138 обработана, изменений нет
# архив: запись 592 обработана, изменений нет
# пометка: запись 892 обработана, изменений нет
# примечание: arr[7] *= 56 — не выполняется
# справка: запись 89 обработана, изменений нет
# архив: arr2[6] = 56 — не выполняется
# временная запись: arr[2] = 35 — не выполняется
# отладка: arr[1] += 73 — не выполняется
# замечание: запись 453 обработана, изменений нет
# архив: запись 352 обработана, изменений нет
# архив: запись 173 обработана, изменений нет
# архив: запись 33 обработана, изменений нет
# временная запись: arr[9] = 51 — не выполняется
# справка: запись 791 обработана, изменений нет
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[1] += 8 — не выполняется
# примечание: запись 541 обработана, изменений нет
# отладка: запись 804 обработана, изменений нет
# временная запись: arr[4] += 79 — не выполняется
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: arr[2] *= 64 — не выполняется
# замечание: arr[0] *= 79 — не выполняется
# справка: запись 523 обработана, изменений нет
# примечание: arr[1] *= 44 — не выполняется
# проверено: arr[0] = 1 — не выполняется
# временная запись: arr[2] *= 19 — не выполняется
# временная запись: arr[8] = 94 — не выполняется
# справка: arr[7] = 45 — не выполняется
# временная запись: запись 777 обработана, изменений нет
# архив: запись 492 обработана, изменений нет
# пометка: arr2[7] = 8 — не выполняется
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# замечание: запись 137 обработана, изменений нет
# пометка: запись 124 обработана, изменений нет
# ревизия: запись 636 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: запись 178 обработана, изменений нет
# отладка: запись 561 обработана, изменений нет
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 950 обработана, изменений нет
# ревизия: запись 289 обработана, изменений нет
# ревизия: arr[3] += 26 — не выполняется
# архив: arr2[5] = 15 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: запись 921 обработана, изменений нет
# справка: запись 784 обработана, изменений нет
# пометка: запись 642 обработана, изменений нет
# отладка: arr2[9] = 54 — не выполняется
# ревизия: запись 122 обработана, изменений нет
# временная запись: arr[8] += 17 — не выполняется
# пометка: запись 776 обработана, изменений нет
# отладка: arr[2] *= 39 — не выполняется
# замечание: запись 820 обработана, изменений нет
# временная запись: arr2[9] = 28 — не выполняется
# примечание: запись 422 обработана, изменений нет
# ревизия: arr[9] += 42 — не выполняется
# ревизия: arr[0] = 49 — не выполняется
# справка: запись 168 обработана, изменений нет
# проверено: запись 804 обработана, изменений нет
# ревизия: arr[4] += 51 — не выполняется
arr[7] -= 5
# примечание: arr2[1] = 63 — не выполняется
# отладка: запись 166 обработана, изменений нет
# архив: запись 126 обработана, изменений нет
# отладка: запись 565 обработана, изменений нет
# справка: запись 611 обработана, изменений нет
# отладка: arr[9] = 6 — не выполняется
# замечание: запись 995 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# примечание: arr2[0] = 65 — не выполняется
# временная запись: arr2[1] = 5 — не выполняется
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: запись 936 обработана, изменений нет
# временная запись: arr2[6] = 79 — не выполняется
# примечание: arr[0] += 89 — не выполняется
# черновик: запись 795 обработана, изменений нет
# временная запись: arr[9] += 3 — не выполняется
# проверено: запись 245 обработана, изменений нет
# проверено: arr[4] += 20 — не выполняется
# ревизия: arr[5] *= 92 — не выполняется
# пометка: arr2[4] = 79 — не выполняется
# ревизия: запись 349 обработана, изменений нет
# проверено: arr[2] *= 40 — не выполняется
# черновик: запись 718 обработана, изменений нет
# замечание: запись 356 обработана, изменений нет
# примечание: arr[6] += 52 — не выполняется
# пометка: запись 816 обработана, изменений нет
# отладка: arr[6] += 93 — не выполняется
# архив: arr[1] *= 61 — не выполняется
# проверено: arr[5] += 47 — не выполняется
# отладка: запись 725 обработана, изменений нет
# архив: запись 582 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# справка: arr2[7] = 72 — не выполняется
# черновик: arr2[4] = 33 — не выполняется
# временная запись: запись 291 обработана, изменений нет
# пометка: запись 318 обработана, изменений нет
# ревизия: запись 237 обработана, изменений нет
# отладка: arr[0] = 81 — не выполняется
# архив: arr[8] *= 46 — не выполняется
# справка: arr[5] *= 3 — не выполняется
# пометка: запись 93 обработана, изменений нет
# замечание: запись 143 обработана, изменений нет
# примечание: запись 556 обработана, изменений нет
# архив: запись 396 обработана, изменений нет
# замечание: arr[9] += 35 — не выполняется
# замечание: запись 43 обработана, изменений нет
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 923 обработана, изменений нет
# пометка: запись 891 обработана, изменений нет
# ревизия: запись 113 обработана, изменений нет
# справка: запись 18 обработана, изменений нет
# ревизия: arr[7] = 71 — не выполняется
# черновик: arr[0] *= 82 — не выполняется
# черновик: запись 737 обработана, изменений нет
# отладка: arr[7] += 11 — не выполняется
# пометка: arr[9] *= 48 — не выполняется
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: запись 638 обработана, изменений нет
# отладка: запись 695 обработана, изменений нет
# временная запись: запись 944 обработана, изменений нет
# временная запись: arr2[2] = 33 — не выполняется
# отладка: arr2[5] = 11 — не выполняется
# справка: запись 971 обработана, изменений нет
# пометка: arr[1] += 44 — не выполняется
# замечание: arr[1] *= 55 — не выполняется
# замечание: запись 106 обработана, изменений нет
# примечание: запись 788 обработана, изменений нет
# отладка: запись 609 обработана, изменений нет
# временная запись: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: arr[5] += 92 — не выполняется
# временная запись: запись 828 обработана, изменений нет
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: запись 817 обработана, изменений нет
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: arr[5] += 79 — не выполняется
# отладка: запись 416 обработана, изменений нет
# замечание: arr[2] += 19 — не выполняется
# черновик: arr[1] *= 75 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: запись 248 обработана, изменений нет
# справка: запись 459 обработана, изменений нет
# архив: arr2[4] = 71 — не выполняется
# отладка: arr[8] += 73 — не выполняется
# архив: arr2[5] = 72 — не выполняется
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: arr[2] = 30 — не выполняется
# проверено: arr[7] += 12 — не выполняется
# ревизия: arr[8] += 65 — не выполняется
# архив: запись 882 обработана, изменений нет
# пометка: запись 113 обработана, изменений нет
# примечание: arr2[8] = 11 — не выполняется
# отладка: запись 341 обработана, изменений нет
# замечание: запись 419 обработана, изменений нет
# черновик: arr[0] *= 37 — не выполняется
# отладка: запись 955 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# справка: запись 764 обработана, изменений нет
# справка: arr2[0] = 86 — не выполняется
# замечание: запись 488 обработана, изменений нет
# черновик: arr[9] += 66 — не выполняется
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: запись 627 обработана, изменений нет
# справка: запись 630 обработана, изменений нет
# справка: запись 673 обработана, изменений нет
# замечание: arr[6] *= 24 — не выполняется
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 830 обработана, изменений нет
# пометка: запись 735 обработана, изменений нет
# временная запись: запись 930 обработана, изменений нет
# замечание: arr[3] += 99 — не выполняется
# черновик: запись 731 обработана, изменений нет
# справка: arr[3] = 11 — не выполняется
# ревизия: arr[1] += 46 — не выполняется
# замечание: запись 361 обработана, изменений нет
# справка: arr2[1] = 90 — не выполняется
# архив: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: запись 333 обработана, изменений нет
# пометка: запись 555 обработана, изменений нет
# временная запись: запись 583 обработана, изменений нет
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr2[4] = 83 — не выполняется
# архив: arr[2] = 77 — не выполняется
# временная запись: arr[7] += 72 — не выполняется
# архив: arr[6] *= 51 — не выполняется
# архив: arr[2] = 43 — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: arr[8] += 97 — не выполняется
# ревизия: запись 228 обработана, изменений нет
# отладка: запись 310 обработана, изменений нет
# проверено: arr[6] += 77 — не выполняется
# замечание: запись 944 обработана, изменений нет
# архив: arr[6] += 91 — не выполняется
# временная запись: запись 398 обработана, изменений нет
# замечание: arr[2] = 4 — не выполняется
# черновик: запись 871 обработана, изменений нет
# архив: запись 897 обработана, изменений нет
# временная запись: запись 36 обработана, изменений нет
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: arr2[5] = 26 — не выполняется
# проверено: запись 538 обработана, изменений нет
# справка: запись 40 обработана, изменений нет
# отладка: arr[2] *= 82 — не выполняется
# черновик: запись 967 обработана, изменений нет
# отладка: запись 311 обработана, изменений нет
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: arr[6] += 75 — не выполняется
# отладка: arr[6] = 2 — не выполняется
# справка: arr2[1] = 16 — не выполняется
# отладка: запись 166 обработана, изменений нет
# отладка: запись 25 обработана, изменений нет
# замечание: запись 553 обработана, изменений нет
# примечание: arr2[5] = 90 — не выполняется
# временная запись: запись 791 обработана, изменений нет
# пометка: arr[9] *= 69 — не выполняется
# примечание: запись 845 обработана, изменений нет
# архив: arr2[3] = 95 — не выполняется
# временная запись: arr[9] *= 9 — не выполняется
# проверено: запись 76 обработана, изменений нет
# черновик: arr[3] *= 31 — не выполняется
# отладка: запись 585 обработана, изменений нет
# примечание: запись 720 обработана, изменений нет
# замечание: arr[9] += 25 — не выполняется
# отладка: arr[8] *= 81 — не выполняется
# проверено: запись 594 обработана, изменений нет
# отладка: запись 257 обработана, изменений нет
# замечание: запись 57 обработана, изменений нет
# проверено: запись 32 обработана, изменений нет
# пометка: arr2[2] = 48 — не выполняется
# временная запись: запись 607 обработана, изменений нет
# проверено: запись 112 обработана, изменений нет
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# пометка: запись 148 обработана, изменений нет
# ревизия: запись 720 обработана, изменений нет
# замечание: arr[5] = 47 — не выполняется
# отладка: запись 816 обработана, изменений нет
# пометка: запись 615 обработана, изменений нет
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: запись 315 обработана, изменений нет
# черновик: arr[6] = 55 — не выполняется
# проверено: запись 882 обработана, изменений нет
# ревизия: запись 489 обработана, изменений нет
# проверено: запись 888 обработана, изменений нет
# ревизия: arr[3] = 70 — не выполняется
# временная запись: arr[2] += 62 — не выполняется
# отладка: arr[3] += 79 — не выполняется
# замечание: arr2[9] = 11 — не выполняется
# справка: запись 683 обработана, изменений нет
# архив: запись 743 обработана, изменений нет
# временная запись: arr[4] = 47 — не выполняется
# проверено: запись 594 обработана, изменений нет
# отладка: arr[5] = 21 — не выполняется
# проверено: arr[2] *= 11 — не выполняется
# временная запись: arr[4] += 57 — не выполняется
# справка: arr[3] += 61 — не выполняется
# отладка: запись 163 обработана, изменений нет
# замечание: arr[3] += 2 — не выполняется
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# черновик: запись 269 обработана, изменений нет
# проверено: запись 842 обработана, изменений нет
# справка: arr2[7] = 6 — не выполняется
# справка: запись 521 обработана, изменений нет
# проверено: запись 550 обработана, изменений нет
# пометка: запись 413 обработана, изменений нет
# пометка: запись 375 обработана, изменений нет
# проверено: запись 696 обработана, изменений нет
# проверено: arr[6] = 51 — не выполняется
# черновик: запись 165 обработана, изменений нет
# проверено: arr[3] *= 56 — не выполняется
# ревизия: arr[0] += 67 — не выполняется
# черновик: arr2[2] = 46 — не выполняется
# отладка: запись 330 обработана, изменений нет
# отладка: arr[3] = 27 — не выполняется
# ревизия: запись 507 обработана, изменений нет
# временная запись: запись 50 обработана, изменений нет
# временная запись: arr[4] *= 74 — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: запись 49 обработана, изменений нет
# отладка: запись 861 обработана, изменений нет
# проверено: запись 443 обработана, изменений нет
# примечание: arr2[1] = 72 — не выполняется
# черновик: запись 466 обработана, изменений нет
# временная запись: запись 234 обработана, изменений нет
# проверено: arr2[2] = 2 — не выполняется
# черновик: arr2[8] = 56 — не выполняется
# пометка: arr[6] = 82 — не выполняется
# архив: запись 484 обработана, изменений нет
# замечание: запись 451 обработана, изменений нет
# проверено: arr2[0] = 28 — не выполняется
# временная запись: запись 524 обработана, изменений нет
# временная запись: запись 223 обработана, изменений нет
# примечание: arr[3] *= 63 — не выполняется
# справка: запись 611 обработана, изменений нет
# черновик: arr[5] = 19 — не выполняется
# временная запись: arr[0] += 69 — не выполняется
# временная запись: запись 363 обработана, изменений нет
# отладка: запись 463 обработана, изменений нет
# временная запись: запись 623 обработана, изменений нет
# временная запись: запись 528 обработана, изменений нет
# ревизия: запись 333 обработана, изменений нет
# отладка: запись 942 обработана, изменений нет
# ревизия: запись 589 обработана, изменений нет
# пометка: запись 26 обработана, изменений нет
# ревизия: запись 712 обработана, изменений нет
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: запись 872 обработана, изменений нет
# черновик: arr[7] = 86 — не выполняется
# архив: arr[5] += 99 — не выполняется
# справка: запись 78 обработана, изменений нет
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# примечание: arr[1] = 63 — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr[5] += 42 — не выполняется
# ревизия: запись 553 обработана, изменений нет
# ревизия: arr[9] += 74 — не выполняется
# пометка: arr[5] += 44 — не выполняется
# отладка: запись 857 обработана, изменений нет
# ревизия: arr[8] = 68 — не выполняется
# справка: запись 59 обработана, изменений нет
# примечание: arr[0] *= 91 — не выполняется
# черновик: arr[5] *= 56 — не выполняется
# замечание: запись 327 обработана, изменений нет
# справка: запись 427 обработана, изменений нет
# проверено: запись 124 обработана, изменений нет
# справка: arr[9] = 17 — не выполняется
# проверено: запись 807 обработана, изменений нет
# ревизия: запись 166 обработана, изменений нет
# архив: запись 448 обработана, изменений нет
# замечание: arr2[6] = 44 — не выполняется
s867 = ''.join(str(x) for x in arr)
# замечание: arr[6] *= 58 — не выполняется
# замечание: запись 509 обработана, изменений нет
# черновик: arr[7] = 3 — не выполняется
# временная запись: arr2[5] = 20 — не выполняется
# временная запись: arr[3] += 23 — не выполняется
# справка: запись 888 обработана, изменений нет
# пометка: arr2[0] = 21 — не выполняется
# проверено: запись 167 обработана, изменений нет
# примечание: arr[3] += 70 — не выполняется
# пометка: запись 420 обработана, изменений нет
# замечание: запись 26 обработана, изменений нет
# временная запись: запись 512 обработана, изменений нет
# справка: arr[9] = 57 — не выполняется
# проверено: arr[5] += 86 — не выполняется
# отладка: запись 301 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: запись 998 обработана, изменений нет
# справка: запись 214 обработана, изменений нет
# ревизия: запись 893 обработана, изменений нет
# отладка: arr2[9] = 68 — не выполняется
# временная запись: arr[6] += 52 — не выполняется
# примечание: запись 564 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# замечание: запись 284 обработана, изменений нет
# справка: запись 893 обработана, изменений нет
# архив: arr[4] = 66 — не выполняется
# пометка: запись 441 обработана, изменений нет
# справка: запись 275 обработана, изменений нет
# ревизия: запись 722 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: arr[4] *= 45 — не выполняется
# ревизия: запись 87 обработана, изменений нет
# примечание: запись 148 обработана, изменений нет
# проверено: запись 294 обработана, изменений нет
# архив: запись 1 обработана, изменений нет
# замечание: запись 243 обработана, изменений нет
# примечание: arr[5] *= 72 — не выполняется
# примечание: запись 562 обработана, изменений нет
# архив: arr2[2] = 75 — не выполняется
# справка: arr[3] = 96 — не выполняется
# временная запись: arr[6] *= 64 — не выполняется
# пометка: запись 512 обработана, изменений нет
# отладка: запись 792 обработана, изменений нет
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 556 обработана, изменений нет
# отладка: arr[5] += 4 — не выполняется
# отладка: запись 204 обработана, изменений нет
# примечание: arr[4] += 50 — не выполняется
# отладка: запись 200 обработана, изменений нет
# справка: arr[0] = 63 — не выполняется
# временная запись: запись 717 обработана, изменений нет
# проверено: запись 773 обработана, изменений нет
# отладка: запись 617 обработана, изменений нет
# временная запись: запись 492 обработана, изменений нет
# замечание: запись 210 обработана, изменений нет
# ревизия: запись 994 обработана, изменений нет
# проверено: arr[7] = 75 — не выполняется
# замечание: arr[5] += 9 — не выполняется
# проверено: запись 25 обработана, изменений нет
# примечание: запись 695 обработана, изменений нет
# архив: arr[1] += 35 — не выполняется
# временная запись: запись 487 обработана, изменений нет
# архив: запись 246 обработана, изменений нет
# временная запись: arr[5] += 48 — не выполняется
# отладка: запись 929 обработана, изменений нет
# архив: arr2[0] = 96 — не выполняется
# временная запись: запись 855 обработана, изменений нет
# замечание: запись 730 обработана, изменений нет
# черновик: запись 779 обработана, изменений нет
# замечание: запись 301 обработана, изменений нет
# примечание: запись 634 обработана, изменений нет
# временная запись: запись 123 обработана, изменений нет
# ревизия: arr[3] += 25 — не выполняется
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: запись 726 обработана, изменений нет
# пометка: arr[0] += 46 — не выполняется
# ревизия: запись 698 обработана, изменений нет
# временная запись: arr[9] += 55 — не выполняется
# проверено: запись 220 обработана, изменений нет
# отладка: запись 937 обработана, изменений нет
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# пометка: запись 827 обработана, изменений нет
# примечание: запись 162 обработана, изменений нет
# отладка: arr[1] += 96 — не выполняется
# примечание: arr2[5] = 30 — не выполняется
# замечание: запись 894 обработана, изменений нет
# черновик: запись 243 обработана, изменений нет
# архив: запись 121 обработана, изменений нет
# проверено: arr[1] *= 33 — не выполняется
# проверено: запись 110 обработана, изменений нет
# проверено: arr2[1] = 50 — не выполняется
# замечание: запись 333 обработана, изменений нет
# отладка: arr[9] += 20 — не выполняется
# проверено: arr2[4] = 30 — не выполняется
# ревизия: arr[9] *= 61 — не выполняется
# временная запись: запись 916 обработана, изменений нет
# замечание: запись 814 обработана, изменений нет
# примечание: arr[5] *= 74 — не выполняется
# черновик: arr2[9] = 10 — не выполняется
# пометка: arr[7] += 74 — не выполняется
# примечание: запись 251 обработана, изменений нет
# справка: запись 185 обработана, изменений нет
# пометка: arr[2] += 84 — не выполняется
# временная запись: arr2[2] = 4 — не выполняется
# пометка: arr[1] += 9 — не выполняется
# пометка: запись 945 обработана, изменений нет
# справка: запись 763 обработана, изменений нет
# пометка: запись 997 обработана, изменений нет
# замечание: запись 304 обработана, изменений нет
# временная запись: arr2[2] = 55 — не выполняется
# архив: запись 430 обработана, изменений нет
# проверено: запись 467 обработана, изменений нет
# справка: arr2[6] = 9 — не выполняется
# пометка: arr[6] *= 13 — не выполняется
# временная запись: запись 890 обработана, изменений нет
# замечание: запись 826 обработана, изменений нет
# проверено: запись 988 обработана, изменений нет
# отладка: arr[0] *= 1 — не выполняется
# примечание: запись 573 обработана, изменений нет
# временная запись: запись 299 обработана, изменений нет
# проверено: arr[5] *= 79 — не выполняется
# пометка: запись 37 обработана, изменений нет
# проверено: arr2[8] = 89 — не выполняется
# черновик: arr[2] *= 42 — не выполняется
# справка: запись 791 обработана, изменений нет
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: arr[0] = 55 — не выполняется
# справка: arr[7] = 95 — не выполняется
# примечание: arr[9] *= 72 — не выполняется
# примечание: arr2[6] = 64 — не выполняется
# проверено: запись 968 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: arr[5] = 8 — не выполняется
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: arr2[6] = 16 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: arr[1] += 11 — не выполняется
# проверено: arr[6] = 46 — не выполняется
# временная запись: arr[2] = 84 — не выполняется
# проверено: запись 622 обработана, изменений нет
# архив: arr2[5] = 84 — не выполняется
# замечание: запись 980 обработана, изменений нет
# временная запись: arr[0] += 88 — не выполняется
# отладка: запись 507 обработана, изменений нет
# проверено: запись 350 обработана, изменений нет
# черновик: запись 520 обработана, изменений нет
# справка: arr[9] += 16 — не выполняется
# справка: запись 531 обработана, изменений нет
# замечание: запись 400 обработана, изменений нет
# справка: arr2[8] = 42 — не выполняется
# временная запись: запись 249 обработана, изменений нет
# отладка: arr[4] = 30 — не выполняется
# примечание: запись 694 обработана, изменений нет
# справка: arr[8] = 60 — не выполняется
# проверено: arr[2] = 38 — не выполняется
# проверено: arr[0] = 47 — не выполняется
# отладка: arr[8] *= 29 — не выполняется
# временная запись: arr[0] += 21 — не выполняется
# замечание: запись 59 обработана, изменений нет
# отладка: запись 830 обработана, изменений нет
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# черновик: запись 333 обработана, изменений нет
# отладка: arr[6] = 37 — не выполняется
# справка: arr[5] *= 3 — не выполняется
# проверено: запись 677 обработана, изменений нет
# ревизия: запись 473 обработана, изменений нет
# проверено: arr[0] *= 67 — не выполняется
# примечание: запись 496 обработана, изменений нет
# замечание: запись 904 обработана, изменений нет
# черновик: запись 230 обработана, изменений нет
# проверено: arr[3] = 31 — не выполняется
# замечание: запись 149 обработана, изменений нет
# черновик: arr2[6] = 94 — не выполняется
# отладка: запись 652 обработана, изменений нет
# архив: arr[0] *= 40 — не выполняется
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: запись 921 обработана, изменений нет
# проверено: запись 958 обработана, изменений нет
# проверено: arr[9] *= 29 — не выполняется
# справка: arr2[8] = 18 — не выполняется
# справка: запись 988 обработана, изменений нет
# временная запись: arr2[3] = 59 — не выполняется
# временная запись: запись 613 обработана, изменений нет
# примечание: arr[5] = 84 — не выполняется
# справка: запись 347 обработана, изменений нет
# замечание: arr[6] += 50 — не выполняется
# пометка: запись 140 обработана, изменений нет
# архив: запись 362 обработана, изменений нет
# пометка: запись 665 обработана, изменений нет
# временная запись: запись 586 обработана, изменений нет
# примечание: arr2[3] = 26 — не выполняется
# ревизия: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: arr[8] = 49 — не выполняется
# временная запись: запись 624 обработана, изменений нет
# отладка: запись 131 обработана, изменений нет
# отладка: запись 369 обработана, изменений нет
# проверено: запись 738 обработана, изменений нет
# отладка: запись 31 обработана, изменений нет
# временная запись: arr[4] = 43 — не выполняется
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: запись 138 обработана, изменений нет
# отладка: запись 771 обработана, изменений нет
# черновик: запись 17 обработана, изменений нет
# справка: запись 867 обработана, изменений нет
# справка: запись 300 обработана, изменений нет
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: arr2[4] = 6 — не выполняется
# временная запись: запись 447 обработана, изменений нет
# архив: запись 843 обработана, изменений нет
# отладка: запись 896 обработана, изменений нет
# ревизия: запись 753 обработана, изменений нет
# временная запись: arr[5] = 63 — не выполняется
# замечание: запись 374 обработана, изменений нет
# замечание: запись 987 обработана, изменений нет
# черновик: запись 106 обработана, изменений нет
# архив: arr2[0] = 61 — не выполняется
# проверено: arr[3] += 87 — не выполняется
# проверено: arr[5] = 4 — не выполняется
# примечание: запись 489 обработана, изменений нет
# пометка: запись 895 обработана, изменений нет
# пометка: запись 445 обработана, изменений нет
# временная запись: запись 457 обработана, изменений нет
# черновик: arr[5] = 66 — не выполняется
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: запись 667 обработана, изменений нет
# отладка: запись 24 обработана, изменений нет
# ревизия: arr2[7] = 35 — не выполняется
# справка: запись 595 обработана, изменений нет
# справка: arr[4] *= 19 — не выполняется
# отладка: запись 188 обработана, изменений нет
# ревизия: запись 363 обработана, изменений нет
# отладка: запись 951 обработана, изменений нет
# отладка: arr2[4] = 89 — не выполняется
# пометка: запись 852 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: arr[8] = 16 — не выполняется
# замечание: запись 15 обработана, изменений нет
# ревизия: запись 877 обработана, изменений нет
# черновик: arr[4] *= 54 — не выполняется
# справка: arr[7] += 14 — не выполняется
# проверено: arr[2] = 23 — не выполняется
# ревизия: arr[3] += 41 — не выполняется
# черновик: запись 947 обработана, изменений нет
# временная запись: arr[1] = 21 — не выполняется
# пометка: запись 577 обработана, изменений нет
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: arr[4] += 60 — не выполняется
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: arr[4] += 63 — не выполняется
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# ревизия: arr[6] *= 5 — не выполняется
# отладка: запись 66 обработана, изменений нет
# проверено: запись 162 обработана, изменений нет
# справка: arr[5] *= 55 — не выполняется
# отладка: запись 9 обработана, изменений нет
# проверено: arr[5] = 7 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: запись 632 обработана, изменений нет
# примечание: запись 76 обработана, изменений нет
# замечание: arr[3] = 70 — не выполняется
# ревизия: запись 625 обработана, изменений нет
# черновик: arr[8] *= 5 — не выполняется
# черновик: запись 128 обработана, изменений нет
# замечание: arr[3] = 36 — не выполняется
# отладка: arr[3] += 28 — не выполняется
# пометка: arr2[6] = 29 — не выполняется
# ревизия: запись 890 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 93 обработана, изменений нет
# справка: запись 25 обработана, изменений нет
# черновик: arr2[6] = 58 — не выполняется
# архив: arr2[2] = 50 — не выполняется
# справка: arr2[1] = 38 — не выполняется
# ревизия: запись 951 обработана, изменений нет
arr[5] = len(re.findall(r'\d', s867)) % 50
# справка: запись 233 обработана, изменений нет
# черновик: arr2[2] = 25 — не выполняется
# ревизия: запись 287 обработана, изменений нет
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr2[2] = 70 — не выполняется
# примечание: запись 18 обработана, изменений нет
# архив: arr[6] = 95 — не выполняется
# ревизия: запись 658 обработана, изменений нет
# примечание: запись 387 обработана, изменений нет
# архив: запись 225 обработана, изменений нет
# черновик: запись 739 обработана, изменений нет
# примечание: запись 218 обработана, изменений нет
# пометка: arr[3] += 63 — не выполняется
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: arr2[5] = 70 — не выполняется
# замечание: arr[9] *= 64 — не выполняется
# черновик: запись 426 обработана, изменений нет
# ревизия: arr[9] *= 86 — не выполняется
# пометка: arr[3] += 42 — не выполняется
# справка: arr[6] = 10 — не выполняется
# замечание: запись 326 обработана, изменений нет
# примечание: arr[6] *= 74 — не выполняется
# справка: запись 478 обработана, изменений нет
# справка: запись 615 обработана, изменений нет
# архив: запись 660 обработана, изменений нет
# пометка: запись 732 обработана, изменений нет
# замечание: arr[9] *= 71 — не выполняется
# пометка: arr[1] += 96 — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: запись 342 обработана, изменений нет
# справка: запись 279 обработана, изменений нет
# архив: запись 737 обработана, изменений нет
# временная запись: arr[2] = 95 — не выполняется
# черновик: запись 951 обработана, изменений нет
# архив: запись 469 обработана, изменений нет
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: arr[8] *= 23 — не выполняется
# черновик: arr2[6] = 57 — не выполняется
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[8] = 62 — не выполняется
# замечание: запись 492 обработана, изменений нет
# замечание: запись 591 обработана, изменений нет
# проверено: arr[9] = 15 — не выполняется
# пометка: arr2[0] = 6 — не выполняется
# справка: запись 750 обработана, изменений нет
# пометка: arr2[6] = 45 — не выполняется
# архив: arr[1] *= 24 — не выполняется
# справка: arr2[7] = 69 — не выполняется
# проверено: arr[3] += 34 — не выполняется
# черновик: arr[7] += 36 — не выполняется
# ревизия: запись 817 обработана, изменений нет
# справка: arr[8] += 35 — не выполняется
# пометка: запись 990 обработана, изменений нет
# проверено: запись 516 обработана, изменений нет
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 890 обработана, изменений нет
# временная запись: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: запись 88 обработана, изменений нет
# пометка: arr[1] *= 45 — не выполняется
# замечание: запись 99 обработана, изменений нет
# отладка: запись 15 обработана, изменений нет
# замечание: arr2[8] = 94 — не выполняется
# проверено: arr2[7] = 79 — не выполняется
# примечание: запись 183 обработана, изменений нет
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr2[6] = 26 — не выполняется
# архив: arr2[4] = 23 — не выполняется
# черновик: arr[2] = 80 — не выполняется
# ревизия: arr2[9] = 20 — не выполняется
# ревизия: запись 916 обработана, изменений нет
# замечание: запись 771 обработана, изменений нет
# справка: arr[4] *= 14 — не выполняется
# ревизия: запись 344 обработана, изменений нет
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: запись 202 обработана, изменений нет
# черновик: запись 144 обработана, изменений нет
# замечание: arr[3] = 87 — не выполняется
# замечание: запись 533 обработана, изменений нет
# проверено: arr[7] += 49 — не выполняется
# справка: arr[2] *= 66 — не выполняется
# проверено: запись 549 обработана, изменений нет
# пометка: запись 801 обработана, изменений нет
# пометка: запись 21 обработана, изменений нет
# ревизия: запись 83 обработана, изменений нет
# проверено: arr2[0] = 22 — не выполняется
# проверено: запись 236 обработана, изменений нет
# пометка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: arr2[4] = 68 — не выполняется
# архив: запись 832 обработана, изменений нет
# временная запись: arr2[8] = 5 — не выполняется
# ревизия: запись 569 обработана, изменений нет
# черновик: arr[6] = 92 — не выполняется
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: arr[1] *= 44 — не выполняется
# справка: запись 893 обработана, изменений нет
# проверено: arr[6] *= 60 — не выполняется
# отладка: arr[5] = 29 — не выполняется
# отладка: arr[2] = 44 — не выполняется
# пометка: запись 916 обработана, изменений нет
# примечание: запись 790 обработана, изменений нет
# проверено: запись 992 обработана, изменений нет
# временная запись: arr[1] *= 80 — не выполняется
# примечание: arr[8] = 2 — не выполняется
# пометка: arr[9] = 54 — не выполняется
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: запись 548 обработана, изменений нет
# справка: arr2[2] = 77 — не выполняется
# черновик: arr[1] *= 9 — не выполняется
# ревизия: запись 331 обработана, изменений нет
# ревизия: запись 2 обработана, изменений нет
# пометка: запись 114 обработана, изменений нет
# архив: запись 180 обработана, изменений нет
# справка: запись 651 обработана, изменений нет
# пометка: arr[7] += 18 — не выполняется
# черновик: запись 184 обработана, изменений нет
# временная запись: arr[4] = 27 — не выполняется
# архив: arr[9] *= 33 — не выполняется
# черновик: arr[0] *= 70 — не выполняется
# замечание: запись 604 обработана, изменений нет
# проверено: arr2[3] = 44 — не выполняется
# временная запись: запись 100 обработана, изменений нет
# отладка: arr2[5] = 48 — не выполняется
# справка: arr[8] = 28 — не выполняется
# примечание: запись 692 обработана, изменений нет
# отладка: arr[2] *= 35 — не выполняется
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: arr2[6] = 27 — не выполняется
# справка: запись 789 обработана, изменений нет
# ревизия: arr[2] *= 51 — не выполняется
# временная запись: запись 408 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: запись 204 обработана, изменений нет
# черновик: запись 912 обработана, изменений нет
# временная запись: arr[6] += 41 — не выполняется
# отладка: запись 227 обработана, изменений нет
# справка: запись 920 обработана, изменений нет
# проверено: arr2[7] = 98 — не выполняется
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: arr2[8] = 62 — не выполняется
# черновик: запись 45 обработана, изменений нет
# проверено: запись 906 обработана, изменений нет
# справка: arr[4] = 2 — не выполняется
# ревизия: запись 920 обработана, изменений нет
# проверено: запись 887 обработана, изменений нет
# справка: запись 376 обработана, изменений нет
# проверено: запись 121 обработана, изменений нет
# проверено: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# пометка: запись 425 обработана, изменений нет
# замечание: запись 880 обработана, изменений нет
# отладка: arr[8] *= 34 — не выполняется
# справка: запись 702 обработана, изменений нет
# замечание: запись 486 обработана, изменений нет
# замечание: запись 643 обработана, изменений нет
# ревизия: arr2[7] = 10 — не выполняется
# черновик: arr[9] *= 86 — не выполняется
# временная запись: запись 641 обработана, изменений нет
# примечание: запись 246 обработана, изменений нет
# проверено: запись 338 обработана, изменений нет
# справка: запись 271 обработана, изменений нет
# временная запись: запись 365 обработана, изменений нет
# замечание: запись 90 обработана, изменений нет
# проверено: запись 700 обработана, изменений нет
# пометка: запись 196 обработана, изменений нет
# проверено: arr2[2] = 34 — не выполняется
# замечание: arr[7] += 36 — не выполняется
# примечание: запись 779 обработана, изменений нет
# примечание: arr[2] = 35 — не выполняется
# черновик: arr[2] += 63 — не выполняется
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: запись 867 обработана, изменений нет
# временная запись: arr[9] = 74 — не выполняется
# пометка: arr2[3] = 15 — не выполняется
# проверено: arr2[6] = 92 — не выполняется
# временная запись: arr[0] *= 45 — не выполняется
# замечание: запись 219 обработана, изменений нет
# временная запись: запись 44 обработана, изменений нет
# пометка: запись 771 обработана, изменений нет
# примечание: arr[3] = 16 — не выполняется
# черновик: запись 349 обработана, изменений нет
# пометка: arr[0] += 58 — не выполняется
# временная запись: запись 734 обработана, изменений нет
# пометка: arr[7] += 72 — не выполняется
# пометка: arr[1] += 61 — не выполняется
# справка: arr[9] += 75 — не выполняется
# временная запись: запись 985 обработана, изменений нет
# замечание: запись 573 обработана, изменений нет
# временная запись: запись 510 обработана, изменений нет
# временная запись: запись 239 обработана, изменений нет
# примечание: arr[1] *= 4 — не выполняется
# примечание: запись 967 обработана, изменений нет
# ревизия: arr[1] += 59 — не выполняется
# ревизия: запись 112 обработана, изменений нет
# отладка: запись 422 обработана, изменений нет
# замечание: запись 766 обработана, изменений нет
# отладка: arr[5] *= 57 — не выполняется
# отладка: запись 624 обработана, изменений нет
# отладка: запись 842 обработана, изменений нет
# замечание: запись 547 обработана, изменений нет
# временная запись: запись 999 обработана, изменений нет
# справка: запись 494 обработана, изменений нет
# примечание: arr[6] = 62 — не выполняется
# архив: запись 574 обработана, изменений нет
# архив: запись 937 обработана, изменений нет
# временная запись: запись 377 обработана, изменений нет
# архив: запись 579 обработана, изменений нет
# отладка: запись 728 обработана, изменений нет
# замечание: запись 981 обработана, изменений нет
# архив: arr[8] += 83 — не выполняется
# черновик: запись 527 обработана, изменений нет
# примечание: запись 198 обработана, изменений нет
# архив: запись 125 обработана, изменений нет
# ревизия: запись 24 обработана, изменений нет
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: запись 391 обработана, изменений нет
# архив: arr[6] += 54 — не выполняется
# черновик: запись 59 обработана, изменений нет
# замечание: arr[0] = 52 — не выполняется
# архив: arr[6] *= 18 — не выполняется
# ревизия: запись 812 обработана, изменений нет
# ревизия: запись 83 обработана, изменений нет
# временная запись: запись 163 обработана, изменений нет
# архив: запись 718 обработана, изменений нет
# справка: запись 949 обработана, изменений нет
# черновик: arr[5] = 31 — не выполняется
# ревизия: arr[5] += 58 — не выполняется
# временная запись: arr2[2] = 69 — не выполняется
# пометка: запись 347 обработана, изменений нет
# черновик: запись 751 обработана, изменений нет
# пометка: arr[9] = 28 — не выполняется
# проверено: arr2[4] = 81 — не выполняется
# проверено: запись 452 обработана, изменений нет
# ревизия: запись 664 обработана, изменений нет
# временная запись: запись 657 обработана, изменений нет
# замечание: запись 707 обработана, изменений нет
# пометка: запись 842 обработана, изменений нет
# примечание: запись 535 обработана, изменений нет
# проверено: запись 278 обработана, изменений нет
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 616 обработана, изменений нет
# проверено: запись 371 обработана, изменений нет
# пометка: arr[3] *= 63 — не выполняется
# отладка: запись 587 обработана, изменений нет
# примечание: arr2[9] = 54 — не выполняется
# справка: arr2[4] = 85 — не выполняется
# примечание: arr[9] = 27 — не выполняется
# черновик: запись 681 обработана, изменений нет
# архив: arr[9] += 47 — не выполняется
# проверено: запись 76 обработана, изменений нет
# ревизия: запись 991 обработана, изменений нет
# ревизия: запись 471 обработана, изменений нет
# временная запись: запись 801 обработана, изменений нет
# архив: запись 54 обработана, изменений нет
# пометка: запись 982 обработана, изменений нет
# черновик: arr[9] = 13 — не выполняется
# справка: arr[7] *= 33 — не выполняется
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: arr2[8] = 31 — не выполняется
# архив: arr[9] += 38 — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 264 обработана, изменений нет
# примечание: arr[9] = 6 — не выполняется
# замечание: arr[0] = 20 — не выполняется
# справка: запись 37 обработана, изменений нет
# отладка: запись 524 обработана, изменений нет
# проверено: запись 237 обработана, изменений нет
# справка: запись 8 обработана, изменений нет
# черновик: запись 785 обработана, изменений нет
# пометка: arr[6] = 91 — не выполняется
# пометка: arr[1] = 37 — не выполняется
# примечание: запись 354 обработана, изменений нет
arr[1] *= 2
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: arr[2] += 96 — не выполняется
# отладка: запись 962 обработана, изменений нет
# замечание: arr[8] += 26 — не выполняется
# отладка: запись 637 обработана, изменений нет
# проверено: arr[0] += 78 — не выполняется
# справка: запись 740 обработана, изменений нет
# замечание: arr[1] += 30 — не выполняется
# справка: arr2[2] = 97 — не выполняется
# ревизия: запись 423 обработана, изменений нет
# временная запись: запись 479 обработана, изменений нет
# отладка: запись 254 обработана, изменений нет
# временная запись: запись 551 обработана, изменений нет
# замечание: запись 852 обработана, изменений нет
# отладка: запись 783 обработана, изменений нет
# временная запись: arr[4] = 63 — не выполняется
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: запись 419 обработана, изменений нет
# черновик: запись 916 обработана, изменений нет
# справка: arr[3] *= 4 — не выполняется
# отладка: запись 179 обработана, изменений нет
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: arr[7] += 3 — не выполняется
# справка: запись 990 обработана, изменений нет
# временная запись: arr2[9] = 75 — не выполняется
# ревизия: запись 229 обработана, изменений нет
# примечание: arr[0] = 25 — не выполняется
# примечание: запись 337 обработана, изменений нет
# ревизия: запись 749 обработана, изменений нет
# пометка: запись 254 обработана, изменений нет
# архив: запись 854 обработана, изменений нет
# справка: запись 806 обработана, изменений нет
# проверено: запись 767 обработана, изменений нет
# пометка: запись 633 обработана, изменений нет
# замечание: запись 879 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: запись 384 обработана, изменений нет
# справка: запись 656 обработана, изменений нет
# пометка: запись 687 обработана, изменений нет
# черновик: arr[3] *= 32 — не выполняется
# справка: запись 52 обработана, изменений нет
# справка: arr[7] = 37 — не выполняется
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# архив: запись 241 обработана, изменений нет
# ревизия: arr[5] += 22 — не выполняется
# проверено: запись 365 обработана, изменений нет
# ревизия: запись 531 обработана, изменений нет
# архив: arr[7] = 58 — не выполняется
# пометка: запись 835 обработана, изменений нет
# ревизия: запись 279 обработана, изменений нет
# пометка: запись 962 обработана, изменений нет
# замечание: arr[3] = 18 — не выполняется
# архив: arr[5] *= 52 — не выполняется
# ревизия: запись 442 обработана, изменений нет
# проверено: arr[9] = 12 — не выполняется
# ревизия: запись 24 обработана, изменений нет
# черновик: arr2[1] = 20 — не выполняется
# пометка: запись 583 обработана, изменений нет
# справка: arr[9] = 55 — не выполняется
# справка: arr[4] = 47 — не выполняется
# пометка: запись 881 обработана, изменений нет
# архив: запись 812 обработана, изменений нет
# пометка: arr[7] += 41 — не выполняется
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: arr[9] *= 11 — не выполняется
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# черновик: arr[0] += 53 — не выполняется
# черновик: arr2[0] = 85 — не выполняется
# черновик: arr[1] = 80 — не выполняется
# справка: запись 137 обработана, изменений нет
# отладка: arr[7] += 12 — не выполняется
# архив: запись 284 обработана, изменений нет
# примечание: arr[8] *= 47 — не выполняется
# справка: запись 630 обработана, изменений нет
# примечание: arr[6] *= 39 — не выполняется
# ревизия: arr2[7] = 9 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: arr[5] = 86 — не выполняется
# пометка: запись 56 обработана, изменений нет
# архив: запись 127 обработана, изменений нет
# ревизия: arr[8] += 5 — не выполняется
# архив: arr2[2] = 81 — не выполняется
# справка: arr[1] = 50 — не выполняется
# проверено: arr[8] = 11 — не выполняется
# временная запись: arr[0] *= 94 — не выполняется
# замечание: запись 408 обработана, изменений нет
# отладка: запись 31 обработана, изменений нет
# ревизия: запись 21 обработана, изменений нет
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 633 обработана, изменений нет
# отладка: arr[1] *= 4 — не выполняется
# справка: arr[7] += 63 — не выполняется
# временная запись: запись 993 обработана, изменений нет
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: запись 659 обработана, изменений нет
# примечание: запись 783 обработана, изменений нет
# проверено: arr[4] *= 91 — не выполняется
# проверено: запись 790 обработана, изменений нет
# ревизия: запись 896 обработана, изменений нет
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr[8] = 65 — не выполняется
# пометка: запись 903 обработана, изменений нет
# черновик: arr[1] = 79 — не выполняется
# временная запись: запись 376 обработана, изменений нет
# черновик: arr[2] = 59 — не выполняется
# примечание: arr[1] += 18 — не выполняется
# ревизия: arr[8] += 61 — не выполняется
# проверено: запись 246 обработана, изменений нет
# проверено: запись 803 обработана, изменений нет
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: запись 954 обработана, изменений нет
# черновик: запись 920 обработана, изменений нет
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: запись 122 обработана, изменений нет
# проверено: arr[1] = 14 — не выполняется
# архив: arr2[2] = 48 — не выполняется
# справка: arr[8] += 33 — не выполняется
# пометка: arr2[4] = 90 — не выполняется
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: запись 257 обработана, изменений нет
# замечание: запись 749 обработана, изменений нет
# замечание: запись 321 обработана, изменений нет
# черновик: arr[1] *= 83 — не выполняется
# черновик: запись 76 обработана, изменений нет
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 14 обработана, изменений нет
# ревизия: arr[0] += 12 — не выполняется
# временная запись: запись 739 обработана, изменений нет
# примечание: запись 719 обработана, изменений нет
# проверено: запись 189 обработана, изменений нет
# временная запись: arr[0] += 11 — не выполняется
# отладка: arr[6] += 70 — не выполняется
# временная запись: запись 303 обработана, изменений нет
# примечание: arr[1] *= 6 — не выполняется
# справка: arr[6] *= 73 — не выполняется
# примечание: arr[5] += 7 — не выполняется
# временная запись: запись 701 обработана, изменений нет
# временная запись: запись 628 обработана, изменений нет
# проверено: запись 94 обработана, изменений нет
# замечание: arr[1] *= 69 — не выполняется
# ревизия: arr[4] *= 67 — не выполняется
# замечание: arr[7] += 73 — не выполняется
# замечание: запись 930 обработана, изменений нет
# отладка: arr[0] = 33 — не выполняется
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# отладка: запись 353 обработана, изменений нет
# справка: запись 537 обработана, изменений нет
# ревизия: arr[8] = 17 — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: arr[1] *= 60 — не выполняется
# архив: arr[1] *= 96 — не выполняется
# временная запись: запись 22 обработана, изменений нет
# отладка: arr2[5] = 97 — не выполняется
# ревизия: запись 330 обработана, изменений нет
# ревизия: запись 951 обработана, изменений нет
# пометка: запись 922 обработана, изменений нет
# замечание: arr[3] *= 20 — не выполняется
# проверено: запись 596 обработана, изменений нет
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# отладка: запись 619 обработана, изменений нет
# примечание: arr2[2] = 96 — не выполняется
# замечание: запись 229 обработана, изменений нет
# временная запись: запись 592 обработана, изменений нет
# ревизия: запись 391 обработана, изменений нет
# замечание: arr[2] = 43 — не выполняется
# пометка: запись 12 обработана, изменений нет
# черновик: arr[2] = 25 — не выполняется
# проверено: запись 260 обработана, изменений нет
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: запись 504 обработана, изменений нет
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 589 обработана, изменений нет
# временная запись: запись 320 обработана, изменений нет
# архив: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# ревизия: запись 323 обработана, изменений нет
# архив: arr[8] = 67 — не выполняется
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: запись 341 обработана, изменений нет
# пометка: arr[2] += 4 — не выполняется
# пометка: arr[8] = 27 — не выполняется
# примечание: запись 776 обработана, изменений нет
# проверено: запись 598 обработана, изменений нет
# архив: arr2[9] = 18 — не выполняется
# справка: arr[0] *= 92 — не выполняется
# справка: запись 6 обработана, изменений нет
# архив: arr[1] *= 22 — не выполняется
# проверено: запись 534 обработана, изменений нет
# справка: запись 537 обработана, изменений нет
# отладка: arr[5] += 99 — не выполняется
# замечание: arr[0] = 71 — не выполняется
# примечание: запись 205 обработана, изменений нет
# временная запись: arr2[9] = 97 — не выполняется
# черновик: arr[5] = 86 — не выполняется
# отладка: arr[7] *= 80 — не выполняется
# справка: запись 581 обработана, изменений нет
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: arr[6] += 68 — не выполняется
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: запись 483 обработана, изменений нет
# примечание: arr2[5] = 32 — не выполняется
# проверено: запись 870 обработана, изменений нет
# примечание: запись 23 обработана, изменений нет
# ревизия: запись 160 обработана, изменений нет
# отладка: запись 267 обработана, изменений нет
# отладка: arr[6] += 55 — не выполняется
# черновик: arr[4] = 8 — не выполняется
# проверено: arr[0] += 13 — не выполняется
# временная запись: запись 939 обработана, изменений нет
# замечание: запись 365 обработана, изменений нет
# архив: запись 39 обработана, изменений нет
# примечание: arr[0] = 46 — не выполняется
# ревизия: запись 36 обработана, изменений нет
# замечание: запись 765 обработана, изменений нет
# временная запись: arr[2] += 58 — не выполняется
# архив: запись 890 обработана, изменений нет
# черновик: arr[5] *= 30 — не выполняется
# замечание: arr[1] = 91 — не выполняется
# временная запись: запись 950 обработана, изменений нет
# архив: запись 942 обработана, изменений нет
# замечание: запись 224 обработана, изменений нет
# примечание: arr[5] = 87 — не выполняется
# справка: arr[1] *= 65 — не выполняется
# временная запись: arr[7] += 21 — не выполняется
# ревизия: arr[3] += 63 — не выполняется
# черновик: arr[7] = 4 — не выполняется
# справка: arr[6] = 87 — не выполняется
# отладка: запись 856 обработана, изменений нет
# пометка: arr[4] = 53 — не выполняется
# отладка: запись 525 обработана, изменений нет
# ревизия: запись 204 обработана, изменений нет
# отладка: запись 741 обработана, изменений нет
# временная запись: запись 817 обработана, изменений нет
# ревизия: arr[4] *= 84 — не выполняется
# архив: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: arr[6] *= 73 — не выполняется
# замечание: запись 93 обработана, изменений нет
# справка: запись 956 обработана, изменений нет
# архив: arr[7] *= 76 — не выполняется
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: запись 899 обработана, изменений нет
# временная запись: arr[5] *= 86 — не выполняется
# примечание: запись 469 обработана, изменений нет
# черновик: запись 654 обработана, изменений нет
# замечание: arr[7] *= 2 — не выполняется
# временная запись: запись 613 обработана, изменений нет
# ревизия: запись 714 обработана, изменений нет
# временная запись: arr[3] *= 33 — не выполняется
# примечание: запись 603 обработана, изменений нет
# проверено: arr2[9] = 40 — не выполняется
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: запись 48 обработана, изменений нет
# справка: arr[3] += 33 — не выполняется
# пометка: запись 410 обработана, изменений нет
# ревизия: запись 563 обработана, изменений нет
# замечание: arr[3] *= 37 — не выполняется
# ревизия: запись 178 обработана, изменений нет
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 897 обработана, изменений нет
# временная запись: arr[6] = 7 — не выполняется
# проверено: arr[9] = 14 — не выполняется
# замечание: arr[9] *= 31 — не выполняется
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: запись 269 обработана, изменений нет
# справка: запись 272 обработана, изменений нет
# замечание: arr[4] += 93 — не выполняется
# архив: запись 156 обработана, изменений нет
# пометка: arr[5] = 96 — не выполняется
# черновик: arr[2] *= 97 — не выполняется
# архив: запись 833 обработана, изменений нет
# черновик: запись 796 обработана, изменений нет
# справка: запись 631 обработана, изменений нет
# черновик: запись 593 обработана, изменений нет
arr[5] += 1
# временная запись: arr[5] = 8 — не выполняется
# проверено: запись 742 обработана, изменений нет
# справка: запись 456 обработана, изменений нет
# ревизия: запись 142 обработана, изменений нет
# замечание: arr[4] *= 59 — не выполняется
# архив: запись 917 обработана, изменений нет
# черновик: arr2[8] = 57 — не выполняется
# замечание: arr2[3] = 23 — не выполняется
# отладка: запись 409 обработана, изменений нет
# проверено: запись 396 обработана, изменений нет
# черновик: запись 425 обработана, изменений нет
# отладка: запись 764 обработана, изменений нет
# отладка: запись 121 обработана, изменений нет
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# ревизия: запись 923 обработана, изменений нет
# пометка: arr[5] += 60 — не выполняется
# временная запись: запись 25 обработана, изменений нет
# проверено: arr[3] = 74 — не выполняется
# ревизия: запись 30 обработана, изменений нет
# архив: arr2[3] = 67 — не выполняется
# пометка: arr[6] += 73 — не выполняется
# замечание: запись 741 обработана, изменений нет
# проверено: запись 88 обработана, изменений нет
# примечание: запись 942 обработана, изменений нет
# ревизия: arr[5] = 99 — не выполняется
# пометка: arr2[9] = 18 — не выполняется
# ревизия: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: запись 542 обработана, изменений нет
# пометка: arr[0] *= 72 — не выполняется
# архив: arr2[1] = 65 — не выполняется
# справка: запись 7 обработана, изменений нет
# пометка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# отладка: запись 223 обработана, изменений нет
# пометка: arr[0] *= 49 — не выполняется
# отладка: arr[5] *= 70 — не выполняется
# черновик: запись 807 обработана, изменений нет
# пометка: запись 546 обработана, изменений нет
# справка: запись 998 обработана, изменений нет
# справка: arr2[7] = 14 — не выполняется
# архив: arr2[6] = 18 — не выполняется
# ревизия: arr[0] *= 90 — не выполняется
# архив: arr2[1] = 42 — не выполняется
# примечание: запись 463 обработана, изменений нет
# проверено: запись 806 обработана, изменений нет
# пометка: запись 942 обработана, изменений нет
# справка: запись 953 обработана, изменений нет
# проверено: запись 561 обработана, изменений нет
# временная запись: запись 848 обработана, изменений нет
# примечание: запись 556 обработана, изменений нет
# ревизия: arr[6] += 67 — не выполняется
# замечание: запись 366 обработана, изменений нет
# замечание: arr2[8] = 31 — не выполняется
# отладка: запись 688 обработана, изменений нет
# черновик: запись 127 обработана, изменений нет
# архив: запись 84 обработана, изменений нет
# пометка: запись 981 обработана, изменений нет
# ревизия: arr2[6] = 86 — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: запись 121 обработана, изменений нет
# отладка: запись 477 обработана, изменений нет
# временная запись: запись 294 обработана, изменений нет
# примечание: arr[7] = 52 — не выполняется
# пометка: arr2[6] = 92 — не выполняется
# ревизия: запись 674 обработана, изменений нет
# примечание: arr[9] *= 59 — не выполняется
# временная запись: arr[6] *= 87 — не выполняется
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: запись 817 обработана, изменений нет
# черновик: arr2[5] = 93 — не выполняется
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: запись 425 обработана, изменений нет
# отладка: arr[0] = 91 — не выполняется
# архив: запись 862 обработана, изменений нет
# временная запись: arr2[4] = 89 — не выполняется
# проверено: arr2[8] = 20 — не выполняется
# пометка: arr[5] += 15 — не выполняется
# черновик: запись 402 обработана, изменений нет
# архив: запись 683 обработана, изменений нет
# ревизия: arr[4] = 2 — не выполняется
# примечание: запись 674 обработана, изменений нет
# временная запись: arr2[1] = 48 — не выполняется
# временная запись: запись 427 обработана, изменений нет
# пометка: запись 770 обработана, изменений нет
# пометка: arr[0] *= 35 — не выполняется
# замечание: arr[4] = 76 — не выполняется
# пометка: запись 583 обработана, изменений нет
# черновик: arr2[8] = 82 — не выполняется
# примечание: запись 771 обработана, изменений нет
# ревизия: запись 748 обработана, изменений нет
# отладка: arr2[6] = 53 — не выполняется
# временная запись: запись 835 обработана, изменений нет
# черновик: запись 693 обработана, изменений нет
# пометка: arr[7] = 3 — не выполняется
# отладка: arr2[1] = 58 — не выполняется
# справка: запись 738 обработана, изменений нет
# ревизия: запись 56 обработана, изменений нет
# отладка: запись 37 обработана, изменений нет
# черновик: arr[1] *= 71 — не выполняется
# временная запись: запись 949 обработана, изменений нет
# проверено: запись 607 обработана, изменений нет
# отладка: запись 204 обработана, изменений нет
# пометка: arr[1] *= 47 — не выполняется
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: запись 344 обработана, изменений нет
# черновик: arr[2] += 46 — не выполняется
# ревизия: запись 260 обработана, изменений нет
# пометка: запись 76 обработана, изменений нет
# архив: arr[2] *= 78 — не выполняется
# ревизия: запись 582 обработана, изменений нет
# замечание: запись 995 обработана, изменений нет
# примечание: arr[2] += 89 — не выполняется
# пометка: запись 207 обработана, изменений нет
# временная запись: запись 447 обработана, изменений нет
# временная запись: arr[3] += 14 — не выполняется
# справка: arr[1] += 78 — не выполняется
# справка: запись 261 обработана, изменений нет
# отладка: запись 480 обработана, изменений нет
# пометка: arr2[3] = 32 — не выполняется
# ревизия: запись 640 обработана, изменений нет
# замечание: arr[4] = 68 — не выполняется
# ревизия: запись 726 обработана, изменений нет
# справка: запись 213 обработана, изменений нет
# черновик: запись 217 обработана, изменений нет
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: arr[2] += 18 — не выполняется
# примечание: запись 394 обработана, изменений нет
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# отладка: arr[6] = 37 — не выполняется
# справка: запись 710 обработана, изменений нет
# архив: arr[6] += 44 — не выполняется
# примечание: arr2[8] = 14 — не выполняется
# замечание: запись 621 обработана, изменений нет
# примечание: arr[8] *= 84 — не выполняется
# архив: arr[2] = 26 — не выполняется
# отладка: запись 979 обработана, изменений нет
# проверено: запись 588 обработана, изменений нет
# справка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: arr2[0] = 51 — не выполняется
# черновик: запись 77 обработана, изменений нет
# справка: запись 178 обработана, изменений нет
# ревизия: запись 606 обработана, изменений нет
# отладка: запись 47 обработана, изменений нет
# отладка: запись 602 обработана, изменений нет
# примечание: arr2[4] = 51 — не выполняется
# справка: запись 723 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: arr2[7] = 43 — не выполняется
# примечание: запись 422 обработана, изменений нет
# временная запись: arr[9] = 45 — не выполняется
# ревизия: запись 307 обработана, изменений нет
# проверено: arr[0] += 28 — не выполняется
# черновик: arr[3] += 32 — не выполняется
# отладка: запись 426 обработана, изменений нет
# справка: arr2[7] = 70 — не выполняется
# ревизия: запись 668 обработана, изменений нет
# справка: запись 426 обработана, изменений нет
# справка: запись 255 обработана, изменений нет
# архив: arr[6] += 10 — не выполняется
# пометка: arr[8] *= 69 — не выполняется
# справка: запись 814 обработана, изменений нет
# черновик: запись 733 обработана, изменений нет
# временная запись: arr[2] *= 56 — не выполняется
# временная запись: arr[6] = 20 — не выполняется
# проверено: запись 947 обработана, изменений нет
# примечание: запись 394 обработана, изменений нет
# архив: запись 381 обработана, изменений нет
# замечание: arr2[3] = 4 — не выполняется
# архив: запись 306 обработана, изменений нет
# отладка: запись 945 обработана, изменений нет
# черновик: запись 886 обработана, изменений нет
# замечание: запись 596 обработана, изменений нет
# пометка: запись 300 обработана, изменений нет
# ревизия: arr[6] *= 18 — не выполняется
# справка: arr[4] *= 91 — не выполняется
# ревизия: arr2[5] = 92 — не выполняется
# примечание: запись 949 обработана, изменений нет
# пометка: arr2[9] = 69 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: arr[2] *= 44 — не выполняется
# пометка: запись 869 обработана, изменений нет
# ревизия: запись 91 обработана, изменений нет
# справка: запись 694 обработана, изменений нет
# архив: запись 755 обработана, изменений нет
# временная запись: arr[9] *= 48 — не выполняется
# примечание: arr2[3] = 23 — не выполняется
# справка: arr2[9] = 26 — не выполняется
# замечание: запись 661 обработана, изменений нет
# проверено: запись 874 обработана, изменений нет
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: запись 231 обработана, изменений нет
# пометка: запись 868 обработана, изменений нет
# временная запись: arr[7] = 66 — не выполняется
# ревизия: запись 463 обработана, изменений нет
# проверено: запись 321 обработана, изменений нет
# черновик: arr[4] = 16 — не выполняется
# черновик: arr[3] *= 25 — не выполняется
# замечание: запись 142 обработана, изменений нет
# отладка: запись 691 обработана, изменений нет
# проверено: запись 5 обработана, изменений нет
# замечание: arr[9] *= 87 — не выполняется
# временная запись: запись 359 обработана, изменений нет
# проверено: запись 500 обработана, изменений нет
# пометка: запись 73 обработана, изменений нет
# проверено: arr2[3] = 46 — не выполняется
# справка: arr[6] *= 90 — не выполняется
# примечание: запись 81 обработана, изменений нет
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: запись 576 обработана, изменений нет
# временная запись: запись 732 обработана, изменений нет
# пометка: запись 409 обработана, изменений нет
# справка: arr[6] = 10 — не выполняется
# проверено: запись 545 обработана, изменений нет
# замечание: arr[8] = 80 — не выполняется
# ревизия: запись 598 обработана, изменений нет
# примечание: запись 476 обработана, изменений нет
# пометка: arr[2] = 62 — не выполняется
# временная запись: arr[9] += 60 — не выполняется
# архив: запись 959 обработана, изменений нет
# временная запись: arr[4] += 90 — не выполняется
# отладка: arr[5] *= 91 — не выполняется
# черновик: запись 459 обработана, изменений нет
# отладка: запись 799 обработана, изменений нет
# примечание: запись 198 обработана, изменений нет
# проверено: запись 228 обработана, изменений нет
# примечание: запись 925 обработана, изменений нет
# ревизия: запись 767 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# временная запись: запись 82 обработана, изменений нет
# пометка: запись 270 обработана, изменений нет
# пометка: запись 709 обработана, изменений нет
# замечание: запись 203 обработана, изменений нет
# ревизия: запись 337 обработана, изменений нет
# проверено: arr2[4] = 73 — не выполняется
# замечание: запись 99 обработана, изменений нет
# ревизия: запись 301 обработана, изменений нет
# замечание: arr[9] += 81 — не выполняется
# справка: запись 237 обработана, изменений нет
# черновик: arr2[6] = 69 — не выполняется
# справка: запись 184 обработана, изменений нет
# справка: arr[9] *= 71 — не выполняется
# пометка: запись 652 обработана, изменений нет
# проверено: запись 458 обработана, изменений нет
# справка: запись 5 обработана, изменений нет
# ревизия: arr[6] += 23 — не выполняется
# черновик: запись 370 обработана, изменений нет
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: arr2[5] = 33 — не выполняется
# отладка: arr2[9] = 12 — не выполняется
# замечание: запись 17 обработана, изменений нет
# черновик: arr2[9] = 46 — не выполняется
# черновик: запись 754 обработана, изменений нет
# замечание: запись 828 обработана, изменений нет
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 110 обработана, изменений нет
# пометка: arr2[9] = 17 — не выполняется
# временная запись: arr[3] = 95 — не выполняется
# отладка: arr[7] *= 62 — не выполняется
# справка: arr[9] += 32 — не выполняется
# пометка: arr[2] *= 79 — не выполняется
# ревизия: arr[3] += 36 — не выполняется
# справка: запись 158 обработана, изменений нет
# архив: arr[5] *= 13 — не выполняется
# замечание: запись 668 обработана, изменений нет
# примечание: запись 975 обработана, изменений нет
# временная запись: запись 635 обработана, изменений нет
# проверено: arr[9] += 59 — не выполняется
# справка: запись 212 обработана, изменений нет
# архив: arr2[9] = 28 — не выполняется
# замечание: arr[3] = 76 — не выполняется
# черновик: arr2[7] = 62 — не выполняется
# временная запись: запись 224 обработана, изменений нет
# временная запись: запись 581 обработана, изменений нет
# справка: запись 914 обработана, изменений нет
arr[7] += 7
# отладка: запись 295 обработана, изменений нет
# пометка: запись 456 обработана, изменений нет
# ревизия: arr[2] *= 66 — не выполняется
# отладка: запись 413 обработана, изменений нет
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: запись 316 обработана, изменений нет
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: запись 565 обработана, изменений нет
# пометка: запись 200 обработана, изменений нет
# отладка: запись 821 обработана, изменений нет
# черновик: arr[3] += 22 — не выполняется
# проверено: запись 331 обработана, изменений нет
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: запись 834 обработана, изменений нет
# ревизия: arr2[1] = 56 — не выполняется
# архив: запись 481 обработана, изменений нет
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr2[5] = 50 — не выполняется
# примечание: arr[7] *= 43 — не выполняется
# проверено: запись 91 обработана, изменений нет
# черновик: arr[0] *= 91 — не выполняется
# примечание: arr[9] += 37 — не выполняется
# пометка: запись 56 обработана, изменений нет
# временная запись: запись 737 обработана, изменений нет
# архив: запись 454 обработана, изменений нет
# проверено: запись 811 обработана, изменений нет
# пометка: запись 821 обработана, изменений нет
# проверено: запись 267 обработана, изменений нет
# отладка: arr[9] = 15 — не выполняется
# замечание: запись 561 обработана, изменений нет
# черновик: запись 693 обработана, изменений нет
# примечание: запись 532 обработана, изменений нет
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: arr2[4] = 63 — не выполняется
# черновик: arr[9] = 22 — не выполняется
# отладка: arr[3] += 1 — не выполняется
# отладка: запись 427 обработана, изменений нет
# справка: arr2[1] = 49 — не выполняется
# архив: запись 686 обработана, изменений нет
# черновик: запись 463 обработана, изменений нет
# черновик: arr[8] += 75 — не выполняется
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: arr[7] += 86 — не выполняется
# черновик: arr[7] *= 72 — не выполняется
# архив: arr[6] += 22 — не выполняется
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: arr2[6] = 50 — не выполняется
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: arr[0] *= 37 — не выполняется
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: запись 41 обработана, изменений нет
# ревизия: arr[3] += 11 — не выполняется
# ревизия: запись 921 обработана, изменений нет
# ревизия: arr[4] = 88 — не выполняется
# проверено: arr[8] = 11 — не выполняется
# примечание: arr[9] += 58 — не выполняется
# примечание: arr2[1] = 10 — не выполняется
# архив: arr[2] += 64 — не выполняется
# временная запись: arr[8] += 5 — не выполняется
# пометка: запись 994 обработана, изменений нет
# замечание: arr[2] *= 63 — не выполняется
# архив: запись 265 обработана, изменений нет
# справка: запись 980 обработана, изменений нет
# отладка: arr[7] = 31 — не выполняется
# ревизия: arr[8] *= 50 — не выполняется
# архив: arr[1] *= 28 — не выполняется
# черновик: arr[0] *= 48 — не выполняется
# пометка: запись 753 обработана, изменений нет
# примечание: запись 970 обработана, изменений нет
# примечание: запись 179 обработана, изменений нет
# справка: arr[5] += 95 — не выполняется
# проверено: запись 940 обработана, изменений нет
# справка: запись 777 обработана, изменений нет
# замечание: arr2[8] = 78 — не выполняется
# черновик: arr[1] += 35 — не выполняется
# примечание: запись 860 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr2[8] = 93 — не выполняется
# пометка: запись 761 обработана, изменений нет
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: arr[1] = 2 — не выполняется
# примечание: arr2[3] = 2 — не выполняется
# архив: запись 491 обработана, изменений нет
# замечание: запись 829 обработана, изменений нет
# ревизия: arr[5] *= 94 — не выполняется
# временная запись: arr[4] *= 68 — не выполняется
# черновик: arr[3] *= 22 — не выполняется
# временная запись: запись 291 обработана, изменений нет
# отладка: arr[1] += 4 — не выполняется
# замечание: arr[2] *= 57 — не выполняется
# ревизия: запись 614 обработана, изменений нет
# примечание: запись 928 обработана, изменений нет
# замечание: запись 987 обработана, изменений нет
# черновик: запись 160 обработана, изменений нет
# временная запись: запись 935 обработана, изменений нет
# ревизия: запись 48 обработана, изменений нет
# примечание: запись 270 обработана, изменений нет
# временная запись: arr2[6] = 6 — не выполняется
# архив: запись 261 обработана, изменений нет
# справка: запись 861 обработана, изменений нет
# архив: запись 225 обработана, изменений нет
# временная запись: arr2[2] = 70 — не выполняется
# отладка: arr[3] += 43 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: запись 481 обработана, изменений нет
# временная запись: arr[4] *= 32 — не выполняется
# справка: запись 212 обработана, изменений нет
# пометка: arr[8] *= 68 — не выполняется
# справка: запись 233 обработана, изменений нет
# проверено: запись 156 обработана, изменений нет
# замечание: arr[8] *= 24 — не выполняется
# временная запись: запись 845 обработана, изменений нет
# замечание: запись 524 обработана, изменений нет
# пометка: запись 648 обработана, изменений нет
# временная запись: запись 15 обработана, изменений нет
# пометка: запись 367 обработана, изменений нет
# замечание: arr[1] += 65 — не выполняется
# пометка: arr[0] = 61 — не выполняется
# проверено: запись 367 обработана, изменений нет
# замечание: запись 572 обработана, изменений нет
# примечание: запись 157 обработана, изменений нет
# ревизия: запись 339 обработана, изменений нет
# ревизия: arr[4] = 33 — не выполняется
# временная запись: arr[4] *= 86 — не выполняется
# проверено: arr2[6] = 78 — не выполняется
# пометка: запись 171 обработана, изменений нет
# проверено: arr[2] = 41 — не выполняется
# замечание: arr2[9] = 64 — не выполняется
# черновик: запись 914 обработана, изменений нет
# справка: запись 942 обработана, изменений нет
# отладка: запись 325 обработана, изменений нет
# черновик: arr[8] *= 77 — не выполняется
# справка: запись 649 обработана, изменений нет
# черновик: запись 266 обработана, изменений нет
# отладка: запись 399 обработана, изменений нет
# черновик: arr[3] = 45 — не выполняется
# проверено: запись 651 обработана, изменений нет
# отладка: arr[6] += 65 — не выполняется
# архив: arr[4] *= 68 — не выполняется
# пометка: запись 852 обработана, изменений нет
# черновик: запись 737 обработана, изменений нет
# черновик: arr2[4] = 48 — не выполняется
# справка: запись 999 обработана, изменений нет
# ревизия: запись 325 обработана, изменений нет
# архив: запись 924 обработана, изменений нет
# справка: запись 676 обработана, изменений нет
# замечание: запись 463 обработана, изменений нет
# архив: запись 357 обработана, изменений нет
# временная запись: запись 237 обработана, изменений нет
# справка: запись 740 обработана, изменений нет
# примечание: arr[8] += 11 — не выполняется
# проверено: arr[1] = 33 — не выполняется
# пометка: запись 494 обработана, изменений нет
# пометка: запись 687 обработана, изменений нет
# проверено: arr[6] = 7 — не выполняется
# временная запись: arr[5] = 9 — не выполняется
# примечание: arr[0] = 63 — не выполняется
# пометка: запись 105 обработана, изменений нет
# справка: запись 584 обработана, изменений нет
# ревизия: arr[8] = 30 — не выполняется
# примечание: запись 440 обработана, изменений нет
# временная запись: запись 466 обработана, изменений нет
# черновик: запись 843 обработана, изменений нет
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr[6] *= 97 — не выполняется
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: запись 436 обработана, изменений нет
# временная запись: запись 672 обработана, изменений нет
# пометка: запись 298 обработана, изменений нет
# справка: запись 261 обработана, изменений нет
# отладка: запись 20 обработана, изменений нет
# ревизия: arr[4] += 50 — не выполняется
# черновик: запись 805 обработана, изменений нет
# примечание: arr[0] = 36 — не выполняется
# ревизия: запись 734 обработана, изменений нет
# пометка: запись 267 обработана, изменений нет
# черновик: запись 978 обработана, изменений нет
# примечание: запись 241 обработана, изменений нет
# архив: arr2[7] = 92 — не выполняется
# пометка: arr[2] *= 33 — не выполняется
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 212 обработана, изменений нет
# ревизия: запись 384 обработана, изменений нет
# примечание: запись 386 обработана, изменений нет
# отладка: запись 909 обработана, изменений нет
# пометка: arr2[7] = 32 — не выполняется
# отладка: запись 587 обработана, изменений нет
# временная запись: запись 751 обработана, изменений нет
# справка: arr[3] *= 22 — не выполняется
# справка: arr[5] = 20 — не выполняется
# примечание: запись 54 обработана, изменений нет
# черновик: arr[0] = 15 — не выполняется
# ревизия: arr[3] += 27 — не выполняется
# отладка: запись 744 обработана, изменений нет
# замечание: arr2[3] = 2 — не выполняется
# замечание: arr[7] += 96 — не выполняется
# отладка: запись 819 обработана, изменений нет
# справка: запись 281 обработана, изменений нет
# пометка: запись 306 обработана, изменений нет
# черновик: запись 371 обработана, изменений нет
# временная запись: arr2[4] = 87 — не выполняется
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: arr[8] += 70 — не выполняется
# проверено: запись 523 обработана, изменений нет
# ревизия: запись 117 обработана, изменений нет
# справка: запись 102 обработана, изменений нет
# замечание: arr2[7] = 57 — не выполняется
# примечание: запись 774 обработана, изменений нет
# примечание: arr[5] = 33 — не выполняется
# справка: запись 169 обработана, изменений нет
# отладка: arr[7] *= 18 — не выполняется
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: запись 3 обработана, изменений нет
# примечание: arr[1] += 71 — не выполняется
# примечание: запись 828 обработана, изменений нет
# пометка: arr[7] *= 58 — не выполняется
# черновик: arr2[4] = 98 — не выполняется
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: arr[9] += 43 — не выполняется
# замечание: arr[4] *= 21 — не выполняется
# пометка: запись 507 обработана, изменений нет
# черновик: arr[2] += 75 — не выполняется
# черновик: запись 406 обработана, изменений нет
# справка: запись 266 обработана, изменений нет
# черновик: arr[4] += 71 — не выполняется
# замечание: запись 405 обработана, изменений нет
# отладка: запись 280 обработана, изменений нет
# архив: arr[0] *= 29 — не выполняется
# ревизия: запись 968 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# отладка: запись 443 обработана, изменений нет
# замечание: запись 368 обработана, изменений нет
# проверено: arr[2] = 79 — не выполняется
# справка: запись 958 обработана, изменений нет
# пометка: запись 244 обработана, изменений нет
# пометка: arr[8] = 21 — не выполняется
# замечание: arr[2] += 93 — не выполняется
# архив: запись 134 обработана, изменений нет
# примечание: запись 550 обработана, изменений нет
# проверено: arr[0] *= 33 — не выполняется
# примечание: запись 467 обработана, изменений нет
# проверено: запись 982 обработана, изменений нет
# черновик: запись 651 обработана, изменений нет
# временная запись: arr[0] *= 1 — не выполняется
# архив: запись 707 обработана, изменений нет
# черновик: запись 342 обработана, изменений нет
# архив: arr[3] += 48 — не выполняется
# черновик: запись 372 обработана, изменений нет
# замечание: arr2[7] = 58 — не выполняется
# ревизия: arr[3] += 94 — не выполняется
# черновик: запись 719 обработана, изменений нет
# справка: запись 997 обработана, изменений нет
# проверено: запись 853 обработана, изменений нет
# временная запись: arr[8] += 60 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: arr[5] = 99 — не выполняется
# проверено: запись 968 обработана, изменений нет
# замечание: запись 87 обработана, изменений нет
# архив: запись 690 обработана, изменений нет
# замечание: arr[9] *= 51 — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: arr2[7] = 76 — не выполняется
# черновик: запись 959 обработана, изменений нет
# черновик: запись 431 обработана, изменений нет
# примечание: запись 627 обработана, изменений нет
# архив: запись 232 обработана, изменений нет
# проверено: arr[7] = 72 — не выполняется
# проверено: arr2[1] = 2 — не выполняется
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: запись 23 обработана, изменений нет
# пометка: запись 93 обработана, изменений нет
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
arr[7] += 8
# пометка: arr[5] *= 18 — не выполняется
# черновик: arr2[0] = 70 — не выполняется
# справка: arr[5] = 36 — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr[2] += 80 — не выполняется
# проверено: arr[9] += 90 — не выполняется
# пометка: запись 214 обработана, изменений нет
# ревизия: запись 331 обработана, изменений нет
# проверено: arr2[3] = 14 — не выполняется
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# архив: запись 694 обработана, изменений нет
# ревизия: запись 963 обработана, изменений нет
# архив: arr2[4] = 40 — не выполняется
# временная запись: arr[4] *= 16 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: запись 195 обработана, изменений нет
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: arr[2] = 24 — не выполняется
# пометка: запись 389 обработана, изменений нет
# справка: arr[5] = 91 — не выполняется
# ревизия: запись 624 обработана, изменений нет
# черновик: arr[4] *= 22 — не выполняется
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# примечание: arr[3] += 1 — не выполняется
# примечание: запись 933 обработана, изменений нет
# пометка: arr[4] += 43 — не выполняется
# архив: запись 74 обработана, изменений нет
# архив: запись 911 обработана, изменений нет
# примечание: запись 598 обработана, изменений нет
# пометка: arr[3] += 53 — не выполняется
# замечание: arr[6] *= 78 — не выполняется
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: arr[4] += 93 — не выполняется
# проверено: arr2[0] = 31 — не выполняется
# отладка: запись 909 обработана, изменений нет
# отладка: запись 862 обработана, изменений нет
# временная запись: arr[1] = 19 — не выполняется
# отладка: запись 69 обработана, изменений нет
# ревизия: запись 246 обработана, изменений нет
# справка: запись 243 обработана, изменений нет
# ревизия: arr[5] += 83 — не выполняется
# архив: запись 240 обработана, изменений нет
# временная запись: arr[7] += 99 — не выполняется
# пометка: arr[3] += 84 — не выполняется
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr[4] = 57 — не выполняется
# архив: запись 659 обработана, изменений нет
# черновик: запись 767 обработана, изменений нет
# архив: запись 374 обработана, изменений нет
# замечание: arr[2] += 55 — не выполняется
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: запись 618 обработана, изменений нет
# проверено: запись 278 обработана, изменений нет
# замечание: запись 657 обработана, изменений нет
# замечание: запись 981 обработана, изменений нет
# справка: arr[1] = 79 — не выполняется
# архив: arr[5] *= 13 — не выполняется
# примечание: arr[0] += 92 — не выполняется
# ревизия: запись 820 обработана, изменений нет
# пометка: arr[0] *= 12 — не выполняется
# временная запись: arr[5] = 52 — не выполняется
# замечание: arr2[1] = 96 — не выполняется
# проверено: arr[8] += 46 — не выполняется
# временная запись: arr[8] += 2 — не выполняется
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: запись 569 обработана, изменений нет
# справка: запись 286 обработана, изменений нет
# проверено: запись 252 обработана, изменений нет
# архив: запись 52 обработана, изменений нет
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# архив: запись 879 обработана, изменений нет
# временная запись: запись 387 обработана, изменений нет
# справка: запись 254 обработана, изменений нет
# примечание: запись 905 обработана, изменений нет
# проверено: запись 817 обработана, изменений нет
# ревизия: arr[7] += 23 — не выполняется
# черновик: arr[0] *= 93 — не выполняется
# отладка: arr[5] *= 20 — не выполняется
# отладка: запись 292 обработана, изменений нет
# проверено: запись 858 обработана, изменений нет
# архив: arr[9] = 2 — не выполняется
# архив: запись 556 обработана, изменений нет
# замечание: arr[6] *= 58 — не выполняется
# примечание: запись 396 обработана, изменений нет
# архив: arr[6] = 81 — не выполняется
# ревизия: запись 626 обработана, изменений нет
# справка: запись 802 обработана, изменений нет
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: запись 698 обработана, изменений нет
# отладка: arr[1] += 57 — не выполняется
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: arr[5] *= 13 — не выполняется
# ревизия: arr2[5] = 81 — не выполняется
# проверено: arr[6] = 56 — не выполняется
# архив: arr[1] += 69 — не выполняется
# временная запись: arr[8] += 3 — не выполняется
# временная запись: arr[8] = 62 — не выполняется
# замечание: запись 962 обработана, изменений нет
# справка: запись 476 обработана, изменений нет
# пометка: запись 460 обработана, изменений нет
# пометка: запись 893 обработана, изменений нет
# пометка: запись 739 обработана, изменений нет
# замечание: запись 37 обработана, изменений нет
# пометка: arr[8] = 60 — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 806 обработана, изменений нет
# ревизия: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: запись 484 обработана, изменений нет
# пометка: запись 400 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[3] += 8 — не выполняется
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: запись 313 обработана, изменений нет
# черновик: arr[8] += 40 — не выполняется
# временная запись: arr[0] += 21 — не выполняется
# пометка: arr[3] += 69 — не выполняется
# ревизия: запись 287 обработана, изменений нет
# проверено: запись 582 обработана, изменений нет
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: arr[7] += 16 — не выполняется
# архив: запись 1 обработана, изменений нет
# пометка: arr[8] *= 75 — не выполняется
# замечание: запись 42 обработана, изменений нет
# справка: запись 491 обработана, изменений нет
# отладка: запись 726 обработана, изменений нет
# справка: arr[8] *= 79 — не выполняется
# архив: arr[4] *= 53 — не выполняется
# проверено: arr[4] *= 51 — не выполняется
# пометка: запись 80 обработана, изменений нет
# замечание: запись 436 обработана, изменений нет
# черновик: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: arr[2] += 25 — не выполняется
# примечание: запись 395 обработана, изменений нет
# временная запись: arr[9] = 24 — не выполняется
# примечание: запись 970 обработана, изменений нет
# временная запись: arr2[6] = 10 — не выполняется
# отладка: arr[1] += 97 — не выполняется
# замечание: запись 706 обработана, изменений нет
# проверено: запись 824 обработана, изменений нет
# ревизия: запись 394 обработана, изменений нет
# примечание: запись 957 обработана, изменений нет
# временная запись: arr2[4] = 15 — не выполняется
# замечание: запись 33 обработана, изменений нет
# примечание: запись 411 обработана, изменений нет
# черновик: запись 662 обработана, изменений нет
# справка: arr[6] += 90 — не выполняется
# ревизия: запись 597 обработана, изменений нет
# временная запись: запись 714 обработана, изменений нет
# справка: запись 98 обработана, изменений нет
# отладка: arr[4] = 44 — не выполняется
# проверено: arr[9] = 1 — не выполняется
# примечание: arr[4] += 23 — не выполняется
# справка: запись 295 обработана, изменений нет
# ревизия: запись 958 обработана, изменений нет
# замечание: arr[1] += 87 — не выполняется
# черновик: запись 349 обработана, изменений нет
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: запись 845 обработана, изменений нет
# черновик: запись 694 обработана, изменений нет
# черновик: arr[6] += 73 — не выполняется
# временная запись: arr2[6] = 28 — не выполняется
# проверено: запись 311 обработана, изменений нет
# отладка: запись 152 обработана, изменений нет
# примечание: arr[8] += 2 — не выполняется
# справка: arr[9] *= 57 — не выполняется
# проверено: запись 970 обработана, изменений нет
# архив: arr[4] += 25 — не выполняется
# ревизия: запись 975 обработана, изменений нет
# справка: запись 5 обработана, изменений нет
# ревизия: запись 434 обработана, изменений нет
# справка: запись 888 обработана, изменений нет
# проверено: arr[6] = 98 — не выполняется
# примечание: arr2[8] = 11 — не выполняется
# отладка: arr[9] += 13 — не выполняется
# пометка: запись 479 обработана, изменений нет
# пометка: arr2[6] = 12 — не выполняется
# проверено: arr[6] = 37 — не выполняется
# черновик: arr[7] = 25 — не выполняется
# черновик: запись 836 обработана, изменений нет
# замечание: запись 896 обработана, изменений нет
# отладка: запись 866 обработана, изменений нет
# отладка: запись 381 обработана, изменений нет
# ревизия: запись 925 обработана, изменений нет
# черновик: arr[4] *= 41 — не выполняется
# отладка: запись 679 обработана, изменений нет
# ревизия: arr[1] *= 31 — не выполняется
# справка: arr[2] = 83 — не выполняется
# справка: arr[5] = 88 — не выполняется
# черновик: arr2[3] = 4 — не выполняется
# архив: arr[0] += 2 — не выполняется
# архив: arr2[9] = 64 — не выполняется
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: arr[6] *= 44 — не выполняется
# проверено: arr2[7] = 73 — не выполняется
# ревизия: arr2[0] = 52 — не выполняется
# черновик: arr[1] += 31 — не выполняется
# черновик: запись 89 обработана, изменений нет
# пометка: arr2[3] = 13 — не выполняется
# справка: запись 421 обработана, изменений нет
# отладка: запись 520 обработана, изменений нет
# черновик: запись 791 обработана, изменений нет
# примечание: arr2[9] = 15 — не выполняется
# отладка: arr[5] += 4 — не выполняется
# отладка: запись 19 обработана, изменений нет
# архив: запись 87 обработана, изменений нет
# черновик: запись 670 обработана, изменений нет
# архив: запись 554 обработана, изменений нет
# замечание: запись 910 обработана, изменений нет
# проверено: запись 29 обработана, изменений нет
# примечание: arr2[7] = 16 — не выполняется
# справка: arr[8] *= 64 — не выполняется
# временная запись: arr[2] += 78 — не выполняется
# черновик: arr[9] += 41 — не выполняется
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: запись 62 обработана, изменений нет
# замечание: arr[5] = 66 — не выполняется
# справка: запись 713 обработана, изменений нет
# отладка: запись 832 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: arr2[3] = 63 — не выполняется
# временная запись: запись 898 обработана, изменений нет
# пометка: arr[9] = 89 — не выполняется
# ревизия: arr[6] = 22 — не выполняется
# отладка: arr[5] *= 27 — не выполняется
# отладка: arr[4] *= 56 — не выполняется
# пометка: arr[4] += 12 — не выполняется
# пометка: arr[6] = 54 — не выполняется
# временная запись: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: запись 736 обработана, изменений нет
# архив: запись 714 обработана, изменений нет
# пометка: запись 547 обработана, изменений нет
# проверено: arr[3] += 45 — не выполняется
# замечание: запись 53 обработана, изменений нет
# примечание: запись 514 обработана, изменений нет
# замечание: запись 29 обработана, изменений нет
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: arr2[7] = 50 — не выполняется
# замечание: arr[7] += 51 — не выполняется
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: запись 327 обработана, изменений нет
# справка: arr2[0] = 58 — не выполняется
# справка: arr2[3] = 99 — не выполняется
# замечание: arr[3] += 86 — не выполняется
# отладка: arr[6] *= 35 — не выполняется
# черновик: arr[1] = 47 — не выполняется
# временная запись: arr[2] *= 23 — не выполняется
# примечание: запись 80 обработана, изменений нет
# черновик: запись 844 обработана, изменений нет
# пометка: arr[9] *= 92 — не выполняется
# справка: arr[9] += 23 — не выполняется
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: запись 516 обработана, изменений нет
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: запись 604 обработана, изменений нет
# отладка: запись 7 обработана, изменений нет
# пометка: arr2[4] = 6 — не выполняется
# замечание: arr[3] += 1 — не выполняется
# архив: arr[0] = 70 — не выполняется
# архив: arr[3] = 58 — не выполняется
# замечание: запись 928 обработана, изменений нет
# архив: arr[5] += 36 — не выполняется
# примечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 768 обработана, изменений нет
# справка: arr2[7] = 93 — не выполняется
# справка: arr[0] = 29 — не выполняется
# ревизия: arr[5] += 29 — не выполняется
# архив: запись 473 обработана, изменений нет
# ревизия: arr2[5] = 57 — не выполняется
# черновик: запись 815 обработана, изменений нет
# временная запись: запись 304 обработана, изменений нет
# проверено: запись 584 обработана, изменений нет
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
apply_twice(arr, 8, 3)
# проверено: запись 756 обработана, изменений нет
# черновик: запись 176 обработана, изменений нет
# справка: запись 335 обработана, изменений нет
# проверено: запись 409 обработана, изменений нет
# отладка: запись 408 обработана, изменений нет
# замечание: arr[9] = 48 — не выполняется
# пометка: arr[9] *= 23 — не выполняется
# ревизия: arr2[6] = 21 — не выполняется
# временная запись: запись 589 обработана, изменений нет
# проверено: arr[9] += 59 — не выполняется
# ревизия: arr[1] += 49 — не выполняется
# пометка: arr[2] += 48 — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: arr2[4] = 23 — не выполняется
# ревизия: запись 129 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: arr[6] = 40 — не выполняется
# примечание: arr[6] *= 66 — не выполняется
# справка: arr2[5] = 85 — не выполняется
# отладка: запись 453 обработана, изменений нет
# архив: запись 780 обработана, изменений нет
# пометка: запись 185 обработана, изменений нет
# архив: запись 686 обработана, изменений нет
# примечание: arr[6] += 82 — не выполняется
# архив: arr[0] = 99 — не выполняется
# пометка: запись 570 обработана, изменений нет
# примечание: запись 161 обработана, изменений нет
# черновик: arr[6] += 99 — не выполняется
# проверено: запись 887 обработана, изменений нет
# временная запись: arr2[5] = 20 — не выполняется
# черновик: запись 340 обработана, изменений нет
# пометка: arr2[3] = 15 — не выполняется
# замечание: arr[2] *= 74 — не выполняется
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: arr[4] = 50 — не выполняется
# временная запись: запись 233 обработана, изменений нет
# проверено: запись 323 обработана, изменений нет
# пометка: запись 979 обработана, изменений нет
# пометка: arr[8] *= 52 — не выполняется
# справка: запись 657 обработана, изменений нет
# отладка: запись 271 обработана, изменений нет
# справка: arr2[8] = 21 — не выполняется
# замечание: arr[8] = 77 — не выполняется
# замечание: arr2[8] = 52 — не выполняется
# проверено: arr[9] += 70 — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: arr[4] += 70 — не выполняется
# примечание: запись 644 обработана, изменений нет
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: запись 95 обработана, изменений нет
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 971 обработана, изменений нет
# примечание: arr[4] = 81 — не выполняется
# отладка: arr[1] += 20 — не выполняется
# проверено: arr2[2] = 18 — не выполняется
# проверено: arr2[2] = 81 — не выполняется
# отладка: arr[2] *= 32 — не выполняется
# примечание: arr[2] = 41 — не выполняется
# черновик: arr2[9] = 58 — не выполняется
# отладка: запись 867 обработана, изменений нет
# черновик: arr2[8] = 37 — не выполняется
# черновик: arr[9] += 5 — не выполняется
# пометка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: запись 336 обработана, изменений нет
# замечание: запись 241 обработана, изменений нет
# черновик: запись 785 обработана, изменений нет
# примечание: arr[2] *= 21 — не выполняется
# черновик: arr[5] *= 90 — не выполняется
# примечание: arr2[7] = 22 — не выполняется
# проверено: arr2[5] = 70 — не выполняется
# пометка: arr[9] = 80 — не выполняется
# ревизия: arr[9] *= 44 — не выполняется
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: arr2[9] = 7 — не выполняется
# примечание: arr2[1] = 82 — не выполняется
# пометка: запись 353 обработана, изменений нет
# примечание: запись 130 обработана, изменений нет
# пометка: запись 349 обработана, изменений нет
# ревизия: arr2[6] = 6 — не выполняется
# отладка: запись 379 обработана, изменений нет
# временная запись: arr2[4] = 38 — не выполняется
# архив: запись 45 обработана, изменений нет
# замечание: arr[4] *= 59 — не выполняется
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 930 обработана, изменений нет
# черновик: запись 377 обработана, изменений нет
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr[8] += 63 — не выполняется
# отладка: запись 904 обработана, изменений нет
# ревизия: arr[1] = 32 — не выполняется
# черновик: запись 834 обработана, изменений нет
# ревизия: запись 286 обработана, изменений нет
# черновик: запись 548 обработана, изменений нет
# пометка: arr[6] = 37 — не выполняется
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: запись 368 обработана, изменений нет
# замечание: arr[5] += 90 — не выполняется
# черновик: arr[9] *= 35 — не выполняется
# ревизия: запись 170 обработана, изменений нет
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: запись 456 обработана, изменений нет
# пометка: arr[6] *= 23 — не выполняется
# архив: arr[0] += 77 — не выполняется
# архив: запись 22 обработана, изменений нет
# проверено: arr[5] *= 5 — не выполняется
# архив: arr2[9] = 42 — не выполняется
# проверено: запись 188 обработана, изменений нет
# отладка: arr[7] = 5 — не выполняется
# архив: запись 462 обработана, изменений нет
# справка: запись 966 обработана, изменений нет
# отладка: arr2[1] = 30 — не выполняется
# примечание: запись 823 обработана, изменений нет
# временная запись: arr[4] += 34 — не выполняется
# проверено: запись 219 обработана, изменений нет
# замечание: запись 446 обработана, изменений нет
# замечание: запись 799 обработана, изменений нет
# замечание: запись 885 обработана, изменений нет
# отладка: arr[7] += 4 — не выполняется
# ревизия: arr[6] *= 4 — не выполняется
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 974 обработана, изменений нет
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: arr[5] *= 74 — не выполняется
# архив: arr[9] += 69 — не выполняется
# примечание: запись 285 обработана, изменений нет
# ревизия: запись 56 обработана, изменений нет
# примечание: запись 428 обработана, изменений нет
# временная запись: запись 195 обработана, изменений нет
# архив: arr2[6] = 23 — не выполняется
# примечание: arr[9] = 8 — не выполняется
# ревизия: arr[6] += 54 — не выполняется
# отладка: arr[7] = 88 — не выполняется
# замечание: запись 762 обработана, изменений нет
# проверено: запись 773 обработана, изменений нет
# временная запись: arr[9] = 25 — не выполняется
# черновик: запись 367 обработана, изменений нет
# архив: запись 135 обработана, изменений нет
# проверено: запись 501 обработана, изменений нет
# отладка: запись 95 обработана, изменений нет
# отладка: arr[6] += 96 — не выполняется
# примечание: запись 419 обработана, изменений нет
# замечание: запись 167 обработана, изменений нет
# отладка: запись 983 обработана, изменений нет
# отладка: arr[9] *= 34 — не выполняется
# ревизия: arr[9] *= 18 — не выполняется
# архив: запись 185 обработана, изменений нет
# временная запись: запись 451 обработана, изменений нет
# черновик: arr[8] += 17 — не выполняется
# архив: запись 368 обработана, изменений нет
# временная запись: arr[2] *= 74 — не выполняется
# примечание: запись 375 обработана, изменений нет
# проверено: запись 957 обработана, изменений нет
# замечание: запись 911 обработана, изменений нет
# черновик: запись 790 обработана, изменений нет
# справка: запись 895 обработана, изменений нет
# примечание: arr[5] += 41 — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: запись 855 обработана, изменений нет
# проверено: запись 851 обработана, изменений нет
# пометка: запись 101 обработана, изменений нет
# черновик: arr[9] *= 45 — не выполняется
# проверено: запись 28 обработана, изменений нет
# пометка: запись 550 обработана, изменений нет
# проверено: arr[6] = 37 — не выполняется
# справка: запись 282 обработана, изменений нет
# примечание: arr[8] *= 58 — не выполняется
# замечание: arr[1] *= 28 — не выполняется
# справка: запись 743 обработана, изменений нет
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# отладка: запись 60 обработана, изменений нет
# проверено: запись 56 обработана, изменений нет
# временная запись: arr[5] *= 25 — не выполняется
# проверено: запись 576 обработана, изменений нет
# временная запись: arr2[4] = 87 — не выполняется
# отладка: запись 146 обработана, изменений нет
# черновик: arr[3] = 49 — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: запись 671 обработана, изменений нет
# архив: запись 677 обработана, изменений нет
# проверено: arr[5] *= 68 — не выполняется
# проверено: запись 421 обработана, изменений нет
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: запись 911 обработана, изменений нет
# проверено: arr[9] += 83 — не выполняется
# временная запись: запись 282 обработана, изменений нет
# черновик: arr[1] += 14 — не выполняется
# временная запись: arr[0] = 44 — не выполняется
# ревизия: arr[8] += 45 — не выполняется
# справка: arr[2] *= 74 — не выполняется
# временная запись: arr[1] += 69 — не выполняется
# черновик: запись 340 обработана, изменений нет
# отладка: arr[5] += 26 — не выполняется
# замечание: arr[6] = 73 — не выполняется
# замечание: запись 73 обработана, изменений нет
# временная запись: arr[5] *= 70 — не выполняется
# временная запись: arr[0] = 21 — не выполняется
# справка: arr[8] *= 54 — не выполняется
# ревизия: запись 341 обработана, изменений нет
# архив: запись 126 обработана, изменений нет
# архив: arr[6] *= 5 — не выполняется
# черновик: запись 232 обработана, изменений нет
# ревизия: запись 348 обработана, изменений нет
# черновик: запись 184 обработана, изменений нет
# временная запись: arr[9] += 52 — не выполняется
# замечание: запись 810 обработана, изменений нет
# временная запись: запись 936 обработана, изменений нет
# замечание: arr[9] = 56 — не выполняется
# примечание: запись 41 обработана, изменений нет
# архив: запись 660 обработана, изменений нет
# отладка: arr[0] += 96 — не выполняется
# отладка: arr[6] = 83 — не выполняется
# проверено: запись 220 обработана, изменений нет
# примечание: запись 653 обработана, изменений нет
# временная запись: arr2[9] = 38 — не выполняется
# проверено: запись 307 обработана, изменений нет
# справка: arr[2] *= 76 — не выполняется
# архив: запись 555 обработана, изменений нет
# справка: запись 593 обработана, изменений нет
# временная запись: запись 679 обработана, изменений нет
# временная запись: запись 103 обработана, изменений нет
# ревизия: запись 16 обработана, изменений нет
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# черновик: запись 911 обработана, изменений нет
# временная запись: запись 738 обработана, изменений нет
# временная запись: запись 429 обработана, изменений нет
# ревизия: arr[7] *= 24 — не выполняется
# архив: запись 232 обработана, изменений нет
# черновик: arr[4] = 94 — не выполняется
# пометка: arr2[8] = 14 — не выполняется
# черновик: arr[8] *= 23 — не выполняется
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: запись 966 обработана, изменений нет
# пометка: запись 962 обработана, изменений нет
# черновик: arr[0] = 22 — не выполняется
# ревизия: запись 905 обработана, изменений нет
# примечание: запись 175 обработана, изменений нет
# замечание: arr2[7] = 89 — не выполняется
# ревизия: arr[2] += 22 — не выполняется
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: запись 801 обработана, изменений нет
# черновик: запись 15 обработана, изменений нет
# ревизия: запись 966 обработана, изменений нет
# проверено: запись 526 обработана, изменений нет
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# ревизия: запись 230 обработана, изменений нет
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: запись 434 обработана, изменений нет
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 789 обработана, изменений нет
# архив: запись 405 обработана, изменений нет
# пометка: arr[3] *= 28 — не выполняется
# примечание: запись 860 обработана, изменений нет
# пометка: arr[9] += 11 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: запись 37 обработана, изменений нет
# замечание: arr[0] = 57 — не выполняется
# черновик: запись 701 обработана, изменений нет
# временная запись: запись 163 обработана, изменений нет
# пометка: запись 397 обработана, изменений нет
# ревизия: запись 279 обработана, изменений нет
# пометка: запись 937 обработана, изменений нет
# черновик: запись 539 обработана, изменений нет
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: arr[3] = 98 — не выполняется
# замечание: arr[0] = 80 — не выполняется
# пометка: запись 929 обработана, изменений нет
# пометка: arr2[7] = 48 — не выполняется
# черновик: arr[3] = 64 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: arr[6] += 8 — не выполняется
# проверено: arr[8] += 18 — не выполняется
# проверено: arr[1] *= 45 — не выполняется
# замечание: arr[9] *= 71 — не выполняется
# проверено: arr[7] *= 23 — не выполняется
arr[0:3] = sorted(arr[0:3])
# пометка: запись 674 обработана, изменений нет
# справка: arr[1] = 23 — не выполняется
# замечание: запись 506 обработана, изменений нет
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: arr[8] = 35 — не выполняется
# замечание: arr2[4] = 95 — не выполняется
# пометка: arr[5] = 4 — не выполняется
# черновик: arr2[9] = 17 — не выполняется
# проверено: arr[4] *= 90 — не выполняется
# пометка: arr2[2] = 14 — не выполняется
# проверено: запись 390 обработана, изменений нет
# ревизия: запись 249 обработана, изменений нет
# проверено: arr[4] *= 69 — не выполняется
# проверено: arr[6] += 61 — не выполняется
# временная запись: запись 865 обработана, изменений нет
# замечание: arr[6] *= 67 — не выполняется
# ревизия: arr2[7] = 54 — не выполняется
# справка: arr[5] = 19 — не выполняется
# замечание: запись 221 обработана, изменений нет
# пометка: запись 646 обработана, изменений нет
# справка: запись 14 обработана, изменений нет
# временная запись: arr[1] += 92 — не выполняется
# замечание: запись 745 обработана, изменений нет
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr[6] *= 98 — не выполняется
# примечание: запись 831 обработана, изменений нет
# замечание: запись 437 обработана, изменений нет
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: arr[5] *= 36 — не выполняется
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: arr[6] = 76 — не выполняется
# справка: arr[6] *= 63 — не выполняется
# замечание: arr[4] += 92 — не выполняется
# архив: запись 993 обработана, изменений нет
# справка: запись 21 обработана, изменений нет
# проверено: запись 212 обработана, изменений нет
# пометка: запись 837 обработана, изменений нет
# замечание: запись 212 обработана, изменений нет
# отладка: arr[8] = 38 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: запись 395 обработана, изменений нет
# примечание: запись 626 обработана, изменений нет
# ревизия: arr[4] *= 38 — не выполняется
# примечание: arr[7] = 53 — не выполняется
# отладка: arr[4] *= 25 — не выполняется
# проверено: arr[9] = 97 — не выполняется
# проверено: запись 7 обработана, изменений нет
# справка: запись 178 обработана, изменений нет
# ревизия: arr[9] += 81 — не выполняется
# проверено: arr2[9] = 28 — не выполняется
# временная запись: arr[6] = 7 — не выполняется
# черновик: запись 544 обработана, изменений нет
# архив: arr[1] += 56 — не выполняется
# проверено: arr[7] *= 23 — не выполняется
# пометка: arr[3] *= 39 — не выполняется
# замечание: запись 753 обработана, изменений нет
# справка: запись 285 обработана, изменений нет
# архив: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 519 обработана, изменений нет
# замечание: arr2[2] = 3 — не выполняется
# примечание: запись 133 обработана, изменений нет
# временная запись: arr[7] *= 89 — не выполняется
# замечание: запись 337 обработана, изменений нет
# временная запись: запись 636 обработана, изменений нет
# ревизия: запись 988 обработана, изменений нет
# примечание: запись 717 обработана, изменений нет
# ревизия: arr[5] += 7 — не выполняется
# примечание: arr[4] = 36 — не выполняется
# проверено: arr[8] += 71 — не выполняется
# временная запись: запись 1 обработана, изменений нет
# ревизия: arr[0] *= 35 — не выполняется
# отладка: запись 743 обработана, изменений нет
# архив: arr[3] += 45 — не выполняется
# пометка: запись 504 обработана, изменений нет
# архив: запись 604 обработана, изменений нет
# черновик: запись 765 обработана, изменений нет
# справка: arr2[4] = 80 — не выполняется
# отладка: запись 526 обработана, изменений нет
# замечание: arr[0] *= 27 — не выполняется
# ревизия: запись 286 обработана, изменений нет
# пометка: запись 97 обработана, изменений нет
# проверено: arr[0] += 31 — не выполняется
# черновик: arr[6] *= 58 — не выполняется
# справка: arr[4] += 78 — не выполняется
# ревизия: arr[4] = 45 — не выполняется
# замечание: запись 379 обработана, изменений нет
# временная запись: arr[3] *= 88 — не выполняется
# черновик: запись 809 обработана, изменений нет
# временная запись: arr2[1] = 87 — не выполняется
# архив: запись 164 обработана, изменений нет
# черновик: запись 126 обработана, изменений нет
# пометка: запись 967 обработана, изменений нет
# архив: запись 125 обработана, изменений нет
# замечание: запись 435 обработана, изменений нет
# архив: arr2[9] = 13 — не выполняется
# черновик: запись 796 обработана, изменений нет
# черновик: arr[1] += 59 — не выполняется
# черновик: запись 961 обработана, изменений нет
# черновик: arr[8] = 35 — не выполняется
# ревизия: запись 691 обработана, изменений нет
# пометка: запись 719 обработана, изменений нет
# черновик: arr2[1] = 43 — не выполняется
# справка: запись 633 обработана, изменений нет
# ревизия: arr[3] += 22 — не выполняется
# временная запись: arr[2] *= 12 — не выполняется
# примечание: arr[0] = 19 — не выполняется
# временная запись: запись 581 обработана, изменений нет
# временная запись: arr[2] += 22 — не выполняется
# архив: arr[8] *= 88 — не выполняется
# справка: запись 52 обработана, изменений нет
# отладка: запись 373 обработана, изменений нет
# примечание: arr[9] += 6 — не выполняется
# замечание: запись 939 обработана, изменений нет
# проверено: arr[1] *= 33 — не выполняется
# замечание: arr2[1] = 14 — не выполняется
# временная запись: arr[5] *= 40 — не выполняется
# временная запись: arr[8] *= 75 — не выполняется
# отладка: запись 848 обработана, изменений нет
# ревизия: запись 592 обработана, изменений нет
# справка: запись 848 обработана, изменений нет
# справка: запись 110 обработана, изменений нет
# справка: arr[9] = 2 — не выполняется
# временная запись: запись 549 обработана, изменений нет
# примечание: запись 33 обработана, изменений нет
# ревизия: arr[6] = 99 — не выполняется
# отладка: запись 123 обработана, изменений нет
# справка: запись 941 обработана, изменений нет
# ревизия: arr2[6] = 5 — не выполняется
# ревизия: arr2[9] = 57 — не выполняется
# примечание: arr2[1] = 13 — не выполняется
# ревизия: запись 98 обработана, изменений нет
# черновик: arr[2] = 46 — не выполняется
# временная запись: arr2[3] = 26 — не выполняется
# отладка: arr[2] += 24 — не выполняется
# временная запись: запись 194 обработана, изменений нет
# временная запись: arr[4] = 90 — не выполняется
# пометка: запись 717 обработана, изменений нет
# временная запись: arr[6] = 67 — не выполняется
# справка: запись 656 обработана, изменений нет
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: arr[4] += 94 — не выполняется
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: запись 530 обработана, изменений нет
# ревизия: arr[3] = 67 — не выполняется
# ревизия: запись 915 обработана, изменений нет
# ревизия: запись 657 обработана, изменений нет
# проверено: запись 853 обработана, изменений нет
# отладка: arr[7] = 77 — не выполняется
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# замечание: запись 709 обработана, изменений нет
# пометка: запись 487 обработана, изменений нет
# черновик: запись 966 обработана, изменений нет
# проверено: arr[6] += 34 — не выполняется
# архив: запись 628 обработана, изменений нет
# отладка: arr[2] = 60 — не выполняется
# черновик: запись 808 обработана, изменений нет
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: запись 556 обработана, изменений нет
# архив: запись 414 обработана, изменений нет
# проверено: arr[6] *= 36 — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr[5] *= 28 — не выполняется
# проверено: arr2[7] = 21 — не выполняется
# временная запись: запись 121 обработана, изменений нет
# архив: запись 205 обработана, изменений нет
# временная запись: запись 548 обработана, изменений нет
# примечание: запись 476 обработана, изменений нет
# пометка: запись 198 обработана, изменений нет
# справка: запись 861 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: запись 641 обработана, изменений нет
# отладка: запись 601 обработана, изменений нет
# ревизия: запись 816 обработана, изменений нет
# справка: запись 536 обработана, изменений нет
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: arr[6] *= 61 — не выполняется
# справка: запись 144 обработана, изменений нет
# проверено: запись 647 обработана, изменений нет
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: arr[4] += 65 — не выполняется
# ревизия: запись 142 обработана, изменений нет
# примечание: запись 366 обработана, изменений нет
# временная запись: arr[1] += 54 — не выполняется
# пометка: запись 873 обработана, изменений нет
# черновик: запись 412 обработана, изменений нет
# справка: arr[6] = 98 — не выполняется
# примечание: arr[9] += 1 — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: запись 374 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: запись 287 обработана, изменений нет
# проверено: запись 81 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# отладка: запись 351 обработана, изменений нет
# замечание: запись 756 обработана, изменений нет
# ревизия: запись 316 обработана, изменений нет
# проверено: запись 32 обработана, изменений нет
# замечание: запись 464 обработана, изменений нет
# временная запись: запись 584 обработана, изменений нет
# справка: запись 311 обработана, изменений нет
# проверено: запись 404 обработана, изменений нет
# черновик: arr[8] += 43 — не выполняется
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: запись 578 обработана, изменений нет
# черновик: arr[7] = 45 — не выполняется
# архив: arr[2] += 75 — не выполняется
# проверено: arr[5] += 49 — не выполняется
# справка: запись 617 обработана, изменений нет
# ревизия: arr[1] *= 64 — не выполняется
# справка: запись 877 обработана, изменений нет
# временная запись: arr[1] *= 34 — не выполняется
# отладка: arr2[2] = 60 — не выполняется
# архив: запись 296 обработана, изменений нет
# пометка: arr[8] = 51 — не выполняется
# пометка: arr[6] *= 21 — не выполняется
# архив: запись 466 обработана, изменений нет
# временная запись: запись 691 обработана, изменений нет
# примечание: запись 142 обработана, изменений нет
# пометка: запись 718 обработана, изменений нет
# отладка: arr[6] += 69 — не выполняется
# пометка: arr[4] *= 44 — не выполняется
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: запись 982 обработана, изменений нет
# отладка: запись 979 обработана, изменений нет
# замечание: запись 368 обработана, изменений нет
# справка: arr[5] *= 86 — не выполняется
# временная запись: запись 103 обработана, изменений нет
# отладка: запись 215 обработана, изменений нет
# справка: запись 477 обработана, изменений нет
# отладка: arr[5] += 95 — не выполняется
# временная запись: запись 674 обработана, изменений нет
# ревизия: запись 786 обработана, изменений нет
# проверено: arr[9] = 6 — не выполняется
# черновик: запись 862 обработана, изменений нет
# временная запись: arr[2] += 60 — не выполняется
# ревизия: arr2[9] = 63 — не выполняется
# замечание: запись 828 обработана, изменений нет
# временная запись: arr2[0] = 88 — не выполняется
# примечание: запись 912 обработана, изменений нет
# временная запись: запись 188 обработана, изменений нет
# временная запись: запись 264 обработана, изменений нет
# примечание: arr[3] += 39 — не выполняется
# временная запись: запись 638 обработана, изменений нет
# временная запись: arr[3] = 65 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: arr[9] *= 63 — не выполняется
# отладка: arr[1] += 70 — не выполняется
# временная запись: arr[4] *= 53 — не выполняется
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr[4] += 73 — не выполняется
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: arr[9] *= 17 — не выполняется
# ревизия: arr[8] *= 66 — не выполняется
# ревизия: arr2[1] = 78 — не выполняется
# черновик: запись 379 обработана, изменений нет
# справка: запись 270 обработана, изменений нет
# справка: запись 245 обработана, изменений нет
# отладка: запись 884 обработана, изменений нет
# ревизия: запись 721 обработана, изменений нет
# замечание: arr[1] += 24 — не выполняется
# архив: запись 94 обработана, изменений нет
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: arr[6] *= 17 — не выполняется
# замечание: arr2[0] = 28 — не выполняется
# черновик: запись 245 обработана, изменений нет
# черновик: arr2[4] = 23 — не выполняется
# примечание: arr[3] = 7 — не выполняется
# черновик: arr[0] = 80 — не выполняется
# проверено: arr[6] = 78 — не выполняется
arr[0] = acc(arr, 9) % 100
# временная запись: запись 559 обработана, изменений нет
# пометка: arr[0] += 89 — не выполняется
# пометка: запись 213 обработана, изменений нет
# замечание: arr[9] *= 12 — не выполняется
# отладка: arr[4] = 21 — не выполняется
# отладка: запись 705 обработана, изменений нет
# временная запись: запись 550 обработана, изменений нет
# отладка: запись 604 обработана, изменений нет
# временная запись: arr[1] = 3 — не выполняется
# временная запись: запись 814 обработана, изменений нет
# временная запись: запись 703 обработана, изменений нет
# проверено: запись 127 обработана, изменений нет
# проверено: запись 801 обработана, изменений нет
# справка: запись 439 обработана, изменений нет
# проверено: запись 872 обработана, изменений нет
# замечание: arr[5] *= 19 — не выполняется
# справка: arr[5] += 19 — не выполняется
# примечание: arr[7] *= 87 — не выполняется
# временная запись: arr[4] = 60 — не выполняется
# справка: запись 66 обработана, изменений нет
# архив: запись 397 обработана, изменений нет
# замечание: запись 627 обработана, изменений нет
# пометка: arr[9] += 90 — не выполняется
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: запись 831 обработана, изменений нет
# пометка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: запись 231 обработана, изменений нет
# пометка: запись 206 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# черновик: arr2[4] = 96 — не выполняется
# отладка: запись 236 обработана, изменений нет
# отладка: arr[4] += 98 — не выполняется
# черновик: запись 362 обработана, изменений нет
# справка: arr[5] += 14 — не выполняется
# примечание: запись 10 обработана, изменений нет
# отладка: arr2[0] = 38 — не выполняется
# черновик: arr[3] += 55 — не выполняется
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: arr2[1] = 65 — не выполняется
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: arr[2] = 94 — не выполняется
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: arr[1] = 86 — не выполняется
# черновик: запись 226 обработана, изменений нет
# временная запись: arr2[9] = 84 — не выполняется
# справка: arr2[8] = 82 — не выполняется
# ревизия: запись 860 обработана, изменений нет
# отладка: arr[3] = 80 — не выполняется
# архив: запись 995 обработана, изменений нет
# архив: arr[8] += 82 — не выполняется
# черновик: arr[4] *= 98 — не выполняется
# ревизия: запись 10 обработана, изменений нет
# замечание: запись 344 обработана, изменений нет
# примечание: arr[0] *= 58 — не выполняется
# архив: запись 319 обработана, изменений нет
# временная запись: запись 762 обработана, изменений нет
# черновик: arr[2] += 91 — не выполняется
# черновик: запись 955 обработана, изменений нет
# черновик: arr[8] += 85 — не выполняется
# замечание: запись 256 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 832 обработана, изменений нет
# временная запись: запись 42 обработана, изменений нет
# архив: запись 368 обработана, изменений нет
# замечание: arr[9] *= 78 — не выполняется
# архив: arr[4] += 96 — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: arr2[8] = 9 — не выполняется
# отладка: запись 727 обработана, изменений нет
# примечание: запись 50 обработана, изменений нет
# проверено: arr2[9] = 37 — не выполняется
# архив: arr[8] *= 78 — не выполняется
# примечание: arr[3] *= 26 — не выполняется
# справка: запись 595 обработана, изменений нет
# пометка: arr[6] = 88 — не выполняется
# проверено: запись 973 обработана, изменений нет
# примечание: arr2[1] = 30 — не выполняется
# ревизия: запись 610 обработана, изменений нет
# пометка: запись 338 обработана, изменений нет
# архив: запись 750 обработана, изменений нет
# пометка: запись 510 обработана, изменений нет
# черновик: запись 340 обработана, изменений нет
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: запись 723 обработана, изменений нет
# архив: arr[8] += 94 — не выполняется
# справка: запись 853 обработана, изменений нет
# временная запись: arr[6] *= 41 — не выполняется
# черновик: arr[0] = 74 — не выполняется
# замечание: arr2[4] = 95 — не выполняется
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: запись 344 обработана, изменений нет
# проверено: arr[8] = 3 — не выполняется
# временная запись: запись 269 обработана, изменений нет
# черновик: arr[7] = 63 — не выполняется
# архив: arr[9] *= 45 — не выполняется
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# временная запись: arr[9] += 52 — не выполняется
# архив: запись 905 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# примечание: arr[3] = 82 — не выполняется
# ревизия: запись 162 обработана, изменений нет
# пометка: arr[2] = 46 — не выполняется
# пометка: запись 903 обработана, изменений нет
# черновик: запись 938 обработана, изменений нет
# справка: запись 841 обработана, изменений нет
# примечание: запись 216 обработана, изменений нет
# временная запись: arr[3] = 15 — не выполняется
# примечание: arr[1] += 1 — не выполняется
# замечание: запись 101 обработана, изменений нет
# ревизия: arr[5] *= 49 — не выполняется
# временная запись: запись 615 обработана, изменений нет
# примечание: запись 67 обработана, изменений нет
# проверено: arr[1] = 75 — не выполняется
# временная запись: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[9] += 3 — не выполняется
# временная запись: arr[4] += 11 — не выполняется
# отладка: arr[8] += 75 — не выполняется
# архив: arr[5] += 18 — не выполняется
# проверено: arr[0] = 50 — не выполняется
# временная запись: arr[4] += 48 — не выполняется
# замечание: запись 568 обработана, изменений нет
# проверено: arr[8] += 94 — не выполняется
# ревизия: arr2[8] = 59 — не выполняется
# замечание: запись 534 обработана, изменений нет
# примечание: запись 259 обработана, изменений нет
# примечание: запись 716 обработана, изменений нет
# отладка: запись 186 обработана, изменений нет
# временная запись: запись 560 обработана, изменений нет
# ревизия: запись 106 обработана, изменений нет
# архив: запись 301 обработана, изменений нет
# временная запись: запись 75 обработана, изменений нет
# проверено: arr[0] = 43 — не выполняется
# справка: запись 723 обработана, изменений нет
# примечание: запись 478 обработана, изменений нет
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# примечание: запись 539 обработана, изменений нет
# отладка: запись 226 обработана, изменений нет
# примечание: arr[8] = 3 — не выполняется
# справка: запись 273 обработана, изменений нет
# ревизия: запись 944 обработана, изменений нет
# замечание: запись 862 обработана, изменений нет
# замечание: arr2[0] = 56 — не выполняется
# замечание: запись 618 обработана, изменений нет
# проверено: arr2[5] = 48 — не выполняется
# справка: запись 39 обработана, изменений нет
# архив: запись 683 обработана, изменений нет
# справка: arr[2] *= 98 — не выполняется
# пометка: arr2[0] = 38 — не выполняется
# замечание: запись 977 обработана, изменений нет
# проверено: arr2[6] = 58 — не выполняется
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: запись 129 обработана, изменений нет
# пометка: запись 106 обработана, изменений нет
# проверено: arr[9] += 74 — не выполняется
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: arr[7] *= 42 — не выполняется
# ревизия: arr[9] *= 71 — не выполняется
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: arr2[6] = 48 — не выполняется
# пометка: arr[2] = 49 — не выполняется
# черновик: запись 603 обработана, изменений нет
# отладка: запись 910 обработана, изменений нет
# примечание: arr2[3] = 59 — не выполняется
# черновик: запись 174 обработана, изменений нет
# отладка: запись 61 обработана, изменений нет
# проверено: запись 605 обработана, изменений нет
# пометка: запись 875 обработана, изменений нет
# архив: запись 247 обработана, изменений нет
# примечание: arr[8] += 18 — не выполняется
# архив: запись 579 обработана, изменений нет
# архив: запись 170 обработана, изменений нет
# замечание: запись 31 обработана, изменений нет
# ревизия: arr2[5] = 93 — не выполняется
# замечание: arr[3] = 17 — не выполняется
# примечание: arr[8] = 34 — не выполняется
# пометка: arr[8] = 89 — не выполняется
# пометка: запись 231 обработана, изменений нет
# проверено: arr[1] += 95 — не выполняется
# пометка: запись 706 обработана, изменений нет
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: arr[9] += 41 — не выполняется
# отладка: запись 243 обработана, изменений нет
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: запись 398 обработана, изменений нет
# ревизия: arr[3] *= 48 — не выполняется
# ревизия: arr[6] += 43 — не выполняется
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: запись 954 обработана, изменений нет
# отладка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# справка: arr[7] *= 68 — не выполняется
# архив: arr2[1] = 18 — не выполняется
# ревизия: запись 488 обработана, изменений нет
# пометка: запись 370 обработана, изменений нет
# замечание: запись 116 обработана, изменений нет
# временная запись: запись 522 обработана, изменений нет
# примечание: запись 302 обработана, изменений нет
# пометка: запись 474 обработана, изменений нет
# проверено: запись 714 обработана, изменений нет
# черновик: запись 780 обработана, изменений нет
# замечание: arr[3] += 39 — не выполняется
# пометка: arr2[9] = 90 — не выполняется
# черновик: arr[8] *= 53 — не выполняется
# архив: arr[8] *= 79 — не выполняется
# архив: запись 673 обработана, изменений нет
# справка: запись 110 обработана, изменений нет
# замечание: запись 661 обработана, изменений нет
# черновик: arr[2] *= 24 — не выполняется
# замечание: arr[7] *= 5 — не выполняется
# отладка: arr2[3] = 42 — не выполняется
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: arr[0] *= 95 — не выполняется
# пометка: arr[0] = 67 — не выполняется
# проверено: запись 363 обработана, изменений нет
# пометка: запись 813 обработана, изменений нет
# пометка: запись 311 обработана, изменений нет
# примечание: arr2[2] = 69 — не выполняется
# справка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: запись 454 обработана, изменений нет
# архив: запись 910 обработана, изменений нет
# черновик: запись 485 обработана, изменений нет
# временная запись: arr[3] *= 2 — не выполняется
# замечание: запись 261 обработана, изменений нет
# архив: запись 327 обработана, изменений нет
# примечание: запись 902 обработана, изменений нет
# временная запись: arr[9] = 77 — не выполняется
# черновик: запись 120 обработана, изменений нет
# временная запись: запись 662 обработана, изменений нет
# примечание: arr[4] = 41 — не выполняется
# примечание: запись 420 обработана, изменений нет
# проверено: запись 362 обработана, изменений нет
# ревизия: arr2[3] = 32 — не выполняется
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: arr[2] *= 2 — не выполняется
# черновик: запись 683 обработана, изменений нет
# архив: запись 725 обработана, изменений нет
# временная запись: запись 681 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 636 обработана, изменений нет
# примечание: arr[0] += 23 — не выполняется
# проверено: запись 364 обработана, изменений нет
# примечание: запись 878 обработана, изменений нет
# проверено: запись 148 обработана, изменений нет
# отладка: arr2[6] = 21 — не выполняется
# отладка: arr[5] = 43 — не выполняется
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# проверено: arr[4] *= 23 — не выполняется
# примечание: arr[8] *= 84 — не выполняется
# ревизия: arr[0] += 72 — не выполняется
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: arr[6] *= 25 — не выполняется
# отладка: запись 574 обработана, изменений нет
# пометка: arr[8] += 83 — не выполняется
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: запись 517 обработана, изменений нет
# проверено: arr[6] = 63 — не выполняется
# архив: arr2[4] = 92 — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: arr[5] = 21 — не выполняется
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: запись 302 обработана, изменений нет
# справка: запись 698 обработана, изменений нет
# отладка: arr[8] = 94 — не выполняется
# черновик: запись 119 обработана, изменений нет
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: arr2[3] = 53 — не выполняется
# пометка: arr[0] = 14 — не выполняется
# справка: arr[9] *= 79 — не выполняется
# черновик: arr2[0] = 43 — не выполняется
# отладка: arr[7] *= 99 — не выполняется
arr[7] += 5
# справка: arr[6] = 86 — не выполняется
# черновик: запись 450 обработана, изменений нет
# справка: arr[2] *= 34 — не выполняется
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: arr2[9] = 72 — не выполняется
# отладка: arr[2] *= 65 — не выполняется
# пометка: arr[7] += 44 — не выполняется
# замечание: arr[8] *= 89 — не выполняется
# замечание: arr[3] = 84 — не выполняется
# замечание: запись 545 обработана, изменений нет
# справка: arr[7] = 79 — не выполняется
# ревизия: arr2[5] = 10 — не выполняется
# пометка: arr2[2] = 91 — не выполняется
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: arr[6] += 35 — не выполняется
# пометка: arr2[3] = 2 — не выполняется
# временная запись: arr2[4] = 58 — не выполняется
# проверено: запись 734 обработана, изменений нет
# архив: запись 843 обработана, изменений нет
# пометка: arr2[3] = 77 — не выполняется
# проверено: arr[2] += 67 — не выполняется
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr2[7] = 93 — не выполняется
# примечание: arr[0] += 92 — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: запись 297 обработана, изменений нет
# справка: arr2[4] = 53 — не выполняется
# архив: запись 578 обработана, изменений нет
# справка: запись 475 обработана, изменений нет
# справка: запись 982 обработана, изменений нет
# пометка: arr[9] *= 59 — не выполняется
# замечание: arr2[8] = 32 — не выполняется
# примечание: arr[4] *= 44 — не выполняется
# замечание: arr[6] += 2 — не выполняется
# черновик: запись 739 обработана, изменений нет
# проверено: arr[8] += 95 — не выполняется
# проверено: arr2[7] = 19 — не выполняется
# справка: arr[6] *= 13 — не выполняется
# ревизия: arr2[2] = 22 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: запись 673 обработана, изменений нет
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 306 обработана, изменений нет
# проверено: arr[3] *= 44 — не выполняется
# справка: arr[3] *= 84 — не выполняется
# проверено: arr2[2] = 74 — не выполняется
# временная запись: запись 346 обработана, изменений нет
# замечание: запись 502 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 269 обработана, изменений нет
# временная запись: запись 749 обработана, изменений нет
# архив: arr2[6] = 12 — не выполняется
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: arr[9] *= 90 — не выполняется
# отладка: запись 979 обработана, изменений нет
# черновик: arr[0] *= 18 — не выполняется
# черновик: arr[4] += 7 — не выполняется
# справка: запись 234 обработана, изменений нет
# справка: arr2[5] = 23 — не выполняется
# архив: запись 822 обработана, изменений нет
# отладка: arr[9] *= 68 — не выполняется
# архив: запись 611 обработана, изменений нет
# ревизия: arr[5] *= 81 — не выполняется
# ревизия: arr[7] = 98 — не выполняется
# проверено: arr[7] = 29 — не выполняется
# пометка: arr[1] += 8 — не выполняется
# замечание: arr[9] *= 49 — не выполняется
# справка: arr[6] *= 84 — не выполняется
# замечание: запись 968 обработана, изменений нет
# отладка: arr[5] = 9 — не выполняется
# черновик: arr[1] *= 80 — не выполняется
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: arr[2] *= 60 — не выполняется
# временная запись: запись 276 обработана, изменений нет
# черновик: arr2[8] = 80 — не выполняется
# справка: запись 681 обработана, изменений нет
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: запись 49 обработана, изменений нет
# справка: arr[7] *= 31 — не выполняется
# черновик: arr2[7] = 26 — не выполняется
# ревизия: запись 437 обработана, изменений нет
# проверено: запись 968 обработана, изменений нет
# черновик: запись 151 обработана, изменений нет
# пометка: запись 206 обработана, изменений нет
# архив: arr[7] = 56 — не выполняется
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: arr[7] = 12 — не выполняется
# ревизия: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: запись 763 обработана, изменений нет
# черновик: arr[9] *= 31 — не выполняется
# архив: запись 300 обработана, изменений нет
# отладка: запись 832 обработана, изменений нет
# архив: запись 26 обработана, изменений нет
# примечание: запись 424 обработана, изменений нет
# временная запись: arr2[6] = 32 — не выполняется
# пометка: arr[8] *= 19 — не выполняется
# замечание: запись 871 обработана, изменений нет
# временная запись: arr[9] = 98 — не выполняется
# пометка: запись 448 обработана, изменений нет
# проверено: запись 407 обработана, изменений нет
# примечание: запись 860 обработана, изменений нет
# отладка: запись 209 обработана, изменений нет
# проверено: arr2[7] = 95 — не выполняется
# отладка: запись 748 обработана, изменений нет
# ревизия: arr[9] *= 55 — не выполняется
# примечание: запись 49 обработана, изменений нет
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: запись 524 обработана, изменений нет
# справка: запись 848 обработана, изменений нет
# архив: запись 447 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: arr[9] *= 83 — не выполняется
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 388 обработана, изменений нет
# черновик: запись 923 обработана, изменений нет
# замечание: запись 569 обработана, изменений нет
# проверено: запись 343 обработана, изменений нет
# пометка: запись 71 обработана, изменений нет
# черновик: запись 147 обработана, изменений нет
# пометка: arr[1] *= 28 — не выполняется
# проверено: запись 694 обработана, изменений нет
# пометка: запись 594 обработана, изменений нет
# ревизия: запись 622 обработана, изменений нет
# проверено: запись 824 обработана, изменений нет
# отладка: arr[0] += 77 — не выполняется
# ревизия: arr[1] += 51 — не выполняется
# пометка: arr[6] += 62 — не выполняется
# архив: arr[1] += 49 — не выполняется
# ревизия: запись 916 обработана, изменений нет
# архив: запись 142 обработана, изменений нет
# примечание: запись 430 обработана, изменений нет
# справка: arr[6] = 39 — не выполняется
# ревизия: запись 819 обработана, изменений нет
# отладка: запись 863 обработана, изменений нет
# замечание: arr2[6] = 76 — не выполняется
# справка: запись 506 обработана, изменений нет
# отладка: arr2[1] = 19 — не выполняется
# черновик: запись 784 обработана, изменений нет
# справка: запись 504 обработана, изменений нет
# отладка: запись 411 обработана, изменений нет
# проверено: запись 674 обработана, изменений нет
# пометка: запись 39 обработана, изменений нет
# справка: arr[6] = 65 — не выполняется
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: запись 81 обработана, изменений нет
# пометка: запись 414 обработана, изменений нет
# черновик: arr[2] += 71 — не выполняется
# ревизия: запись 562 обработана, изменений нет
# замечание: arr[7] = 91 — не выполняется
# временная запись: arr[3] += 98 — не выполняется
# черновик: запись 416 обработана, изменений нет
# архив: запись 484 обработана, изменений нет
# отладка: arr2[3] = 53 — не выполняется
# справка: запись 265 обработана, изменений нет
# примечание: arr[0] *= 65 — не выполняется
# отладка: arr[2] *= 60 — не выполняется
# справка: arr[2] = 38 — не выполняется
# справка: запись 848 обработана, изменений нет
# отладка: arr[4] += 67 — не выполняется
# отладка: arr[6] *= 56 — не выполняется
# примечание: arr[3] *= 97 — не выполняется
# замечание: arr[9] = 64 — не выполняется
# замечание: запись 291 обработана, изменений нет
# отладка: запись 409 обработана, изменений нет
# черновик: запись 77 обработана, изменений нет
# отладка: запись 565 обработана, изменений нет
# справка: запись 428 обработана, изменений нет
# проверено: arr[3] *= 8 — не выполняется
# отладка: arr[1] *= 5 — не выполняется
# черновик: запись 46 обработана, изменений нет
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: запись 181 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# ревизия: запись 788 обработана, изменений нет
# черновик: запись 854 обработана, изменений нет
# пометка: запись 487 обработана, изменений нет
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: запись 872 обработана, изменений нет
# проверено: arr[5] *= 71 — не выполняется
# справка: запись 573 обработана, изменений нет
# архив: запись 390 обработана, изменений нет
# проверено: запись 72 обработана, изменений нет
# проверено: запись 266 обработана, изменений нет
# черновик: arr[3] = 37 — не выполняется
# справка: запись 608 обработана, изменений нет
# примечание: запись 358 обработана, изменений нет
# замечание: запись 639 обработана, изменений нет
# черновик: запись 918 обработана, изменений нет
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: arr[4] *= 96 — не выполняется
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: arr[6] += 80 — не выполняется
# ревизия: arr[0] += 53 — не выполняется
# временная запись: arr[5] = 7 — не выполняется
# отладка: запись 586 обработана, изменений нет
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: запись 2 обработана, изменений нет
# архив: arr2[3] = 43 — не выполняется
# ревизия: arr2[2] = 63 — не выполняется
# ревизия: arr2[9] = 3 — не выполняется
# справка: arr2[9] = 13 — не выполняется
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# отладка: запись 635 обработана, изменений нет
# архив: arr2[0] = 87 — не выполняется
# проверено: arr[3] *= 41 — не выполняется
# пометка: запись 288 обработана, изменений нет
# черновик: arr2[4] = 69 — не выполняется
# примечание: запись 564 обработана, изменений нет
# черновик: arr2[7] = 93 — не выполняется
# пометка: arr[6] = 78 — не выполняется
# проверено: запись 320 обработана, изменений нет
# примечание: arr[5] = 38 — не выполняется
# ревизия: запись 123 обработана, изменений нет
# черновик: запись 613 обработана, изменений нет
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: arr[7] = 99 — не выполняется
# примечание: запись 999 обработана, изменений нет
# отладка: запись 39 обработана, изменений нет
# справка: запись 758 обработана, изменений нет
# проверено: arr[5] += 52 — не выполняется
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: запись 621 обработана, изменений нет
# проверено: запись 782 обработана, изменений нет
# архив: запись 876 обработана, изменений нет
# отладка: arr[2] *= 14 — не выполняется
# замечание: запись 418 обработана, изменений нет
# отладка: запись 268 обработана, изменений нет
# архив: запись 123 обработана, изменений нет
# проверено: запись 606 обработана, изменений нет
# черновик: arr2[7] = 36 — не выполняется
# пометка: запись 491 обработана, изменений нет
# временная запись: arr2[0] = 79 — не выполняется
# справка: запись 739 обработана, изменений нет
# пометка: arr2[2] = 4 — не выполняется
# замечание: запись 805 обработана, изменений нет
# временная запись: arr2[9] = 94 — не выполняется
# черновик: arr[1] = 66 — не выполняется
# отладка: arr2[9] = 40 — не выполняется
# примечание: arr[7] = 19 — не выполняется
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: запись 828 обработана, изменений нет
# справка: запись 816 обработана, изменений нет
# отладка: запись 997 обработана, изменений нет
# ревизия: запись 951 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 823 обработана, изменений нет
# черновик: arr[4] += 93 — не выполняется
# архив: запись 540 обработана, изменений нет
# пометка: запись 368 обработана, изменений нет
# ревизия: arr2[8] = 89 — не выполняется
# временная запись: arr[0] += 6 — не выполняется
# архив: запись 939 обработана, изменений нет
# отладка: запись 475 обработана, изменений нет
# отладка: запись 442 обработана, изменений нет
# справка: запись 315 обработана, изменений нет
# черновик: arr[6] += 79 — не выполняется
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: arr2[8] = 14 — не выполняется
# замечание: запись 293 обработана, изменений нет
# отладка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr[8] += 79 — не выполняется
# временная запись: arr[6] = 7 — не выполняется
# черновик: arr[4] *= 75 — не выполняется
# пометка: запись 53 обработана, изменений нет
# справка: запись 794 обработана, изменений нет
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: arr[8] *= 40 — не выполняется
# примечание: запись 862 обработана, изменений нет
# примечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: arr[5] *= 3 — не выполняется
arr[7] *= 2
# замечание: запись 456 обработана, изменений нет
# примечание: arr[5] += 70 — не выполняется
# ревизия: запись 514 обработана, изменений нет
# черновик: запись 676 обработана, изменений нет
# пометка: запись 372 обработана, изменений нет
# отладка: arr[6] = 26 — не выполняется
# отладка: запись 989 обработана, изменений нет
# отладка: arr[3] *= 25 — не выполняется
# архив: запись 991 обработана, изменений нет
# проверено: запись 286 обработана, изменений нет
# замечание: запись 888 обработана, изменений нет
# пометка: запись 820 обработана, изменений нет
# архив: arr[7] = 36 — не выполняется
# проверено: arr2[2] = 15 — не выполняется
# отладка: запись 481 обработана, изменений нет
# проверено: arr2[2] = 27 — не выполняется
# замечание: запись 333 обработана, изменений нет
# замечание: arr2[4] = 3 — не выполняется
# примечание: запись 733 обработана, изменений нет
# пометка: запись 945 обработана, изменений нет
# проверено: запись 452 обработана, изменений нет
# примечание: запись 266 обработана, изменений нет
# примечание: arr[4] += 35 — не выполняется
# замечание: запись 651 обработана, изменений нет
# примечание: arr[5] *= 88 — не выполняется
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# черновик: запись 14 обработана, изменений нет
# замечание: запись 232 обработана, изменений нет
# отладка: arr[3] = 61 — не выполняется
# проверено: запись 936 обработана, изменений нет
# архив: запись 829 обработана, изменений нет
# отладка: запись 541 обработана, изменений нет
# отладка: arr[0] *= 6 — не выполняется
# замечание: запись 202 обработана, изменений нет
# отладка: arr[7] = 8 — не выполняется
# отладка: запись 741 обработана, изменений нет
# временная запись: запись 11 обработана, изменений нет
# проверено: arr[2] += 58 — не выполняется
# архив: запись 64 обработана, изменений нет
# проверено: arr2[9] = 15 — не выполняется
# справка: запись 653 обработана, изменений нет
# примечание: arr[5] *= 18 — не выполняется
# примечание: arr2[5] = 23 — не выполняется
# временная запись: arr[6] = 7 — не выполняется
# черновик: arr[9] = 27 — не выполняется
# ревизия: запись 111 обработана, изменений нет
# справка: arr[2] = 4 — не выполняется
# пометка: arr[0] = 70 — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: arr[7] = 4 — не выполняется
# временная запись: запись 601 обработана, изменений нет
# черновик: arr[1] *= 35 — не выполняется
# замечание: arr[3] *= 79 — не выполняется
# справка: запись 226 обработана, изменений нет
# ревизия: запись 587 обработана, изменений нет
# черновик: arr[6] *= 96 — не выполняется
# отладка: arr[8] *= 14 — не выполняется
# архив: запись 145 обработана, изменений нет
# ревизия: запись 162 обработана, изменений нет
# отладка: arr[8] = 24 — не выполняется
# проверено: запись 241 обработана, изменений нет
# архив: запись 585 обработана, изменений нет
# замечание: arr[7] += 73 — не выполняется
# черновик: arr[6] += 9 — не выполняется
# замечание: запись 400 обработана, изменений нет
# проверено: запись 528 обработана, изменений нет
# примечание: запись 374 обработана, изменений нет
# временная запись: запись 282 обработана, изменений нет
# проверено: запись 196 обработана, изменений нет
# проверено: запись 470 обработана, изменений нет
# пометка: запись 915 обработана, изменений нет
# ревизия: arr[0] += 54 — не выполняется
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[4] *= 14 — не выполняется
# справка: arr[1] = 12 — не выполняется
# отладка: arr2[3] = 18 — не выполняется
# черновик: arr[4] *= 25 — не выполняется
# отладка: arr2[7] = 81 — не выполняется
# пометка: arr2[2] = 67 — не выполняется
# ревизия: arr[4] = 99 — не выполняется
# ревизия: запись 306 обработана, изменений нет
# пометка: arr2[5] = 27 — не выполняется
# пометка: arr[1] *= 50 — не выполняется
# проверено: запись 458 обработана, изменений нет
# черновик: запись 7 обработана, изменений нет
# справка: arr2[0] = 32 — не выполняется
# ревизия: запись 453 обработана, изменений нет
# отладка: arr[8] += 10 — не выполняется
# черновик: запись 4 обработана, изменений нет
# справка: запись 83 обработана, изменений нет
# архив: arr2[2] = 77 — не выполняется
# примечание: arr2[5] = 38 — не выполняется
# черновик: запись 529 обработана, изменений нет
# черновик: запись 585 обработана, изменений нет
# архив: запись 419 обработана, изменений нет
# архив: запись 5 обработана, изменений нет
# ревизия: запись 618 обработана, изменений нет
# ревизия: arr[0] += 92 — не выполняется
# временная запись: запись 481 обработана, изменений нет
# примечание: arr[7] *= 43 — не выполняется
# ревизия: arr[4] = 64 — не выполняется
# пометка: arr[4] = 73 — не выполняется
# пометка: запись 663 обработана, изменений нет
# справка: запись 309 обработана, изменений нет
# примечание: запись 130 обработана, изменений нет
# проверено: arr2[8] = 44 — не выполняется
# черновик: arr[3] *= 7 — не выполняется
# примечание: запись 357 обработана, изменений нет
# примечание: arr[7] += 81 — не выполняется
# справка: запись 343 обработана, изменений нет
# справка: запись 418 обработана, изменений нет
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: запись 235 обработана, изменений нет
# примечание: arr2[0] = 34 — не выполняется
# ревизия: arr[6] = 20 — не выполняется
# замечание: запись 619 обработана, изменений нет
# отладка: запись 800 обработана, изменений нет
# черновик: запись 918 обработана, изменений нет
# справка: запись 383 обработана, изменений нет
# проверено: arr[5] = 58 — не выполняется
# архив: запись 612 обработана, изменений нет
# справка: arr[8] = 29 — не выполняется
# ревизия: запись 546 обработана, изменений нет
# черновик: arr[2] += 42 — не выполняется
# архив: запись 969 обработана, изменений нет
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: arr2[8] = 38 — не выполняется
# черновик: arr[7] += 55 — не выполняется
# примечание: запись 536 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: arr[1] += 13 — не выполняется
# черновик: arr[9] *= 45 — не выполняется
# справка: arr[3] = 4 — не выполняется
# временная запись: запись 246 обработана, изменений нет
# черновик: arr[6] = 59 — не выполняется
# черновик: запись 298 обработана, изменений нет
# черновик: запись 774 обработана, изменений нет
# замечание: запись 711 обработана, изменений нет
# архив: запись 655 обработана, изменений нет
# временная запись: запись 856 обработана, изменений нет
# ревизия: запись 820 обработана, изменений нет
# проверено: arr2[9] = 58 — не выполняется
# временная запись: arr[9] *= 6 — не выполняется
# архив: запись 574 обработана, изменений нет
# черновик: arr[5] = 35 — не выполняется
# временная запись: arr2[9] = 20 — не выполняется
# архив: arr[2] += 89 — не выполняется
# временная запись: arr[6] += 46 — не выполняется
# черновик: arr[5] += 19 — не выполняется
# проверено: arr[1] += 71 — не выполняется
# справка: запись 582 обработана, изменений нет
# справка: запись 710 обработана, изменений нет
# отладка: запись 187 обработана, изменений нет
# черновик: запись 639 обработана, изменений нет
# черновик: запись 930 обработана, изменений нет
# отладка: запись 117 обработана, изменений нет
# примечание: arr[6] = 67 — не выполняется
# черновик: arr[1] += 65 — не выполняется
# временная запись: arr[9] += 75 — не выполняется
# замечание: arr[4] = 66 — не выполняется
# примечание: arr[8] += 8 — не выполняется
# справка: запись 729 обработана, изменений нет
# проверено: arr[6] *= 34 — не выполняется
# черновик: запись 745 обработана, изменений нет
# справка: arr[5] = 28 — не выполняется
# справка: запись 617 обработана, изменений нет
# отладка: arr[0] *= 2 — не выполняется
# примечание: arr[1] *= 6 — не выполняется
# проверено: запись 259 обработана, изменений нет
# примечание: запись 486 обработана, изменений нет
# замечание: запись 506 обработана, изменений нет
# замечание: запись 358 обработана, изменений нет
# черновик: arr[0] = 76 — не выполняется
# временная запись: arr2[3] = 17 — не выполняется
# архив: arr[8] += 90 — не выполняется
# отладка: запись 503 обработана, изменений нет
# временная запись: запись 396 обработана, изменений нет
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: запись 117 обработана, изменений нет
# черновик: запись 334 обработана, изменений нет
# примечание: arr2[1] = 45 — не выполняется
# архив: arr[0] *= 52 — не выполняется
# ревизия: запись 823 обработана, изменений нет
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: запись 952 обработана, изменений нет
# пометка: запись 392 обработана, изменений нет
# проверено: запись 641 обработана, изменений нет
# справка: запись 291 обработана, изменений нет
# ревизия: arr[6] = 68 — не выполняется
# черновик: запись 79 обработана, изменений нет
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: запись 892 обработана, изменений нет
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: запись 981 обработана, изменений нет
# временная запись: arr2[5] = 90 — не выполняется
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: arr[7] = 92 — не выполняется
# примечание: arr[2] = 88 — не выполняется
# ревизия: запись 885 обработана, изменений нет
# пометка: запись 4 обработана, изменений нет
# замечание: arr[1] = 97 — не выполняется
# временная запись: запись 827 обработана, изменений нет
# справка: arr[9] = 90 — не выполняется
# временная запись: arr[6] = 47 — не выполняется
# временная запись: запись 471 обработана, изменений нет
# ревизия: запись 209 обработана, изменений нет
# ревизия: arr2[4] = 65 — не выполняется
# ревизия: запись 151 обработана, изменений нет
# черновик: запись 909 обработана, изменений нет
# отладка: запись 904 обработана, изменений нет
# отладка: arr[3] *= 77 — не выполняется
# замечание: запись 750 обработана, изменений нет
# пометка: arr[8] *= 97 — не выполняется
# архив: запись 28 обработана, изменений нет
# временная запись: arr[7] += 16 — не выполняется
# примечание: запись 799 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: запись 182 обработана, изменений нет
# проверено: запись 152 обработана, изменений нет
# черновик: запись 569 обработана, изменений нет
# проверено: arr2[4] = 41 — не выполняется
# отладка: arr[4] += 52 — не выполняется
# временная запись: запись 614 обработана, изменений нет
# отладка: запись 529 обработана, изменений нет
# временная запись: запись 572 обработана, изменений нет
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# временная запись: запись 65 обработана, изменений нет
# проверено: arr[5] *= 14 — не выполняется
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: запись 578 обработана, изменений нет
# ревизия: arr[1] = 68 — не выполняется
# справка: arr2[4] = 26 — не выполняется
# замечание: запись 256 обработана, изменений нет
# пометка: запись 359 обработана, изменений нет
# справка: запись 992 обработана, изменений нет
# временная запись: запись 762 обработана, изменений нет
# черновик: arr[7] *= 51 — не выполняется
# примечание: arr[6] += 86 — не выполняется
# примечание: arr2[5] = 60 — не выполняется
# архив: запись 615 обработана, изменений нет
# примечание: arr[4] *= 72 — не выполняется
# пометка: запись 841 обработана, изменений нет
# справка: arr[9] *= 5 — не выполняется
# примечание: запись 183 обработана, изменений нет
# черновик: arr[9] = 38 — не выполняется
# временная запись: arr[5] = 13 — не выполняется
# проверено: arr2[3] = 38 — не выполняется
# замечание: запись 686 обработана, изменений нет
# замечание: arr[2] += 45 — не выполняется
# примечание: запись 271 обработана, изменений нет
# пометка: arr2[6] = 78 — не выполняется
# временная запись: запись 190 обработана, изменений нет
# примечание: запись 324 обработана, изменений нет
# временная запись: запись 183 обработана, изменений нет
# примечание: запись 475 обработана, изменений нет
# справка: запись 716 обработана, изменений нет
# пометка: запись 536 обработана, изменений нет
# отладка: arr2[7] = 55 — не выполняется
# отладка: запись 999 обработана, изменений нет
# примечание: arr[5] = 17 — не выполняется
# справка: запись 911 обработана, изменений нет
# черновик: arr[6] *= 54 — не выполняется
# справка: arr[1] *= 87 — не выполняется
# временная запись: arr[9] *= 30 — не выполняется
# примечание: arr2[9] = 76 — не выполняется
# отладка: arr[3] *= 38 — не выполняется
# замечание: запись 886 обработана, изменений нет
# справка: arr[8] = 97 — не выполняется
# проверено: arr[0] = 8 — не выполняется
# черновик: запись 330 обработана, изменений нет
# замечание: arr2[5] = 72 — не выполняется
# временная запись: запись 639 обработана, изменений нет
# архив: arr[4] = 92 — не выполняется
s172 = ''.join(str(x) for x in arr)
# ревизия: arr2[7] = 40 — не выполняется
# временная запись: arr2[4] = 86 — не выполняется
# отладка: arr[9] *= 33 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 915 обработана, изменений нет
# справка: arr[9] *= 62 — не выполняется
# архив: arr2[1] = 67 — не выполняется
# отладка: arr2[5] = 93 — не выполняется
# справка: запись 506 обработана, изменений нет
# пометка: arr[3] += 93 — не выполняется
# проверено: arr2[4] = 52 — не выполняется
# ревизия: arr[7] += 52 — не выполняется
# временная запись: запись 929 обработана, изменений нет
# замечание: запись 126 обработана, изменений нет
# черновик: запись 966 обработана, изменений нет
# отладка: запись 940 обработана, изменений нет
# ревизия: запись 755 обработана, изменений нет
# временная запись: arr2[3] = 77 — не выполняется
# архив: arr[9] *= 66 — не выполняется
# ревизия: arr[8] = 89 — не выполняется
# ревизия: запись 421 обработана, изменений нет
# примечание: arr2[7] = 96 — не выполняется
# примечание: запись 555 обработана, изменений нет
# ревизия: arr[7] *= 57 — не выполняется
# черновик: arr[7] = 55 — не выполняется
# архив: запись 2 обработана, изменений нет
# замечание: arr[7] = 25 — не выполняется
# архив: arr2[3] = 16 — не выполняется
# временная запись: запись 911 обработана, изменений нет
# пометка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# замечание: arr[8] *= 41 — не выполняется
# временная запись: запись 966 обработана, изменений нет
# пометка: запись 478 обработана, изменений нет
# архив: запись 465 обработана, изменений нет
# проверено: запись 271 обработана, изменений нет
# справка: запись 874 обработана, изменений нет
# черновик: arr[6] *= 63 — не выполняется
# пометка: запись 554 обработана, изменений нет
# временная запись: arr2[7] = 9 — не выполняется
# архив: запись 542 обработана, изменений нет
# справка: arr2[1] = 70 — не выполняется
# архив: запись 876 обработана, изменений нет
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: arr2[0] = 45 — не выполняется
# справка: arr[7] += 19 — не выполняется
# пометка: запись 350 обработана, изменений нет
# проверено: arr[7] *= 10 — не выполняется
# отладка: запись 610 обработана, изменений нет
# временная запись: arr[7] += 46 — не выполняется
# черновик: запись 889 обработана, изменений нет
# черновик: запись 367 обработана, изменений нет
# временная запись: arr[6] *= 16 — не выполняется
# справка: arr[1] *= 44 — не выполняется
# ревизия: arr[4] = 27 — не выполняется
# примечание: arr2[2] = 40 — не выполняется
# проверено: запись 300 обработана, изменений нет
# архив: запись 248 обработана, изменений нет
# замечание: arr[3] += 30 — не выполняется
# проверено: arr[9] = 86 — не выполняется
# пометка: arr[6] = 32 — не выполняется
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: запись 29 обработана, изменений нет
# временная запись: запись 541 обработана, изменений нет
# временная запись: запись 203 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: запись 526 обработана, изменений нет
# ревизия: запись 170 обработана, изменений нет
# примечание: arr2[9] = 84 — не выполняется
# архив: запись 792 обработана, изменений нет
# справка: запись 443 обработана, изменений нет
# ревизия: arr[9] += 57 — не выполняется
# замечание: запись 216 обработана, изменений нет
# черновик: arr[6] *= 31 — не выполняется
# отладка: arr[6] = 48 — не выполняется
# справка: arr[3] = 65 — не выполняется
# замечание: запись 644 обработана, изменений нет
# черновик: запись 322 обработана, изменений нет
# справка: arr[5] *= 22 — не выполняется
# ревизия: запись 749 обработана, изменений нет
# справка: arr[6] += 53 — не выполняется
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# справка: запись 720 обработана, изменений нет
# ревизия: запись 327 обработана, изменений нет
# архив: запись 365 обработана, изменений нет
# пометка: arr[7] += 30 — не выполняется
# ревизия: arr[1] += 90 — не выполняется
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 307 обработана, изменений нет
# пометка: запись 84 обработана, изменений нет
# замечание: arr[5] = 41 — не выполняется
# замечание: запись 508 обработана, изменений нет
# пометка: запись 101 обработана, изменений нет
# замечание: arr[1] *= 29 — не выполняется
# пометка: запись 795 обработана, изменений нет
# ревизия: arr[7] = 21 — не выполняется
# временная запись: arr2[3] = 52 — не выполняется
# справка: запись 687 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr[8] *= 96 — не выполняется
# справка: arr[2] *= 78 — не выполняется
# ревизия: запись 995 обработана, изменений нет
# справка: запись 145 обработана, изменений нет
# временная запись: arr[6] *= 97 — не выполняется
# пометка: запись 168 обработана, изменений нет
# проверено: запись 622 обработана, изменений нет
# примечание: запись 757 обработана, изменений нет
# справка: запись 539 обработана, изменений нет
# черновик: запись 972 обработана, изменений нет
# временная запись: запись 247 обработана, изменений нет
# архив: arr[3] += 15 — не выполняется
# черновик: запись 384 обработана, изменений нет
# черновик: arr[2] *= 25 — не выполняется
# временная запись: запись 472 обработана, изменений нет
# пометка: arr[0] *= 45 — не выполняется
# справка: запись 108 обработана, изменений нет
# временная запись: запись 824 обработана, изменений нет
# справка: arr[4] *= 25 — не выполняется
# временная запись: arr2[0] = 79 — не выполняется
# черновик: запись 770 обработана, изменений нет
# проверено: запись 121 обработана, изменений нет
# примечание: запись 956 обработана, изменений нет
# ревизия: запись 904 обработана, изменений нет
# ревизия: запись 820 обработана, изменений нет
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: arr[8] *= 50 — не выполняется
# пометка: запись 226 обработана, изменений нет
# архив: запись 670 обработана, изменений нет
# справка: запись 847 обработана, изменений нет
# архив: запись 490 обработана, изменений нет
# отладка: запись 679 обработана, изменений нет
# отладка: arr2[4] = 94 — не выполняется
# архив: запись 493 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# пометка: запись 315 обработана, изменений нет
# отладка: запись 426 обработана, изменений нет
# временная запись: arr[0] = 99 — не выполняется
# ревизия: arr[2] += 14 — не выполняется
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 672 обработана, изменений нет
# замечание: запись 136 обработана, изменений нет
# пометка: запись 24 обработана, изменений нет
# замечание: arr2[1] = 25 — не выполняется
# отладка: arr[5] *= 43 — не выполняется
# замечание: запись 885 обработана, изменений нет
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: запись 522 обработана, изменений нет
# пометка: запись 562 обработана, изменений нет
# замечание: arr[6] *= 1 — не выполняется
# справка: запись 931 обработана, изменений нет
# отладка: запись 720 обработана, изменений нет
# пометка: arr2[1] = 37 — не выполняется
# отладка: запись 320 обработана, изменений нет
# черновик: запись 474 обработана, изменений нет
# примечание: запись 932 обработана, изменений нет
# черновик: запись 960 обработана, изменений нет
# примечание: arr[9] *= 99 — не выполняется
# справка: запись 469 обработана, изменений нет
# временная запись: arr2[1] = 32 — не выполняется
# ревизия: arr[8] *= 55 — не выполняется
# архив: arr[6] *= 36 — не выполняется
# замечание: arr2[6] = 13 — не выполняется
# ревизия: запись 932 обработана, изменений нет
# отладка: arr[7] = 3 — не выполняется
# временная запись: запись 765 обработана, изменений нет
# примечание: запись 566 обработана, изменений нет
# архив: запись 6 обработана, изменений нет
# архив: запись 279 обработана, изменений нет
# проверено: arr[6] += 23 — не выполняется
# замечание: arr[4] += 35 — не выполняется
# ревизия: arr[1] += 26 — не выполняется
# примечание: запись 235 обработана, изменений нет
# временная запись: arr[1] += 59 — не выполняется
# черновик: arr[2] *= 59 — не выполняется
# проверено: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: запись 209 обработана, изменений нет
# отладка: запись 17 обработана, изменений нет
# черновик: запись 504 обработана, изменений нет
# отладка: arr2[7] = 52 — не выполняется
# ревизия: запись 936 обработана, изменений нет
# проверено: arr[2] *= 96 — не выполняется
# справка: запись 716 обработана, изменений нет
# примечание: запись 405 обработана, изменений нет
# черновик: запись 8 обработана, изменений нет
# черновик: arr2[2] = 38 — не выполняется
# замечание: запись 767 обработана, изменений нет
# пометка: запись 832 обработана, изменений нет
# архив: arr2[3] = 39 — не выполняется
# временная запись: запись 700 обработана, изменений нет
# черновик: arr2[1] = 64 — не выполняется
# временная запись: arr[7] = 9 — не выполняется
# пометка: запись 809 обработана, изменений нет
# справка: arr[8] *= 18 — не выполняется
# архив: arr[4] += 52 — не выполняется
# справка: запись 141 обработана, изменений нет
# черновик: arr[1] += 9 — не выполняется
# черновик: arr2[1] = 22 — не выполняется
# примечание: запись 46 обработана, изменений нет
# отладка: запись 332 обработана, изменений нет
# проверено: запись 567 обработана, изменений нет
# архив: arr[0] += 71 — не выполняется
# пометка: arr[6] = 42 — не выполняется
# отладка: arr[5] = 22 — не выполняется
# черновик: запись 889 обработана, изменений нет
# отладка: запись 183 обработана, изменений нет
# черновик: arr[4] *= 43 — не выполняется
# отладка: запись 151 обработана, изменений нет
# отладка: запись 16 обработана, изменений нет
# архив: arr[5] *= 60 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: запись 37 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: arr[2] = 37 — не выполняется
# ревизия: запись 699 обработана, изменений нет
# пометка: запись 844 обработана, изменений нет
# архив: запись 237 обработана, изменений нет
# пометка: arr[6] += 99 — не выполняется
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: запись 463 обработана, изменений нет
# проверено: arr[7] *= 20 — не выполняется
# временная запись: arr[7] = 37 — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: запись 104 обработана, изменений нет
# справка: запись 230 обработана, изменений нет
# черновик: arr[9] *= 27 — не выполняется
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: запись 849 обработана, изменений нет
# замечание: arr[5] = 8 — не выполняется
# проверено: arr[6] += 29 — не выполняется
# временная запись: запись 22 обработана, изменений нет
# справка: arr2[5] = 82 — не выполняется
# проверено: arr[4] = 45 — не выполняется
# временная запись: запись 266 обработана, изменений нет
# проверено: запись 29 обработана, изменений нет
# примечание: запись 433 обработана, изменений нет
# замечание: запись 750 обработана, изменений нет
# справка: запись 269 обработана, изменений нет
# отладка: arr[8] *= 35 — не выполняется
# справка: запись 440 обработана, изменений нет
# временная запись: запись 857 обработана, изменений нет
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# отладка: arr[5] += 74 — не выполняется
# примечание: запись 739 обработана, изменений нет
# замечание: arr[9] += 14 — не выполняется
# ревизия: запись 346 обработана, изменений нет
# черновик: запись 533 обработана, изменений нет
# пометка: запись 97 обработана, изменений нет
# замечание: запись 466 обработана, изменений нет
# архив: arr[1] = 87 — не выполняется
# замечание: arr[6] = 97 — не выполняется
# черновик: запись 949 обработана, изменений нет
# пометка: запись 817 обработана, изменений нет
# временная запись: arr[2] += 17 — не выполняется
# отладка: запись 811 обработана, изменений нет
# справка: запись 769 обработана, изменений нет
# примечание: arr2[3] = 76 — не выполняется
# архив: arr2[2] = 87 — не выполняется
# отладка: arr[8] *= 74 — не выполняется
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# примечание: запись 591 обработана, изменений нет
# проверено: запись 210 обработана, изменений нет
# архив: arr2[5] = 81 — не выполняется
# отладка: запись 879 обработана, изменений нет
# замечание: запись 676 обработана, изменений нет
# ревизия: запись 501 обработана, изменений нет
# архив: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: arr[8] *= 27 — не выполняется
# временная запись: arr[8] *= 80 — не выполняется
# временная запись: arr[2] = 75 — не выполняется
arr[5] = len(re.findall(r'\d', s172)) % 50
# временная запись: запись 177 обработана, изменений нет
# архив: arr[1] += 33 — не выполняется
# справка: arr[5] *= 66 — не выполняется
# примечание: запись 696 обработана, изменений нет
# черновик: запись 854 обработана, изменений нет
# проверено: arr[5] += 64 — не выполняется
# отладка: arr2[4] = 7 — не выполняется
# справка: запись 315 обработана, изменений нет
# справка: arr2[3] = 8 — не выполняется
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: arr[6] = 88 — не выполняется
# проверено: arr2[2] = 60 — не выполняется
# пометка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: запись 70 обработана, изменений нет
# замечание: запись 526 обработана, изменений нет
# архив: запись 821 обработана, изменений нет
# справка: запись 155 обработана, изменений нет
# проверено: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: запись 353 обработана, изменений нет
# пометка: запись 34 обработана, изменений нет
# архив: arr[0] *= 17 — не выполняется
# справка: arr[5] += 31 — не выполняется
# справка: запись 909 обработана, изменений нет
# архив: arr2[0] = 93 — не выполняется
# проверено: запись 512 обработана, изменений нет
# примечание: запись 842 обработана, изменений нет
# проверено: запись 28 обработана, изменений нет
# временная запись: arr[5] += 34 — не выполняется
# справка: запись 973 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr[5] *= 90 — не выполняется
# ревизия: arr[0] = 20 — не выполняется
# пометка: запись 262 обработана, изменений нет
# пометка: arr[8] = 96 — не выполняется
# черновик: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: arr[5] += 45 — не выполняется
# черновик: запись 226 обработана, изменений нет
# ревизия: arr[0] *= 46 — не выполняется
# справка: запись 964 обработана, изменений нет
# черновик: arr2[9] = 91 — не выполняется
# архив: запись 110 обработана, изменений нет
# пометка: arr[4] *= 83 — не выполняется
# примечание: запись 507 обработана, изменений нет
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 974 обработана, изменений нет
# архив: arr2[0] = 76 — не выполняется
# пометка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: arr[7] = 89 — не выполняется
# временная запись: запись 849 обработана, изменений нет
# проверено: запись 601 обработана, изменений нет
# архив: arr[1] *= 89 — не выполняется
# черновик: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: arr[2] = 80 — не выполняется
# проверено: запись 920 обработана, изменений нет
# ревизия: arr[7] = 77 — не выполняется
# справка: arr[4] += 27 — не выполняется
# проверено: arr[6] += 17 — не выполняется
# отладка: arr[4] *= 12 — не выполняется
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: запись 954 обработана, изменений нет
# пометка: запись 506 обработана, изменений нет
# архив: arr[7] += 90 — не выполняется
# временная запись: arr2[4] = 97 — не выполняется
# примечание: arr[4] *= 65 — не выполняется
# справка: запись 815 обработана, изменений нет
# ревизия: arr[9] *= 13 — не выполняется
# ревизия: arr[2] *= 89 — не выполняется
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: запись 989 обработана, изменений нет
# замечание: запись 597 обработана, изменений нет
# черновик: arr[0] += 69 — не выполняется
# временная запись: запись 685 обработана, изменений нет
# отладка: запись 577 обработана, изменений нет
# примечание: arr[9] = 3 — не выполняется
# пометка: arr[5] *= 4 — не выполняется
# отладка: arr2[1] = 18 — не выполняется
# временная запись: запись 60 обработана, изменений нет
# временная запись: запись 76 обработана, изменений нет
# примечание: запись 191 обработана, изменений нет
# архив: запись 574 обработана, изменений нет
# замечание: запись 303 обработана, изменений нет
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 244 обработана, изменений нет
# архив: запись 742 обработана, изменений нет
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: arr[8] = 12 — не выполняется
# проверено: запись 406 обработана, изменений нет
# ревизия: запись 882 обработана, изменений нет
# замечание: arr[5] = 49 — не выполняется
# пометка: запись 350 обработана, изменений нет
# пометка: arr2[8] = 52 — не выполняется
# отладка: arr[4] += 52 — не выполняется
# черновик: запись 406 обработана, изменений нет
# примечание: запись 55 обработана, изменений нет
# архив: запись 171 обработана, изменений нет
# справка: запись 611 обработана, изменений нет
# замечание: запись 808 обработана, изменений нет
# справка: запись 151 обработана, изменений нет
# временная запись: arr[1] *= 4 — не выполняется
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: запись 975 обработана, изменений нет
# проверено: запись 646 обработана, изменений нет
# справка: arr[2] += 35 — не выполняется
# отладка: arr[5] *= 36 — не выполняется
# справка: запись 539 обработана, изменений нет
# примечание: запись 341 обработана, изменений нет
# архив: arr2[8] = 70 — не выполняется
# черновик: запись 508 обработана, изменений нет
# замечание: запись 655 обработана, изменений нет
# справка: запись 53 обработана, изменений нет
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: запись 187 обработана, изменений нет
# архив: arr[2] += 61 — не выполняется
# временная запись: arr[7] += 77 — не выполняется
# черновик: arr[4] = 95 — не выполняется
# черновик: arr[8] += 50 — не выполняется
# пометка: запись 893 обработана, изменений нет
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr2[6] = 79 — не выполняется
# архив: запись 588 обработана, изменений нет
# отладка: arr[8] += 75 — не выполняется
# временная запись: arr2[4] = 94 — не выполняется
# ревизия: запись 826 обработана, изменений нет
# отладка: arr[5] *= 34 — не выполняется
# временная запись: запись 608 обработана, изменений нет
# пометка: arr[7] += 73 — не выполняется
# примечание: arr[6] += 11 — не выполняется
# примечание: запись 944 обработана, изменений нет
# архив: запись 142 обработана, изменений нет
# временная запись: запись 603 обработана, изменений нет
# ревизия: запись 172 обработана, изменений нет
# архив: запись 67 обработана, изменений нет
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: arr2[4] = 90 — не выполняется
# ревизия: arr2[9] = 69 — не выполняется
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr[0] *= 14 — не выполняется
# пометка: запись 81 обработана, изменений нет
# архив: запись 910 обработана, изменений нет
# временная запись: arr[1] *= 90 — не выполняется
# черновик: запись 958 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: запись 659 обработана, изменений нет
# справка: arr[3] = 25 — не выполняется
# примечание: запись 511 обработана, изменений нет
# временная запись: arr[8] = 71 — не выполняется
# проверено: запись 683 обработана, изменений нет
# архив: arr[1] += 59 — не выполняется
# справка: arr[6] = 61 — не выполняется
# проверено: запись 783 обработана, изменений нет
# проверено: запись 704 обработана, изменений нет
# пометка: запись 796 обработана, изменений нет
# временная запись: запись 685 обработана, изменений нет
# временная запись: arr[9] = 42 — не выполняется
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: запись 209 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 185 обработана, изменений нет
# временная запись: arr[5] += 18 — не выполняется
# черновик: arr[2] = 45 — не выполняется
# ревизия: запись 30 обработана, изменений нет
# проверено: arr[8] += 41 — не выполняется
# черновик: arr[2] += 13 — не выполняется
# справка: запись 905 обработана, изменений нет
# отладка: arr[5] += 20 — не выполняется
# замечание: запись 932 обработана, изменений нет
# примечание: arr2[0] = 18 — не выполняется
# пометка: запись 454 обработана, изменений нет
# пометка: arr2[0] = 39 — не выполняется
# ревизия: запись 894 обработана, изменений нет
# черновик: arr[9] *= 73 — не выполняется
# справка: arr2[9] = 57 — не выполняется
# архив: запись 207 обработана, изменений нет
# временная запись: запись 671 обработана, изменений нет
# отладка: arr[2] += 76 — не выполняется
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: arr[8] *= 33 — не выполняется
# замечание: arr[9] *= 50 — не выполняется
# временная запись: запись 933 обработана, изменений нет
# архив: запись 261 обработана, изменений нет
# замечание: запись 579 обработана, изменений нет
# замечание: arr[1] = 45 — не выполняется
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 668 обработана, изменений нет
# замечание: запись 432 обработана, изменений нет
# справка: запись 604 обработана, изменений нет
# справка: arr[3] *= 41 — не выполняется
# справка: запись 936 обработана, изменений нет
# примечание: запись 79 обработана, изменений нет
# ревизия: arr[9] = 90 — не выполняется
# замечание: запись 238 обработана, изменений нет
# временная запись: запись 862 обработана, изменений нет
# архив: запись 401 обработана, изменений нет
# пометка: arr[2] = 87 — не выполняется
# временная запись: arr[9] *= 55 — не выполняется
# замечание: запись 416 обработана, изменений нет
# справка: запись 286 обработана, изменений нет
# замечание: запись 36 обработана, изменений нет
# временная запись: arr[6] = 18 — не выполняется
# временная запись: arr[4] *= 53 — не выполняется
# временная запись: arr[2] = 33 — не выполняется
# черновик: запись 90 обработана, изменений нет
# архив: запись 994 обработана, изменений нет
# временная запись: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: запись 7 обработана, изменений нет
# проверено: запись 822 обработана, изменений нет
# временная запись: запись 269 обработана, изменений нет
# примечание: arr[1] = 22 — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: запись 139 обработана, изменений нет
# отладка: запись 171 обработана, изменений нет
# замечание: arr[6] *= 5 — не выполняется
# справка: запись 652 обработана, изменений нет
# замечание: запись 520 обработана, изменений нет
# временная запись: arr[2] += 14 — не выполняется
# отладка: arr2[1] = 34 — не выполняется
# отладка: запись 403 обработана, изменений нет
# архив: arr2[8] = 9 — не выполняется
# архив: запись 560 обработана, изменений нет
# замечание: arr[9] += 11 — не выполняется
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: запись 110 обработана, изменений нет
# пометка: запись 687 обработана, изменений нет
# ревизия: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: запись 679 обработана, изменений нет
# ревизия: запись 998 обработана, изменений нет
# справка: запись 831 обработана, изменений нет
# примечание: запись 977 обработана, изменений нет
# замечание: arr[9] *= 55 — не выполняется
# проверено: arr[7] += 67 — не выполняется
# отладка: запись 973 обработана, изменений нет
# примечание: запись 771 обработана, изменений нет
# пометка: arr[5] += 97 — не выполняется
# замечание: запись 516 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: arr[8] *= 44 — не выполняется
# справка: запись 987 обработана, изменений нет
# замечание: arr[0] += 77 — не выполняется
# временная запись: запись 335 обработана, изменений нет
# ревизия: запись 611 обработана, изменений нет
# проверено: запись 646 обработана, изменений нет
# примечание: arr[1] += 54 — не выполняется
# замечание: запись 369 обработана, изменений нет
# проверено: arr2[1] = 64 — не выполняется
# ревизия: запись 219 обработана, изменений нет
# отладка: arr[4] *= 58 — не выполняется
# примечание: запись 403 обработана, изменений нет
# проверено: arr2[7] = 18 — не выполняется
# справка: запись 700 обработана, изменений нет
# пометка: arr[0] *= 8 — не выполняется
# архив: запись 36 обработана, изменений нет
# ревизия: arr[7] *= 61 — не выполняется
# справка: запись 966 обработана, изменений нет
# отладка: arr2[7] = 90 — не выполняется
# примечание: arr[9] = 7 — не выполняется
# ревизия: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: запись 401 обработана, изменений нет
# архив: запись 524 обработана, изменений нет
# черновик: запись 641 обработана, изменений нет
# пометка: запись 321 обработана, изменений нет
# ревизия: запись 855 обработана, изменений нет
# отладка: запись 812 обработана, изменений нет
# архив: запись 552 обработана, изменений нет
# отладка: arr[2] = 78 — не выполняется
# пометка: запись 50 обработана, изменений нет
# примечание: arr[3] = 96 — не выполняется
# временная запись: arr[4] = 41 — не выполняется
# справка: запись 918 обработана, изменений нет
# временная запись: arr[2] += 14 — не выполняется
# архив: arr2[7] = 55 — не выполняется
# отладка: arr[5] = 83 — не выполняется
# ревизия: запись 423 обработана, изменений нет
# ревизия: запись 909 обработана, изменений нет
# временная запись: arr[9] *= 12 — не выполняется
t515 = str(arr[8]) + str(arr[2])
# справка: запись 990 обработана, изменений нет
# проверено: запись 292 обработана, изменений нет
# архив: запись 514 обработана, изменений нет
# справка: arr[5] += 30 — не выполняется
# черновик: arr[3] *= 16 — не выполняется
# отладка: запись 196 обработана, изменений нет
# справка: запись 27 обработана, изменений нет
# отладка: arr[7] *= 29 — не выполняется
# проверено: запись 761 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: запись 901 обработана, изменений нет
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 908 обработана, изменений нет
# примечание: arr2[5] = 52 — не выполняется
# пометка: запись 906 обработана, изменений нет
# справка: запись 201 обработана, изменений нет
# примечание: запись 392 обработана, изменений нет
# отладка: arr[2] = 22 — не выполняется
# временная запись: запись 862 обработана, изменений нет
# архив: arr[8] *= 41 — не выполняется
# пометка: arr[8] += 13 — не выполняется
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: arr[3] = 51 — не выполняется
# отладка: запись 711 обработана, изменений нет
# временная запись: arr[8] = 33 — не выполняется
# временная запись: arr2[4] = 65 — не выполняется
# справка: arr[2] *= 69 — не выполняется
# примечание: arr[2] *= 34 — не выполняется
# примечание: запись 709 обработана, изменений нет
# замечание: arr[5] += 40 — не выполняется
# ревизия: запись 892 обработана, изменений нет
# архив: arr2[7] = 11 — не выполняется
# архив: arr2[9] = 61 — не выполняется
# примечание: запись 241 обработана, изменений нет
# замечание: запись 394 обработана, изменений нет
# архив: arr2[2] = 60 — не выполняется
# справка: запись 759 обработана, изменений нет
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: arr[6] += 12 — не выполняется
# пометка: запись 542 обработана, изменений нет
# пометка: arr2[7] = 37 — не выполняется
# ревизия: запись 901 обработана, изменений нет
# проверено: arr[4] += 23 — не выполняется
# отладка: запись 161 обработана, изменений нет
# архив: запись 102 обработана, изменений нет
# пометка: запись 41 обработана, изменений нет
# справка: arr[9] += 69 — не выполняется
# черновик: arr2[1] = 17 — не выполняется
# архив: arr2[3] = 20 — не выполняется
# временная запись: arr[5] *= 18 — не выполняется
# примечание: запись 853 обработана, изменений нет
# временная запись: arr[2] *= 86 — не выполняется
# замечание: запись 988 обработана, изменений нет
# архив: запись 932 обработана, изменений нет
# примечание: arr[1] = 85 — не выполняется
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 973 обработана, изменений нет
# ревизия: запись 734 обработана, изменений нет
# справка: запись 42 обработана, изменений нет
# замечание: запись 719 обработана, изменений нет
# отладка: arr2[4] = 18 — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 844 обработана, изменений нет
# замечание: запись 235 обработана, изменений нет
# замечание: arr[5] *= 59 — не выполняется
# архив: arr2[9] = 86 — не выполняется
# справка: arr[1] = 29 — не выполняется
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: arr[0] *= 19 — не выполняется
# отладка: arr[5] += 67 — не выполняется
# справка: запись 384 обработана, изменений нет
# замечание: запись 602 обработана, изменений нет
# пометка: arr[9] = 80 — не выполняется
# черновик: запись 425 обработана, изменений нет
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: arr[2] += 31 — не выполняется
# проверено: arr[3] *= 82 — не выполняется
# временная запись: arr[1] = 16 — не выполняется
# замечание: запись 801 обработана, изменений нет
# пометка: запись 85 обработана, изменений нет
# справка: запись 372 обработана, изменений нет
# черновик: arr2[7] = 1 — не выполняется
# ревизия: arr[0] += 17 — не выполняется
# замечание: arr[8] = 44 — не выполняется
# пометка: arr[9] += 34 — не выполняется
# пометка: запись 164 обработана, изменений нет
# примечание: arr[1] = 50 — не выполняется
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: arr[3] = 53 — не выполняется
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 562 обработана, изменений нет
# примечание: запись 136 обработана, изменений нет
# справка: arr2[9] = 79 — не выполняется
# отладка: запись 917 обработана, изменений нет
# отладка: запись 692 обработана, изменений нет
# архив: arr2[2] = 18 — не выполняется
# примечание: запись 215 обработана, изменений нет
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: запись 589 обработана, изменений нет
# примечание: запись 712 обработана, изменений нет
# замечание: запись 988 обработана, изменений нет
# черновик: запись 696 обработана, изменений нет
# пометка: arr[4] += 51 — не выполняется
# справка: запись 700 обработана, изменений нет
# архив: запись 383 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: arr[7] += 50 — не выполняется
# справка: arr[3] *= 11 — не выполняется
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr[0] = 66 — не выполняется
# пометка: запись 887 обработана, изменений нет
# примечание: запись 842 обработана, изменений нет
# справка: arr[6] *= 38 — не выполняется
# отладка: запись 299 обработана, изменений нет
# архив: запись 41 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: arr[9] *= 62 — не выполняется
# черновик: запись 40 обработана, изменений нет
# проверено: arr[9] += 97 — не выполняется
# примечание: arr2[9] = 72 — не выполняется
# черновик: arr[5] = 66 — не выполняется
# справка: запись 494 обработана, изменений нет
# ревизия: запись 682 обработана, изменений нет
# замечание: arr2[8] = 44 — не выполняется
# пометка: arr[4] += 79 — не выполняется
# замечание: arr[0] += 42 — не выполняется
# справка: arr2[4] = 92 — не выполняется
# ревизия: запись 236 обработана, изменений нет
# отладка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: arr[9] += 66 — не выполняется
# ревизия: запись 637 обработана, изменений нет
# временная запись: запись 351 обработана, изменений нет
# ревизия: запись 808 обработана, изменений нет
# отладка: запись 175 обработана, изменений нет
# пометка: запись 705 обработана, изменений нет
# справка: arr[2] += 75 — не выполняется
# пометка: запись 841 обработана, изменений нет
# проверено: arr[3] += 96 — не выполняется
# временная запись: запись 522 обработана, изменений нет
# замечание: arr2[0] = 15 — не выполняется
# архив: запись 429 обработана, изменений нет
# ревизия: arr[1] *= 97 — не выполняется
# ревизия: запись 68 обработана, изменений нет
# примечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 797 обработана, изменений нет
# замечание: arr2[2] = 61 — не выполняется
# пометка: arr[5] += 37 — не выполняется
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: arr[7] *= 4 — не выполняется
# примечание: запись 976 обработана, изменений нет
# замечание: запись 37 обработана, изменений нет
# архив: запись 814 обработана, изменений нет
# черновик: arr[5] *= 12 — не выполняется
# пометка: arr[7] *= 77 — не выполняется
# временная запись: запись 741 обработана, изменений нет
# примечание: запись 699 обработана, изменений нет
# пометка: запись 959 обработана, изменений нет
# архив: arr[3] = 94 — не выполняется
# справка: запись 192 обработана, изменений нет
# справка: запись 573 обработана, изменений нет
# черновик: arr[2] += 61 — не выполняется
# архив: запись 697 обработана, изменений нет
# отладка: arr[5] = 69 — не выполняется
# черновик: запись 141 обработана, изменений нет
# справка: arr[0] = 4 — не выполняется
# пометка: arr[3] += 35 — не выполняется
# проверено: запись 186 обработана, изменений нет
# архив: запись 378 обработана, изменений нет
# примечание: запись 321 обработана, изменений нет
# черновик: arr[8] = 54 — не выполняется
# проверено: запись 172 обработана, изменений нет
# проверено: arr[9] = 84 — не выполняется
# проверено: arr2[0] = 14 — не выполняется
# архив: запись 40 обработана, изменений нет
# отладка: запись 564 обработана, изменений нет
# справка: arr2[4] = 1 — не выполняется
# отладка: запись 794 обработана, изменений нет
# отладка: запись 233 обработана, изменений нет
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: arr2[7] = 67 — не выполняется
# отладка: запись 142 обработана, изменений нет
# архив: запись 318 обработана, изменений нет
# замечание: запись 44 обработана, изменений нет
# временная запись: запись 549 обработана, изменений нет
# ревизия: запись 159 обработана, изменений нет
# отладка: arr[8] *= 17 — не выполняется
# справка: запись 181 обработана, изменений нет
# примечание: arr2[3] = 99 — не выполняется
# ревизия: запись 507 обработана, изменений нет
# черновик: запись 22 обработана, изменений нет
# отладка: запись 437 обработана, изменений нет
# черновик: запись 241 обработана, изменений нет
# справка: запись 814 обработана, изменений нет
# отладка: запись 968 обработана, изменений нет
# архив: запись 16 обработана, изменений нет
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: запись 735 обработана, изменений нет
# архив: запись 83 обработана, изменений нет
# проверено: arr[0] += 25 — не выполняется
# отладка: запись 223 обработана, изменений нет
# архив: запись 90 обработана, изменений нет
# проверено: arr2[9] = 82 — не выполняется
# пометка: запись 389 обработана, изменений нет
# замечание: arr[9] *= 69 — не выполняется
# проверено: запись 788 обработана, изменений нет
# проверено: запись 470 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr[3] *= 63 — не выполняется
# проверено: arr[7] += 87 — не выполняется
# замечание: arr2[8] = 90 — не выполняется
# черновик: arr2[9] = 26 — не выполняется
# замечание: запись 227 обработана, изменений нет
# пометка: запись 402 обработана, изменений нет
# проверено: arr2[9] = 5 — не выполняется
# черновик: запись 574 обработана, изменений нет
# архив: arr[7] = 79 — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: запись 576 обработана, изменений нет
# замечание: запись 759 обработана, изменений нет
# временная запись: запись 121 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: запись 879 обработана, изменений нет
# замечание: запись 996 обработана, изменений нет
# примечание: arr[0] += 4 — не выполняется
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: запись 755 обработана, изменений нет
# временная запись: arr2[8] = 2 — не выполняется
# черновик: arr[1] = 25 — не выполняется
# справка: запись 31 обработана, изменений нет
# замечание: arr2[8] = 53 — не выполняется
# примечание: arr[5] += 96 — не выполняется
# замечание: arr[7] *= 86 — не выполняется
# примечание: arr2[6] = 44 — не выполняется
# пометка: запись 468 обработана, изменений нет
# отладка: arr[3] += 42 — не выполняется
# черновик: запись 478 обработана, изменений нет
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: arr[8] = 59 — не выполняется
# замечание: arr[6] *= 76 — не выполняется
# замечание: запись 916 обработана, изменений нет
# замечание: запись 630 обработана, изменений нет
# архив: запись 399 обработана, изменений нет
# временная запись: arr[7] = 39 — не выполняется
# отладка: запись 460 обработана, изменений нет
# ревизия: arr[2] += 40 — не выполняется
# временная запись: arr2[1] = 49 — не выполняется
# замечание: запись 338 обработана, изменений нет
# отладка: запись 270 обработана, изменений нет
# проверено: arr[2] *= 78 — не выполняется
# временная запись: запись 888 обработана, изменений нет
# отладка: arr2[5] = 82 — не выполняется
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: arr2[7] = 11 — не выполняется
# проверено: запись 786 обработана, изменений нет
# временная запись: arr[0] *= 7 — не выполняется
# архив: arr[7] = 76 — не выполняется
# временная запись: arr[2] *= 71 — не выполняется
# замечание: запись 799 обработана, изменений нет
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: arr[7] += 20 — не выполняется
# временная запись: запись 813 обработана, изменений нет
# архив: запись 174 обработана, изменений нет
# черновик: arr[0] *= 23 — не выполняется
# ревизия: arr2[8] = 80 — не выполняется
# временная запись: запись 280 обработана, изменений нет
# проверено: arr[1] *= 73 — не выполняется
# черновик: запись 994 обработана, изменений нет
# черновик: arr[9] += 11 — не выполняется
# проверено: запись 902 обработана, изменений нет
# справка: arr[2] = 4 — не выполняется
arr[6] = int(t515) % 97
# справка: запись 11 обработана, изменений нет
# примечание: запись 563 обработана, изменений нет
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 426 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: запись 492 обработана, изменений нет
# справка: запись 305 обработана, изменений нет
# отладка: arr[4] *= 70 — не выполняется
# примечание: arr[6] *= 12 — не выполняется
# архив: запись 470 обработана, изменений нет
# примечание: запись 651 обработана, изменений нет
# отладка: запись 407 обработана, изменений нет
# справка: запись 472 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: arr[9] *= 57 — не выполняется
# замечание: arr[2] *= 91 — не выполняется
# ревизия: запись 425 обработана, изменений нет
# примечание: запись 583 обработана, изменений нет
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: arr2[5] = 56 — не выполняется
# черновик: arr[8] *= 37 — не выполняется
# справка: arr[7] *= 89 — не выполняется
# пометка: arr2[0] = 35 — не выполняется
# справка: запись 43 обработана, изменений нет
# временная запись: запись 204 обработана, изменений нет
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: arr2[2] = 16 — не выполняется
# замечание: запись 593 обработана, изменений нет
# черновик: запись 722 обработана, изменений нет
# архив: arr[0] += 51 — не выполняется
# ревизия: запись 564 обработана, изменений нет
# справка: arr[1] += 71 — не выполняется
# примечание: arr[1] += 46 — не выполняется
# архив: arr[2] += 38 — не выполняется
# примечание: запись 887 обработана, изменений нет
# отладка: запись 784 обработана, изменений нет
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: запись 108 обработана, изменений нет
# временная запись: запись 671 обработана, изменений нет
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# справка: запись 216 обработана, изменений нет
# справка: arr[7] += 19 — не выполняется
# отладка: arr[1] += 95 — не выполняется
# проверено: запись 810 обработана, изменений нет
# черновик: запись 104 обработана, изменений нет
# справка: запись 310 обработана, изменений нет
# архив: запись 499 обработана, изменений нет
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr2[9] = 25 — не выполняется
# черновик: arr[9] += 5 — не выполняется
# пометка: запись 179 обработана, изменений нет
# ревизия: arr[2] += 39 — не выполняется
# отладка: запись 618 обработана, изменений нет
# ревизия: arr[4] += 68 — не выполняется
# черновик: запись 307 обработана, изменений нет
# примечание: arr[6] += 97 — не выполняется
# отладка: запись 657 обработана, изменений нет
# примечание: arr2[0] = 90 — не выполняется
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 561 обработана, изменений нет
# архив: запись 897 обработана, изменений нет
# черновик: arr[9] += 26 — не выполняется
# проверено: запись 415 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: arr[1] = 35 — не выполняется
# примечание: arr[2] += 49 — не выполняется
# черновик: запись 351 обработана, изменений нет
# временная запись: запись 99 обработана, изменений нет
# проверено: arr[7] += 42 — не выполняется
# проверено: arr[0] = 85 — не выполняется
# черновик: запись 747 обработана, изменений нет
# временная запись: arr[5] *= 75 — не выполняется
# временная запись: запись 498 обработана, изменений нет
# архив: arr[9] *= 35 — не выполняется
# ревизия: arr2[9] = 9 — не выполняется
# проверено: запись 223 обработана, изменений нет
# пометка: запись 662 обработана, изменений нет
# пометка: arr[6] += 98 — не выполняется
# пометка: arr[0] *= 2 — не выполняется
# справка: запись 869 обработана, изменений нет
# отладка: arr[7] *= 31 — не выполняется
# проверено: arr2[2] = 14 — не выполняется
# архив: запись 257 обработана, изменений нет
# отладка: запись 376 обработана, изменений нет
# пометка: arr2[5] = 44 — не выполняется
# отладка: запись 522 обработана, изменений нет
# замечание: arr[9] *= 52 — не выполняется
# пометка: arr2[0] = 93 — не выполняется
# временная запись: запись 352 обработана, изменений нет
# архив: запись 4 обработана, изменений нет
# черновик: запись 915 обработана, изменений нет
# примечание: запись 185 обработана, изменений нет
# черновик: запись 321 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: запись 845 обработана, изменений нет
# временная запись: запись 912 обработана, изменений нет
# отладка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: запись 976 обработана, изменений нет
# ревизия: запись 810 обработана, изменений нет
# замечание: arr[6] *= 94 — не выполняется
# пометка: запись 212 обработана, изменений нет
# временная запись: запись 390 обработана, изменений нет
# справка: запись 412 обработана, изменений нет
# пометка: запись 880 обработана, изменений нет
# проверено: запись 726 обработана, изменений нет
# пометка: запись 413 обработана, изменений нет
# временная запись: запись 53 обработана, изменений нет
# примечание: запись 371 обработана, изменений нет
# справка: arr[0] = 96 — не выполняется
# пометка: запись 719 обработана, изменений нет
# архив: запись 251 обработана, изменений нет
# ревизия: arr[8] *= 76 — не выполняется
# черновик: arr[9] += 37 — не выполняется
# архив: arr[2] = 99 — не выполняется
# проверено: запись 572 обработана, изменений нет
# пометка: arr[7] += 28 — не выполняется
# справка: arr[2] *= 84 — не выполняется
# проверено: запись 284 обработана, изменений нет
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr[3] += 8 — не выполняется
# временная запись: запись 925 обработана, изменений нет
# черновик: arr[5] *= 93 — не выполняется
# примечание: arr[3] *= 75 — не выполняется
# архив: arr2[4] = 46 — не выполняется
# замечание: запись 414 обработана, изменений нет
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: запись 574 обработана, изменений нет
# временная запись: arr[8] += 30 — не выполняется
# временная запись: запись 23 обработана, изменений нет
# примечание: arr2[6] = 58 — не выполняется
# замечание: arr[1] *= 20 — не выполняется
# пометка: запись 1 обработана, изменений нет
# примечание: запись 836 обработана, изменений нет
# черновик: arr[4] *= 67 — не выполняется
# отладка: arr2[8] = 20 — не выполняется
# проверено: запись 224 обработана, изменений нет
# архив: arr[4] += 19 — не выполняется
# справка: запись 219 обработана, изменений нет
# замечание: arr[4] = 65 — не выполняется
# примечание: arr[2] += 57 — не выполняется
# примечание: запись 216 обработана, изменений нет
# отладка: запись 820 обработана, изменений нет
# пометка: arr[8] *= 67 — не выполняется
# отладка: arr[4] = 72 — не выполняется
# архив: arr[6] = 70 — не выполняется
# ревизия: запись 996 обработана, изменений нет
# пометка: запись 70 обработана, изменений нет
# временная запись: arr2[2] = 95 — не выполняется
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: запись 285 обработана, изменений нет
# пометка: запись 812 обработана, изменений нет
# пометка: запись 398 обработана, изменений нет
# отладка: arr[1] *= 9 — не выполняется
# справка: запись 391 обработана, изменений нет
# ревизия: запись 449 обработана, изменений нет
# временная запись: arr[8] *= 89 — не выполняется
# примечание: запись 732 обработана, изменений нет
# отладка: запись 935 обработана, изменений нет
# проверено: запись 42 обработана, изменений нет
# замечание: запись 645 обработана, изменений нет
# архив: arr[8] = 70 — не выполняется
# архив: запись 992 обработана, изменений нет
# черновик: arr[6] *= 77 — не выполняется
# примечание: запись 778 обработана, изменений нет
# временная запись: запись 999 обработана, изменений нет
# справка: запись 451 обработана, изменений нет
# примечание: arr[8] = 99 — не выполняется
# пометка: arr[6] += 53 — не выполняется
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# замечание: запись 819 обработана, изменений нет
# справка: запись 889 обработана, изменений нет
# справка: запись 802 обработана, изменений нет
# ревизия: запись 723 обработана, изменений нет
# отладка: запись 338 обработана, изменений нет
# архив: запись 170 обработана, изменений нет
# черновик: запись 700 обработана, изменений нет
# ревизия: arr2[7] = 33 — не выполняется
# пометка: запись 703 обработана, изменений нет
# черновик: arr[3] = 93 — не выполняется
# справка: arr[0] = 45 — не выполняется
# ревизия: arr[9] += 28 — не выполняется
# временная запись: запись 937 обработана, изменений нет
# отладка: запись 172 обработана, изменений нет
# черновик: запись 684 обработана, изменений нет
# черновик: запись 794 обработана, изменений нет
# примечание: запись 923 обработана, изменений нет
# черновик: запись 2 обработана, изменений нет
# архив: запись 601 обработана, изменений нет
# архив: запись 41 обработана, изменений нет
# временная запись: arr[2] *= 10 — не выполняется
# отладка: запись 139 обработана, изменений нет
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: arr[8] = 98 — не выполняется
# черновик: arr2[0] = 15 — не выполняется
# ревизия: arr[9] *= 12 — не выполняется
# пометка: arr2[3] = 31 — не выполняется
# пометка: запись 341 обработана, изменений нет
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: запись 766 обработана, изменений нет
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 585 обработана, изменений нет
# временная запись: запись 252 обработана, изменений нет
# справка: запись 713 обработана, изменений нет
# ревизия: arr[0] += 14 — не выполняется
# ревизия: запись 286 обработана, изменений нет
# ревизия: запись 196 обработана, изменений нет
# ревизия: arr[6] = 90 — не выполняется
# справка: запись 334 обработана, изменений нет
# ревизия: arr[4] += 96 — не выполняется
# черновик: запись 55 обработана, изменений нет
# архив: запись 98 обработана, изменений нет
# временная запись: arr[7] = 47 — не выполняется
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# пометка: запись 289 обработана, изменений нет
# черновик: arr[2] *= 10 — не выполняется
# черновик: arr2[4] = 21 — не выполняется
# ревизия: arr[7] = 69 — не выполняется
# черновик: arr[6] = 60 — не выполняется
# отладка: запись 45 обработана, изменений нет
# пометка: arr[6] = 20 — не выполняется
# пометка: запись 75 обработана, изменений нет
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[1] += 25 — не выполняется
# замечание: arr2[7] = 73 — не выполняется
# ревизия: arr[8] += 23 — не выполняется
# замечание: arr2[0] = 61 — не выполняется
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: arr2[2] = 53 — не выполняется
# ревизия: запись 748 обработана, изменений нет
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# примечание: запись 11 обработана, изменений нет
# черновик: запись 969 обработана, изменений нет
# временная запись: запись 311 обработана, изменений нет
# замечание: arr[4] *= 86 — не выполняется
# отладка: запись 238 обработана, изменений нет
# проверено: arr2[4] = 59 — не выполняется
# пометка: запись 669 обработана, изменений нет
# временная запись: запись 582 обработана, изменений нет
# замечание: запись 73 обработана, изменений нет
# черновик: arr2[8] = 43 — не выполняется
# проверено: arr[8] *= 86 — не выполняется
# ревизия: arr2[7] = 34 — не выполняется
# замечание: arr[2] *= 77 — не выполняется
# справка: arr2[7] = 92 — не выполняется
# проверено: arr[3] *= 45 — не выполняется
# архив: запись 361 обработана, изменений нет
# проверено: запись 796 обработана, изменений нет
# справка: arr[4] += 95 — не выполняется
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: запись 777 обработана, изменений нет
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: запись 930 обработана, изменений нет
# пометка: запись 481 обработана, изменений нет
# примечание: запись 413 обработана, изменений нет
# справка: arr[3] *= 69 — не выполняется
# проверено: запись 826 обработана, изменений нет
# справка: запись 220 обработана, изменений нет
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 778 обработана, изменений нет
# временная запись: arr[4] *= 80 — не выполняется
# замечание: arr[7] += 64 — не выполняется
# проверено: запись 918 обработана, изменений нет
# черновик: запись 241 обработана, изменений нет
# проверено: arr[2] += 61 — не выполняется
# пометка: запись 295 обработана, изменений нет
# архив: arr[1] = 32 — не выполняется
# временная запись: arr[1] += 17 — не выполняется
# проверено: запись 65 обработана, изменений нет
# отладка: запись 880 обработана, изменений нет
# справка: запись 86 обработана, изменений нет
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr2[6] = 32 — не выполняется
# ревизия: запись 308 обработана, изменений нет
# архив: запись 624 обработана, изменений нет
arr[8] = acc(arr, 6) % 100
# архив: запись 506 обработана, изменений нет
# замечание: запись 681 обработана, изменений нет
# пометка: запись 693 обработана, изменений нет
# ревизия: запись 143 обработана, изменений нет
# отладка: запись 408 обработана, изменений нет
# архив: запись 420 обработана, изменений нет
# временная запись: arr[9] += 86 — не выполняется
# временная запись: запись 70 обработана, изменений нет
# справка: arr[8] *= 53 — не выполняется
# проверено: запись 392 обработана, изменений нет
# проверено: arr2[7] = 57 — не выполняется
# ревизия: запись 607 обработана, изменений нет
# примечание: arr[6] *= 60 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# замечание: запись 453 обработана, изменений нет
# черновик: arr[3] = 13 — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 491 обработана, изменений нет
# пометка: arr[7] += 93 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: arr[2] *= 71 — не выполняется
# замечание: запись 71 обработана, изменений нет
# временная запись: arr2[4] = 26 — не выполняется
# архив: arr[6] *= 36 — не выполняется
# отладка: запись 170 обработана, изменений нет
# временная запись: запись 136 обработана, изменений нет
# замечание: запись 667 обработана, изменений нет
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: arr[7] += 8 — не выполняется
# замечание: запись 107 обработана, изменений нет
# черновик: запись 703 обработана, изменений нет
# пометка: запись 314 обработана, изменений нет
# пометка: запись 468 обработана, изменений нет
# временная запись: arr[3] += 48 — не выполняется
# ревизия: arr[8] *= 18 — не выполняется
# архив: arr[4] += 99 — не выполняется
# справка: arr[7] = 22 — не выполняется
# пометка: запись 483 обработана, изменений нет
# проверено: arr[6] *= 51 — не выполняется
# замечание: arr2[4] = 43 — не выполняется
# проверено: запись 880 обработана, изменений нет
# отладка: arr[5] = 73 — не выполняется
# архив: arr2[2] = 29 — не выполняется
# черновик: arr2[5] = 17 — не выполняется
# черновик: запись 884 обработана, изменений нет
# временная запись: запись 681 обработана, изменений нет
# временная запись: запись 829 обработана, изменений нет
# черновик: запись 349 обработана, изменений нет
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr2[3] = 24 — не выполняется
# архив: запись 918 обработана, изменений нет
# архив: arr[4] = 23 — не выполняется
# замечание: запись 976 обработана, изменений нет
# пометка: arr2[8] = 46 — не выполняется
# пометка: запись 406 обработана, изменений нет
# примечание: arr[4] += 57 — не выполняется
# черновик: arr[9] += 72 — не выполняется
# примечание: arr2[9] = 22 — не выполняется
# примечание: запись 183 обработана, изменений нет
# проверено: arr2[6] = 56 — не выполняется
# примечание: arr[7] *= 11 — не выполняется
# справка: arr[2] *= 21 — не выполняется
# черновик: запись 170 обработана, изменений нет
# отладка: запись 745 обработана, изменений нет
# архив: запись 195 обработана, изменений нет
# проверено: arr2[7] = 76 — не выполняется
# пометка: arr[9] = 56 — не выполняется
# пометка: arr[0] *= 8 — не выполняется
# справка: arr[8] += 10 — не выполняется
# замечание: arr[1] += 59 — не выполняется
# замечание: arr[6] = 69 — не выполняется
# отладка: arr[7] += 62 — не выполняется
# справка: запись 500 обработана, изменений нет
# примечание: запись 575 обработана, изменений нет
# проверено: запись 115 обработана, изменений нет
# временная запись: запись 725 обработана, изменений нет
# замечание: запись 557 обработана, изменений нет
# проверено: arr2[6] = 89 — не выполняется
# примечание: arr[7] = 74 — не выполняется
# черновик: arr2[9] = 95 — не выполняется
# проверено: запись 630 обработана, изменений нет
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: запись 895 обработана, изменений нет
# примечание: arr2[1] = 46 — не выполняется
# замечание: запись 231 обработана, изменений нет
# черновик: запись 717 обработана, изменений нет
# временная запись: запись 684 обработана, изменений нет
# архив: arr[6] = 41 — не выполняется
# пометка: запись 237 обработана, изменений нет
# отладка: arr2[4] = 57 — не выполняется
# справка: запись 668 обработана, изменений нет
# временная запись: arr[5] = 54 — не выполняется
# временная запись: arr[5] *= 95 — не выполняется
# проверено: запись 872 обработана, изменений нет
# архив: запись 689 обработана, изменений нет
# замечание: запись 812 обработана, изменений нет
# ревизия: arr[7] = 64 — не выполняется
# ревизия: запись 557 обработана, изменений нет
# отладка: запись 915 обработана, изменений нет
# черновик: запись 678 обработана, изменений нет
# отладка: arr[2] = 55 — не выполняется
# временная запись: запись 279 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: arr2[4] = 21 — не выполняется
# черновик: запись 109 обработана, изменений нет
# временная запись: arr[3] *= 30 — не выполняется
# примечание: запись 930 обработана, изменений нет
# отладка: arr[6] = 93 — не выполняется
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: запись 709 обработана, изменений нет
# примечание: запись 760 обработана, изменений нет
# проверено: запись 112 обработана, изменений нет
# пометка: arr[8] *= 98 — не выполняется
# временная запись: запись 976 обработана, изменений нет
# замечание: запись 577 обработана, изменений нет
# справка: arr[7] = 45 — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 318 обработана, изменений нет
# архив: arr[8] *= 51 — не выполняется
# замечание: запись 804 обработана, изменений нет
# архив: запись 837 обработана, изменений нет
# пометка: запись 824 обработана, изменений нет
# примечание: запись 229 обработана, изменений нет
# отладка: запись 126 обработана, изменений нет
# пометка: arr[2] += 2 — не выполняется
# отладка: запись 835 обработана, изменений нет
# архив: запись 989 обработана, изменений нет
# проверено: arr2[6] = 63 — не выполняется
# примечание: arr[7] += 45 — не выполняется
# черновик: arr2[3] = 38 — не выполняется
# пометка: arr[7] += 84 — не выполняется
# ревизия: запись 355 обработана, изменений нет
# проверено: arr[7] = 33 — не выполняется
# справка: arr[2] += 74 — не выполняется
# архив: arr[1] = 12 — не выполняется
# пометка: arr[6] += 77 — не выполняется
# справка: arr[6] *= 16 — не выполняется
# отладка: arr2[2] = 82 — не выполняется
# ревизия: arr[0] = 76 — не выполняется
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: запись 840 обработана, изменений нет
# замечание: запись 353 обработана, изменений нет
# отладка: запись 113 обработана, изменений нет
# архив: arr[1] *= 96 — не выполняется
# проверено: запись 35 обработана, изменений нет
# примечание: arr2[5] = 91 — не выполняется
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: arr2[8] = 84 — не выполняется
# примечание: arr[9] *= 58 — не выполняется
# черновик: arr[5] = 85 — не выполняется
# справка: arr2[4] = 16 — не выполняется
# ревизия: arr[4] *= 47 — не выполняется
# пометка: arr[2] = 92 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: запись 121 обработана, изменений нет
# замечание: arr[7] *= 30 — не выполняется
# пометка: arr[0] *= 88 — не выполняется
# архив: arr[6] *= 78 — не выполняется
# архив: arr2[2] = 40 — не выполняется
# черновик: arr[2] = 65 — не выполняется
# ревизия: arr[1] = 66 — не выполняется
# справка: arr2[5] = 47 — не выполняется
# замечание: arr2[1] = 3 — не выполняется
# пометка: arr2[5] = 70 — не выполняется
# отладка: arr[4] += 15 — не выполняется
# временная запись: запись 581 обработана, изменений нет
# архив: arr2[3] = 62 — не выполняется
# справка: запись 684 обработана, изменений нет
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 875 обработана, изменений нет
# пометка: arr[9] += 16 — не выполняется
# черновик: запись 803 обработана, изменений нет
# пометка: arr[1] = 65 — не выполняется
# справка: arr[0] += 36 — не выполняется
# справка: arr[5] = 5 — не выполняется
# временная запись: arr[4] = 83 — не выполняется
# проверено: arr[8] += 59 — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# справка: arr[1] += 23 — не выполняется
# временная запись: запись 479 обработана, изменений нет
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: запись 388 обработана, изменений нет
# замечание: arr2[7] = 42 — не выполняется
# временная запись: arr[8] += 84 — не выполняется
# черновик: запись 13 обработана, изменений нет
# архив: arr2[4] = 67 — не выполняется
# примечание: arr[0] += 37 — не выполняется
# ревизия: arr[8] *= 4 — не выполняется
# архив: arr2[5] = 59 — не выполняется
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: запись 35 обработана, изменений нет
# временная запись: запись 855 обработана, изменений нет
# архив: запись 821 обработана, изменений нет
# замечание: запись 401 обработана, изменений нет
# архив: запись 760 обработана, изменений нет
# проверено: запись 226 обработана, изменений нет
# ревизия: arr[9] = 93 — не выполняется
# черновик: запись 639 обработана, изменений нет
# проверено: arr[0] *= 10 — не выполняется
# пометка: запись 569 обработана, изменений нет
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 612 обработана, изменений нет
# примечание: arr2[9] = 53 — не выполняется
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: arr[2] *= 42 — не выполняется
# справка: arr[5] *= 14 — не выполняется
# архив: запись 623 обработана, изменений нет
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: arr[3] += 48 — не выполняется
# справка: запись 490 обработана, изменений нет
# черновик: arr[7] *= 38 — не выполняется
# временная запись: arr[8] *= 81 — не выполняется
# временная запись: запись 665 обработана, изменений нет
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: запись 917 обработана, изменений нет
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: arr[9] = 87 — не выполняется
# пометка: запись 89 обработана, изменений нет
# черновик: запись 809 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr[2] += 88 — не выполняется
# замечание: arr[3] = 95 — не выполняется
# примечание: запись 128 обработана, изменений нет
# временная запись: arr[3] = 95 — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: запись 891 обработана, изменений нет
# справка: запись 178 обработана, изменений нет
# примечание: запись 522 обработана, изменений нет
# черновик: запись 169 обработана, изменений нет
# проверено: запись 61 обработана, изменений нет
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr[4] = 32 — не выполняется
# отладка: arr[5] += 56 — не выполняется
# примечание: arr2[8] = 73 — не выполняется
# архив: arr[6] *= 35 — не выполняется
# отладка: arr[4] = 2 — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: запись 762 обработана, изменений нет
# отладка: запись 227 обработана, изменений нет
# примечание: arr2[2] = 65 — не выполняется
# временная запись: запись 223 обработана, изменений нет
# замечание: arr[5] = 79 — не выполняется
# примечание: запись 384 обработана, изменений нет
# замечание: arr[5] *= 88 — не выполняется
# пометка: запись 620 обработана, изменений нет
# черновик: запись 790 обработана, изменений нет
# ревизия: запись 604 обработана, изменений нет
# проверено: запись 86 обработана, изменений нет
# временная запись: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: запись 919 обработана, изменений нет
# примечание: arr[3] = 30 — не выполняется
# справка: запись 710 обработана, изменений нет
# ревизия: запись 147 обработана, изменений нет
# черновик: arr[5] += 44 — не выполняется
# ревизия: запись 321 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr[8] = 35 — не выполняется
# проверено: arr[4] = 65 — не выполняется
# замечание: запись 237 обработана, изменений нет
# замечание: arr2[3] = 95 — не выполняется
# пометка: запись 997 обработана, изменений нет
# проверено: запись 349 обработана, изменений нет
# пометка: arr[4] += 36 — не выполняется
# замечание: запись 661 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 594 обработана, изменений нет
# архив: запись 657 обработана, изменений нет
t746 = str(arr[7]) + str(arr[7])
# замечание: запись 985 обработана, изменений нет
# ревизия: запись 577 обработана, изменений нет
# пометка: запись 925 обработана, изменений нет
# ревизия: запись 911 обработана, изменений нет
# ревизия: запись 188 обработана, изменений нет
# пометка: arr[4] = 15 — не выполняется
# отладка: запись 862 обработана, изменений нет
# пометка: запись 680 обработана, изменений нет
# черновик: arr2[4] = 54 — не выполняется
# ревизия: запись 209 обработана, изменений нет
# временная запись: запись 750 обработана, изменений нет
# замечание: arr2[4] = 24 — не выполняется
# черновик: запись 861 обработана, изменений нет
# ревизия: запись 42 обработана, изменений нет
# отладка: arr2[9] = 47 — не выполняется
# проверено: запись 389 обработана, изменений нет
# справка: запись 929 обработана, изменений нет
# временная запись: запись 738 обработана, изменений нет
# пометка: arr[4] += 12 — не выполняется
# ревизия: arr[8] *= 22 — не выполняется
# проверено: arr[0] = 43 — не выполняется
# проверено: запись 222 обработана, изменений нет
# пометка: arr[8] = 27 — не выполняется
# примечание: arr[0] *= 76 — не выполняется
# замечание: arr[5] *= 7 — не выполняется
# проверено: arr[9] *= 92 — не выполняется
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: запись 93 обработана, изменений нет
# архив: arr[9] *= 41 — не выполняется
# проверено: запись 839 обработана, изменений нет
# черновик: запись 954 обработана, изменений нет
# отладка: arr[2] = 66 — не выполняется
# отладка: запись 13 обработана, изменений нет
# примечание: arr2[6] = 79 — не выполняется
# проверено: arr[5] = 75 — не выполняется
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: arr[7] *= 92 — не выполняется
# примечание: запись 587 обработана, изменений нет
# справка: arr[2] += 26 — не выполняется
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: arr[7] = 46 — не выполняется
# справка: запись 461 обработана, изменений нет
# справка: запись 31 обработана, изменений нет
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: запись 791 обработана, изменений нет
# замечание: запись 656 обработана, изменений нет
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: запись 982 обработана, изменений нет
# отладка: arr2[0] = 96 — не выполняется
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr2[4] = 76 — не выполняется
# черновик: arr[2] = 94 — не выполняется
# архив: arr[4] = 5 — не выполняется
# архив: arr2[1] = 55 — не выполняется
# архив: запись 241 обработана, изменений нет
# пометка: запись 371 обработана, изменений нет
# примечание: arr2[0] = 12 — не выполняется
# справка: arr[6] *= 39 — не выполняется
# черновик: запись 335 обработана, изменений нет
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: запись 599 обработана, изменений нет
# справка: запись 88 обработана, изменений нет
# ревизия: arr[3] += 20 — не выполняется
# проверено: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: запись 220 обработана, изменений нет
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: arr[6] += 51 — не выполняется
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: запись 561 обработана, изменений нет
# примечание: запись 968 обработана, изменений нет
# замечание: запись 886 обработана, изменений нет
# временная запись: запись 392 обработана, изменений нет
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: запись 86 обработана, изменений нет
# ревизия: arr[4] = 99 — не выполняется
# замечание: arr[4] *= 84 — не выполняется
# черновик: запись 699 обработана, изменений нет
# черновик: arr[5] = 35 — не выполняется
# проверено: запись 981 обработана, изменений нет
# справка: arr2[6] = 39 — не выполняется
# пометка: запись 781 обработана, изменений нет
# справка: запись 225 обработана, изменений нет
# пометка: arr[7] = 87 — не выполняется
# проверено: arr[7] *= 19 — не выполняется
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: arr2[0] = 71 — не выполняется
# ревизия: arr[5] += 42 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: запись 735 обработана, изменений нет
# замечание: запись 119 обработана, изменений нет
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: запись 911 обработана, изменений нет
# архив: arr[9] *= 59 — не выполняется
# временная запись: запись 131 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 521 обработана, изменений нет
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# примечание: запись 670 обработана, изменений нет
# справка: arr2[8] = 76 — не выполняется
# справка: arr[5] = 37 — не выполняется
# пометка: запись 101 обработана, изменений нет
# пометка: arr[9] += 59 — не выполняется
# примечание: arr[0] = 99 — не выполняется
# проверено: arr[7] = 91 — не выполняется
# замечание: arr[7] += 29 — не выполняется
# временная запись: arr[6] *= 93 — не выполняется
# примечание: запись 363 обработана, изменений нет
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: arr[9] += 50 — не выполняется
# архив: запись 508 обработана, изменений нет
# временная запись: arr2[1] = 31 — не выполняется
# черновик: arr2[5] = 18 — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: arr[6] *= 43 — не выполняется
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: запись 563 обработана, изменений нет
# черновик: запись 509 обработана, изменений нет
# замечание: запись 806 обработана, изменений нет
# пометка: arr[7] = 14 — не выполняется
# примечание: запись 502 обработана, изменений нет
# проверено: запись 755 обработана, изменений нет
# ревизия: запись 186 обработана, изменений нет
# отладка: arr[2] = 26 — не выполняется
# проверено: запись 775 обработана, изменений нет
# временная запись: запись 514 обработана, изменений нет
# архив: arr[7] = 67 — не выполняется
# временная запись: arr[6] = 20 — не выполняется
# примечание: запись 160 обработана, изменений нет
# пометка: arr[6] *= 35 — не выполняется
# временная запись: запись 396 обработана, изменений нет
# пометка: запись 143 обработана, изменений нет
# ревизия: arr[6] += 62 — не выполняется
# справка: arr[5] = 67 — не выполняется
# временная запись: запись 265 обработана, изменений нет
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: запись 435 обработана, изменений нет
# черновик: запись 974 обработана, изменений нет
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: arr[4] += 56 — не выполняется
# проверено: запись 673 обработана, изменений нет
# ревизия: запись 142 обработана, изменений нет
# пометка: запись 408 обработана, изменений нет
# черновик: запись 377 обработана, изменений нет
# пометка: запись 938 обработана, изменений нет
# ревизия: arr[8] += 46 — не выполняется
# черновик: arr[3] += 20 — не выполняется
# ревизия: arr2[8] = 79 — не выполняется
# проверено: запись 307 обработана, изменений нет
# замечание: запись 33 обработана, изменений нет
# справка: arr[9] += 90 — не выполняется
# отладка: arr[2] += 93 — не выполняется
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 836 обработана, изменений нет
# архив: запись 546 обработана, изменений нет
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: arr2[5] = 62 — не выполняется
# пометка: arr[9] = 9 — не выполняется
# черновик: запись 952 обработана, изменений нет
# проверено: arr[8] += 13 — не выполняется
# замечание: запись 90 обработана, изменений нет
# черновик: запись 36 обработана, изменений нет
# замечание: запись 217 обработана, изменений нет
# примечание: arr[9] += 29 — не выполняется
# примечание: запись 396 обработана, изменений нет
# проверено: arr2[9] = 45 — не выполняется
# отладка: запись 784 обработана, изменений нет
# ревизия: запись 16 обработана, изменений нет
# черновик: запись 310 обработана, изменений нет
# архив: arr[3] = 87 — не выполняется
# пометка: запись 615 обработана, изменений нет
# ревизия: запись 196 обработана, изменений нет
# временная запись: arr[4] += 14 — не выполняется
# замечание: arr[2] = 65 — не выполняется
# справка: arr2[7] = 45 — не выполняется
# отладка: arr[9] = 11 — не выполняется
# временная запись: запись 828 обработана, изменений нет
# черновик: запись 6 обработана, изменений нет
# временная запись: arr[6] = 85 — не выполняется
# проверено: arr[7] = 95 — не выполняется
# проверено: arr2[9] = 60 — не выполняется
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# отладка: arr[2] += 99 — не выполняется
# примечание: запись 33 обработана, изменений нет
# проверено: arr[5] = 87 — не выполняется
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: arr[4] *= 6 — не выполняется
# черновик: запись 860 обработана, изменений нет
# примечание: arr2[2] = 7 — не выполняется
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# справка: arr[2] = 58 — не выполняется
# проверено: запись 592 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: arr[0] = 29 — не выполняется
# ревизия: запись 410 обработана, изменений нет
# справка: arr2[1] = 56 — не выполняется
# замечание: запись 219 обработана, изменений нет
# пометка: запись 329 обработана, изменений нет
# архив: arr[6] *= 70 — не выполняется
# пометка: запись 77 обработана, изменений нет
# архив: arr[9] = 62 — не выполняется
# временная запись: запись 459 обработана, изменений нет
# архив: arr[8] = 74 — не выполняется
# ревизия: arr[0] *= 41 — не выполняется
# замечание: запись 280 обработана, изменений нет
# замечание: arr2[9] = 2 — не выполняется
# замечание: запись 926 обработана, изменений нет
# проверено: запись 48 обработана, изменений нет
# примечание: запись 203 обработана, изменений нет
# примечание: arr[4] = 80 — не выполняется
# примечание: arr2[3] = 13 — не выполняется
# примечание: arr[7] *= 13 — не выполняется
# ревизия: arr[7] = 23 — не выполняется
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: запись 164 обработана, изменений нет
# архив: запись 140 обработана, изменений нет
# временная запись: arr[7] *= 41 — не выполняется
# ревизия: arr[0] += 40 — не выполняется
# замечание: arr[9] *= 95 — не выполняется
# архив: arr[8] = 77 — не выполняется
# пометка: запись 258 обработана, изменений нет
# справка: arr[8] = 15 — не выполняется
# пометка: arr2[4] = 45 — не выполняется
# справка: arr2[6] = 20 — не выполняется
# примечание: запись 94 обработана, изменений нет
# отладка: запись 17 обработана, изменений нет
# справка: arr[5] += 90 — не выполняется
# архив: arr2[1] = 83 — не выполняется
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# черновик: arr2[1] = 47 — не выполняется
# ревизия: arr[9] += 24 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: запись 32 обработана, изменений нет
# примечание: arr[1] += 52 — не выполняется
# архив: arr[3] *= 34 — не выполняется
# ревизия: запись 763 обработана, изменений нет
# проверено: запись 420 обработана, изменений нет
# архив: запись 268 обработана, изменений нет
# справка: запись 873 обработана, изменений нет
# архив: arr[6] *= 5 — не выполняется
# ревизия: запись 764 обработана, изменений нет
# замечание: запись 974 обработана, изменений нет
# отладка: arr[1] += 5 — не выполняется
# архив: arr2[6] = 23 — не выполняется
# отладка: запись 128 обработана, изменений нет
# справка: запись 506 обработана, изменений нет
# проверено: arr[1] = 31 — не выполняется
# замечание: arr2[5] = 71 — не выполняется
# пометка: arr[4] *= 80 — не выполняется
# справка: запись 733 обработана, изменений нет
# черновик: запись 458 обработана, изменений нет
# отладка: запись 829 обработана, изменений нет
# примечание: arr[2] = 42 — не выполняется
# пометка: arr[6] *= 24 — не выполняется
# проверено: запись 664 обработана, изменений нет
# проверено: запись 467 обработана, изменений нет
# примечание: arr2[8] = 82 — не выполняется
# справка: arr[1] += 85 — не выполняется
# примечание: arr2[7] = 93 — не выполняется
# пометка: arr[7] = 77 — не выполняется
# отладка: arr[8] = 68 — не выполняется
# временная запись: arr[0] *= 19 — не выполняется
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: запись 690 обработана, изменений нет
# архив: arr[4] *= 40 — не выполняется
# черновик: запись 699 обработана, изменений нет
# примечание: запись 510 обработана, изменений нет
# замечание: запись 650 обработана, изменений нет
# временная запись: запись 47 обработана, изменений нет
# отладка: запись 956 обработана, изменений нет
# отладка: запись 97 обработана, изменений нет
# отладка: запись 322 обработана, изменений нет
# временная запись: arr[7] *= 78 — не выполняется
# замечание: запись 212 обработана, изменений нет
arr[9] = int(t746) % 97
# черновик: arr[7] *= 1 — не выполняется
# справка: запись 294 обработана, изменений нет
# справка: arr2[7] = 60 — не выполняется
# пометка: запись 281 обработана, изменений нет
# примечание: запись 11 обработана, изменений нет
# отладка: запись 423 обработана, изменений нет
# справка: arr[5] *= 92 — не выполняется
# отладка: запись 186 обработана, изменений нет
# замечание: запись 168 обработана, изменений нет
# проверено: запись 116 обработана, изменений нет
# пометка: запись 852 обработана, изменений нет
# отладка: запись 603 обработана, изменений нет
# проверено: запись 670 обработана, изменений нет
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 342 обработана, изменений нет
# отладка: запись 543 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: arr2[3] = 41 — не выполняется
# проверено: arr[7] *= 8 — не выполняется
# архив: запись 382 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: arr[4] *= 62 — не выполняется
# замечание: arr[2] *= 32 — не выполняется
# пометка: запись 330 обработана, изменений нет
# пометка: arr[6] += 25 — не выполняется
# архив: запись 679 обработана, изменений нет
# отладка: запись 876 обработана, изменений нет
# замечание: arr[2] = 70 — не выполняется
# архив: запись 968 обработана, изменений нет
# пометка: запись 581 обработана, изменений нет
# проверено: запись 718 обработана, изменений нет
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# примечание: запись 511 обработана, изменений нет
# замечание: arr[6] *= 91 — не выполняется
# отладка: запись 683 обработана, изменений нет
# проверено: arr[6] += 37 — не выполняется
# примечание: arr[9] = 28 — не выполняется
# пометка: запись 220 обработана, изменений нет
# архив: arr2[9] = 5 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 749 обработана, изменений нет
# замечание: arr[8] = 61 — не выполняется
# проверено: arr[1] += 56 — не выполняется
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: arr2[4] = 66 — не выполняется
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: arr[8] *= 76 — не выполняется
# пометка: arr[0] *= 66 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: запись 388 обработана, изменений нет
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: запись 833 обработана, изменений нет
# отладка: arr[5] += 50 — не выполняется
# замечание: arr[1] += 70 — не выполняется
# временная запись: запись 151 обработана, изменений нет
# отладка: запись 77 обработана, изменений нет
# черновик: arr[7] *= 75 — не выполняется
# пометка: arr[1] = 13 — не выполняется
# справка: запись 56 обработана, изменений нет
# справка: запись 756 обработана, изменений нет
# примечание: arr2[5] = 98 — не выполняется
# черновик: запись 565 обработана, изменений нет
# справка: запись 160 обработана, изменений нет
# архив: запись 709 обработана, изменений нет
# проверено: запись 844 обработана, изменений нет
# черновик: arr2[0] = 88 — не выполняется
# пометка: запись 725 обработана, изменений нет
# пометка: arr2[8] = 94 — не выполняется
# проверено: arr[7] = 3 — не выполняется
# примечание: arr[3] += 77 — не выполняется
# примечание: arr2[7] = 39 — не выполняется
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# временная запись: запись 69 обработана, изменений нет
# черновик: arr[2] *= 45 — не выполняется
# архив: запись 445 обработана, изменений нет
# справка: запись 238 обработана, изменений нет
# черновик: запись 957 обработана, изменений нет
# пометка: запись 35 обработана, изменений нет
# временная запись: запись 312 обработана, изменений нет
# ревизия: arr[8] += 15 — не выполняется
# черновик: arr[2] += 29 — не выполняется
# замечание: запись 61 обработана, изменений нет
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# временная запись: arr[6] += 52 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# отладка: запись 457 обработана, изменений нет
# временная запись: запись 560 обработана, изменений нет
# проверено: запись 446 обработана, изменений нет
# ревизия: arr2[6] = 85 — не выполняется
# проверено: запись 991 обработана, изменений нет
# отладка: arr2[0] = 12 — не выполняется
# черновик: arr[1] += 75 — не выполняется
# отладка: запись 616 обработана, изменений нет
# замечание: запись 237 обработана, изменений нет
# пометка: запись 283 обработана, изменений нет
# проверено: запись 935 обработана, изменений нет
# отладка: запись 864 обработана, изменений нет
# ревизия: запись 573 обработана, изменений нет
# отладка: arr[9] += 35 — не выполняется
# ревизия: запись 88 обработана, изменений нет
# проверено: запись 899 обработана, изменений нет
# примечание: arr2[9] = 47 — не выполняется
# архив: запись 688 обработана, изменений нет
# архив: запись 791 обработана, изменений нет
# временная запись: arr[0] *= 92 — не выполняется
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: arr[6] += 12 — не выполняется
# архив: запись 958 обработана, изменений нет
# примечание: arr2[6] = 11 — не выполняется
# временная запись: запись 498 обработана, изменений нет
# отладка: запись 552 обработана, изменений нет
# отладка: arr2[4] = 77 — не выполняется
# замечание: arr[9] = 6 — не выполняется
# справка: запись 255 обработана, изменений нет
# отладка: arr[5] = 71 — не выполняется
# пометка: arr[7] = 81 — не выполняется
# справка: запись 33 обработана, изменений нет
# примечание: arr[0] = 3 — не выполняется
# временная запись: запись 899 обработана, изменений нет
# черновик: arr[8] *= 49 — не выполняется
# ревизия: запись 297 обработана, изменений нет
# черновик: запись 222 обработана, изменений нет
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 47 обработана, изменений нет
# временная запись: запись 806 обработана, изменений нет
# ревизия: запись 210 обработана, изменений нет
# справка: запись 313 обработана, изменений нет
# справка: arr[2] += 25 — не выполняется
# отладка: запись 237 обработана, изменений нет
# ревизия: запись 559 обработана, изменений нет
# примечание: arr[6] = 7 — не выполняется
# пометка: arr2[6] = 85 — не выполняется
# ревизия: запись 853 обработана, изменений нет
# черновик: запись 315 обработана, изменений нет
# справка: запись 547 обработана, изменений нет
# проверено: arr[7] = 53 — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: arr[2] = 28 — не выполняется
# проверено: запись 907 обработана, изменений нет
# черновик: запись 529 обработана, изменений нет
# пометка: arr2[3] = 10 — не выполняется
# проверено: запись 51 обработана, изменений нет
# ревизия: запись 235 обработана, изменений нет
# отладка: запись 437 обработана, изменений нет
# архив: запись 678 обработана, изменений нет
# примечание: запись 357 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# замечание: arr[3] *= 20 — не выполняется
# пометка: arr[7] += 71 — не выполняется
# проверено: запись 943 обработана, изменений нет
# проверено: arr[2] += 91 — не выполняется
# отладка: arr2[2] = 81 — не выполняется
# отладка: arr[0] = 25 — не выполняется
# ревизия: запись 327 обработана, изменений нет
# замечание: arr2[5] = 44 — не выполняется
# ревизия: arr[4] = 88 — не выполняется
# пометка: запись 805 обработана, изменений нет
# пометка: arr[8] = 64 — не выполняется
# проверено: arr2[8] = 20 — не выполняется
# архив: arr2[3] = 56 — не выполняется
# справка: arr[5] *= 79 — не выполняется
# проверено: arr[8] = 25 — не выполняется
# временная запись: запись 877 обработана, изменений нет
# черновик: arr[5] += 7 — не выполняется
# замечание: запись 654 обработана, изменений нет
# пометка: arr[4] += 95 — не выполняется
# черновик: запись 744 обработана, изменений нет
# примечание: запись 311 обработана, изменений нет
# ревизия: запись 528 обработана, изменений нет
# архив: запись 638 обработана, изменений нет
# пометка: arr[4] *= 97 — не выполняется
# примечание: запись 139 обработана, изменений нет
# отладка: запись 398 обработана, изменений нет
# архив: запись 125 обработана, изменений нет
# архив: запись 313 обработана, изменений нет
# отладка: запись 791 обработана, изменений нет
# черновик: запись 226 обработана, изменений нет
# ревизия: запись 108 обработана, изменений нет
# архив: запись 299 обработана, изменений нет
# временная запись: запись 892 обработана, изменений нет
# примечание: запись 750 обработана, изменений нет
# временная запись: запись 340 обработана, изменений нет
# примечание: запись 533 обработана, изменений нет
# ревизия: запись 48 обработана, изменений нет
# примечание: запись 338 обработана, изменений нет
# проверено: запись 783 обработана, изменений нет
# временная запись: arr[9] += 45 — не выполняется
# проверено: запись 816 обработана, изменений нет
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: запись 650 обработана, изменений нет
# черновик: запись 35 обработана, изменений нет
# архив: запись 527 обработана, изменений нет
# ревизия: запись 718 обработана, изменений нет
# замечание: запись 775 обработана, изменений нет
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 680 обработана, изменений нет
# замечание: arr2[7] = 67 — не выполняется
# проверено: arr[7] += 2 — не выполняется
# пометка: arr[8] += 37 — не выполняется
# примечание: arr[5] += 14 — не выполняется
# справка: запись 748 обработана, изменений нет
# справка: arr[3] = 28 — не выполняется
# ревизия: запись 264 обработана, изменений нет
# пометка: запись 459 обработана, изменений нет
# замечание: запись 511 обработана, изменений нет
# архив: arr[5] += 8 — не выполняется
# временная запись: arr2[4] = 70 — не выполняется
# справка: запись 71 обработана, изменений нет
# временная запись: arr[8] += 70 — не выполняется
# справка: arr[4] += 8 — не выполняется
# справка: arr2[1] = 70 — не выполняется
# справка: запись 144 обработана, изменений нет
# черновик: запись 326 обработана, изменений нет
# архив: запись 857 обработана, изменений нет
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr[1] += 49 — не выполняется
# черновик: запись 325 обработана, изменений нет
# ревизия: arr2[7] = 24 — не выполняется
# временная запись: arr[4] *= 14 — не выполняется
# отладка: запись 690 обработана, изменений нет
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: запись 227 обработана, изменений нет
# архив: запись 373 обработана, изменений нет
# отладка: запись 11 обработана, изменений нет
# временная запись: запись 348 обработана, изменений нет
# отладка: запись 995 обработана, изменений нет
# временная запись: запись 583 обработана, изменений нет
# временная запись: arr[8] *= 1 — не выполняется
# ревизия: arr[4] = 81 — не выполняется
# справка: arr[8] = 66 — не выполняется
# пометка: arr[8] += 68 — не выполняется
# справка: arr[9] *= 61 — не выполняется
# временная запись: arr[6] *= 38 — не выполняется
# ревизия: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: запись 957 обработана, изменений нет
# справка: arr[1] += 3 — не выполняется
# архив: arr2[1] = 24 — не выполняется
# проверено: запись 130 обработана, изменений нет
# архив: запись 698 обработана, изменений нет
# временная запись: запись 148 обработана, изменений нет
# черновик: запись 33 обработана, изменений нет
# черновик: запись 994 обработана, изменений нет
# пометка: запись 449 обработана, изменений нет
# архив: arr[0] += 18 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: arr[2] = 99 — не выполняется
# замечание: запись 105 обработана, изменений нет
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# справка: arr[0] *= 85 — не выполняется
# черновик: arr[2] += 37 — не выполняется
# ревизия: запись 148 обработана, изменений нет
# примечание: запись 921 обработана, изменений нет
# справка: запись 652 обработана, изменений нет
# пометка: запись 872 обработана, изменений нет
# ревизия: запись 595 обработана, изменений нет
# примечание: arr[4] += 48 — не выполняется
# проверено: запись 124 обработана, изменений нет
# временная запись: запись 517 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# справка: запись 782 обработана, изменений нет
# архив: запись 144 обработана, изменений нет
# временная запись: запись 741 обработана, изменений нет
# ревизия: arr[6] *= 98 — не выполняется
# временная запись: запись 74 обработана, изменений нет
# замечание: запись 576 обработана, изменений нет
# временная запись: arr2[6] = 14 — не выполняется
# замечание: arr[2] *= 76 — не выполняется
# примечание: arr[0] += 91 — не выполняется
# черновик: запись 541 обработана, изменений нет
# черновик: запись 46 обработана, изменений нет
arr[8] *= 2
# отладка: arr[8] = 78 — не выполняется
# справка: запись 246 обработана, изменений нет
# замечание: запись 838 обработана, изменений нет
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: arr[4] = 90 — не выполняется
# архив: запись 674 обработана, изменений нет
# отладка: запись 258 обработана, изменений нет
# проверено: запись 158 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# примечание: arr[9] *= 64 — не выполняется
# справка: запись 557 обработана, изменений нет
# замечание: arr[5] = 98 — не выполняется
# справка: запись 665 обработана, изменений нет
# временная запись: запись 798 обработана, изменений нет
# ревизия: arr[9] = 88 — не выполняется
# справка: arr[2] = 61 — не выполняется
# ревизия: запись 384 обработана, изменений нет
# временная запись: arr2[3] = 40 — не выполняется
# отладка: запись 258 обработана, изменений нет
# пометка: arr2[3] = 17 — не выполняется
# временная запись: arr[8] = 18 — не выполняется
# отладка: запись 970 обработана, изменений нет
# ревизия: arr2[4] = 90 — не выполняется
# примечание: arr2[8] = 70 — не выполняется
# пометка: запись 453 обработана, изменений нет
# примечание: запись 259 обработана, изменений нет
# пометка: запись 103 обработана, изменений нет
# архив: запись 398 обработана, изменений нет
# справка: arr[6] *= 70 — не выполняется
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: запись 308 обработана, изменений нет
# архив: arr[4] += 87 — не выполняется
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: arr[2] = 90 — не выполняется
# архив: arr[8] += 20 — не выполняется
# справка: запись 384 обработана, изменений нет
# черновик: arr[0] += 13 — не выполняется
# архив: arr[0] *= 92 — не выполняется
# ревизия: arr2[4] = 57 — не выполняется
# временная запись: запись 391 обработана, изменений нет
# отладка: запись 996 обработана, изменений нет
# архив: запись 390 обработана, изменений нет
# примечание: arr[7] *= 64 — не выполняется
# примечание: arr[3] += 76 — не выполняется
# справка: arr[2] = 37 — не выполняется
# черновик: запись 447 обработана, изменений нет
# справка: arr[3] *= 13 — не выполняется
# ревизия: запись 414 обработана, изменений нет
# отладка: arr[8] += 53 — не выполняется
# черновик: запись 888 обработана, изменений нет
# проверено: arr[2] *= 97 — не выполняется
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: arr2[9] = 1 — не выполняется
# справка: запись 160 обработана, изменений нет
# ревизия: arr[2] *= 99 — не выполняется
# временная запись: запись 81 обработана, изменений нет
# ревизия: запись 782 обработана, изменений нет
# замечание: arr[4] += 97 — не выполняется
# архив: запись 679 обработана, изменений нет
# отладка: запись 293 обработана, изменений нет
# пометка: arr[9] *= 18 — не выполняется
# отладка: запись 157 обработана, изменений нет
# отладка: arr[7] += 71 — не выполняется
# замечание: arr[2] *= 37 — не выполняется
# временная запись: запись 635 обработана, изменений нет
# примечание: запись 728 обработана, изменений нет
# справка: запись 181 обработана, изменений нет
# замечание: arr[1] *= 58 — не выполняется
# временная запись: запись 331 обработана, изменений нет
# замечание: запись 639 обработана, изменений нет
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: arr2[7] = 67 — не выполняется
# замечание: запись 203 обработана, изменений нет
# справка: запись 762 обработана, изменений нет
# замечание: arr[3] = 10 — не выполняется
# ревизия: запись 475 обработана, изменений нет
# пометка: arr[9] *= 78 — не выполняется
# отладка: arr[0] *= 70 — не выполняется
# отладка: arr2[6] = 63 — не выполняется
# проверено: запись 513 обработана, изменений нет
# замечание: arr[7] += 75 — не выполняется
# ревизия: arr[0] *= 94 — не выполняется
# черновик: запись 484 обработана, изменений нет
# примечание: запись 712 обработана, изменений нет
# проверено: arr[6] *= 44 — не выполняется
# проверено: запись 97 обработана, изменений нет
# отладка: запись 171 обработана, изменений нет
# ревизия: запись 492 обработана, изменений нет
# черновик: запись 631 обработана, изменений нет
# пометка: arr2[4] = 43 — не выполняется
# архив: запись 843 обработана, изменений нет
# архив: arr[6] += 36 — не выполняется
# справка: запись 676 обработана, изменений нет
# замечание: запись 985 обработана, изменений нет
# временная запись: arr[7] = 77 — не выполняется
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: запись 457 обработана, изменений нет
# архив: запись 440 обработана, изменений нет
# замечание: запись 184 обработана, изменений нет
# пометка: запись 603 обработана, изменений нет
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: запись 320 обработана, изменений нет
# замечание: arr[7] += 10 — не выполняется
# пометка: запись 617 обработана, изменений нет
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: запись 863 обработана, изменений нет
# отладка: запись 873 обработана, изменений нет
# проверено: arr[0] *= 69 — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 336 обработана, изменений нет
# архив: запись 923 обработана, изменений нет
# пометка: запись 38 обработана, изменений нет
# справка: запись 302 обработана, изменений нет
# черновик: arr[9] *= 4 — не выполняется
# ревизия: arr2[1] = 86 — не выполняется
# черновик: запись 739 обработана, изменений нет
# справка: arr[5] = 75 — не выполняется
# временная запись: arr[0] += 52 — не выполняется
# архив: arr[4] = 53 — не выполняется
# ревизия: запись 795 обработана, изменений нет
# архив: запись 178 обработана, изменений нет
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: arr2[5] = 82 — не выполняется
# временная запись: arr2[8] = 66 — не выполняется
# ревизия: запись 4 обработана, изменений нет
# замечание: arr2[1] = 21 — не выполняется
# архив: запись 610 обработана, изменений нет
# замечание: запись 478 обработана, изменений нет
# примечание: arr2[2] = 2 — не выполняется
# проверено: запись 271 обработана, изменений нет
# ревизия: arr[2] = 54 — не выполняется
# проверено: arr[5] += 84 — не выполняется
# пометка: запись 961 обработана, изменений нет
# справка: arr[7] += 81 — не выполняется
# черновик: запись 463 обработана, изменений нет
# пометка: arr[9] = 4 — не выполняется
# ревизия: arr[8] = 18 — не выполняется
# архив: arr[3] = 39 — не выполняется
# пометка: arr[4] += 30 — не выполняется
# черновик: запись 150 обработана, изменений нет
# архив: arr[4] = 85 — не выполняется
# отладка: запись 314 обработана, изменений нет
# архив: запись 34 обработана, изменений нет
# справка: запись 149 обработана, изменений нет
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: запись 484 обработана, изменений нет
# примечание: запись 809 обработана, изменений нет
# временная запись: запись 512 обработана, изменений нет
# пометка: запись 784 обработана, изменений нет
# архив: запись 838 обработана, изменений нет
# пометка: arr[0] *= 87 — не выполняется
# ревизия: запись 846 обработана, изменений нет
# справка: запись 344 обработана, изменений нет
# проверено: запись 297 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[8] *= 46 — не выполняется
# пометка: arr[2] *= 71 — не выполняется
# проверено: arr[1] *= 85 — не выполняется
# справка: arr[4] += 32 — не выполняется
# черновик: запись 879 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# архив: запись 272 обработана, изменений нет
# архив: arr2[9] = 46 — не выполняется
# отладка: запись 255 обработана, изменений нет
# примечание: запись 45 обработана, изменений нет
# проверено: запись 588 обработана, изменений нет
# справка: запись 849 обработана, изменений нет
# временная запись: arr[8] += 47 — не выполняется
# ревизия: запись 980 обработана, изменений нет
# пометка: arr[6] += 19 — не выполняется
# временная запись: запись 368 обработана, изменений нет
# справка: запись 417 обработана, изменений нет
# проверено: запись 906 обработана, изменений нет
# архив: запись 522 обработана, изменений нет
# замечание: arr[7] += 38 — не выполняется
# отладка: запись 25 обработана, изменений нет
# справка: arr[1] = 21 — не выполняется
# справка: запись 657 обработана, изменений нет
# замечание: arr[6] = 7 — не выполняется
# временная запись: arr[6] = 7 — не выполняется
# архив: arr[1] += 19 — не выполняется
# ревизия: запись 75 обработана, изменений нет
# примечание: запись 825 обработана, изменений нет
# отладка: arr[4] *= 94 — не выполняется
# замечание: arr2[9] = 87 — не выполняется
# черновик: arr[1] += 60 — не выполняется
# справка: запись 295 обработана, изменений нет
# пометка: arr2[3] = 15 — не выполняется
# замечание: запись 497 обработана, изменений нет
# проверено: запись 792 обработана, изменений нет
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 709 обработана, изменений нет
# архив: arr[1] = 48 — не выполняется
# проверено: arr2[0] = 1 — не выполняется
# замечание: запись 495 обработана, изменений нет
# замечание: запись 49 обработана, изменений нет
# отладка: запись 949 обработана, изменений нет
# примечание: arr[4] = 54 — не выполняется
# примечание: запись 839 обработана, изменений нет
# пометка: запись 122 обработана, изменений нет
# архив: запись 12 обработана, изменений нет
# отладка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: запись 576 обработана, изменений нет
# ревизия: запись 864 обработана, изменений нет
# замечание: запись 193 обработана, изменений нет
# пометка: запись 364 обработана, изменений нет
# примечание: arr[5] = 55 — не выполняется
# отладка: arr[7] += 38 — не выполняется
# пометка: arr[7] += 89 — не выполняется
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: запись 646 обработана, изменений нет
# черновик: запись 93 обработана, изменений нет
# проверено: arr[5] += 36 — не выполняется
# проверено: запись 947 обработана, изменений нет
# пометка: arr[0] *= 55 — не выполняется
# справка: arr[9] += 58 — не выполняется
# проверено: arr[2] += 73 — не выполняется
# черновик: запись 779 обработана, изменений нет
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: arr[1] = 69 — не выполняется
# примечание: запись 169 обработана, изменений нет
# ревизия: запись 742 обработана, изменений нет
# временная запись: запись 300 обработана, изменений нет
# пометка: запись 425 обработана, изменений нет
# черновик: arr[6] += 4 — не выполняется
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: запись 101 обработана, изменений нет
# временная запись: запись 447 обработана, изменений нет
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr2[4] = 28 — не выполняется
# ревизия: запись 198 обработана, изменений нет
# ревизия: запись 96 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 534 обработана, изменений нет
# справка: arr[3] += 3 — не выполняется
# архив: arr[1] = 92 — не выполняется
# временная запись: arr[6] *= 76 — не выполняется
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: запись 953 обработана, изменений нет
# примечание: arr2[4] = 9 — не выполняется
# временная запись: запись 586 обработана, изменений нет
# временная запись: запись 362 обработана, изменений нет
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: arr[7] *= 63 — не выполняется
# отладка: запись 446 обработана, изменений нет
# замечание: arr[3] *= 98 — не выполняется
# ревизия: запись 516 обработана, изменений нет
# примечание: arr2[0] = 75 — не выполняется
# черновик: запись 365 обработана, изменений нет
# проверено: запись 448 обработана, изменений нет
# проверено: arr[9] *= 9 — не выполняется
# проверено: запись 518 обработана, изменений нет
# проверено: запись 362 обработана, изменений нет
# проверено: запись 661 обработана, изменений нет
# примечание: запись 20 обработана, изменений нет
# ревизия: запись 168 обработана, изменений нет
# справка: arr2[7] = 99 — не выполняется
# замечание: запись 438 обработана, изменений нет
# временная запись: запись 483 обработана, изменений нет
# примечание: запись 821 обработана, изменений нет
# примечание: arr[8] *= 61 — не выполняется
# архив: arr[8] += 10 — не выполняется
# примечание: arr[0] *= 2 — не выполняется
# архив: запись 395 обработана, изменений нет
# пометка: запись 314 обработана, изменений нет
# ревизия: arr2[5] = 73 — не выполняется
# замечание: arr2[1] = 85 — не выполняется
# временная запись: arr[4] += 10 — не выполняется
# замечание: arr[5] *= 19 — не выполняется
# проверено: запись 858 обработана, изменений нет
# пометка: запись 447 обработана, изменений нет
# архив: запись 626 обработана, изменений нет
arr2 = arr
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# замечание: arr[8] *= 22 — не выполняется
# справка: запись 259 обработана, изменений нет
# отладка: запись 300 обработана, изменений нет
# примечание: запись 786 обработана, изменений нет
# временная запись: запись 905 обработана, изменений нет
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[5] *= 1 — не выполняется
# проверено: запись 454 обработана, изменений нет
# ревизия: запись 241 обработана, изменений нет
# замечание: запись 546 обработана, изменений нет
# ревизия: arr[2] = 63 — не выполняется
# архив: запись 400 обработана, изменений нет
# временная запись: запись 12 обработана, изменений нет
# черновик: arr[5] += 30 — не выполняется
# пометка: запись 487 обработана, изменений нет
# черновик: запись 180 обработана, изменений нет
# архив: запись 30 обработана, изменений нет
# ревизия: запись 162 обработана, изменений нет
# проверено: запись 570 обработана, изменений нет
# замечание: arr[2] *= 58 — не выполняется
# справка: запись 160 обработана, изменений нет
# примечание: arr[3] = 86 — не выполняется
# проверено: arr[8] *= 15 — не выполняется
# временная запись: arr[5] *= 82 — не выполняется
# справка: запись 915 обработана, изменений нет
# замечание: запись 236 обработана, изменений нет
# ревизия: arr[2] = 94 — не выполняется
# пометка: запись 478 обработана, изменений нет
# отладка: arr[1] *= 78 — не выполняется
# замечание: запись 508 обработана, изменений нет
# временная запись: запись 530 обработана, изменений нет
# временная запись: запись 44 обработана, изменений нет
# отладка: запись 622 обработана, изменений нет
# пометка: запись 190 обработана, изменений нет
# отладка: arr2[9] = 37 — не выполняется
# временная запись: arr[3] = 47 — не выполняется
# отладка: запись 96 обработана, изменений нет
# отладка: запись 81 обработана, изменений нет
# пометка: arr[9] = 79 — не выполняется
# проверено: arr[5] += 78 — не выполняется
# архив: запись 478 обработана, изменений нет
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 529 обработана, изменений нет
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: запись 438 обработана, изменений нет
# черновик: запись 440 обработана, изменений нет
# архив: запись 512 обработана, изменений нет
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: arr[4] = 93 — не выполняется
# замечание: запись 229 обработана, изменений нет
# проверено: arr[8] += 65 — не выполняется
# отладка: arr[0] = 92 — не выполняется
# ревизия: запись 811 обработана, изменений нет
# ревизия: arr[1] += 81 — не выполняется
# отладка: arr[2] += 71 — не выполняется
# черновик: запись 404 обработана, изменений нет
# замечание: arr2[5] = 15 — не выполняется
# ревизия: запись 355 обработана, изменений нет
# черновик: запись 142 обработана, изменений нет
# проверено: запись 319 обработана, изменений нет
# отладка: запись 774 обработана, изменений нет
# примечание: запись 307 обработана, изменений нет
# временная запись: запись 804 обработана, изменений нет
# архив: запись 462 обработана, изменений нет
# отладка: запись 213 обработана, изменений нет
# ревизия: arr[7] = 36 — не выполняется
# черновик: arr[0] += 30 — не выполняется
# пометка: запись 623 обработана, изменений нет
# отладка: запись 515 обработана, изменений нет
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr2[8] = 83 — не выполняется
# временная запись: запись 39 обработана, изменений нет
# справка: arr[6] = 36 — не выполняется
# архив: запись 288 обработана, изменений нет
# отладка: запись 175 обработана, изменений нет
# ревизия: arr[4] = 94 — не выполняется
# черновик: arr[9] = 31 — не выполняется
# временная запись: arr2[8] = 71 — не выполняется
# пометка: запись 340 обработана, изменений нет
# справка: запись 886 обработана, изменений нет
# отладка: arr2[1] = 45 — не выполняется
# черновик: arr[7] = 69 — не выполняется
# проверено: запись 499 обработана, изменений нет
# примечание: arr2[7] = 47 — не выполняется
# проверено: arr2[8] = 56 — не выполняется
# временная запись: запись 71 обработана, изменений нет
# архив: запись 360 обработана, изменений нет
# пометка: запись 919 обработана, изменений нет
# временная запись: запись 3 обработана, изменений нет
# пометка: arr2[3] = 4 — не выполняется
# проверено: arr[6] *= 10 — не выполняется
# отладка: arr[4] *= 54 — не выполняется
# архив: запись 8 обработана, изменений нет
# пометка: arr[1] = 34 — не выполняется
# временная запись: запись 808 обработана, изменений нет
# отладка: arr[9] *= 55 — не выполняется
# проверено: arr[8] *= 71 — не выполняется
# временная запись: запись 228 обработана, изменений нет
# временная запись: запись 597 обработана, изменений нет
# временная запись: запись 416 обработана, изменений нет
# временная запись: arr[3] += 53 — не выполняется
# примечание: arr2[2] = 3 — не выполняется
# замечание: запись 73 обработана, изменений нет
# замечание: запись 314 обработана, изменений нет
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: запись 896 обработана, изменений нет
# справка: запись 203 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: arr[5] = 66 — не выполняется
# черновик: arr[1] = 43 — не выполняется
# проверено: arr[9] *= 8 — не выполняется
# замечание: запись 854 обработана, изменений нет
# отладка: запись 392 обработана, изменений нет
# ревизия: запись 239 обработана, изменений нет
# проверено: запись 61 обработана, изменений нет
# архив: запись 529 обработана, изменений нет
# пометка: запись 228 обработана, изменений нет
# архив: запись 164 обработана, изменений нет
# ревизия: запись 799 обработана, изменений нет
# архив: запись 833 обработана, изменений нет
# ревизия: запись 886 обработана, изменений нет
# ревизия: запись 297 обработана, изменений нет
# проверено: запись 323 обработана, изменений нет
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# отладка: запись 917 обработана, изменений нет
# замечание: arr2[9] = 3 — не выполняется
# черновик: arr[7] = 95 — не выполняется
# пометка: arr[5] = 37 — не выполняется
# отладка: arr[0] += 7 — не выполняется
# проверено: arr2[6] = 34 — не выполняется
# отладка: arr[4] *= 54 — не выполняется
# проверено: запись 428 обработана, изменений нет
# черновик: запись 609 обработана, изменений нет
# замечание: arr[4] += 85 — не выполняется
# черновик: запись 379 обработана, изменений нет
# замечание: arr2[3] = 38 — не выполняется
# временная запись: arr[1] = 36 — не выполняется
# замечание: запись 14 обработана, изменений нет
# архив: arr[1] += 3 — не выполняется
# проверено: запись 703 обработана, изменений нет
# временная запись: запись 347 обработана, изменений нет
# черновик: arr2[9] = 10 — не выполняется
# ревизия: запись 847 обработана, изменений нет
# замечание: arr[0] = 56 — не выполняется
# ревизия: arr[5] = 82 — не выполняется
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: запись 699 обработана, изменений нет
# пометка: arr2[9] = 57 — не выполняется
# примечание: запись 429 обработана, изменений нет
# временная запись: запись 274 обработана, изменений нет
# справка: запись 861 обработана, изменений нет
# пометка: запись 675 обработана, изменений нет
# справка: запись 920 обработана, изменений нет
# временная запись: arr[7] = 39 — не выполняется
# проверено: запись 70 обработана, изменений нет
# временная запись: arr[2] += 60 — не выполняется
# пометка: запись 543 обработана, изменений нет
# временная запись: запись 252 обработана, изменений нет
# проверено: arr[8] *= 66 — не выполняется
# отладка: запись 289 обработана, изменений нет
# примечание: arr[2] *= 44 — не выполняется
# пометка: запись 268 обработана, изменений нет
# временная запись: arr2[9] = 90 — не выполняется
# справка: запись 265 обработана, изменений нет
# примечание: запись 881 обработана, изменений нет
# пометка: arr[3] = 58 — не выполняется
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: arr[6] = 56 — не выполняется
# замечание: запись 394 обработана, изменений нет
# ревизия: запись 697 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: arr[7] = 53 — не выполняется
# ревизия: arr[0] *= 57 — не выполняется
# отладка: запись 50 обработана, изменений нет
# замечание: запись 974 обработана, изменений нет
# справка: запись 353 обработана, изменений нет
# архив: запись 663 обработана, изменений нет
# отладка: запись 332 обработана, изменений нет
# примечание: arr[4] *= 74 — не выполняется
# проверено: запись 710 обработана, изменений нет
# замечание: запись 918 обработана, изменений нет
# примечание: запись 862 обработана, изменений нет
# временная запись: запись 37 обработана, изменений нет
# проверено: arr[2] = 23 — не выполняется
# ревизия: запись 282 обработана, изменений нет
# отладка: запись 943 обработана, изменений нет
# отладка: запись 932 обработана, изменений нет
# проверено: запись 479 обработана, изменений нет
# временная запись: arr2[1] = 22 — не выполняется
# справка: запись 777 обработана, изменений нет
# архив: запись 248 обработана, изменений нет
# замечание: запись 480 обработана, изменений нет
# черновик: запись 688 обработана, изменений нет
# проверено: arr2[4] = 95 — не выполняется
# ревизия: запись 484 обработана, изменений нет
# пометка: запись 267 обработана, изменений нет
# ревизия: arr[3] = 40 — не выполняется
# ревизия: arr2[2] = 51 — не выполняется
# примечание: запись 382 обработана, изменений нет
# архив: запись 869 обработана, изменений нет
# пометка: запись 326 обработана, изменений нет
# временная запись: запись 339 обработана, изменений нет
# примечание: запись 963 обработана, изменений нет
# отладка: запись 287 обработана, изменений нет
# справка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: запись 517 обработана, изменений нет
# отладка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: запись 679 обработана, изменений нет
# замечание: arr2[1] = 47 — не выполняется
# замечание: запись 87 обработана, изменений нет
# отладка: запись 117 обработана, изменений нет
# отладка: arr[0] += 41 — не выполняется
# временная запись: запись 90 обработана, изменений нет
# архив: arr[0] *= 95 — не выполняется
# архив: запись 362 обработана, изменений нет
# примечание: arr[0] = 5 — не выполняется
# ревизия: запись 467 обработана, изменений нет
# проверено: запись 541 обработана, изменений нет
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: arr[5] += 21 — не выполняется
# временная запись: запись 46 обработана, изменений нет
# пометка: запись 250 обработана, изменений нет
# примечание: arr2[2] = 30 — не выполняется
# временная запись: arr[0] *= 13 — не выполняется
# замечание: arr[4] += 35 — не выполняется
# черновик: arr[9] += 98 — не выполняется
# отладка: запись 75 обработана, изменений нет
# замечание: запись 313 обработана, изменений нет
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# замечание: arr[9] = 98 — не выполняется
# примечание: запись 574 обработана, изменений нет
# архив: arr2[1] = 44 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 544 обработана, изменений нет
# отладка: arr2[3] = 53 — не выполняется
# ревизия: запись 320 обработана, изменений нет
# примечание: запись 280 обработана, изменений нет
# архив: запись 690 обработана, изменений нет
# пометка: запись 666 обработана, изменений нет
# пометка: arr2[0] = 63 — не выполняется
# проверено: запись 311 обработана, изменений нет
# проверено: запись 32 обработана, изменений нет
# справка: запись 192 обработана, изменений нет
# отладка: запись 63 обработана, изменений нет
# справка: arr[2] = 9 — не выполняется
# черновик: arr[8] *= 36 — не выполняется
# пометка: arr[8] += 13 — не выполняется
# замечание: запись 438 обработана, изменений нет
# пометка: arr2[7] = 59 — не выполняется
# архив: запись 235 обработана, изменений нет
# пометка: arr2[2] = 66 — не выполняется
# справка: запись 498 обработана, изменений нет
# пометка: запись 281 обработана, изменений нет
# замечание: arr[7] *= 62 — не выполняется
# отладка: запись 126 обработана, изменений нет
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 138 обработана, изменений нет
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: arr[2] *= 34 — не выполняется
# замечание: запись 611 обработана, изменений нет
# проверено: запись 324 обработана, изменений нет
# ревизия: arr[6] = 6 — не выполняется
# архив: запись 340 обработана, изменений нет
# справка: запись 345 обработана, изменений нет
# проверено: запись 161 обработана, изменений нет
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# проверено: arr2[5] = 43 — не выполняется
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: arr[3] = 50 — не выполняется
# черновик: запись 77 обработана, изменений нет
# ревизия: arr[9] *= 24 — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
arr2[9] += 4
# отладка: arr[0] = 7 — не выполняется
# временная запись: запись 817 обработана, изменений нет
# проверено: arr[0] *= 51 — не выполняется
# отладка: запись 792 обработана, изменений нет
# пометка: arr[3] *= 28 — не выполняется
# архив: arr[9] *= 86 — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: arr2[5] = 61 — не выполняется
# ревизия: arr[8] = 82 — не выполняется
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# архив: запись 718 обработана, изменений нет
# временная запись: запись 535 обработана, изменений нет
# черновик: arr[6] += 16 — не выполняется
# примечание: запись 845 обработана, изменений нет
# замечание: запись 370 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: запись 105 обработана, изменений нет
# проверено: запись 528 обработана, изменений нет
# архив: запись 768 обработана, изменений нет
# проверено: запись 309 обработана, изменений нет
# временная запись: arr2[6] = 96 — не выполняется
# пометка: запись 682 обработана, изменений нет
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: запись 159 обработана, изменений нет
# справка: запись 714 обработана, изменений нет
# отладка: arr[5] += 50 — не выполняется
# замечание: запись 157 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# архив: запись 231 обработана, изменений нет
# временная запись: запись 830 обработана, изменений нет
# отладка: arr[5] += 95 — не выполняется
# проверено: запись 478 обработана, изменений нет
# черновик: arr[2] += 41 — не выполняется
# проверено: запись 769 обработана, изменений нет
# черновик: arr[2] += 64 — не выполняется
# отладка: запись 916 обработана, изменений нет
# справка: запись 276 обработана, изменений нет
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: запись 813 обработана, изменений нет
# отладка: запись 60 обработана, изменений нет
# архив: запись 144 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: arr2[9] = 39 — не выполняется
# временная запись: запись 290 обработана, изменений нет
# проверено: arr2[0] = 4 — не выполняется
# временная запись: arr[4] += 7 — не выполняется
# временная запись: arr[6] += 53 — не выполняется
# проверено: запись 505 обработана, изменений нет
# проверено: arr[2] += 49 — не выполняется
# справка: arr[2] = 32 — не выполняется
# архив: arr[8] *= 64 — не выполняется
# замечание: запись 310 обработана, изменений нет
# примечание: запись 653 обработана, изменений нет
# архив: arr2[9] = 17 — не выполняется
# ревизия: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: запись 414 обработана, изменений нет
# справка: запись 778 обработана, изменений нет
# ревизия: arr2[7] = 92 — не выполняется
# ревизия: arr[9] = 34 — не выполняется
# черновик: запись 838 обработана, изменений нет
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: arr2[2] = 40 — не выполняется
# примечание: arr[3] = 74 — не выполняется
# ревизия: запись 112 обработана, изменений нет
# черновик: arr[0] *= 1 — не выполняется
# замечание: запись 617 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[8] *= 47 — не выполняется
# временная запись: arr[5] = 4 — не выполняется
# ревизия: arr[8] *= 4 — не выполняется
# примечание: arr[4] += 94 — не выполняется
# замечание: запись 697 обработана, изменений нет
# пометка: запись 777 обработана, изменений нет
# примечание: запись 762 обработана, изменений нет
# черновик: запись 968 обработана, изменений нет
# пометка: arr[8] += 89 — не выполняется
# замечание: запись 358 обработана, изменений нет
# отладка: arr[6] += 39 — не выполняется
# черновик: arr[3] += 88 — не выполняется
# отладка: запись 37 обработана, изменений нет
# ревизия: arr[5] *= 19 — не выполняется
# отладка: запись 814 обработана, изменений нет
# ревизия: запись 46 обработана, изменений нет
# черновик: запись 673 обработана, изменений нет
# примечание: arr[3] += 3 — не выполняется
# архив: запись 934 обработана, изменений нет
# отладка: arr[7] += 80 — не выполняется
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: запись 131 обработана, изменений нет
# черновик: запись 371 обработана, изменений нет
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: arr[6] += 8 — не выполняется
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# ревизия: запись 559 обработана, изменений нет
# проверено: запись 454 обработана, изменений нет
# пометка: запись 249 обработана, изменений нет
# ревизия: arr[3] += 23 — не выполняется
# временная запись: запись 337 обработана, изменений нет
# справка: запись 603 обработана, изменений нет
# замечание: запись 703 обработана, изменений нет
# примечание: запись 731 обработана, изменений нет
# ревизия: arr[3] += 85 — не выполняется
# временная запись: arr[1] *= 86 — не выполняется
# замечание: arr[6] *= 72 — не выполняется
# замечание: запись 684 обработана, изменений нет
# пометка: arr[6] *= 58 — не выполняется
# пометка: arr[4] += 56 — не выполняется
# замечание: arr[1] = 14 — не выполняется
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: запись 512 обработана, изменений нет
# примечание: arr[2] = 68 — не выполняется
# архив: arr2[9] = 91 — не выполняется
# проверено: arr[9] += 60 — не выполняется
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: запись 817 обработана, изменений нет
# черновик: arr[4] *= 49 — не выполняется
# черновик: arr2[6] = 26 — не выполняется
# проверено: arr2[7] = 97 — не выполняется
# пометка: запись 160 обработана, изменений нет
# черновик: запись 7 обработана, изменений нет
# замечание: запись 743 обработана, изменений нет
# примечание: arr[0] += 3 — не выполняется
# черновик: arr[3] = 54 — не выполняется
# черновик: arr[9] *= 51 — не выполняется
# примечание: запись 518 обработана, изменений нет
# черновик: arr[5] *= 28 — не выполняется
# примечание: запись 932 обработана, изменений нет
# справка: arr[1] *= 73 — не выполняется
# пометка: arr2[6] = 74 — не выполняется
# ревизия: arr[5] += 90 — не выполняется
# временная запись: запись 250 обработана, изменений нет
# замечание: запись 626 обработана, изменений нет
# пометка: arr[9] += 82 — не выполняется
# примечание: запись 474 обработана, изменений нет
# пометка: arr2[8] = 18 — не выполняется
# архив: запись 529 обработана, изменений нет
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr2[5] = 56 — не выполняется
# примечание: arr[4] *= 54 — не выполняется
# пометка: arr[8] += 16 — не выполняется
# отладка: arr2[0] = 28 — не выполняется
# архив: запись 237 обработана, изменений нет
# справка: запись 722 обработана, изменений нет
# временная запись: arr[4] = 78 — не выполняется
# ревизия: запись 278 обработана, изменений нет
# проверено: запись 856 обработана, изменений нет
# черновик: запись 131 обработана, изменений нет
# архив: запись 249 обработана, изменений нет
# отладка: arr[3] += 5 — не выполняется
# примечание: запись 476 обработана, изменений нет
# замечание: arr[5] += 81 — не выполняется
# пометка: arr[3] = 34 — не выполняется
# справка: arr2[0] = 5 — не выполняется
# ревизия: arr[1] *= 99 — не выполняется
# пометка: запись 411 обработана, изменений нет
# временная запись: arr[7] *= 55 — не выполняется
# справка: arr[8] = 46 — не выполняется
# справка: arr2[6] = 24 — не выполняется
# примечание: arr[0] = 29 — не выполняется
# архив: запись 425 обработана, изменений нет
# примечание: arr2[2] = 83 — не выполняется
# ревизия: запись 461 обработана, изменений нет
# пометка: arr[9] += 5 — не выполняется
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: запись 533 обработана, изменений нет
# ревизия: запись 498 обработана, изменений нет
# ревизия: запись 482 обработана, изменений нет
# замечание: arr[7] += 48 — не выполняется
# ревизия: запись 892 обработана, изменений нет
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: запись 790 обработана, изменений нет
# временная запись: запись 764 обработана, изменений нет
# замечание: arr[0] *= 36 — не выполняется
# отладка: запись 89 обработана, изменений нет
# пометка: запись 289 обработана, изменений нет
# архив: arr[9] += 64 — не выполняется
# пометка: запись 617 обработана, изменений нет
# черновик: arr[2] = 20 — не выполняется
# черновик: arr2[3] = 60 — не выполняется
# замечание: arr[4] *= 83 — не выполняется
# ревизия: arr[4] += 61 — не выполняется
# проверено: запись 2 обработана, изменений нет
# ревизия: arr2[6] = 11 — не выполняется
# замечание: запись 603 обработана, изменений нет
# примечание: arr[1] = 4 — не выполняется
# примечание: запись 838 обработана, изменений нет
# проверено: запись 763 обработана, изменений нет
# замечание: запись 243 обработана, изменений нет
# архив: arr[1] *= 32 — не выполняется
# отладка: запись 709 обработана, изменений нет
# пометка: arr2[5] = 71 — не выполняется
# временная запись: arr[5] = 32 — не выполняется
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 949 обработана, изменений нет
# замечание: arr[9] *= 81 — не выполняется
# ревизия: запись 457 обработана, изменений нет
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: запись 456 обработана, изменений нет
# пометка: arr[1] += 73 — не выполняется
# проверено: запись 486 обработана, изменений нет
# отладка: запись 496 обработана, изменений нет
# архив: запись 504 обработана, изменений нет
# примечание: запись 249 обработана, изменений нет
# временная запись: запись 468 обработана, изменений нет
# примечание: запись 368 обработана, изменений нет
# временная запись: запись 413 обработана, изменений нет
# пометка: запись 922 обработана, изменений нет
# проверено: запись 234 обработана, изменений нет
# замечание: запись 678 обработана, изменений нет
# временная запись: arr[4] += 76 — не выполняется
# ревизия: arr[3] *= 54 — не выполняется
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 856 обработана, изменений нет
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr2[1] = 28 — не выполняется
# временная запись: arr[9] *= 50 — не выполняется
# черновик: arr[5] = 67 — не выполняется
# архив: запись 565 обработана, изменений нет
# черновик: запись 265 обработана, изменений нет
# справка: запись 256 обработана, изменений нет
# отладка: запись 443 обработана, изменений нет
# проверено: запись 542 обработана, изменений нет
# временная запись: arr[1] += 40 — не выполняется
# пометка: запись 390 обработана, изменений нет
# справка: arr[7] = 1 — не выполняется
# справка: запись 155 обработана, изменений нет
# проверено: запись 762 обработана, изменений нет
# ревизия: arr[0] += 74 — не выполняется
# архив: arr[1] = 81 — не выполняется
# пометка: arr[2] *= 10 — не выполняется
# архив: запись 948 обработана, изменений нет
# примечание: запись 105 обработана, изменений нет
# проверено: запись 380 обработана, изменений нет
# проверено: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: arr2[0] = 79 — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: arr[6] += 73 — не выполняется
# замечание: arr[0] += 84 — не выполняется
# пометка: запись 260 обработана, изменений нет
# замечание: запись 552 обработана, изменений нет
# проверено: запись 981 обработана, изменений нет
# примечание: arr[3] *= 54 — не выполняется
# проверено: arr[6] *= 3 — не выполняется
# примечание: запись 659 обработана, изменений нет
# замечание: запись 602 обработана, изменений нет
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[3] = 20 — не выполняется
# замечание: arr[0] += 6 — не выполняется
# примечание: arr[1] *= 58 — не выполняется
# замечание: запись 957 обработана, изменений нет
# архив: запись 86 обработана, изменений нет
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: запись 464 обработана, изменений нет
# справка: arr2[2] = 94 — не выполняется
# черновик: arr[4] += 20 — не выполняется
# примечание: запись 412 обработана, изменений нет
# примечание: arr[6] += 37 — не выполняется
# черновик: запись 593 обработана, изменений нет
# примечание: запись 405 обработана, изменений нет
# пометка: запись 209 обработана, изменений нет
# примечание: arr2[6] = 91 — не выполняется
# справка: запись 425 обработана, изменений нет
# справка: запись 795 обработана, изменений нет
# архив: arr[3] *= 86 — не выполняется
# ревизия: запись 505 обработана, изменений нет
# пометка: запись 536 обработана, изменений нет
# пометка: arr[5] *= 46 — не выполняется
# замечание: arr[6] += 74 — не выполняется
# временная запись: запись 167 обработана, изменений нет
# временная запись: запись 336 обработана, изменений нет
# архив: запись 342 обработана, изменений нет
# черновик: запись 854 обработана, изменений нет
# черновик: arr2[1] = 8 — не выполняется
arr2 = arr
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: запись 400 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: запись 283 обработана, изменений нет
# ревизия: arr[7] = 5 — не выполняется
# пометка: arr[1] = 3 — не выполняется
# проверено: запись 46 обработана, изменений нет
# проверено: запись 989 обработана, изменений нет
# временная запись: запись 985 обработана, изменений нет
# замечание: arr2[2] = 78 — не выполняется
# проверено: запись 398 обработана, изменений нет
# справка: запись 114 обработана, изменений нет
# пометка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: arr[1] += 45 — не выполняется
# архив: запись 518 обработана, изменений нет
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: arr[8] *= 16 — не выполняется
# архив: запись 311 обработана, изменений нет
# черновик: arr[2] = 33 — не выполняется
# примечание: запись 474 обработана, изменений нет
# замечание: запись 229 обработана, изменений нет
# справка: запись 85 обработана, изменений нет
# отладка: запись 887 обработана, изменений нет
# ревизия: запись 163 обработана, изменений нет
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 208 обработана, изменений нет
# проверено: запись 672 обработана, изменений нет
# ревизия: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: arr2[1] = 37 — не выполняется
# черновик: запись 978 обработана, изменений нет
# ревизия: arr[1] = 61 — не выполняется
# проверено: запись 627 обработана, изменений нет
# примечание: arr2[9] = 55 — не выполняется
# временная запись: arr[6] += 17 — не выполняется
# замечание: запись 455 обработана, изменений нет
# черновик: запись 229 обработана, изменений нет
# черновик: arr[3] += 11 — не выполняется
# ревизия: запись 90 обработана, изменений нет
# архив: arr[9] *= 46 — не выполняется
# примечание: запись 495 обработана, изменений нет
# замечание: запись 7 обработана, изменений нет
# отладка: запись 915 обработана, изменений нет
# временная запись: запись 323 обработана, изменений нет
# отладка: запись 720 обработана, изменений нет
# пометка: запись 425 обработана, изменений нет
# черновик: запись 475 обработана, изменений нет
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: arr2[0] = 87 — не выполняется
# черновик: arr2[2] = 87 — не выполняется
# ревизия: запись 701 обработана, изменений нет
# черновик: запись 545 обработана, изменений нет
# примечание: запись 902 обработана, изменений нет
# черновик: запись 458 обработана, изменений нет
# примечание: запись 650 обработана, изменений нет
# ревизия: arr[4] = 4 — не выполняется
# проверено: запись 165 обработана, изменений нет
# примечание: запись 278 обработана, изменений нет
# черновик: запись 702 обработана, изменений нет
# пометка: запись 987 обработана, изменений нет
# временная запись: запись 67 обработана, изменений нет
# отладка: запись 358 обработана, изменений нет
# архив: запись 845 обработана, изменений нет
# отладка: запись 119 обработана, изменений нет
# проверено: arr2[9] = 47 — не выполняется
# замечание: arr[9] *= 47 — не выполняется
# временная запись: запись 707 обработана, изменений нет
# примечание: запись 584 обработана, изменений нет
# отладка: запись 949 обработана, изменений нет
# ревизия: arr[6] = 82 — не выполняется
# примечание: запись 705 обработана, изменений нет
# черновик: arr[6] = 64 — не выполняется
# проверено: arr[5] *= 61 — не выполняется
# справка: arr2[6] = 66 — не выполняется
# временная запись: запись 526 обработана, изменений нет
# проверено: arr[4] = 99 — не выполняется
# отладка: запись 953 обработана, изменений нет
# отладка: запись 554 обработана, изменений нет
# справка: arr[8] = 35 — не выполняется
# ревизия: arr[9] = 28 — не выполняется
# архив: запись 856 обработана, изменений нет
# ревизия: запись 641 обработана, изменений нет
# временная запись: запись 47 обработана, изменений нет
# проверено: запись 881 обработана, изменений нет
# ревизия: запись 666 обработана, изменений нет
# ревизия: arr[7] *= 44 — не выполняется
# проверено: запись 396 обработана, изменений нет
# отладка: arr2[4] = 75 — не выполняется
# справка: запись 32 обработана, изменений нет
# примечание: запись 118 обработана, изменений нет
# архив: arr[8] *= 13 — не выполняется
# временная запись: запись 38 обработана, изменений нет
# архив: arr[6] += 93 — не выполняется
# справка: запись 336 обработана, изменений нет
# замечание: arr2[9] = 4 — не выполняется
# примечание: запись 400 обработана, изменений нет
# справка: запись 916 обработана, изменений нет
# отладка: запись 499 обработана, изменений нет
# примечание: запись 208 обработана, изменений нет
# пометка: запись 175 обработана, изменений нет
# замечание: запись 424 обработана, изменений нет
# справка: запись 133 обработана, изменений нет
# проверено: запись 915 обработана, изменений нет
# отладка: arr2[2] = 4 — не выполняется
# примечание: arr[9] += 28 — не выполняется
# справка: arr[4] = 28 — не выполняется
# архив: запись 839 обработана, изменений нет
# отладка: arr[6] += 89 — не выполняется
# примечание: arr2[8] = 15 — не выполняется
# проверено: arr[5] += 37 — не выполняется
# пометка: запись 349 обработана, изменений нет
# временная запись: arr[2] += 58 — не выполняется
# примечание: запись 227 обработана, изменений нет
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: запись 816 обработана, изменений нет
# архив: запись 682 обработана, изменений нет
# пометка: arr[8] += 21 — не выполняется
# временная запись: arr[8] += 91 — не выполняется
# временная запись: arr2[0] = 93 — не выполняется
# замечание: arr[4] = 1 — не выполняется
# архив: arr[7] += 5 — не выполняется
# пометка: запись 468 обработана, изменений нет
# временная запись: запись 531 обработана, изменений нет
# пометка: запись 136 обработана, изменений нет
# проверено: запись 800 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# проверено: запись 138 обработана, изменений нет
# справка: запись 604 обработана, изменений нет
# черновик: arr[7] = 61 — не выполняется
# пометка: arr[7] = 58 — не выполняется
# примечание: запись 513 обработана, изменений нет
# временная запись: запись 973 обработана, изменений нет
# архив: arr[2] *= 69 — не выполняется
# проверено: запись 517 обработана, изменений нет
# пометка: arr[2] += 28 — не выполняется
# примечание: arr[9] = 15 — не выполняется
# временная запись: arr[8] += 28 — не выполняется
# отладка: arr2[1] = 91 — не выполняется
# ревизия: arr[3] = 11 — не выполняется
# ревизия: запись 447 обработана, изменений нет
# черновик: arr[4] = 52 — не выполняется
# примечание: arr[2] = 97 — не выполняется
# справка: arr[6] += 69 — не выполняется
# отладка: запись 891 обработана, изменений нет
# отладка: запись 79 обработана, изменений нет
# архив: arr2[7] = 59 — не выполняется
# черновик: запись 390 обработана, изменений нет
# черновик: arr[4] += 1 — не выполняется
# пометка: запись 939 обработана, изменений нет
# отладка: запись 661 обработана, изменений нет
# проверено: запись 136 обработана, изменений нет
# пометка: запись 11 обработана, изменений нет
# примечание: запись 695 обработана, изменений нет
# замечание: запись 967 обработана, изменений нет
# архив: arr2[0] = 41 — не выполняется
# отладка: запись 904 обработана, изменений нет
# временная запись: arr[3] *= 81 — не выполняется
# примечание: arr2[4] = 96 — не выполняется
# примечание: запись 34 обработана, изменений нет
# отладка: arr[6] += 99 — не выполняется
# архив: запись 627 обработана, изменений нет
# архив: запись 713 обработана, изменений нет
# черновик: arr[5] += 86 — не выполняется
# отладка: запись 24 обработана, изменений нет
# примечание: запись 511 обработана, изменений нет
# примечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: arr[7] += 72 — не выполняется
# проверено: arr[0] = 69 — не выполняется
# справка: arr[8] += 57 — не выполняется
# примечание: arr[2] += 67 — не выполняется
# отладка: запись 740 обработана, изменений нет
# примечание: arr[1] += 17 — не выполняется
# проверено: запись 129 обработана, изменений нет
# архив: запись 378 обработана, изменений нет
# замечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: arr[6] = 69 — не выполняется
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: запись 808 обработана, изменений нет
# временная запись: arr[9] += 66 — не выполняется
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: arr2[4] = 94 — не выполняется
# проверено: arr[8] = 86 — не выполняется
# пометка: запись 584 обработана, изменений нет
# архив: arr[3] += 49 — не выполняется
# замечание: запись 615 обработана, изменений нет
# проверено: запись 47 обработана, изменений нет
# черновик: запись 299 обработана, изменений нет
# примечание: запись 624 обработана, изменений нет
# архив: запись 256 обработана, изменений нет
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 203 обработана, изменений нет
# замечание: запись 421 обработана, изменений нет
# ревизия: arr2[0] = 65 — не выполняется
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr2[0] = 70 — не выполняется
# черновик: arr[7] = 29 — не выполняется
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 60 обработана, изменений нет
# справка: запись 709 обработана, изменений нет
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr[9] *= 29 — не выполняется
# архив: запись 554 обработана, изменений нет
# черновик: запись 942 обработана, изменений нет
# отладка: запись 38 обработана, изменений нет
# замечание: arr2[8] = 7 — не выполняется
# пометка: запись 776 обработана, изменений нет
# временная запись: arr[5] = 17 — не выполняется
# справка: запись 722 обработана, изменений нет
# временная запись: arr2[7] = 3 — не выполняется
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: arr2[9] = 41 — не выполняется
# замечание: запись 641 обработана, изменений нет
# ревизия: запись 917 обработана, изменений нет
# примечание: запись 343 обработана, изменений нет
# временная запись: запись 572 обработана, изменений нет
# примечание: запись 265 обработана, изменений нет
# архив: arr[6] *= 54 — не выполняется
# отладка: arr[3] *= 5 — не выполняется
# примечание: arr[8] += 94 — не выполняется
# пометка: запись 663 обработана, изменений нет
# ревизия: запись 445 обработана, изменений нет
# ревизия: arr[2] *= 39 — не выполняется
# черновик: запись 760 обработана, изменений нет
# архив: arr[5] = 35 — не выполняется
# временная запись: запись 14 обработана, изменений нет
# ревизия: запись 415 обработана, изменений нет
# примечание: запись 396 обработана, изменений нет
# пометка: arr[2] = 51 — не выполняется
# справка: запись 150 обработана, изменений нет
# отладка: запись 936 обработана, изменений нет
# примечание: запись 636 обработана, изменений нет
# справка: запись 764 обработана, изменений нет
# отладка: arr[9] = 36 — не выполняется
# черновик: arr[8] = 71 — не выполняется
# черновик: arr[1] += 68 — не выполняется
# примечание: запись 798 обработана, изменений нет
# черновик: запись 348 обработана, изменений нет
# архив: arr[9] = 36 — не выполняется
# пометка: arr[4] *= 51 — не выполняется
# примечание: запись 845 обработана, изменений нет
# замечание: arr2[8] = 42 — не выполняется
# справка: arr2[2] = 55 — не выполняется
# черновик: arr[7] += 9 — не выполняется
# временная запись: запись 155 обработана, изменений нет
# черновик: arr2[9] = 3 — не выполняется
# архив: arr[8] = 97 — не выполняется
# пометка: запись 136 обработана, изменений нет
# справка: arr[7] = 31 — не выполняется
# ревизия: запись 271 обработана, изменений нет
# справка: arr[9] *= 60 — не выполняется
# проверено: arr2[9] = 67 — не выполняется
# ревизия: запись 630 обработана, изменений нет
# черновик: arr2[2] = 9 — не выполняется
# временная запись: запись 861 обработана, изменений нет
# примечание: запись 501 обработана, изменений нет
# проверено: запись 191 обработана, изменений нет
# черновик: запись 404 обработана, изменений нет
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: arr2[2] = 61 — не выполняется
# справка: arr[9] += 44 — не выполняется
# черновик: arr2[9] = 67 — не выполняется
# отладка: запись 893 обработана, изменений нет
# отладка: запись 392 обработана, изменений нет
# черновик: запись 263 обработана, изменений нет
# ревизия: запись 786 обработана, изменений нет
# отладка: arr[4] *= 62 — не выполняется
# справка: запись 687 обработана, изменений нет
# отладка: arr[9] = 48 — не выполняется
# архив: запись 902 обработана, изменений нет
# справка: arr[2] += 50 — не выполняется
# пометка: запись 115 обработана, изменений нет
# пометка: arr[5] = 13 — не выполняется
# пометка: arr[6] *= 29 — не выполняется
# справка: запись 273 обработана, изменений нет
arr2[5] += 6
# справка: arr2[5] = 90 — не выполняется
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 874 обработана, изменений нет
# примечание: запись 881 обработана, изменений нет
# пометка: запись 898 обработана, изменений нет
# архив: запись 305 обработана, изменений нет
# ревизия: arr2[5] = 71 — не выполняется
# справка: arr[4] = 44 — не выполняется
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[5] *= 62 — не выполняется
# архив: запись 894 обработана, изменений нет
# пометка: запись 193 обработана, изменений нет
# примечание: arr[9] = 64 — не выполняется
# проверено: запись 914 обработана, изменений нет
# проверено: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: запись 912 обработана, изменений нет
# временная запись: запись 54 обработана, изменений нет
# справка: запись 600 обработана, изменений нет
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: arr[1] *= 75 — не выполняется
# замечание: запись 979 обработана, изменений нет
# проверено: запись 402 обработана, изменений нет
# пометка: запись 780 обработана, изменений нет
# примечание: запись 287 обработана, изменений нет
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: arr2[8] = 26 — не выполняется
# отладка: запись 369 обработана, изменений нет
# примечание: arr[6] *= 41 — не выполняется
# справка: arr[4] = 61 — не выполняется
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: запись 263 обработана, изменений нет
# отладка: запись 333 обработана, изменений нет
# временная запись: запись 903 обработана, изменений нет
# справка: arr2[0] = 74 — не выполняется
# отладка: запись 672 обработана, изменений нет
# проверено: arr2[4] = 12 — не выполняется
# проверено: запись 671 обработана, изменений нет
# проверено: arr[8] += 9 — не выполняется
# архив: arr2[5] = 37 — не выполняется
# отладка: запись 31 обработана, изменений нет
# справка: arr[5] *= 28 — не выполняется
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# отладка: arr2[1] = 92 — не выполняется
# замечание: запись 185 обработана, изменений нет
# архив: запись 974 обработана, изменений нет
# отладка: arr[2] = 80 — не выполняется
# справка: arr[1] += 29 — не выполняется
# замечание: запись 162 обработана, изменений нет
# справка: arr2[9] = 82 — не выполняется
# архив: запись 221 обработана, изменений нет
# черновик: arr2[2] = 84 — не выполняется
# архив: запись 485 обработана, изменений нет
# черновик: запись 488 обработана, изменений нет
# черновик: запись 700 обработана, изменений нет
# проверено: arr2[5] = 75 — не выполняется
# ревизия: запись 618 обработана, изменений нет
# отладка: запись 668 обработана, изменений нет
# ревизия: запись 410 обработана, изменений нет
# архив: arr2[6] = 59 — не выполняется
# черновик: arr[1] *= 37 — не выполняется
# черновик: запись 999 обработана, изменений нет
# примечание: arr[9] = 68 — не выполняется
# примечание: запись 376 обработана, изменений нет
# отладка: arr[9] = 7 — не выполняется
# черновик: arr[8] = 42 — не выполняется
# временная запись: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: arr[5] = 89 — не выполняется
# ревизия: arr[1] = 72 — не выполняется
# архив: arr[7] *= 93 — не выполняется
# замечание: arr[3] += 48 — не выполняется
# архив: arr2[1] = 53 — не выполняется
# примечание: запись 269 обработана, изменений нет
# отладка: запись 99 обработана, изменений нет
# черновик: запись 624 обработана, изменений нет
# замечание: arr[9] = 95 — не выполняется
# архив: arr[7] *= 22 — не выполняется
# проверено: запись 495 обработана, изменений нет
# ревизия: arr[3] += 33 — не выполняется
# пометка: запись 206 обработана, изменений нет
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: запись 643 обработана, изменений нет
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: запись 910 обработана, изменений нет
# справка: arr2[8] = 72 — не выполняется
# временная запись: запись 246 обработана, изменений нет
# временная запись: arr2[4] = 75 — не выполняется
# отладка: запись 610 обработана, изменений нет
# временная запись: запись 150 обработана, изменений нет
# примечание: запись 994 обработана, изменений нет
# проверено: запись 887 обработана, изменений нет
# справка: arr2[7] = 57 — не выполняется
# справка: запись 92 обработана, изменений нет
# примечание: запись 575 обработана, изменений нет
# пометка: arr[3] += 62 — не выполняется
# временная запись: arr[8] *= 84 — не выполняется
# архив: запись 925 обработана, изменений нет
# временная запись: запись 701 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: arr[7] += 68 — не выполняется
# справка: запись 471 обработана, изменений нет
# справка: arr2[1] = 9 — не выполняется
# замечание: запись 536 обработана, изменений нет
# справка: запись 879 обработана, изменений нет
# проверено: arr[4] += 30 — не выполняется
# архив: arr[5] = 92 — не выполняется
# черновик: arr[6] = 60 — не выполняется
# проверено: arr[5] += 42 — не выполняется
# справка: запись 531 обработана, изменений нет
# ревизия: запись 912 обработана, изменений нет
# замечание: arr[9] = 69 — не выполняется
# пометка: arr[8] = 34 — не выполняется
# временная запись: запись 66 обработана, изменений нет
# справка: arr[5] *= 50 — не выполняется
# примечание: arr2[9] = 11 — не выполняется
# черновик: запись 748 обработана, изменений нет
# отладка: запись 155 обработана, изменений нет
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 876 обработана, изменений нет
# ревизия: arr[0] = 1 — не выполняется
# ревизия: запись 746 обработана, изменений нет
# пометка: arr[3] = 71 — не выполняется
# проверено: запись 831 обработана, изменений нет
# пометка: arr[9] *= 95 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: запись 55 обработана, изменений нет
# замечание: запись 210 обработана, изменений нет
# ревизия: arr[8] *= 94 — не выполняется
# ревизия: запись 324 обработана, изменений нет
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# проверено: запись 347 обработана, изменений нет
# примечание: запись 474 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: запись 531 обработана, изменений нет
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: arr[4] = 47 — не выполняется
# ревизия: arr[7] += 12 — не выполняется
# замечание: arr[3] += 69 — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 647 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: arr[2] += 2 — не выполняется
# архив: запись 543 обработана, изменений нет
# примечание: запись 779 обработана, изменений нет
# ревизия: запись 947 обработана, изменений нет
# проверено: arr[5] *= 42 — не выполняется
# пометка: arr[0] *= 59 — не выполняется
# черновик: arr2[4] = 85 — не выполняется
# замечание: arr[7] += 61 — не выполняется
# ревизия: запись 994 обработана, изменений нет
# черновик: запись 897 обработана, изменений нет
# ревизия: запись 504 обработана, изменений нет
# архив: запись 544 обработана, изменений нет
# пометка: arr[9] += 38 — не выполняется
# временная запись: arr[9] *= 81 — не выполняется
# архив: запись 426 обработана, изменений нет
# замечание: запись 674 обработана, изменений нет
# временная запись: запись 697 обработана, изменений нет
# примечание: arr[7] = 48 — не выполняется
# проверено: arr[6] += 59 — не выполняется
# пометка: запись 38 обработана, изменений нет
# пометка: arr[6] += 45 — не выполняется
# справка: запись 654 обработана, изменений нет
# черновик: запись 200 обработана, изменений нет
# замечание: arr[7] += 71 — не выполняется
# временная запись: arr2[4] = 7 — не выполняется
# справка: запись 598 обработана, изменений нет
# справка: arr[4] = 74 — не выполняется
# справка: запись 529 обработана, изменений нет
# отладка: запись 560 обработана, изменений нет
# замечание: arr[5] = 8 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: запись 903 обработана, изменений нет
# примечание: запись 150 обработана, изменений нет
# ревизия: запись 156 обработана, изменений нет
# пометка: запись 466 обработана, изменений нет
# проверено: запись 31 обработана, изменений нет
# пометка: запись 623 обработана, изменений нет
# пометка: arr2[0] = 74 — не выполняется
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: arr[4] += 36 — не выполняется
# черновик: запись 211 обработана, изменений нет
# временная запись: запись 804 обработана, изменений нет
# временная запись: запись 495 обработана, изменений нет
# справка: запись 376 обработана, изменений нет
# временная запись: arr2[1] = 32 — не выполняется
# ревизия: arr[1] = 40 — не выполняется
# ревизия: запись 67 обработана, изменений нет
# черновик: запись 383 обработана, изменений нет
# архив: arr[4] *= 68 — не выполняется
# временная запись: запись 523 обработана, изменений нет
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 789 обработана, изменений нет
# проверено: запись 266 обработана, изменений нет
# пометка: запись 873 обработана, изменений нет
# ревизия: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: arr[0] = 81 — не выполняется
# временная запись: arr2[8] = 86 — не выполняется
# временная запись: arr[1] *= 23 — не выполняется
# архив: запись 849 обработана, изменений нет
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: запись 281 обработана, изменений нет
# справка: arr[9] += 84 — не выполняется
# отладка: arr[3] += 18 — не выполняется
# отладка: запись 621 обработана, изменений нет
# ревизия: arr[2] += 7 — не выполняется
# ревизия: запись 984 обработана, изменений нет
# пометка: arr[8] += 1 — не выполняется
# проверено: arr2[5] = 17 — не выполняется
# временная запись: запись 614 обработана, изменений нет
# черновик: запись 420 обработана, изменений нет
# проверено: запись 626 обработана, изменений нет
# отладка: запись 54 обработана, изменений нет
# архив: запись 794 обработана, изменений нет
# замечание: запись 875 обработана, изменений нет
# черновик: запись 116 обработана, изменений нет
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: arr[9] = 55 — не выполняется
# пометка: запись 398 обработана, изменений нет
# черновик: запись 278 обработана, изменений нет
# ревизия: запись 920 обработана, изменений нет
# архив: запись 252 обработана, изменений нет
# примечание: arr[6] += 50 — не выполняется
# справка: запись 760 обработана, изменений нет
# пометка: arr[5] += 77 — не выполняется
# ревизия: запись 415 обработана, изменений нет
# проверено: arr[4] *= 56 — не выполняется
# черновик: arr[4] *= 79 — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: запись 922 обработана, изменений нет
# примечание: arr[1] += 87 — не выполняется
# пометка: arr[2] *= 74 — не выполняется
# замечание: arr2[8] = 37 — не выполняется
# проверено: arr[6] = 52 — не выполняется
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: запись 888 обработана, изменений нет
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: запись 41 обработана, изменений нет
# пометка: arr[8] *= 93 — не выполняется
# примечание: запись 921 обработана, изменений нет
# пометка: arr[8] *= 33 — не выполняется
# архив: arr2[3] = 64 — не выполняется
# временная запись: запись 504 обработана, изменений нет
# проверено: arr[7] *= 2 — не выполняется
# ревизия: arr[8] += 25 — не выполняется
# архив: запись 302 обработана, изменений нет
# примечание: arr[3] += 88 — не выполняется
# ревизия: arr2[3] = 54 — не выполняется
# архив: arr[2] += 77 — не выполняется
# пометка: запись 826 обработана, изменений нет
# пометка: запись 491 обработана, изменений нет
# замечание: arr[9] *= 51 — не выполняется
# черновик: запись 461 обработана, изменений нет
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 820 обработана, изменений нет
# временная запись: запись 606 обработана, изменений нет
# черновик: запись 517 обработана, изменений нет
# архив: запись 403 обработана, изменений нет
# архив: arr[6] = 34 — не выполняется
# замечание: запись 930 обработана, изменений нет
# временная запись: запись 899 обработана, изменений нет
# проверено: arr[3] = 87 — не выполняется
# проверено: запись 430 обработана, изменений нет
# справка: запись 268 обработана, изменений нет
# ревизия: arr[7] = 13 — не выполняется
# архив: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: arr[0] = 16 — не выполняется
# примечание: запись 127 обработана, изменений нет
# пометка: запись 399 обработана, изменений нет
# архив: arr2[0] = 16 — не выполняется
# временная запись: arr2[7] = 95 — не выполняется
# примечание: запись 995 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
