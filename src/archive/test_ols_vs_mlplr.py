from doubleml import DoubleMLData

from doubleml import DoubleMLPLR

from sklearn.ensemble import RandomForestRegressor

from sklearn.base import clone

import numpy as np

from scipy import stats

import matplotlib.pyplot as plt

import seaborn as sns


from doubleml.datasets import make_plr_CCDDHNR2018


face_colors = sns.color_palette('pastel')

edge_colors = sns.color_palette('dark')

np.random.seed(1111)

def non_orth_score(y, d, l_hat, m_hat, g_hat, smpls):
     u_hat = y - g_hat
     psi_a = -np.multiply(d, d)
     psi_b = np.multiply(d, u_hat)
     return psi_a, psi_b
 
ml_l = RandomForestRegressor(n_estimators=132, max_features=12, max_depth=5, min_samples_leaf=1)

ml_m = RandomForestRegressor(n_estimators=378, max_features=20, max_depth=3, min_samples_leaf=6)

ml_g = clone(ml_l)    

import numpy as np

from doubleml.datasets import make_plr_CCDDHNR2018

np.random.seed(1234)

n_rep = 1000

n_obs = 500

n_vars = 20

alpha = 0.5

data = list()

for i_rep in range(n_rep):
    (x, y, d) = make_plr_CCDDHNR2018(alpha=alpha, n_obs=n_obs, dim_x=n_vars, return_type='array')
    data.append((x, y, d))


import numpy as np

np.random.seed(5555)

theta_dml_po = np.array([0.52876386, 0.49642496, 0.43558359, 0.48385395, 0.48263744, 0.52065436, 0.51196604, 0.45457013, 0.50236773, 0.60226776, 0.49525345, 0.54929426, 0.55862886, 0.38668434, 0.46651516, 0.48596014, 0.51073451, 0.47555414, 0.56154942, 0.47712008, 0.45908535, 0.47905771, 0.48119272, 0.5039857 , 0.48549178, 0.44828651, 0.51054201, 0.46965257, 0.44771795, 0.54639828, 0.47136481, 0.58571177, 0.40240481, 0.43868009, 0.46543858, 0.44238912, 0.45729493, 0.55316233, 0.49995909, 0.53027911, 0.48020647, 0.5191674 , 0.49229801, 0.37730406, 0.57612697, 0.50399902, 0.49049858, 0.51522608, 0.51054361, 0.4939221 , 0.48388515, 0.49238434, 0.47703209, 0.51727205, 0.61579399, 0.38693497, 0.55208572, 0.48290605, 0.49366392, 0.47067728, 0.48912104, 0.54112017, 0.54915469, 0.48089163, 0.56427844, 0.46009275, 0.4533473 , 0.49321491, 0.56400308, 0.56071557, 0.4453699 , 0.48957027, 0.50948593, 0.47617631, 0.49869524, 0.52732989, 0.49713173, 0.51638675, 0.5039623 , 0.53514343, 0.52809171, 0.48055678, 0.47932269, 0.44400388, 0.43742165, 0.5035799 , 0.55940179, 0.52720895, 0.48898253, 0.55113636, 0.38530608, 0.48212808, 0.56255715, 0.4681873 , 0.50922832, 0.49665169, 0.49973596, 0.50728249, 0.61919775, 0.52980464, 0.4470384 , 0.54970346, 0.4603203 , 0.50395574, 0.44948521, 0.59271845, 0.54610525, 0.48435625, 0.40402406, 0.49332716, 0.42959719, 0.48235224, 0.44457234, 0.43675964, 0.48845666, 0.450786  , 0.47855978, 0.4693617 , 0.48993912, 0.41517384, 0.45892182, 0.60196253, 0.50991046, 0.47869586, 0.39594481, 0.58051677, 0.45685749, 0.45722061, 0.48340673, 0.46928463, 0.50811054, 0.48351326, 0.49455325, 0.47532855, 0.45697168, 0.52864274, 0.51573529, 0.55979803, 0.46307792, 0.49551285, 0.4476106 , 0.47584211, 0.57505639, 0.47849081, 0.5754398 , 0.42882078, 0.43890495, 0.5712939 , 0.45392337, 0.54160894, 0.56094447, 0.47404527, 0.47344072, 0.46475148, 0.5162425 , 0.61577599, 0.48598403, 0.4706845 , 0.43193503, 0.60009588, 0.49000676, 0.46722224, 0.53955457, 0.53058301, 0.49350086, 0.46416138, 0.56295573, 0.50641166, 0.50500217, 0.53639407, 0.53181473, 0.49211802, 0.5137631 , 0.47101913, 0.50834946, 0.49639409, 0.49041039, 0.58718694, 0.5053225 , 0.47442319, 0.45029834, 0.53214004, 0.48029363, 0.43771314, 0.41368455, 0.43934673, 0.42540836, 0.45567131, 0.56527456, 0.50845985, 0.44297089, 0.48081024, 0.49390183, 0.41014255, 0.50802301, 0.4715952 , 0.44784824, 0.52827121, 0.461319  , 0.4661665 , 0.52817668, 0.5774521 , 0.4795185 , 0.51946092, 0.45543458, 0.45574257, 0.48488458, 0.48652943, 0.54044881, 0.55479025, 0.44064243, 0.62755167, 0.42012331, 0.40775333, 0.43366019, 0.52687122, 0.4517471 , 0.53678077, 0.50584558, 0.53164932, 0.53117984, 0.50457742, 0.46806336, 0.52904057, 0.5307677 , 0.54662925, 0.45878668, 0.49324139, 0.574838  , 0.49137141, 0.58268286, 0.5924264 , 0.62310897, 0.47510252, 0.53649311, 0.57229299, 0.51940046, 0.45731134, 0.54884152, 0.48680994, 0.51510473, 0.50922301, 0.51677578, 0.57780639, 0.46816876, 0.44897551, 0.51321758, 0.49450203, 0.42872782, 0.4365137 , 0.4628704 , 0.51399804, 0.55653439, 0.52488332, 0.50600489, 0.48140922, 0.50350718, 0.52654721, 0.59815318, 0.42071962, 0.47969415, 0.4456638 , 0.50211309, 0.49697633, 0.44140602, 0.53930818, 0.47884922, 0.56818849, 0.51630494, 0.48671292, 0.46039979, 0.41114395, 0.39818181, 0.56145449, 0.542998  , 0.50010098, 0.49820963, 0.49003785, 0.50305572, 0.51292791, 0.48933725, 0.45660895, 0.49518821, 0.4849069 , 0.52267743, 0.50392296, 0.58937665, 0.47274635, 0.56755771, 0.38741005, 0.52876889, 0.49566081, 0.50850134, 0.44876604, 0.43954376, 0.49462121, 0.59135693, 0.46764294, 0.58774516, 0.42427519, 0.55204104, 0.59373285, 0.5284568 , 0.47892363, 0.46903582, 0.473618  , 0.53177486, 0.42273053, 0.52900964, 0.48550055, 0.50106813, 0.45814701, 0.4722137 , 0.57443057, 0.39776497, 0.49355381, 0.36617604, 0.50976518, 0.52859814, 0.52722868, 0.61453654, 0.45841707, 0.55796556, 0.55644629, 0.5506848 , 0.4702159 , 0.50083763, 0.53856514, 0.46602807, 0.45204245, 0.48080515, 0.56483207, 0.45621144, 0.42794771, 0.4860271 , 0.46479965, 0.56875931, 0.41161689, 0.55302315, 0.47271993, 0.50344196, 0.42053369, 0.52565845, 0.43104463, 0.43922226, 0.57412536, 0.49435242, 0.5598449 , 0.50651293, 0.4243393 , 0.47901695, 0.42058707, 0.5476903 , 0.50184981, 0.57823467, 0.55067893, 0.51966014, 0.41881399, 0.44953744, 0.46319358, 0.53574066, 0.45995912, 0.47871539, 0.56629616, 0.57595297, 0.53876127, 0.53609786, 0.52978709, 0.53875115, 0.50847709, 0.4149362 , 0.45260669, 0.4536379 , 0.50394067, 0.42305305, 0.41424964, 0.52197237, 0.48594172, 0.45009749, 0.4307894 , 0.56654082, 0.52400503, 0.50464779, 0.4883888 , 0.50770741, 0.44965224, 0.48960481, 0.55406137, 0.47093463, 0.46452095, 0.47775312, 0.49929834, 0.54082214, 0.48656641, 0.44160879, 0.40050997, 0.43967865, 0.52972772, 0.48894344, 0.48959524, 0.45225519, 0.46477098, 0.45606621, 0.5488213 , 0.42547011, 0.49625743, 0.4865749 , 0.49467224, 0.55015222, 0.50699681, 0.47427151, 0.43403248, 0.42448919, 0.39432154, 0.48474832, 0.47421844, 0.53084624, 0.46260523, 0.45064904, 0.48230808, 0.43730637, 0.51041301, 0.47497435, 0.49359209, 0.5595982 , 0.48490794, 0.51250825, 0.46914558, 0.53257313, 0.54640514, 0.55242549, 0.43611181, 0.52036922, 0.47315045, 0.46437181, 0.47094681, 0.52144713, 0.52288962, 0.52173716, 0.48752518, 0.52550315, 0.50604638, 0.52228596, 0.49880518, 0.50851985, 0.4465949 , 0.52202277, 0.50249377, 0.46322091, 0.54615601, 0.50894802, 0.43345177, 0.50954733, 0.46339897, 0.46015515, 0.50448629, 0.51675392, 0.50012197, 0.44156462, 0.53740657, 0.53755287, 0.51308269, 0.49421434, 0.39274913, 0.47712458, 0.47812675, 0.49915688, 0.53254843, 0.42084555, 0.46325418, 0.49086648, 0.45019164, 0.5420365 , 0.47279955, 0.48982796, 0.54589376, 0.51462906, 0.43819174, 0.50983744, 0.50781399, 0.49550464, 0.46471352, 0.58631511, 0.47949176, 0.51639418, 0.39523312, 0.51664646, 0.5448198 , 0.56068757, 0.50757457, 0.47905316, 0.45066173, 0.41872143, 0.50006031, 0.42814963, 0.57007205, 0.58021248, 0.53159123, 0.42537663, 0.51625064, 0.47240764, 0.55303755, 0.48823736, 0.42029816, 0.53373549, 0.44653573, 0.43038701, 0.57681681, 0.54862281, 0.5205924 , 0.50207264, 0.46024779, 0.49115148, 0.58285578, 0.56729901, 0.50065596, 0.43313588, 0.53193915, 0.46971056, 0.46810937, 0.54975298, 0.44592224, 0.5273588 , 0.45066263, 0.49022521, 0.54036456, 0.52373846, 0.51341698, 0.49523554, 0.46354297, 0.59599975, 0.46715844, 0.51362765, 0.49410913, 0.44571835, 0.41595069, 0.57077163, 0.52015364, 0.48560591, 0.48571281, 0.51829923, 0.47543306, 0.46038   , 0.44356321, 0.46757523, 0.46887054, 0.55768647, 0.54349256, 0.47197434, 0.51751084, 0.51076787, 0.49690516, 0.60331217, 0.57465717, 0.51494865, 0.56925775, 0.47763364, 0.46602821, 0.5187162 , 0.45728743, 0.37034602, 0.54977269, 0.4680515 , 0.5262913 , 0.48117704, 0.49573812, 0.54406615, 0.51055961, 0.56104265, 0.5592123 , 0.41827194, 0.527187  , 0.46604307, 0.49439706, 0.53662182, 0.51926518, 0.47345959, 0.47946106, 0.47932428, 0.59299744, 0.42411538, 0.60750248, 0.56642017, 0.51119554, 0.49077337, 0.40567808, 0.37298201, 0.48068202, 0.4868408 , 0.41970932, 0.45143647, 0.48364514, 0.4945257 , 0.49703403, 0.49551628, 0.44295951, 0.53390061, 0.43523352, 0.49790843, 0.53749617, 0.46802951, 0.55940488, 0.52359195, 0.50736714, 0.52502905, 0.48463152, 0.45303868, 0.57144172, 0.48372973, 0.53818662, 0.50312434, 0.50637077, 0.54574298, 0.41583979, 0.48042361, 0.50222613, 0.47359926, 0.56900104, 0.46190257, 0.55831883, 0.56685946, 0.52938241, 0.49552427, 0.50929147, 0.47357133, 0.49662637, 0.4343192 , 0.53597924, 0.53930657, 0.53026288, 0.4861995 , 0.61926515, 0.52733928, 0.45598938, 0.53494507, 0.52942118, 0.47078208, 0.53457652, 0.48507914, 0.50306637, 0.4412238 , 0.59952472, 0.52392443, 0.54847361, 0.56994672, 0.41829809, 0.5814434 , 0.45197069, 0.55710022, 0.45528081, 0.5401222 , 0.54592327, 0.44220664, 0.47673524, 0.52873844, 0.4829449 , 0.48515887, 0.54134607, 0.450466  , 0.54837702, 0.47590747, 0.57199309, 0.58851981, 0.47132444, 0.44442932, 0.56183549, 0.48979552, 0.51374854, 0.41011541, 0.46538776, 0.58606274, 0.51545543, 0.54614756, 0.4506355 , 0.49779654, 0.443503  , 0.47268849, 0.4504294 , 0.39291152, 0.54669478, 0.54779101, 0.47582864, 0.50894455, 0.51927094, 0.49861091, 0.59310058, 0.45429373, 0.48678437, 0.50288586, 0.48069622, 0.52760912, 0.5118683 , 0.60196906, 0.4282119 , 0.51393524, 0.5106446 , 0.53389979, 0.53176284, 0.47265592, 0.45720696, 0.42943445, 0.54018803, 0.43633861, 0.51280376, 0.42495233, 0.48423667, 0.53328973, 0.51377185, 0.45810269, 0.49723702, 0.403323  , 0.56444141, 0.51351277, 0.47767768, 0.51641341, 0.4966969 , 0.42828877, 0.55426548, 0.53245294, 0.48623397, 0.42692114, 0.50321609, 0.53440262, 0.54244648, 0.51299351, 0.43263567, 0.47331176, 0.48165027, 0.51232191, 0.55445258, 0.54323231, 0.50930401, 0.50153814, 0.54471426, 0.53923209, 0.47315923, 0.43551507, 0.55701856, 0.55112787, 0.50850312, 0.49295049, 0.47247679, 0.58057907, 0.52169959, 0.51034787, 0.42896117, 0.55294684, 0.52292619, 0.42976747, 0.4706387 , 0.46060276, 0.60014024, 0.51666398, 0.51434187, 0.49136887, 0.61065831, 0.38513663, 0.56736394, 0.54790665, 0.44434231, 0.48441654, 0.57945827, 0.53637528, 0.47735573, 0.52615155, 0.51504026, 0.4641185 , 0.50871316, 0.56002337, 0.4707652 , 0.42641551, 0.48532868, 0.48351299, 0.47063727, 0.46747184, 0.42279864, 0.46458271, 0.51786366, 0.51228997, 0.5033719 , 0.48058348, 0.40904451, 0.43758533, 0.44100579, 0.57999117, 0.4925471 , 0.47551867, 0.5286477 , 0.46000318, 0.5637859 , 0.59928435, 0.48360782, 0.4771193 , 0.53749157, 0.45664404, 0.58401153, 0.46197167, 0.50154002, 0.54169984, 0.47225318, 0.50535922, 0.46600936, 0.48476778, 0.45769416, 0.49335976, 0.47891549, 0.47997919, 0.45763229, 0.53670601, 0.45686323, 0.56551689, 0.59629776, 0.47251306, 0.48778836, 0.56468832, 0.48890077, 0.52307882, 0.53440244, 0.50813894, 0.4428279 , 0.52356287, 0.47703679, 0.60258583, 0.4108778 , 0.54088935, 0.53795036, 0.44628152, 0.48215627, 0.44107261, 0.45252552, 0.46111263, 0.50135487, 0.55187685, 0.51325235, 0.51514277, 0.5680781 , 0.48667023, 0.48555444, 0.45070021, 0.39405688, 0.48145638, 0.54777308, 0.57570516, 0.55441856, 0.58127967, 0.47059829, 0.55769376, 0.52569789, 0.47112601, 0.5010574 , 0.35419379, 0.57555654, 0.47210866, 0.50287819, 0.4258165 , 0.56729575, 0.45470128, 0.55061083, 0.46312785, 0.51492596, 0.51134206, 0.48960366, 0.57966146, 0.37426146, 0.51913096, 0.51783745, 0.51242465, 0.45738121, 0.51659558, 0.48073267, 0.45818103, 0.52604388, 0.53847543, 0.46773059, 0.44172535, 0.43433353, 0.43758119, 0.52672775, 0.50251892, 0.57854698, 0.5175629 , 0.4611426 , 0.52172734, 0.45272314, 0.51589939, 0.43278818, 0.53944443, 0.53054068, 0.49185357, 0.42120363, 0.577586  , 0.52179469, 0.51180071, 0.55495018, 0.42470079, 0.54284353, 0.50912782, 0.43475174, 0.52285215, 0.53892128, 0.46787949, 0.53336718, 0.46930669, 0.45339336, 0.49623817, 0.4311819 , 0.55982476, 0.38516919, 0.49657255, 0.55963216, 0.47214567, 0.5240232 , 0.43767568, 0.46480375, 0.57115072, 0.49141717, 0.49789593, 0.46457368, 0.46656324, 0.55545586, 0.63923336, 0.46879923, 0.45622937, 0.42976341, 0.51129408, 0.49839078, 0.5164966 , 0.57959171, 0.45868351, 0.54262484, 0.49203866, 0.42105985, 0.60347606, 0.55442278, 0.51974864, 0.55806284, 0.56181645, 0.54627102, 0.50413101, 0.48039105, 0.46379635, 0.58390471, 0.5377935 , 0.41095458, 0.42925395, 0.42520725, 0.4893355 , 0.48419668, 0.51066485, 0.46864138, 0.59308306, 0.54484266, 0.4790423 , 0.48557658, 0.43889655, 0.50258992, 0.50661835, 0.45562128, 0.47451614, 0.50141995, 0.52912567, 0.48534654, 0.50892843, 0.43341213, 0.54916986, 0.52695849, 0.47247929, 0.46517683, 0.55822228, 0.43617081, 0.54370429, 0.45345871, 0.4418124 , 0.45103698, 0.3915015 , 0.51655919, 0.51625817, 0.4902453 , 0.47138125, 0.50868646, 0.53437357, 0.5563727 , 0.4870521 , 0.47828182, 0.44788723, 0.48242661, 0.58646635, 0.52495117, 0.53766765, 0.51010016, 0.47590069, 0.49285749, 0.33303451, 0.58635962, 0.47230682, 0.46693197, 0.53479744, 0.49730085, 0.4686777 , 0.52578667])

se_dml_po = np.array([0.04366143, 0.04632413, 0.03934783, 0.04376407, 0.04776953, 0.04294894, 0.0493605 , 0.05057076, 0.04993363, 0.04528385, 0.04716893, 0.04316392, 0.03844692, 0.04002265, 0.04364729, 0.04180496, 0.04915626, 0.04444379, 0.04258075, 0.04642707, 0.0453024 , 0.05041915, 0.04495728, 0.04627783, 0.04774967, 0.03613853, 0.04456387, 0.0428944 , 0.04773842, 0.04278792, 0.03998002, 0.04199909, 0.04050232, 0.04279711, 0.04826966, 0.04232603, 0.04629067, 0.04520752, 0.04292975, 0.04775048, 0.04387756, 0.04303141, 0.04699689, 0.04426411, 0.04174037, 0.0450418 , 0.04357423, 0.04296971, 0.04115976, 0.04803088, 0.0440271 , 0.03910127, 0.04188743, 0.0461947 , 0.04445704, 0.04758127, 0.04105246, 0.04229529, 0.04348393, 0.03940532, 0.04691201, 0.04712129, 0.04532333, 0.04198115, 0.04467275, 0.0456634 , 0.04796472, 0.04080751, 0.04541844, 0.04754002, 0.04303026, 0.03978123, 0.04099255, 0.04866286, 0.04067465, 0.04196374, 0.04548078, 0.04779556, 0.04321585, 0.04544103, 0.04639701, 0.04444337, 0.04158797, 0.04212771, 0.04294366, 0.04862461, 0.03713917, 0.04505446, 0.04856092, 0.04640594, 0.04342124, 0.04298389, 0.04025997, 0.04828067, 0.04270125, 0.04275123, 0.04282572, 0.04353543, 0.04703092, 0.04467834, 0.04520262, 0.04597939, 0.04693617, 0.04535161, 0.04437884, 0.04265513, 0.04768799, 0.04478721, 0.04296025, 0.04637604, 0.0487638 , 0.04499217, 0.04168946, 0.0439831 , 0.04748039, 0.05013583, 0.05015454, 0.04192372, 0.04506462, 0.04632873, 0.04833074, 0.04748367, 0.04152701, 0.04165487, 0.04654159, 0.04765364, 0.04452404, 0.04139589, 0.0442406 , 0.0457696 , 0.04844991, 0.04943656, 0.04777142, 0.03825993, 0.04597716, 0.04874836, 0.04776631, 0.04595611, 0.0458343 , 0.0428256 , 0.04534578, 0.0448361 , 0.042015  , 0.04811913, 0.0448321 , 0.04292421, 0.03894937, 0.04272008, 0.04455543, 0.03876354, 0.04314453, 0.04628697, 0.04603369, 0.04497386, 0.04267185, 0.04019239, 0.0422623 , 0.04053257, 0.04286978, 0.04745838, 0.04552007, 0.04932073, 0.04500954, 0.04000683, 0.0472705 , 0.04828826, 0.04341315, 0.0464942 , 0.04558246, 0.04395118, 0.04105528, 0.04638659, 0.04586976, 0.04029563, 0.04217629, 0.04204087, 0.04093607, 0.04969833, 0.04664773, 0.04504618, 0.03758201, 0.0452988 , 0.04503191, 0.04843537, 0.04914253, 0.04435506, 0.0368011 , 0.05420537, 0.04624779, 0.04433298, 0.05062355, 0.0447908 , 0.04379796, 0.04982575, 0.04793812, 0.0467464 , 0.0506507 , 0.04515699, 0.04629882, 0.04103533, 0.04999819, 0.04301357, 0.04669165, 0.04087331, 0.04158373, 0.0439232 , 0.04715809, 0.04692125, 0.04897129, 0.04748409, 0.04625044, 0.04551256, 0.04820112, 0.04693338, 0.04282482, 0.04321722, 0.04492408, 0.04680481, 0.04651601, 0.04297949, 0.04045679, 0.04618816, 0.0493394 , 0.03985102, 0.05072911, 0.04725812, 0.0481278 , 0.04495275, 0.04530795, 0.04074308, 0.04334787, 0.04071895, 0.04912917, 0.03774198, 0.04314333, 0.04086531, 0.04824108, 0.04406156, 0.04409377, 0.04891328, 0.0500406 , 0.04516683, 0.0414013 , 0.04620527, 0.04709315, 0.04822646, 0.04682268, 0.05036133, 0.04125324, 0.0461525 , 0.04235533, 0.04557972, 0.04499424, 0.04816397, 0.042596  , 0.04261622, 0.04148597, 0.046121  , 0.04583109, 0.04317212, 0.04462103, 0.04028714, 0.04365713, 0.04248785, 0.0467333 , 0.04079037, 0.04934807, 0.04507899, 0.04644339, 0.04587939, 0.04737139, 0.04552572, 0.04947069, 0.04414528, 0.04099972, 0.04527949, 0.04627014, 0.04386254, 0.04570415, 0.04411444, 0.04289963, 0.04525811, 0.0474116 , 0.04547358, 0.05100277, 0.04175249, 0.0485154 , 0.04771437, 0.04406015, 0.04622295, 0.039592  , 0.04335127, 0.04427896, 0.0393652 , 0.04025816, 0.04790163, 0.04682166, 0.04510704, 0.04299321, 0.0476545 , 0.0473511 , 0.04064169, 0.04439331, 0.04040281, 0.04181763, 0.04290026, 0.04493665, 0.04679808, 0.04864147, 0.04560976, 0.05244334, 0.05009814, 0.04916519, 0.04749958, 0.04397354, 0.04772573, 0.04904464, 0.04965606, 0.04217941, 0.04897094, 0.04123459, 0.0432386 , 0.04709203, 0.04826865, 0.04435245, 0.04306565, 0.04210565, 0.04290201, 0.04805011, 0.04584127, 0.04447501, 0.04654913, 0.04310199, 0.03854194, 0.04580982, 0.04767768, 0.04875136, 0.05074004, 0.04464792, 0.03933025, 0.04077989, 0.04167724, 0.04390614, 0.04570174, 0.04538323, 0.04332988, 0.04665934, 0.04842956, 0.03863581, 0.04017111, 0.04204172, 0.04213322, 0.04268302, 0.04363571, 0.04629439, 0.04024711, 0.04315797, 0.04541346, 0.04428588, 0.03936651, 0.04484814, 0.049777  , 0.04682585, 0.04265238, 0.05493733, 0.04141143, 0.04255895, 0.04297288, 0.04319185, 0.04368864, 0.04448444, 0.04807221, 0.04451277, 0.04842245, 0.03945935, 0.04650975, 0.04165787, 0.04001618, 0.04819221, 0.04239392, 0.04135269, 0.04276419, 0.04041064, 0.04346972, 0.04214591, 0.04530573, 0.04295206, 0.04447011, 0.0476322 , 0.04297454, 0.04802991, 0.04303747, 0.03914079, 0.04454937, 0.04833492, 0.04789917, 0.04606072, 0.04715249, 0.04573149, 0.04279117, 0.04254376, 0.0403669 , 0.05619312, 0.04938559, 0.04313127, 0.04490884, 0.04155294, 0.04682644, 0.04952157, 0.04256427, 0.04280082, 0.04634973, 0.04157787, 0.04059484, 0.04625132, 0.04861964, 0.0456383 , 0.0428753 , 0.0455957 , 0.04186756, 0.0464355 , 0.04185124, 0.04173826, 0.0410638 , 0.04593701, 0.04863952, 0.04531707, 0.04692063, 0.04615908, 0.04105317, 0.049331  , 0.04502511, 0.04493834, 0.04664758, 0.04615444, 0.04554463, 0.04199733, 0.04431206, 0.04118765, 0.04591012, 0.05045064, 0.04158319, 0.04429355, 0.04223113, 0.03969192, 0.0436478 , 0.05076127, 0.04303168, 0.0415556 , 0.04470683, 0.04511164, 0.04486504, 0.04502342, 0.04492337, 0.04252807, 0.0495405 , 0.04566507, 0.04596565, 0.0449505 , 0.04786531, 0.04569081, 0.04213937, 0.05005629, 0.0434723 , 0.04626321, 0.04364834, 0.04566388, 0.04713147, 0.04182015, 0.04457914, 0.04805054, 0.05225486, 0.0474002 , 0.0409488 , 0.04760028, 0.04486234, 0.05135251, 0.04853203, 0.04888681, 0.04967928, 0.04514113, 0.04408134, 0.04518277, 0.04647372, 0.04210594, 0.04183561, 0.04759757, 0.04638927, 0.04695067, 0.04202962, 0.04183168, 0.04637013, 0.04551546, 0.05082791, 0.04615458, 0.04567446, 0.04877952, 0.03922464, 0.03864079, 0.04345652, 0.04472654, 0.04329195, 0.04336706, 0.04380224, 0.0436433 , 0.04703133, 0.04542158, 0.04070404, 0.043123  , 0.04304618, 0.04756028, 0.04466588, 0.04008962, 0.04416704, 0.047083  , 0.04343354, 0.04328825, 0.04128289, 0.04797098, 0.04484212, 0.04503446, 0.04188074, 0.04671925, 0.04465078, 0.04874003, 0.04494375, 0.04625267, 0.04066548, 0.04330019, 0.03913068, 0.05079306, 0.04596748, 0.04518592, 0.04711726, 0.04508213, 0.03804182, 0.04560625, 0.042082  , 0.05198356, 0.04671626, 0.04238704, 0.04577586, 0.04322268, 0.04775087, 0.04692211, 0.04132109, 0.04906609, 0.04861446, 0.04307522, 0.04761847, 0.0442623 , 0.04528084, 0.04601433, 0.04184879, 0.04013743, 0.04537962, 0.04560355, 0.04082902, 0.04771007, 0.04810656, 0.04181141, 0.04363583, 0.04545695, 0.04517319, 0.04270835, 0.04530133, 0.04461901, 0.04362228, 0.04520353, 0.04039833, 0.04185737, 0.03957646, 0.04536973, 0.04023931, 0.04685081, 0.04439482, 0.03921729, 0.04959055, 0.04746106, 0.04675399, 0.05214294, 0.0464757 , 0.04585351, 0.04133049, 0.05058726, 0.04815479, 0.04493285, 0.04227591, 0.04229086, 0.04359974, 0.04692625, 0.04852676, 0.04481415, 0.04475359, 0.04732867, 0.04378654, 0.04859246, 0.04766565, 0.05149647, 0.04758104, 0.04476619, 0.0447561 , 0.04652143, 0.04465528, 0.04485388, 0.04102461, 0.04152636, 0.04844676, 0.04338375, 0.04316988, 0.04247638, 0.03906722, 0.04504118, 0.04430981, 0.04747676, 0.0533095 , 0.04781572, 0.04675546, 0.04594965, 0.04523947, 0.04254596, 0.04441746, 0.04408057, 0.04147999, 0.04516373, 0.04318777, 0.04395332, 0.04136753, 0.04404612, 0.04481491, 0.04865378, 0.04253294, 0.04267905, 0.04477323, 0.04448586, 0.04958079, 0.04415501, 0.04776651, 0.04070179, 0.04699118, 0.04397997, 0.04592556, 0.04276607, 0.03956084, 0.04080207, 0.04035732, 0.0468081 , 0.04875999, 0.03868134, 0.04715079, 0.04108798, 0.0443913 , 0.04569703, 0.04387604, 0.04179464, 0.04015547, 0.0433569 , 0.04528929, 0.03860953, 0.04976271, 0.04108088, 0.04336586, 0.05090655, 0.04489043, 0.03832453, 0.0438332 , 0.04216618, 0.04244166, 0.04889756, 0.04376899, 0.04459088, 0.04060368, 0.04171002, 0.04291755, 0.04042948, 0.04301972, 0.04504935, 0.04075044, 0.04658386, 0.04667455, 0.04239227, 0.0454948 , 0.04395952, 0.04566263, 0.04644776, 0.0472576 , 0.04320539, 0.04367673, 0.04372062, 0.04109036, 0.04963561, 0.04485157, 0.04830976, 0.03934099, 0.04930203, 0.04521219, 0.04431363, 0.04630182, 0.04414541, 0.04679306, 0.04193693, 0.04414566, 0.04577935, 0.04780609, 0.04347577, 0.05090181, 0.04015752, 0.03947669, 0.04295765, 0.04977118, 0.05137322, 0.04235594, 0.04365023, 0.04671102, 0.04115597, 0.04226988, 0.04707771, 0.03925437, 0.04513961, 0.0465118 , 0.04131011, 0.04014652, 0.0512401 , 0.04836521, 0.0448319 , 0.04389894, 0.04354019, 0.04021803, 0.04309532, 0.04263222, 0.04396544, 0.04923313, 0.0477914 , 0.04328708, 0.04245669, 0.04302829, 0.04192883, 0.04812229, 0.04801755, 0.04761739, 0.04598512, 0.04248567, 0.04684313, 0.04273867, 0.03934617, 0.04554571, 0.04926563, 0.04315612, 0.05041068, 0.04821278, 0.04494212, 0.04427627, 0.04560213, 0.03987408, 0.04400685, 0.04709236, 0.04158083, 0.0447051 , 0.04390364, 0.04233113, 0.04103328, 0.0488311 , 0.04185222, 0.04171723, 0.04182328, 0.0444572 , 0.04489263, 0.04402228, 0.03943944, 0.04881562, 0.04686757, 0.04589471, 0.03900169, 0.04893455, 0.04732217, 0.04823214, 0.04237029, 0.04492963, 0.04876891, 0.04788519, 0.04728083, 0.05084502, 0.04555633, 0.05153353, 0.04245686, 0.0445393 , 0.04529056, 0.04805109, 0.03909855, 0.0441579 , 0.04009273, 0.04833389, 0.04335762, 0.0487235 , 0.04793003, 0.04744083, 0.04497436, 0.04439482, 0.04417169, 0.04487584, 0.04149336, 0.04581779, 0.04302379, 0.04730023, 0.04074397, 0.0426177 , 0.04144998, 0.04554913, 0.04398114, 0.04368888, 0.04684536, 0.04893886, 0.04441862, 0.04646384, 0.04373368, 0.04583414, 0.04424393, 0.04435307, 0.05151157, 0.04523948, 0.04624434, 0.04763616, 0.04429373, 0.04435428, 0.04066626, 0.04850437, 0.0440769 , 0.04807946, 0.04242926, 0.04600121, 0.04535562, 0.05036463, 0.04495395, 0.04966027, 0.04020707, 0.04710001, 0.03835692, 0.04706426, 0.04517028, 0.04060998, 0.04117483, 0.05759099, 0.05168384, 0.04488953, 0.04298455, 0.05004272, 0.0454869 , 0.0449041 , 0.04490075, 0.04452586, 0.04675966, 0.04110656, 0.04448455, 0.04590486, 0.04961628, 0.04045468, 0.05065138, 0.04290253, 0.04904711, 0.04510714, 0.04169845, 0.04017691, 0.04575501, 0.04605821, 0.04405548, 0.04664584, 0.0478982 , 0.04628937, 0.04424418, 0.04613777, 0.04578426, 0.04725448, 0.04645413, 0.04135783, 0.04062497, 0.04972194, 0.04393031, 0.04443315, 0.04687277, 0.04239731, 0.0421795 , 0.04737418, 0.04182724, 0.04215289, 0.04455361, 0.04328229, 0.03965512, 0.04787494, 0.04640227, 0.04050011, 0.04418661, 0.04282853, 0.05295413, 0.04282882, 0.04227624, 0.04621299, 0.04420618, 0.0464249 , 0.04677917, 0.0447752 , 0.04577487, 0.04751948, 0.04174396, 0.04717273, 0.04712549, 0.04967362, 0.04212043, 0.04126582, 0.0400929 , 0.04729312, 0.04916058, 0.04743923, 0.04674456, 0.0426739 , 0.04807577, 0.0471212 , 0.04660028, 0.04404454, 0.04386943, 0.04671481, 0.04770813, 0.04276558, 0.04236685, 0.04024044, 0.04031839, 0.04509778, 0.05081884, 0.0452145 , 0.04434399, 0.04777426, 0.04267024, 0.03933003, 0.04722241, 0.04739409, 0.05255036, 0.04003435, 0.04533648, 0.04412494, 0.04411879, 0.04261987, 0.04469745, 0.04263345, 0.04239181, 0.04201696, 0.04423246, 0.04341077, 0.04819775, 0.04691498, 0.04237232, 0.04410359, 0.04044761, 0.044337  , 0.04929771, 0.04925044, 0.04694016, 0.0438847 , 0.04710392, 0.0415846 , 0.0441434 , 0.04246665, 0.04861628, 0.04398318, 0.04258132, 0.04593046, 0.04446947, 0.04809013, 0.04357285, 0.04728308, 0.04466791, 0.04391723, 0.04725787, 0.04057481, 0.04136977, 0.05221815, 0.04425619, 0.04415679, 0.0404598 , 0.04464952, 0.04641681, 0.04791448, 0.04399596, 0.04606058, 0.04165912, 0.04747206, 0.04528619, 0.05164746, 0.04341658, 0.04389238, 0.04312489, 0.04597068, 0.04712426, 0.04022928, 0.04500399, 0.04459979, 0.04872266, 0.04756165, 0.04166714, 0.04580468, 0.04350212, 0.0425324])

for i_rep in range(1):
     (x, y, d) = data[i_rep]
     obj_dml_data = DoubleMLData.from_arrays(x, y, d)
     obj_dml_plr = DoubleMLPLR(obj_dml_data,
                               ml_l, ml_m,
                               n_folds=2,
                               score='partialling out')
     obj_dml_plr.fit()
     this_theta = obj_dml_plr.coef[0]
     this_se = obj_dml_plr.se[0]
     print(np.abs(theta_dml_po[i_rep] - this_theta))
     print(np.abs(se_dml_po[i_rep] - this_se))
     theta_dml_po[i_rep] = this_theta
     se_dml_po[i_rep] = this_se
 

plt.figure(constrained_layout=True);

ax = sns.histplot((theta_dml_po - alpha)/se_dml_po,
                   color=face_colors[2], edgecolor = edge_colors[2],
                   stat='density', bins=30, label='Double ML with cross-fitting');
 

ax.axvline(0., color='k');

xx = np.arange(-5, +5, 0.001)

yy = stats.norm.pdf(xx)

ax.plot(xx, yy, color='k', label='$\\mathcal{N}(0, 1)$');

ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0));

ax.set_xlim([-6., 6.]);

ax.set_xlabel('$(\hat{\\theta}_0 - \\theta_0)/\hat{\sigma}$');


# %% OLS
for i_rep in range(1):
     (x, y, d) = data[i_rep]
     obj_dml_data = DoubleMLData.from_arrays(x, y, d)
     obj_dml_plr = DoubleMLPLR(obj_dml_data,
                               ml_l, ml_m,
                               n_folds=2,
                               score='partialling out')
     obj_dml_plr.fit()
     this_theta = obj_dml_plr.coef[0]
     this_se = obj_dml_plr.se[0]
     print(np.abs(theta_dml_po[i_rep] - this_theta))
     print(np.abs(se_dml_po[i_rep] - this_se))
     theta_dml_po[i_rep] = this_theta
     se_dml_po[i_rep] = this_se
 

plt.figure(constrained_layout=True);

ax = sns.histplot((theta_dml_po - alpha)/se_dml_po,
                   color=face_colors[2], edgecolor = edge_colors[2],
                   stat='density', bins=30, label='Double ML with cross-fitting');
 

ax.axvline(0., color='k');

xx = np.arange(-5, +5, 0.001)

yy = stats.norm.pdf(xx)

ax.plot(xx, yy, color='k', label='$\\mathcal{N}(0, 1)$');

ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0));

ax.set_xlim([-6., 6.]);

ax.set_xlabel('$(\hat{\\theta}_0 - \\theta_0)/\hat{\sigma}$');



import pandas as pd

from statsmodels.sandbox.regression.gmm import  OLS

theta_ols_po = np.array([])
se_ols_po = np.array([])
for i_rep in range(n_rep):
     (x, y, d) = data[i_rep]
     data1 = pd.DataFrame(x,columns = ['x'+str(i) for i in range(x.shape[1])] )
     data1['y']=y
     data1['d']=d
     data1.loc[:,'const'] = 1
     exog = [i for i in data1.columns if i.lower().startswith('x')] + ['const'] 
     
     model_obj = OLS(endog=data1.loc[:,'y'], exog = data1.loc[:,['d']+exog])            
     
     model_obj_fitted=model_obj.fit()
     this_theta = model_obj_fitted.params[0]
     this_se = model_obj_fitted.cov_params().iloc[0,0]
     #print(np.abs(theta_dml_po[i_rep] - this_theta))
     #print(np.abs(se_dml_po[i_rep] - this_se))
     theta_ols_po = np.append(theta_ols_po,  this_theta)
     se_ols_po = np.append(se_ols_po, this_se)
 

plt.figure(constrained_layout=True);

ax = sns.histplot((theta_ols_po - alpha)/se_dml_po,
                   color=face_colors[0], edgecolor = edge_colors[0],
                   stat='density', bins=30, label='OLS');
 

ax.axvline(0., color='k');

xx = np.arange(-5, +5, 0.001)

yy = stats.norm.pdf(xx)

ax.plot(xx, yy, color='k', label='$\\mathcal{N}(0, 1)$');

ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0));

ax.set_xlim([-6., 6.]);

ax.set_xlabel('$(\hat{\\theta}_0 - \\theta_0)/\hat{\sigma}$');