from app import app
from models import db, Drug, Pharmacy

db.drop_all()
db.create_all()


def create_drugs():
    """Function for creating drugs for database"""
    drug_list = []
    for num in range(232):
        print(f'd{num} = (name="{TOP_200[num]}"", price={prices[num]})')


d0 = Drug(name="Lexapro", price=5)
d1 = Drug(name="Vicodin", price=65)
d2 = Drug(name="Prinivil", price=55)
d3 = Drug(name="Qbrelis", price=89)
d4 = Drug(name="Zocor", price=80)
d5 = Drug(name="Synthroid", price=7)
d6 = Drug(name="Amoxil", price=70)
d7 = Drug(name="Trimox", price=15)
d8 = Drug(name="Zithromax", price=69)
d9 = Drug(name="Microzide", price=8)
d10 = Drug(name="Aquazide", price=20)
d11 = Drug(name="Norvasc", price=66)
d12 = Drug(name="Xanax", price=43)
d13 = Drug(name="Glucophage", price=34)
d14 = Drug(name="Lipitor", price=22)
d15 = Drug(name="Prilosec", price=94)
d16 = Drug(name="Cipro", price=87)
d17 = Drug(name="Proquin", price=42)
d18 = Drug(name="Zofran", price=60)
d19 = Drug(name="Clozaril", price=34)
d20 = Drug(name="Lasix", price=70)
d21 = Drug(name="Levitra", price=25)
d22 = Drug(name="Sumycin", price=100)
d23 = Drug(name="Ala-Tet", price=19)
d24 = Drug(name="Brodspec", price=79)
d25 = Drug(name="Heparin Sodium", price=58)
d26 = Drug(name="Valcyte", price=46)
d27 = Drug(name="Lamictal", price=92)
d28 = Drug(name="Diflucan", price=23)
d29 = Drug(name="Tenormin", price=17)
d30 = Drug(name="Singulair", price=2)
d31 = Drug(name="Flonase Nasal Spray", price=79)
d32 = Drug(name="Zyloprim", price=73)
d33 = Drug(name="Fosamax", price=95)
d34 = Drug(name="Pepcid", price=24)
d35 = Drug(name="Omnicef", price=84)
d36 = Drug(name="Yaz", price=55)
d37 = Drug(name="Apresoline", price=76)
d38 = Drug(name="Cogentin", price=55)
d39 = Drug(name="Tussionex PennKinetic", price=75)
d40 = Drug(name="Paxil", price=84)
d41 = Drug(name="Ativan", price=43)
d42 = Drug(name="Pyridium", price=86)
d43 = Drug(name="Plaquenil", price=27)
d44 = Drug(name="Lidoderm", price=86)
d45 = Drug(name="Cataflam", price=35)
d46 = Drug(name="Rayos", price=18)
d47 = Drug(name="Deltasone", price=12)
d48 = Drug(name="Zetia", price=57)
d49 = Drug(name="Evista", price=86)
d50 = Drug(name="Dilantin", price=52)
d51 = Drug(name="Lovaza", price=65)
d52 = Drug(name="Zanaflex", price=66)
d53 = Drug(name="Hytrin", price=47)
d54 = Drug(name="Dyrenium", price=89)
d55 = Drug(name="Altace", price=38)
d56 = Drug(name="Pravachol", price=42)
d57 = Drug(name="Risperdal", price=16)
d58 = Drug(name="Lunesta", price=49)
d59 = Drug(name="Celebrex", price=83)
d60 = Drug(name="Premarin", price=56)
d61 = Drug(name="Avelox", price=10)
d62 = Drug(name="Aricept", price=83)
d63 = Drug(name="Macrobid", price=49)
d64 = Drug(name="Macrodantin", price=8)
d65 = Drug(name="Duragesic Skin Patch", price=84)
d66 = Drug(name="Imdur", price=35)
d67 = Drug(name="Prozac", price=95)
d68 = Drug(name="Sarafem", price=35)
d69 = Drug(name="Aristocort", price=85)
d70 = Drug(name="Suboxone", price=93)
d71 = Drug(name="Vyvanse", price=31)
d72 = Drug(name="Pamelor", price=48)
d73 = Drug(name="HumaLOG", price=57)
d74 = Drug(name="Depacon", price=82)
d75 = Drug(name="Depakote", price=37)
d76 = Drug(name="BetaSept", price=47)
d77 = Drug(name="ChloraPrep", price=47)
d78 = Drug(name="Bentyl", price=66)
d79 = Drug(name="Imitrex", price=45)
d80 = Drug(name="Protonix", price=89)
d81 = Drug(name="Lopressor", price=86)
d82 = Drug(name="Robitussen", price=92)
d83 = Drug(name="Valium", price=96)
d84 = Drug(name="Viagra", price=8)
d85 = Drug(name="Bactroban", price=26)
d86 = Drug(name="Januvia", price=78)
d87 = Drug(name="Reglan", price=39)
d88 = Drug(name="Relafen", price=46)
d89 = Drug(name="Keflex", price=37)
d90 = Drug(name="Effexor", price=66)
d91 = Drug(name="Boniva", price=75)
d92 = Drug(name="Zantac", price=72)
d93 = Drug(name="Ex-Lax", price=8)
d94 = Drug(name="Senna Lax", price=52)
d95 = Drug(name="NovoLog", price=25)
d96 = Drug(name="Bayer", price=49)
d97 = Drug(name="Ecotrin", price=101)
d98 = Drug(name="Bufferin", price=76)
d99 = Drug(name="Lioresal", price=22)
d100 = Drug(name="Flagyl", price=74)
d101 = Drug(name="Keppra", price=37)
d102 = Drug(name="Colcrys", price=71)
d103 = Drug(name="Mitigare", price=64)
d104 = Drug(name="Zyprexa", price=71)
d105 = Drug(name="Avodart", price=66)
d106 = Drug(name="TriCor", price=66)
d107 = Drug(name="Antara", price=35)
d108 = Drug(name="Cardura", price=23)
d109 = Drug(name="Aleve", price=6)
d110 = Drug(name="Aldactone", price=17)
d111 = Drug(name="Namenda", price=41)
d112 = Drug(name="Methadose", price=79)
d113 = Drug(name="Vasotec", price=11)
d114 = Drug(name="Epaned", price=54)
d115 = Drug(name="Tamiflu", price=85)
d116 = Drug(name="Requip", price=26)
d117 = Drug(name="PC Pen VK", price=29)
d118 = Drug(name="Pen V", price=14)
d119 = Drug(name="Strattera", price=31)
d120 = Drug(name="Ambien", price=80)
d121 = Drug(name="Advair", price=88)
d122 = Drug(name="Levaquin", price=97)
d123 = Drug(name="Tofranil", price=47)
d124 = Drug(name="Reclast", price=97)
d125 = Drug(name="Zometa", price=84)
d126 = Drug(name="Glucotrol", price=91)
d127 = Drug(name="Constulose", price=2)
d128 = Drug(name="AcipHex", price=73)
d129 = Drug(name="Otrexup", price=1)
d130 = Drug(name="Cleocin", price=10)
d131 = Drug(name="Tylenol", price=76)
d132 = Drug(name="Feosol", price=15)
d133 = Drug(name="Relpax", price=23)
d134 = Drug(name="Carbacot", price=96)
d135 = Drug(name="Robaxin", price=48)
d136 = Drug(name="DiaBeta", price=61)
d137 = Drug(name="Celexa", price=14)
d138 = Drug(name="Benicar", price=91)
d139 = Drug(name="Coreg", price=38)
d140 = Drug(name="Spiriva", price=60)
d141 = Drug(name="Xolair", price=93)
d142 = Drug(name="NitroStat Sublingual", price=55)
d143 = Drug(name="Eliquis", price=65)
d144 = Drug(name="Neurontin", price=57)
d145 = Drug(name="Enbrel", price=32)
d146 = Drug(name="Herceptin", price=12)
d147 = Drug(name="Atripla", price=82)
d148 = Drug(name="Xarelto", price=19)
d149 = Drug(name="Stalevo 50", price=83)
d150 = Drug(name="Fioricet", price=71)
d151 = Drug(name="Levemir", price=99)
d152 = Drug(name="Lovenox", price=26)
d153 = Drug(name="Ritalin", price=93)
d154 = Drug(name="Concerta", price=36)
d155 = Drug(name="Crestor", price=37)
d156 = Drug(name="Xgeva", price=1)
d157 = Drug(name="Prolia", price=90)
d158 = Drug(name="Pradaxa", price=46)
d159 = Drug(name="Sensipar", price=21)
d160 = Drug(name="Vesicare", price=4)
d161 = Drug(name="Haldol", price=81)
d162 = Drug(name="Ala-Cort", price=95)
d163 = Drug(name="HumuLIN", price=60)
d164 = Drug(name="Isentress", price=15)
d165 = Drug(name="Stelara", price=12)
d166 = Drug(name="Mobic", price=89)
d167 = Drug(name="Remicade", price=18)
d168 = Drug(name="Night Time", price=18)
d169 = Drug(name="Renvela", price=39)
d170 = Drug(name="Fragmin", price=44)
d171 = Drug(name="Zoloft", price=100)
d172 = Drug(name="Klonopin", price=17)
d173 = Drug(name="Avalide", price=83)
d174 = Drug(name="Ceftin", price=68)
d175 = Drug(name="Nizoral Topical", price=68)
d176 = Drug(name="Lyrica", price=90)
d177 = Drug(name="Nexium", price=56)
d178 = Drug(name="Combivent Respimat", price=15)
d179 = Drug(name="Niaspan", price=75)
d180 = Drug(name="Uroxatral", price=73)
d181 = Drug(name="Biaxin", price=61)
d182 = Drug(name="Zomig", price=74)
d183 = Drug(name="Invokana", price=81)
d184 = Drug(name="Saxenda", price=20)
d185 = Drug(name="Victoza", price=41)
d186 = Drug(name="Alimta", price=18)
d187 = Drug(name="Lotrisone", price=73)
d188 = Drug(name="Avastin", price=100)
d189 = Drug(name="Sovaldi", price=63)
d190 = Drug(name="Gilenya", price=8)
d191 = Drug(name="Epogen", price=37)
d192 = Drug(name="Seroquel", price=83)
d193 = Drug(name="Amaryl", price=44)
d194 = Drug(name="Percocet", price=87)
d195 = Drug(name="SandIMMUNE", price=2)
d196 = Drug(name="Neoral", price=43)
d197 = Drug(name="Lantus", price=53)
d198 = Drug(name="Cialis", price=50)
d199 = Drug(name="Elavil", price=72)
d200 = Drug(name="Vanatrip", price=87)
d201 = Drug(name="Lopid", price=1)
d202 = Drug(name="Flo-Pred", price=27)
d203 = Drug(name="Advil", price=99)
d204 = Drug(name="Aceon", price=92)
d205 = Drug(name="Desyrel", price=3)
d206 = Drug(name="Actos", price=22)
d207 = Drug(name="Proscar", price=81)
d208 = Drug(name="Inbrija", price=80)
d209 = Drug(name="Dopar", price=41)
d210 = Drug(name="Larodopa", price=21)
d211 = Drug(name="Actonel", price=37)
d212 = Drug(name="ProAir", price=41)
d213 = Drug(name="Ventolin", price=90)
d214 = Drug(name="Proventil", price=96)
d215 = Drug(name="Ultram", price=71)
d216 = Drug(name="Sonata", price=38)
d217 = Drug(name="Zebeta", price=57)
d218 = Drug(name="Zovirax", price=56)
d219 = Drug(name="Coumadin", price=67)
d220 = Drug(name="Luvox", price=59)
d221 = Drug(name="Plavix", price=37)
d222 = Drug(name="Vibramycin", price=2)
d223 = Drug(name="Adoxa", price=61)
d224 = Drug(name="Hyzaar", price=41)
d225 = Drug(name="Kytril", price=11)
d226 = Drug(name="Sancuso", price=28)
d227 = Drug(name="Restoril", price=37)
d228 = Drug(name="Prevacid", price=7)
d229 = Drug(name="Augmentin", price=55)
d230 = Drug(name="Mevacor", price=96)
d231 = Drug(name="Altoprev", price=9)

p1 = Pharmacy(name="CVS", address='580 Marketplace Dr. Bel Air, MD 21014')
p2 = Pharmacy(name="Walgreens", address='1927 Emmorton Rd, Bel Air, MD 21015')
p3 = Pharmacy(name="Walmart",
              address='401 Constant Friendship Blvd, Abingdon, MD 21009')
p4 = Pharmacy(name="Wegmans",
              address='21 Wegmans Boulevard, Abingdon, MD 21009')

db.session.add_all([d0,
                    d1,
                    d2,
                    d3,
                    d4,
                    d5,
                    d6,
                    d7,
                    d8,
                    d9,
                    d10,
                    d11,
                    d12,
                    d13,
                    d14,
                    d15,
                    d16,
                    d17,
                    d18,
                    d19,
                    d20,
                    d21,
                    d22,
                    d23,
                    d24,
                    d25,
                    d26,
                    d27,
                    d28,
                    d29,
                    d30,
                    d31,
                    d32,
                    d33,
                    d34,
                    d35,
                    d36,
                    d37,
                    d38,
                    d39,
                    d40,
                    d41,
                    d42,
                    d43,
                    d44,
                    d45,
                    d46,
                    d47,
                    d48,
                    d49,
                    d50,
                    d51,
                    d52,
                    d53,
                    d54,
                    d55,
                    d56,
                    d57,
                    d58,
                    d59,
                    d60,
                    d61,
                    d62,
                    d63,
                    d64,
                    d65,
                    d66,
                    d67,
                    d68,
                    d69,
                    d70,
                    d71,
                    d72,
                    d73,
                    d74,
                    d75,
                    d76,
                    d77,
                    d78,
                    d79,
                    d80,
                    d81,
                    d82,
                    d83,
                    d84,
                    d85,
                    d86,
                    d87,
                    d88,
                    d89,
                    d90,
                    d91,
                    d92,
                    d93,
                    d94,
                    d95,
                    d96,
                    d97,
                    d98,
                    d99,
                    d100,
                    d101,
                    d102,
                    d103,
                    d104,
                    d105,
                    d106,
                    d107,
                    d108,
                    d109,
                    d110,
                    d111,
                    d112,
                    d113,
                    d114,
                    d115,
                    d116,
                    d117,
                    d118,
                    d119,
                    d120,
                    d121,
                    d122,
                    d123,
                    d124,
                    d125,
                    d126,
                    d127,
                    d128,
                    d129,
                    d130,
                    d131,
                    d132,
                    d133,
                    d134,
                    d135,
                    d136,
                    d137,
                    d138,
                    d139,
                    d140,
                    d141,
                    d142,
                    d143,
                    d144,
                    d145,
                    d146,
                    d147,
                    d148,
                    d149,
                    d150,
                    d151,
                    d152,
                    d153,
                    d154,
                    d155,
                    d156,
                    d157,
                    d158,
                    d159,
                    d160,
                    d161,
                    d162,
                    d163,
                    d164,
                    d165,
                    d166,
                    d167,
                    d168,
                    d169,
                    d170,
                    d171,
                    d172,
                    d173,
                    d174,
                    d175,
                    d176,
                    d177,
                    d178,
                    d179,
                    d180,
                    d181,
                    d182,
                    d183,
                    d184,
                    d185,
                    d186,
                    d187,
                    d188,
                    d189,
                    d190,
                    d191,
                    d192,
                    d193,
                    d194,
                    d195,
                    d196,
                    d197,
                    d198,
                    d199,
                    d200,
                    d201,
                    d202,
                    d203,
                    d204,
                    d205,
                    d206,
                    d207,
                    d208,
                    d209,
                    d210,
                    d211,
                    d212,
                    d213,
                    d214,
                    d215,
                    d216,
                    d217,
                    d218,
                    d219,
                    d220,
                    d221,
                    d222,
                    d223,
                    d224,
                    d225,
                    d226,
                    d227,
                    d228,
                    d229,
                    d230,
                    d231])
db.session.add_all([p1, p2, p3, p4])
db.session.commit()
