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
arr[5], arr[5] = arr[5], arr[5]
arr2[3] = 38
arr[2] *= 14
arr[9] += 24
arr[6], arr[1] = arr[1], arr[6]
arr[5] *= 41
arr2[1] = 4
arr2[1] = 51
"""

TRAP_0 = "arr[7] = 440"
TRAP_1 = "arr[9] = 844"
TRAP_2 = "arr[5] = 520"
TRAP_3 = "arr[2] = 918"
TRAP_4 = "arr[6] = 384"
TRAP_5 = "arr[9] = 796"
TRAP_6 = "arr[7] = 171"
TRAP_7 = "arr[7] = 101"
TRAP_8 = "arr[7] = 255"
TRAP_9 = "arr[1] = 708"
TRAP_10 = "arr[6] = 464"
TRAP_11 = "arr[2] = 251"
TRAP_12 = "arr[9] = 248"
TRAP_13 = "arr[0] = 810"
TRAP_14 = "arr[2] = 601"
TRAP_15 = "arr[8] = 198"
TRAP_16 = "arr[7] = 871"
TRAP_17 = "arr[8] = 698"
TRAP_18 = "arr[7] = 731"
TRAP_19 = "arr[5] = 475"
TRAP_20 = "arr[4] = 139"
TRAP_21 = "arr[0] = 462"
TRAP_22 = "arr[3] = 703"
TRAP_23 = "arr[7] = 165"
TRAP_24 = "arr[9] = 393"
TRAP_25 = "arr[5] = 947"
TRAP_26 = "arr[5] = 942"
TRAP_27 = "arr[0] = 323"
TRAP_28 = "arr[6] = 907"
TRAP_29 = "arr[1] = 736"
TRAP_30 = "arr[3] = 213"
TRAP_31 = "arr[5] = 436"
TRAP_32 = "arr[7] = 133"
TRAP_33 = "arr[9] = 313"
TRAP_34 = "arr[3] = 620"
TRAP_35 = "arr[0] = 567"
TRAP_36 = "arr[0] = 162"
TRAP_37 = "arr[0] = 181"
TRAP_38 = "arr[8] = 980"
TRAP_39 = "arr[6] = 109"
TRAP_40 = "arr[8] = 345"
TRAP_41 = "arr[7] = 864"
TRAP_42 = "arr[7] = 827"
TRAP_43 = "arr[6] = 517"
TRAP_44 = "arr[5] = 418"
TRAP_45 = "arr[0] = 767"
TRAP_46 = "arr[6] = 279"
TRAP_47 = "arr[7] = 819"
TRAP_48 = "arr[2] = 789"
TRAP_49 = "arr[4] = 373"
TRAP_50 = "arr[8] = 546"
TRAP_51 = "arr[7] = 909"
TRAP_52 = "arr[8] = 535"
TRAP_53 = "arr[2] = 315"
TRAP_54 = "arr[9] = 912"
TRAP_55 = "arr[1] = 723"
TRAP_56 = "arr[9] = 520"
TRAP_57 = "arr[4] = 725"
TRAP_58 = "arr[9] = 171"
TRAP_59 = "arr[4] = 932"
TRAP_60 = "arr[1] = 440"
TRAP_61 = "arr[0] = 484"
TRAP_62 = "arr[3] = 906"
TRAP_63 = "arr[8] = 863"
TRAP_64 = "arr[4] = 244"
TRAP_65 = "arr[0] = 874"
TRAP_66 = "arr[2] = 732"
TRAP_67 = "arr[9] = 186"
TRAP_68 = "arr[5] = 238"
TRAP_69 = "arr[1] = 913"
TRAP_70 = "arr[8] = 669"
TRAP_71 = "arr[7] = 702"
TRAP_72 = "arr[2] = 887"
TRAP_73 = "arr[0] = 373"
TRAP_74 = "arr[2] = 305"
TRAP_75 = "arr[9] = 321"
TRAP_76 = "arr[9] = 625"
TRAP_77 = "arr[1] = 877"
TRAP_78 = "arr[5] = 867"
TRAP_79 = "arr[0] = 125"
TRAP_80 = "arr[4] = 651"
TRAP_81 = "arr[8] = 337"
TRAP_82 = "arr[0] = 445"
TRAP_83 = "arr[0] = 194"
TRAP_84 = "arr[2] = 183"
TRAP_85 = "arr[5] = 745"
TRAP_86 = "arr[8] = 113"
TRAP_87 = "arr[5] = 772"
TRAP_88 = "arr[0] = 784"
TRAP_89 = "arr[4] = 255"
TRAP_90 = "arr[0] = 971"
TRAP_91 = "arr[3] = 777"
TRAP_92 = "arr[8] = 431"
TRAP_93 = "arr[6] = 336"
TRAP_94 = "arr[7] = 205"
TRAP_95 = "arr[9] = 162"
TRAP_96 = "arr[8] = 719"
TRAP_97 = "arr[4] = 264"
TRAP_98 = "arr[5] = 573"
TRAP_99 = "arr[4] = 162"
TRAP_100 = "arr[1] = 733"
TRAP_101 = "arr[3] = 512"
TRAP_102 = "arr[0] = 486"
TRAP_103 = "arr[2] = 408"
TRAP_104 = "arr[5] = 790"
TRAP_105 = "arr[4] = 346"
TRAP_106 = "arr[6] = 965"
TRAP_107 = "arr[7] = 967"
TRAP_108 = "arr[3] = 327"
TRAP_109 = "arr[7] = 902"
TRAP_110 = "arr[3] = 752"
TRAP_111 = "arr[1] = 171"
TRAP_112 = "arr[3] = 887"
TRAP_113 = "arr[1] = 839"
TRAP_114 = "arr[8] = 848"
TRAP_115 = "arr[8] = 767"
TRAP_116 = "arr[7] = 643"
TRAP_117 = "arr[8] = 654"
TRAP_118 = "arr[3] = 634"
TRAP_119 = "arr[5] = 308"
TRAP_120 = "arr[3] = 341"
TRAP_121 = "arr[2] = 125"
TRAP_122 = "arr[0] = 475"
TRAP_123 = "arr[5] = 218"
TRAP_124 = "arr[6] = 602"
TRAP_125 = "arr[0] = 673"
TRAP_126 = "arr[6] = 131"
TRAP_127 = "arr[3] = 845"
TRAP_128 = "arr[1] = 102"
TRAP_129 = "arr[4] = 740"
TRAP_130 = "arr[2] = 169"
TRAP_131 = "arr[5] = 134"
TRAP_132 = "arr[4] = 137"
TRAP_133 = "arr[1] = 233"
TRAP_134 = "arr[8] = 993"
TRAP_135 = "arr[2] = 505"
TRAP_136 = "arr[6] = 272"
TRAP_137 = "arr[5] = 246"
TRAP_138 = "arr[9] = 162"
TRAP_139 = "arr[3] = 160"
TRAP_140 = "arr[7] = 541"
TRAP_141 = "arr[5] = 149"
TRAP_142 = "arr[4] = 268"
TRAP_143 = "arr[7] = 589"
TRAP_144 = "arr[3] = 593"
TRAP_145 = "arr[2] = 791"
TRAP_146 = "arr[8] = 765"
TRAP_147 = "arr[0] = 183"
TRAP_148 = "arr[4] = 392"
TRAP_149 = "arr[9] = 374"

arr = [18, 3, 7, 22, 9, 6, 10, 19, 29, 28]

code_0 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_1 = arr[4] + 48
code_2 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_3 = arr[0]
note_4 = str(arr[7]) + str(arr[9])
label_5 = "запись 5 не применялась"
tmp_6 = arr[8] + 25
code_7 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_8 = arr[5]
tmp_9 = arr[6] + 2
code_10 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_11 = arr[9] + 11
note_12 = str(arr[6]) + str(arr[4])
code_13 = re.sub(r'[0-9]', '#', str(arr[5]))
label_14 = "запись 14 не применялась"
code_15 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_16 = arr[8] + 43
copy_17 = arr[9]
code_18 = re.sub(r'[0-9]', '#', str(arr[1]))
label_19 = "запись 19 не применялась"
code_20 = re.sub(r'[0-9]', '#', str(arr[1]))
note_21 = str(arr[4]) + str(arr[8])
label_22 = "запись 22 не применялась"
code_23 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_24 = arr[4] + 14
tmp_25 = arr[9] + 2
code_26 = re.sub(r'[0-9]', '#', str(arr[6]))
label_27 = "запись 27 не применялась"
tmp_28 = arr[6] + 5
code_29 = re.sub(r'[0-9]', '#', str(arr[7]))
code_30 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_31 = arr[8] + 19
copy_32 = arr[7]
tmp_33 = arr[9] + 27
code_34 = re.sub(r'[0-9]', '#', str(arr[5]))
label_35 = "запись 35 не применялась"
note_36 = str(arr[2]) + str(arr[3])
copy_37 = arr[4]
tmp_38 = arr[6] + 48
code_39 = re.sub(r'[0-9]', '#', str(arr[9]))
note_40 = str(arr[1]) + str(arr[3])
tmp_41 = arr[5] + 22
tmp_42 = arr[3] + 42
tmp_43 = arr[1] + 22
tmp_44 = arr[4] + 12
note_45 = str(arr[8]) + str(arr[0])
copy_46 = arr[0]
copy_47 = arr[6]
code_48 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_49 = arr[6] + 38
note_50 = str(arr[0]) + str(arr[4])
tmp_51 = arr[1] + 2
code_52 = re.sub(r'[0-9]', '#', str(arr[5]))
label_53 = "запись 53 не применялась"
tmp_54 = arr[8] + 12
tmp_55 = arr[2] + 8
tmp_56 = arr[4] + 48
tmp_57 = arr[7] + 34
label_58 = "запись 58 не применялась"
tmp_59 = arr[7] + 46
tmp_60 = arr[0] + 27
tmp_61 = arr[3] + 20
tmp_62 = arr[5] + 15
copy_63 = arr[0]
copy_64 = arr[9]
tmp_65 = arr[2] + 43
tmp_66 = arr[9] + 28
tmp_67 = arr[8] + 20
label_68 = "запись 68 не применялась"
tmp_69 = arr[2] + 5
tmp_70 = arr[9] + 47
tmp_71 = arr[7] + 14
note_72 = str(arr[5]) + str(arr[4])
label_73 = "запись 73 не применялась"
note_74 = str(arr[8]) + str(arr[8])
code_75 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_76 = arr[0] + 35
note_77 = str(arr[9]) + str(arr[2])
tmp_78 = arr[2] + 3
note_79 = str(arr[4]) + str(arr[9])
copy_80 = arr[7]
tmp_81 = arr[7] + 14
tmp_82 = arr[8] + 34
code_83 = re.sub(r'[0-9]', '#', str(arr[4]))
code_84 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_85 = arr[5]
tmp_86 = arr[4] + 36
tmp_87 = arr[7] + 41
tmp_88 = arr[0] + 50
tmp_89 = arr[7] + 15
label_90 = "запись 90 не применялась"
label_91 = "запись 91 не применялась"
copy_92 = arr[0]
code_93 = re.sub(r'[0-9]', '#', str(arr[4]))
label_94 = "запись 94 не применялась"
note_95 = str(arr[1]) + str(arr[7])
copy_96 = arr[4]
tmp_97 = arr[9] + 9
note_98 = str(arr[6]) + str(arr[5])
tmp_99 = arr[6] + 26
tmp_100 = arr[5] + 47
note_101 = str(arr[6]) + str(arr[6])
copy_102 = arr[8]
code_103 = re.sub(r'[0-9]', '#', str(arr[2]))
code_104 = re.sub(r'[0-9]', '#', str(arr[4]))
note_105 = str(arr[7]) + str(arr[0])
note_106 = str(arr[4]) + str(arr[0])
label_107 = "запись 107 не применялась"
note_108 = str(arr[8]) + str(arr[1])
tmp_109 = arr[3] + 25
note_110 = str(arr[4]) + str(arr[4])
note_111 = str(arr[5]) + str(arr[8])
copy_112 = arr[8]
tmp_113 = arr[9] + 50
note_114 = str(arr[3]) + str(arr[3])
copy_115 = arr[7]
tmp_116 = arr[9] + 44
code_117 = re.sub(r'[0-9]', '#', str(arr[8]))
code_118 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_119 = arr[0]
code_120 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_121 = arr[0] + 18
code_122 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_123 = arr[9] + 41
note_124 = str(arr[4]) + str(arr[5])
code_125 = re.sub(r'[0-9]', '#', str(arr[2]))
note_126 = str(arr[4]) + str(arr[9])
label_127 = "запись 127 не применялась"
code_128 = re.sub(r'[0-9]', '#', str(arr[0]))
note_129 = str(arr[9]) + str(arr[2])
note_130 = str(arr[7]) + str(arr[0])
copy_131 = arr[4]
code_132 = re.sub(r'[0-9]', '#', str(arr[5]))
label_133 = "запись 133 не применялась"
tmp_134 = arr[7] + 46
code_135 = re.sub(r'[0-9]', '#', str(arr[3]))
label_136 = "запись 136 не применялась"
note_137 = str(arr[1]) + str(arr[7])
note_138 = str(arr[9]) + str(arr[9])
note_139 = str(arr[8]) + str(arr[6])
label_140 = "запись 140 не применялась"
label_141 = "запись 141 не применялась"
note_142 = str(arr[0]) + str(arr[4])
note_143 = str(arr[9]) + str(arr[5])
copy_144 = arr[3]
tmp_145 = arr[0] + 10
note_146 = str(arr[6]) + str(arr[8])
note_147 = str(arr[5]) + str(arr[4])
label_148 = "запись 148 не применялась"
note_149 = str(arr[2]) + str(arr[3])
tmp_150 = arr[9] + 13
tmp_151 = arr[5] + 14
tmp_152 = arr[4] + 37
code_153 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_154 = arr[2]
tmp_155 = arr[0] + 33
copy_156 = arr[5]
note_157 = str(arr[3]) + str(arr[9])
tmp_158 = arr[2] + 5
tmp_159 = arr[8] + 37
copy_160 = arr[4]
code_161 = re.sub(r'[0-9]', '#', str(arr[2]))
note_162 = str(arr[2]) + str(arr[1])
copy_163 = arr[6]
tmp_164 = arr[4] + 33
tmp_165 = arr[2] + 50
label_166 = "запись 166 не применялась"
tmp_167 = arr[6] + 8
tmp_168 = arr[6] + 10
note_169 = str(arr[4]) + str(arr[0])
copy_170 = arr[5]
copy_171 = arr[9]
label_172 = "запись 172 не применялась"
tmp_173 = arr[3] + 17
copy_174 = arr[4]
note_175 = str(arr[6]) + str(arr[9])
note_176 = str(arr[9]) + str(arr[8])
copy_177 = arr[0]
tmp_178 = arr[9] + 47
tmp_179 = arr[5] + 45
label_180 = "запись 180 не применялась"
note_181 = str(arr[2]) + str(arr[6])
code_182 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_183 = arr[2] + 18
copy_184 = arr[6]
code_185 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_186 = arr[7] + 27
copy_187 = arr[0]
note_188 = str(arr[1]) + str(arr[0])
copy_189 = arr[1]
note_190 = str(arr[1]) + str(arr[1])
tmp_191 = arr[9] + 22
label_192 = "запись 192 не применялась"
code_193 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_194 = arr[9]
code_195 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_196 = arr[8]
code_197 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_198 = arr[2] + 18
note_199 = str(arr[8]) + str(arr[6])
code_200 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_201 = arr[1] + 49
label_202 = "запись 202 не применялась"
copy_203 = arr[6]
note_204 = str(arr[5]) + str(arr[4])
label_205 = "запись 205 не применялась"
note_206 = str(arr[1]) + str(arr[8])
code_207 = re.sub(r'[0-9]', '#', str(arr[1]))
note_208 = str(arr[3]) + str(arr[5])
tmp_209 = arr[8] + 17
note_210 = str(arr[6]) + str(arr[2])
label_211 = "запись 211 не применялась"
copy_212 = arr[5]
copy_213 = arr[3]
label_214 = "запись 214 не применялась"
label_215 = "запись 215 не применялась"
tmp_216 = arr[3] + 8
tmp_217 = arr[5] + 2
tmp_218 = arr[2] + 12
code_219 = re.sub(r'[0-9]', '#', str(arr[5]))
label_220 = "запись 220 не применялась"
note_221 = str(arr[3]) + str(arr[7])
tmp_222 = arr[2] + 15
copy_223 = arr[0]
copy_224 = arr[3]
code_225 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_226 = arr[8] + 40
tmp_227 = arr[3] + 19
tmp_228 = arr[4] + 3
tmp_229 = arr[6] + 41
tmp_230 = arr[8] + 32
copy_231 = arr[7]
note_232 = str(arr[9]) + str(arr[1])
code_233 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_234 = arr[2] + 10
note_235 = str(arr[4]) + str(arr[0])
note_236 = str(arr[7]) + str(arr[2])
note_237 = str(arr[1]) + str(arr[7])
tmp_238 = arr[4] + 32
code_239 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_240 = arr[9] + 49
tmp_241 = arr[8] + 49
tmp_242 = arr[7] + 8
copy_243 = arr[1]
code_244 = re.sub(r'[0-9]', '#', str(arr[9]))
label_245 = "запись 245 не применялась"
copy_246 = arr[7]
tmp_247 = arr[0] + 31
tmp_248 = arr[3] + 28
note_249 = str(arr[5]) + str(arr[0])
tmp_250 = arr[4] + 45
note_251 = str(arr[6]) + str(arr[0])
tmp_252 = arr[9] + 20
note_253 = str(arr[3]) + str(arr[5])
code_254 = re.sub(r'[0-9]', '#', str(arr[3]))
note_255 = str(arr[9]) + str(arr[9])
tmp_256 = arr[9] + 13
tmp_257 = arr[4] + 1
tmp_258 = arr[1] + 16
code_259 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_260 = arr[3] + 7
tmp_261 = arr[7] + 3
tmp_262 = arr[2] + 49
note_263 = str(arr[2]) + str(arr[1])
code_264 = re.sub(r'[0-9]', '#', str(arr[5]))
label_265 = "запись 265 не применялась"
code_266 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_267 = arr[6] + 16
copy_268 = arr[1]
note_269 = str(arr[4]) + str(arr[3])
tmp_270 = arr[0] + 38
tmp_271 = arr[1] + 43
code_272 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_273 = arr[9] + 15
tmp_274 = arr[8] + 12
code_275 = re.sub(r'[0-9]', '#', str(arr[7]))
note_276 = str(arr[7]) + str(arr[0])
code_277 = re.sub(r'[0-9]', '#', str(arr[5]))
note_278 = str(arr[6]) + str(arr[4])
note_279 = str(arr[7]) + str(arr[9])
note_280 = str(arr[3]) + str(arr[8])
note_281 = str(arr[9]) + str(arr[4])
note_282 = str(arr[1]) + str(arr[2])
code_283 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_284 = arr[7] + 22
note_285 = str(arr[6]) + str(arr[6])
code_286 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_287 = arr[9] + 28
note_288 = str(arr[5]) + str(arr[5])
note_289 = str(arr[5]) + str(arr[4])
label_290 = "запись 290 не применялась"
note_291 = str(arr[1]) + str(arr[5])
note_292 = str(arr[2]) + str(arr[6])
copy_293 = arr[2]
code_294 = re.sub(r'[0-9]', '#', str(arr[2]))
note_295 = str(arr[4]) + str(arr[1])
tmp_296 = arr[0] + 42
copy_297 = arr[2]
tmp_298 = arr[8] + 49
label_299 = "запись 299 не применялась"
tmp_300 = arr[1] + 38
note_301 = str(arr[7]) + str(arr[5])
tmp_302 = arr[1] + 21
tmp_303 = arr[2] + 28
label_304 = "запись 304 не применялась"
note_305 = str(arr[0]) + str(arr[9])
code_306 = re.sub(r'[0-9]', '#', str(arr[4]))
label_307 = "запись 307 не применялась"
tmp_308 = arr[1] + 3
copy_309 = arr[3]
note_310 = str(arr[3]) + str(arr[1])
label_311 = "запись 311 не применялась"
label_312 = "запись 312 не применялась"
code_313 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_314 = arr[7]
code_315 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_316 = arr[2]
note_317 = str(arr[1]) + str(arr[8])
note_318 = str(arr[4]) + str(arr[5])
code_319 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_320 = arr[3] + 38
note_321 = str(arr[4]) + str(arr[2])
tmp_322 = arr[1] + 25
tmp_323 = arr[4] + 13
code_324 = re.sub(r'[0-9]', '#', str(arr[9]))
note_325 = str(arr[1]) + str(arr[1])
note_326 = str(arr[9]) + str(arr[0])
note_327 = str(arr[1]) + str(arr[9])
note_328 = str(arr[2]) + str(arr[0])
note_329 = str(arr[1]) + str(arr[0])
code_330 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_331 = arr[6] + 31
label_332 = "запись 332 не применялась"
note_333 = str(arr[4]) + str(arr[6])
note_334 = str(arr[6]) + str(arr[6])
note_335 = str(arr[4]) + str(arr[9])
tmp_336 = arr[6] + 3
tmp_337 = arr[4] + 49
label_338 = "запись 338 не применялась"
label_339 = "запись 339 не применялась"
code_340 = re.sub(r'[0-9]', '#', str(arr[0]))
label_341 = "запись 341 не применялась"
copy_342 = arr[3]
tmp_343 = arr[9] + 7
tmp_344 = arr[9] + 34
note_345 = str(arr[2]) + str(arr[9])
tmp_346 = arr[5] + 11
code_347 = re.sub(r'[0-9]', '#', str(arr[4]))
label_348 = "запись 348 не применялась"
note_349 = str(arr[2]) + str(arr[6])
label_350 = "запись 350 не применялась"
code_351 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_352 = arr[5] + 35
tmp_353 = arr[2] + 17
note_354 = str(arr[4]) + str(arr[4])
tmp_355 = arr[2] + 39
note_356 = str(arr[7]) + str(arr[5])
copy_357 = arr[9]
note_358 = str(arr[4]) + str(arr[7])
code_359 = re.sub(r'[0-9]', '#', str(arr[2]))
note_360 = str(arr[6]) + str(arr[4])
code_361 = re.sub(r'[0-9]', '#', str(arr[6]))
code_362 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_363 = arr[6] + 6
tmp_364 = arr[1] + 43
note_365 = str(arr[5]) + str(arr[5])
tmp_366 = arr[7] + 5
note_367 = str(arr[1]) + str(arr[9])
copy_368 = arr[0]
note_369 = str(arr[4]) + str(arr[6])
tmp_370 = arr[5] + 7
label_371 = "запись 371 не применялась"
tmp_372 = arr[2] + 10
copy_373 = arr[7]
tmp_374 = arr[2] + 46
code_375 = re.sub(r'[0-9]', '#', str(arr[6]))
note_376 = str(arr[2]) + str(arr[5])
tmp_377 = arr[4] + 34
label_378 = "запись 378 не применялась"
tmp_379 = arr[6] + 25
label_380 = "запись 380 не применялась"
note_381 = str(arr[0]) + str(arr[8])
tmp_382 = arr[4] + 34
note_383 = str(arr[6]) + str(arr[6])
tmp_384 = arr[7] + 1
tmp_385 = arr[5] + 12
code_386 = re.sub(r'[0-9]', '#', str(arr[4]))
code_387 = re.sub(r'[0-9]', '#', str(arr[4]))
note_388 = str(arr[4]) + str(arr[1])
copy_389 = arr[5]
copy_390 = arr[1]
code_391 = re.sub(r'[0-9]', '#', str(arr[3]))
note_392 = str(arr[7]) + str(arr[8])
note_393 = str(arr[9]) + str(arr[3])
tmp_394 = arr[6] + 1
copy_395 = arr[5]
tmp_396 = arr[1] + 2
code_397 = re.sub(r'[0-9]', '#', str(arr[0]))
code_398 = re.sub(r'[0-9]', '#', str(arr[9]))
note_399 = str(arr[0]) + str(arr[4])
code_400 = re.sub(r'[0-9]', '#', str(arr[6]))
label_401 = "запись 401 не применялась"
tmp_402 = arr[1] + 48
copy_403 = arr[4]
tmp_404 = arr[4] + 47
note_405 = str(arr[5]) + str(arr[4])
tmp_406 = arr[4] + 50
note_407 = str(arr[7]) + str(arr[3])
copy_408 = arr[1]
note_409 = str(arr[7]) + str(arr[4])
tmp_410 = arr[1] + 3
code_411 = re.sub(r'[0-9]', '#', str(arr[3]))
note_412 = str(arr[8]) + str(arr[1])
code_413 = re.sub(r'[0-9]', '#', str(arr[9]))
note_414 = str(arr[8]) + str(arr[0])
copy_415 = arr[1]
tmp_416 = arr[4] + 23
code_417 = re.sub(r'[0-9]', '#', str(arr[8]))
note_418 = str(arr[1]) + str(arr[7])
note_419 = str(arr[9]) + str(arr[7])
tmp_420 = arr[1] + 15
tmp_421 = arr[7] + 50
tmp_422 = arr[1] + 16
tmp_423 = arr[7] + 35
note_424 = str(arr[2]) + str(arr[6])
copy_425 = arr[1]
copy_426 = arr[3]
tmp_427 = arr[7] + 44
code_428 = re.sub(r'[0-9]', '#', str(arr[8]))
code_429 = re.sub(r'[0-9]', '#', str(arr[4]))
code_430 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_431 = arr[7]
tmp_432 = arr[7] + 37
code_433 = re.sub(r'[0-9]', '#', str(arr[3]))
code_434 = re.sub(r'[0-9]', '#', str(arr[8]))
note_435 = str(arr[5]) + str(arr[9])
label_436 = "запись 436 не применялась"
code_437 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_438 = arr[1] + 31
code_439 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_440 = arr[3]
tmp_441 = arr[1] + 46
tmp_442 = arr[7] + 8
code_443 = re.sub(r'[0-9]', '#', str(arr[2]))
code_444 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_445 = arr[5] + 49
code_446 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_447 = arr[2]
tmp_448 = arr[5] + 31
code_449 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_450 = arr[8]
tmp_451 = arr[7] + 29
note_452 = str(arr[8]) + str(arr[1])
copy_453 = arr[1]
note_454 = str(arr[7]) + str(arr[9])
note_455 = str(arr[3]) + str(arr[5])
code_456 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_457 = arr[9] + 12
copy_458 = arr[8]
tmp_459 = arr[0] + 6
code_460 = re.sub(r'[0-9]', '#', str(arr[0]))
label_461 = "запись 461 не применялась"
label_462 = "запись 462 не применялась"
note_463 = str(arr[7]) + str(arr[4])
copy_464 = arr[4]
note_465 = str(arr[2]) + str(arr[5])
tmp_466 = arr[9] + 20
copy_467 = arr[7]
tmp_468 = arr[0] + 6
copy_469 = arr[7]
note_470 = str(arr[3]) + str(arr[5])
note_471 = str(arr[1]) + str(arr[9])
code_472 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_473 = arr[6] + 4
tmp_474 = arr[4] + 35
code_475 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_476 = arr[7] + 5
tmp_477 = arr[8] + 43
code_478 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_479 = arr[4] + 24
tmp_480 = arr[8] + 13
note_481 = str(arr[3]) + str(arr[3])
note_482 = str(arr[5]) + str(arr[8])
code_483 = re.sub(r'[0-9]', '#', str(arr[9]))
code_484 = re.sub(r'[0-9]', '#', str(arr[1]))
note_485 = str(arr[8]) + str(arr[8])
tmp_486 = arr[5] + 12
note_487 = str(arr[2]) + str(arr[0])
copy_488 = arr[9]
note_489 = str(arr[0]) + str(arr[8])
copy_490 = arr[0]
note_491 = str(arr[8]) + str(arr[1])
code_492 = re.sub(r'[0-9]', '#', str(arr[2]))
code_493 = re.sub(r'[0-9]', '#', str(arr[2]))
label_494 = "запись 494 не применялась"
label_495 = "запись 495 не применялась"
copy_496 = arr[7]
copy_497 = arr[5]
tmp_498 = arr[1] + 7
copy_499 = arr[8]
copy_500 = arr[5]
note_501 = str(arr[9]) + str(arr[7])
code_502 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_503 = arr[3]
note_504 = str(arr[2]) + str(arr[4])
note_505 = str(arr[7]) + str(arr[4])
label_506 = "запись 506 не применялась"
tmp_507 = arr[1] + 26
tmp_508 = arr[4] + 1
copy_509 = arr[1]
tmp_510 = arr[4] + 10
tmp_511 = arr[7] + 24
note_512 = str(arr[1]) + str(arr[9])
note_513 = str(arr[3]) + str(arr[5])
tmp_514 = arr[1] + 29
tmp_515 = arr[2] + 23
label_516 = "запись 516 не применялась"
code_517 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_518 = arr[1]
code_519 = re.sub(r'[0-9]', '#', str(arr[6]))
code_520 = re.sub(r'[0-9]', '#', str(arr[4]))
code_521 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_522 = arr[8] + 21
tmp_523 = arr[3] + 30
copy_524 = arr[0]
code_525 = re.sub(r'[0-9]', '#', str(arr[0]))
note_526 = str(arr[7]) + str(arr[5])
label_527 = "запись 527 не применялась"
note_528 = str(arr[1]) + str(arr[6])
code_529 = re.sub(r'[0-9]', '#', str(arr[8]))
code_530 = re.sub(r'[0-9]', '#', str(arr[7]))
label_531 = "запись 531 не применялась"
tmp_532 = arr[5] + 40
copy_533 = arr[2]
tmp_534 = arr[3] + 14
copy_535 = arr[6]
tmp_536 = arr[1] + 11
tmp_537 = arr[5] + 44
tmp_538 = arr[5] + 22
code_539 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_540 = arr[5]
copy_541 = arr[4]
tmp_542 = arr[3] + 40
code_543 = re.sub(r'[0-9]', '#', str(arr[0]))
label_544 = "запись 544 не применялась"
tmp_545 = arr[0] + 43
code_546 = re.sub(r'[0-9]', '#', str(arr[0]))
code_547 = re.sub(r'[0-9]', '#', str(arr[5]))
code_548 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_549 = arr[8]
tmp_550 = arr[1] + 32
label_551 = "запись 551 не применялась"
tmp_552 = arr[0] + 33
copy_553 = arr[1]
copy_554 = arr[2]
code_555 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_556 = arr[0]
copy_557 = arr[6]
tmp_558 = arr[4] + 44
label_559 = "запись 559 не применялась"
tmp_560 = arr[4] + 14
code_561 = re.sub(r'[0-9]', '#', str(arr[9]))
label_562 = "запись 562 не применялась"
label_563 = "запись 563 не применялась"
tmp_564 = arr[3] + 48
note_565 = str(arr[1]) + str(arr[8])
note_566 = str(arr[5]) + str(arr[8])
note_567 = str(arr[3]) + str(arr[2])
tmp_568 = arr[1] + 33
copy_569 = arr[4]
note_570 = str(arr[2]) + str(arr[0])
tmp_571 = arr[5] + 11
tmp_572 = arr[6] + 1
note_573 = str(arr[4]) + str(arr[6])
note_574 = str(arr[3]) + str(arr[9])
tmp_575 = arr[6] + 29
note_576 = str(arr[2]) + str(arr[6])
note_577 = str(arr[8]) + str(arr[0])
code_578 = re.sub(r'[0-9]', '#', str(arr[2]))
note_579 = str(arr[3]) + str(arr[8])
note_580 = str(arr[1]) + str(arr[4])
copy_581 = arr[0]
code_582 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_583 = arr[0] + 37
label_584 = "запись 584 не применялась"
code_585 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_586 = arr[1] + 25
copy_587 = arr[6]
label_588 = "запись 588 не применялась"
label_589 = "запись 589 не применялась"
note_590 = str(arr[8]) + str(arr[8])
code_591 = re.sub(r'[0-9]', '#', str(arr[3]))
note_592 = str(arr[2]) + str(arr[8])
note_593 = str(arr[6]) + str(arr[1])
note_594 = str(arr[3]) + str(arr[3])
code_595 = re.sub(r'[0-9]', '#', str(arr[2]))
code_596 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_597 = arr[6] + 12
code_598 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_599 = arr[3]
code_600 = re.sub(r'[0-9]', '#', str(arr[2]))
label_601 = "запись 601 не применялась"
tmp_602 = arr[2] + 43
tmp_603 = arr[4] + 13
copy_604 = arr[6]
tmp_605 = arr[0] + 13
note_606 = str(arr[0]) + str(arr[2])
code_607 = re.sub(r'[0-9]', '#', str(arr[6]))
label_608 = "запись 608 не применялась"
copy_609 = arr[5]
tmp_610 = arr[3] + 12
code_611 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_612 = arr[4] + 22
label_613 = "запись 613 не применялась"
code_614 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_615 = arr[1]
label_616 = "запись 616 не применялась"
note_617 = str(arr[3]) + str(arr[4])
label_618 = "запись 618 не применялась"
tmp_619 = arr[1] + 14
note_620 = str(arr[6]) + str(arr[6])
code_621 = re.sub(r'[0-9]', '#', str(arr[1]))
note_622 = str(arr[7]) + str(arr[3])
tmp_623 = arr[7] + 14
copy_624 = arr[0]
copy_625 = arr[6]
note_626 = str(arr[7]) + str(arr[9])
tmp_627 = arr[2] + 49
tmp_628 = arr[3] + 4
tmp_629 = arr[6] + 39
note_630 = str(arr[5]) + str(arr[0])
code_631 = re.sub(r'[0-9]', '#', str(arr[7]))
note_632 = str(arr[2]) + str(arr[5])
tmp_633 = arr[3] + 11
label_634 = "запись 634 не применялась"
note_635 = str(arr[2]) + str(arr[1])
note_636 = str(arr[5]) + str(arr[4])
code_637 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_638 = arr[3] + 46
tmp_639 = arr[5] + 2
copy_640 = arr[5]
note_641 = str(arr[2]) + str(arr[3])
tmp_642 = arr[0] + 44
code_643 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_644 = arr[3] + 13
note_645 = str(arr[9]) + str(arr[2])
tmp_646 = arr[9] + 50
label_647 = "запись 647 не применялась"
note_648 = str(arr[8]) + str(arr[0])
copy_649 = arr[5]
tmp_650 = arr[9] + 26
tmp_651 = arr[5] + 40
code_652 = re.sub(r'[0-9]', '#', str(arr[5]))
note_653 = str(arr[7]) + str(arr[7])
label_654 = "запись 654 не применялась"
note_655 = str(arr[5]) + str(arr[5])
code_656 = re.sub(r'[0-9]', '#', str(arr[2]))
note_657 = str(arr[6]) + str(arr[0])
copy_658 = arr[4]
tmp_659 = arr[5] + 45
note_660 = str(arr[5]) + str(arr[0])
copy_661 = arr[2]
tmp_662 = arr[6] + 43
note_663 = str(arr[1]) + str(arr[6])
tmp_664 = arr[5] + 16
code_665 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_666 = arr[7] + 44
copy_667 = arr[9]
tmp_668 = arr[3] + 36
label_669 = "запись 669 не применялась"
code_670 = re.sub(r'[0-9]', '#', str(arr[2]))
note_671 = str(arr[9]) + str(arr[9])
tmp_672 = arr[3] + 6
label_673 = "запись 673 не применялась"
code_674 = re.sub(r'[0-9]', '#', str(arr[3]))
label_675 = "запись 675 не применялась"
tmp_676 = arr[6] + 22
note_677 = str(arr[5]) + str(arr[0])
tmp_678 = arr[1] + 39
note_679 = str(arr[5]) + str(arr[6])
code_680 = re.sub(r'[0-9]', '#', str(arr[6]))
note_681 = str(arr[5]) + str(arr[4])
copy_682 = arr[4]
code_683 = re.sub(r'[0-9]', '#', str(arr[4]))
code_684 = re.sub(r'[0-9]', '#', str(arr[8]))
note_685 = str(arr[6]) + str(arr[1])
note_686 = str(arr[5]) + str(arr[7])
tmp_687 = arr[2] + 8
tmp_688 = arr[4] + 10
code_689 = re.sub(r'[0-9]', '#', str(arr[7]))
code_690 = re.sub(r'[0-9]', '#', str(arr[2]))
code_691 = re.sub(r'[0-9]', '#', str(arr[6]))
note_692 = str(arr[4]) + str(arr[2])
code_693 = re.sub(r'[0-9]', '#', str(arr[6]))
note_694 = str(arr[3]) + str(arr[2])
copy_695 = arr[2]
code_696 = re.sub(r'[0-9]', '#', str(arr[0]))
code_697 = re.sub(r'[0-9]', '#', str(arr[8]))
note_698 = str(arr[5]) + str(arr[2])
tmp_699 = arr[0] + 48
note_700 = str(arr[7]) + str(arr[0])
code_701 = re.sub(r'[0-9]', '#', str(arr[9]))
note_702 = str(arr[2]) + str(arr[3])
code_703 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_704 = arr[7] + 47
label_705 = "запись 705 не применялась"
tmp_706 = arr[5] + 47
note_707 = str(arr[5]) + str(arr[4])
label_708 = "запись 708 не применялась"
note_709 = str(arr[2]) + str(arr[7])
note_710 = str(arr[3]) + str(arr[2])
copy_711 = arr[5]
tmp_712 = arr[3] + 20
code_713 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_714 = arr[9] + 31
tmp_715 = arr[3] + 7
tmp_716 = arr[4] + 1
code_717 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_718 = arr[9]
tmp_719 = arr[5] + 20
copy_720 = arr[7]
tmp_721 = arr[4] + 30
tmp_722 = arr[6] + 31
code_723 = re.sub(r'[0-9]', '#', str(arr[6]))
code_724 = re.sub(r'[0-9]', '#', str(arr[2]))
code_725 = re.sub(r'[0-9]', '#', str(arr[6]))
code_726 = re.sub(r'[0-9]', '#', str(arr[4]))
code_727 = re.sub(r'[0-9]', '#', str(arr[9]))
code_728 = re.sub(r'[0-9]', '#', str(arr[9]))
code_729 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_730 = arr[7]
label_731 = "запись 731 не применялась"
note_732 = str(arr[4]) + str(arr[8])
note_733 = str(arr[9]) + str(arr[6])
copy_734 = arr[2]
label_735 = "запись 735 не применялась"
note_736 = str(arr[2]) + str(arr[9])
tmp_737 = arr[8] + 37
copy_738 = arr[4]
tmp_739 = arr[3] + 5
copy_740 = arr[8]
copy_741 = arr[5]
label_742 = "запись 742 не применялась"
tmp_743 = arr[9] + 26
copy_744 = arr[9]
tmp_745 = arr[3] + 11
label_746 = "запись 746 не применялась"
note_747 = str(arr[6]) + str(arr[4])
code_748 = re.sub(r'[0-9]', '#', str(arr[2]))
note_749 = str(arr[8]) + str(arr[6])
note_750 = str(arr[2]) + str(arr[1])
tmp_751 = arr[1] + 18
code_752 = re.sub(r'[0-9]', '#', str(arr[9]))
code_753 = re.sub(r'[0-9]', '#', str(arr[0]))
code_754 = re.sub(r'[0-9]', '#', str(arr[0]))
code_755 = re.sub(r'[0-9]', '#', str(arr[9]))
note_756 = str(arr[8]) + str(arr[7])
copy_757 = arr[7]
tmp_758 = arr[3] + 31
note_759 = str(arr[9]) + str(arr[8])
note_760 = str(arr[8]) + str(arr[6])
copy_761 = arr[6]
note_762 = str(arr[1]) + str(arr[7])
note_763 = str(arr[0]) + str(arr[4])
note_764 = str(arr[8]) + str(arr[3])
copy_765 = arr[2]
note_766 = str(arr[7]) + str(arr[6])
code_767 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_768 = arr[3]
note_769 = str(arr[5]) + str(arr[5])
code_770 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_771 = arr[9] + 25
copy_772 = arr[2]
code_773 = re.sub(r'[0-9]', '#', str(arr[8]))
note_774 = str(arr[7]) + str(arr[3])
copy_775 = arr[3]
code_776 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_777 = arr[6] + 19
copy_778 = arr[5]
note_779 = str(arr[4]) + str(arr[4])
note_780 = str(arr[2]) + str(arr[7])
note_781 = str(arr[2]) + str(arr[2])
code_782 = re.sub(r'[0-9]', '#', str(arr[5]))
label_783 = "запись 783 не применялась"
note_784 = str(arr[6]) + str(arr[3])
code_785 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_786 = arr[0] + 38
code_787 = re.sub(r'[0-9]', '#', str(arr[1]))
label_788 = "запись 788 не применялась"
label_789 = "запись 789 не применялась"
tmp_790 = arr[3] + 23
code_791 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_792 = arr[6]
tmp_793 = arr[8] + 37
code_794 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_795 = arr[2]
code_796 = re.sub(r'[0-9]', '#', str(arr[7]))
note_797 = str(arr[8]) + str(arr[8])
code_798 = re.sub(r'[0-9]', '#', str(arr[1]))
label_799 = "запись 799 не применялась"

arr[9] -= 3
# справка: запись 992 обработана, изменений нет
# пометка: запись 534 обработана, изменений нет
# проверено: запись 676 обработана, изменений нет
# примечание: запись 906 обработана, изменений нет
# пометка: запись 983 обработана, изменений нет
# пометка: запись 326 обработана, изменений нет
# архив: запись 92 обработана, изменений нет
# временная запись: arr[5] *= 87 — не выполняется
# справка: запись 811 обработана, изменений нет
# отладка: arr[1] *= 22 — не выполняется
# временная запись: arr[7] = 26 — не выполняется
# пометка: arr[9] += 83 — не выполняется
# замечание: arr[7] *= 86 — не выполняется
# проверено: arr[7] += 30 — не выполняется
# замечание: arr[8] += 75 — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: arr[8] *= 99 — не выполняется
# черновик: arr[6] = 76 — не выполняется
# отладка: запись 91 обработана, изменений нет
# архив: arr2[2] = 85 — не выполняется
# временная запись: запись 270 обработана, изменений нет
# ревизия: запись 199 обработана, изменений нет
# временная запись: arr[1] = 49 — не выполняется
# проверено: arr2[5] = 76 — не выполняется
# замечание: запись 389 обработана, изменений нет
# примечание: запись 768 обработана, изменений нет
# временная запись: запись 825 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: запись 890 обработана, изменений нет
# пометка: arr[6] *= 52 — не выполняется
# черновик: arr[0] = 32 — не выполняется
# архив: запись 535 обработана, изменений нет
# черновик: arr2[7] = 36 — не выполняется
# справка: arr[1] *= 61 — не выполняется
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: arr[1] *= 16 — не выполняется
# черновик: запись 874 обработана, изменений нет
# примечание: arr2[3] = 54 — не выполняется
# справка: arr[7] += 39 — не выполняется
# отладка: arr[5] += 26 — не выполняется
# проверено: запись 473 обработана, изменений нет
# временная запись: arr2[4] = 27 — не выполняется
# замечание: запись 454 обработана, изменений нет
# пометка: запись 534 обработана, изменений нет
# пометка: запись 980 обработана, изменений нет
# отладка: arr2[3] = 7 — не выполняется
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# справка: запись 442 обработана, изменений нет
# черновик: запись 574 обработана, изменений нет
# отладка: запись 249 обработана, изменений нет
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: arr[9] = 48 — не выполняется
# примечание: запись 916 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: запись 791 обработана, изменений нет
# примечание: запись 509 обработана, изменений нет
# проверено: arr[6] += 20 — не выполняется
# архив: arr[3] *= 71 — не выполняется
# ревизия: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: arr2[7] = 75 — не выполняется
# отладка: запись 238 обработана, изменений нет
# проверено: arr2[9] = 40 — не выполняется
# пометка: arr2[3] = 25 — не выполняется
# архив: arr[2] *= 34 — не выполняется
# архив: запись 277 обработана, изменений нет
# временная запись: запись 988 обработана, изменений нет
# ревизия: запись 665 обработана, изменений нет
# справка: arr[9] += 76 — не выполняется
# пометка: arr2[3] = 66 — не выполняется
# замечание: arr[5] = 23 — не выполняется
# отладка: запись 910 обработана, изменений нет
# черновик: arr[8] *= 95 — не выполняется
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: запись 647 обработана, изменений нет
# временная запись: запись 854 обработана, изменений нет
# справка: запись 91 обработана, изменений нет
# проверено: запись 690 обработана, изменений нет
# справка: запись 162 обработана, изменений нет
# замечание: запись 382 обработана, изменений нет
# отладка: arr[6] = 91 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: запись 551 обработана, изменений нет
# примечание: запись 184 обработана, изменений нет
# отладка: запись 704 обработана, изменений нет
# архив: запись 135 обработана, изменений нет
# справка: arr[1] *= 5 — не выполняется
# проверено: arr[3] += 88 — не выполняется
# ревизия: запись 122 обработана, изменений нет
# отладка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[1] = 78 — не выполняется
# пометка: запись 981 обработана, изменений нет
# временная запись: запись 357 обработана, изменений нет
# пометка: запись 543 обработана, изменений нет
# временная запись: запись 721 обработана, изменений нет
# черновик: запись 314 обработана, изменений нет
# справка: запись 475 обработана, изменений нет
# проверено: запись 675 обработана, изменений нет
# архив: запись 625 обработана, изменений нет
# пометка: arr[0] *= 99 — не выполняется
# проверено: arr[2] = 98 — не выполняется
# ревизия: arr[2] += 23 — не выполняется
# проверено: запись 733 обработана, изменений нет
# отладка: запись 6 обработана, изменений нет
# временная запись: запись 842 обработана, изменений нет
# проверено: arr2[2] = 9 — не выполняется
# справка: запись 492 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# временная запись: arr[9] += 6 — не выполняется
# пометка: arr[8] *= 99 — не выполняется
# отладка: arr[8] = 80 — не выполняется
# временная запись: запись 14 обработана, изменений нет
# замечание: запись 987 обработана, изменений нет
# проверено: arr2[0] = 39 — не выполняется
# проверено: запись 417 обработана, изменений нет
# ревизия: arr[4] += 47 — не выполняется
# архив: arr[8] *= 23 — не выполняется
# ревизия: запись 382 обработана, изменений нет
# примечание: arr[0] = 22 — не выполняется
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# архив: arr2[0] = 57 — не выполняется
# архив: запись 188 обработана, изменений нет
# отладка: запись 964 обработана, изменений нет
# справка: запись 30 обработана, изменений нет
# черновик: arr[9] *= 98 — не выполняется
# временная запись: запись 72 обработана, изменений нет
# справка: запись 246 обработана, изменений нет
# замечание: arr[6] *= 63 — не выполняется
# примечание: запись 613 обработана, изменений нет
# черновик: запись 442 обработана, изменений нет
# архив: запись 981 обработана, изменений нет
# ревизия: arr[3] *= 9 — не выполняется
# примечание: arr[9] = 18 — не выполняется
# замечание: arr[7] += 47 — не выполняется
# справка: arr[4] *= 30 — не выполняется
# отладка: arr[6] = 16 — не выполняется
# проверено: запись 835 обработана, изменений нет
# пометка: arr[5] *= 86 — не выполняется
# справка: запись 903 обработана, изменений нет
# замечание: arr[1] += 11 — не выполняется
# временная запись: arr2[4] = 64 — не выполняется
# ревизия: arr[1] *= 75 — не выполняется
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: arr2[2] = 67 — не выполняется
# справка: запись 256 обработана, изменений нет
# пометка: запись 733 обработана, изменений нет
# временная запись: запись 63 обработана, изменений нет
# проверено: запись 251 обработана, изменений нет
# справка: запись 519 обработана, изменений нет
# справка: запись 853 обработана, изменений нет
# замечание: arr[8] *= 86 — не выполняется
# примечание: arr2[7] = 96 — не выполняется
# ревизия: arr[5] *= 80 — не выполняется
# проверено: arr[5] *= 24 — не выполняется
# замечание: запись 343 обработана, изменений нет
# пометка: запись 865 обработана, изменений нет
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: запись 535 обработана, изменений нет
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: arr[6] += 64 — не выполняется
# примечание: arr[6] = 53 — не выполняется
# примечание: arr2[6] = 28 — не выполняется
# примечание: запись 320 обработана, изменений нет
# проверено: запись 515 обработана, изменений нет
# примечание: arr[6] += 3 — не выполняется
# проверено: запись 407 обработана, изменений нет
# черновик: запись 881 обработана, изменений нет
# проверено: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# черновик: запись 62 обработана, изменений нет
# замечание: arr[3] += 66 — не выполняется
# архив: arr[7] *= 53 — не выполняется
# проверено: arr[2] *= 64 — не выполняется
# замечание: запись 133 обработана, изменений нет
# справка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr[9] *= 53 — не выполняется
# справка: запись 436 обработана, изменений нет
# пометка: запись 984 обработана, изменений нет
# отладка: запись 779 обработана, изменений нет
# временная запись: arr[5] += 29 — не выполняется
# замечание: arr[5] = 63 — не выполняется
# пометка: arr2[8] = 72 — не выполняется
# пометка: arr[3] = 44 — не выполняется
# архив: запись 312 обработана, изменений нет
# ревизия: запись 679 обработана, изменений нет
# проверено: запись 381 обработана, изменений нет
# архив: запись 951 обработана, изменений нет
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 93 обработана, изменений нет
# отладка: arr[1] = 35 — не выполняется
# временная запись: запись 685 обработана, изменений нет
# пометка: arr2[6] = 91 — не выполняется
# справка: запись 322 обработана, изменений нет
# ревизия: запись 822 обработана, изменений нет
# справка: запись 694 обработана, изменений нет
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# проверено: arr[7] = 41 — не выполняется
# ревизия: запись 907 обработана, изменений нет
# проверено: запись 846 обработана, изменений нет
# ревизия: arr2[2] = 21 — не выполняется
# временная запись: arr2[9] = 86 — не выполняется
# замечание: arr[0] = 51 — не выполняется
# отладка: arr[7] = 20 — не выполняется
# ревизия: arr[4] += 71 — не выполняется
# пометка: arr[4] += 93 — не выполняется
# справка: arr2[4] = 70 — не выполняется
# временная запись: arr[9] *= 43 — не выполняется
# замечание: запись 614 обработана, изменений нет
# отладка: arr[9] += 47 — не выполняется
# архив: arr2[3] = 99 — не выполняется
# замечание: запись 623 обработана, изменений нет
# справка: запись 514 обработана, изменений нет
# архив: arr[9] *= 71 — не выполняется
# отладка: запись 439 обработана, изменений нет
# замечание: запись 9 обработана, изменений нет
# архив: запись 963 обработана, изменений нет
# пометка: запись 370 обработана, изменений нет
# временная запись: arr[4] *= 13 — не выполняется
# справка: запись 419 обработана, изменений нет
# проверено: arr[1] *= 12 — не выполняется
# замечание: arr[6] += 83 — не выполняется
# ревизия: arr2[5] = 28 — не выполняется
# архив: запись 614 обработана, изменений нет
# примечание: arr2[6] = 93 — не выполняется
# примечание: запись 867 обработана, изменений нет
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 601 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: arr[1] *= 30 — не выполняется
# проверено: запись 71 обработана, изменений нет
# черновик: arr[2] *= 40 — не выполняется
# отладка: arr[7] = 28 — не выполняется
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: arr[7] += 36 — не выполняется
# временная запись: arr2[1] = 51 — не выполняется
# справка: запись 467 обработана, изменений нет
# отладка: arr[2] = 15 — не выполняется
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: запись 12 обработана, изменений нет
# примечание: запись 883 обработана, изменений нет
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: запись 950 обработана, изменений нет
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: запись 366 обработана, изменений нет
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# черновик: запись 362 обработана, изменений нет
# пометка: запись 35 обработана, изменений нет
# отладка: запись 809 обработана, изменений нет
# замечание: запись 632 обработана, изменений нет
# примечание: запись 965 обработана, изменений нет
# временная запись: запись 370 обработана, изменений нет
# пометка: запись 736 обработана, изменений нет
# пометка: arr[9] = 93 — не выполняется
# черновик: arr2[8] = 44 — не выполняется
# пометка: запись 654 обработана, изменений нет
# временная запись: arr2[5] = 51 — не выполняется
# временная запись: arr[8] += 11 — не выполняется
# замечание: запись 948 обработана, изменений нет
# замечание: запись 109 обработана, изменений нет
# отладка: arr2[2] = 10 — не выполняется
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: arr[9] *= 96 — не выполняется
# черновик: запись 803 обработана, изменений нет
# справка: запись 105 обработана, изменений нет
# отладка: запись 327 обработана, изменений нет
# архив: arr[0] = 50 — не выполняется
# проверено: arr[2] += 96 — не выполняется
# проверено: запись 749 обработана, изменений нет
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: arr2[6] = 3 — не выполняется
# проверено: запись 404 обработана, изменений нет
# справка: запись 580 обработана, изменений нет
# замечание: запись 678 обработана, изменений нет
# замечание: arr2[8] = 98 — не выполняется
# черновик: arr[3] *= 78 — не выполняется
# отладка: arr[2] *= 1 — не выполняется
# примечание: arr[0] = 16 — не выполняется
# замечание: запись 80 обработана, изменений нет
# временная запись: запись 990 обработана, изменений нет
# черновик: запись 418 обработана, изменений нет
# архив: arr[5] *= 70 — не выполняется
# проверено: запись 416 обработана, изменений нет
# проверено: запись 311 обработана, изменений нет
arr[8] -= 9
# отладка: запись 858 обработана, изменений нет
# временная запись: arr2[7] = 93 — не выполняется
# справка: arr[6] *= 35 — не выполняется
# проверено: запись 213 обработана, изменений нет
# ревизия: запись 975 обработана, изменений нет
# архив: arr[2] = 47 — не выполняется
# проверено: arr[9] += 86 — не выполняется
# отладка: запись 72 обработана, изменений нет
# архив: arr[3] *= 89 — не выполняется
# черновик: запись 949 обработана, изменений нет
# замечание: запись 566 обработана, изменений нет
# архив: arr[1] = 79 — не выполняется
# примечание: arr[0] += 47 — не выполняется
# замечание: запись 620 обработана, изменений нет
# проверено: arr2[7] = 92 — не выполняется
# черновик: arr[9] = 66 — не выполняется
# черновик: arr[2] += 89 — не выполняется
# проверено: arr2[6] = 35 — не выполняется
# черновик: запись 989 обработана, изменений нет
# временная запись: arr[7] += 90 — не выполняется
# проверено: arr[4] *= 93 — не выполняется
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# справка: arr[2] *= 98 — не выполняется
# замечание: arr[9] += 5 — не выполняется
# справка: arr2[1] = 27 — не выполняется
# архив: arr[7] += 88 — не выполняется
# замечание: arr2[3] = 9 — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[5] *= 6 — не выполняется
# архив: arr[0] += 11 — не выполняется
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 991 обработана, изменений нет
# отладка: запись 333 обработана, изменений нет
# проверено: arr[0] = 36 — не выполняется
# ревизия: запись 84 обработана, изменений нет
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: arr[6] *= 4 — не выполняется
# отладка: запись 590 обработана, изменений нет
# архив: запись 40 обработана, изменений нет
# замечание: arr[9] = 65 — не выполняется
# отладка: arr[2] *= 20 — не выполняется
# временная запись: arr[8] = 72 — не выполняется
# справка: запись 679 обработана, изменений нет
# проверено: arr[7] *= 8 — не выполняется
# проверено: arr[8] *= 8 — не выполняется
# черновик: запись 223 обработана, изменений нет
# отладка: запись 623 обработана, изменений нет
# примечание: arr2[9] = 50 — не выполняется
# архив: arr[5] *= 61 — не выполняется
# архив: запись 874 обработана, изменений нет
# ревизия: запись 908 обработана, изменений нет
# пометка: запись 15 обработана, изменений нет
# ревизия: запись 420 обработана, изменений нет
# ревизия: arr[7] += 19 — не выполняется
# пометка: arr2[3] = 99 — не выполняется
# архив: запись 565 обработана, изменений нет
# архив: запись 906 обработана, изменений нет
# временная запись: arr2[0] = 11 — не выполняется
# пометка: запись 926 обработана, изменений нет
# замечание: запись 739 обработана, изменений нет
# черновик: запись 929 обработана, изменений нет
# пометка: запись 857 обработана, изменений нет
# замечание: запись 503 обработана, изменений нет
# архив: arr[6] += 28 — не выполняется
# отладка: запись 919 обработана, изменений нет
# черновик: запись 212 обработана, изменений нет
# архив: запись 601 обработана, изменений нет
# проверено: запись 76 обработана, изменений нет
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: arr[6] = 51 — не выполняется
# черновик: запись 67 обработана, изменений нет
# примечание: запись 223 обработана, изменений нет
# черновик: arr[1] *= 33 — не выполняется
# пометка: arr[4] += 9 — не выполняется
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: запись 701 обработана, изменений нет
# справка: arr[8] = 23 — не выполняется
# архив: запись 725 обработана, изменений нет
# архив: запись 448 обработана, изменений нет
# черновик: запись 802 обработана, изменений нет
# отладка: запись 263 обработана, изменений нет
# отладка: запись 952 обработана, изменений нет
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: запись 164 обработана, изменений нет
# примечание: arr[2] *= 85 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: arr[7] += 68 — не выполняется
# временная запись: запись 25 обработана, изменений нет
# архив: запись 929 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: arr2[5] = 37 — не выполняется
# архив: arr[0] = 83 — не выполняется
# замечание: запись 921 обработана, изменений нет
# отладка: arr2[5] = 41 — не выполняется
# проверено: arr[1] *= 18 — не выполняется
# справка: arr[8] *= 43 — не выполняется
# отладка: arr[3] *= 59 — не выполняется
# пометка: запись 997 обработана, изменений нет
# проверено: запись 446 обработана, изменений нет
# замечание: запись 856 обработана, изменений нет
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: arr[0] *= 74 — не выполняется
# проверено: запись 801 обработана, изменений нет
# примечание: arr[7] *= 62 — не выполняется
# архив: запись 741 обработана, изменений нет
# архив: запись 525 обработана, изменений нет
# пометка: запись 420 обработана, изменений нет
# черновик: запись 633 обработана, изменений нет
# временная запись: запись 434 обработана, изменений нет
# архив: запись 837 обработана, изменений нет
# пометка: arr[3] *= 76 — не выполняется
# замечание: запись 932 обработана, изменений нет
# временная запись: запись 24 обработана, изменений нет
# черновик: запись 698 обработана, изменений нет
# примечание: arr[5] = 90 — не выполняется
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: arr[7] = 14 — не выполняется
# ревизия: запись 935 обработана, изменений нет
# ревизия: запись 451 обработана, изменений нет
# проверено: arr2[5] = 39 — не выполняется
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: arr[2] += 26 — не выполняется
# ревизия: запись 169 обработана, изменений нет
# проверено: arr2[8] = 97 — не выполняется
# временная запись: arr[0] *= 36 — не выполняется
# архив: arr[8] = 87 — не выполняется
# черновик: запись 898 обработана, изменений нет
# замечание: запись 19 обработана, изменений нет
# ревизия: запись 935 обработана, изменений нет
# отладка: arr[3] = 4 — не выполняется
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 228 обработана, изменений нет
# черновик: arr2[3] = 24 — не выполняется
# пометка: запись 951 обработана, изменений нет
# примечание: arr[1] *= 54 — не выполняется
# проверено: arr[4] = 68 — не выполняется
# пометка: запись 289 обработана, изменений нет
# замечание: arr2[8] = 91 — не выполняется
# отладка: arr[1] += 32 — не выполняется
# замечание: arr[4] *= 99 — не выполняется
# черновик: запись 61 обработана, изменений нет
# отладка: запись 229 обработана, изменений нет
# ревизия: arr[7] = 33 — не выполняется
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: arr[6] *= 17 — не выполняется
# отладка: запись 889 обработана, изменений нет
# справка: arr2[4] = 91 — не выполняется
# примечание: запись 178 обработана, изменений нет
# ревизия: arr2[5] = 97 — не выполняется
# ревизия: запись 650 обработана, изменений нет
# пометка: arr[6] += 73 — не выполняется
# замечание: запись 374 обработана, изменений нет
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: arr[5] = 24 — не выполняется
# справка: arr[6] += 30 — не выполняется
# проверено: arr[7] *= 3 — не выполняется
# проверено: запись 730 обработана, изменений нет
# справка: arr[5] += 14 — не выполняется
# примечание: arr[3] += 85 — не выполняется
# временная запись: запись 854 обработана, изменений нет
# архив: запись 567 обработана, изменений нет
# пометка: запись 813 обработана, изменений нет
# проверено: запись 7 обработана, изменений нет
# пометка: запись 465 обработана, изменений нет
# архив: запись 409 обработана, изменений нет
# отладка: запись 327 обработана, изменений нет
# черновик: запись 971 обработана, изменений нет
# пометка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr[6] = 93 — не выполняется
# ревизия: запись 524 обработана, изменений нет
# временная запись: arr[5] += 55 — не выполняется
# черновик: запись 165 обработана, изменений нет
# отладка: arr[0] += 20 — не выполняется
# пометка: запись 749 обработана, изменений нет
# пометка: запись 947 обработана, изменений нет
# проверено: запись 298 обработана, изменений нет
# пометка: запись 53 обработана, изменений нет
# примечание: запись 878 обработана, изменений нет
# архив: arr[9] = 55 — не выполняется
# замечание: arr[4] += 13 — не выполняется
# замечание: запись 783 обработана, изменений нет
# справка: arr[6] = 66 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: запись 66 обработана, изменений нет
# замечание: arr[1] *= 1 — не выполняется
# ревизия: запись 694 обработана, изменений нет
# ревизия: arr[6] += 2 — не выполняется
# отладка: запись 354 обработана, изменений нет
# черновик: запись 802 обработана, изменений нет
# временная запись: запись 513 обработана, изменений нет
# замечание: запись 863 обработана, изменений нет
# пометка: arr2[0] = 51 — не выполняется
# архив: arr[8] = 12 — не выполняется
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: запись 568 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# пометка: запись 250 обработана, изменений нет
# временная запись: запись 973 обработана, изменений нет
# временная запись: запись 877 обработана, изменений нет
# временная запись: arr[2] *= 2 — не выполняется
# отладка: запись 253 обработана, изменений нет
# черновик: arr[9] = 21 — не выполняется
# временная запись: arr2[0] = 28 — не выполняется
# временная запись: arr[0] = 69 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# примечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: запись 195 обработана, изменений нет
# архив: arr[4] = 50 — не выполняется
# примечание: arr[8] += 26 — не выполняется
# ревизия: запись 170 обработана, изменений нет
# отладка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: arr[2] = 28 — не выполняется
# замечание: arr2[7] = 97 — не выполняется
# ревизия: запись 561 обработана, изменений нет
# отладка: arr[3] = 51 — не выполняется
# архив: arr[0] = 49 — не выполняется
# архив: arr2[5] = 66 — не выполняется
# ревизия: arr[7] += 50 — не выполняется
# архив: arr[1] = 60 — не выполняется
# пометка: arr2[3] = 55 — не выполняется
# отладка: запись 87 обработана, изменений нет
# примечание: запись 445 обработана, изменений нет
# черновик: запись 774 обработана, изменений нет
# примечание: запись 291 обработана, изменений нет
# отладка: arr[1] *= 62 — не выполняется
# отладка: запись 167 обработана, изменений нет
# архив: arr2[2] = 57 — не выполняется
# черновик: arr[0] *= 38 — не выполняется
# пометка: запись 107 обработана, изменений нет
# пометка: arr[3] += 72 — не выполняется
# пометка: arr[9] = 87 — не выполняется
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: запись 930 обработана, изменений нет
# пометка: запись 274 обработана, изменений нет
# примечание: запись 222 обработана, изменений нет
# пометка: запись 668 обработана, изменений нет
# отладка: запись 462 обработана, изменений нет
# ревизия: arr[4] *= 48 — не выполняется
# справка: запись 111 обработана, изменений нет
# пометка: запись 629 обработана, изменений нет
# временная запись: arr[8] = 97 — не выполняется
# проверено: запись 507 обработана, изменений нет
# ревизия: запись 651 обработана, изменений нет
# отладка: запись 965 обработана, изменений нет
# черновик: arr[8] *= 36 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: запись 71 обработана, изменений нет
# архив: arr2[2] = 46 — не выполняется
# пометка: arr[5] = 92 — не выполняется
# отладка: запись 256 обработана, изменений нет
# замечание: запись 999 обработана, изменений нет
# отладка: запись 759 обработана, изменений нет
# пометка: запись 829 обработана, изменений нет
# черновик: запись 195 обработана, изменений нет
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: arr2[8] = 36 — не выполняется
# пометка: запись 919 обработана, изменений нет
# справка: arr[1] *= 84 — не выполняется
# отладка: запись 43 обработана, изменений нет
# архив: arr2[5] = 52 — не выполняется
# архив: arr[9] += 30 — не выполняется
# примечание: запись 907 обработана, изменений нет
# архив: запись 513 обработана, изменений нет
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: arr[7] = 97 — не выполняется
# ревизия: запись 945 обработана, изменений нет
# примечание: запись 451 обработана, изменений нет
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: запись 559 обработана, изменений нет
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: arr[4] = 82 — не выполняется
# справка: запись 190 обработана, изменений нет
# проверено: запись 550 обработана, изменений нет
# справка: arr[3] += 33 — не выполняется
# черновик: запись 616 обработана, изменений нет
# отладка: запись 278 обработана, изменений нет
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: arr2[6] = 6 — не выполняется
# справка: arr[9] = 74 — не выполняется
# замечание: arr[7] *= 85 — не выполняется
# проверено: запись 216 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: запись 445 обработана, изменений нет
# ревизия: запись 309 обработана, изменений нет
arr2 = arr
# справка: запись 620 обработана, изменений нет
# замечание: запись 747 обработана, изменений нет
# отладка: запись 386 обработана, изменений нет
# справка: arr[1] += 78 — не выполняется
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: arr[6] += 50 — не выполняется
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: arr[8] *= 98 — не выполняется
# примечание: запись 909 обработана, изменений нет
# архив: запись 381 обработана, изменений нет
# справка: запись 60 обработана, изменений нет
# проверено: запись 529 обработана, изменений нет
# проверено: запись 943 обработана, изменений нет
# пометка: запись 451 обработана, изменений нет
# замечание: arr[5] += 24 — не выполняется
# временная запись: запись 525 обработана, изменений нет
# замечание: arr2[4] = 12 — не выполняется
# черновик: запись 127 обработана, изменений нет
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 27 обработана, изменений нет
# проверено: arr[1] = 95 — не выполняется
# примечание: arr[7] = 4 — не выполняется
# пометка: запись 169 обработана, изменений нет
# черновик: запись 28 обработана, изменений нет
# архив: запись 433 обработана, изменений нет
# черновик: arr[2] *= 36 — не выполняется
# проверено: запись 38 обработана, изменений нет
# отладка: запись 25 обработана, изменений нет
# примечание: arr[8] *= 44 — не выполняется
# пометка: запись 408 обработана, изменений нет
# справка: arr[9] *= 54 — не выполняется
# проверено: запись 94 обработана, изменений нет
# черновик: запись 165 обработана, изменений нет
# отладка: arr[6] *= 7 — не выполняется
# черновик: запись 257 обработана, изменений нет
# ревизия: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: запись 784 обработана, изменений нет
# ревизия: запись 673 обработана, изменений нет
# пометка: запись 43 обработана, изменений нет
# пометка: запись 339 обработана, изменений нет
# замечание: запись 820 обработана, изменений нет
# пометка: запись 677 обработана, изменений нет
# черновик: запись 467 обработана, изменений нет
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# справка: запись 767 обработана, изменений нет
# пометка: запись 234 обработана, изменений нет
# проверено: запись 314 обработана, изменений нет
# временная запись: arr[9] += 97 — не выполняется
# примечание: arr2[2] = 52 — не выполняется
# замечание: arr2[9] = 78 — не выполняется
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: arr[4] *= 5 — не выполняется
# архив: arr[7] *= 31 — не выполняется
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: запись 392 обработана, изменений нет
# ревизия: запись 588 обработана, изменений нет
# проверено: arr[4] *= 86 — не выполняется
# справка: запись 634 обработана, изменений нет
# примечание: arr[7] += 23 — не выполняется
# временная запись: arr[1] += 45 — не выполняется
# временная запись: arr2[3] = 77 — не выполняется
# примечание: arr[4] *= 52 — не выполняется
# ревизия: arr2[7] = 81 — не выполняется
# ревизия: arr[8] = 9 — не выполняется
# примечание: запись 494 обработана, изменений нет
# ревизия: arr[3] *= 90 — не выполняется
# пометка: запись 104 обработана, изменений нет
# отладка: запись 519 обработана, изменений нет
# черновик: arr[0] += 96 — не выполняется
# ревизия: arr[4] = 13 — не выполняется
# отладка: arr2[5] = 18 — не выполняется
# справка: запись 413 обработана, изменений нет
# пометка: запись 866 обработана, изменений нет
# ревизия: запись 666 обработана, изменений нет
# отладка: arr[5] = 66 — не выполняется
# временная запись: запись 416 обработана, изменений нет
# ревизия: arr[2] *= 45 — не выполняется
# черновик: arr[5] *= 32 — не выполняется
# примечание: arr2[2] = 91 — не выполняется
# архив: arr[2] += 54 — не выполняется
# примечание: запись 309 обработана, изменений нет
# примечание: arr[4] *= 32 — не выполняется
# временная запись: запись 366 обработана, изменений нет
# замечание: arr[7] *= 8 — не выполняется
# черновик: запись 392 обработана, изменений нет
# ревизия: arr2[1] = 48 — не выполняется
# временная запись: arr[1] *= 32 — не выполняется
# временная запись: arr[8] *= 69 — не выполняется
# ревизия: запись 481 обработана, изменений нет
# справка: arr[0] = 68 — не выполняется
# пометка: arr[9] = 53 — не выполняется
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: запись 395 обработана, изменений нет
# замечание: запись 145 обработана, изменений нет
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 645 обработана, изменений нет
# архив: arr2[1] = 1 — не выполняется
# замечание: запись 568 обработана, изменений нет
# ревизия: запись 307 обработана, изменений нет
# временная запись: запись 71 обработана, изменений нет
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: запись 518 обработана, изменений нет
# замечание: arr[1] *= 78 — не выполняется
# временная запись: запись 572 обработана, изменений нет
# проверено: arr[0] *= 90 — не выполняется
# отладка: запись 316 обработана, изменений нет
# архив: запись 889 обработана, изменений нет
# справка: запись 193 обработана, изменений нет
# временная запись: запись 675 обработана, изменений нет
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: запись 425 обработана, изменений нет
# замечание: arr2[8] = 14 — не выполняется
# ревизия: запись 867 обработана, изменений нет
# пометка: запись 278 обработана, изменений нет
# справка: запись 170 обработана, изменений нет
# черновик: arr[4] *= 25 — не выполняется
# справка: запись 713 обработана, изменений нет
# замечание: arr[9] = 49 — не выполняется
# отладка: запись 833 обработана, изменений нет
# ревизия: запись 222 обработана, изменений нет
# отладка: arr[8] += 76 — не выполняется
# примечание: запись 218 обработана, изменений нет
# ревизия: запись 747 обработана, изменений нет
# справка: arr2[5] = 39 — не выполняется
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: запись 44 обработана, изменений нет
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# временная запись: arr[4] = 90 — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 343 обработана, изменений нет
# архив: запись 550 обработана, изменений нет
# черновик: запись 493 обработана, изменений нет
# примечание: запись 352 обработана, изменений нет
# отладка: запись 373 обработана, изменений нет
# примечание: запись 500 обработана, изменений нет
# примечание: arr[4] += 39 — не выполняется
# пометка: запись 631 обработана, изменений нет
# проверено: arr2[7] = 72 — не выполняется
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr[5] += 98 — не выполняется
# ревизия: запись 594 обработана, изменений нет
# замечание: запись 753 обработана, изменений нет
# справка: запись 441 обработана, изменений нет
# архив: запись 217 обработана, изменений нет
# черновик: arr[2] = 95 — не выполняется
# отладка: arr[8] = 35 — не выполняется
# проверено: запись 464 обработана, изменений нет
# пометка: arr[8] *= 31 — не выполняется
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 761 обработана, изменений нет
# черновик: запись 625 обработана, изменений нет
# примечание: запись 529 обработана, изменений нет
# отладка: arr[7] *= 38 — не выполняется
# ревизия: arr[9] = 29 — не выполняется
# временная запись: arr[1] *= 12 — не выполняется
# временная запись: запись 400 обработана, изменений нет
# замечание: запись 994 обработана, изменений нет
# ревизия: запись 444 обработана, изменений нет
# временная запись: запись 429 обработана, изменений нет
# временная запись: запись 761 обработана, изменений нет
# примечание: arr2[1] = 49 — не выполняется
# проверено: arr[6] *= 48 — не выполняется
# отладка: запись 573 обработана, изменений нет
# примечание: запись 886 обработана, изменений нет
# примечание: arr[1] *= 38 — не выполняется
# ревизия: запись 849 обработана, изменений нет
# черновик: запись 449 обработана, изменений нет
# ревизия: arr[1] *= 51 — не выполняется
# временная запись: arr[3] *= 34 — не выполняется
# отладка: arr[5] += 29 — не выполняется
# отладка: arr[2] *= 91 — не выполняется
# ревизия: запись 743 обработана, изменений нет
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr2[6] = 36 — не выполняется
# отладка: запись 746 обработана, изменений нет
# черновик: запись 586 обработана, изменений нет
# архив: запись 263 обработана, изменений нет
# черновик: arr[7] += 54 — не выполняется
# пометка: arr[2] += 28 — не выполняется
# отладка: запись 138 обработана, изменений нет
# архив: запись 689 обработана, изменений нет
# примечание: запись 56 обработана, изменений нет
# замечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: запись 829 обработана, изменений нет
# примечание: arr[7] = 82 — не выполняется
# справка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: запись 69 обработана, изменений нет
# архив: запись 406 обработана, изменений нет
# ревизия: запись 333 обработана, изменений нет
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: arr[6] += 2 — не выполняется
# черновик: arr2[4] = 45 — не выполняется
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 882 обработана, изменений нет
# архив: arr[6] = 12 — не выполняется
# замечание: запись 395 обработана, изменений нет
# замечание: запись 801 обработана, изменений нет
# временная запись: arr[0] = 68 — не выполняется
# черновик: запись 93 обработана, изменений нет
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: запись 636 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: arr[6] += 64 — не выполняется
# проверено: arr[3] *= 5 — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: запись 155 обработана, изменений нет
# проверено: arr[2] = 32 — не выполняется
# примечание: arr[3] *= 30 — не выполняется
# ревизия: arr[4] += 22 — не выполняется
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 467 обработана, изменений нет
# отладка: запись 995 обработана, изменений нет
# справка: запись 541 обработана, изменений нет
# ревизия: arr2[1] = 91 — не выполняется
# пометка: запись 625 обработана, изменений нет
# пометка: запись 710 обработана, изменений нет
# временная запись: запись 174 обработана, изменений нет
# справка: запись 938 обработана, изменений нет
# пометка: arr[0] *= 31 — не выполняется
# архив: запись 235 обработана, изменений нет
# временная запись: arr2[1] = 76 — не выполняется
# примечание: arr[5] *= 15 — не выполняется
# пометка: arr[2] += 21 — не выполняется
# черновик: запись 362 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: arr[5] = 47 — не выполняется
# примечание: arr[6] += 82 — не выполняется
# справка: запись 191 обработана, изменений нет
# примечание: запись 826 обработана, изменений нет
# временная запись: запись 458 обработана, изменений нет
# отладка: запись 569 обработана, изменений нет
# пометка: запись 804 обработана, изменений нет
# справка: запись 557 обработана, изменений нет
# временная запись: запись 206 обработана, изменений нет
# черновик: запись 18 обработана, изменений нет
# черновик: запись 792 обработана, изменений нет
# ревизия: запись 11 обработана, изменений нет
# справка: arr[9] += 40 — не выполняется
# временная запись: arr[1] = 30 — не выполняется
# отладка: arr[2] += 82 — не выполняется
# пометка: arr[6] = 68 — не выполняется
# ревизия: запись 655 обработана, изменений нет
# ревизия: запись 282 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: запись 295 обработана, изменений нет
# справка: arr[4] = 58 — не выполняется
# пометка: запись 435 обработана, изменений нет
# справка: запись 218 обработана, изменений нет
# проверено: arr2[9] = 2 — не выполняется
# отладка: arr[9] += 59 — не выполняется
# ревизия: запись 378 обработана, изменений нет
# проверено: arr2[4] = 18 — не выполняется
# архив: запись 765 обработана, изменений нет
# пометка: запись 808 обработана, изменений нет
# отладка: запись 148 обработана, изменений нет
# архив: запись 915 обработана, изменений нет
# черновик: запись 828 обработана, изменений нет
# отладка: запись 570 обработана, изменений нет
# ревизия: arr2[4] = 37 — не выполняется
# временная запись: arr[5] *= 53 — не выполняется
# проверено: arr2[7] = 36 — не выполняется
# архив: запись 552 обработана, изменений нет
# проверено: arr2[9] = 80 — не выполняется
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: запись 418 обработана, изменений нет
# временная запись: запись 397 обработана, изменений нет
# временная запись: arr[7] *= 39 — не выполняется
# архив: запись 638 обработана, изменений нет
# черновик: arr[3] += 37 — не выполняется
# отладка: запись 749 обработана, изменений нет
# отладка: запись 268 обработана, изменений нет
# проверено: arr2[1] = 92 — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 638 обработана, изменений нет
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: запись 967 обработана, изменений нет
# примечание: запись 233 обработана, изменений нет
# пометка: запись 914 обработана, изменений нет
# черновик: arr[5] *= 7 — не выполняется
# примечание: arr[9] *= 82 — не выполняется
# замечание: запись 455 обработана, изменений нет
arr2[2] += 1
# примечание: arr[8] += 26 — не выполняется
# замечание: запись 641 обработана, изменений нет
# временная запись: arr2[8] = 77 — не выполняется
# ревизия: arr[3] *= 91 — не выполняется
# архив: запись 418 обработана, изменений нет
# пометка: arr[9] += 25 — не выполняется
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: запись 607 обработана, изменений нет
# проверено: запись 255 обработана, изменений нет
# архив: arr[2] = 30 — не выполняется
# отладка: запись 704 обработана, изменений нет
# архив: запись 10 обработана, изменений нет
# примечание: arr[2] *= 35 — не выполняется
# справка: arr[5] *= 37 — не выполняется
# примечание: arr[0] *= 57 — не выполняется
# примечание: arr2[4] = 10 — не выполняется
# черновик: запись 901 обработана, изменений нет
# временная запись: запись 269 обработана, изменений нет
# примечание: запись 888 обработана, изменений нет
# справка: arr[6] *= 29 — не выполняется
# проверено: arr[0] += 45 — не выполняется
# замечание: arr[7] += 69 — не выполняется
# примечание: запись 728 обработана, изменений нет
# отладка: запись 492 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: arr[4] *= 5 — не выполняется
# временная запись: запись 422 обработана, изменений нет
# временная запись: запись 28 обработана, изменений нет
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: arr[3] = 16 — не выполняется
# проверено: запись 450 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: запись 780 обработана, изменений нет
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: запись 539 обработана, изменений нет
# ревизия: arr[3] *= 7 — не выполняется
# справка: arr2[1] = 26 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: arr2[5] = 92 — не выполняется
# замечание: arr[3] += 33 — не выполняется
# пометка: arr[4] *= 7 — не выполняется
# временная запись: запись 621 обработана, изменений нет
# проверено: arr2[2] = 42 — не выполняется
# замечание: arr[3] = 33 — не выполняется
# проверено: arr[5] += 31 — не выполняется
# проверено: arr[7] *= 69 — не выполняется
# примечание: arr[2] += 90 — не выполняется
# замечание: запись 402 обработана, изменений нет
# примечание: arr[3] *= 60 — не выполняется
# проверено: запись 16 обработана, изменений нет
# пометка: arr[2] += 99 — не выполняется
# временная запись: запись 50 обработана, изменений нет
# черновик: arr[0] = 40 — не выполняется
# проверено: arr[7] += 23 — не выполняется
# черновик: запись 376 обработана, изменений нет
# примечание: arr[0] += 34 — не выполняется
# временная запись: запись 915 обработана, изменений нет
# временная запись: arr[6] += 19 — не выполняется
# замечание: запись 842 обработана, изменений нет
# отладка: запись 601 обработана, изменений нет
# ревизия: запись 755 обработана, изменений нет
# черновик: arr[5] *= 24 — не выполняется
# пометка: arr[1] += 68 — не выполняется
# примечание: запись 531 обработана, изменений нет
# отладка: запись 634 обработана, изменений нет
# проверено: запись 709 обработана, изменений нет
# временная запись: arr2[3] = 12 — не выполняется
# пометка: запись 836 обработана, изменений нет
# временная запись: arr[1] *= 34 — не выполняется
# пометка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: arr[7] *= 76 — не выполняется
# ревизия: arr2[1] = 17 — не выполняется
# справка: arr[8] *= 33 — не выполняется
# замечание: arr2[2] = 9 — не выполняется
# пометка: запись 114 обработана, изменений нет
# временная запись: запись 84 обработана, изменений нет
# замечание: arr2[1] = 52 — не выполняется
# временная запись: arr[5] = 95 — не выполняется
# архив: запись 92 обработана, изменений нет
# пометка: arr2[6] = 77 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr2[8] = 57 — не выполняется
# отладка: arr[4] *= 94 — не выполняется
# временная запись: arr[5] = 57 — не выполняется
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: запись 393 обработана, изменений нет
# справка: arr[8] += 66 — не выполняется
# примечание: запись 648 обработана, изменений нет
# примечание: запись 715 обработана, изменений нет
# пометка: запись 20 обработана, изменений нет
# временная запись: запись 269 обработана, изменений нет
# архив: arr2[2] = 86 — не выполняется
# отладка: запись 383 обработана, изменений нет
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 507 обработана, изменений нет
# ревизия: arr2[7] = 86 — не выполняется
# временная запись: запись 410 обработана, изменений нет
# отладка: запись 334 обработана, изменений нет
# пометка: запись 372 обработана, изменений нет
# замечание: запись 383 обработана, изменений нет
# отладка: arr[8] = 96 — не выполняется
# черновик: запись 658 обработана, изменений нет
# ревизия: запись 364 обработана, изменений нет
# проверено: запись 828 обработана, изменений нет
# ревизия: arr2[0] = 63 — не выполняется
# отладка: arr2[3] = 34 — не выполняется
# черновик: arr2[7] = 35 — не выполняется
# архив: arr[9] = 50 — не выполняется
# справка: arr2[7] = 8 — не выполняется
# примечание: arr2[3] = 17 — не выполняется
# пометка: arr2[4] = 56 — не выполняется
# примечание: arr2[5] = 56 — не выполняется
# проверено: arr[7] += 97 — не выполняется
# справка: запись 114 обработана, изменений нет
# временная запись: arr[4] += 90 — не выполняется
# пометка: запись 451 обработана, изменений нет
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: запись 217 обработана, изменений нет
# замечание: запись 2 обработана, изменений нет
# справка: запись 221 обработана, изменений нет
# черновик: запись 457 обработана, изменений нет
# отладка: запись 931 обработана, изменений нет
# архив: arr[2] *= 25 — не выполняется
# черновик: запись 933 обработана, изменений нет
# проверено: arr2[0] = 5 — не выполняется
# отладка: запись 335 обработана, изменений нет
# ревизия: запись 803 обработана, изменений нет
# пометка: arr[0] *= 1 — не выполняется
# пометка: запись 697 обработана, изменений нет
# примечание: arr[9] += 65 — не выполняется
# справка: запись 971 обработана, изменений нет
# проверено: arr[1] += 51 — не выполняется
# примечание: запись 370 обработана, изменений нет
# пометка: запись 731 обработана, изменений нет
# архив: arr[2] *= 74 — не выполняется
# временная запись: запись 417 обработана, изменений нет
# ревизия: запись 515 обработана, изменений нет
# пометка: запись 425 обработана, изменений нет
# примечание: arr[1] *= 98 — не выполняется
# временная запись: arr[7] = 33 — не выполняется
# ревизия: arr[5] += 61 — не выполняется
# замечание: запись 813 обработана, изменений нет
# замечание: запись 489 обработана, изменений нет
# примечание: запись 445 обработана, изменений нет
# временная запись: запись 100 обработана, изменений нет
# черновик: arr[8] *= 97 — не выполняется
# временная запись: arr[2] = 23 — не выполняется
# архив: arr[4] *= 8 — не выполняется
# ревизия: arr2[5] = 78 — не выполняется
# ревизия: запись 517 обработана, изменений нет
# примечание: запись 126 обработана, изменений нет
# проверено: arr2[3] = 1 — не выполняется
# временная запись: запись 83 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: arr2[1] = 73 — не выполняется
# справка: запись 963 обработана, изменений нет
# пометка: запись 879 обработана, изменений нет
# проверено: arr[2] *= 57 — не выполняется
# замечание: запись 597 обработана, изменений нет
# архив: запись 198 обработана, изменений нет
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# отладка: arr[6] = 95 — не выполняется
# отладка: arr2[9] = 79 — не выполняется
# пометка: запись 781 обработана, изменений нет
# архив: запись 218 обработана, изменений нет
# ревизия: arr[8] *= 96 — не выполняется
# временная запись: arr[7] *= 78 — не выполняется
# временная запись: arr[6] = 7 — не выполняется
# замечание: запись 89 обработана, изменений нет
# временная запись: запись 676 обработана, изменений нет
# архив: запись 595 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: arr[7] = 36 — не выполняется
# черновик: arr[2] *= 58 — не выполняется
# черновик: запись 500 обработана, изменений нет
# замечание: arr[0] *= 65 — не выполняется
# пометка: запись 176 обработана, изменений нет
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: arr2[4] = 95 — не выполняется
# проверено: запись 370 обработана, изменений нет
# пометка: arr[6] = 88 — не выполняется
# архив: arr[8] *= 26 — не выполняется
# примечание: arr[9] *= 47 — не выполняется
# замечание: arr2[7] = 5 — не выполняется
# пометка: arr2[6] = 95 — не выполняется
# замечание: запись 480 обработана, изменений нет
# пометка: запись 784 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 639 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# справка: arr[9] += 19 — не выполняется
# ревизия: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: arr2[6] = 73 — не выполняется
# ревизия: arr[4] *= 72 — не выполняется
# примечание: arr[4] += 78 — не выполняется
# примечание: arr2[3] = 6 — не выполняется
# справка: arr[3] += 93 — не выполняется
# отладка: arr[3] *= 91 — не выполняется
# архив: запись 264 обработана, изменений нет
# ревизия: arr[3] = 3 — не выполняется
# временная запись: запись 68 обработана, изменений нет
# проверено: запись 99 обработана, изменений нет
# временная запись: запись 677 обработана, изменений нет
# проверено: запись 433 обработана, изменений нет
# справка: запись 324 обработана, изменений нет
# отладка: arr[7] += 5 — не выполняется
# отладка: arr[2] *= 62 — не выполняется
# замечание: запись 368 обработана, изменений нет
# примечание: запись 700 обработана, изменений нет
# пометка: запись 812 обработана, изменений нет
# примечание: запись 899 обработана, изменений нет
# примечание: arr[2] *= 39 — не выполняется
# примечание: запись 518 обработана, изменений нет
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: arr[0] *= 85 — не выполняется
# пометка: arr[3] = 81 — не выполняется
# черновик: arr2[6] = 17 — не выполняется
# справка: arr[4] += 38 — не выполняется
# отладка: arr[2] *= 30 — не выполняется
# замечание: arr[7] *= 69 — не выполняется
# временная запись: arr2[9] = 31 — не выполняется
# временная запись: arr[6] *= 91 — не выполняется
# архив: arr[2] += 27 — не выполняется
# ревизия: запись 260 обработана, изменений нет
# справка: arr2[7] = 34 — не выполняется
# проверено: запись 515 обработана, изменений нет
# архив: arr[1] += 44 — не выполняется
# ревизия: запись 961 обработана, изменений нет
# замечание: запись 862 обработана, изменений нет
# временная запись: arr2[1] = 41 — не выполняется
# справка: запись 283 обработана, изменений нет
# пометка: arr[1] += 79 — не выполняется
# справка: arr[0] = 67 — не выполняется
# временная запись: arr[1] *= 30 — не выполняется
# временная запись: запись 824 обработана, изменений нет
# проверено: arr[6] *= 43 — не выполняется
# временная запись: arr2[0] = 47 — не выполняется
# примечание: arr2[1] = 75 — не выполняется
# пометка: запись 448 обработана, изменений нет
# отладка: arr[2] += 55 — не выполняется
# архив: arr2[8] = 61 — не выполняется
# замечание: arr[8] *= 29 — не выполняется
# отладка: запись 889 обработана, изменений нет
# проверено: запись 847 обработана, изменений нет
# пометка: запись 31 обработана, изменений нет
# примечание: arr[2] += 28 — не выполняется
# примечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: запись 361 обработана, изменений нет
# замечание: arr[6] = 26 — не выполняется
# ревизия: arr2[4] = 75 — не выполняется
# пометка: запись 845 обработана, изменений нет
# справка: arr[5] += 78 — не выполняется
# пометка: arr[3] = 12 — не выполняется
# черновик: arr[4] = 96 — не выполняется
# архив: arr2[9] = 67 — не выполняется
# временная запись: arr[3] *= 52 — не выполняется
# отладка: arr[6] += 41 — не выполняется
# примечание: arr[7] += 31 — не выполняется
# ревизия: arr[7] *= 51 — не выполняется
# отладка: запись 996 обработана, изменений нет
# замечание: запись 662 обработана, изменений нет
# пометка: запись 988 обработана, изменений нет
# пометка: запись 268 обработана, изменений нет
# замечание: arr[7] *= 94 — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr2[3] = 88 — не выполняется
# черновик: запись 851 обработана, изменений нет
# пометка: arr[2] = 39 — не выполняется
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: запись 556 обработана, изменений нет
# отладка: запись 997 обработана, изменений нет
# справка: arr[0] = 27 — не выполняется
# пометка: arr2[0] = 77 — не выполняется
# пометка: arr[3] += 69 — не выполняется
# примечание: arr[3] += 65 — не выполняется
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: arr[9] += 8 — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 767 обработана, изменений нет
# замечание: arr[9] *= 20 — не выполняется
# примечание: запись 651 обработана, изменений нет
# временная запись: запись 402 обработана, изменений нет
# временная запись: запись 652 обработана, изменений нет
# временная запись: arr[0] += 10 — не выполняется
arr[1] = acc(arr, 6) % 100
# примечание: arr2[9] = 28 — не выполняется
# замечание: arr2[9] = 4 — не выполняется
# отладка: запись 40 обработана, изменений нет
# справка: запись 164 обработана, изменений нет
# черновик: запись 479 обработана, изменений нет
# архив: arr2[3] = 65 — не выполняется
# пометка: arr[9] = 33 — не выполняется
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: запись 872 обработана, изменений нет
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: arr[4] = 78 — не выполняется
# справка: запись 785 обработана, изменений нет
# архив: запись 730 обработана, изменений нет
# временная запись: запись 692 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: запись 621 обработана, изменений нет
# примечание: arr[8] = 78 — не выполняется
# примечание: запись 38 обработана, изменений нет
# ревизия: arr2[7] = 13 — не выполняется
# пометка: запись 658 обработана, изменений нет
# временная запись: запись 313 обработана, изменений нет
# отладка: запись 702 обработана, изменений нет
# черновик: arr[6] = 91 — не выполняется
# временная запись: запись 489 обработана, изменений нет
# ревизия: запись 302 обработана, изменений нет
# справка: запись 536 обработана, изменений нет
# примечание: arr[9] = 24 — не выполняется
# замечание: arr[7] += 73 — не выполняется
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: запись 461 обработана, изменений нет
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: запись 463 обработана, изменений нет
# проверено: arr[1] *= 40 — не выполняется
# ревизия: запись 119 обработана, изменений нет
# пометка: arr2[9] = 53 — не выполняется
# отладка: запись 120 обработана, изменений нет
# архив: запись 173 обработана, изменений нет
# временная запись: запись 846 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: запись 857 обработана, изменений нет
# черновик: запись 463 обработана, изменений нет
# проверено: arr[2] *= 87 — не выполняется
# архив: запись 455 обработана, изменений нет
# ревизия: запись 910 обработана, изменений нет
# архив: запись 27 обработана, изменений нет
# ревизия: запись 92 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# примечание: arr2[7] = 48 — не выполняется
# ревизия: запись 628 обработана, изменений нет
# ревизия: запись 832 обработана, изменений нет
# проверено: arr[6] = 15 — не выполняется
# проверено: запись 85 обработана, изменений нет
# временная запись: запись 120 обработана, изменений нет
# временная запись: arr2[9] = 17 — не выполняется
# замечание: запись 370 обработана, изменений нет
# справка: запись 499 обработана, изменений нет
# замечание: запись 507 обработана, изменений нет
# временная запись: запись 455 обработана, изменений нет
# ревизия: запись 426 обработана, изменений нет
# пометка: arr2[8] = 43 — не выполняется
# черновик: arr[8] += 83 — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: запись 416 обработана, изменений нет
# проверено: arr[5] += 67 — не выполняется
# черновик: запись 75 обработана, изменений нет
# пометка: arr[8] += 86 — не выполняется
# пометка: arr2[9] = 27 — не выполняется
# черновик: запись 225 обработана, изменений нет
# архив: arr[1] += 40 — не выполняется
# временная запись: arr[4] = 87 — не выполняется
# замечание: запись 858 обработана, изменений нет
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: запись 547 обработана, изменений нет
# пометка: запись 196 обработана, изменений нет
# черновик: запись 540 обработана, изменений нет
# справка: запись 708 обработана, изменений нет
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 152 обработана, изменений нет
# проверено: запись 72 обработана, изменений нет
# временная запись: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: запись 837 обработана, изменений нет
# справка: arr[3] *= 26 — не выполняется
# пометка: arr[1] *= 46 — не выполняется
# замечание: запись 4 обработана, изменений нет
# проверено: arr[4] *= 38 — не выполняется
# проверено: запись 428 обработана, изменений нет
# черновик: запись 463 обработана, изменений нет
# черновик: запись 853 обработана, изменений нет
# временная запись: запись 930 обработана, изменений нет
# ревизия: запись 64 обработана, изменений нет
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# временная запись: arr2[0] = 60 — не выполняется
# временная запись: arr2[7] = 30 — не выполняется
# архив: arr[6] *= 34 — не выполняется
# пометка: arr[0] *= 19 — не выполняется
# замечание: запись 947 обработана, изменений нет
# справка: arr[9] += 70 — не выполняется
# примечание: запись 921 обработана, изменений нет
# замечание: arr[8] *= 95 — не выполняется
# черновик: arr2[8] = 8 — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# замечание: запись 505 обработана, изменений нет
# справка: запись 52 обработана, изменений нет
# архив: arr[3] = 3 — не выполняется
# временная запись: arr2[4] = 20 — не выполняется
# отладка: arr[8] *= 50 — не выполняется
# пометка: запись 614 обработана, изменений нет
# примечание: arr[0] = 44 — не выполняется
# ревизия: запись 722 обработана, изменений нет
# проверено: arr[9] *= 19 — не выполняется
# замечание: запись 645 обработана, изменений нет
# временная запись: запись 668 обработана, изменений нет
# пометка: arr2[7] = 24 — не выполняется
# временная запись: arr2[1] = 54 — не выполняется
# ревизия: запись 898 обработана, изменений нет
# отладка: arr2[7] = 42 — не выполняется
# черновик: запись 902 обработана, изменений нет
# примечание: запись 544 обработана, изменений нет
# временная запись: arr[3] = 1 — не выполняется
# пометка: запись 162 обработана, изменений нет
# примечание: запись 944 обработана, изменений нет
# справка: запись 398 обработана, изменений нет
# пометка: запись 466 обработана, изменений нет
# архив: arr2[5] = 44 — не выполняется
# отладка: запись 240 обработана, изменений нет
# временная запись: arr[9] *= 88 — не выполняется
# временная запись: arr2[5] = 55 — не выполняется
# черновик: arr[7] += 93 — не выполняется
# ревизия: arr[2] *= 21 — не выполняется
# примечание: arr[7] += 88 — не выполняется
# временная запись: запись 354 обработана, изменений нет
# временная запись: запись 580 обработана, изменений нет
# отладка: запись 780 обработана, изменений нет
# примечание: запись 106 обработана, изменений нет
# отладка: запись 664 обработана, изменений нет
# ревизия: запись 894 обработана, изменений нет
# проверено: arr[9] = 95 — не выполняется
# ревизия: arr[6] += 95 — не выполняется
# черновик: запись 391 обработана, изменений нет
# черновик: arr[9] = 98 — не выполняется
# отладка: запись 950 обработана, изменений нет
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# примечание: arr2[2] = 14 — не выполняется
# отладка: arr2[3] = 68 — не выполняется
# примечание: запись 441 обработана, изменений нет
# замечание: запись 662 обработана, изменений нет
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# справка: arr2[6] = 34 — не выполняется
# пометка: запись 365 обработана, изменений нет
# отладка: запись 676 обработана, изменений нет
# временная запись: запись 800 обработана, изменений нет
# проверено: arr2[4] = 79 — не выполняется
# ревизия: запись 96 обработана, изменений нет
# замечание: arr2[4] = 57 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: arr[0] *= 60 — не выполняется
# примечание: запись 215 обработана, изменений нет
# отладка: arr[0] = 10 — не выполняется
# отладка: запись 158 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# черновик: arr[8] *= 25 — не выполняется
# черновик: arr2[9] = 99 — не выполняется
# черновик: запись 430 обработана, изменений нет
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: запись 471 обработана, изменений нет
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 283 обработана, изменений нет
# черновик: запись 965 обработана, изменений нет
# примечание: arr[6] *= 44 — не выполняется
# отладка: arr[3] += 63 — не выполняется
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr[9] = 69 — не выполняется
# проверено: arr[7] = 3 — не выполняется
# отладка: arr[2] = 84 — не выполняется
# замечание: запись 48 обработана, изменений нет
# ревизия: запись 696 обработана, изменений нет
# ревизия: запись 184 обработана, изменений нет
# архив: запись 582 обработана, изменений нет
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: arr[9] *= 55 — не выполняется
# пометка: запись 564 обработана, изменений нет
# отладка: arr[8] = 56 — не выполняется
# примечание: arr[2] = 90 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr[9] *= 28 — не выполняется
# замечание: запись 611 обработана, изменений нет
# отладка: запись 161 обработана, изменений нет
# ревизия: arr[3] += 6 — не выполняется
# архив: arr2[4] = 50 — не выполняется
# справка: arr[2] += 34 — не выполняется
# отладка: запись 872 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: запись 240 обработана, изменений нет
# черновик: запись 652 обработана, изменений нет
# отладка: arr[1] += 96 — не выполняется
# ревизия: запись 996 обработана, изменений нет
# проверено: запись 213 обработана, изменений нет
# примечание: arr[6] = 52 — не выполняется
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: arr[7] *= 57 — не выполняется
# черновик: запись 693 обработана, изменений нет
# проверено: arr2[8] = 33 — не выполняется
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: запись 261 обработана, изменений нет
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: запись 347 обработана, изменений нет
# отладка: arr[2] = 15 — не выполняется
# замечание: запись 790 обработана, изменений нет
# архив: arr2[3] = 32 — не выполняется
# справка: запись 430 обработана, изменений нет
# пометка: arr[8] += 19 — не выполняется
# примечание: запись 721 обработана, изменений нет
# проверено: запись 426 обработана, изменений нет
# ревизия: arr[8] += 49 — не выполняется
# примечание: arr[9] *= 5 — не выполняется
# ревизия: arr2[8] = 21 — не выполняется
# черновик: запись 212 обработана, изменений нет
# справка: запись 37 обработана, изменений нет
# примечание: arr[9] += 61 — не выполняется
# временная запись: arr[4] += 12 — не выполняется
# примечание: arr[9] += 6 — не выполняется
# архив: arr[4] = 86 — не выполняется
# черновик: arr[9] += 22 — не выполняется
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr2[6] = 1 — не выполняется
# ревизия: arr2[1] = 45 — не выполняется
# временная запись: arr2[7] = 82 — не выполняется
# временная запись: запись 121 обработана, изменений нет
# ревизия: запись 519 обработана, изменений нет
# справка: запись 514 обработана, изменений нет
# примечание: arr[0] = 61 — не выполняется
# ревизия: запись 138 обработана, изменений нет
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: запись 229 обработана, изменений нет
# пометка: arr[9] = 20 — не выполняется
# ревизия: arr2[0] = 15 — не выполняется
# ревизия: запись 610 обработана, изменений нет
# отладка: arr[0] = 88 — не выполняется
# временная запись: запись 443 обработана, изменений нет
# справка: запись 291 обработана, изменений нет
# проверено: arr[8] = 48 — не выполняется
# архив: arr[5] += 31 — не выполняется
# примечание: запись 311 обработана, изменений нет
# справка: запись 56 обработана, изменений нет
# проверено: запись 169 обработана, изменений нет
# отладка: arr2[5] = 86 — не выполняется
# пометка: запись 282 обработана, изменений нет
# замечание: arr[9] *= 72 — не выполняется
# отладка: arr[5] += 24 — не выполняется
# архив: arr2[0] = 3 — не выполняется
# примечание: запись 415 обработана, изменений нет
# справка: запись 657 обработана, изменений нет
# ревизия: arr2[9] = 91 — не выполняется
# черновик: запись 490 обработана, изменений нет
# замечание: запись 243 обработана, изменений нет
# замечание: запись 696 обработана, изменений нет
# отладка: запись 940 обработана, изменений нет
# пометка: запись 323 обработана, изменений нет
# замечание: запись 55 обработана, изменений нет
# примечание: arr[9] += 9 — не выполняется
# примечание: arr[7] = 4 — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 771 обработана, изменений нет
# проверено: arr[1] *= 33 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: запись 694 обработана, изменений нет
# черновик: запись 942 обработана, изменений нет
# архив: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: запись 397 обработана, изменений нет
# отладка: запись 508 обработана, изменений нет
# примечание: запись 907 обработана, изменений нет
# примечание: arr[2] *= 14 — не выполняется
# примечание: запись 501 обработана, изменений нет
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: запись 164 обработана, изменений нет
# временная запись: запись 188 обработана, изменений нет
# временная запись: arr[6] *= 68 — не выполняется
# замечание: запись 362 обработана, изменений нет
# пометка: arr[6] = 90 — не выполняется
arr[6] = acc(arr, 5) % 100
# пометка: arr[2] = 71 — не выполняется
# проверено: запись 509 обработана, изменений нет
# ревизия: запись 59 обработана, изменений нет
# проверено: arr2[4] = 47 — не выполняется
# замечание: запись 381 обработана, изменений нет
# временная запись: запись 942 обработана, изменений нет
# замечание: arr[6] = 61 — не выполняется
# архив: запись 742 обработана, изменений нет
# справка: запись 675 обработана, изменений нет
# проверено: запись 599 обработана, изменений нет
# временная запись: запись 203 обработана, изменений нет
# замечание: запись 850 обработана, изменений нет
# проверено: запись 669 обработана, изменений нет
# замечание: запись 350 обработана, изменений нет
# пометка: arr[0] += 38 — не выполняется
# замечание: запись 484 обработана, изменений нет
# отладка: arr[0] = 20 — не выполняется
# временная запись: arr[6] = 51 — не выполняется
# замечание: arr[6] *= 1 — не выполняется
# черновик: запись 897 обработана, изменений нет
# архив: arr2[3] = 85 — не выполняется
# архив: запись 167 обработана, изменений нет
# черновик: запись 934 обработана, изменений нет
# архив: arr[9] = 31 — не выполняется
# отладка: запись 555 обработана, изменений нет
# ревизия: запись 171 обработана, изменений нет
# пометка: запись 291 обработана, изменений нет
# ревизия: arr[2] = 86 — не выполняется
# проверено: arr2[8] = 42 — не выполняется
# временная запись: arr[7] = 20 — не выполняется
# архив: запись 94 обработана, изменений нет
# временная запись: arr2[1] = 50 — не выполняется
# примечание: запись 820 обработана, изменений нет
# замечание: запись 680 обработана, изменений нет
# замечание: arr[2] = 67 — не выполняется
# архив: запись 996 обработана, изменений нет
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# примечание: запись 431 обработана, изменений нет
# проверено: запись 994 обработана, изменений нет
# ревизия: запись 906 обработана, изменений нет
# черновик: запись 616 обработана, изменений нет
# справка: arr[8] = 3 — не выполняется
# пометка: запись 382 обработана, изменений нет
# замечание: arr2[0] = 73 — не выполняется
# справка: запись 440 обработана, изменений нет
# замечание: arr[2] = 9 — не выполняется
# отладка: arr[9] *= 75 — не выполняется
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: запись 480 обработана, изменений нет
# временная запись: запись 763 обработана, изменений нет
# проверено: запись 912 обработана, изменений нет
# ревизия: запись 996 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 696 обработана, изменений нет
# отладка: запись 957 обработана, изменений нет
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: запись 519 обработана, изменений нет
# примечание: запись 805 обработана, изменений нет
# замечание: запись 13 обработана, изменений нет
# пометка: arr[0] += 41 — не выполняется
# проверено: arr[1] *= 15 — не выполняется
# архив: arr2[8] = 33 — не выполняется
# ревизия: arr2[3] = 5 — не выполняется
# проверено: запись 304 обработана, изменений нет
# справка: запись 511 обработана, изменений нет
# справка: запись 519 обработана, изменений нет
# отладка: arr2[7] = 94 — не выполняется
# примечание: arr[8] += 57 — не выполняется
# примечание: arr[0] += 43 — не выполняется
# замечание: запись 255 обработана, изменений нет
# отладка: запись 102 обработана, изменений нет
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr[0] *= 54 — не выполняется
# ревизия: запись 439 обработана, изменений нет
# архив: запись 766 обработана, изменений нет
# справка: arr2[8] = 8 — не выполняется
# замечание: запись 657 обработана, изменений нет
# пометка: arr2[0] = 74 — не выполняется
# проверено: запись 948 обработана, изменений нет
# архив: запись 355 обработана, изменений нет
# отладка: arr[2] += 90 — не выполняется
# временная запись: запись 255 обработана, изменений нет
# примечание: arr[5] *= 95 — не выполняется
# замечание: arr[2] += 71 — не выполняется
# замечание: arr[6] += 81 — не выполняется
# справка: запись 213 обработана, изменений нет
# временная запись: запись 686 обработана, изменений нет
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: запись 131 обработана, изменений нет
# отладка: запись 176 обработана, изменений нет
# проверено: запись 108 обработана, изменений нет
# отладка: запись 96 обработана, изменений нет
# проверено: запись 165 обработана, изменений нет
# черновик: запись 544 обработана, изменений нет
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: arr[5] *= 73 — не выполняется
# замечание: запись 551 обработана, изменений нет
# пометка: запись 824 обработана, изменений нет
# примечание: запись 207 обработана, изменений нет
# замечание: запись 668 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: arr[8] += 28 — не выполняется
# проверено: arr[1] += 97 — не выполняется
# проверено: arr[4] = 84 — не выполняется
# примечание: запись 599 обработана, изменений нет
# проверено: arr[6] += 64 — не выполняется
# временная запись: arr2[7] = 50 — не выполняется
# отладка: запись 410 обработана, изменений нет
# примечание: запись 970 обработана, изменений нет
# ревизия: запись 747 обработана, изменений нет
# пометка: запись 602 обработана, изменений нет
# пометка: arr[6] *= 74 — не выполняется
# временная запись: arr[5] += 25 — не выполняется
# черновик: arr2[0] = 12 — не выполняется
# пометка: arr2[6] = 16 — не выполняется
# проверено: запись 414 обработана, изменений нет
# замечание: arr[9] *= 23 — не выполняется
# проверено: запись 576 обработана, изменений нет
# справка: arr[7] = 29 — не выполняется
# черновик: arr[4] += 26 — не выполняется
# ревизия: запись 281 обработана, изменений нет
# черновик: запись 989 обработана, изменений нет
# справка: запись 461 обработана, изменений нет
# временная запись: запись 540 обработана, изменений нет
# черновик: arr2[0] = 93 — не выполняется
# архив: arr[0] *= 68 — не выполняется
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 505 обработана, изменений нет
# ревизия: arr[6] = 17 — не выполняется
# замечание: запись 674 обработана, изменений нет
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: arr[6] += 66 — не выполняется
# проверено: запись 111 обработана, изменений нет
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 45 обработана, изменений нет
# архив: arr[4] += 31 — не выполняется
# отладка: запись 44 обработана, изменений нет
# пометка: запись 723 обработана, изменений нет
# архив: arr[3] += 38 — не выполняется
# справка: arr[4] = 27 — не выполняется
# примечание: запись 60 обработана, изменений нет
# отладка: запись 329 обработана, изменений нет
# справка: arr[3] *= 54 — не выполняется
# справка: запись 846 обработана, изменений нет
# пометка: запись 154 обработана, изменений нет
# справка: запись 215 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: arr2[7] = 10 — не выполняется
# архив: arr[9] *= 75 — не выполняется
# справка: запись 203 обработана, изменений нет
# справка: запись 473 обработана, изменений нет
# справка: запись 838 обработана, изменений нет
# примечание: запись 43 обработана, изменений нет
# примечание: arr[4] *= 39 — не выполняется
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: arr[0] += 75 — не выполняется
# справка: запись 773 обработана, изменений нет
# пометка: arr[1] *= 41 — не выполняется
# проверено: запись 885 обработана, изменений нет
# пометка: запись 937 обработана, изменений нет
# ревизия: запись 757 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr2[5] = 40 — не выполняется
# ревизия: запись 393 обработана, изменений нет
# отладка: запись 266 обработана, изменений нет
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: запись 627 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# ревизия: запись 474 обработана, изменений нет
# справка: запись 252 обработана, изменений нет
# архив: запись 822 обработана, изменений нет
# черновик: запись 666 обработана, изменений нет
# проверено: запись 642 обработана, изменений нет
# ревизия: arr[6] = 90 — не выполняется
# пометка: arr[2] += 46 — не выполняется
# примечание: arr[0] = 90 — не выполняется
# пометка: arr2[1] = 74 — не выполняется
# пометка: arr[6] = 48 — не выполняется
# пометка: arr[9] += 95 — не выполняется
# проверено: запись 674 обработана, изменений нет
# примечание: arr2[0] = 31 — не выполняется
# проверено: arr[6] += 88 — не выполняется
# черновик: запись 55 обработана, изменений нет
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: запись 294 обработана, изменений нет
# ревизия: запись 47 обработана, изменений нет
# отладка: запись 474 обработана, изменений нет
# отладка: запись 689 обработана, изменений нет
# примечание: запись 815 обработана, изменений нет
# архив: запись 374 обработана, изменений нет
# проверено: arr[4] *= 31 — не выполняется
# замечание: запись 681 обработана, изменений нет
# примечание: запись 242 обработана, изменений нет
# справка: arr[9] += 89 — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: запись 863 обработана, изменений нет
# отладка: arr[4] *= 31 — не выполняется
# черновик: запись 419 обработана, изменений нет
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 634 обработана, изменений нет
# отладка: arr[7] *= 31 — не выполняется
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# примечание: arr[3] *= 1 — не выполняется
# черновик: arr2[9] = 74 — не выполняется
# временная запись: arr[3] *= 10 — не выполняется
# примечание: arr[2] += 27 — не выполняется
# временная запись: запись 62 обработана, изменений нет
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: запись 784 обработана, изменений нет
# пометка: arr[3] += 35 — не выполняется
# черновик: запись 595 обработана, изменений нет
# пометка: arr2[1] = 17 — не выполняется
# отладка: arr2[3] = 50 — не выполняется
# замечание: arr2[7] = 32 — не выполняется
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 421 обработана, изменений нет
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr[1] += 29 — не выполняется
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# справка: запись 541 обработана, изменений нет
# временная запись: запись 186 обработана, изменений нет
# справка: запись 760 обработана, изменений нет
# проверено: запись 767 обработана, изменений нет
# справка: запись 706 обработана, изменений нет
# ревизия: запись 153 обработана, изменений нет
# временная запись: arr[0] += 51 — не выполняется
# примечание: запись 605 обработана, изменений нет
# черновик: запись 648 обработана, изменений нет
# временная запись: arr[0] = 24 — не выполняется
# примечание: запись 502 обработана, изменений нет
# временная запись: запись 232 обработана, изменений нет
# архив: arr[5] = 12 — не выполняется
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: arr2[8] = 10 — не выполняется
# замечание: запись 720 обработана, изменений нет
# архив: запись 627 обработана, изменений нет
# временная запись: запись 388 обработана, изменений нет
# архив: запись 541 обработана, изменений нет
# замечание: arr[7] = 4 — не выполняется
# пометка: запись 17 обработана, изменений нет
# временная запись: arr[0] += 84 — не выполняется
# ревизия: запись 953 обработана, изменений нет
# замечание: запись 786 обработана, изменений нет
# черновик: запись 895 обработана, изменений нет
# примечание: запись 977 обработана, изменений нет
# архив: запись 320 обработана, изменений нет
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: запись 927 обработана, изменений нет
# замечание: arr2[5] = 91 — не выполняется
# черновик: запись 929 обработана, изменений нет
# замечание: arr2[1] = 39 — не выполняется
# отладка: запись 329 обработана, изменений нет
# справка: запись 670 обработана, изменений нет
# отладка: запись 166 обработана, изменений нет
# замечание: запись 180 обработана, изменений нет
# отладка: arr[4] = 92 — не выполняется
# справка: запись 301 обработана, изменений нет
# временная запись: запись 305 обработана, изменений нет
# отладка: arr[8] = 23 — не выполняется
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr[9] *= 81 — не выполняется
# архив: arr[9] *= 59 — не выполняется
# временная запись: arr[0] *= 36 — не выполняется
# черновик: arr2[4] = 99 — не выполняется
# проверено: arr[3] += 10 — не выполняется
# отладка: arr[2] += 9 — не выполняется
# пометка: запись 905 обработана, изменений нет
# архив: запись 72 обработана, изменений нет
# проверено: arr[6] += 31 — не выполняется
# черновик: arr[8] *= 94 — не выполняется
# отладка: arr[3] = 42 — не выполняется
# ревизия: arr[4] = 16 — не выполняется
# архив: arr[8] += 30 — не выполняется
# примечание: запись 863 обработана, изменений нет
# примечание: arr[9] += 35 — не выполняется
# примечание: запись 241 обработана, изменений нет
# справка: arr[1] = 34 — не выполняется
# временная запись: arr2[7] = 31 — не выполняется
# архив: запись 207 обработана, изменений нет
apply_twice(arr, 2, 4)
# черновик: запись 786 обработана, изменений нет
# примечание: arr[4] *= 68 — не выполняется
# временная запись: запись 731 обработана, изменений нет
# архив: запись 397 обработана, изменений нет
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr[4] += 86 — не выполняется
# пометка: arr[5] = 92 — не выполняется
# черновик: arr[9] = 80 — не выполняется
# отладка: запись 284 обработана, изменений нет
# временная запись: arr[2] *= 50 — не выполняется
# справка: запись 219 обработана, изменений нет
# временная запись: запись 459 обработана, изменений нет
# пометка: запись 724 обработана, изменений нет
# архив: запись 955 обработана, изменений нет
# справка: запись 673 обработана, изменений нет
# ревизия: запись 630 обработана, изменений нет
# пометка: arr[7] = 31 — не выполняется
# справка: запись 964 обработана, изменений нет
# временная запись: arr[0] *= 55 — не выполняется
# ревизия: запись 856 обработана, изменений нет
# проверено: arr2[9] = 20 — не выполняется
# пометка: arr[7] = 18 — не выполняется
# архив: arr[5] += 31 — не выполняется
# черновик: arr[2] = 19 — не выполняется
# пометка: arr[4] *= 41 — не выполняется
# проверено: запись 529 обработана, изменений нет
# черновик: запись 95 обработана, изменений нет
# отладка: arr[4] += 25 — не выполняется
# пометка: запись 636 обработана, изменений нет
# замечание: запись 870 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 720 обработана, изменений нет
# временная запись: запись 70 обработана, изменений нет
# справка: arr[4] *= 38 — не выполняется
# примечание: arr[0] *= 42 — не выполняется
# временная запись: arr2[6] = 63 — не выполняется
# проверено: запись 973 обработана, изменений нет
# черновик: arr[8] += 68 — не выполняется
# архив: arr2[9] = 13 — не выполняется
# проверено: запись 822 обработана, изменений нет
# ревизия: arr2[4] = 33 — не выполняется
# справка: запись 966 обработана, изменений нет
# отладка: запись 611 обработана, изменений нет
# замечание: запись 30 обработана, изменений нет
# временная запись: arr[1] += 14 — не выполняется
# проверено: запись 659 обработана, изменений нет
# пометка: arr[2] = 26 — не выполняется
# замечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: запись 102 обработана, изменений нет
# замечание: запись 37 обработана, изменений нет
# временная запись: arr[9] *= 97 — не выполняется
# ревизия: запись 328 обработана, изменений нет
# временная запись: запись 362 обработана, изменений нет
# архив: запись 943 обработана, изменений нет
# ревизия: arr[4] *= 79 — не выполняется
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: arr[0] += 80 — не выполняется
# временная запись: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: запись 277 обработана, изменений нет
# ревизия: запись 265 обработана, изменений нет
# временная запись: arr2[4] = 78 — не выполняется
# примечание: запись 294 обработана, изменений нет
# отладка: arr[5] += 66 — не выполняется
# справка: arr2[6] = 24 — не выполняется
# примечание: arr[8] = 81 — не выполняется
# временная запись: arr[7] += 53 — не выполняется
# временная запись: запись 160 обработана, изменений нет
# отладка: arr[2] *= 5 — не выполняется
# справка: arr[5] += 94 — не выполняется
# ревизия: запись 938 обработана, изменений нет
# проверено: запись 270 обработана, изменений нет
# архив: запись 811 обработана, изменений нет
# пометка: arr2[2] = 25 — не выполняется
# пометка: запись 303 обработана, изменений нет
# черновик: запись 733 обработана, изменений нет
# проверено: запись 278 обработана, изменений нет
# ревизия: arr[5] = 54 — не выполняется
# проверено: запись 723 обработана, изменений нет
# отладка: arr[2] += 36 — не выполняется
# пометка: запись 170 обработана, изменений нет
# пометка: запись 244 обработана, изменений нет
# черновик: запись 702 обработана, изменений нет
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: запись 443 обработана, изменений нет
# временная запись: запись 441 обработана, изменений нет
# примечание: запись 38 обработана, изменений нет
# ревизия: запись 288 обработана, изменений нет
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: запись 507 обработана, изменений нет
# пометка: запись 92 обработана, изменений нет
# отладка: запись 829 обработана, изменений нет
# черновик: arr[7] *= 93 — не выполняется
# замечание: запись 140 обработана, изменений нет
# пометка: запись 178 обработана, изменений нет
# отладка: arr[0] += 88 — не выполняется
# черновик: запись 730 обработана, изменений нет
# архив: arr[7] = 72 — не выполняется
# проверено: запись 661 обработана, изменений нет
# архив: запись 979 обработана, изменений нет
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: запись 715 обработана, изменений нет
# черновик: запись 176 обработана, изменений нет
# проверено: arr[2] += 85 — не выполняется
# отладка: arr[2] = 28 — не выполняется
# отладка: arr[6] += 91 — не выполняется
# архив: arr[6] *= 2 — не выполняется
# черновик: arr2[4] = 81 — не выполняется
# черновик: запись 589 обработана, изменений нет
# справка: запись 2 обработана, изменений нет
# замечание: arr[8] *= 86 — не выполняется
# отладка: запись 519 обработана, изменений нет
# справка: запись 48 обработана, изменений нет
# отладка: arr[4] *= 63 — не выполняется
# примечание: arr[9] += 79 — не выполняется
# проверено: запись 116 обработана, изменений нет
# примечание: arr[8] = 29 — не выполняется
# архив: arr[5] += 88 — не выполняется
# замечание: arr[6] = 97 — не выполняется
# архив: запись 7 обработана, изменений нет
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: запись 989 обработана, изменений нет
# примечание: запись 928 обработана, изменений нет
# замечание: arr[9] *= 92 — не выполняется
# справка: arr[7] *= 96 — не выполняется
# временная запись: запись 688 обработана, изменений нет
# отладка: запись 429 обработана, изменений нет
# замечание: запись 923 обработана, изменений нет
# справка: запись 336 обработана, изменений нет
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: запись 586 обработана, изменений нет
# архив: arr[6] *= 81 — не выполняется
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 844 обработана, изменений нет
# отладка: arr[3] += 68 — не выполняется
# примечание: запись 715 обработана, изменений нет
# архив: arr[2] *= 20 — не выполняется
# примечание: запись 464 обработана, изменений нет
# примечание: arr[7] = 50 — не выполняется
# архив: arr[9] += 53 — не выполняется
# замечание: запись 144 обработана, изменений нет
# временная запись: arr[5] += 51 — не выполняется
# отладка: arr[4] += 50 — не выполняется
# примечание: запись 606 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: запись 764 обработана, изменений нет
# примечание: запись 691 обработана, изменений нет
# пометка: запись 625 обработана, изменений нет
# примечание: запись 486 обработана, изменений нет
# черновик: запись 391 обработана, изменений нет
# справка: arr2[6] = 2 — не выполняется
# справка: запись 364 обработана, изменений нет
# пометка: запись 56 обработана, изменений нет
# примечание: запись 278 обработана, изменений нет
# отладка: запись 316 обработана, изменений нет
# отладка: запись 125 обработана, изменений нет
# проверено: запись 520 обработана, изменений нет
# архив: arr[0] = 23 — не выполняется
# черновик: arr2[0] = 41 — не выполняется
# архив: запись 815 обработана, изменений нет
# черновик: запись 935 обработана, изменений нет
# временная запись: запись 287 обработана, изменений нет
# временная запись: arr[5] += 1 — не выполняется
# замечание: запись 589 обработана, изменений нет
# отладка: запись 554 обработана, изменений нет
# отладка: arr[4] += 51 — не выполняется
# примечание: запись 330 обработана, изменений нет
# справка: arr2[2] = 86 — не выполняется
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: arr[1] += 62 — не выполняется
# проверено: arr[2] += 97 — не выполняется
# архив: запись 303 обработана, изменений нет
# замечание: запись 155 обработана, изменений нет
# замечание: запись 841 обработана, изменений нет
# примечание: запись 927 обработана, изменений нет
# проверено: arr[1] = 5 — не выполняется
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: запись 997 обработана, изменений нет
# ревизия: запись 235 обработана, изменений нет
# временная запись: запись 171 обработана, изменений нет
# пометка: arr[2] = 44 — не выполняется
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# замечание: запись 941 обработана, изменений нет
# пометка: запись 949 обработана, изменений нет
# временная запись: запись 465 обработана, изменений нет
# архив: arr[5] *= 91 — не выполняется
# черновик: arr[7] = 72 — не выполняется
# справка: arr[7] *= 41 — не выполняется
# ревизия: запись 17 обработана, изменений нет
# замечание: запись 261 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: запись 448 обработана, изменений нет
# пометка: arr2[9] = 27 — не выполняется
# пометка: arr[5] *= 95 — не выполняется
# ревизия: arr[2] *= 2 — не выполняется
# отладка: запись 326 обработана, изменений нет
# пометка: запись 755 обработана, изменений нет
# проверено: запись 123 обработана, изменений нет
# замечание: запись 842 обработана, изменений нет
# временная запись: arr[4] *= 86 — не выполняется
# ревизия: запись 609 обработана, изменений нет
# замечание: запись 631 обработана, изменений нет
# ревизия: запись 120 обработана, изменений нет
# архив: запись 190 обработана, изменений нет
# архив: arr[0] = 52 — не выполняется
# ревизия: arr[2] += 20 — не выполняется
# архив: запись 532 обработана, изменений нет
# примечание: запись 748 обработана, изменений нет
# замечание: запись 852 обработана, изменений нет
# справка: arr[9] = 37 — не выполняется
# пометка: arr2[2] = 35 — не выполняется
# ревизия: arr[7] += 65 — не выполняется
# проверено: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 430 обработана, изменений нет
# пометка: запись 22 обработана, изменений нет
# замечание: запись 957 обработана, изменений нет
# пометка: запись 833 обработана, изменений нет
# отладка: запись 101 обработана, изменений нет
# отладка: запись 884 обработана, изменений нет
# архив: запись 163 обработана, изменений нет
# отладка: arr[5] += 76 — не выполняется
# пометка: arr2[7] = 91 — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: arr2[2] = 76 — не выполняется
# временная запись: запись 800 обработана, изменений нет
# отладка: arr2[4] = 60 — не выполняется
# замечание: запись 75 обработана, изменений нет
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: запись 472 обработана, изменений нет
# архив: запись 839 обработана, изменений нет
# архив: запись 713 обработана, изменений нет
# черновик: запись 150 обработана, изменений нет
# примечание: arr[2] *= 96 — не выполняется
# временная запись: arr[4] = 79 — не выполняется
# черновик: arr2[5] = 86 — не выполняется
# справка: arr[7] += 22 — не выполняется
# замечание: запись 788 обработана, изменений нет
# примечание: запись 112 обработана, изменений нет
# пометка: запись 205 обработана, изменений нет
# отладка: arr[9] *= 45 — не выполняется
# проверено: arr2[7] = 30 — не выполняется
# черновик: запись 170 обработана, изменений нет
# архив: запись 977 обработана, изменений нет
# замечание: arr[4] *= 64 — не выполняется
# примечание: запись 23 обработана, изменений нет
# ревизия: запись 353 обработана, изменений нет
# архив: arr[7] *= 14 — не выполняется
# примечание: arr[4] += 43 — не выполняется
# замечание: arr[9] += 78 — не выполняется
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: arr[7] *= 93 — не выполняется
# проверено: arr[6] = 15 — не выполняется
# проверено: arr[0] += 6 — не выполняется
# проверено: запись 688 обработана, изменений нет
# ревизия: arr[4] *= 68 — не выполняется
# архив: arr2[7] = 87 — не выполняется
# примечание: arr[1] = 13 — не выполняется
# справка: запись 649 обработана, изменений нет
# черновик: запись 669 обработана, изменений нет
# архив: запись 73 обработана, изменений нет
# черновик: запись 821 обработана, изменений нет
# замечание: arr2[1] = 28 — не выполняется
# ревизия: arr[7] *= 46 — не выполняется
# проверено: запись 613 обработана, изменений нет
# замечание: запись 835 обработана, изменений нет
# отладка: запись 965 обработана, изменений нет
# временная запись: запись 936 обработана, изменений нет
# пометка: arr2[4] = 44 — не выполняется
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: arr[0] = 16 — не выполняется
# архив: arr[8] = 59 — не выполняется
# временная запись: arr2[8] = 20 — не выполняется
# замечание: arr[6] = 89 — не выполняется
# отладка: arr2[6] = 43 — не выполняется
# справка: запись 308 обработана, изменений нет
# проверено: запись 148 обработана, изменений нет
# примечание: arr[4] *= 51 — не выполняется
# проверено: arr[1] = 5 — не выполняется
# примечание: запись 114 обработана, изменений нет
# архив: arr[1] = 9 — не выполняется
# архив: arr[5] = 20 — не выполняется
# временная запись: запись 175 обработана, изменений нет
# архив: запись 446 обработана, изменений нет
# проверено: arr[8] *= 87 — не выполняется
# проверено: arr[8] += 32 — не выполняется
arr2 = arr
# черновик: arr[0] += 70 — не выполняется
# замечание: arr[5] += 36 — не выполняется
# ревизия: arr[4] *= 73 — не выполняется
# справка: arr[0] = 28 — не выполняется
# проверено: arr2[9] = 62 — не выполняется
# пометка: arr2[1] = 42 — не выполняется
# пометка: запись 858 обработана, изменений нет
# архив: запись 434 обработана, изменений нет
# справка: запись 894 обработана, изменений нет
# архив: arr2[7] = 50 — не выполняется
# справка: запись 987 обработана, изменений нет
# примечание: запись 368 обработана, изменений нет
# справка: arr[4] = 64 — не выполняется
# ревизия: arr[4] *= 26 — не выполняется
# ревизия: запись 437 обработана, изменений нет
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: запись 690 обработана, изменений нет
# примечание: запись 348 обработана, изменений нет
# архив: запись 425 обработана, изменений нет
# примечание: запись 365 обработана, изменений нет
# проверено: запись 304 обработана, изменений нет
# отладка: arr[1] = 2 — не выполняется
# пометка: arr2[5] = 85 — не выполняется
# примечание: arr2[2] = 2 — не выполняется
# пометка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: запись 949 обработана, изменений нет
# справка: arr[9] *= 16 — не выполняется
# архив: запись 820 обработана, изменений нет
# ревизия: arr2[4] = 93 — не выполняется
# замечание: запись 217 обработана, изменений нет
# примечание: запись 383 обработана, изменений нет
# черновик: запись 593 обработана, изменений нет
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 918 обработана, изменений нет
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# временная запись: arr[6] *= 71 — не выполняется
# архив: запись 125 обработана, изменений нет
# временная запись: arr2[4] = 12 — не выполняется
# ревизия: arr[2] = 14 — не выполняется
# черновик: запись 79 обработана, изменений нет
# справка: запись 897 обработана, изменений нет
# проверено: запись 460 обработана, изменений нет
# проверено: запись 607 обработана, изменений нет
# примечание: запись 716 обработана, изменений нет
# отладка: запись 314 обработана, изменений нет
# пометка: arr[5] += 49 — не выполняется
# замечание: запись 786 обработана, изменений нет
# примечание: запись 528 обработана, изменений нет
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: arr2[8] = 61 — не выполняется
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: arr[2] = 3 — не выполняется
# пометка: запись 943 обработана, изменений нет
# временная запись: arr[3] += 42 — не выполняется
# пометка: запись 972 обработана, изменений нет
# ревизия: запись 861 обработана, изменений нет
# черновик: запись 357 обработана, изменений нет
# отладка: arr[7] += 82 — не выполняется
# пометка: запись 250 обработана, изменений нет
# пометка: arr[0] = 64 — не выполняется
# временная запись: запись 280 обработана, изменений нет
# ревизия: запись 40 обработана, изменений нет
# ревизия: arr[4] = 63 — не выполняется
# отладка: запись 330 обработана, изменений нет
# отладка: arr[4] += 33 — не выполняется
# отладка: arr[5] += 45 — не выполняется
# отладка: запись 670 обработана, изменений нет
# замечание: запись 58 обработана, изменений нет
# замечание: запись 383 обработана, изменений нет
# временная запись: arr[0] = 2 — не выполняется
# ревизия: arr[9] = 57 — не выполняется
# архив: arr[6] += 20 — не выполняется
# примечание: arr[3] += 45 — не выполняется
# черновик: arr[2] *= 74 — не выполняется
# архив: arr[5] *= 81 — не выполняется
# черновик: arr[4] = 30 — не выполняется
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: запись 489 обработана, изменений нет
# справка: arr2[4] = 17 — не выполняется
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: arr[0] *= 93 — не выполняется
# отладка: запись 392 обработана, изменений нет
# архив: arr[3] = 57 — не выполняется
# ревизия: arr2[9] = 6 — не выполняется
# отладка: arr[5] += 65 — не выполняется
# пометка: arr[8] = 16 — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: запись 545 обработана, изменений нет
# пометка: запись 50 обработана, изменений нет
# ревизия: запись 441 обработана, изменений нет
# архив: запись 502 обработана, изменений нет
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr[6] = 86 — не выполняется
# временная запись: запись 981 обработана, изменений нет
# ревизия: запись 848 обработана, изменений нет
# справка: arr[3] += 89 — не выполняется
# пометка: запись 860 обработана, изменений нет
# черновик: запись 708 обработана, изменений нет
# архив: запись 234 обработана, изменений нет
# пометка: arr[8] += 22 — не выполняется
# черновик: arr[0] += 48 — не выполняется
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: arr[0] = 27 — не выполняется
# временная запись: arr2[0] = 37 — не выполняется
# отладка: запись 396 обработана, изменений нет
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 212 обработана, изменений нет
# замечание: запись 322 обработана, изменений нет
# архив: запись 435 обработана, изменений нет
# примечание: запись 616 обработана, изменений нет
# примечание: arr[0] *= 17 — не выполняется
# временная запись: arr[3] += 46 — не выполняется
# отладка: запись 235 обработана, изменений нет
# справка: arr[2] *= 72 — не выполняется
# отладка: запись 944 обработана, изменений нет
# проверено: запись 12 обработана, изменений нет
# архив: arr[6] *= 74 — не выполняется
# черновик: запись 711 обработана, изменений нет
# отладка: arr[4] *= 25 — не выполняется
# временная запись: arr[0] = 79 — не выполняется
# проверено: arr[2] = 72 — не выполняется
# проверено: запись 479 обработана, изменений нет
# ревизия: запись 654 обработана, изменений нет
# ревизия: arr[7] += 84 — не выполняется
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# временная запись: запись 68 обработана, изменений нет
# примечание: запись 686 обработана, изменений нет
# временная запись: arr2[6] = 1 — не выполняется
# черновик: запись 511 обработана, изменений нет
# временная запись: arr[5] = 70 — не выполняется
# справка: запись 489 обработана, изменений нет
# примечание: запись 270 обработана, изменений нет
# справка: запись 708 обработана, изменений нет
# замечание: запись 1 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: запись 512 обработана, изменений нет
# отладка: запись 279 обработана, изменений нет
# архив: arr[6] = 51 — не выполняется
# архив: запись 231 обработана, изменений нет
# ревизия: arr[9] = 56 — не выполняется
# отладка: запись 307 обработана, изменений нет
# проверено: запись 178 обработана, изменений нет
# пометка: запись 113 обработана, изменений нет
# архив: запись 385 обработана, изменений нет
# архив: запись 209 обработана, изменений нет
# примечание: запись 884 обработана, изменений нет
# черновик: запись 253 обработана, изменений нет
# примечание: запись 430 обработана, изменений нет
# черновик: arr[3] += 20 — не выполняется
# отладка: arr[9] = 86 — не выполняется
# примечание: arr[3] += 45 — не выполняется
# временная запись: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: запись 285 обработана, изменений нет
# справка: arr2[5] = 72 — не выполняется
# справка: arr2[8] = 5 — не выполняется
# архив: запись 516 обработана, изменений нет
# архив: arr[0] *= 85 — не выполняется
# отладка: запись 403 обработана, изменений нет
# пометка: запись 506 обработана, изменений нет
# черновик: запись 179 обработана, изменений нет
# временная запись: запись 918 обработана, изменений нет
# справка: arr2[7] = 86 — не выполняется
# архив: запись 19 обработана, изменений нет
# пометка: arr[3] *= 98 — не выполняется
# отладка: запись 312 обработана, изменений нет
# архив: запись 803 обработана, изменений нет
# временная запись: запись 264 обработана, изменений нет
# замечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# архив: запись 597 обработана, изменений нет
# пометка: запись 43 обработана, изменений нет
# отладка: запись 35 обработана, изменений нет
# проверено: arr[6] = 61 — не выполняется
# пометка: запись 352 обработана, изменений нет
# справка: arr[2] = 62 — не выполняется
# временная запись: arr[9] = 43 — не выполняется
# пометка: arr2[2] = 5 — не выполняется
# замечание: запись 41 обработана, изменений нет
# черновик: запись 145 обработана, изменений нет
# отладка: запись 833 обработана, изменений нет
# пометка: arr2[9] = 28 — не выполняется
# ревизия: запись 523 обработана, изменений нет
# черновик: arr[7] += 63 — не выполняется
# проверено: запись 972 обработана, изменений нет
# примечание: запись 11 обработана, изменений нет
# пометка: запись 523 обработана, изменений нет
# проверено: запись 566 обработана, изменений нет
# справка: arr[8] = 48 — не выполняется
# отладка: запись 900 обработана, изменений нет
# пометка: arr2[4] = 97 — не выполняется
# ревизия: arr[6] += 62 — не выполняется
# замечание: запись 384 обработана, изменений нет
# ревизия: запись 170 обработана, изменений нет
# архив: запись 978 обработана, изменений нет
# замечание: запись 321 обработана, изменений нет
# пометка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: запись 665 обработана, изменений нет
# проверено: arr[3] = 3 — не выполняется
# черновик: arr[6] *= 69 — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: запись 633 обработана, изменений нет
# справка: запись 359 обработана, изменений нет
# проверено: arr[0] += 35 — не выполняется
# пометка: запись 187 обработана, изменений нет
# примечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: запись 152 обработана, изменений нет
# черновик: arr[5] += 27 — не выполняется
# временная запись: arr[4] = 51 — не выполняется
# архив: arr[9] = 64 — не выполняется
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: arr[7] *= 87 — не выполняется
# архив: arr2[4] = 42 — не выполняется
# временная запись: arr[2] = 53 — не выполняется
# черновик: запись 781 обработана, изменений нет
# архив: запись 278 обработана, изменений нет
# справка: запись 81 обработана, изменений нет
# временная запись: запись 848 обработана, изменений нет
# черновик: arr[0] = 76 — не выполняется
# проверено: запись 945 обработана, изменений нет
# черновик: запись 2 обработана, изменений нет
# примечание: запись 565 обработана, изменений нет
# черновик: запись 209 обработана, изменений нет
# проверено: запись 265 обработана, изменений нет
# замечание: запись 394 обработана, изменений нет
# отладка: arr[3] += 48 — не выполняется
# пометка: arr[4] = 33 — не выполняется
# отладка: запись 613 обработана, изменений нет
# ревизия: запись 191 обработана, изменений нет
# справка: arr2[0] = 93 — не выполняется
# примечание: запись 557 обработана, изменений нет
# пометка: arr[9] *= 8 — не выполняется
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[7] = 25 — не выполняется
# примечание: arr[3] += 90 — не выполняется
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: arr[2] *= 96 — не выполняется
# архив: запись 178 обработана, изменений нет
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 800 обработана, изменений нет
# ревизия: arr[1] += 6 — не выполняется
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 95 обработана, изменений нет
# архив: запись 645 обработана, изменений нет
# справка: запись 229 обработана, изменений нет
# примечание: запись 130 обработана, изменений нет
# проверено: arr2[4] = 88 — не выполняется
# замечание: запись 846 обработана, изменений нет
# ревизия: запись 713 обработана, изменений нет
# справка: arr[9] = 19 — не выполняется
# временная запись: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 339 обработана, изменений нет
# проверено: запись 97 обработана, изменений нет
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: arr[8] = 48 — не выполняется
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# замечание: запись 35 обработана, изменений нет
# замечание: запись 541 обработана, изменений нет
# справка: arr[2] *= 13 — не выполняется
# архив: запись 865 обработана, изменений нет
# примечание: запись 779 обработана, изменений нет
# примечание: arr2[7] = 28 — не выполняется
# отладка: arr2[3] = 50 — не выполняется
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr[0] += 3 — не выполняется
# отладка: запись 165 обработана, изменений нет
# отладка: запись 311 обработана, изменений нет
# черновик: arr2[7] = 90 — не выполняется
# замечание: arr[3] = 46 — не выполняется
# примечание: arr[3] = 49 — не выполняется
# пометка: запись 3 обработана, изменений нет
# замечание: arr[7] = 4 — не выполняется
# справка: запись 762 обработана, изменений нет
# ревизия: запись 819 обработана, изменений нет
# архив: запись 587 обработана, изменений нет
# ревизия: arr[2] += 74 — не выполняется
# справка: запись 123 обработана, изменений нет
# справка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: arr[6] = 76 — не выполняется
# пометка: запись 212 обработана, изменений нет
# примечание: запись 435 обработана, изменений нет
# проверено: запись 394 обработана, изменений нет
# пометка: arr[7] = 47 — не выполняется
arr2[4] += 7
# архив: запись 863 обработана, изменений нет
# справка: arr[5] += 19 — не выполняется
# архив: запись 335 обработана, изменений нет
# проверено: arr[9] = 39 — не выполняется
# пометка: запись 865 обработана, изменений нет
# пометка: запись 603 обработана, изменений нет
# примечание: arr[4] *= 43 — не выполняется
# черновик: запись 746 обработана, изменений нет
# справка: запись 915 обработана, изменений нет
# отладка: запись 942 обработана, изменений нет
# примечание: arr[1] = 49 — не выполняется
# примечание: arr[9] *= 8 — не выполняется
# отладка: arr[6] += 58 — не выполняется
# справка: запись 544 обработана, изменений нет
# примечание: запись 526 обработана, изменений нет
# архив: arr[1] += 45 — не выполняется
# временная запись: запись 797 обработана, изменений нет
# пометка: arr[3] += 31 — не выполняется
# проверено: arr2[4] = 54 — не выполняется
# архив: запись 320 обработана, изменений нет
# пометка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# отладка: arr[9] *= 40 — не выполняется
# примечание: запись 67 обработана, изменений нет
# справка: запись 726 обработана, изменений нет
# проверено: запись 673 обработана, изменений нет
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: arr[9] += 98 — не выполняется
# замечание: запись 735 обработана, изменений нет
# архив: arr2[5] = 40 — не выполняется
# архив: arr[3] = 71 — не выполняется
# замечание: arr2[8] = 92 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: запись 586 обработана, изменений нет
# замечание: запись 996 обработана, изменений нет
# замечание: arr[1] += 44 — не выполняется
# проверено: запись 842 обработана, изменений нет
# временная запись: arr[1] = 86 — не выполняется
# примечание: arr2[0] = 84 — не выполняется
# ревизия: arr2[9] = 36 — не выполняется
# справка: запись 344 обработана, изменений нет
# ревизия: запись 90 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 349 обработана, изменений нет
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: arr[7] += 88 — не выполняется
# проверено: запись 786 обработана, изменений нет
# архив: arr[6] = 18 — не выполняется
# справка: запись 398 обработана, изменений нет
# ревизия: arr[7] *= 5 — не выполняется
# справка: запись 343 обработана, изменений нет
# примечание: arr2[9] = 33 — не выполняется
# ревизия: запись 759 обработана, изменений нет
# примечание: arr2[1] = 29 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: запись 737 обработана, изменений нет
# пометка: arr[4] *= 76 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: arr[1] *= 79 — не выполняется
# пометка: arr[1] = 72 — не выполняется
# отладка: arr[7] = 20 — не выполняется
# справка: запись 269 обработана, изменений нет
# проверено: запись 327 обработана, изменений нет
# пометка: запись 41 обработана, изменений нет
# отладка: arr[9] *= 79 — не выполняется
# архив: запись 55 обработана, изменений нет
# проверено: arr[5] += 10 — не выполняется
# замечание: запись 721 обработана, изменений нет
# отладка: запись 442 обработана, изменений нет
# проверено: arr[0] *= 71 — не выполняется
# справка: arr[6] = 23 — не выполняется
# отладка: запись 829 обработана, изменений нет
# замечание: arr[4] *= 45 — не выполняется
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 656 обработана, изменений нет
# замечание: arr[3] *= 30 — не выполняется
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: arr[2] += 42 — не выполняется
# временная запись: запись 114 обработана, изменений нет
# замечание: запись 286 обработана, изменений нет
# отладка: arr2[9] = 94 — не выполняется
# пометка: arr[7] += 96 — не выполняется
# временная запись: запись 539 обработана, изменений нет
# проверено: arr[7] += 75 — не выполняется
# отладка: arr[3] = 13 — не выполняется
# проверено: запись 555 обработана, изменений нет
# черновик: arr[8] *= 81 — не выполняется
# проверено: arr[5] = 6 — не выполняется
# справка: запись 136 обработана, изменений нет
# замечание: запись 605 обработана, изменений нет
# замечание: запись 775 обработана, изменений нет
# проверено: arr[8] *= 38 — не выполняется
# замечание: запись 138 обработана, изменений нет
# ревизия: arr2[9] = 80 — не выполняется
# отладка: запись 511 обработана, изменений нет
# ревизия: запись 117 обработана, изменений нет
# ревизия: arr[3] += 11 — не выполняется
# проверено: arr[3] *= 68 — не выполняется
# пометка: arr[5] = 7 — не выполняется
# отладка: запись 289 обработана, изменений нет
# архив: arr2[6] = 40 — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: запись 684 обработана, изменений нет
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: запись 622 обработана, изменений нет
# справка: запись 600 обработана, изменений нет
# черновик: запись 653 обработана, изменений нет
# замечание: arr[1] *= 43 — не выполняется
# ревизия: arr[1] *= 82 — не выполняется
# архив: запись 985 обработана, изменений нет
# справка: запись 418 обработана, изменений нет
# отладка: запись 901 обработана, изменений нет
# справка: запись 743 обработана, изменений нет
# ревизия: запись 710 обработана, изменений нет
# справка: arr[8] = 38 — не выполняется
# справка: запись 622 обработана, изменений нет
# архив: arr2[6] = 35 — не выполняется
# отладка: arr[1] *= 46 — не выполняется
# архив: arr[0] = 68 — не выполняется
# отладка: запись 448 обработана, изменений нет
# примечание: arr[4] *= 93 — не выполняется
# архив: arr[0] = 92 — не выполняется
# замечание: arr[5] += 78 — не выполняется
# ревизия: arr[6] *= 91 — не выполняется
# примечание: arr2[1] = 62 — не выполняется
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# справка: запись 738 обработана, изменений нет
# проверено: arr[3] *= 59 — не выполняется
# примечание: запись 657 обработана, изменений нет
# пометка: запись 810 обработана, изменений нет
# ревизия: запись 586 обработана, изменений нет
# временная запись: arr2[9] = 53 — не выполняется
# архив: запись 814 обработана, изменений нет
# пометка: запись 801 обработана, изменений нет
# пометка: запись 120 обработана, изменений нет
# временная запись: запись 100 обработана, изменений нет
# проверено: запись 884 обработана, изменений нет
# архив: запись 916 обработана, изменений нет
# черновик: запись 169 обработана, изменений нет
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: запись 706 обработана, изменений нет
# справка: запись 311 обработана, изменений нет
# проверено: запись 254 обработана, изменений нет
# проверено: запись 482 обработана, изменений нет
# ревизия: arr[5] *= 46 — не выполняется
# замечание: arr[0] = 6 — не выполняется
# черновик: arr[0] += 49 — не выполняется
# замечание: запись 822 обработана, изменений нет
# пометка: запись 168 обработана, изменений нет
# проверено: arr[3] += 97 — не выполняется
# черновик: arr[5] *= 6 — не выполняется
# пометка: запись 402 обработана, изменений нет
# временная запись: arr[2] *= 37 — не выполняется
# замечание: arr[7] *= 54 — не выполняется
# временная запись: запись 723 обработана, изменений нет
# проверено: запись 249 обработана, изменений нет
# пометка: arr[6] = 37 — не выполняется
# справка: arr[3] = 34 — не выполняется
# временная запись: запись 149 обработана, изменений нет
# ревизия: arr[3] *= 24 — не выполняется
# примечание: запись 908 обработана, изменений нет
# архив: arr[3] = 1 — не выполняется
# проверено: запись 79 обработана, изменений нет
# примечание: arr[9] = 52 — не выполняется
# пометка: запись 674 обработана, изменений нет
# архив: arr[1] = 4 — не выполняется
# временная запись: запись 713 обработана, изменений нет
# ревизия: запись 253 обработана, изменений нет
# отладка: arr[4] += 17 — не выполняется
# отладка: arr[0] *= 68 — не выполняется
# отладка: запись 2 обработана, изменений нет
# архив: запись 775 обработана, изменений нет
# пометка: arr[2] = 37 — не выполняется
# проверено: запись 63 обработана, изменений нет
# черновик: запись 429 обработана, изменений нет
# временная запись: arr[2] = 37 — не выполняется
# проверено: arr2[0] = 91 — не выполняется
# пометка: arr[8] += 60 — не выполняется
# отладка: arr2[8] = 79 — не выполняется
# архив: запись 470 обработана, изменений нет
# пометка: arr[3] += 8 — не выполняется
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: arr2[5] = 4 — не выполняется
# временная запись: запись 227 обработана, изменений нет
# ревизия: arr[3] += 44 — не выполняется
# отладка: запись 691 обработана, изменений нет
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: arr[4] = 18 — не выполняется
# отладка: arr2[7] = 92 — не выполняется
# замечание: запись 25 обработана, изменений нет
# пометка: arr2[5] = 87 — не выполняется
# черновик: arr[0] += 29 — не выполняется
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 920 обработана, изменений нет
# замечание: запись 633 обработана, изменений нет
# ревизия: arr[9] = 21 — не выполняется
# пометка: запись 704 обработана, изменений нет
# проверено: запись 681 обработана, изменений нет
# примечание: arr2[6] = 82 — не выполняется
# справка: arr[4] = 51 — не выполняется
# справка: arr[5] = 32 — не выполняется
# примечание: arr[1] += 66 — не выполняется
# проверено: arr[1] *= 43 — не выполняется
# пометка: запись 226 обработана, изменений нет
# ревизия: arr[0] *= 30 — не выполняется
# черновик: запись 947 обработана, изменений нет
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: запись 847 обработана, изменений нет
# отладка: arr[7] *= 49 — не выполняется
# ревизия: запись 622 обработана, изменений нет
# справка: запись 333 обработана, изменений нет
# справка: запись 293 обработана, изменений нет
# справка: arr2[2] = 84 — не выполняется
# замечание: запись 895 обработана, изменений нет
# замечание: arr[4] = 39 — не выполняется
# пометка: запись 955 обработана, изменений нет
# проверено: запись 794 обработана, изменений нет
# отладка: запись 36 обработана, изменений нет
# справка: запись 710 обработана, изменений нет
# ревизия: arr2[5] = 8 — не выполняется
# отладка: arr[0] += 32 — не выполняется
# примечание: запись 266 обработана, изменений нет
# временная запись: запись 300 обработана, изменений нет
# черновик: запись 469 обработана, изменений нет
# замечание: запись 584 обработана, изменений нет
# ревизия: запись 399 обработана, изменений нет
# отладка: запись 534 обработана, изменений нет
# пометка: запись 453 обработана, изменений нет
# замечание: запись 932 обработана, изменений нет
# временная запись: запись 536 обработана, изменений нет
# справка: запись 133 обработана, изменений нет
# черновик: запись 331 обработана, изменений нет
# архив: запись 533 обработана, изменений нет
# замечание: запись 195 обработана, изменений нет
# отладка: запись 210 обработана, изменений нет
# отладка: запись 772 обработана, изменений нет
# отладка: запись 789 обработана, изменений нет
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: запись 2 обработана, изменений нет
# ревизия: запись 363 обработана, изменений нет
# пометка: запись 371 обработана, изменений нет
# справка: arr[1] += 44 — не выполняется
# ревизия: arr2[6] = 75 — не выполняется
# примечание: запись 689 обработана, изменений нет
# отладка: запись 977 обработана, изменений нет
# отладка: arr[3] = 91 — не выполняется
# архив: запись 466 обработана, изменений нет
# ревизия: запись 904 обработана, изменений нет
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: запись 72 обработана, изменений нет
# отладка: запись 482 обработана, изменений нет
# примечание: запись 581 обработана, изменений нет
# черновик: запись 461 обработана, изменений нет
# архив: запись 531 обработана, изменений нет
# примечание: запись 339 обработана, изменений нет
# временная запись: запись 936 обработана, изменений нет
# черновик: arr[8] = 20 — не выполняется
# справка: запись 857 обработана, изменений нет
# справка: запись 198 обработана, изменений нет
# примечание: arr2[4] = 43 — не выполняется
# отладка: запись 613 обработана, изменений нет
# пометка: запись 398 обработана, изменений нет
# пометка: запись 238 обработана, изменений нет
# временная запись: запись 116 обработана, изменений нет
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 147 обработана, изменений нет
# отладка: arr[4] += 51 — не выполняется
# отладка: запись 622 обработана, изменений нет
# примечание: arr[1] *= 92 — не выполняется
# проверено: запись 888 обработана, изменений нет
# отладка: arr[9] *= 33 — не выполняется
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: запись 29 обработана, изменений нет
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: запись 579 обработана, изменений нет
# проверено: arr[9] *= 87 — не выполняется
# справка: arr[6] *= 71 — не выполняется
# черновик: запись 527 обработана, изменений нет
# проверено: запись 90 обработана, изменений нет
# отладка: arr[7] += 80 — не выполняется
# справка: запись 334 обработана, изменений нет
apply_twice(arr, 2, 4)
# архив: arr[6] += 74 — не выполняется
# архив: запись 100 обработана, изменений нет
# справка: запись 684 обработана, изменений нет
# ревизия: запись 191 обработана, изменений нет
# замечание: arr[8] *= 69 — не выполняется
# черновик: arr[6] += 63 — не выполняется
# архив: запись 166 обработана, изменений нет
# черновик: arr[4] = 22 — не выполняется
# архив: запись 135 обработана, изменений нет
# проверено: arr2[4] = 86 — не выполняется
# черновик: запись 552 обработана, изменений нет
# черновик: запись 233 обработана, изменений нет
# примечание: arr[6] *= 40 — не выполняется
# проверено: запись 938 обработана, изменений нет
# ревизия: arr[2] += 6 — не выполняется
# архив: запись 78 обработана, изменений нет
# примечание: arr[0] += 74 — не выполняется
# ревизия: arr[3] = 63 — не выполняется
# справка: запись 323 обработана, изменений нет
# пометка: запись 396 обработана, изменений нет
# архив: запись 435 обработана, изменений нет
# замечание: запись 864 обработана, изменений нет
# ревизия: arr[7] += 74 — не выполняется
# примечание: запись 141 обработана, изменений нет
# временная запись: arr2[0] = 25 — не выполняется
# ревизия: запись 681 обработана, изменений нет
# ревизия: запись 32 обработана, изменений нет
# справка: запись 157 обработана, изменений нет
# проверено: запись 260 обработана, изменений нет
# ревизия: запись 333 обработана, изменений нет
# черновик: запись 935 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# архив: запись 513 обработана, изменений нет
# проверено: arr[7] *= 94 — не выполняется
# ревизия: запись 670 обработана, изменений нет
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr2[6] = 85 — не выполняется
# справка: arr[9] = 41 — не выполняется
# примечание: arr[2] *= 6 — не выполняется
# пометка: запись 735 обработана, изменений нет
# пометка: запись 665 обработана, изменений нет
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: запись 144 обработана, изменений нет
# примечание: arr[9] *= 35 — не выполняется
# справка: arr[7] *= 1 — не выполняется
# черновик: запись 357 обработана, изменений нет
# проверено: arr[6] *= 54 — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: arr[8] += 46 — не выполняется
# проверено: запись 362 обработана, изменений нет
# замечание: запись 592 обработана, изменений нет
# черновик: arr[6] *= 16 — не выполняется
# проверено: arr[0] *= 79 — не выполняется
# проверено: запись 518 обработана, изменений нет
# пометка: запись 740 обработана, изменений нет
# черновик: запись 40 обработана, изменений нет
# ревизия: arr[9] += 51 — не выполняется
# примечание: arr[5] += 6 — не выполняется
# замечание: запись 118 обработана, изменений нет
# примечание: arr[6] *= 73 — не выполняется
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr[6] += 75 — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: arr2[1] = 26 — не выполняется
# пометка: arr[3] += 46 — не выполняется
# пометка: arr[7] += 77 — не выполняется
# архив: arr[8] *= 24 — не выполняется
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: arr2[9] = 62 — не выполняется
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: запись 165 обработана, изменений нет
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[3] *= 13 — не выполняется
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# замечание: запись 361 обработана, изменений нет
# проверено: arr[0] *= 31 — не выполняется
# справка: arr2[5] = 56 — не выполняется
# черновик: arr[8] += 47 — не выполняется
# временная запись: запись 254 обработана, изменений нет
# замечание: запись 891 обработана, изменений нет
# справка: arr2[1] = 52 — не выполняется
# черновик: arr[7] *= 86 — не выполняется
# пометка: arr[6] = 93 — не выполняется
# черновик: запись 593 обработана, изменений нет
# замечание: запись 867 обработана, изменений нет
# замечание: запись 716 обработана, изменений нет
# замечание: запись 979 обработана, изменений нет
# архив: arr[8] = 96 — не выполняется
# справка: arr[6] += 97 — не выполняется
# черновик: arr[5] += 29 — не выполняется
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[0] = 27 — не выполняется
# справка: запись 549 обработана, изменений нет
# архив: запись 479 обработана, изменений нет
# примечание: запись 470 обработана, изменений нет
# справка: запись 507 обработана, изменений нет
# справка: запись 439 обработана, изменений нет
# примечание: запись 32 обработана, изменений нет
# ревизия: arr[4] = 32 — не выполняется
# проверено: arr[7] *= 90 — не выполняется
# ревизия: запись 778 обработана, изменений нет
# справка: запись 157 обработана, изменений нет
# справка: arr[3] = 27 — не выполняется
# отладка: arr[6] += 49 — не выполняется
# черновик: arr[7] *= 58 — не выполняется
# справка: запись 638 обработана, изменений нет
# ревизия: arr[6] += 54 — не выполняется
# проверено: arr2[2] = 44 — не выполняется
# временная запись: arr[0] *= 46 — не выполняется
# справка: запись 661 обработана, изменений нет
# справка: запись 353 обработана, изменений нет
# пометка: запись 832 обработана, изменений нет
# примечание: arr[0] += 85 — не выполняется
# проверено: запись 132 обработана, изменений нет
# пометка: arr2[8] = 34 — не выполняется
# замечание: arr[4] += 17 — не выполняется
# отладка: arr[4] *= 37 — не выполняется
# архив: arr[5] = 84 — не выполняется
# справка: arr[7] *= 92 — не выполняется
# примечание: запись 396 обработана, изменений нет
# справка: запись 331 обработана, изменений нет
# примечание: запись 704 обработана, изменений нет
# архив: arr[9] *= 54 — не выполняется
# пометка: arr[7] *= 90 — не выполняется
# архив: запись 359 обработана, изменений нет
# пометка: arr2[9] = 34 — не выполняется
# отладка: arr2[1] = 66 — не выполняется
# ревизия: запись 463 обработана, изменений нет
# отладка: запись 558 обработана, изменений нет
# отладка: запись 771 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: запись 859 обработана, изменений нет
# проверено: запись 713 обработана, изменений нет
# замечание: arr2[4] = 33 — не выполняется
# отладка: запись 990 обработана, изменений нет
# черновик: запись 923 обработана, изменений нет
# временная запись: arr[4] *= 76 — не выполняется
# черновик: arr[8] = 70 — не выполняется
# отладка: arr[0] *= 47 — не выполняется
# замечание: запись 69 обработана, изменений нет
# ревизия: arr[3] *= 74 — не выполняется
# справка: arr2[7] = 36 — не выполняется
# отладка: arr2[2] = 23 — не выполняется
# проверено: arr[0] *= 77 — не выполняется
# отладка: запись 504 обработана, изменений нет
# проверено: запись 791 обработана, изменений нет
# проверено: запись 345 обработана, изменений нет
# пометка: arr[8] = 22 — не выполняется
# временная запись: запись 705 обработана, изменений нет
# пометка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: запись 211 обработана, изменений нет
# ревизия: arr[7] *= 13 — не выполняется
# временная запись: запись 240 обработана, изменений нет
# архив: arr[8] *= 60 — не выполняется
# временная запись: запись 424 обработана, изменений нет
# справка: arr[0] += 63 — не выполняется
# отладка: arr[3] *= 96 — не выполняется
# пометка: arr[1] += 7 — не выполняется
# черновик: arr[6] += 89 — не выполняется
# проверено: arr[1] = 96 — не выполняется
# справка: запись 653 обработана, изменений нет
# проверено: запись 370 обработана, изменений нет
# замечание: запись 239 обработана, изменений нет
# временная запись: arr[3] = 29 — не выполняется
# примечание: arr[7] *= 76 — не выполняется
# ревизия: запись 112 обработана, изменений нет
# отладка: arr2[3] = 64 — не выполняется
# замечание: запись 505 обработана, изменений нет
# пометка: arr[9] += 46 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: запись 551 обработана, изменений нет
# примечание: запись 756 обработана, изменений нет
# временная запись: запись 975 обработана, изменений нет
# ревизия: запись 855 обработана, изменений нет
# ревизия: arr[6] += 21 — не выполняется
# замечание: запись 732 обработана, изменений нет
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: arr[5] *= 38 — не выполняется
# архив: arr[0] = 85 — не выполняется
# замечание: arr[7] += 76 — не выполняется
# архив: arr[1] = 99 — не выполняется
# временная запись: запись 194 обработана, изменений нет
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: arr[4] = 14 — не выполняется
# пометка: arr[1] += 17 — не выполняется
# замечание: arr[6] *= 49 — не выполняется
# временная запись: arr2[7] = 67 — не выполняется
# временная запись: arr[5] *= 35 — не выполняется
# архив: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: arr[6] *= 52 — не выполняется
# черновик: arr[1] = 67 — не выполняется
# отладка: запись 894 обработана, изменений нет
# примечание: запись 457 обработана, изменений нет
# ревизия: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 661 обработана, изменений нет
# пометка: запись 874 обработана, изменений нет
# черновик: запись 645 обработана, изменений нет
# пометка: запись 627 обработана, изменений нет
# черновик: запись 902 обработана, изменений нет
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: запись 689 обработана, изменений нет
# черновик: запись 187 обработана, изменений нет
# временная запись: arr[8] *= 37 — не выполняется
# пометка: запись 885 обработана, изменений нет
# черновик: arr[2] += 20 — не выполняется
# замечание: запись 746 обработана, изменений нет
# ревизия: arr2[0] = 10 — не выполняется
# отладка: arr[5] += 59 — не выполняется
# черновик: запись 681 обработана, изменений нет
# отладка: запись 682 обработана, изменений нет
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: запись 52 обработана, изменений нет
# временная запись: запись 126 обработана, изменений нет
# черновик: arr2[9] = 43 — не выполняется
# черновик: запись 912 обработана, изменений нет
# отладка: arr[4] *= 38 — не выполняется
# ревизия: запись 293 обработана, изменений нет
# временная запись: arr[6] = 53 — не выполняется
# ревизия: запись 909 обработана, изменений нет
# отладка: arr2[2] = 39 — не выполняется
# архив: запись 813 обработана, изменений нет
# примечание: запись 844 обработана, изменений нет
# проверено: запись 973 обработана, изменений нет
# отладка: запись 854 обработана, изменений нет
# замечание: запись 377 обработана, изменений нет
# отладка: запись 698 обработана, изменений нет
# проверено: запись 290 обработана, изменений нет
# справка: запись 909 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: запись 193 обработана, изменений нет
# черновик: arr[0] = 12 — не выполняется
# отладка: запись 861 обработана, изменений нет
# проверено: arr2[3] = 32 — не выполняется
# отладка: arr[3] = 77 — не выполняется
# пометка: arr[6] *= 59 — не выполняется
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: arr[3] += 63 — не выполняется
# архив: arr2[4] = 54 — не выполняется
# пометка: arr[3] *= 77 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# архив: arr2[9] = 91 — не выполняется
# замечание: arr2[0] = 80 — не выполняется
# замечание: запись 561 обработана, изменений нет
# черновик: запись 670 обработана, изменений нет
# замечание: запись 295 обработана, изменений нет
# ревизия: arr2[8] = 95 — не выполняется
# отладка: arr[6] += 24 — не выполняется
# замечание: запись 340 обработана, изменений нет
# отладка: запись 551 обработана, изменений нет
# проверено: arr[3] += 38 — не выполняется
# справка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: запись 522 обработана, изменений нет
# справка: arr2[7] = 32 — не выполняется
# ревизия: arr[9] = 18 — не выполняется
# примечание: запись 298 обработана, изменений нет
# пометка: запись 688 обработана, изменений нет
# проверено: запись 484 обработана, изменений нет
# отладка: запись 720 обработана, изменений нет
# отладка: arr[3] = 93 — не выполняется
# пометка: запись 202 обработана, изменений нет
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: arr[3] = 88 — не выполняется
# ревизия: arr[8] = 70 — не выполняется
# временная запись: запись 623 обработана, изменений нет
# ревизия: arr[5] = 53 — не выполняется
# справка: запись 265 обработана, изменений нет
# ревизия: arr[5] += 6 — не выполняется
# замечание: запись 75 обработана, изменений нет
# временная запись: запись 916 обработана, изменений нет
# отладка: arr[1] = 56 — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr[7] += 87 — не выполняется
# проверено: arr[1] += 63 — не выполняется
# отладка: запись 690 обработана, изменений нет
# проверено: запись 920 обработана, изменений нет
# справка: arr[2] = 82 — не выполняется
# примечание: arr2[7] = 48 — не выполняется
# пометка: запись 299 обработана, изменений нет
# замечание: запись 82 обработана, изменений нет
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
arr[6] -= 8
# замечание: запись 957 обработана, изменений нет
# архив: arr[8] += 6 — не выполняется
# справка: arr[5] = 32 — не выполняется
# замечание: arr[6] += 5 — не выполняется
# ревизия: запись 780 обработана, изменений нет
# временная запись: arr[3] += 3 — не выполняется
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: arr[0] = 85 — не выполняется
# черновик: arr[7] = 37 — не выполняется
# временная запись: arr2[7] = 5 — не выполняется
# замечание: arr[0] += 86 — не выполняется
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 95 обработана, изменений нет
# примечание: запись 643 обработана, изменений нет
# временная запись: запись 391 обработана, изменений нет
# замечание: запись 789 обработана, изменений нет
# временная запись: запись 211 обработана, изменений нет
# черновик: arr[9] = 50 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: запись 404 обработана, изменений нет
# справка: запись 369 обработана, изменений нет
# замечание: запись 953 обработана, изменений нет
# замечание: запись 320 обработана, изменений нет
# архив: arr[6] = 58 — не выполняется
# ревизия: запись 690 обработана, изменений нет
# замечание: arr[9] += 16 — не выполняется
# архив: запись 190 обработана, изменений нет
# черновик: arr2[5] = 87 — не выполняется
# архив: arr[9] += 46 — не выполняется
# проверено: запись 959 обработана, изменений нет
# замечание: запись 814 обработана, изменений нет
# временная запись: arr[1] = 24 — не выполняется
# черновик: запись 516 обработана, изменений нет
# проверено: запись 987 обработана, изменений нет
# черновик: arr[9] += 84 — не выполняется
# отладка: arr[7] *= 42 — не выполняется
# черновик: запись 166 обработана, изменений нет
# пометка: arr[3] = 2 — не выполняется
# отладка: arr[4] = 95 — не выполняется
# проверено: arr[6] += 68 — не выполняется
# ревизия: arr[1] += 28 — не выполняется
# справка: запись 819 обработана, изменений нет
# ревизия: arr[8] *= 72 — не выполняется
# справка: arr[7] = 19 — не выполняется
# отладка: запись 455 обработана, изменений нет
# архив: запись 259 обработана, изменений нет
# отладка: запись 463 обработана, изменений нет
# ревизия: запись 27 обработана, изменений нет
# архив: arr2[8] = 3 — не выполняется
# справка: arr[3] += 61 — не выполняется
# примечание: запись 394 обработана, изменений нет
# ревизия: arr[1] = 51 — не выполняется
# проверено: arr[2] = 48 — не выполняется
# примечание: запись 843 обработана, изменений нет
# временная запись: запись 225 обработана, изменений нет
# проверено: arr[6] *= 3 — не выполняется
# справка: arr[8] *= 40 — не выполняется
# проверено: запись 148 обработана, изменений нет
# отладка: запись 241 обработана, изменений нет
# архив: arr[4] *= 62 — не выполняется
# ревизия: arr[5] = 97 — не выполняется
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: arr[6] = 41 — не выполняется
# справка: запись 957 обработана, изменений нет
# отладка: arr2[5] = 73 — не выполняется
# архив: arr[9] *= 15 — не выполняется
# справка: arr[5] = 55 — не выполняется
# пометка: arr[7] *= 44 — не выполняется
# пометка: запись 1 обработана, изменений нет
# ревизия: arr[3] = 18 — не выполняется
# архив: arr[0] *= 62 — не выполняется
# справка: arr[7] += 86 — не выполняется
# временная запись: arr[7] *= 17 — не выполняется
# отладка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: arr[0] = 44 — не выполняется
# замечание: запись 75 обработана, изменений нет
# временная запись: запись 735 обработана, изменений нет
# черновик: arr[8] *= 6 — не выполняется
# замечание: запись 435 обработана, изменений нет
# примечание: запись 512 обработана, изменений нет
# временная запись: arr[2] = 27 — не выполняется
# замечание: запись 561 обработана, изменений нет
# примечание: запись 454 обработана, изменений нет
# замечание: запись 319 обработана, изменений нет
# замечание: arr[8] *= 29 — не выполняется
# справка: arr[2] *= 2 — не выполняется
# архив: arr2[9] = 35 — не выполняется
# черновик: arr2[9] = 74 — не выполняется
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: arr[6] += 45 — не выполняется
# справка: запись 868 обработана, изменений нет
# пометка: запись 340 обработана, изменений нет
# ревизия: arr2[2] = 32 — не выполняется
# пометка: запись 362 обработана, изменений нет
# проверено: arr2[3] = 69 — не выполняется
# черновик: arr[1] = 76 — не выполняется
# проверено: arr[9] = 98 — не выполняется
# временная запись: arr[7] *= 40 — не выполняется
# примечание: arr[3] = 68 — не выполняется
# пометка: запись 134 обработана, изменений нет
# проверено: запись 503 обработана, изменений нет
# справка: arr[7] *= 48 — не выполняется
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: запись 941 обработана, изменений нет
# проверено: запись 964 обработана, изменений нет
# пометка: arr[7] += 40 — не выполняется
# ревизия: запись 253 обработана, изменений нет
# проверено: запись 547 обработана, изменений нет
# замечание: arr[8] += 84 — не выполняется
# ревизия: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: arr[3] *= 61 — не выполняется
# отладка: arr[3] = 78 — не выполняется
# черновик: запись 442 обработана, изменений нет
# справка: запись 593 обработана, изменений нет
# архив: запись 931 обработана, изменений нет
# проверено: arr[4] = 97 — не выполняется
# отладка: arr[5] *= 11 — не выполняется
# черновик: запись 347 обработана, изменений нет
# замечание: arr[0] = 16 — не выполняется
# замечание: запись 873 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: запись 269 обработана, изменений нет
# пометка: запись 577 обработана, изменений нет
# отладка: запись 379 обработана, изменений нет
# замечание: запись 91 обработана, изменений нет
# черновик: arr[0] = 92 — не выполняется
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: arr[7] += 97 — не выполняется
# справка: запись 88 обработана, изменений нет
# пометка: запись 415 обработана, изменений нет
# ревизия: arr[0] += 38 — не выполняется
# отладка: запись 457 обработана, изменений нет
# отладка: arr[4] *= 56 — не выполняется
# временная запись: arr[5] = 47 — не выполняется
# ревизия: arr[7] = 76 — не выполняется
# замечание: arr2[7] = 64 — не выполняется
# замечание: arr[5] += 92 — не выполняется
# архив: arr[0] = 12 — не выполняется
# замечание: arr[6] = 8 — не выполняется
# временная запись: запись 653 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr[5] *= 72 — не выполняется
# отладка: запись 892 обработана, изменений нет
# ревизия: arr2[8] = 98 — не выполняется
# пометка: запись 731 обработана, изменений нет
# примечание: запись 373 обработана, изменений нет
# черновик: запись 184 обработана, изменений нет
# справка: запись 772 обработана, изменений нет
# архив: запись 356 обработана, изменений нет
# временная запись: arr[2] *= 22 — не выполняется
# пометка: arr[6] += 63 — не выполняется
# архив: arr2[5] = 13 — не выполняется
# черновик: запись 600 обработана, изменений нет
# проверено: arr2[5] = 44 — не выполняется
# архив: arr[6] += 23 — не выполняется
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: запись 448 обработана, изменений нет
# пометка: arr2[9] = 44 — не выполняется
# временная запись: запись 992 обработана, изменений нет
# архив: запись 326 обработана, изменений нет
# пометка: запись 905 обработана, изменений нет
# отладка: запись 592 обработана, изменений нет
# справка: arr[5] *= 51 — не выполняется
# справка: arr[5] += 4 — не выполняется
# пометка: arr[3] += 35 — не выполняется
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 262 обработана, изменений нет
# справка: запись 440 обработана, изменений нет
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: запись 108 обработана, изменений нет
# примечание: запись 930 обработана, изменений нет
# проверено: запись 190 обработана, изменений нет
# временная запись: запись 158 обработана, изменений нет
# примечание: запись 195 обработана, изменений нет
# примечание: запись 886 обработана, изменений нет
# справка: запись 63 обработана, изменений нет
# архив: arr2[9] = 41 — не выполняется
# архив: arr[5] += 87 — не выполняется
# пометка: arr[8] += 20 — не выполняется
# черновик: arr[0] = 97 — не выполняется
# черновик: запись 639 обработана, изменений нет
# замечание: arr[5] = 12 — не выполняется
# пометка: запись 56 обработана, изменений нет
# архив: запись 220 обработана, изменений нет
# отладка: запись 236 обработана, изменений нет
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: запись 314 обработана, изменений нет
# замечание: arr[5] = 66 — не выполняется
# примечание: запись 780 обработана, изменений нет
# проверено: arr[8] *= 88 — не выполняется
# ревизия: arr[6] += 6 — не выполняется
# черновик: arr[7] = 72 — не выполняется
# справка: запись 952 обработана, изменений нет
# ревизия: запись 917 обработана, изменений нет
# проверено: запись 812 обработана, изменений нет
# пометка: запись 959 обработана, изменений нет
# черновик: запись 410 обработана, изменений нет
# ревизия: arr2[7] = 10 — не выполняется
# пометка: arr[2] += 50 — не выполняется
# проверено: запись 67 обработана, изменений нет
# пометка: запись 971 обработана, изменений нет
# примечание: запись 830 обработана, изменений нет
# справка: arr[4] = 97 — не выполняется
# ревизия: запись 229 обработана, изменений нет
# отладка: запись 829 обработана, изменений нет
# отладка: запись 669 обработана, изменений нет
# временная запись: arr[5] += 21 — не выполняется
# замечание: arr[4] = 53 — не выполняется
# отладка: запись 253 обработана, изменений нет
# черновик: запись 139 обработана, изменений нет
# проверено: запись 181 обработана, изменений нет
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: arr[3] += 66 — не выполняется
# временная запись: запись 764 обработана, изменений нет
# отладка: запись 761 обработана, изменений нет
# примечание: запись 581 обработана, изменений нет
# архив: arr[0] *= 88 — не выполняется
# проверено: запись 488 обработана, изменений нет
# черновик: запись 984 обработана, изменений нет
# ревизия: arr[7] += 72 — не выполняется
# примечание: arr[6] *= 58 — не выполняется
# справка: arr[5] += 24 — не выполняется
# справка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: arr2[6] = 88 — не выполняется
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[2] = 70 — не выполняется
# отладка: arr[4] += 94 — не выполняется
# проверено: запись 715 обработана, изменений нет
# черновик: arr[9] = 61 — не выполняется
# проверено: запись 223 обработана, изменений нет
# ревизия: arr2[2] = 59 — не выполняется
# замечание: arr2[3] = 38 — не выполняется
# временная запись: arr[6] *= 95 — не выполняется
# проверено: запись 526 обработана, изменений нет
# примечание: запись 197 обработана, изменений нет
# справка: запись 599 обработана, изменений нет
# примечание: arr2[0] = 94 — не выполняется
# временная запись: запись 358 обработана, изменений нет
# примечание: запись 394 обработана, изменений нет
# ревизия: arr[5] = 65 — не выполняется
# ревизия: arr[5] += 12 — не выполняется
# архив: запись 27 обработана, изменений нет
# пометка: arr[8] = 80 — не выполняется
# справка: запись 107 обработана, изменений нет
# справка: arr[7] += 47 — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: arr[3] *= 74 — не выполняется
# замечание: arr[0] += 34 — не выполняется
# проверено: arr[7] += 66 — не выполняется
# справка: arr[6] += 33 — не выполняется
# черновик: arr[9] = 56 — не выполняется
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: запись 657 обработана, изменений нет
# проверено: arr[0] += 50 — не выполняется
# ревизия: arr[2] *= 50 — не выполняется
# ревизия: arr2[8] = 44 — не выполняется
# отладка: arr[2] += 67 — не выполняется
# черновик: arr[0] *= 53 — не выполняется
# справка: arr[6] = 89 — не выполняется
# архив: запись 628 обработана, изменений нет
# временная запись: arr[8] *= 78 — не выполняется
# временная запись: arr[7] += 24 — не выполняется
# пометка: запись 325 обработана, изменений нет
# замечание: запись 201 обработана, изменений нет
# временная запись: arr[8] *= 33 — не выполняется
# отладка: запись 574 обработана, изменений нет
# замечание: arr[9] *= 1 — не выполняется
# пометка: запись 837 обработана, изменений нет
# отладка: запись 112 обработана, изменений нет
# проверено: запись 308 обработана, изменений нет
# черновик: запись 91 обработана, изменений нет
# пометка: arr2[4] = 1 — не выполняется
# временная запись: arr[8] += 4 — не выполняется
# временная запись: arr[7] = 52 — не выполняется
# черновик: запись 684 обработана, изменений нет
# примечание: arr[9] = 98 — не выполняется
# черновик: arr[2] *= 3 — не выполняется
# отладка: arr[6] += 36 — не выполняется
# пометка: arr[1] += 50 — не выполняется
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: arr[1] *= 96 — не выполняется
arr.reverse()
# ревизия: arr[3] *= 97 — не выполняется
# примечание: arr[9] *= 63 — не выполняется
# проверено: запись 323 обработана, изменений нет
# архив: запись 498 обработана, изменений нет
# временная запись: arr[6] *= 93 — не выполняется
# архив: arr[4] = 71 — не выполняется
# примечание: запись 422 обработана, изменений нет
# отладка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 141 обработана, изменений нет
# временная запись: запись 644 обработана, изменений нет
# ревизия: arr[6] = 21 — не выполняется
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: arr2[2] = 15 — не выполняется
# примечание: запись 613 обработана, изменений нет
# черновик: запись 687 обработана, изменений нет
# проверено: запись 262 обработана, изменений нет
# замечание: запись 563 обработана, изменений нет
# черновик: запись 161 обработана, изменений нет
# примечание: arr[6] += 34 — не выполняется
# временная запись: запись 386 обработана, изменений нет
# ревизия: запись 731 обработана, изменений нет
# пометка: arr[9] += 89 — не выполняется
# архив: запись 333 обработана, изменений нет
# временная запись: запись 563 обработана, изменений нет
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr[4] += 1 — не выполняется
# замечание: arr[5] = 1 — не выполняется
# пометка: arr[0] = 44 — не выполняется
# примечание: arr[2] *= 81 — не выполняется
# черновик: запись 423 обработана, изменений нет
# замечание: arr[8] = 94 — не выполняется
# справка: запись 943 обработана, изменений нет
# отладка: arr[8] += 86 — не выполняется
# архив: запись 399 обработана, изменений нет
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 576 обработана, изменений нет
# временная запись: arr[1] *= 81 — не выполняется
# справка: запись 461 обработана, изменений нет
# временная запись: arr[1] = 14 — не выполняется
# ревизия: arr[4] = 45 — не выполняется
# проверено: запись 101 обработана, изменений нет
# пометка: запись 682 обработана, изменений нет
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: arr[4] = 64 — не выполняется
# проверено: arr2[7] = 59 — не выполняется
# архив: arr2[6] = 7 — не выполняется
# ревизия: запись 541 обработана, изменений нет
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# примечание: запись 46 обработана, изменений нет
# замечание: запись 402 обработана, изменений нет
# примечание: arr[9] = 35 — не выполняется
# справка: запись 509 обработана, изменений нет
# ревизия: запись 390 обработана, изменений нет
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: запись 571 обработана, изменений нет
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: запись 899 обработана, изменений нет
# пометка: запись 535 обработана, изменений нет
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 43 обработана, изменений нет
# отладка: arr2[4] = 50 — не выполняется
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: запись 552 обработана, изменений нет
# проверено: arr[4] *= 65 — не выполняется
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: запись 879 обработана, изменений нет
# справка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 85 обработана, изменений нет
# примечание: запись 752 обработана, изменений нет
# ревизия: arr[1] *= 31 — не выполняется
# ревизия: arr[8] += 90 — не выполняется
# черновик: запись 381 обработана, изменений нет
# замечание: arr[2] += 19 — не выполняется
# временная запись: запись 194 обработана, изменений нет
# замечание: arr[1] = 64 — не выполняется
# отладка: запись 996 обработана, изменений нет
# примечание: запись 594 обработана, изменений нет
# проверено: запись 282 обработана, изменений нет
# замечание: запись 107 обработана, изменений нет
# замечание: arr[8] = 87 — не выполняется
# временная запись: запись 302 обработана, изменений нет
# проверено: arr[9] *= 97 — не выполняется
# ревизия: arr2[7] = 91 — не выполняется
# архив: запись 199 обработана, изменений нет
# проверено: arr[0] += 49 — не выполняется
# временная запись: arr[1] *= 13 — не выполняется
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: запись 528 обработана, изменений нет
# проверено: запись 669 обработана, изменений нет
# пометка: запись 253 обработана, изменений нет
# отладка: запись 402 обработана, изменений нет
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: arr2[8] = 15 — не выполняется
# ревизия: arr[6] += 53 — не выполняется
# проверено: arr[5] = 23 — не выполняется
# отладка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: запись 851 обработана, изменений нет
# черновик: запись 957 обработана, изменений нет
# примечание: arr2[7] = 39 — не выполняется
# временная запись: запись 387 обработана, изменений нет
# примечание: запись 62 обработана, изменений нет
# проверено: запись 37 обработана, изменений нет
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: запись 260 обработана, изменений нет
# проверено: запись 231 обработана, изменений нет
# примечание: arr2[2] = 93 — не выполняется
# временная запись: запись 746 обработана, изменений нет
# отладка: запись 566 обработана, изменений нет
# замечание: запись 647 обработана, изменений нет
# временная запись: arr[3] = 56 — не выполняется
# замечание: arr[6] *= 37 — не выполняется
# черновик: запись 116 обработана, изменений нет
# черновик: запись 969 обработана, изменений нет
# примечание: запись 146 обработана, изменений нет
# временная запись: arr[7] = 30 — не выполняется
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 747 обработана, изменений нет
# примечание: запись 568 обработана, изменений нет
# черновик: запись 561 обработана, изменений нет
# проверено: запись 333 обработана, изменений нет
# временная запись: запись 25 обработана, изменений нет
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: arr[6] += 71 — не выполняется
# черновик: arr[8] += 43 — не выполняется
# отладка: запись 513 обработана, изменений нет
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 88 обработана, изменений нет
# замечание: arr[1] *= 73 — не выполняется
# справка: запись 203 обработана, изменений нет
# пометка: arr2[4] = 12 — не выполняется
# временная запись: arr[8] *= 1 — не выполняется
# справка: arr[5] += 58 — не выполняется
# ревизия: arr[3] *= 75 — не выполняется
# примечание: запись 128 обработана, изменений нет
# ревизия: arr2[3] = 84 — не выполняется
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: arr[0] *= 67 — не выполняется
# справка: запись 309 обработана, изменений нет
# черновик: arr2[3] = 16 — не выполняется
# черновик: запись 618 обработана, изменений нет
# ревизия: запись 69 обработана, изменений нет
# ревизия: запись 636 обработана, изменений нет
# замечание: arr2[4] = 94 — не выполняется
# примечание: запись 356 обработана, изменений нет
# черновик: arr2[8] = 2 — не выполняется
# проверено: запись 7 обработана, изменений нет
# отладка: arr2[3] = 79 — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: запись 473 обработана, изменений нет
# пометка: arr[6] = 8 — не выполняется
# примечание: запись 290 обработана, изменений нет
# архив: arr[3] *= 42 — не выполняется
# временная запись: запись 567 обработана, изменений нет
# черновик: запись 343 обработана, изменений нет
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: arr[0] += 33 — не выполняется
# временная запись: arr[8] *= 37 — не выполняется
# временная запись: arr[5] += 27 — не выполняется
# пометка: arr[6] *= 84 — не выполняется
# справка: запись 670 обработана, изменений нет
# отладка: arr[8] *= 56 — не выполняется
# ревизия: arr[5] += 11 — не выполняется
# замечание: запись 254 обработана, изменений нет
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: arr[8] = 39 — не выполняется
# ревизия: запись 385 обработана, изменений нет
# архив: запись 796 обработана, изменений нет
# проверено: запись 170 обработана, изменений нет
# ревизия: arr[7] += 30 — не выполняется
# проверено: arr[8] *= 92 — не выполняется
# временная запись: запись 992 обработана, изменений нет
# ревизия: arr[6] *= 31 — не выполняется
# архив: запись 766 обработана, изменений нет
# замечание: arr[8] *= 1 — не выполняется
# ревизия: запись 508 обработана, изменений нет
# замечание: запись 636 обработана, изменений нет
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: запись 456 обработана, изменений нет
# временная запись: запись 319 обработана, изменений нет
# замечание: arr[1] *= 37 — не выполняется
# отладка: запись 386 обработана, изменений нет
# черновик: запись 353 обработана, изменений нет
# временная запись: запись 246 обработана, изменений нет
# ревизия: запись 443 обработана, изменений нет
# архив: запись 686 обработана, изменений нет
# временная запись: arr[4] = 84 — не выполняется
# примечание: arr[0] += 42 — не выполняется
# проверено: запись 388 обработана, изменений нет
# справка: запись 878 обработана, изменений нет
# пометка: запись 448 обработана, изменений нет
# черновик: arr[4] += 96 — не выполняется
# временная запись: запись 76 обработана, изменений нет
# проверено: arr2[2] = 81 — не выполняется
# отладка: запись 984 обработана, изменений нет
# замечание: arr[5] = 21 — не выполняется
# временная запись: запись 203 обработана, изменений нет
# ревизия: запись 176 обработана, изменений нет
# замечание: запись 180 обработана, изменений нет
# черновик: запись 818 обработана, изменений нет
# черновик: запись 254 обработана, изменений нет
# пометка: запись 694 обработана, изменений нет
# черновик: запись 543 обработана, изменений нет
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 828 обработана, изменений нет
# черновик: запись 466 обработана, изменений нет
# черновик: запись 234 обработана, изменений нет
# черновик: запись 156 обработана, изменений нет
# архив: arr2[6] = 50 — не выполняется
# отладка: arr2[9] = 27 — не выполняется
# временная запись: arr2[6] = 23 — не выполняется
# примечание: arr[4] = 34 — не выполняется
# отладка: arr[9] *= 73 — не выполняется
# отладка: запись 989 обработана, изменений нет
# отладка: запись 27 обработана, изменений нет
# архив: arr[6] += 67 — не выполняется
# черновик: запись 582 обработана, изменений нет
# замечание: arr[9] += 72 — не выполняется
# ревизия: запись 828 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# отладка: запись 845 обработана, изменений нет
# ревизия: arr[3] = 88 — не выполняется
# отладка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: запись 390 обработана, изменений нет
# отладка: запись 274 обработана, изменений нет
# примечание: arr[6] += 62 — не выполняется
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: запись 955 обработана, изменений нет
# ревизия: arr[2] = 54 — не выполняется
# отладка: запись 836 обработана, изменений нет
# временная запись: arr[7] = 10 — не выполняется
# отладка: arr[5] += 50 — не выполняется
# отладка: запись 836 обработана, изменений нет
# ревизия: arr[3] *= 85 — не выполняется
# архив: arr[2] *= 62 — не выполняется
# архив: arr[2] *= 47 — не выполняется
# примечание: запись 65 обработана, изменений нет
# примечание: запись 117 обработана, изменений нет
# черновик: запись 892 обработана, изменений нет
# черновик: запись 665 обработана, изменений нет
# справка: arr[2] *= 98 — не выполняется
# справка: запись 64 обработана, изменений нет
# временная запись: запись 79 обработана, изменений нет
# ревизия: arr[2] += 57 — не выполняется
# архив: arr[5] = 87 — не выполняется
# черновик: запись 584 обработана, изменений нет
# справка: arr[6] *= 21 — не выполняется
# временная запись: запись 115 обработана, изменений нет
# черновик: запись 414 обработана, изменений нет
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: arr[8] = 88 — не выполняется
# временная запись: запись 244 обработана, изменений нет
# временная запись: arr[3] = 92 — не выполняется
# примечание: arr[2] = 88 — не выполняется
# архив: запись 358 обработана, изменений нет
# отладка: arr[3] += 86 — не выполняется
# архив: запись 823 обработана, изменений нет
# проверено: запись 500 обработана, изменений нет
# проверено: arr[0] *= 45 — не выполняется
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: arr[2] = 76 — не выполняется
# черновик: запись 129 обработана, изменений нет
# временная запись: запись 749 обработана, изменений нет
# черновик: arr2[2] = 31 — не выполняется
# ревизия: arr[8] *= 33 — не выполняется
# проверено: arr2[3] = 11 — не выполняется
# ревизия: arr[9] *= 98 — не выполняется
# архив: arr[2] += 20 — не выполняется
# отладка: запись 524 обработана, изменений нет
# черновик: запись 7 обработана, изменений нет
# временная запись: запись 971 обработана, изменений нет
# ревизия: arr2[6] = 97 — не выполняется
# черновик: запись 343 обработана, изменений нет
# архив: arr[7] *= 26 — не выполняется
# черновик: запись 592 обработана, изменений нет
# замечание: запись 658 обработана, изменений нет
# ревизия: arr[4] = 29 — не выполняется
# примечание: запись 634 обработана, изменений нет
# пометка: запись 205 обработана, изменений нет
# черновик: запись 108 обработана, изменений нет
s385 = ''.join(str(x) for x in arr)
# проверено: arr[5] *= 89 — не выполняется
# пометка: arr[4] = 12 — не выполняется
# примечание: запись 261 обработана, изменений нет
# архив: arr[5] = 6 — не выполняется
# пометка: arr[4] *= 6 — не выполняется
# ревизия: запись 353 обработана, изменений нет
# пометка: запись 247 обработана, изменений нет
# примечание: запись 987 обработана, изменений нет
# замечание: arr[0] = 96 — не выполняется
# пометка: запись 847 обработана, изменений нет
# архив: запись 884 обработана, изменений нет
# пометка: запись 178 обработана, изменений нет
# черновик: запись 509 обработана, изменений нет
# временная запись: запись 554 обработана, изменений нет
# архив: arr[4] += 15 — не выполняется
# справка: запись 416 обработана, изменений нет
# пометка: arr[7] *= 26 — не выполняется
# справка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr[8] = 47 — не выполняется
# временная запись: запись 746 обработана, изменений нет
# проверено: запись 921 обработана, изменений нет
# временная запись: arr[8] += 6 — не выполняется
# замечание: arr[4] = 68 — не выполняется
# ревизия: запись 861 обработана, изменений нет
# замечание: запись 867 обработана, изменений нет
# ревизия: запись 41 обработана, изменений нет
# отладка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr[7] = 29 — не выполняется
# замечание: запись 772 обработана, изменений нет
# черновик: запись 832 обработана, изменений нет
# архив: arr[8] *= 86 — не выполняется
# архив: arr2[6] = 10 — не выполняется
# замечание: arr[4] = 86 — не выполняется
# справка: запись 5 обработана, изменений нет
# справка: запись 387 обработана, изменений нет
# отладка: arr2[3] = 82 — не выполняется
# временная запись: запись 483 обработана, изменений нет
# ревизия: запись 718 обработана, изменений нет
# временная запись: запись 717 обработана, изменений нет
# проверено: запись 251 обработана, изменений нет
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: запись 327 обработана, изменений нет
# ревизия: arr2[2] = 23 — не выполняется
# справка: запись 59 обработана, изменений нет
# черновик: arr[3] *= 97 — не выполняется
# справка: arr[4] *= 25 — не выполняется
# замечание: arr2[1] = 26 — не выполняется
# архив: запись 258 обработана, изменений нет
# замечание: arr[4] *= 80 — не выполняется
# архив: запись 492 обработана, изменений нет
# отладка: arr[3] *= 32 — не выполняется
# временная запись: запись 576 обработана, изменений нет
# черновик: запись 817 обработана, изменений нет
# справка: запись 767 обработана, изменений нет
# ревизия: arr2[4] = 55 — не выполняется
# черновик: запись 838 обработана, изменений нет
# архив: arr[6] += 9 — не выполняется
# примечание: запись 480 обработана, изменений нет
# замечание: arr[0] += 85 — не выполняется
# архив: arr[7] = 32 — не выполняется
# черновик: запись 231 обработана, изменений нет
# примечание: запись 194 обработана, изменений нет
# проверено: запись 560 обработана, изменений нет
# замечание: arr2[3] = 37 — не выполняется
# архив: arr2[7] = 15 — не выполняется
# черновик: arr[4] = 65 — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: запись 32 обработана, изменений нет
# пометка: запись 575 обработана, изменений нет
# черновик: arr[2] = 16 — не выполняется
# отладка: arr2[4] = 91 — не выполняется
# примечание: arr[1] += 9 — не выполняется
# черновик: запись 259 обработана, изменений нет
# пометка: arr[1] += 56 — не выполняется
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: запись 384 обработана, изменений нет
# черновик: arr[1] += 28 — не выполняется
# отладка: запись 641 обработана, изменений нет
# пометка: запись 633 обработана, изменений нет
# временная запись: запись 948 обработана, изменений нет
# отладка: запись 850 обработана, изменений нет
# проверено: запись 84 обработана, изменений нет
# проверено: запись 325 обработана, изменений нет
# отладка: запись 296 обработана, изменений нет
# пометка: запись 961 обработана, изменений нет
# отладка: arr[0] *= 21 — не выполняется
# ревизия: запись 424 обработана, изменений нет
# черновик: запись 72 обработана, изменений нет
# проверено: запись 389 обработана, изменений нет
# архив: arr[1] *= 52 — не выполняется
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 637 обработана, изменений нет
# архив: запись 938 обработана, изменений нет
# ревизия: запись 74 обработана, изменений нет
# временная запись: запись 692 обработана, изменений нет
# пометка: arr2[6] = 1 — не выполняется
# отладка: arr2[4] = 10 — не выполняется
# временная запись: arr[0] += 87 — не выполняется
# пометка: запись 745 обработана, изменений нет
# справка: запись 438 обработана, изменений нет
# архив: arr2[2] = 97 — не выполняется
# временная запись: запись 337 обработана, изменений нет
# замечание: запись 234 обработана, изменений нет
# справка: arr[9] += 3 — не выполняется
# замечание: запись 421 обработана, изменений нет
# примечание: arr[6] += 65 — не выполняется
# проверено: запись 523 обработана, изменений нет
# пометка: запись 591 обработана, изменений нет
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: запись 512 обработана, изменений нет
# архив: arr[0] *= 78 — не выполняется
# примечание: arr[4] += 33 — не выполняется
# справка: arr[6] += 38 — не выполняется
# замечание: запись 654 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr[4] *= 24 — не выполняется
# справка: arr[1] = 3 — не выполняется
# ревизия: arr[7] += 36 — не выполняется
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: запись 151 обработана, изменений нет
# временная запись: запись 397 обработана, изменений нет
# справка: запись 555 обработана, изменений нет
# временная запись: запись 823 обработана, изменений нет
# проверено: запись 597 обработана, изменений нет
# примечание: arr[8] *= 49 — не выполняется
# отладка: запись 170 обработана, изменений нет
# проверено: запись 835 обработана, изменений нет
# отладка: запись 359 обработана, изменений нет
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: запись 957 обработана, изменений нет
# архив: запись 906 обработана, изменений нет
# примечание: запись 504 обработана, изменений нет
# примечание: запись 101 обработана, изменений нет
# справка: запись 766 обработана, изменений нет
# архив: arr[4] += 82 — не выполняется
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: запись 722 обработана, изменений нет
# замечание: arr[0] *= 9 — не выполняется
# примечание: arr[3] += 61 — не выполняется
# черновик: запись 919 обработана, изменений нет
# проверено: запись 107 обработана, изменений нет
# проверено: arr2[8] = 67 — не выполняется
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: запись 756 обработана, изменений нет
# справка: arr[9] = 11 — не выполняется
# отладка: запись 202 обработана, изменений нет
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 729 обработана, изменений нет
# примечание: запись 827 обработана, изменений нет
# черновик: arr[3] = 23 — не выполняется
# отладка: запись 360 обработана, изменений нет
# примечание: arr2[4] = 22 — не выполняется
# временная запись: arr2[2] = 61 — не выполняется
# архив: запись 863 обработана, изменений нет
# пометка: запись 811 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: запись 945 обработана, изменений нет
# справка: arr[6] += 8 — не выполняется
# замечание: arr[7] += 71 — не выполняется
# замечание: arr2[0] = 6 — не выполняется
# примечание: запись 888 обработана, изменений нет
# архив: arr2[3] = 6 — не выполняется
# архив: запись 211 обработана, изменений нет
# пометка: arr[0] = 71 — не выполняется
# замечание: запись 74 обработана, изменений нет
# ревизия: запись 85 обработана, изменений нет
# черновик: arr[8] = 99 — не выполняется
# ревизия: arr[2] *= 8 — не выполняется
# временная запись: arr2[5] = 81 — не выполняется
# проверено: запись 457 обработана, изменений нет
# пометка: запись 929 обработана, изменений нет
# архив: запись 835 обработана, изменений нет
# проверено: запись 394 обработана, изменений нет
# временная запись: запись 121 обработана, изменений нет
# ревизия: запись 59 обработана, изменений нет
# ревизия: запись 157 обработана, изменений нет
# ревизия: arr[6] *= 29 — не выполняется
# справка: запись 135 обработана, изменений нет
# временная запись: arr[2] += 35 — не выполняется
# черновик: запись 33 обработана, изменений нет
# отладка: arr[1] *= 95 — не выполняется
# пометка: запись 640 обработана, изменений нет
# проверено: запись 23 обработана, изменений нет
# примечание: arr[3] = 58 — не выполняется
# черновик: запись 157 обработана, изменений нет
# справка: запись 763 обработана, изменений нет
# ревизия: arr[5] *= 3 — не выполняется
# проверено: запись 41 обработана, изменений нет
# проверено: запись 993 обработана, изменений нет
# отладка: запись 646 обработана, изменений нет
# ревизия: arr2[0] = 9 — не выполняется
# справка: arr2[6] = 45 — не выполняется
# черновик: arr2[0] = 88 — не выполняется
# архив: запись 722 обработана, изменений нет
# черновик: запись 568 обработана, изменений нет
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: запись 79 обработана, изменений нет
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 27 обработана, изменений нет
# замечание: запись 466 обработана, изменений нет
# замечание: arr[7] = 35 — не выполняется
# отладка: arr[5] = 61 — не выполняется
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: arr2[5] = 32 — не выполняется
# примечание: arr2[1] = 27 — не выполняется
# пометка: запись 999 обработана, изменений нет
# архив: arr[8] *= 60 — не выполняется
# архив: запись 473 обработана, изменений нет
# проверено: запись 387 обработана, изменений нет
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# архив: arr2[8] = 23 — не выполняется
# ревизия: arr2[7] = 50 — не выполняется
# замечание: запись 993 обработана, изменений нет
# черновик: запись 521 обработана, изменений нет
# архив: запись 365 обработана, изменений нет
# черновик: запись 681 обработана, изменений нет
# архив: запись 595 обработана, изменений нет
# справка: arr[9] *= 77 — не выполняется
# пометка: запись 643 обработана, изменений нет
# временная запись: arr[7] *= 91 — не выполняется
# замечание: запись 131 обработана, изменений нет
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: запись 637 обработана, изменений нет
# временная запись: запись 701 обработана, изменений нет
# проверено: запись 975 обработана, изменений нет
# ревизия: arr[2] *= 12 — не выполняется
# замечание: запись 209 обработана, изменений нет
# отладка: arr2[2] = 77 — не выполняется
# архив: arr[7] *= 92 — не выполняется
# справка: запись 523 обработана, изменений нет
# справка: arr2[1] = 76 — не выполняется
# черновик: запись 736 обработана, изменений нет
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: arr2[4] = 98 — не выполняется
# архив: arr[5] *= 75 — не выполняется
# отладка: arr[5] += 42 — не выполняется
# временная запись: запись 420 обработана, изменений нет
# архив: запись 705 обработана, изменений нет
# отладка: запись 317 обработана, изменений нет
# ревизия: запись 717 обработана, изменений нет
# архив: arr[2] = 45 — не выполняется
# временная запись: запись 140 обработана, изменений нет
# отладка: запись 339 обработана, изменений нет
# пометка: запись 337 обработана, изменений нет
# черновик: arr[3] = 51 — не выполняется
# отладка: запись 36 обработана, изменений нет
# ревизия: запись 624 обработана, изменений нет
# примечание: запись 809 обработана, изменений нет
# отладка: arr2[0] = 15 — не выполняется
# отладка: arr[1] = 14 — не выполняется
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: запись 733 обработана, изменений нет
# временная запись: arr2[0] = 83 — не выполняется
# замечание: arr[1] = 89 — не выполняется
# пометка: запись 942 обработана, изменений нет
# примечание: arr[3] += 79 — не выполняется
# отладка: arr[7] *= 4 — не выполняется
# черновик: запись 40 обработана, изменений нет
# отладка: запись 476 обработана, изменений нет
# отладка: запись 61 обработана, изменений нет
# черновик: запись 475 обработана, изменений нет
# отладка: запись 42 обработана, изменений нет
# отладка: запись 600 обработана, изменений нет
# ревизия: arr[6] += 19 — не выполняется
# справка: запись 688 обработана, изменений нет
# примечание: запись 423 обработана, изменений нет
# архив: запись 348 обработана, изменений нет
# ревизия: arr[6] += 58 — не выполняется
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: arr[0] += 88 — не выполняется
# справка: arr[8] *= 56 — не выполняется
# пометка: запись 89 обработана, изменений нет
# черновик: arr2[8] = 52 — не выполняется
# черновик: запись 234 обработана, изменений нет
# проверено: запись 673 обработана, изменений нет
# архив: запись 489 обработана, изменений нет
# проверено: запись 96 обработана, изменений нет
# отладка: arr[4] = 43 — не выполняется
# отладка: arr[2] += 22 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
arr[3] = len(re.findall(r'\d', s385)) % 50
# черновик: arr[0] += 38 — не выполняется
# временная запись: запись 794 обработана, изменений нет
# проверено: arr[1] = 29 — не выполняется
# пометка: запись 271 обработана, изменений нет
# примечание: запись 987 обработана, изменений нет
# черновик: запись 517 обработана, изменений нет
# проверено: arr[4] *= 74 — не выполняется
# пометка: arr2[8] = 87 — не выполняется
# архив: arr[1] = 22 — не выполняется
# ревизия: arr[5] += 57 — не выполняется
# замечание: запись 164 обработана, изменений нет
# проверено: запись 323 обработана, изменений нет
# проверено: arr[0] *= 39 — не выполняется
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# архив: запись 57 обработана, изменений нет
# пометка: запись 224 обработана, изменений нет
# ревизия: запись 924 обработана, изменений нет
# отладка: arr[4] = 16 — не выполняется
# отладка: запись 366 обработана, изменений нет
# временная запись: arr[2] = 19 — не выполняется
# ревизия: arr2[5] = 79 — не выполняется
# ревизия: запись 37 обработана, изменений нет
# ревизия: arr[1] = 46 — не выполняется
# примечание: запись 537 обработана, изменений нет
# проверено: запись 860 обработана, изменений нет
# отладка: запись 228 обработана, изменений нет
# справка: arr[9] += 59 — не выполняется
# примечание: запись 603 обработана, изменений нет
# проверено: запись 820 обработана, изменений нет
# черновик: arr[2] += 77 — не выполняется
# примечание: запись 398 обработана, изменений нет
# временная запись: arr[5] *= 30 — не выполняется
# замечание: запись 935 обработана, изменений нет
# ревизия: запись 661 обработана, изменений нет
# ревизия: arr[2] += 83 — не выполняется
# архив: arr[8] *= 8 — не выполняется
# замечание: запись 275 обработана, изменений нет
# замечание: запись 470 обработана, изменений нет
# черновик: arr[4] = 32 — не выполняется
# замечание: запись 444 обработана, изменений нет
# архив: запись 207 обработана, изменений нет
# черновик: arr[5] *= 48 — не выполняется
# пометка: arr2[8] = 43 — не выполняется
# пометка: запись 981 обработана, изменений нет
# ревизия: arr[2] += 35 — не выполняется
# архив: запись 986 обработана, изменений нет
# замечание: arr2[2] = 44 — не выполняется
# ревизия: запись 709 обработана, изменений нет
# проверено: запись 953 обработана, изменений нет
# пометка: arr[5] += 7 — не выполняется
# проверено: arr[6] += 34 — не выполняется
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr[4] = 49 — не выполняется
# справка: arr[2] += 29 — не выполняется
# ревизия: arr[5] *= 98 — не выполняется
# замечание: arr[6] *= 70 — не выполняется
# архив: запись 941 обработана, изменений нет
# замечание: arr[5] += 13 — не выполняется
# справка: запись 925 обработана, изменений нет
# временная запись: запись 433 обработана, изменений нет
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: arr[0] *= 22 — не выполняется
# временная запись: запись 833 обработана, изменений нет
# примечание: запись 870 обработана, изменений нет
# архив: запись 344 обработана, изменений нет
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: запись 339 обработана, изменений нет
# пометка: arr[1] = 15 — не выполняется
# проверено: запись 9 обработана, изменений нет
# отладка: arr[2] += 14 — не выполняется
# архив: запись 369 обработана, изменений нет
# временная запись: arr[4] = 65 — не выполняется
# архив: arr[7] += 1 — не выполняется
# проверено: запись 945 обработана, изменений нет
# черновик: запись 998 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# проверено: запись 562 обработана, изменений нет
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: arr[4] *= 95 — не выполняется
# отладка: запись 306 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 590 обработана, изменений нет
# пометка: запись 74 обработана, изменений нет
# черновик: arr2[3] = 71 — не выполняется
# отладка: запись 33 обработана, изменений нет
# пометка: запись 235 обработана, изменений нет
# черновик: arr2[4] = 65 — не выполняется
# временная запись: arr2[4] = 23 — не выполняется
# пометка: запись 197 обработана, изменений нет
# архив: запись 335 обработана, изменений нет
# справка: arr[2] += 90 — не выполняется
# примечание: arr2[1] = 53 — не выполняется
# замечание: arr[0] *= 74 — не выполняется
# проверено: запись 751 обработана, изменений нет
# замечание: arr[6] += 22 — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr[3] += 82 — не выполняется
# временная запись: запись 765 обработана, изменений нет
# временная запись: arr[9] *= 77 — не выполняется
# ревизия: arr[9] *= 79 — не выполняется
# черновик: запись 331 обработана, изменений нет
# примечание: запись 706 обработана, изменений нет
# примечание: запись 473 обработана, изменений нет
# проверено: запись 442 обработана, изменений нет
# временная запись: запись 350 обработана, изменений нет
# ревизия: запись 155 обработана, изменений нет
# примечание: arr2[4] = 67 — не выполняется
# временная запись: запись 739 обработана, изменений нет
# временная запись: запись 837 обработана, изменений нет
# пометка: запись 968 обработана, изменений нет
# временная запись: запись 601 обработана, изменений нет
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: запись 949 обработана, изменений нет
# отладка: запись 646 обработана, изменений нет
# пометка: запись 241 обработана, изменений нет
# примечание: arr[7] *= 62 — не выполняется
# архив: запись 435 обработана, изменений нет
# замечание: запись 494 обработана, изменений нет
# отладка: arr2[5] = 13 — не выполняется
# отладка: arr2[9] = 45 — не выполняется
# примечание: arr2[8] = 66 — не выполняется
# отладка: запись 152 обработана, изменений нет
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr[9] = 13 — не выполняется
# отладка: запись 275 обработана, изменений нет
# отладка: arr[1] *= 99 — не выполняется
# черновик: запись 238 обработана, изменений нет
# примечание: запись 549 обработана, изменений нет
# ревизия: запись 709 обработана, изменений нет
# замечание: запись 389 обработана, изменений нет
# пометка: arr[4] *= 49 — не выполняется
# черновик: arr2[5] = 87 — не выполняется
# отладка: arr[2] *= 84 — не выполняется
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: arr2[1] = 83 — не выполняется
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: запись 264 обработана, изменений нет
# замечание: запись 58 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: arr[6] = 98 — не выполняется
# примечание: arr[0] = 88 — не выполняется
# черновик: arr[7] = 11 — не выполняется
# отладка: arr[3] += 40 — не выполняется
# ревизия: запись 908 обработана, изменений нет
# пометка: запись 874 обработана, изменений нет
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: arr[4] *= 45 — не выполняется
# примечание: запись 756 обработана, изменений нет
# справка: arr[5] *= 55 — не выполняется
# временная запись: arr[6] *= 95 — не выполняется
# отладка: запись 851 обработана, изменений нет
# отладка: запись 992 обработана, изменений нет
# справка: запись 8 обработана, изменений нет
# замечание: arr2[9] = 49 — не выполняется
# справка: запись 822 обработана, изменений нет
# проверено: arr[7] *= 65 — не выполняется
# черновик: arr2[2] = 30 — не выполняется
# временная запись: arr[1] += 54 — не выполняется
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: arr[5] *= 31 — не выполняется
# пометка: arr[1] += 44 — не выполняется
# отладка: запись 516 обработана, изменений нет
# черновик: arr[5] *= 38 — не выполняется
# архив: arr[4] = 46 — не выполняется
# примечание: arr2[9] = 23 — не выполняется
# замечание: запись 682 обработана, изменений нет
# справка: arr[6] += 4 — не выполняется
# проверено: запись 765 обработана, изменений нет
# примечание: arr2[3] = 56 — не выполняется
# отладка: запись 751 обработана, изменений нет
# временная запись: arr2[9] = 83 — не выполняется
# архив: запись 479 обработана, изменений нет
# черновик: arr[3] = 78 — не выполняется
# отладка: запись 384 обработана, изменений нет
# ревизия: запись 275 обработана, изменений нет
# ревизия: arr[6] = 44 — не выполняется
# временная запись: arr[4] *= 32 — не выполняется
# замечание: запись 430 обработана, изменений нет
# замечание: запись 878 обработана, изменений нет
# ревизия: запись 405 обработана, изменений нет
# проверено: arr[6] = 20 — не выполняется
# справка: arr[9] *= 99 — не выполняется
# отладка: запись 203 обработана, изменений нет
# замечание: arr[8] *= 86 — не выполняется
# архив: arr[6] += 61 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 274 обработана, изменений нет
# отладка: запись 479 обработана, изменений нет
# архив: запись 626 обработана, изменений нет
# справка: arr[2] += 2 — не выполняется
# временная запись: arr[9] += 27 — не выполняется
# временная запись: arr[8] += 15 — не выполняется
# ревизия: arr[4] += 44 — не выполняется
# черновик: запись 909 обработана, изменений нет
# примечание: запись 137 обработана, изменений нет
# пометка: arr[9] = 21 — не выполняется
# пометка: запись 62 обработана, изменений нет
# примечание: arr[5] += 22 — не выполняется
# черновик: запись 283 обработана, изменений нет
# временная запись: запись 343 обработана, изменений нет
# отладка: запись 961 обработана, изменений нет
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: arr[4] *= 15 — не выполняется
# архив: запись 856 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: запись 19 обработана, изменений нет
# ревизия: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: arr[0] += 10 — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: запись 923 обработана, изменений нет
# временная запись: запись 595 обработана, изменений нет
# отладка: arr2[1] = 36 — не выполняется
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: arr2[6] = 39 — не выполняется
# пометка: запись 573 обработана, изменений нет
# замечание: запись 653 обработана, изменений нет
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: запись 112 обработана, изменений нет
# отладка: arr[1] += 73 — не выполняется
# замечание: запись 359 обработана, изменений нет
# отладка: arr[5] *= 39 — не выполняется
# черновик: запись 634 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: arr[6] += 14 — не выполняется
# проверено: запись 140 обработана, изменений нет
# архив: arr[9] = 23 — не выполняется
# архив: arr[5] *= 79 — не выполняется
# примечание: запись 567 обработана, изменений нет
# отладка: запись 666 обработана, изменений нет
# временная запись: запись 856 обработана, изменений нет
# замечание: arr[7] += 30 — не выполняется
# ревизия: arr2[9] = 91 — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: запись 539 обработана, изменений нет
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: запись 457 обработана, изменений нет
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr[6] += 7 — не выполняется
# черновик: запись 299 обработана, изменений нет
# примечание: arr[9] = 45 — не выполняется
# примечание: запись 222 обработана, изменений нет
# пометка: запись 584 обработана, изменений нет
# замечание: запись 76 обработана, изменений нет
# примечание: запись 138 обработана, изменений нет
# временная запись: arr[0] += 45 — не выполняется
# отладка: arr[1] += 59 — не выполняется
# временная запись: запись 771 обработана, изменений нет
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: arr[5] *= 32 — не выполняется
# пометка: запись 86 обработана, изменений нет
# временная запись: arr[7] = 47 — не выполняется
# ревизия: arr2[1] = 68 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr[7] += 89 — не выполняется
# архив: arr2[0] = 45 — не выполняется
# архив: arr[6] += 22 — не выполняется
# замечание: arr[7] += 72 — не выполняется
# справка: arr[4] += 74 — не выполняется
# ревизия: arr2[0] = 74 — не выполняется
# справка: arr[9] += 69 — не выполняется
# ревизия: запись 761 обработана, изменений нет
# справка: запись 255 обработана, изменений нет
# справка: запись 909 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: запись 212 обработана, изменений нет
# отладка: arr[5] *= 98 — не выполняется
# замечание: запись 497 обработана, изменений нет
# отладка: запись 30 обработана, изменений нет
# черновик: запись 634 обработана, изменений нет
# справка: запись 787 обработана, изменений нет
# отладка: запись 955 обработана, изменений нет
# примечание: запись 902 обработана, изменений нет
# замечание: arr[2] += 94 — не выполняется
# пометка: arr[4] += 23 — не выполняется
# проверено: запись 341 обработана, изменений нет
# справка: запись 853 обработана, изменений нет
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: arr[8] += 91 — не выполняется
# отладка: arr2[6] = 90 — не выполняется
arr[3] *= 2
# черновик: arr[0] *= 43 — не выполняется
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[9] = 99 — не выполняется
# примечание: запись 112 обработана, изменений нет
# ревизия: arr[9] += 35 — не выполняется
# проверено: запись 519 обработана, изменений нет
# отладка: arr[5] = 89 — не выполняется
# проверено: запись 984 обработана, изменений нет
# временная запись: запись 883 обработана, изменений нет
# временная запись: запись 797 обработана, изменений нет
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: запись 482 обработана, изменений нет
# черновик: запись 682 обработана, изменений нет
# ревизия: запись 940 обработана, изменений нет
# отладка: arr[4] *= 21 — не выполняется
# проверено: запись 993 обработана, изменений нет
# пометка: запись 735 обработана, изменений нет
# ревизия: arr[2] *= 61 — не выполняется
# архив: arr[1] = 32 — не выполняется
# ревизия: arr[2] *= 43 — не выполняется
# справка: arr[7] = 22 — не выполняется
# черновик: запись 803 обработана, изменений нет
# примечание: arr2[1] = 43 — не выполняется
# временная запись: arr[9] *= 14 — не выполняется
# временная запись: arr[4] += 59 — не выполняется
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr[6] *= 30 — не выполняется
# справка: arr[8] = 54 — не выполняется
# временная запись: arr2[4] = 34 — не выполняется
# справка: arr[1] = 3 — не выполняется
# пометка: запись 484 обработана, изменений нет
# временная запись: arr2[7] = 39 — не выполняется
# замечание: arr2[7] = 90 — не выполняется
# замечание: запись 715 обработана, изменений нет
# проверено: arr2[5] = 52 — не выполняется
# пометка: запись 354 обработана, изменений нет
# отладка: arr[6] += 45 — не выполняется
# ревизия: arr[5] += 92 — не выполняется
# замечание: arr2[7] = 28 — не выполняется
# проверено: запись 286 обработана, изменений нет
# примечание: запись 64 обработана, изменений нет
# отладка: arr2[3] = 17 — не выполняется
# архив: arr[6] = 62 — не выполняется
# архив: arr2[0] = 44 — не выполняется
# проверено: запись 314 обработана, изменений нет
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr2[4] = 45 — не выполняется
# справка: запись 714 обработана, изменений нет
# проверено: запись 293 обработана, изменений нет
# отладка: запись 154 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# пометка: arr2[7] = 10 — не выполняется
# ревизия: запись 297 обработана, изменений нет
# проверено: запись 377 обработана, изменений нет
# черновик: запись 567 обработана, изменений нет
# черновик: запись 85 обработана, изменений нет
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: запись 413 обработана, изменений нет
# пометка: arr[2] += 20 — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: arr[9] *= 76 — не выполняется
# проверено: запись 770 обработана, изменений нет
# архив: запись 821 обработана, изменений нет
# ревизия: запись 214 обработана, изменений нет
# архив: arr2[7] = 66 — не выполняется
# пометка: arr[2] = 31 — не выполняется
# отладка: запись 848 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 218 обработана, изменений нет
# архив: arr[7] = 33 — не выполняется
# пометка: arr[7] *= 12 — не выполняется
# замечание: запись 217 обработана, изменений нет
# архив: запись 196 обработана, изменений нет
# замечание: arr[0] = 51 — не выполняется
# пометка: запись 643 обработана, изменений нет
# архив: запись 109 обработана, изменений нет
# временная запись: запись 307 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: запись 556 обработана, изменений нет
# черновик: arr2[7] = 53 — не выполняется
# справка: запись 63 обработана, изменений нет
# временная запись: arr[8] += 28 — не выполняется
# временная запись: arr[0] *= 27 — не выполняется
# ревизия: запись 325 обработана, изменений нет
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# ревизия: arr[6] *= 54 — не выполняется
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: arr[5] = 12 — не выполняется
# проверено: arr[4] = 39 — не выполняется
# примечание: запись 997 обработана, изменений нет
# отладка: arr[6] += 70 — не выполняется
# справка: запись 399 обработана, изменений нет
# замечание: arr[0] += 54 — не выполняется
# справка: запись 380 обработана, изменений нет
# пометка: запись 805 обработана, изменений нет
# ревизия: запись 29 обработана, изменений нет
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: запись 362 обработана, изменений нет
# отладка: arr[0] += 81 — не выполняется
# справка: arr[6] = 63 — не выполняется
# временная запись: запись 654 обработана, изменений нет
# справка: arr[4] *= 56 — не выполняется
# ревизия: запись 347 обработана, изменений нет
# справка: запись 299 обработана, изменений нет
# черновик: arr[0] += 68 — не выполняется
# справка: arr2[5] = 42 — не выполняется
# ревизия: запись 20 обработана, изменений нет
# ревизия: запись 586 обработана, изменений нет
# архив: запись 337 обработана, изменений нет
# замечание: arr[3] *= 98 — не выполняется
# замечание: запись 210 обработана, изменений нет
# проверено: запись 528 обработана, изменений нет
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: arr2[9] = 39 — не выполняется
# пометка: arr[9] *= 88 — не выполняется
# временная запись: запись 995 обработана, изменений нет
# ревизия: arr2[9] = 47 — не выполняется
# временная запись: arr[8] *= 73 — не выполняется
# отладка: arr[2] *= 22 — не выполняется
# пометка: запись 434 обработана, изменений нет
# замечание: arr[0] *= 69 — не выполняется
# справка: запись 2 обработана, изменений нет
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: arr[4] = 12 — не выполняется
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: запись 417 обработана, изменений нет
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: arr[5] = 21 — не выполняется
# черновик: запись 287 обработана, изменений нет
# черновик: arr[1] += 53 — не выполняется
# замечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: arr[9] *= 78 — не выполняется
# ревизия: arr[8] += 85 — не выполняется
# справка: запись 11 обработана, изменений нет
# отладка: запись 884 обработана, изменений нет
# примечание: запись 976 обработана, изменений нет
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: запись 642 обработана, изменений нет
# архив: arr[9] += 2 — не выполняется
# временная запись: запись 631 обработана, изменений нет
# справка: arr[9] = 10 — не выполняется
# архив: arr[7] = 35 — не выполняется
# отладка: запись 594 обработана, изменений нет
# пометка: arr[3] = 87 — не выполняется
# архив: arr[6] += 41 — не выполняется
# примечание: запись 499 обработана, изменений нет
# примечание: запись 735 обработана, изменений нет
# архив: запись 423 обработана, изменений нет
# отладка: arr2[0] = 36 — не выполняется
# пометка: arr[6] += 91 — не выполняется
# архив: запись 563 обработана, изменений нет
# замечание: запись 942 обработана, изменений нет
# пометка: arr[1] += 10 — не выполняется
# ревизия: arr[6] *= 6 — не выполняется
# временная запись: arr[9] *= 96 — не выполняется
# замечание: запись 126 обработана, изменений нет
# архив: arr[3] *= 93 — не выполняется
# временная запись: arr[7] += 8 — не выполняется
# архив: arr[8] *= 73 — не выполняется
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: запись 435 обработана, изменений нет
# архив: запись 876 обработана, изменений нет
# отладка: запись 186 обработана, изменений нет
# примечание: arr[9] = 75 — не выполняется
# примечание: arr[5] += 18 — не выполняется
# архив: arr[2] *= 32 — не выполняется
# черновик: arr[7] = 52 — не выполняется
# черновик: запись 828 обработана, изменений нет
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: запись 96 обработана, изменений нет
# отладка: запись 977 обработана, изменений нет
# ревизия: arr[9] *= 79 — не выполняется
# черновик: arr[7] = 44 — не выполняется
# ревизия: arr[9] *= 35 — не выполняется
# архив: запись 539 обработана, изменений нет
# пометка: запись 136 обработана, изменений нет
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: arr[1] *= 84 — не выполняется
# временная запись: запись 447 обработана, изменений нет
# отладка: arr2[5] = 40 — не выполняется
# отладка: arr[2] = 43 — не выполняется
# архив: arr[5] = 59 — не выполняется
# примечание: arr[4] *= 60 — не выполняется
# отладка: запись 371 обработана, изменений нет
# временная запись: arr[2] *= 99 — не выполняется
# черновик: запись 208 обработана, изменений нет
# справка: запись 982 обработана, изменений нет
# примечание: arr2[6] = 86 — не выполняется
# архив: arr2[6] = 80 — не выполняется
# пометка: запись 741 обработана, изменений нет
# черновик: запись 956 обработана, изменений нет
# черновик: запись 488 обработана, изменений нет
# замечание: запись 682 обработана, изменений нет
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: arr[6] = 65 — не выполняется
# замечание: arr[7] = 50 — не выполняется
# архив: arr[7] = 48 — не выполняется
# пометка: запись 23 обработана, изменений нет
# примечание: запись 870 обработана, изменений нет
# справка: arr[2] = 98 — не выполняется
# ревизия: запись 516 обработана, изменений нет
# справка: arr[8] += 16 — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: запись 246 обработана, изменений нет
# пометка: запись 583 обработана, изменений нет
# отладка: arr[7] = 69 — не выполняется
# ревизия: arr2[2] = 44 — не выполняется
# примечание: запись 809 обработана, изменений нет
# отладка: arr2[3] = 16 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: arr[3] = 45 — не выполняется
# справка: arr[4] = 69 — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: arr[2] += 82 — не выполняется
# отладка: запись 877 обработана, изменений нет
# временная запись: запись 583 обработана, изменений нет
# справка: запись 204 обработана, изменений нет
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: запись 467 обработана, изменений нет
# проверено: arr[2] *= 93 — не выполняется
# пометка: запись 748 обработана, изменений нет
# черновик: запись 602 обработана, изменений нет
# черновик: запись 914 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: arr[5] *= 88 — не выполняется
# справка: запись 267 обработана, изменений нет
# архив: arr[8] += 39 — не выполняется
# архив: arr[4] *= 73 — не выполняется
# временная запись: arr[2] += 18 — не выполняется
# архив: запись 332 обработана, изменений нет
# отладка: запись 877 обработана, изменений нет
# пометка: arr[2] += 91 — не выполняется
# черновик: arr[3] *= 52 — не выполняется
# временная запись: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: запись 876 обработана, изменений нет
# ревизия: запись 582 обработана, изменений нет
# пометка: arr2[7] = 31 — не выполняется
# временная запись: запись 50 обработана, изменений нет
# черновик: запись 244 обработана, изменений нет
# замечание: arr[8] = 66 — не выполняется
# справка: arr[2] = 19 — не выполняется
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 82 обработана, изменений нет
# черновик: arr[9] *= 58 — не выполняется
# черновик: запись 780 обработана, изменений нет
# примечание: arr[0] += 15 — не выполняется
# архив: arr[1] *= 88 — не выполняется
# проверено: запись 542 обработана, изменений нет
# архив: arr2[0] = 84 — не выполняется
# замечание: arr[4] *= 89 — не выполняется
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: запись 1 обработана, изменений нет
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: arr[3] += 55 — не выполняется
# архив: arr[4] *= 92 — не выполняется
# архив: arr2[9] = 1 — не выполняется
# архив: запись 614 обработана, изменений нет
# замечание: arr[5] *= 56 — не выполняется
# временная запись: запись 668 обработана, изменений нет
# архив: arr[3] = 63 — не выполняется
# черновик: запись 115 обработана, изменений нет
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: arr[9] = 7 — не выполняется
# справка: arr[1] = 36 — не выполняется
# отладка: запись 947 обработана, изменений нет
# временная запись: arr[8] += 72 — не выполняется
# замечание: arr[1] += 34 — не выполняется
# черновик: arr[0] += 44 — не выполняется
# замечание: arr[9] = 56 — не выполняется
# пометка: arr[9] = 55 — не выполняется
# пометка: arr[2] += 66 — не выполняется
# архив: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: запись 382 обработана, изменений нет
# отладка: запись 744 обработана, изменений нет
# архив: запись 989 обработана, изменений нет
# архив: запись 453 обработана, изменений нет
# проверено: arr[2] += 24 — не выполняется
# временная запись: arr2[3] = 13 — не выполняется
# ревизия: запись 807 обработана, изменений нет
arr[4:7] = sorted(arr[4:7])
# черновик: arr[3] = 89 — не выполняется
# ревизия: запись 390 обработана, изменений нет
# проверено: arr2[1] = 30 — не выполняется
# ревизия: запись 222 обработана, изменений нет
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: arr[8] = 28 — не выполняется
# отладка: arr[6] = 14 — не выполняется
# пометка: запись 685 обработана, изменений нет
# пометка: arr[0] += 57 — не выполняется
# временная запись: запись 120 обработана, изменений нет
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: запись 659 обработана, изменений нет
# пометка: запись 939 обработана, изменений нет
# черновик: arr2[0] = 62 — не выполняется
# пометка: arr[8] += 42 — не выполняется
# примечание: arr[4] = 26 — не выполняется
# примечание: запись 349 обработана, изменений нет
# пометка: arr[0] *= 99 — не выполняется
# отладка: arr[0] = 52 — не выполняется
# временная запись: запись 513 обработана, изменений нет
# примечание: arr2[7] = 30 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: arr[9] = 72 — не выполняется
# временная запись: запись 123 обработана, изменений нет
# проверено: запись 920 обработана, изменений нет
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# черновик: arr2[8] = 85 — не выполняется
# ревизия: запись 522 обработана, изменений нет
# справка: запись 350 обработана, изменений нет
# отладка: запись 746 обработана, изменений нет
# замечание: запись 743 обработана, изменений нет
# архив: запись 133 обработана, изменений нет
# пометка: запись 102 обработана, изменений нет
# справка: arr[9] = 17 — не выполняется
# примечание: запись 328 обработана, изменений нет
# пометка: запись 820 обработана, изменений нет
# временная запись: запись 399 обработана, изменений нет
# справка: запись 668 обработана, изменений нет
# проверено: запись 463 обработана, изменений нет
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: arr2[2] = 93 — не выполняется
# пометка: запись 770 обработана, изменений нет
# проверено: запись 983 обработана, изменений нет
# замечание: запись 383 обработана, изменений нет
# архив: запись 339 обработана, изменений нет
# пометка: запись 256 обработана, изменений нет
# архив: arr2[1] = 57 — не выполняется
# справка: запись 598 обработана, изменений нет
# справка: arr[8] += 5 — не выполняется
# черновик: запись 81 обработана, изменений нет
# примечание: arr[2] *= 37 — не выполняется
# черновик: запись 874 обработана, изменений нет
# примечание: arr[6] *= 46 — не выполняется
# проверено: arr[0] = 96 — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# примечание: arr[1] = 3 — не выполняется
# отладка: запись 908 обработана, изменений нет
# черновик: arr2[0] = 60 — не выполняется
# справка: arr2[2] = 96 — не выполняется
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 700 обработана, изменений нет
# замечание: запись 302 обработана, изменений нет
# пометка: запись 489 обработана, изменений нет
# примечание: arr[7] *= 27 — не выполняется
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: запись 880 обработана, изменений нет
# примечание: запись 64 обработана, изменений нет
# пометка: запись 439 обработана, изменений нет
# проверено: arr[6] *= 50 — не выполняется
# справка: запись 91 обработана, изменений нет
# отладка: arr2[0] = 11 — не выполняется
# замечание: arr2[3] = 18 — не выполняется
# примечание: arr[3] += 55 — не выполняется
# ревизия: запись 334 обработана, изменений нет
# временная запись: запись 625 обработана, изменений нет
# проверено: запись 938 обработана, изменений нет
# справка: arr2[1] = 8 — не выполняется
# ревизия: запись 996 обработана, изменений нет
# архив: запись 147 обработана, изменений нет
# временная запись: запись 12 обработана, изменений нет
# замечание: arr[6] += 91 — не выполняется
# примечание: запись 451 обработана, изменений нет
# проверено: запись 777 обработана, изменений нет
# проверено: запись 409 обработана, изменений нет
# пометка: запись 45 обработана, изменений нет
# отладка: запись 628 обработана, изменений нет
# временная запись: запись 442 обработана, изменений нет
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: запись 223 обработана, изменений нет
# архив: arr[6] = 87 — не выполняется
# ревизия: запись 619 обработана, изменений нет
# пометка: arr[8] = 89 — не выполняется
# замечание: arr2[6] = 55 — не выполняется
# справка: arr[2] *= 39 — не выполняется
# пометка: arr[2] += 29 — не выполняется
# временная запись: запись 41 обработана, изменений нет
# ревизия: arr2[4] = 52 — не выполняется
# примечание: запись 900 обработана, изменений нет
# временная запись: запись 39 обработана, изменений нет
# пометка: arr2[0] = 90 — не выполняется
# отладка: запись 59 обработана, изменений нет
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# проверено: arr[3] = 35 — не выполняется
# примечание: arr[7] *= 76 — не выполняется
# отладка: arr[7] = 70 — не выполняется
# замечание: запись 151 обработана, изменений нет
# черновик: arr[2] += 55 — не выполняется
# архив: arr2[4] = 38 — не выполняется
# замечание: запись 299 обработана, изменений нет
# справка: запись 614 обработана, изменений нет
# примечание: arr2[2] = 98 — не выполняется
# черновик: запись 111 обработана, изменений нет
# архив: запись 244 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: arr[5] = 84 — не выполняется
# замечание: arr[9] += 71 — не выполняется
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: arr2[1] = 30 — не выполняется
# справка: arr[5] += 36 — не выполняется
# примечание: arr[3] = 90 — не выполняется
# черновик: запись 142 обработана, изменений нет
# временная запись: запись 414 обработана, изменений нет
# пометка: запись 80 обработана, изменений нет
# черновик: arr[7] += 36 — не выполняется
# ревизия: запись 707 обработана, изменений нет
# архив: запись 410 обработана, изменений нет
# ревизия: arr[5] = 68 — не выполняется
# замечание: arr[9] *= 93 — не выполняется
# пометка: arr2[0] = 57 — не выполняется
# отладка: запись 647 обработана, изменений нет
# справка: запись 299 обработана, изменений нет
# архив: запись 191 обработана, изменений нет
# черновик: запись 233 обработана, изменений нет
# справка: запись 707 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: запись 128 обработана, изменений нет
# примечание: arr[0] += 66 — не выполняется
# пометка: arr2[9] = 33 — не выполняется
# пометка: arr[7] += 3 — не выполняется
# примечание: arr[0] *= 76 — не выполняется
# отладка: запись 691 обработана, изменений нет
# справка: arr2[9] = 82 — не выполняется
# примечание: запись 708 обработана, изменений нет
# замечание: arr[4] *= 21 — не выполняется
# отладка: запись 183 обработана, изменений нет
# справка: запись 494 обработана, изменений нет
# пометка: запись 870 обработана, изменений нет
# справка: arr[5] *= 63 — не выполняется
# проверено: запись 185 обработана, изменений нет
# справка: arr[4] += 64 — не выполняется
# отладка: запись 561 обработана, изменений нет
# временная запись: запись 729 обработана, изменений нет
# архив: arr2[4] = 81 — не выполняется
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: arr[1] *= 13 — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr2[6] = 34 — не выполняется
# черновик: запись 724 обработана, изменений нет
# архив: запись 152 обработана, изменений нет
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 465 обработана, изменений нет
# справка: запись 219 обработана, изменений нет
# ревизия: запись 438 обработана, изменений нет
# проверено: запись 819 обработана, изменений нет
# проверено: запись 213 обработана, изменений нет
# временная запись: запись 68 обработана, изменений нет
# примечание: запись 680 обработана, изменений нет
# черновик: arr[8] = 93 — не выполняется
# отладка: arr[8] += 2 — не выполняется
# пометка: запись 273 обработана, изменений нет
# справка: запись 756 обработана, изменений нет
# замечание: запись 194 обработана, изменений нет
# замечание: запись 267 обработана, изменений нет
# справка: запись 367 обработана, изменений нет
# замечание: arr[1] += 85 — не выполняется
# замечание: запись 39 обработана, изменений нет
# справка: запись 216 обработана, изменений нет
# проверено: запись 39 обработана, изменений нет
# ревизия: запись 943 обработана, изменений нет
# справка: запись 285 обработана, изменений нет
# пометка: запись 820 обработана, изменений нет
# отладка: запись 398 обработана, изменений нет
# примечание: arr[8] *= 91 — не выполняется
# черновик: arr2[9] = 82 — не выполняется
# черновик: запись 928 обработана, изменений нет
# временная запись: запись 605 обработана, изменений нет
# архив: запись 627 обработана, изменений нет
# архив: запись 380 обработана, изменений нет
# пометка: запись 945 обработана, изменений нет
# временная запись: arr[2] += 59 — не выполняется
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: arr[0] = 90 — не выполняется
# архив: запись 578 обработана, изменений нет
# примечание: запись 813 обработана, изменений нет
# черновик: запись 219 обработана, изменений нет
# архив: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: arr2[7] = 48 — не выполняется
# пометка: arr[5] *= 56 — не выполняется
# ревизия: arr[8] = 60 — не выполняется
# ревизия: arr2[3] = 93 — не выполняется
# временная запись: arr[4] = 66 — не выполняется
# примечание: запись 66 обработана, изменений нет
# замечание: arr[6] += 2 — не выполняется
# пометка: запись 625 обработана, изменений нет
# архив: запись 774 обработана, изменений нет
# справка: arr[5] = 41 — не выполняется
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# временная запись: arr2[0] = 11 — не выполняется
# проверено: arr[9] *= 8 — не выполняется
# проверено: arr[5] *= 31 — не выполняется
# справка: arr2[4] = 12 — не выполняется
# замечание: запись 762 обработана, изменений нет
# пометка: запись 368 обработана, изменений нет
# замечание: запись 106 обработана, изменений нет
# пометка: запись 849 обработана, изменений нет
# архив: запись 949 обработана, изменений нет
# временная запись: запись 469 обработана, изменений нет
# ревизия: arr2[5] = 64 — не выполняется
# замечание: запись 290 обработана, изменений нет
# отладка: запись 956 обработана, изменений нет
# замечание: arr2[2] = 3 — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: arr[6] = 82 — не выполняется
# ревизия: запись 959 обработана, изменений нет
# отладка: запись 540 обработана, изменений нет
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# черновик: arr2[1] = 50 — не выполняется
# примечание: запись 121 обработана, изменений нет
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: запись 491 обработана, изменений нет
# ревизия: запись 16 обработана, изменений нет
# замечание: arr[1] = 52 — не выполняется
# ревизия: arr[8] *= 35 — не выполняется
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: запись 749 обработана, изменений нет
# проверено: запись 42 обработана, изменений нет
# замечание: arr[4] *= 1 — не выполняется
# пометка: запись 178 обработана, изменений нет
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: запись 121 обработана, изменений нет
# проверено: запись 752 обработана, изменений нет
# пометка: запись 939 обработана, изменений нет
# примечание: запись 36 обработана, изменений нет
# примечание: запись 439 обработана, изменений нет
# архив: запись 110 обработана, изменений нет
# архив: запись 114 обработана, изменений нет
# черновик: запись 424 обработана, изменений нет
# справка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: запись 322 обработана, изменений нет
# пометка: запись 817 обработана, изменений нет
# проверено: запись 842 обработана, изменений нет
# отладка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: arr2[0] = 77 — не выполняется
# временная запись: запись 91 обработана, изменений нет
# архив: arr[0] = 55 — не выполняется
# отладка: запись 993 обработана, изменений нет
# проверено: запись 215 обработана, изменений нет
# временная запись: запись 857 обработана, изменений нет
# замечание: запись 403 обработана, изменений нет
# ревизия: arr[4] += 67 — не выполняется
# черновик: запись 570 обработана, изменений нет
# замечание: arr[6] += 25 — не выполняется
# временная запись: запись 589 обработана, изменений нет
# замечание: запись 283 обработана, изменений нет
# пометка: arr[5] = 47 — не выполняется
# примечание: запись 260 обработана, изменений нет
# замечание: arr[1] *= 73 — не выполняется
# проверено: arr[8] = 13 — не выполняется
# ревизия: arr[2] = 77 — не выполняется
# архив: запись 337 обработана, изменений нет
# проверено: arr[5] += 47 — не выполняется
# черновик: arr[7] *= 99 — не выполняется
# архив: запись 444 обработана, изменений нет
# ревизия: arr[6] = 27 — не выполняется
# справка: запись 227 обработана, изменений нет
# архив: arr[0] = 41 — не выполняется
# проверено: arr[5] = 61 — не выполняется
# ревизия: arr2[1] = 4 — не выполняется
# отладка: запись 276 обработана, изменений нет
# ревизия: запись 118 обработана, изменений нет
# пометка: arr2[3] = 7 — не выполняется
# пометка: arr[0] += 56 — не выполняется
arr[6] -= 5
# проверено: arr[8] = 16 — не выполняется
# временная запись: запись 58 обработана, изменений нет
# пометка: запись 489 обработана, изменений нет
# замечание: arr2[5] = 72 — не выполняется
# отладка: arr[8] = 88 — не выполняется
# ревизия: запись 280 обработана, изменений нет
# пометка: запись 105 обработана, изменений нет
# архив: arr[8] *= 48 — не выполняется
# временная запись: запись 661 обработана, изменений нет
# архив: запись 580 обработана, изменений нет
# проверено: arr[4] = 34 — не выполняется
# архив: arr[5] *= 20 — не выполняется
# ревизия: запись 671 обработана, изменений нет
# временная запись: arr[7] = 12 — не выполняется
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: запись 316 обработана, изменений нет
# справка: запись 858 обработана, изменений нет
# пометка: arr[2] += 56 — не выполняется
# пометка: запись 271 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: arr[9] *= 52 — не выполняется
# справка: запись 228 обработана, изменений нет
# отладка: arr2[2] = 96 — не выполняется
# справка: запись 653 обработана, изменений нет
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: запись 222 обработана, изменений нет
# замечание: arr[7] = 4 — не выполняется
# проверено: запись 689 обработана, изменений нет
# временная запись: arr[6] = 83 — не выполняется
# архив: запись 484 обработана, изменений нет
# справка: arr[1] += 40 — не выполняется
# временная запись: arr[2] = 35 — не выполняется
# справка: arr2[7] = 58 — не выполняется
# замечание: arr2[2] = 65 — не выполняется
# пометка: запись 605 обработана, изменений нет
# примечание: arr[6] *= 91 — не выполняется
# справка: arr2[1] = 59 — не выполняется
# пометка: запись 239 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: запись 111 обработана, изменений нет
# отладка: запись 514 обработана, изменений нет
# черновик: запись 108 обработана, изменений нет
# временная запись: arr2[1] = 50 — не выполняется
# справка: запись 389 обработана, изменений нет
# черновик: запись 653 обработана, изменений нет
# пометка: запись 522 обработана, изменений нет
# проверено: arr[6] += 1 — не выполняется
# ревизия: запись 939 обработана, изменений нет
# черновик: запись 99 обработана, изменений нет
# ревизия: запись 28 обработана, изменений нет
# черновик: arr[7] += 45 — не выполняется
# справка: arr[3] = 36 — не выполняется
# черновик: запись 668 обработана, изменений нет
# черновик: запись 773 обработана, изменений нет
# пометка: запись 531 обработана, изменений нет
# справка: запись 995 обработана, изменений нет
# временная запись: arr[8] = 82 — не выполняется
# справка: запись 970 обработана, изменений нет
# справка: arr[8] += 42 — не выполняется
# пометка: arr2[8] = 1 — не выполняется
# проверено: arr[8] = 22 — не выполняется
# замечание: запись 392 обработана, изменений нет
# ревизия: arr[4] = 73 — не выполняется
# проверено: запись 90 обработана, изменений нет
# проверено: запись 297 обработана, изменений нет
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[1] = 70 — не выполняется
# ревизия: запись 6 обработана, изменений нет
# отладка: запись 717 обработана, изменений нет
# черновик: запись 942 обработана, изменений нет
# проверено: запись 977 обработана, изменений нет
# замечание: arr[7] = 35 — не выполняется
# проверено: запись 196 обработана, изменений нет
# отладка: arr[5] += 70 — не выполняется
# проверено: arr[2] += 90 — не выполняется
# временная запись: arr[6] = 22 — не выполняется
# архив: запись 538 обработана, изменений нет
# примечание: запись 473 обработана, изменений нет
# пометка: arr[5] *= 7 — не выполняется
# черновик: arr[8] += 53 — не выполняется
# проверено: запись 766 обработана, изменений нет
# архив: запись 382 обработана, изменений нет
# проверено: запись 122 обработана, изменений нет
# пометка: arr[4] *= 5 — не выполняется
# отладка: arr[7] += 60 — не выполняется
# примечание: arr2[9] = 13 — не выполняется
# примечание: запись 665 обработана, изменений нет
# проверено: запись 714 обработана, изменений нет
# проверено: arr[5] *= 94 — не выполняется
# пометка: запись 276 обработана, изменений нет
# замечание: запись 53 обработана, изменений нет
# справка: arr[2] *= 28 — не выполняется
# замечание: arr[2] = 12 — не выполняется
# временная запись: arr[3] += 58 — не выполняется
# временная запись: arr2[1] = 27 — не выполняется
# примечание: запись 217 обработана, изменений нет
# архив: arr[4] += 50 — не выполняется
# черновик: запись 537 обработана, изменений нет
# архив: запись 427 обработана, изменений нет
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: arr[5] += 78 — не выполняется
# замечание: запись 459 обработана, изменений нет
# временная запись: запись 191 обработана, изменений нет
# проверено: запись 598 обработана, изменений нет
# проверено: запись 7 обработана, изменений нет
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: arr[2] = 8 — не выполняется
# черновик: запись 945 обработана, изменений нет
# пометка: arr[8] = 71 — не выполняется
# временная запись: запись 654 обработана, изменений нет
# справка: запись 282 обработана, изменений нет
# замечание: arr2[1] = 94 — не выполняется
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: запись 613 обработана, изменений нет
# отладка: запись 351 обработана, изменений нет
# отладка: запись 987 обработана, изменений нет
# архив: arr[1] = 74 — не выполняется
# отладка: запись 524 обработана, изменений нет
# проверено: arr2[7] = 89 — не выполняется
# отладка: arr[6] *= 43 — не выполняется
# проверено: запись 77 обработана, изменений нет
# замечание: запись 581 обработана, изменений нет
# черновик: arr[9] *= 81 — не выполняется
# проверено: запись 874 обработана, изменений нет
# отладка: запись 169 обработана, изменений нет
# пометка: запись 430 обработана, изменений нет
# черновик: запись 422 обработана, изменений нет
# справка: запись 784 обработана, изменений нет
# справка: arr2[7] = 15 — не выполняется
# примечание: запись 221 обработана, изменений нет
# примечание: запись 525 обработана, изменений нет
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: arr[5] += 80 — не выполняется
# справка: запись 87 обработана, изменений нет
# архив: запись 202 обработана, изменений нет
# справка: arr[3] = 59 — не выполняется
# замечание: arr2[3] = 28 — не выполняется
# пометка: arr[2] += 35 — не выполняется
# замечание: запись 490 обработана, изменений нет
# ревизия: arr2[6] = 39 — не выполняется
# проверено: запись 899 обработана, изменений нет
# проверено: запись 157 обработана, изменений нет
# отладка: arr[8] = 60 — не выполняется
# проверено: arr[4] += 59 — не выполняется
# отладка: запись 41 обработана, изменений нет
# справка: arr2[4] = 51 — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# архив: запись 437 обработана, изменений нет
# замечание: запись 217 обработана, изменений нет
# примечание: запись 104 обработана, изменений нет
# архив: запись 679 обработана, изменений нет
# примечание: запись 838 обработана, изменений нет
# отладка: запись 540 обработана, изменений нет
# ревизия: arr[3] = 85 — не выполняется
# пометка: запись 460 обработана, изменений нет
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: arr[2] += 84 — не выполняется
# временная запись: запись 558 обработана, изменений нет
# архив: запись 776 обработана, изменений нет
# ревизия: arr[2] += 4 — не выполняется
# примечание: запись 110 обработана, изменений нет
# замечание: запись 672 обработана, изменений нет
# замечание: запись 8 обработана, изменений нет
# временная запись: запись 212 обработана, изменений нет
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: arr[5] += 62 — не выполняется
# архив: arr[9] += 21 — не выполняется
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 364 обработана, изменений нет
# отладка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: запись 967 обработана, изменений нет
# ревизия: запись 532 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: arr[9] += 45 — не выполняется
# временная запись: запись 615 обработана, изменений нет
# архив: запись 271 обработана, изменений нет
# отладка: запись 484 обработана, изменений нет
# временная запись: запись 248 обработана, изменений нет
# проверено: запись 89 обработана, изменений нет
# пометка: arr[1] += 86 — не выполняется
# пометка: запись 527 обработана, изменений нет
# ревизия: arr[4] *= 61 — не выполняется
# пометка: запись 604 обработана, изменений нет
# замечание: arr2[3] = 17 — не выполняется
# черновик: запись 178 обработана, изменений нет
# архив: arr[3] += 70 — не выполняется
# временная запись: arr[4] = 79 — не выполняется
# отладка: arr[4] += 91 — не выполняется
# отладка: arr2[1] = 30 — не выполняется
# архив: запись 277 обработана, изменений нет
# черновик: запись 462 обработана, изменений нет
# замечание: запись 992 обработана, изменений нет
# ревизия: запись 312 обработана, изменений нет
# отладка: arr[6] += 94 — не выполняется
# временная запись: запись 744 обработана, изменений нет
# черновик: arr[8] *= 22 — не выполняется
# ревизия: запись 275 обработана, изменений нет
# ревизия: запись 319 обработана, изменений нет
# черновик: запись 18 обработана, изменений нет
# пометка: запись 225 обработана, изменений нет
# черновик: запись 292 обработана, изменений нет
# временная запись: arr[6] *= 53 — не выполняется
# отладка: запись 823 обработана, изменений нет
# временная запись: arr2[6] = 51 — не выполняется
# временная запись: запись 785 обработана, изменений нет
# проверено: arr2[5] = 22 — не выполняется
# справка: запись 868 обработана, изменений нет
# примечание: запись 196 обработана, изменений нет
# черновик: arr2[9] = 44 — не выполняется
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 693 обработана, изменений нет
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 167 обработана, изменений нет
# временная запись: arr2[1] = 55 — не выполняется
# временная запись: arr[7] += 13 — не выполняется
# замечание: запись 140 обработана, изменений нет
# примечание: запись 778 обработана, изменений нет
# ревизия: запись 573 обработана, изменений нет
# примечание: запись 213 обработана, изменений нет
# пометка: arr[8] *= 53 — не выполняется
# временная запись: arr[9] *= 49 — не выполняется
# ревизия: arr[1] += 82 — не выполняется
# справка: arr2[2] = 88 — не выполняется
# замечание: запись 571 обработана, изменений нет
# временная запись: запись 944 обработана, изменений нет
# архив: arr[1] *= 83 — не выполняется
# примечание: arr[0] *= 82 — не выполняется
# проверено: запись 70 обработана, изменений нет
# отладка: запись 487 обработана, изменений нет
# временная запись: запись 530 обработана, изменений нет
# черновик: запись 347 обработана, изменений нет
# справка: запись 110 обработана, изменений нет
# отладка: запись 896 обработана, изменений нет
# проверено: запись 986 обработана, изменений нет
# замечание: запись 909 обработана, изменений нет
# временная запись: запись 752 обработана, изменений нет
# примечание: arr[8] = 80 — не выполняется
# справка: запись 54 обработана, изменений нет
# справка: arr2[1] = 17 — не выполняется
# архив: запись 941 обработана, изменений нет
# проверено: запись 765 обработана, изменений нет
# отладка: запись 614 обработана, изменений нет
# пометка: запись 525 обработана, изменений нет
# временная запись: запись 98 обработана, изменений нет
# архив: запись 482 обработана, изменений нет
# архив: запись 879 обработана, изменений нет
# примечание: arr[9] *= 38 — не выполняется
# черновик: arr[5] += 85 — не выполняется
# временная запись: arr[6] = 97 — не выполняется
# временная запись: arr2[8] = 60 — не выполняется
# архив: arr[7] += 58 — не выполняется
# черновик: запись 558 обработана, изменений нет
# временная запись: arr[2] = 98 — не выполняется
# проверено: запись 795 обработана, изменений нет
# замечание: arr2[5] = 24 — не выполняется
# ревизия: запись 710 обработана, изменений нет
# справка: запись 713 обработана, изменений нет
# временная запись: arr[2] = 53 — не выполняется
# архив: arr[3] = 40 — не выполняется
# проверено: запись 499 обработана, изменений нет
# справка: arr2[2] = 98 — не выполняется
# примечание: arr[9] += 20 — не выполняется
# отладка: запись 272 обработана, изменений нет
# черновик: arr2[0] = 43 — не выполняется
# справка: запись 907 обработана, изменений нет
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: запись 654 обработана, изменений нет
# примечание: запись 893 обработана, изменений нет
# черновик: arr2[4] = 96 — не выполняется
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: запись 343 обработана, изменений нет
# справка: запись 611 обработана, изменений нет
# справка: arr[2] = 22 — не выполняется
# черновик: запись 679 обработана, изменений нет
# архив: запись 61 обработана, изменений нет
# примечание: запись 528 обработана, изменений нет
# проверено: arr2[6] = 88 — не выполняется
# архив: запись 784 обработана, изменений нет
# проверено: запись 307 обработана, изменений нет
# отладка: arr[0] = 79 — не выполняется
# справка: запись 469 обработана, изменений нет
arr[9] += 7
# архив: запись 37 обработана, изменений нет
# ревизия: arr[8] += 61 — не выполняется
# черновик: arr2[4] = 54 — не выполняется
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr2[2] = 48 — не выполняется
# временная запись: запись 288 обработана, изменений нет
# замечание: запись 731 обработана, изменений нет
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: запись 727 обработана, изменений нет
# отладка: arr[3] = 59 — не выполняется
# справка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: arr2[1] = 95 — не выполняется
# замечание: запись 477 обработана, изменений нет
# временная запись: arr[2] += 86 — не выполняется
# черновик: запись 695 обработана, изменений нет
# пометка: запись 523 обработана, изменений нет
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[1] = 19 — не выполняется
# пометка: запись 85 обработана, изменений нет
# примечание: arr[6] += 96 — не выполняется
# отладка: запись 577 обработана, изменений нет
# проверено: запись 42 обработана, изменений нет
# примечание: arr2[2] = 77 — не выполняется
# черновик: arr[8] *= 10 — не выполняется
# временная запись: запись 729 обработана, изменений нет
# ревизия: запись 564 обработана, изменений нет
# отладка: arr[6] += 85 — не выполняется
# замечание: запись 796 обработана, изменений нет
# замечание: arr[6] *= 51 — не выполняется
# примечание: запись 192 обработана, изменений нет
# пометка: arr[1] += 9 — не выполняется
# черновик: arr[3] += 67 — не выполняется
# черновик: arr2[7] = 77 — не выполняется
# проверено: arr[8] = 20 — не выполняется
# временная запись: запись 691 обработана, изменений нет
# замечание: arr2[3] = 14 — не выполняется
# пометка: запись 221 обработана, изменений нет
# архив: запись 901 обработана, изменений нет
# отладка: arr2[4] = 15 — не выполняется
# временная запись: запись 340 обработана, изменений нет
# ревизия: arr[7] = 77 — не выполняется
# справка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: запись 732 обработана, изменений нет
# отладка: запись 209 обработана, изменений нет
# проверено: arr[0] = 25 — не выполняется
# пометка: запись 399 обработана, изменений нет
# временная запись: запись 14 обработана, изменений нет
# архив: запись 744 обработана, изменений нет
# черновик: запись 679 обработана, изменений нет
# замечание: запись 710 обработана, изменений нет
# примечание: arr[3] += 90 — не выполняется
# отладка: запись 328 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# замечание: arr[1] *= 40 — не выполняется
# временная запись: запись 211 обработана, изменений нет
# пометка: запись 117 обработана, изменений нет
# пометка: запись 50 обработана, изменений нет
# архив: запись 717 обработана, изменений нет
# пометка: arr2[5] = 83 — не выполняется
# черновик: arr[9] *= 48 — не выполняется
# отладка: запись 458 обработана, изменений нет
# проверено: arr[9] += 38 — не выполняется
# ревизия: arr[3] += 57 — не выполняется
# временная запись: arr[6] += 81 — не выполняется
# архив: запись 640 обработана, изменений нет
# проверено: запись 927 обработана, изменений нет
# архив: запись 905 обработана, изменений нет
# черновик: запись 609 обработана, изменений нет
# пометка: запись 644 обработана, изменений нет
# проверено: arr[1] += 60 — не выполняется
# архив: запись 370 обработана, изменений нет
# отладка: arr[0] = 39 — не выполняется
# ревизия: arr[1] = 65 — не выполняется
# замечание: запись 923 обработана, изменений нет
# отладка: запись 934 обработана, изменений нет
# архив: запись 578 обработана, изменений нет
# проверено: arr2[4] = 65 — не выполняется
# проверено: запись 336 обработана, изменений нет
# архив: запись 959 обработана, изменений нет
# ревизия: arr2[9] = 46 — не выполняется
# черновик: запись 417 обработана, изменений нет
# отладка: запись 569 обработана, изменений нет
# ревизия: arr[7] = 71 — не выполняется
# справка: arr2[9] = 1 — не выполняется
# архив: arr2[3] = 44 — не выполняется
# архив: запись 295 обработана, изменений нет
# временная запись: запись 542 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: запись 534 обработана, изменений нет
# черновик: arr[9] = 8 — не выполняется
# ревизия: запись 218 обработана, изменений нет
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 138 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[5] = 78 — не выполняется
# пометка: arr[8] *= 55 — не выполняется
# отладка: запись 396 обработана, изменений нет
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: arr[3] = 35 — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 397 обработана, изменений нет
# отладка: запись 627 обработана, изменений нет
# примечание: запись 51 обработана, изменений нет
# временная запись: запись 864 обработана, изменений нет
# архив: arr[4] += 86 — не выполняется
# временная запись: запись 732 обработана, изменений нет
# пометка: запись 401 обработана, изменений нет
# отладка: запись 134 обработана, изменений нет
# черновик: arr[5] *= 67 — не выполняется
# замечание: запись 925 обработана, изменений нет
# отладка: запись 774 обработана, изменений нет
# отладка: запись 76 обработана, изменений нет
# временная запись: запись 817 обработана, изменений нет
# отладка: arr[5] = 33 — не выполняется
# ревизия: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: запись 79 обработана, изменений нет
# проверено: запись 224 обработана, изменений нет
# архив: запись 144 обработана, изменений нет
# справка: arr[9] = 7 — не выполняется
# черновик: arr[6] = 56 — не выполняется
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: arr[0] = 80 — не выполняется
# отладка: arr[4] += 69 — не выполняется
# ревизия: arr[4] *= 50 — не выполняется
# примечание: arr2[3] = 62 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: запись 621 обработана, изменений нет
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr[7] = 41 — не выполняется
# ревизия: запись 301 обработана, изменений нет
# проверено: arr[3] += 22 — не выполняется
# отладка: запись 32 обработана, изменений нет
# ревизия: запись 241 обработана, изменений нет
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr2[9] = 95 — не выполняется
# временная запись: запись 62 обработана, изменений нет
# справка: запись 44 обработана, изменений нет
# временная запись: arr[3] = 15 — не выполняется
# черновик: arr2[1] = 90 — не выполняется
# пометка: запись 188 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 730 обработана, изменений нет
# пометка: запись 361 обработана, изменений нет
# примечание: запись 622 обработана, изменений нет
# проверено: запись 926 обработана, изменений нет
# замечание: arr[9] *= 21 — не выполняется
# примечание: запись 838 обработана, изменений нет
# ревизия: запись 520 обработана, изменений нет
# справка: запись 696 обработана, изменений нет
# архив: arr[8] = 35 — не выполняется
# временная запись: arr[7] *= 92 — не выполняется
# справка: arr[5] += 97 — не выполняется
# ревизия: запись 680 обработана, изменений нет
# отладка: запись 472 обработана, изменений нет
# примечание: запись 737 обработана, изменений нет
# справка: arr[3] = 88 — не выполняется
# проверено: arr2[1] = 27 — не выполняется
# проверено: запись 983 обработана, изменений нет
# справка: arr[9] = 16 — не выполняется
# справка: запись 542 обработана, изменений нет
# отладка: запись 826 обработана, изменений нет
# пометка: запись 440 обработана, изменений нет
# отладка: запись 930 обработана, изменений нет
# примечание: запись 182 обработана, изменений нет
# проверено: запись 374 обработана, изменений нет
# замечание: arr[6] *= 63 — не выполняется
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: запись 601 обработана, изменений нет
# примечание: запись 80 обработана, изменений нет
# временная запись: arr[1] = 5 — не выполняется
# проверено: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: arr[8] *= 90 — не выполняется
# ревизия: запись 243 обработана, изменений нет
# ревизия: запись 830 обработана, изменений нет
# замечание: запись 5 обработана, изменений нет
# проверено: запись 214 обработана, изменений нет
# примечание: запись 330 обработана, изменений нет
# временная запись: запись 843 обработана, изменений нет
# ревизия: запись 528 обработана, изменений нет
# черновик: запись 502 обработана, изменений нет
# замечание: arr2[7] = 67 — не выполняется
# черновик: arr[4] += 65 — не выполняется
# временная запись: запись 702 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# замечание: запись 427 обработана, изменений нет
# примечание: запись 200 обработана, изменений нет
# замечание: запись 268 обработана, изменений нет
# ревизия: arr[3] += 59 — не выполняется
# примечание: arr[6] += 64 — не выполняется
# ревизия: arr[8] *= 86 — не выполняется
# черновик: запись 300 обработана, изменений нет
# замечание: arr2[5] = 94 — не выполняется
# замечание: arr[0] = 58 — не выполняется
# временная запись: запись 748 обработана, изменений нет
# временная запись: arr[9] *= 62 — не выполняется
# ревизия: запись 455 обработана, изменений нет
# архив: запись 493 обработана, изменений нет
# временная запись: arr[2] = 39 — не выполняется
# замечание: запись 309 обработана, изменений нет
# справка: arr[1] += 95 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr[4] += 35 — не выполняется
# справка: arr[0] *= 17 — не выполняется
# черновик: запись 734 обработана, изменений нет
# ревизия: запись 74 обработана, изменений нет
# временная запись: запись 857 обработана, изменений нет
# отладка: запись 677 обработана, изменений нет
# справка: arr2[7] = 8 — не выполняется
# отладка: arr[4] *= 30 — не выполняется
# пометка: arr[4] = 11 — не выполняется
# замечание: arr[9] *= 72 — не выполняется
# пометка: запись 502 обработана, изменений нет
# отладка: arr[5] += 8 — не выполняется
# примечание: arr2[0] = 3 — не выполняется
# примечание: запись 618 обработана, изменений нет
# пометка: arr[7] *= 40 — не выполняется
# проверено: arr2[1] = 90 — не выполняется
# отладка: запись 216 обработана, изменений нет
# пометка: запись 565 обработана, изменений нет
# проверено: запись 445 обработана, изменений нет
# проверено: запись 558 обработана, изменений нет
# черновик: arr2[8] = 69 — не выполняется
# черновик: arr2[2] = 6 — не выполняется
# отладка: запись 432 обработана, изменений нет
# справка: arr[5] += 72 — не выполняется
# черновик: arr[1] += 49 — не выполняется
# временная запись: запись 817 обработана, изменений нет
# справка: запись 857 обработана, изменений нет
# отладка: arr2[5] = 55 — не выполняется
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: запись 836 обработана, изменений нет
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[5] *= 76 — не выполняется
# ревизия: arr[0] += 20 — не выполняется
# черновик: arr2[9] = 67 — не выполняется
# проверено: arr[7] = 29 — не выполняется
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: запись 738 обработана, изменений нет
# архив: запись 90 обработана, изменений нет
# временная запись: запись 974 обработана, изменений нет
# черновик: запись 348 обработана, изменений нет
# временная запись: arr[7] += 8 — не выполняется
# временная запись: запись 52 обработана, изменений нет
# пометка: arr2[9] = 17 — не выполняется
# ревизия: запись 529 обработана, изменений нет
# ревизия: запись 46 обработана, изменений нет
# примечание: arr[8] += 45 — не выполняется
# пометка: arr[0] = 41 — не выполняется
# отладка: arr[0] *= 33 — не выполняется
# справка: arr2[4] = 56 — не выполняется
# пометка: запись 305 обработана, изменений нет
# отладка: arr[9] *= 94 — не выполняется
# отладка: запись 371 обработана, изменений нет
# временная запись: запись 657 обработана, изменений нет
# отладка: arr[1] += 99 — не выполняется
# отладка: запись 540 обработана, изменений нет
# справка: arr[0] += 91 — не выполняется
# архив: запись 106 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# временная запись: запись 516 обработана, изменений нет
# примечание: запись 620 обработана, изменений нет
# примечание: запись 989 обработана, изменений нет
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: arr[5] = 95 — не выполняется
# справка: запись 752 обработана, изменений нет
# пометка: arr[6] = 33 — не выполняется
# примечание: arr[2] *= 23 — не выполняется
# пометка: arr[7] += 36 — не выполняется
# справка: arr[6] *= 54 — не выполняется
# временная запись: arr[3] += 67 — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: arr[3] += 92 — не выполняется
# примечание: arr[4] += 67 — не выполняется
# замечание: arr2[4] = 35 — не выполняется
# замечание: arr[8] += 30 — не выполняется
# отладка: arr[4] += 43 — не выполняется
# черновик: arr[7] *= 7 — не выполняется
# временная запись: запись 495 обработана, изменений нет
t334 = str(arr[1]) + str(arr[1])
# справка: arr[1] += 54 — не выполняется
# ревизия: arr[0] = 73 — не выполняется
# примечание: запись 440 обработана, изменений нет
# архив: запись 269 обработана, изменений нет
# черновик: arr2[2] = 1 — не выполняется
# замечание: запись 279 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: arr[4] *= 20 — не выполняется
# черновик: запись 191 обработана, изменений нет
# справка: запись 676 обработана, изменений нет
# замечание: arr[0] = 80 — не выполняется
# архив: запись 828 обработана, изменений нет
# отладка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: arr[6] = 54 — не выполняется
# справка: arr[6] *= 42 — не выполняется
# проверено: запись 398 обработана, изменений нет
# отладка: запись 49 обработана, изменений нет
# отладка: запись 528 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[0] *= 95 — не выполняется
# черновик: запись 576 обработана, изменений нет
# пометка: arr2[0] = 3 — не выполняется
# справка: arr[1] = 71 — не выполняется
# проверено: arr2[9] = 80 — не выполняется
# примечание: запись 955 обработана, изменений нет
# архив: запись 638 обработана, изменений нет
# черновик: arr[9] += 46 — не выполняется
# проверено: arr[1] += 2 — не выполняется
# примечание: запись 350 обработана, изменений нет
# пометка: запись 272 обработана, изменений нет
# отладка: arr[4] = 2 — не выполняется
# пометка: запись 278 обработана, изменений нет
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 297 обработана, изменений нет
# ревизия: запись 726 обработана, изменений нет
# черновик: arr[9] = 31 — не выполняется
# проверено: запись 742 обработана, изменений нет
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: запись 369 обработана, изменений нет
# отладка: arr2[5] = 4 — не выполняется
# справка: arr2[6] = 59 — не выполняется
# ревизия: arr[0] = 97 — не выполняется
# временная запись: arr[8] += 72 — не выполняется
# отладка: запись 824 обработана, изменений нет
# ревизия: arr[2] *= 25 — не выполняется
# временная запись: запись 648 обработана, изменений нет
# архив: запись 484 обработана, изменений нет
# замечание: arr[4] += 5 — не выполняется
# временная запись: запись 561 обработана, изменений нет
# отладка: запись 984 обработана, изменений нет
# черновик: arr[3] *= 60 — не выполняется
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: запись 620 обработана, изменений нет
# проверено: arr[2] *= 26 — не выполняется
# примечание: arr[9] = 77 — не выполняется
# пометка: запись 352 обработана, изменений нет
# отладка: запись 706 обработана, изменений нет
# черновик: запись 485 обработана, изменений нет
# примечание: arr[7] *= 45 — не выполняется
# ревизия: arr[9] += 32 — не выполняется
# временная запись: запись 637 обработана, изменений нет
# проверено: arr[4] *= 61 — не выполняется
# черновик: запись 794 обработана, изменений нет
# ревизия: arr[0] = 60 — не выполняется
# справка: запись 358 обработана, изменений нет
# пометка: запись 800 обработана, изменений нет
# проверено: arr[9] *= 66 — не выполняется
# справка: arr[7] *= 33 — не выполняется
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: arr[9] *= 52 — не выполняется
# временная запись: arr[4] *= 49 — не выполняется
# проверено: arr[0] = 35 — не выполняется
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: запись 651 обработана, изменений нет
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: запись 600 обработана, изменений нет
# справка: запись 19 обработана, изменений нет
# пометка: запись 35 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: запись 48 обработана, изменений нет
# пометка: запись 14 обработана, изменений нет
# замечание: запись 362 обработана, изменений нет
# архив: запись 390 обработана, изменений нет
# отладка: запись 744 обработана, изменений нет
# пометка: запись 837 обработана, изменений нет
# пометка: arr[4] += 87 — не выполняется
# примечание: arr[2] = 76 — не выполняется
# замечание: запись 211 обработана, изменений нет
# ревизия: запись 336 обработана, изменений нет
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 57 обработана, изменений нет
# замечание: arr[6] *= 52 — не выполняется
# черновик: запись 691 обработана, изменений нет
# справка: запись 163 обработана, изменений нет
# ревизия: arr2[8] = 54 — не выполняется
# ревизия: arr[2] *= 51 — не выполняется
# примечание: arr[8] += 35 — не выполняется
# проверено: arr[4] *= 10 — не выполняется
# пометка: запись 23 обработана, изменений нет
# проверено: arr[5] += 57 — не выполняется
# справка: arr2[1] = 42 — не выполняется
# черновик: arr2[4] = 57 — не выполняется
# замечание: arr[4] += 12 — не выполняется
# черновик: arr[2] += 28 — не выполняется
# замечание: запись 495 обработана, изменений нет
# примечание: arr2[7] = 13 — не выполняется
# архив: запись 172 обработана, изменений нет
# примечание: запись 67 обработана, изменений нет
# примечание: запись 530 обработана, изменений нет
# архив: arr[8] = 8 — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: arr[2] *= 17 — не выполняется
# замечание: запись 466 обработана, изменений нет
# примечание: arr[0] += 65 — не выполняется
# примечание: arr[2] *= 13 — не выполняется
# замечание: запись 439 обработана, изменений нет
# проверено: запись 321 обработана, изменений нет
# примечание: arr[6] += 5 — не выполняется
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: arr2[8] = 35 — не выполняется
# замечание: arr[1] = 45 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr[1] += 74 — не выполняется
# примечание: запись 802 обработана, изменений нет
# архив: запись 11 обработана, изменений нет
# черновик: arr[3] += 66 — не выполняется
# архив: запись 884 обработана, изменений нет
# замечание: запись 18 обработана, изменений нет
# пометка: arr[5] *= 55 — не выполняется
# ревизия: запись 374 обработана, изменений нет
# замечание: arr2[7] = 34 — не выполняется
# черновик: arr[8] = 17 — не выполняется
# отладка: arr[2] *= 12 — не выполняется
# проверено: запись 779 обработана, изменений нет
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr[8] *= 72 — не выполняется
# пометка: arr[6] = 13 — не выполняется
# пометка: запись 861 обработана, изменений нет
# справка: arr[4] *= 11 — не выполняется
# справка: arr2[3] = 23 — не выполняется
# справка: запись 763 обработана, изменений нет
# проверено: запись 204 обработана, изменений нет
# пометка: запись 665 обработана, изменений нет
# пометка: запись 489 обработана, изменений нет
# архив: arr[3] += 16 — не выполняется
# архив: запись 906 обработана, изменений нет
# временная запись: запись 717 обработана, изменений нет
# архив: запись 103 обработана, изменений нет
# ревизия: запись 314 обработана, изменений нет
# отладка: arr[4] += 78 — не выполняется
# справка: arr[0] = 29 — не выполняется
# черновик: arr2[5] = 26 — не выполняется
# временная запись: запись 409 обработана, изменений нет
# временная запись: arr[1] += 61 — не выполняется
# замечание: arr[6] *= 77 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 397 обработана, изменений нет
# черновик: запись 354 обработана, изменений нет
# отладка: arr[9] += 14 — не выполняется
# ревизия: запись 23 обработана, изменений нет
# отладка: arr[3] *= 7 — не выполняется
# ревизия: arr[3] = 56 — не выполняется
# пометка: arr[9] *= 43 — не выполняется
# справка: arr[7] = 92 — не выполняется
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: arr[3] *= 51 — не выполняется
# временная запись: запись 922 обработана, изменений нет
# черновик: arr[0] *= 15 — не выполняется
# проверено: arr[7] *= 96 — не выполняется
# замечание: arr2[9] = 59 — не выполняется
# проверено: arr2[1] = 88 — не выполняется
# замечание: запись 60 обработана, изменений нет
# отладка: arr2[0] = 34 — не выполняется
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 661 обработана, изменений нет
# отладка: запись 636 обработана, изменений нет
# отладка: arr[5] = 37 — не выполняется
# черновик: arr[6] += 20 — не выполняется
# архив: запись 35 обработана, изменений нет
# архив: запись 910 обработана, изменений нет
# замечание: запись 4 обработана, изменений нет
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: запись 616 обработана, изменений нет
# примечание: arr[9] *= 1 — не выполняется
# примечание: запись 9 обработана, изменений нет
# замечание: arr[6] += 13 — не выполняется
# справка: запись 800 обработана, изменений нет
# примечание: arr[9] = 31 — не выполняется
# черновик: arr[4] *= 69 — не выполняется
# черновик: arr[5] = 80 — не выполняется
# временная запись: запись 163 обработана, изменений нет
# справка: запись 473 обработана, изменений нет
# замечание: запись 391 обработана, изменений нет
# замечание: arr2[5] = 33 — не выполняется
# ревизия: arr[6] = 39 — не выполняется
# временная запись: запись 690 обработана, изменений нет
# пометка: arr[1] *= 98 — не выполняется
# временная запись: arr[5] += 43 — не выполняется
# архив: arr[3] += 91 — не выполняется
# отладка: запись 601 обработана, изменений нет
# пометка: запись 508 обработана, изменений нет
# замечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: arr[1] = 42 — не выполняется
# архив: запись 47 обработана, изменений нет
# замечание: запись 704 обработана, изменений нет
# отладка: запись 710 обработана, изменений нет
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 133 обработана, изменений нет
# примечание: запись 518 обработана, изменений нет
# примечание: запись 880 обработана, изменений нет
# замечание: arr[9] *= 11 — не выполняется
# справка: arr[3] += 57 — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: запись 411 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# замечание: запись 771 обработана, изменений нет
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 696 обработана, изменений нет
# черновик: запись 229 обработана, изменений нет
# архив: запись 840 обработана, изменений нет
# архив: arr[8] = 7 — не выполняется
# отладка: arr[1] *= 66 — не выполняется
# примечание: запись 567 обработана, изменений нет
# проверено: запись 319 обработана, изменений нет
# ревизия: запись 216 обработана, изменений нет
# черновик: запись 775 обработана, изменений нет
# пометка: запись 97 обработана, изменений нет
# проверено: запись 431 обработана, изменений нет
# ревизия: arr[2] = 68 — не выполняется
# справка: запись 988 обработана, изменений нет
# временная запись: запись 592 обработана, изменений нет
# замечание: arr2[4] = 82 — не выполняется
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: arr[4] = 80 — не выполняется
# замечание: запись 860 обработана, изменений нет
# архив: запись 836 обработана, изменений нет
# примечание: запись 618 обработана, изменений нет
# примечание: arr[4] = 71 — не выполняется
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: запись 460 обработана, изменений нет
# отладка: запись 65 обработана, изменений нет
# архив: запись 439 обработана, изменений нет
# справка: arr2[0] = 94 — не выполняется
# черновик: запись 155 обработана, изменений нет
# замечание: запись 940 обработана, изменений нет
# замечание: запись 594 обработана, изменений нет
# справка: запись 910 обработана, изменений нет
# справка: arr2[6] = 14 — не выполняется
# архив: arr[6] += 37 — не выполняется
# архив: запись 211 обработана, изменений нет
# черновик: arr[5] = 57 — не выполняется
# проверено: arr[7] *= 56 — не выполняется
# примечание: arr[2] *= 79 — не выполняется
# черновик: запись 463 обработана, изменений нет
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: запись 835 обработана, изменений нет
# проверено: запись 509 обработана, изменений нет
# замечание: запись 492 обработана, изменений нет
# замечание: arr[9] *= 26 — не выполняется
# проверено: запись 214 обработана, изменений нет
# замечание: запись 554 обработана, изменений нет
# ревизия: запись 810 обработана, изменений нет
# отладка: запись 899 обработана, изменений нет
# временная запись: arr[0] += 42 — не выполняется
# примечание: запись 841 обработана, изменений нет
# временная запись: arr[4] = 83 — не выполняется
# проверено: arr[5] *= 31 — не выполняется
# проверено: arr2[8] = 71 — не выполняется
# пометка: запись 729 обработана, изменений нет
# пометка: запись 885 обработана, изменений нет
# ревизия: запись 344 обработана, изменений нет
# проверено: arr[6] *= 72 — не выполняется
# ревизия: arr[5] *= 66 — не выполняется
# архив: запись 452 обработана, изменений нет
# отладка: arr[7] = 34 — не выполняется
# проверено: arr[5] += 99 — не выполняется
# примечание: arr2[0] = 3 — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# проверено: запись 727 обработана, изменений нет
# проверено: arr[8] += 94 — не выполняется
# отладка: arr2[4] = 83 — не выполняется
# замечание: запись 365 обработана, изменений нет
arr[9] = int(t334) % 97
# временная запись: запись 350 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 975 обработана, изменений нет
# проверено: запись 851 обработана, изменений нет
# ревизия: запись 431 обработана, изменений нет
# справка: запись 431 обработана, изменений нет
# проверено: запись 782 обработана, изменений нет
# пометка: запись 692 обработана, изменений нет
# примечание: arr[2] *= 15 — не выполняется
# отладка: запись 483 обработана, изменений нет
# отладка: arr[0] = 72 — не выполняется
# отладка: arr[7] += 61 — не выполняется
# ревизия: arr[4] += 88 — не выполняется
# справка: запись 101 обработана, изменений нет
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: запись 792 обработана, изменений нет
# отладка: arr[7] = 87 — не выполняется
# временная запись: запись 213 обработана, изменений нет
# ревизия: запись 910 обработана, изменений нет
# архив: arr[1] *= 29 — не выполняется
# отладка: arr[2] *= 30 — не выполняется
# примечание: arr[6] *= 45 — не выполняется
# замечание: arr[0] = 58 — не выполняется
# справка: arr[8] = 10 — не выполняется
# проверено: arr[9] += 31 — не выполняется
# ревизия: запись 392 обработана, изменений нет
# отладка: запись 675 обработана, изменений нет
# замечание: arr2[8] = 72 — не выполняется
# временная запись: запись 101 обработана, изменений нет
# пометка: arr2[2] = 41 — не выполняется
# отладка: запись 938 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: запись 213 обработана, изменений нет
# архив: запись 228 обработана, изменений нет
# ревизия: arr[6] *= 95 — не выполняется
# ревизия: запись 551 обработана, изменений нет
# временная запись: arr[7] = 35 — не выполняется
# замечание: запись 706 обработана, изменений нет
# справка: запись 898 обработана, изменений нет
# архив: arr2[4] = 14 — не выполняется
# архив: запись 826 обработана, изменений нет
# черновик: arr[8] *= 51 — не выполняется
# замечание: запись 725 обработана, изменений нет
# отладка: arr[0] += 16 — не выполняется
# временная запись: arr[5] += 74 — не выполняется
# пометка: запись 361 обработана, изменений нет
# справка: запись 940 обработана, изменений нет
# черновик: запись 66 обработана, изменений нет
# отладка: arr2[7] = 94 — не выполняется
# пометка: запись 124 обработана, изменений нет
# проверено: arr[5] += 55 — не выполняется
# отладка: arr2[8] = 39 — не выполняется
# замечание: запись 923 обработана, изменений нет
# архив: arr[1] *= 18 — не выполняется
# примечание: запись 391 обработана, изменений нет
# отладка: arr2[5] = 40 — не выполняется
# замечание: запись 626 обработана, изменений нет
# справка: arr2[7] = 88 — не выполняется
# архив: запись 513 обработана, изменений нет
# пометка: arr[3] += 95 — не выполняется
# черновик: arr[0] += 95 — не выполняется
# примечание: запись 35 обработана, изменений нет
# черновик: arr[1] = 83 — не выполняется
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: arr[1] += 39 — не выполняется
# временная запись: запись 650 обработана, изменений нет
# примечание: запись 935 обработана, изменений нет
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: arr[1] *= 86 — не выполняется
# примечание: запись 701 обработана, изменений нет
# проверено: arr[7] *= 63 — не выполняется
# черновик: запись 323 обработана, изменений нет
# замечание: запись 324 обработана, изменений нет
# пометка: arr[8] += 66 — не выполняется
# справка: arr[1] += 60 — не выполняется
# отладка: запись 670 обработана, изменений нет
# черновик: arr2[1] = 98 — не выполняется
# справка: запись 837 обработана, изменений нет
# ревизия: запись 421 обработана, изменений нет
# черновик: arr[4] = 56 — не выполняется
# ревизия: запись 395 обработана, изменений нет
# проверено: запись 286 обработана, изменений нет
# черновик: arr[3] *= 32 — не выполняется
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# примечание: запись 819 обработана, изменений нет
# пометка: запись 203 обработана, изменений нет
# примечание: запись 586 обработана, изменений нет
# временная запись: arr[9] *= 90 — не выполняется
# ревизия: запись 13 обработана, изменений нет
# пометка: запись 913 обработана, изменений нет
# ревизия: запись 989 обработана, изменений нет
# временная запись: запись 800 обработана, изменений нет
# проверено: запись 288 обработана, изменений нет
# ревизия: arr[1] += 24 — не выполняется
# пометка: arr[3] += 24 — не выполняется
# временная запись: запись 356 обработана, изменений нет
# примечание: arr2[3] = 61 — не выполняется
# проверено: запись 417 обработана, изменений нет
# архив: arr2[7] = 6 — не выполняется
# временная запись: запись 423 обработана, изменений нет
# пометка: arr2[5] = 42 — не выполняется
# примечание: arr[9] *= 66 — не выполняется
# временная запись: arr[6] += 52 — не выполняется
# проверено: запись 935 обработана, изменений нет
# архив: запись 560 обработана, изменений нет
# проверено: arr[9] *= 96 — не выполняется
# ревизия: запись 441 обработана, изменений нет
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: запись 255 обработана, изменений нет
# пометка: запись 827 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[2] *= 4 — не выполняется
# архив: запись 874 обработана, изменений нет
# отладка: arr[1] *= 57 — не выполняется
# пометка: запись 535 обработана, изменений нет
# отладка: arr2[1] = 61 — не выполняется
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: запись 363 обработана, изменений нет
# черновик: arr[7] *= 80 — не выполняется
# проверено: запись 386 обработана, изменений нет
# примечание: arr[4] += 88 — не выполняется
# примечание: arr2[1] = 3 — не выполняется
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[6] *= 10 — не выполняется
# ревизия: запись 408 обработана, изменений нет
# пометка: запись 231 обработана, изменений нет
# временная запись: запись 22 обработана, изменений нет
# черновик: запись 245 обработана, изменений нет
# архив: запись 39 обработана, изменений нет
# справка: запись 24 обработана, изменений нет
# проверено: arr[7] = 33 — не выполняется
# архив: arr[0] = 47 — не выполняется
# ревизия: запись 987 обработана, изменений нет
# справка: запись 640 обработана, изменений нет
# отладка: запись 491 обработана, изменений нет
# замечание: запись 804 обработана, изменений нет
# отладка: arr2[1] = 83 — не выполняется
# ревизия: arr2[0] = 97 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: запись 918 обработана, изменений нет
# проверено: запись 128 обработана, изменений нет
# примечание: arr[6] = 51 — не выполняется
# пометка: запись 91 обработана, изменений нет
# архив: arr[4] *= 45 — не выполняется
# замечание: запись 721 обработана, изменений нет
# проверено: запись 799 обработана, изменений нет
# пометка: arr[0] = 74 — не выполняется
# черновик: запись 257 обработана, изменений нет
# архив: запись 605 обработана, изменений нет
# архив: arr[2] += 52 — не выполняется
# архив: arr[9] = 40 — не выполняется
# временная запись: запись 994 обработана, изменений нет
# отладка: arr[0] = 14 — не выполняется
# проверено: arr[2] = 45 — не выполняется
# примечание: arr[9] += 37 — не выполняется
# справка: arr[4] = 97 — не выполняется
# замечание: запись 130 обработана, изменений нет
# черновик: arr[5] = 41 — не выполняется
# пометка: arr[4] = 13 — не выполняется
# черновик: запись 366 обработана, изменений нет
# справка: arr2[3] = 84 — не выполняется
# справка: запись 529 обработана, изменений нет
# ревизия: arr[7] += 49 — не выполняется
# замечание: запись 317 обработана, изменений нет
# ревизия: запись 12 обработана, изменений нет
# архив: запись 754 обработана, изменений нет
# ревизия: arr[4] += 1 — не выполняется
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: запись 165 обработана, изменений нет
# пометка: arr[1] = 29 — не выполняется
# ревизия: запись 314 обработана, изменений нет
# замечание: запись 168 обработана, изменений нет
# справка: запись 287 обработана, изменений нет
# ревизия: запись 351 обработана, изменений нет
# пометка: запись 865 обработана, изменений нет
# пометка: запись 402 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: запись 534 обработана, изменений нет
# замечание: arr[2] = 38 — не выполняется
# пометка: arr2[9] = 92 — не выполняется
# примечание: запись 169 обработана, изменений нет
# примечание: arr[5] += 73 — не выполняется
# справка: запись 497 обработана, изменений нет
# архив: arr[9] += 62 — не выполняется
# архив: запись 747 обработана, изменений нет
# временная запись: запись 934 обработана, изменений нет
# ревизия: запись 548 обработана, изменений нет
# ревизия: arr[5] *= 80 — не выполняется
# черновик: запись 173 обработана, изменений нет
# проверено: arr2[6] = 40 — не выполняется
# архив: запись 130 обработана, изменений нет
# пометка: arr[3] *= 33 — не выполняется
# архив: arr[9] *= 71 — не выполняется
# ревизия: arr2[8] = 82 — не выполняется
# черновик: arr[1] *= 30 — не выполняется
# ревизия: arr2[0] = 75 — не выполняется
# черновик: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 164 обработана, изменений нет
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# замечание: arr[0] *= 38 — не выполняется
# отладка: arr[4] = 56 — не выполняется
# временная запись: arr[4] *= 59 — не выполняется
# черновик: arr[3] = 90 — не выполняется
# временная запись: arr2[5] = 74 — не выполняется
# черновик: запись 96 обработана, изменений нет
# справка: arr[5] += 40 — не выполняется
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: arr[8] *= 54 — не выполняется
# архив: запись 669 обработана, изменений нет
# замечание: arr[1] *= 62 — не выполняется
# архив: запись 92 обработана, изменений нет
# ревизия: arr[2] += 59 — не выполняется
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: arr[2] *= 76 — не выполняется
# черновик: запись 678 обработана, изменений нет
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr[4] += 39 — не выполняется
# проверено: запись 882 обработана, изменений нет
# замечание: запись 713 обработана, изменений нет
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# примечание: arr2[5] = 88 — не выполняется
# отладка: arr[1] = 96 — не выполняется
# отладка: запись 117 обработана, изменений нет
# примечание: запись 645 обработана, изменений нет
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: запись 686 обработана, изменений нет
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: arr2[2] = 24 — не выполняется
# архив: запись 663 обработана, изменений нет
# справка: запись 603 обработана, изменений нет
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: arr[4] *= 46 — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 975 обработана, изменений нет
# архив: arr[4] = 35 — не выполняется
# временная запись: arr2[7] = 38 — не выполняется
# черновик: arr[6] += 80 — не выполняется
# черновик: запись 803 обработана, изменений нет
# примечание: запись 684 обработана, изменений нет
# примечание: запись 248 обработана, изменений нет
# пометка: arr[0] *= 56 — не выполняется
# ревизия: arr2[6] = 51 — не выполняется
# архив: arr[1] *= 72 — не выполняется
# черновик: arr[5] *= 37 — не выполняется
# пометка: запись 818 обработана, изменений нет
# отладка: запись 578 обработана, изменений нет
# пометка: arr[2] = 62 — не выполняется
# пометка: arr[9] *= 22 — не выполняется
# справка: arr[2] *= 44 — не выполняется
# справка: запись 837 обработана, изменений нет
# ревизия: запись 732 обработана, изменений нет
# пометка: запись 11 обработана, изменений нет
# примечание: arr2[8] = 20 — не выполняется
# временная запись: arr[4] = 1 — не выполняется
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: arr[6] += 86 — не выполняется
# замечание: arr2[2] = 6 — не выполняется
# замечание: arr[6] = 50 — не выполняется
# ревизия: arr[6] = 88 — не выполняется
# отладка: запись 119 обработана, изменений нет
# временная запись: arr[4] = 76 — не выполняется
# справка: запись 667 обработана, изменений нет
# временная запись: запись 896 обработана, изменений нет
# проверено: запись 877 обработана, изменений нет
# ревизия: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: запись 600 обработана, изменений нет
# архив: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: arr2[5] = 88 — не выполняется
# ревизия: запись 501 обработана, изменений нет
# примечание: запись 751 обработана, изменений нет
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: запись 12 обработана, изменений нет
# справка: arr[3] = 49 — не выполняется
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[8] = 67 — не выполняется
# проверено: arr[5] += 64 — не выполняется
# проверено: запись 440 обработана, изменений нет
# архив: запись 390 обработана, изменений нет
# ревизия: запись 490 обработана, изменений нет
# архив: arr[9] += 9 — не выполняется
# пометка: arr[8] += 32 — не выполняется
# временная запись: запись 682 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
arr[6] += 2
# ревизия: запись 107 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: запись 14 обработана, изменений нет
# временная запись: arr[5] += 6 — не выполняется
# замечание: запись 90 обработана, изменений нет
# черновик: запись 593 обработана, изменений нет
# пометка: запись 972 обработана, изменений нет
# примечание: запись 214 обработана, изменений нет
# проверено: запись 188 обработана, изменений нет
# архив: arr[9] *= 81 — не выполняется
# проверено: arr[7] += 8 — не выполняется
# черновик: arr[6] = 73 — не выполняется
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# черновик: arr[8] = 7 — не выполняется
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: arr[2] += 23 — не выполняется
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: запись 659 обработана, изменений нет
# замечание: запись 874 обработана, изменений нет
# замечание: arr[1] += 29 — не выполняется
# отладка: запись 304 обработана, изменений нет
# справка: запись 118 обработана, изменений нет
# архив: запись 86 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# справка: запись 186 обработана, изменений нет
# отладка: arr2[8] = 82 — не выполняется
# архив: arr2[9] = 64 — не выполняется
# архив: arr2[3] = 97 — не выполняется
# замечание: запись 567 обработана, изменений нет
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: запись 818 обработана, изменений нет
# черновик: arr[1] += 98 — не выполняется
# ревизия: arr2[9] = 35 — не выполняется
# отладка: запись 12 обработана, изменений нет
# справка: arr2[9] = 1 — не выполняется
# проверено: запись 74 обработана, изменений нет
# архив: arr[6] *= 60 — не выполняется
# черновик: запись 87 обработана, изменений нет
# пометка: запись 431 обработана, изменений нет
# примечание: arr[9] = 58 — не выполняется
# временная запись: запись 510 обработана, изменений нет
# примечание: arr[0] = 48 — не выполняется
# замечание: arr[4] = 20 — не выполняется
# справка: arr[6] += 59 — не выполняется
# проверено: запись 731 обработана, изменений нет
# справка: arr[2] *= 52 — не выполняется
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: запись 435 обработана, изменений нет
# черновик: arr[0] = 40 — не выполняется
# ревизия: запись 157 обработана, изменений нет
# архив: запись 783 обработана, изменений нет
# временная запись: arr2[8] = 11 — не выполняется
# временная запись: запись 86 обработана, изменений нет
# временная запись: запись 760 обработана, изменений нет
# черновик: запись 962 обработана, изменений нет
# черновик: запись 607 обработана, изменений нет
# проверено: запись 51 обработана, изменений нет
# отладка: arr[5] = 32 — не выполняется
# черновик: запись 291 обработана, изменений нет
# пометка: запись 124 обработана, изменений нет
# справка: запись 569 обработана, изменений нет
# пометка: arr2[0] = 68 — не выполняется
# черновик: arr2[7] = 83 — не выполняется
# временная запись: запись 419 обработана, изменений нет
# архив: arr[7] += 44 — не выполняется
# отладка: запись 415 обработана, изменений нет
# временная запись: запись 299 обработана, изменений нет
# проверено: arr2[8] = 31 — не выполняется
# замечание: запись 734 обработана, изменений нет
# отладка: запись 126 обработана, изменений нет
# ревизия: запись 987 обработана, изменений нет
# справка: запись 845 обработана, изменений нет
# проверено: arr[5] *= 84 — не выполняется
# справка: arr2[5] = 76 — не выполняется
# ревизия: запись 461 обработана, изменений нет
# ревизия: arr[0] = 97 — не выполняется
# примечание: arr[8] *= 9 — не выполняется
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: arr2[9] = 80 — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: arr[9] *= 75 — не выполняется
# проверено: arr[2] = 39 — не выполняется
# проверено: запись 86 обработана, изменений нет
# черновик: запись 69 обработана, изменений нет
# проверено: arr[1] = 15 — не выполняется
# проверено: запись 170 обработана, изменений нет
# проверено: arr[2] += 78 — не выполняется
# архив: arr[0] *= 39 — не выполняется
# ревизия: arr[6] *= 11 — не выполняется
# замечание: запись 564 обработана, изменений нет
# проверено: arr[8] = 49 — не выполняется
# проверено: запись 573 обработана, изменений нет
# черновик: arr[2] *= 83 — не выполняется
# проверено: запись 940 обработана, изменений нет
# отладка: запись 458 обработана, изменений нет
# справка: запись 154 обработана, изменений нет
# замечание: запись 60 обработана, изменений нет
# архив: запись 838 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: arr2[6] = 59 — не выполняется
# отладка: запись 347 обработана, изменений нет
# черновик: запись 964 обработана, изменений нет
# примечание: arr[0] = 63 — не выполняется
# справка: arr[0] *= 61 — не выполняется
# черновик: arr[2] = 2 — не выполняется
# замечание: arr2[6] = 62 — не выполняется
# проверено: arr[7] = 30 — не выполняется
# справка: запись 374 обработана, изменений нет
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: запись 110 обработана, изменений нет
# пометка: arr[8] += 96 — не выполняется
# ревизия: запись 961 обработана, изменений нет
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: запись 853 обработана, изменений нет
# замечание: запись 287 обработана, изменений нет
# архив: запись 14 обработана, изменений нет
# черновик: запись 979 обработана, изменений нет
# архив: запись 735 обработана, изменений нет
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: запись 489 обработана, изменений нет
# справка: запись 788 обработана, изменений нет
# отладка: arr[9] *= 21 — не выполняется
# пометка: arr[6] = 51 — не выполняется
# черновик: запись 348 обработана, изменений нет
# временная запись: запись 641 обработана, изменений нет
# пометка: arr[0] += 62 — не выполняется
# отладка: arr2[0] = 49 — не выполняется
# примечание: запись 343 обработана, изменений нет
# временная запись: arr[9] += 82 — не выполняется
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: arr[2] += 48 — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: arr2[9] = 90 — не выполняется
# отладка: запись 78 обработана, изменений нет
# справка: запись 732 обработана, изменений нет
# ревизия: запись 448 обработана, изменений нет
# отладка: запись 490 обработана, изменений нет
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: запись 420 обработана, изменений нет
# справка: запись 851 обработана, изменений нет
# черновик: arr[4] *= 35 — не выполняется
# архив: arr2[3] = 64 — не выполняется
# замечание: запись 463 обработана, изменений нет
# справка: arr2[6] = 7 — не выполняется
# пометка: arr[9] *= 16 — не выполняется
# отладка: arr[1] += 10 — не выполняется
# проверено: запись 315 обработана, изменений нет
# проверено: arr[5] += 15 — не выполняется
# черновик: arr[5] += 31 — не выполняется
# пометка: запись 715 обработана, изменений нет
# примечание: arr2[9] = 95 — не выполняется
# ревизия: arr[0] = 38 — не выполняется
# проверено: запись 498 обработана, изменений нет
# ревизия: запись 709 обработана, изменений нет
# примечание: запись 992 обработана, изменений нет
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# временная запись: arr[0] *= 22 — не выполняется
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: запись 88 обработана, изменений нет
# архив: arr[1] *= 32 — не выполняется
# ревизия: arr[2] *= 57 — не выполняется
# временная запись: запись 176 обработана, изменений нет
# ревизия: arr[4] *= 49 — не выполняется
# ревизия: arr2[4] = 90 — не выполняется
# пометка: arr[7] *= 94 — не выполняется
# черновик: arr2[4] = 54 — не выполняется
# ревизия: arr[1] = 67 — не выполняется
# замечание: arr[8] = 22 — не выполняется
# ревизия: запись 542 обработана, изменений нет
# примечание: запись 914 обработана, изменений нет
# пометка: arr[9] *= 7 — не выполняется
# отладка: запись 30 обработана, изменений нет
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: arr[2] += 23 — не выполняется
# отладка: запись 208 обработана, изменений нет
# ревизия: запись 364 обработана, изменений нет
# черновик: запись 904 обработана, изменений нет
# временная запись: запись 949 обработана, изменений нет
# проверено: arr[7] = 5 — не выполняется
# отладка: arr[1] += 10 — не выполняется
# замечание: запись 867 обработана, изменений нет
# отладка: arr2[7] = 40 — не выполняется
# примечание: запись 453 обработана, изменений нет
# временная запись: arr[2] *= 35 — не выполняется
# отладка: arr[3] += 87 — не выполняется
# черновик: запись 9 обработана, изменений нет
# ревизия: запись 57 обработана, изменений нет
# пометка: arr2[9] = 13 — не выполняется
# временная запись: запись 738 обработана, изменений нет
# проверено: запись 422 обработана, изменений нет
# примечание: arr2[2] = 32 — не выполняется
# отладка: arr[3] *= 53 — не выполняется
# справка: запись 150 обработана, изменений нет
# временная запись: запись 750 обработана, изменений нет
# архив: arr[0] += 48 — не выполняется
# проверено: arr[3] *= 79 — не выполняется
# временная запись: arr2[4] = 41 — не выполняется
# отладка: запись 979 обработана, изменений нет
# временная запись: запись 529 обработана, изменений нет
# проверено: запись 198 обработана, изменений нет
# ревизия: arr2[4] = 12 — не выполняется
# справка: arr[0] *= 20 — не выполняется
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# замечание: запись 961 обработана, изменений нет
# справка: запись 332 обработана, изменений нет
# проверено: arr[9] += 64 — не выполняется
# ревизия: arr[8] += 36 — не выполняется
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: arr2[7] = 98 — не выполняется
# проверено: запись 56 обработана, изменений нет
# замечание: запись 726 обработана, изменений нет
# пометка: запись 943 обработана, изменений нет
# архив: запись 706 обработана, изменений нет
# проверено: запись 764 обработана, изменений нет
# временная запись: запись 84 обработана, изменений нет
# архив: запись 476 обработана, изменений нет
# справка: arr[3] *= 86 — не выполняется
# черновик: запись 601 обработана, изменений нет
# отладка: запись 252 обработана, изменений нет
# проверено: запись 570 обработана, изменений нет
# черновик: arr2[3] = 46 — не выполняется
# примечание: запись 897 обработана, изменений нет
# справка: arr[2] *= 78 — не выполняется
# черновик: запись 362 обработана, изменений нет
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: запись 680 обработана, изменений нет
# справка: arr2[3] = 55 — не выполняется
# ревизия: arr[0] += 18 — не выполняется
# черновик: запись 484 обработана, изменений нет
# отладка: запись 538 обработана, изменений нет
# черновик: запись 451 обработана, изменений нет
# замечание: запись 673 обработана, изменений нет
# черновик: arr[1] += 45 — не выполняется
# пометка: arr[1] *= 13 — не выполняется
# пометка: запись 641 обработана, изменений нет
# справка: запись 111 обработана, изменений нет
# отладка: запись 178 обработана, изменений нет
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: запись 827 обработана, изменений нет
# временная запись: arr[7] = 15 — не выполняется
# временная запись: запись 779 обработана, изменений нет
# черновик: запись 371 обработана, изменений нет
# ревизия: arr[9] *= 87 — не выполняется
# замечание: запись 888 обработана, изменений нет
# справка: запись 499 обработана, изменений нет
# временная запись: arr[1] += 70 — не выполняется
# временная запись: запись 235 обработана, изменений нет
# черновик: arr2[7] = 88 — не выполняется
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: arr[3] *= 95 — не выполняется
# архив: запись 643 обработана, изменений нет
# отладка: запись 99 обработана, изменений нет
# проверено: запись 194 обработана, изменений нет
# временная запись: arr[9] *= 88 — не выполняется
# примечание: arr[7] *= 13 — не выполняется
# временная запись: запись 643 обработана, изменений нет
# архив: запись 933 обработана, изменений нет
# примечание: arr2[1] = 91 — не выполняется
# справка: запись 162 обработана, изменений нет
# временная запись: запись 324 обработана, изменений нет
# примечание: arr[1] *= 32 — не выполняется
# временная запись: arr2[4] = 77 — не выполняется
# пометка: arr[2] += 9 — не выполняется
# черновик: запись 607 обработана, изменений нет
# справка: arr2[9] = 28 — не выполняется
# справка: запись 393 обработана, изменений нет
# временная запись: arr2[0] = 77 — не выполняется
# справка: arr2[6] = 22 — не выполняется
# архив: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 219 обработана, изменений нет
# проверено: запись 323 обработана, изменений нет
# архив: запись 446 обработана, изменений нет
# пометка: arr[1] += 47 — не выполняется
# отладка: запись 806 обработана, изменений нет
# пометка: запись 613 обработана, изменений нет
# примечание: arr[6] *= 25 — не выполняется
# отладка: arr[0] *= 79 — не выполняется
# временная запись: запись 977 обработана, изменений нет
# примечание: arr2[2] = 89 — не выполняется
arr[3] *= 2
# черновик: arr[7] += 24 — не выполняется
# замечание: запись 121 обработана, изменений нет
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 624 обработана, изменений нет
# проверено: запись 280 обработана, изменений нет
# примечание: arr[5] += 14 — не выполняется
# ревизия: запись 594 обработана, изменений нет
# замечание: запись 369 обработана, изменений нет
# справка: запись 19 обработана, изменений нет
# примечание: arr[4] = 88 — не выполняется
# примечание: запись 442 обработана, изменений нет
# проверено: arr2[3] = 66 — не выполняется
# справка: arr[9] += 82 — не выполняется
# справка: arr[9] = 76 — не выполняется
# пометка: запись 704 обработана, изменений нет
# примечание: запись 588 обработана, изменений нет
# временная запись: arr[1] = 91 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: запись 354 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: запись 890 обработана, изменений нет
# проверено: arr2[7] = 61 — не выполняется
# справка: запись 795 обработана, изменений нет
# справка: arr[8] *= 58 — не выполняется
# пометка: запись 608 обработана, изменений нет
# ревизия: arr[1] = 88 — не выполняется
# пометка: arr[5] += 55 — не выполняется
# черновик: arr2[9] = 1 — не выполняется
# справка: arr[8] = 23 — не выполняется
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 854 обработана, изменений нет
# черновик: запись 150 обработана, изменений нет
# ревизия: arr[1] += 46 — не выполняется
# замечание: запись 594 обработана, изменений нет
# отладка: запись 830 обработана, изменений нет
# пометка: запись 983 обработана, изменений нет
# примечание: запись 324 обработана, изменений нет
# проверено: запись 837 обработана, изменений нет
# пометка: запись 257 обработана, изменений нет
# отладка: arr2[2] = 1 — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: запись 646 обработана, изменений нет
# справка: запись 632 обработана, изменений нет
# отладка: запись 875 обработана, изменений нет
# ревизия: arr[9] = 28 — не выполняется
# архив: arr[1] = 84 — не выполняется
# справка: arr[4] *= 74 — не выполняется
# временная запись: запись 465 обработана, изменений нет
# замечание: запись 615 обработана, изменений нет
# ревизия: arr[0] += 26 — не выполняется
# черновик: запись 844 обработана, изменений нет
# примечание: arr[2] = 82 — не выполняется
# отладка: запись 929 обработана, изменений нет
# временная запись: запись 679 обработана, изменений нет
# архив: arr[1] *= 26 — не выполняется
# пометка: arr2[0] = 30 — не выполняется
# черновик: запись 191 обработана, изменений нет
# пометка: запись 574 обработана, изменений нет
# черновик: arr[5] += 58 — не выполняется
# примечание: arr2[7] = 88 — не выполняется
# отладка: запись 376 обработана, изменений нет
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: arr2[6] = 79 — не выполняется
# проверено: запись 288 обработана, изменений нет
# ревизия: arr2[4] = 64 — не выполняется
# справка: arr2[8] = 89 — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[7] = 82 — не выполняется
# примечание: запись 359 обработана, изменений нет
# черновик: arr2[1] = 86 — не выполняется
# примечание: запись 106 обработана, изменений нет
# архив: запись 949 обработана, изменений нет
# проверено: arr[2] *= 94 — не выполняется
# ревизия: arr2[9] = 28 — не выполняется
# пометка: arr[3] = 22 — не выполняется
# пометка: запись 320 обработана, изменений нет
# ревизия: запись 192 обработана, изменений нет
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: arr2[1] = 40 — не выполняется
# проверено: arr2[4] = 61 — не выполняется
# справка: arr[8] = 42 — не выполняется
# проверено: запись 849 обработана, изменений нет
# справка: запись 344 обработана, изменений нет
# замечание: запись 86 обработана, изменений нет
# отладка: запись 853 обработана, изменений нет
# проверено: запись 157 обработана, изменений нет
# примечание: arr[4] = 70 — не выполняется
# замечание: arr[8] *= 59 — не выполняется
# архив: arr2[1] = 74 — не выполняется
# черновик: arr[4] = 41 — не выполняется
# временная запись: запись 58 обработана, изменений нет
# замечание: arr2[6] = 94 — не выполняется
# временная запись: запись 224 обработана, изменений нет
# пометка: запись 186 обработана, изменений нет
# черновик: запись 218 обработана, изменений нет
# архив: запись 912 обработана, изменений нет
# примечание: запись 741 обработана, изменений нет
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: запись 996 обработана, изменений нет
# временная запись: запись 59 обработана, изменений нет
# пометка: запись 268 обработана, изменений нет
# временная запись: arr2[1] = 13 — не выполняется
# примечание: arr[4] += 17 — не выполняется
# проверено: запись 726 обработана, изменений нет
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: запись 831 обработана, изменений нет
# замечание: arr[4] += 23 — не выполняется
# пометка: запись 323 обработана, изменений нет
# временная запись: запись 415 обработана, изменений нет
# проверено: arr[0] *= 68 — не выполняется
# замечание: запись 987 обработана, изменений нет
# отладка: запись 943 обработана, изменений нет
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: arr2[6] = 30 — не выполняется
# ревизия: запись 21 обработана, изменений нет
# ревизия: arr[9] = 66 — не выполняется
# пометка: arr2[1] = 19 — не выполняется
# замечание: запись 641 обработана, изменений нет
# временная запись: запись 583 обработана, изменений нет
# временная запись: запись 562 обработана, изменений нет
# черновик: arr[8] = 89 — не выполняется
# ревизия: запись 541 обработана, изменений нет
# пометка: запись 219 обработана, изменений нет
# пометка: запись 555 обработана, изменений нет
# черновик: запись 817 обработана, изменений нет
# справка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: arr[4] += 32 — не выполняется
# отладка: arr[4] *= 11 — не выполняется
# черновик: arr[9] = 36 — не выполняется
# замечание: запись 309 обработана, изменений нет
# справка: arr[9] += 46 — не выполняется
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: запись 552 обработана, изменений нет
# примечание: запись 123 обработана, изменений нет
# отладка: запись 322 обработана, изменений нет
# отладка: arr[1] *= 40 — не выполняется
# временная запись: запись 710 обработана, изменений нет
# справка: запись 615 обработана, изменений нет
# ревизия: запись 257 обработана, изменений нет
# примечание: arr2[9] = 78 — не выполняется
# отладка: запись 877 обработана, изменений нет
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: arr2[0] = 93 — не выполняется
# пометка: arr[5] += 18 — не выполняется
# ревизия: arr[6] = 40 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: arr[2] += 21 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: arr2[3] = 92 — не выполняется
# пометка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: запись 831 обработана, изменений нет
# ревизия: запись 20 обработана, изменений нет
# черновик: запись 533 обработана, изменений нет
# отладка: запись 712 обработана, изменений нет
# черновик: запись 122 обработана, изменений нет
# временная запись: arr[2] += 8 — не выполняется
# архив: запись 219 обработана, изменений нет
# ревизия: запись 827 обработана, изменений нет
# пометка: запись 181 обработана, изменений нет
# ревизия: запись 440 обработана, изменений нет
# отладка: запись 665 обработана, изменений нет
# проверено: запись 928 обработана, изменений нет
# временная запись: запись 686 обработана, изменений нет
# замечание: arr[2] += 30 — не выполняется
# проверено: запись 280 обработана, изменений нет
# ревизия: запись 551 обработана, изменений нет
# пометка: запись 959 обработана, изменений нет
# отладка: arr2[2] = 65 — не выполняется
# пометка: arr[3] = 15 — не выполняется
# черновик: запись 66 обработана, изменений нет
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: arr[3] = 10 — не выполняется
# черновик: запись 132 обработана, изменений нет
# временная запись: запись 642 обработана, изменений нет
# отладка: запись 600 обработана, изменений нет
# замечание: arr2[3] = 54 — не выполняется
# архив: arr[2] = 25 — не выполняется
# временная запись: запись 439 обработана, изменений нет
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: запись 814 обработана, изменений нет
# временная запись: запись 808 обработана, изменений нет
# справка: запись 809 обработана, изменений нет
# архив: arr[0] = 33 — не выполняется
# замечание: запись 862 обработана, изменений нет
# черновик: arr2[2] = 79 — не выполняется
# замечание: arr[3] = 8 — не выполняется
# пометка: arr[9] += 31 — не выполняется
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: запись 47 обработана, изменений нет
# проверено: запись 516 обработана, изменений нет
# пометка: запись 486 обработана, изменений нет
# черновик: arr[6] *= 88 — не выполняется
# примечание: arr[3] = 39 — не выполняется
# замечание: arr2[6] = 64 — не выполняется
# справка: запись 517 обработана, изменений нет
# справка: arr2[8] = 31 — не выполняется
# справка: запись 58 обработана, изменений нет
# замечание: arr2[3] = 90 — не выполняется
# справка: запись 18 обработана, изменений нет
# черновик: запись 737 обработана, изменений нет
# проверено: запись 140 обработана, изменений нет
# временная запись: arr[5] = 28 — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: arr[7] *= 64 — не выполняется
# архив: запись 237 обработана, изменений нет
# замечание: запись 485 обработана, изменений нет
# ревизия: запись 436 обработана, изменений нет
# справка: запись 490 обработана, изменений нет
# справка: запись 686 обработана, изменений нет
# временная запись: запись 33 обработана, изменений нет
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 121 обработана, изменений нет
# отладка: arr[7] = 16 — не выполняется
# отладка: arr[8] += 7 — не выполняется
# замечание: запись 253 обработана, изменений нет
# проверено: запись 805 обработана, изменений нет
# пометка: запись 793 обработана, изменений нет
# пометка: запись 924 обработана, изменений нет
# черновик: arr[6] = 2 — не выполняется
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: запись 222 обработана, изменений нет
# черновик: запись 140 обработана, изменений нет
# черновик: запись 783 обработана, изменений нет
# замечание: запись 752 обработана, изменений нет
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: arr[4] *= 36 — не выполняется
# отладка: запись 485 обработана, изменений нет
# примечание: запись 973 обработана, изменений нет
# архив: arr[4] = 49 — не выполняется
# пометка: запись 536 обработана, изменений нет
# примечание: запись 112 обработана, изменений нет
# проверено: запись 973 обработана, изменений нет
# примечание: запись 54 обработана, изменений нет
# архив: arr2[0] = 53 — не выполняется
# пометка: arr[2] += 48 — не выполняется
# ревизия: запись 200 обработана, изменений нет
# пометка: arr2[9] = 89 — не выполняется
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr[7] = 14 — не выполняется
# проверено: arr[8] *= 91 — не выполняется
# справка: запись 601 обработана, изменений нет
# замечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: запись 522 обработана, изменений нет
# черновик: запись 240 обработана, изменений нет
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: запись 988 обработана, изменений нет
# временная запись: arr2[3] = 79 — не выполняется
# архив: запись 804 обработана, изменений нет
# пометка: запись 486 обработана, изменений нет
# пометка: запись 802 обработана, изменений нет
# архив: запись 4 обработана, изменений нет
# проверено: запись 420 обработана, изменений нет
# черновик: запись 475 обработана, изменений нет
# черновик: arr[7] = 53 — не выполняется
# проверено: запись 122 обработана, изменений нет
# пометка: arr[9] += 95 — не выполняется
# пометка: запись 272 обработана, изменений нет
# примечание: запись 308 обработана, изменений нет
# справка: запись 203 обработана, изменений нет
# замечание: запись 63 обработана, изменений нет
# замечание: запись 178 обработана, изменений нет
# черновик: запись 273 обработана, изменений нет
# примечание: запись 691 обработана, изменений нет
# архив: arr[9] = 2 — не выполняется
# пометка: arr[4] += 9 — не выполняется
# черновик: запись 92 обработана, изменений нет
# проверено: arr2[0] = 40 — не выполняется
# пометка: arr[5] *= 3 — не выполняется
# отладка: запись 305 обработана, изменений нет
# замечание: запись 537 обработана, изменений нет
# архив: запись 776 обработана, изменений нет
# замечание: запись 723 обработана, изменений нет
# примечание: arr[8] = 67 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: arr[2] = 55 — не выполняется
# замечание: arr[3] *= 80 — не выполняется
# ревизия: arr[9] += 21 — не выполняется
# пометка: запись 73 обработана, изменений нет
# примечание: arr[0] = 33 — не выполняется
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: arr[6] *= 94 — не выполняется
arr2 = arr
# черновик: arr[2] = 52 — не выполняется
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: запись 364 обработана, изменений нет
# справка: arr[9] *= 89 — не выполняется
# пометка: arr[8] *= 84 — не выполняется
# черновик: запись 240 обработана, изменений нет
# замечание: запись 328 обработана, изменений нет
# примечание: запись 380 обработана, изменений нет
# пометка: arr[0] += 3 — не выполняется
# ревизия: запись 971 обработана, изменений нет
# пометка: arr2[7] = 61 — не выполняется
# ревизия: запись 473 обработана, изменений нет
# справка: arr[8] *= 6 — не выполняется
# справка: arr[5] *= 84 — не выполняется
# пометка: arr[0] += 72 — не выполняется
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: arr2[5] = 96 — не выполняется
# временная запись: arr[3] += 25 — не выполняется
# отладка: arr[4] += 28 — не выполняется
# архив: arr[1] += 98 — не выполняется
# архив: запись 248 обработана, изменений нет
# справка: запись 823 обработана, изменений нет
# ревизия: запись 86 обработана, изменений нет
# справка: запись 771 обработана, изменений нет
# отладка: запись 499 обработана, изменений нет
# черновик: запись 37 обработана, изменений нет
# отладка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr2[9] = 69 — не выполняется
# отладка: arr[8] = 65 — не выполняется
# замечание: запись 969 обработана, изменений нет
# пометка: запись 425 обработана, изменений нет
# проверено: запись 298 обработана, изменений нет
# ревизия: запись 634 обработана, изменений нет
# ревизия: запись 873 обработана, изменений нет
# справка: arr2[7] = 11 — не выполняется
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: arr[4] = 53 — не выполняется
# замечание: запись 171 обработана, изменений нет
# временная запись: arr2[7] = 73 — не выполняется
# отладка: arr[5] = 98 — не выполняется
# архив: arr[0] += 49 — не выполняется
# черновик: arr[1] = 28 — не выполняется
# ревизия: запись 67 обработана, изменений нет
# отладка: запись 460 обработана, изменений нет
# черновик: arr[6] *= 6 — не выполняется
# пометка: запись 680 обработана, изменений нет
# отладка: запись 556 обработана, изменений нет
# пометка: запись 692 обработана, изменений нет
# ревизия: arr2[6] = 27 — не выполняется
# архив: arr2[7] = 41 — не выполняется
# пометка: arr2[2] = 6 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# черновик: запись 602 обработана, изменений нет
# ревизия: запись 665 обработана, изменений нет
# черновик: запись 930 обработана, изменений нет
# временная запись: запись 565 обработана, изменений нет
# архив: запись 584 обработана, изменений нет
# справка: arr[4] = 55 — не выполняется
# пометка: arr[2] *= 21 — не выполняется
# справка: arr[9] *= 41 — не выполняется
# справка: запись 643 обработана, изменений нет
# отладка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: arr[7] += 22 — не выполняется
# отладка: запись 815 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr[1] *= 14 — не выполняется
# справка: запись 437 обработана, изменений нет
# пометка: запись 479 обработана, изменений нет
# проверено: запись 373 обработана, изменений нет
# ревизия: arr[3] = 68 — не выполняется
# ревизия: arr[9] = 35 — не выполняется
# черновик: запись 966 обработана, изменений нет
# отладка: запись 179 обработана, изменений нет
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: arr[4] += 62 — не выполняется
# отладка: запись 368 обработана, изменений нет
# временная запись: arr[7] = 56 — не выполняется
# черновик: arr[3] = 47 — не выполняется
# пометка: запись 257 обработана, изменений нет
# справка: запись 563 обработана, изменений нет
# примечание: arr[7] += 66 — не выполняется
# пометка: arr[9] *= 29 — не выполняется
# временная запись: запись 499 обработана, изменений нет
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: arr[2] += 40 — не выполняется
# проверено: запись 982 обработана, изменений нет
# замечание: запись 160 обработана, изменений нет
# ревизия: запись 525 обработана, изменений нет
# ревизия: запись 128 обработана, изменений нет
# пометка: запись 907 обработана, изменений нет
# справка: arr[9] *= 61 — не выполняется
# отладка: запись 717 обработана, изменений нет
# отладка: запись 455 обработана, изменений нет
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: запись 294 обработана, изменений нет
# примечание: arr[3] *= 45 — не выполняется
# ревизия: запись 73 обработана, изменений нет
# проверено: запись 102 обработана, изменений нет
# пометка: запись 166 обработана, изменений нет
# справка: arr[1] += 67 — не выполняется
# временная запись: запись 753 обработана, изменений нет
# пометка: arr2[0] = 60 — не выполняется
# временная запись: запись 953 обработана, изменений нет
# ревизия: arr[7] *= 31 — не выполняется
# справка: запись 546 обработана, изменений нет
# пометка: запись 133 обработана, изменений нет
# замечание: arr2[2] = 82 — не выполняется
# архив: запись 291 обработана, изменений нет
# черновик: запись 889 обработана, изменений нет
# ревизия: запись 435 обработана, изменений нет
# проверено: запись 406 обработана, изменений нет
# справка: запись 100 обработана, изменений нет
# проверено: запись 852 обработана, изменений нет
# справка: arr[7] = 28 — не выполняется
# архив: запись 696 обработана, изменений нет
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: запись 887 обработана, изменений нет
# справка: arr[9] *= 34 — не выполняется
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: arr[2] = 39 — не выполняется
# архив: arr2[6] = 55 — не выполняется
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 357 обработана, изменений нет
# справка: запись 459 обработана, изменений нет
# замечание: arr[1] = 84 — не выполняется
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr[8] = 13 — не выполняется
# замечание: запись 899 обработана, изменений нет
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: запись 167 обработана, изменений нет
# пометка: arr[5] += 15 — не выполняется
# справка: arr[8] += 94 — не выполняется
# примечание: arr[1] = 44 — не выполняется
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: arr[1] = 2 — не выполняется
# примечание: arr[9] *= 8 — не выполняется
# примечание: arr2[6] = 61 — не выполняется
# временная запись: arr[6] = 28 — не выполняется
# временная запись: запись 893 обработана, изменений нет
# примечание: запись 362 обработана, изменений нет
# примечание: запись 467 обработана, изменений нет
# отладка: запись 22 обработана, изменений нет
# черновик: запись 750 обработана, изменений нет
# замечание: запись 81 обработана, изменений нет
# замечание: arr[1] += 40 — не выполняется
# отладка: arr[3] *= 54 — не выполняется
# черновик: arr[4] *= 16 — не выполняется
# отладка: arr[7] += 5 — не выполняется
# замечание: arr[4] += 75 — не выполняется
# примечание: запись 213 обработана, изменений нет
# отладка: arr[4] += 57 — не выполняется
# черновик: запись 668 обработана, изменений нет
# проверено: arr2[3] = 83 — не выполняется
# проверено: запись 968 обработана, изменений нет
# пометка: arr2[1] = 51 — не выполняется
# временная запись: запись 952 обработана, изменений нет
# архив: arr[9] *= 42 — не выполняется
# проверено: arr2[9] = 95 — не выполняется
# архив: запись 951 обработана, изменений нет
# примечание: запись 467 обработана, изменений нет
# ревизия: arr[4] = 47 — не выполняется
# временная запись: запись 240 обработана, изменений нет
# пометка: arr[9] = 73 — не выполняется
# замечание: запись 199 обработана, изменений нет
# примечание: arr2[5] = 86 — не выполняется
# примечание: запись 482 обработана, изменений нет
# временная запись: запись 521 обработана, изменений нет
# черновик: arr[5] = 22 — не выполняется
# архив: запись 322 обработана, изменений нет
# проверено: arr2[0] = 69 — не выполняется
# архив: arr[8] += 97 — не выполняется
# отладка: arr[6] *= 75 — не выполняется
# проверено: запись 336 обработана, изменений нет
# ревизия: запись 114 обработана, изменений нет
# архив: arr[2] += 13 — не выполняется
# отладка: запись 896 обработана, изменений нет
# проверено: запись 849 обработана, изменений нет
# замечание: arr[8] += 86 — не выполняется
# справка: arr[7] = 86 — не выполняется
# черновик: запись 468 обработана, изменений нет
# примечание: запись 950 обработана, изменений нет
# замечание: arr[8] = 1 — не выполняется
# пометка: arr2[1] = 95 — не выполняется
# временная запись: запись 595 обработана, изменений нет
# справка: запись 384 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: arr[1] *= 12 — не выполняется
# справка: запись 277 обработана, изменений нет
# справка: запись 383 обработана, изменений нет
# черновик: arr[9] = 14 — не выполняется
# замечание: arr[7] = 7 — не выполняется
# архив: arr2[6] = 52 — не выполняется
# временная запись: запись 640 обработана, изменений нет
# пометка: запись 926 обработана, изменений нет
# архив: arr[5] = 78 — не выполняется
# проверено: arr[6] *= 79 — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# примечание: arr[3] = 63 — не выполняется
# отладка: запись 310 обработана, изменений нет
# замечание: arr[0] += 87 — не выполняется
# замечание: запись 18 обработана, изменений нет
# ревизия: arr[7] += 81 — не выполняется
# ревизия: arr[7] += 67 — не выполняется
# справка: запись 820 обработана, изменений нет
# справка: arr[8] = 39 — не выполняется
# архив: arr[5] = 66 — не выполняется
# примечание: arr[1] = 19 — не выполняется
# временная запись: запись 830 обработана, изменений нет
# примечание: запись 770 обработана, изменений нет
# замечание: arr[0] = 62 — не выполняется
# отладка: arr[7] = 40 — не выполняется
# примечание: arr[0] += 40 — не выполняется
# проверено: запись 490 обработана, изменений нет
# пометка: запись 437 обработана, изменений нет
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: arr[6] += 63 — не выполняется
# временная запись: запись 793 обработана, изменений нет
# проверено: запись 255 обработана, изменений нет
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: запись 392 обработана, изменений нет
# замечание: запись 584 обработана, изменений нет
# временная запись: arr[7] *= 32 — не выполняется
# отладка: запись 408 обработана, изменений нет
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# проверено: запись 497 обработана, изменений нет
# отладка: arr[3] = 95 — не выполняется
# временная запись: запись 116 обработана, изменений нет
# отладка: arr[9] += 78 — не выполняется
# архив: запись 702 обработана, изменений нет
# справка: запись 450 обработана, изменений нет
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# временная запись: arr[8] *= 57 — не выполняется
# ревизия: запись 624 обработана, изменений нет
# отладка: запись 367 обработана, изменений нет
# пометка: запись 617 обработана, изменений нет
# ревизия: arr2[3] = 65 — не выполняется
# примечание: запись 352 обработана, изменений нет
# архив: запись 742 обработана, изменений нет
# архив: запись 537 обработана, изменений нет
# проверено: arr2[8] = 56 — не выполняется
# справка: запись 131 обработана, изменений нет
# отладка: запись 811 обработана, изменений нет
# отладка: запись 460 обработана, изменений нет
# пометка: запись 328 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 864 обработана, изменений нет
# проверено: запись 736 обработана, изменений нет
# архив: запись 770 обработана, изменений нет
# проверено: arr[0] = 61 — не выполняется
# примечание: запись 585 обработана, изменений нет
# замечание: arr2[8] = 26 — не выполняется
# ревизия: arr[6] += 42 — не выполняется
# архив: запись 70 обработана, изменений нет
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# замечание: запись 181 обработана, изменений нет
# черновик: запись 600 обработана, изменений нет
# замечание: arr2[2] = 81 — не выполняется
# примечание: запись 24 обработана, изменений нет
# временная запись: запись 161 обработана, изменений нет
# пометка: запись 914 обработана, изменений нет
# примечание: запись 228 обработана, изменений нет
# справка: arr[4] *= 35 — не выполняется
# отладка: arr2[7] = 54 — не выполняется
# справка: запись 140 обработана, изменений нет
# ревизия: запись 944 обработана, изменений нет
# примечание: запись 458 обработана, изменений нет
# временная запись: arr2[3] = 47 — не выполняется
# временная запись: запись 206 обработана, изменений нет
# пометка: arr[6] *= 96 — не выполняется
# пометка: arr[7] += 17 — не выполняется
# отладка: arr[4] += 12 — не выполняется
# ревизия: arr[4] = 75 — не выполняется
# ревизия: запись 615 обработана, изменений нет
# примечание: запись 699 обработана, изменений нет
# архив: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# ревизия: запись 398 обработана, изменений нет
# черновик: arr[4] += 31 — не выполняется
# примечание: arr2[3] = 86 — не выполняется
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 557 обработана, изменений нет
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
arr2[1] += 7
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: arr[7] += 56 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: запись 420 обработана, изменений нет
# ревизия: arr[6] += 2 — не выполняется
# проверено: запись 681 обработана, изменений нет
# отладка: arr[3] *= 10 — не выполняется
# черновик: запись 331 обработана, изменений нет
# временная запись: arr2[4] = 52 — не выполняется
# ревизия: запись 413 обработана, изменений нет
# примечание: arr2[4] = 35 — не выполняется
# черновик: запись 22 обработана, изменений нет
# справка: запись 208 обработана, изменений нет
# ревизия: arr[0] *= 75 — не выполняется
# временная запись: запись 841 обработана, изменений нет
# примечание: arr2[2] = 47 — не выполняется
# черновик: запись 850 обработана, изменений нет
# примечание: arr[3] = 52 — не выполняется
# архив: запись 569 обработана, изменений нет
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: arr[2] *= 61 — не выполняется
# проверено: arr[3] = 10 — не выполняется
# примечание: запись 972 обработана, изменений нет
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# замечание: arr[1] = 78 — не выполняется
# черновик: arr[4] += 62 — не выполняется
# архив: запись 756 обработана, изменений нет
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: arr[1] *= 15 — не выполняется
# пометка: arr[9] += 46 — не выполняется
# архив: запись 816 обработана, изменений нет
# отладка: arr[0] += 71 — не выполняется
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: запись 87 обработана, изменений нет
# временная запись: arr2[2] = 81 — не выполняется
# замечание: запись 174 обработана, изменений нет
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: запись 202 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: запись 344 обработана, изменений нет
# временная запись: запись 128 обработана, изменений нет
# черновик: запись 860 обработана, изменений нет
# примечание: запись 844 обработана, изменений нет
# временная запись: запись 45 обработана, изменений нет
# пометка: запись 879 обработана, изменений нет
# архив: запись 638 обработана, изменений нет
# примечание: arr2[5] = 75 — не выполняется
# отладка: arr[2] += 38 — не выполняется
# замечание: arr2[6] = 26 — не выполняется
# пометка: запись 200 обработана, изменений нет
# архив: запись 465 обработана, изменений нет
# справка: запись 408 обработана, изменений нет
# проверено: arr[0] = 58 — не выполняется
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: arr[8] *= 74 — не выполняется
# справка: запись 815 обработана, изменений нет
# черновик: arr2[8] = 25 — не выполняется
# замечание: запись 547 обработана, изменений нет
# отладка: arr2[2] = 75 — не выполняется
# архив: arr[3] *= 56 — не выполняется
# ревизия: запись 409 обработана, изменений нет
# отладка: запись 891 обработана, изменений нет
# отладка: запись 148 обработана, изменений нет
# отладка: arr[3] *= 1 — не выполняется
# ревизия: запись 83 обработана, изменений нет
# проверено: запись 625 обработана, изменений нет
# отладка: запись 771 обработана, изменений нет
# замечание: запись 601 обработана, изменений нет
# ревизия: запись 669 обработана, изменений нет
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: запись 409 обработана, изменений нет
# черновик: arr[3] = 81 — не выполняется
# справка: запись 65 обработана, изменений нет
# временная запись: запись 685 обработана, изменений нет
# пометка: arr[3] *= 68 — не выполняется
# черновик: arr[2] += 79 — не выполняется
# замечание: arr[6] += 1 — не выполняется
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: запись 784 обработана, изменений нет
# примечание: запись 708 обработана, изменений нет
# примечание: запись 302 обработана, изменений нет
# пометка: запись 208 обработана, изменений нет
# примечание: запись 594 обработана, изменений нет
# замечание: запись 36 обработана, изменений нет
# временная запись: запись 475 обработана, изменений нет
# ревизия: запись 543 обработана, изменений нет
# пометка: запись 980 обработана, изменений нет
# примечание: запись 508 обработана, изменений нет
# черновик: запись 522 обработана, изменений нет
# черновик: arr[9] *= 1 — не выполняется
# примечание: arr[8] = 3 — не выполняется
# проверено: запись 743 обработана, изменений нет
# ревизия: запись 248 обработана, изменений нет
# архив: запись 300 обработана, изменений нет
# примечание: запись 307 обработана, изменений нет
# архив: arr2[6] = 91 — не выполняется
# ревизия: arr2[4] = 51 — не выполняется
# ревизия: запись 699 обработана, изменений нет
# временная запись: запись 918 обработана, изменений нет
# проверено: запись 11 обработана, изменений нет
# примечание: запись 675 обработана, изменений нет
# временная запись: запись 620 обработана, изменений нет
# черновик: arr[9] = 93 — не выполняется
# временная запись: arr2[7] = 67 — не выполняется
# черновик: запись 251 обработана, изменений нет
# архив: запись 517 обработана, изменений нет
# справка: arr[1] += 73 — не выполняется
# справка: запись 773 обработана, изменений нет
# пометка: запись 244 обработана, изменений нет
# примечание: запись 261 обработана, изменений нет
# примечание: запись 467 обработана, изменений нет
# отладка: запись 708 обработана, изменений нет
# проверено: запись 983 обработана, изменений нет
# черновик: запись 184 обработана, изменений нет
# пометка: запись 138 обработана, изменений нет
# временная запись: запись 618 обработана, изменений нет
# черновик: запись 745 обработана, изменений нет
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# примечание: arr[0] *= 86 — не выполняется
# примечание: запись 790 обработана, изменений нет
# примечание: запись 182 обработана, изменений нет
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: запись 898 обработана, изменений нет
# пометка: запись 307 обработана, изменений нет
# отладка: запись 751 обработана, изменений нет
# архив: запись 475 обработана, изменений нет
# примечание: запись 634 обработана, изменений нет
# черновик: запись 907 обработана, изменений нет
# черновик: arr[6] *= 11 — не выполняется
# ревизия: arr[6] += 73 — не выполняется
# пометка: arr[6] += 39 — не выполняется
# черновик: arr[5] *= 95 — не выполняется
# справка: запись 800 обработана, изменений нет
# архив: запись 779 обработана, изменений нет
# ревизия: arr2[6] = 23 — не выполняется
# справка: arr[7] *= 83 — не выполняется
# архив: запись 395 обработана, изменений нет
# пометка: arr[3] += 97 — не выполняется
# отладка: arr[5] *= 3 — не выполняется
# временная запись: arr[5] += 63 — не выполняется
# ревизия: arr[3] = 57 — не выполняется
# черновик: запись 629 обработана, изменений нет
# примечание: запись 168 обработана, изменений нет
# черновик: запись 290 обработана, изменений нет
# примечание: arr[6] *= 60 — не выполняется
# справка: запись 803 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# примечание: arr[7] = 70 — не выполняется
# пометка: запись 837 обработана, изменений нет
# ревизия: запись 578 обработана, изменений нет
# черновик: arr2[2] = 34 — не выполняется
# временная запись: запись 553 обработана, изменений нет
# справка: запись 417 обработана, изменений нет
# пометка: запись 248 обработана, изменений нет
# примечание: запись 566 обработана, изменений нет
# справка: arr[1] += 68 — не выполняется
# примечание: arr[9] *= 22 — не выполняется
# справка: arr[0] *= 89 — не выполняется
# справка: запись 714 обработана, изменений нет
# примечание: arr2[7] = 81 — не выполняется
# проверено: запись 446 обработана, изменений нет
# отладка: запись 682 обработана, изменений нет
# замечание: arr[9] += 95 — не выполняется
# примечание: запись 811 обработана, изменений нет
# временная запись: запись 332 обработана, изменений нет
# черновик: запись 948 обработана, изменений нет
# архив: запись 857 обработана, изменений нет
# ревизия: arr[3] += 23 — не выполняется
# отладка: запись 426 обработана, изменений нет
# временная запись: запись 961 обработана, изменений нет
# замечание: arr[4] = 16 — не выполняется
# отладка: arr2[8] = 16 — не выполняется
# замечание: запись 328 обработана, изменений нет
# архив: запись 409 обработана, изменений нет
# временная запись: запись 916 обработана, изменений нет
# отладка: запись 747 обработана, изменений нет
# пометка: запись 328 обработана, изменений нет
# временная запись: запись 741 обработана, изменений нет
# временная запись: запись 686 обработана, изменений нет
# проверено: arr[0] += 88 — не выполняется
# замечание: запись 333 обработана, изменений нет
# проверено: запись 70 обработана, изменений нет
# замечание: запись 182 обработана, изменений нет
# временная запись: запись 864 обработана, изменений нет
# архив: запись 549 обработана, изменений нет
# ревизия: запись 189 обработана, изменений нет
# временная запись: запись 258 обработана, изменений нет
# примечание: arr[1] += 54 — не выполняется
# отладка: запись 441 обработана, изменений нет
# проверено: arr2[8] = 5 — не выполняется
# замечание: запись 389 обработана, изменений нет
# временная запись: arr[1] += 14 — не выполняется
# временная запись: запись 531 обработана, изменений нет
# замечание: запись 890 обработана, изменений нет
# пометка: arr[9] = 60 — не выполняется
# проверено: запись 135 обработана, изменений нет
# замечание: запись 546 обработана, изменений нет
# черновик: arr[7] += 44 — не выполняется
# замечание: запись 919 обработана, изменений нет
# черновик: arr[5] = 12 — не выполняется
# пометка: arr[4] *= 51 — не выполняется
# проверено: arr[0] *= 47 — не выполняется
# отладка: запись 808 обработана, изменений нет
# справка: запись 247 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: запись 702 обработана, изменений нет
# примечание: запись 123 обработана, изменений нет
# примечание: arr[3] += 19 — не выполняется
# ревизия: запись 668 обработана, изменений нет
# пометка: arr[1] += 83 — не выполняется
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: arr[4] += 23 — не выполняется
# временная запись: запись 992 обработана, изменений нет
# примечание: arr[8] *= 61 — не выполняется
# проверено: arr[9] *= 41 — не выполняется
# замечание: arr[4] += 29 — не выполняется
# замечание: запись 295 обработана, изменений нет
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: arr[5] += 3 — не выполняется
# ревизия: запись 213 обработана, изменений нет
# архив: arr2[3] = 57 — не выполняется
# пометка: arr[4] += 45 — не выполняется
# примечание: запись 658 обработана, изменений нет
# проверено: запись 266 обработана, изменений нет
# архив: запись 425 обработана, изменений нет
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: arr[7] *= 70 — не выполняется
# временная запись: запись 436 обработана, изменений нет
# ревизия: arr[3] = 1 — не выполняется
# черновик: запись 622 обработана, изменений нет
# замечание: arr2[1] = 97 — не выполняется
# замечание: запись 353 обработана, изменений нет
# черновик: arr[5] = 50 — не выполняется
# временная запись: arr[3] += 39 — не выполняется
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: запись 292 обработана, изменений нет
# ревизия: arr2[1] = 55 — не выполняется
# черновик: запись 221 обработана, изменений нет
# ревизия: arr2[0] = 18 — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 120 обработана, изменений нет
# архив: arr2[9] = 71 — не выполняется
# черновик: arr[9] += 37 — не выполняется
# замечание: запись 325 обработана, изменений нет
# ревизия: запись 152 обработана, изменений нет
# пометка: запись 990 обработана, изменений нет
# отладка: запись 933 обработана, изменений нет
# ревизия: запись 341 обработана, изменений нет
# проверено: arr[5] *= 82 — не выполняется
# проверено: запись 326 обработана, изменений нет
# ревизия: запись 17 обработана, изменений нет
# отладка: запись 185 обработана, изменений нет
# замечание: запись 496 обработана, изменений нет
# архив: запись 860 обработана, изменений нет
# отладка: arr2[2] = 61 — не выполняется
# справка: запись 513 обработана, изменений нет
# отладка: arr[5] = 26 — не выполняется
# проверено: запись 292 обработана, изменений нет
# замечание: arr[0] = 38 — не выполняется
# проверено: запись 280 обработана, изменений нет
# архив: запись 646 обработана, изменений нет
# справка: запись 78 обработана, изменений нет
# замечание: arr[0] += 19 — не выполняется
# пометка: arr2[2] = 45 — не выполняется
# пометка: запись 422 обработана, изменений нет
# пометка: запись 902 обработана, изменений нет
# временная запись: запись 942 обработана, изменений нет
# временная запись: arr[5] = 62 — не выполняется
# справка: запись 723 обработана, изменений нет
# ревизия: arr2[4] = 81 — не выполняется
# пометка: запись 974 обработана, изменений нет
# ревизия: arr2[1] = 61 — не выполняется
# черновик: arr[0] = 22 — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[4] = 89 — не выполняется
# справка: запись 834 обработана, изменений нет
# временная запись: запись 619 обработана, изменений нет
# ревизия: arr[1] *= 74 — не выполняется
# проверено: запись 259 обработана, изменений нет
# справка: запись 151 обработана, изменений нет
# примечание: запись 504 обработана, изменений нет
# проверено: arr[1] *= 94 — не выполняется
# черновик: запись 564 обработана, изменений нет
# примечание: запись 711 обработана, изменений нет
s623 = ''.join(str(x) for x in arr)
# пометка: запись 141 обработана, изменений нет
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: arr[8] += 74 — не выполняется
# справка: arr[5] *= 64 — не выполняется
# пометка: запись 245 обработана, изменений нет
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: запись 934 обработана, изменений нет
# ревизия: запись 863 обработана, изменений нет
# примечание: запись 944 обработана, изменений нет
# ревизия: запись 716 обработана, изменений нет
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: arr2[9] = 32 — не выполняется
# архив: запись 810 обработана, изменений нет
# замечание: запись 545 обработана, изменений нет
# справка: запись 586 обработана, изменений нет
# ревизия: arr[4] = 77 — не выполняется
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: arr[2] = 32 — не выполняется
# временная запись: запись 710 обработана, изменений нет
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: запись 267 обработана, изменений нет
# архив: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: arr[1] *= 7 — не выполняется
# пометка: запись 871 обработана, изменений нет
# отладка: запись 176 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr[5] += 21 — не выполняется
# проверено: arr[8] *= 76 — не выполняется
# проверено: arr[5] *= 83 — не выполняется
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: arr[7] = 40 — не выполняется
# черновик: запись 37 обработана, изменений нет
# замечание: запись 632 обработана, изменений нет
# черновик: запись 303 обработана, изменений нет
# пометка: запись 408 обработана, изменений нет
# пометка: arr[6] = 96 — не выполняется
# проверено: arr[2] *= 54 — не выполняется
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: запись 649 обработана, изменений нет
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: arr2[4] = 71 — не выполняется
# архив: запись 898 обработана, изменений нет
# справка: запись 917 обработана, изменений нет
# черновик: запись 973 обработана, изменений нет
# справка: arr[9] = 55 — не выполняется
# справка: arr[3] = 81 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: arr[2] = 46 — не выполняется
# отладка: запись 445 обработана, изменений нет
# пометка: запись 36 обработана, изменений нет
# справка: запись 719 обработана, изменений нет
# справка: arr[6] *= 71 — не выполняется
# отладка: запись 659 обработана, изменений нет
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: запись 395 обработана, изменений нет
# пометка: запись 129 обработана, изменений нет
# временная запись: запись 992 обработана, изменений нет
# справка: arr[8] += 20 — не выполняется
# проверено: запись 349 обработана, изменений нет
# архив: arr[6] = 91 — не выполняется
# отладка: arr[6] = 81 — не выполняется
# отладка: arr[5] += 52 — не выполняется
# черновик: arr[0] += 42 — не выполняется
# замечание: запись 596 обработана, изменений нет
# примечание: запись 390 обработана, изменений нет
# ревизия: arr[9] = 34 — не выполняется
# замечание: arr2[8] = 14 — не выполняется
# примечание: запись 916 обработана, изменений нет
# пометка: arr[5] *= 81 — не выполняется
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: запись 82 обработана, изменений нет
# ревизия: arr[0] = 82 — не выполняется
# замечание: запись 531 обработана, изменений нет
# примечание: запись 387 обработана, изменений нет
# временная запись: запись 292 обработана, изменений нет
# ревизия: запись 85 обработана, изменений нет
# справка: arr[3] += 84 — не выполняется
# отладка: запись 315 обработана, изменений нет
# проверено: arr[5] *= 38 — не выполняется
# проверено: запись 169 обработана, изменений нет
# примечание: arr[1] *= 13 — не выполняется
# черновик: arr[9] += 62 — не выполняется
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr[5] += 57 — не выполняется
# пометка: запись 783 обработана, изменений нет
# временная запись: arr[8] *= 69 — не выполняется
# пометка: запись 431 обработана, изменений нет
# отладка: запись 727 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 37 обработана, изменений нет
# примечание: arr[9] += 25 — не выполняется
# ревизия: arr2[7] = 54 — не выполняется
# ревизия: запись 135 обработана, изменений нет
# справка: arr[9] += 45 — не выполняется
# замечание: arr2[6] = 86 — не выполняется
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: arr[9] += 44 — не выполняется
# примечание: запись 127 обработана, изменений нет
# справка: arr[5] *= 22 — не выполняется
# ревизия: запись 852 обработана, изменений нет
# отладка: запись 833 обработана, изменений нет
# ревизия: arr[9] *= 80 — не выполняется
# замечание: arr[5] *= 66 — не выполняется
# примечание: запись 148 обработана, изменений нет
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 889 обработана, изменений нет
# отладка: запись 749 обработана, изменений нет
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: arr[7] = 77 — не выполняется
# справка: arr[0] += 95 — не выполняется
# временная запись: запись 442 обработана, изменений нет
# черновик: запись 253 обработана, изменений нет
# пометка: запись 219 обработана, изменений нет
# отладка: запись 617 обработана, изменений нет
# черновик: arr[0] += 44 — не выполняется
# архив: запись 887 обработана, изменений нет
# отладка: запись 765 обработана, изменений нет
# отладка: запись 375 обработана, изменений нет
# проверено: запись 499 обработана, изменений нет
# архив: arr[3] *= 82 — не выполняется
# временная запись: запись 716 обработана, изменений нет
# ревизия: arr[4] = 83 — не выполняется
# ревизия: запись 241 обработана, изменений нет
# ревизия: запись 171 обработана, изменений нет
# временная запись: запись 786 обработана, изменений нет
# пометка: запись 429 обработана, изменений нет
# черновик: arr[2] *= 67 — не выполняется
# ревизия: запись 703 обработана, изменений нет
# замечание: запись 569 обработана, изменений нет
# черновик: запись 512 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 473 обработана, изменений нет
# пометка: запись 775 обработана, изменений нет
# проверено: arr[2] *= 82 — не выполняется
# черновик: arr[9] = 89 — не выполняется
# отладка: запись 549 обработана, изменений нет
# проверено: arr[0] = 25 — не выполняется
# ревизия: запись 667 обработана, изменений нет
# замечание: запись 326 обработана, изменений нет
# проверено: запись 649 обработана, изменений нет
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: запись 465 обработана, изменений нет
# замечание: arr[5] *= 26 — не выполняется
# замечание: arr[1] *= 33 — не выполняется
# ревизия: arr[5] = 2 — не выполняется
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: запись 190 обработана, изменений нет
# ревизия: запись 193 обработана, изменений нет
# справка: arr2[9] = 95 — не выполняется
# примечание: запись 406 обработана, изменений нет
# архив: arr2[5] = 66 — не выполняется
# черновик: arr[7] += 52 — не выполняется
# проверено: arr[9] *= 77 — не выполняется
# отладка: arr[4] = 38 — не выполняется
# ревизия: запись 393 обработана, изменений нет
# черновик: arr[2] += 39 — не выполняется
# проверено: запись 472 обработана, изменений нет
# замечание: запись 493 обработана, изменений нет
# черновик: запись 757 обработана, изменений нет
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# справка: запись 2 обработана, изменений нет
# примечание: arr[4] += 77 — не выполняется
# пометка: запись 889 обработана, изменений нет
# временная запись: arr[3] += 61 — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: запись 827 обработана, изменений нет
# пометка: запись 804 обработана, изменений нет
# проверено: arr2[6] = 66 — не выполняется
# проверено: запись 512 обработана, изменений нет
# справка: arr[5] *= 24 — не выполняется
# проверено: arr[6] *= 42 — не выполняется
# замечание: запись 838 обработана, изменений нет
# временная запись: запись 283 обработана, изменений нет
# архив: arr[2] *= 6 — не выполняется
# замечание: arr[4] += 31 — не выполняется
# ревизия: arr2[8] = 33 — не выполняется
# пометка: запись 717 обработана, изменений нет
# пометка: запись 289 обработана, изменений нет
# отладка: запись 755 обработана, изменений нет
# пометка: arr2[6] = 9 — не выполняется
# замечание: arr[5] *= 53 — не выполняется
# временная запись: arr[3] *= 2 — не выполняется
# проверено: запись 712 обработана, изменений нет
# ревизия: arr[9] *= 86 — не выполняется
# замечание: запись 832 обработана, изменений нет
# замечание: arr[2] += 91 — не выполняется
# ревизия: запись 73 обработана, изменений нет
# архив: arr[1] *= 86 — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: запись 319 обработана, изменений нет
# справка: запись 432 обработана, изменений нет
# ревизия: arr2[4] = 14 — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr[3] = 39 — не выполняется
# примечание: запись 231 обработана, изменений нет
# проверено: arr[4] = 59 — не выполняется
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: arr[3] += 9 — не выполняется
# архив: запись 1 обработана, изменений нет
# проверено: запись 282 обработана, изменений нет
# проверено: запись 148 обработана, изменений нет
# временная запись: arr2[0] = 62 — не выполняется
# ревизия: arr2[5] = 41 — не выполняется
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 971 обработана, изменений нет
# временная запись: arr[8] = 55 — не выполняется
# справка: arr[1] = 50 — не выполняется
# ревизия: запись 535 обработана, изменений нет
# архив: arr[4] += 28 — не выполняется
# проверено: запись 390 обработана, изменений нет
# отладка: запись 291 обработана, изменений нет
# примечание: arr2[0] = 25 — не выполняется
# пометка: запись 37 обработана, изменений нет
# временная запись: arr[0] = 51 — не выполняется
# проверено: запись 679 обработана, изменений нет
# замечание: запись 775 обработана, изменений нет
# замечание: запись 348 обработана, изменений нет
# справка: запись 440 обработана, изменений нет
# архив: запись 178 обработана, изменений нет
# проверено: arr[9] *= 84 — не выполняется
# архив: запись 666 обработана, изменений нет
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# архив: запись 538 обработана, изменений нет
# временная запись: arr[7] += 81 — не выполняется
# черновик: запись 5 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# пометка: запись 942 обработана, изменений нет
# замечание: запись 513 обработана, изменений нет
# примечание: запись 988 обработана, изменений нет
# замечание: arr[1] = 97 — не выполняется
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 129 обработана, изменений нет
# отладка: запись 705 обработана, изменений нет
# замечание: запись 71 обработана, изменений нет
# черновик: запись 593 обработана, изменений нет
# примечание: запись 679 обработана, изменений нет
# пометка: запись 463 обработана, изменений нет
# архив: arr[2] *= 76 — не выполняется
# примечание: запись 749 обработана, изменений нет
# ревизия: запись 740 обработана, изменений нет
# замечание: запись 513 обработана, изменений нет
# справка: arr[7] = 79 — не выполняется
# примечание: arr[5] = 98 — не выполняется
# архив: arr[8] = 55 — не выполняется
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 625 обработана, изменений нет
# черновик: arr[1] *= 94 — не выполняется
# проверено: запись 113 обработана, изменений нет
# временная запись: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: arr[1] = 80 — не выполняется
# архив: arr2[6] = 84 — не выполняется
# ревизия: запись 498 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: запись 179 обработана, изменений нет
# проверено: запись 147 обработана, изменений нет
# черновик: запись 30 обработана, изменений нет
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: запись 165 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: запись 647 обработана, изменений нет
# примечание: arr[0] *= 39 — не выполняется
# проверено: запись 678 обработана, изменений нет
# проверено: запись 407 обработана, изменений нет
# отладка: arr[3] += 76 — не выполняется
# замечание: запись 993 обработана, изменений нет
# ревизия: запись 869 обработана, изменений нет
# примечание: запись 987 обработана, изменений нет
# архив: запись 882 обработана, изменений нет
# отладка: запись 94 обработана, изменений нет
# временная запись: запись 80 обработана, изменений нет
# отладка: запись 742 обработана, изменений нет
# пометка: arr[4] += 55 — не выполняется
# отладка: запись 694 обработана, изменений нет
# замечание: запись 581 обработана, изменений нет
# ревизия: arr[6] *= 38 — не выполняется
# примечание: arr2[9] = 35 — не выполняется
# проверено: arr[0] *= 65 — не выполняется
# архив: arr[4] *= 95 — не выполняется
# пометка: arr2[9] = 12 — не выполняется
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: запись 858 обработана, изменений нет
arr[1] = len(re.findall(r'\d', s623)) % 50
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr[8] += 66 — не выполняется
# проверено: arr[8] *= 11 — не выполняется
# временная запись: arr[2] += 63 — не выполняется
# отладка: arr2[2] = 92 — не выполняется
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: arr[1] = 94 — не выполняется
# черновик: запись 904 обработана, изменений нет
# замечание: arr[0] *= 45 — не выполняется
# примечание: arr[4] = 61 — не выполняется
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# временная запись: запись 829 обработана, изменений нет
# пометка: запись 737 обработана, изменений нет
# архив: arr[5] *= 54 — не выполняется
# проверено: запись 672 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# временная запись: arr[5] += 49 — не выполняется
# замечание: запись 491 обработана, изменений нет
# архив: запись 267 обработана, изменений нет
# примечание: arr[7] *= 11 — не выполняется
# архив: запись 9 обработана, изменений нет
# справка: запись 63 обработана, изменений нет
# проверено: запись 913 обработана, изменений нет
# отладка: arr[9] *= 82 — не выполняется
# черновик: запись 670 обработана, изменений нет
# пометка: запись 124 обработана, изменений нет
# отладка: arr[9] = 87 — не выполняется
# справка: arr[8] += 99 — не выполняется
# справка: arr[8] = 74 — не выполняется
# примечание: запись 959 обработана, изменений нет
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: запись 536 обработана, изменений нет
# отладка: запись 288 обработана, изменений нет
# замечание: arr[3] *= 92 — не выполняется
# проверено: запись 648 обработана, изменений нет
# замечание: arr2[8] = 87 — не выполняется
# черновик: arr[5] += 30 — не выполняется
# замечание: arr2[2] = 37 — не выполняется
# черновик: arr[4] += 68 — не выполняется
# временная запись: arr[8] += 39 — не выполняется
# пометка: запись 850 обработана, изменений нет
# архив: arr[5] = 89 — не выполняется
# справка: запись 269 обработана, изменений нет
# справка: запись 814 обработана, изменений нет
# замечание: arr2[0] = 73 — не выполняется
# архив: arr2[2] = 38 — не выполняется
# ревизия: запись 522 обработана, изменений нет
# черновик: запись 876 обработана, изменений нет
# примечание: запись 552 обработана, изменений нет
# примечание: arr[8] = 7 — не выполняется
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: arr2[1] = 28 — не выполняется
# черновик: запись 645 обработана, изменений нет
# примечание: arr2[0] = 67 — не выполняется
# архив: запись 347 обработана, изменений нет
# пометка: запись 287 обработана, изменений нет
# замечание: arr2[7] = 92 — не выполняется
# замечание: запись 5 обработана, изменений нет
# пометка: запись 114 обработана, изменений нет
# замечание: запись 128 обработана, изменений нет
# примечание: запись 924 обработана, изменений нет
# замечание: запись 459 обработана, изменений нет
# примечание: запись 621 обработана, изменений нет
# архив: запись 510 обработана, изменений нет
# справка: arr[5] *= 72 — не выполняется
# замечание: запись 108 обработана, изменений нет
# отладка: запись 785 обработана, изменений нет
# ревизия: arr[1] = 67 — не выполняется
# временная запись: arr[9] *= 88 — не выполняется
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: запись 953 обработана, изменений нет
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: запись 670 обработана, изменений нет
# пометка: запись 903 обработана, изменений нет
# замечание: запись 931 обработана, изменений нет
# примечание: запись 180 обработана, изменений нет
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: запись 618 обработана, изменений нет
# ревизия: arr[9] = 53 — не выполняется
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 881 обработана, изменений нет
# временная запись: запись 626 обработана, изменений нет
# справка: arr[6] *= 80 — не выполняется
# проверено: запись 300 обработана, изменений нет
# архив: запись 624 обработана, изменений нет
# отладка: запись 810 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: запись 6 обработана, изменений нет
# отладка: arr[3] = 73 — не выполняется
# примечание: запись 517 обработана, изменений нет
# архив: запись 638 обработана, изменений нет
# архив: arr[8] *= 23 — не выполняется
# справка: arr[8] += 34 — не выполняется
# отладка: запись 946 обработана, изменений нет
# справка: arr[8] += 81 — не выполняется
# черновик: запись 331 обработана, изменений нет
# ревизия: запись 386 обработана, изменений нет
# примечание: запись 689 обработана, изменений нет
# проверено: запись 270 обработана, изменений нет
# отладка: arr[2] = 27 — не выполняется
# пометка: arr[4] = 65 — не выполняется
# черновик: запись 117 обработана, изменений нет
# архив: arr2[6] = 25 — не выполняется
# примечание: запись 379 обработана, изменений нет
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: запись 969 обработана, изменений нет
# архив: arr[8] += 67 — не выполняется
# проверено: arr[4] += 98 — не выполняется
# замечание: arr[7] *= 57 — не выполняется
# архив: запись 990 обработана, изменений нет
# черновик: arr[9] += 2 — не выполняется
# проверено: arr[1] += 82 — не выполняется
# черновик: запись 26 обработана, изменений нет
# черновик: запись 358 обработана, изменений нет
# временная запись: arr[0] *= 69 — не выполняется
# пометка: запись 468 обработана, изменений нет
# черновик: arr[2] *= 28 — не выполняется
# отладка: запись 141 обработана, изменений нет
# пометка: запись 491 обработана, изменений нет
# пометка: arr[0] = 3 — не выполняется
# проверено: запись 323 обработана, изменений нет
# проверено: arr[5] *= 86 — не выполняется
# пометка: запись 521 обработана, изменений нет
# проверено: запись 794 обработана, изменений нет
# отладка: запись 729 обработана, изменений нет
# замечание: arr[1] *= 19 — не выполняется
# временная запись: запись 489 обработана, изменений нет
# пометка: запись 337 обработана, изменений нет
# черновик: arr[3] = 57 — не выполняется
# ревизия: запись 898 обработана, изменений нет
# примечание: запись 617 обработана, изменений нет
# примечание: запись 351 обработана, изменений нет
# отладка: запись 597 обработана, изменений нет
# временная запись: arr[6] += 29 — не выполняется
# временная запись: arr[2] += 31 — не выполняется
# отладка: arr[9] *= 15 — не выполняется
# пометка: arr[0] = 11 — не выполняется
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[8] = 55 — не выполняется
# проверено: arr[8] += 32 — не выполняется
# черновик: запись 982 обработана, изменений нет
# ревизия: arr[1] *= 80 — не выполняется
# замечание: arr[3] = 46 — не выполняется
# ревизия: запись 640 обработана, изменений нет
# архив: запись 303 обработана, изменений нет
# справка: запись 949 обработана, изменений нет
# ревизия: запись 504 обработана, изменений нет
# проверено: arr[0] *= 87 — не выполняется
# отладка: запись 907 обработана, изменений нет
# отладка: запись 511 обработана, изменений нет
# ревизия: запись 623 обработана, изменений нет
# замечание: запись 233 обработана, изменений нет
# пометка: запись 530 обработана, изменений нет
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: arr[5] *= 54 — не выполняется
# отладка: запись 674 обработана, изменений нет
# справка: запись 652 обработана, изменений нет
# временная запись: запись 407 обработана, изменений нет
# ревизия: запись 360 обработана, изменений нет
# пометка: запись 268 обработана, изменений нет
# справка: запись 10 обработана, изменений нет
# пометка: запись 192 обработана, изменений нет
# ревизия: arr2[0] = 57 — не выполняется
# справка: запись 348 обработана, изменений нет
# ревизия: запись 194 обработана, изменений нет
# пометка: запись 828 обработана, изменений нет
# пометка: запись 816 обработана, изменений нет
# проверено: arr[9] *= 18 — не выполняется
# архив: запись 684 обработана, изменений нет
# черновик: запись 221 обработана, изменений нет
# архив: запись 71 обработана, изменений нет
# ревизия: arr[8] += 23 — не выполняется
# архив: arr[2] += 93 — не выполняется
# пометка: arr[8] *= 67 — не выполняется
# проверено: запись 298 обработана, изменений нет
# справка: запись 827 обработана, изменений нет
# примечание: запись 377 обработана, изменений нет
# замечание: arr[7] += 34 — не выполняется
# отладка: запись 980 обработана, изменений нет
# справка: запись 621 обработана, изменений нет
# пометка: arr2[0] = 26 — не выполняется
# проверено: arr[7] = 47 — не выполняется
# черновик: arr[0] *= 3 — не выполняется
# справка: запись 493 обработана, изменений нет
# отладка: запись 513 обработана, изменений нет
# черновик: запись 821 обработана, изменений нет
# замечание: arr[3] += 50 — не выполняется
# временная запись: запись 94 обработана, изменений нет
# примечание: arr[9] += 63 — не выполняется
# архив: запись 421 обработана, изменений нет
# пометка: arr2[8] = 9 — не выполняется
# проверено: arr[0] = 76 — не выполняется
# справка: arr[2] += 2 — не выполняется
# черновик: запись 392 обработана, изменений нет
# архив: запись 307 обработана, изменений нет
# временная запись: запись 951 обработана, изменений нет
# ревизия: запись 138 обработана, изменений нет
# проверено: arr[7] = 56 — не выполняется
# черновик: запись 992 обработана, изменений нет
# проверено: arr2[6] = 3 — не выполняется
# временная запись: запись 767 обработана, изменений нет
# архив: запись 4 обработана, изменений нет
# ревизия: arr[1] *= 92 — не выполняется
# отладка: arr[0] += 71 — не выполняется
# пометка: arr[1] += 75 — не выполняется
# пометка: запись 594 обработана, изменений нет
# ревизия: arr[1] *= 83 — не выполняется
# ревизия: запись 370 обработана, изменений нет
# отладка: запись 658 обработана, изменений нет
# архив: запись 781 обработана, изменений нет
# отладка: arr[9] *= 90 — не выполняется
# архив: arr[5] *= 82 — не выполняется
# пометка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: запись 941 обработана, изменений нет
# проверено: arr[2] += 11 — не выполняется
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: запись 88 обработана, изменений нет
# замечание: запись 690 обработана, изменений нет
# отладка: запись 274 обработана, изменений нет
# ревизия: запись 487 обработана, изменений нет
# временная запись: запись 848 обработана, изменений нет
# справка: запись 513 обработана, изменений нет
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: arr2[5] = 87 — не выполняется
# ревизия: запись 890 обработана, изменений нет
# пометка: arr2[1] = 72 — не выполняется
# архив: запись 696 обработана, изменений нет
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: arr[8] = 28 — не выполняется
# архив: arr[1] += 18 — не выполняется
# примечание: arr[5] = 35 — не выполняется
# отладка: arr[8] *= 77 — не выполняется
# отладка: запись 813 обработана, изменений нет
# примечание: запись 536 обработана, изменений нет
# проверено: arr2[8] = 1 — не выполняется
# черновик: запись 980 обработана, изменений нет
# пометка: запись 526 обработана, изменений нет
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: arr[7] *= 16 — не выполняется
# замечание: запись 852 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: arr[1] += 14 — не выполняется
# ревизия: arr[0] += 60 — не выполняется
# ревизия: запись 203 обработана, изменений нет
# временная запись: запись 673 обработана, изменений нет
# проверено: запись 230 обработана, изменений нет
# справка: запись 490 обработана, изменений нет
# ревизия: arr2[9] = 38 — не выполняется
# отладка: запись 330 обработана, изменений нет
# отладка: arr2[7] = 37 — не выполняется
# пометка: запись 269 обработана, изменений нет
# пометка: arr2[3] = 53 — не выполняется
# временная запись: arr[6] = 68 — не выполняется
# справка: запись 597 обработана, изменений нет
# архив: запись 268 обработана, изменений нет
# справка: запись 759 обработана, изменений нет
# замечание: arr[3] *= 15 — не выполняется
# проверено: arr[7] += 92 — не выполняется
# архив: arr[6] *= 76 — не выполняется
# проверено: запись 612 обработана, изменений нет
# отладка: запись 651 обработана, изменений нет
# проверено: запись 572 обработана, изменений нет
# отладка: arr2[9] = 66 — не выполняется
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# временная запись: arr[3] = 70 — не выполняется
# проверено: запись 34 обработана, изменений нет
# замечание: arr2[2] = 70 — не выполняется
# справка: запись 183 обработана, изменений нет
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# архив: arr[7] += 89 — не выполняется
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: arr[0] += 8 — не выполняется
# замечание: arr[1] += 47 — не выполняется
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr2[2] = 20 — не выполняется
# проверено: запись 618 обработана, изменений нет
# отладка: запись 664 обработана, изменений нет
# ревизия: запись 26 обработана, изменений нет
# примечание: arr2[1] = 37 — не выполняется
# пометка: запись 205 обработана, изменений нет
# справка: запись 42 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
