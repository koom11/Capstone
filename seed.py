from app import app
from models import db, Drug, Pharmacy

db.drop_all()
db.create_all()


def create_drugs():
    """Function for creating drugs for database"""
    drug_list = []
    for num in range(232):
        print(f'd{num} = (name="{TOP_200[num]}"", price={prices[num]})')


""" for num in range(232):
    for p in pharmacies:
        print(
            f'{p}{num} = Price(drug_name="{TOP_200_DRUGS[num]}", pharmacy_name="{p}", price={r(1,100)})') """


d0 = Drug(name="Lexapro")
d1 = Drug(name="Vicodin")
d2 = Drug(name="Prinivil")
d3 = Drug(name="Qbrelis")
d4 = Drug(name="Zocor")
d5 = Drug(name="Synthroid")
d6 = Drug(name="Amoxil")
d7 = Drug(name="Trimox")
d8 = Drug(name="Zithromax")
d9 = Drug(name="Microzide")
d10 = Drug(name="Aquazide")
d11 = Drug(name="Norvasc")
d12 = Drug(name="Xanax")
d13 = Drug(name="Glucophage")
d14 = Drug(name="Lipitor")
d15 = Drug(name="Prilosec")
d16 = Drug(name="Cipro")
d17 = Drug(name="Proquin")
d18 = Drug(name="Zofran")
d19 = Drug(name="Clozaril")
d20 = Drug(name="Lasix")
d21 = Drug(name="Levitra")
d22 = Drug(name="Sumycin")
d23 = Drug(name="Ala-Tet")
d24 = Drug(name="Brodspec")
d25 = Drug(name="Heparin Sodium")
d26 = Drug(name="Valcyte")
d27 = Drug(name="Lamictal")
d28 = Drug(name="Diflucan")
d29 = Drug(name="Tenormin")
d30 = Drug(name="Singulair")
d31 = Drug(name="Flonase Nasal Spray")
d32 = Drug(name="Zyloprim")
d33 = Drug(name="Fosamax")
d34 = Drug(name="Pepcid")
d35 = Drug(name="Omnicef")
d36 = Drug(name="Yaz")
d37 = Drug(name="Apresoline")
d38 = Drug(name="Cogentin")
d39 = Drug(name="Tussionex PennKinetic")
d40 = Drug(name="Paxil")
d41 = Drug(name="Ativan")
d42 = Drug(name="Pyridium")
d43 = Drug(name="Plaquenil")
d44 = Drug(name="Lidoderm")
d45 = Drug(name="Cataflam")
d46 = Drug(name="Rayos")
d47 = Drug(name="Deltasone")
d48 = Drug(name="Zetia")
d49 = Drug(name="Evista")
d50 = Drug(name="Dilantin")
d51 = Drug(name="Lovaza")
d52 = Drug(name="Zanaflex")
d53 = Drug(name="Hytrin")
d54 = Drug(name="Dyrenium")
d55 = Drug(name="Altace")
d56 = Drug(name="Pravachol")
d57 = Drug(name="Risperdal")
d58 = Drug(name="Lunesta")
d59 = Drug(name="Celebrex")
d60 = Drug(name="Premarin")
d61 = Drug(name="Avelox")
d62 = Drug(name="Aricept")
d63 = Drug(name="Macrobid")
d64 = Drug(name="Macrodantin")
d65 = Drug(name="Duragesic Skin Patch")
d66 = Drug(name="Imdur")
d67 = Drug(name="Prozac")
d68 = Drug(name="Sarafem")
d69 = Drug(name="Aristocort")
d70 = Drug(name="Suboxone")
d71 = Drug(name="Vyvanse")
d72 = Drug(name="Pamelor")
d73 = Drug(name="HumaLOG")
d74 = Drug(name="Depacon")
d75 = Drug(name="Depakote")
d76 = Drug(name="BetaSept")
d77 = Drug(name="ChloraPrep")
d78 = Drug(name="Bentyl")
d79 = Drug(name="Imitrex")
d80 = Drug(name="Protonix")
d81 = Drug(name="Lopressor")
d82 = Drug(name="Robitussen")
d83 = Drug(name="Valium")
d84 = Drug(name="Viagra")
d85 = Drug(name="Bactroban")
d86 = Drug(name="Januvia")
d87 = Drug(name="Reglan")
d88 = Drug(name="Relafen")
d89 = Drug(name="Keflex")
d90 = Drug(name="Effexor")
d91 = Drug(name="Boniva")
d92 = Drug(name="Zantac")
d93 = Drug(name="Ex-Lax")
d94 = Drug(name="Senna Lax")
d95 = Drug(name="NovoLog")
d96 = Drug(name="Bayer")
d97 = Drug(name="Ecotrin")
d98 = Drug(name="Bufferin")
d99 = Drug(name="Lioresal")
d100 = Drug(name="Flagyl")
d101 = Drug(name="Keppra")
d102 = Drug(name="Colcrys")
d103 = Drug(name="Mitigare")
d104 = Drug(name="Zyprexa")
d105 = Drug(name="Avodart")
d106 = Drug(name="TriCor")
d107 = Drug(name="Antara")
d108 = Drug(name="Cardura")
d109 = Drug(name="Aleve")
d110 = Drug(name="Aldactone")
d111 = Drug(name="Namenda")
d112 = Drug(name="Methadose")
d113 = Drug(name="Vasotec")
d114 = Drug(name="Epaned")
d115 = Drug(name="Tamiflu")
d116 = Drug(name="Requip")
d117 = Drug(name="PC Pen VK")
d118 = Drug(name="Pen V")
d119 = Drug(name="Strattera")
d120 = Drug(name="Ambien")
d121 = Drug(name="Advair")
d122 = Drug(name="Levaquin")
d123 = Drug(name="Tofranil")
d124 = Drug(name="Reclast")
d125 = Drug(name="Zometa")
d126 = Drug(name="Glucotrol")
d127 = Drug(name="Constulose")
d128 = Drug(name="AcipHex")
d129 = Drug(name="Otrexup")
d130 = Drug(name="Cleocin")
d131 = Drug(name="Tylenol")
d132 = Drug(name="Feosol")
d133 = Drug(name="Relpax")
d134 = Drug(name="Carbacot")
d135 = Drug(name="Robaxin")
d136 = Drug(name="DiaBeta")
d137 = Drug(name="Celexa")
d138 = Drug(name="Benicar")
d139 = Drug(name="Coreg")
d140 = Drug(name="Spiriva")
d141 = Drug(name="Xolair")
d142 = Drug(name="NitroStat Sublingual")
d143 = Drug(name="Eliquis")
d144 = Drug(name="Neurontin")
d145 = Drug(name="Enbrel")
d146 = Drug(name="Herceptin")
d147 = Drug(name="Atripla")
d148 = Drug(name="Xarelto")
d149 = Drug(name="Stalevo 50")
d150 = Drug(name="Fioricet")
d151 = Drug(name="Levemir")
d152 = Drug(name="Lovenox")
d153 = Drug(name="Ritalin")
d154 = Drug(name="Concerta")
d155 = Drug(name="Crestor")
d156 = Drug(name="Xgeva")
d157 = Drug(name="Prolia")
d158 = Drug(name="Pradaxa")
d159 = Drug(name="Sensipar")
d160 = Drug(name="Vesicare")
d161 = Drug(name="Haldol")
d162 = Drug(name="Ala-Cort")
d163 = Drug(name="HumuLIN")
d164 = Drug(name="Isentress")
d165 = Drug(name="Stelara")
d166 = Drug(name="Mobic")
d167 = Drug(name="Remicade")
d168 = Drug(name="Night Time")
d169 = Drug(name="Renvela")
d170 = Drug(name="Fragmin")
d171 = Drug(name="Zoloft")
d172 = Drug(name="Klonopin")
d173 = Drug(name="Avalide")
d174 = Drug(name="Ceftin")
d175 = Drug(name="Nizoral Topical")
d176 = Drug(name="Lyrica")
d177 = Drug(name="Nexium")
d178 = Drug(name="Combivent Respimat")
d179 = Drug(name="Niaspan")
d180 = Drug(name="Uroxatral")
d181 = Drug(name="Biaxin")
d182 = Drug(name="Zomig")
d183 = Drug(name="Invokana")
d184 = Drug(name="Saxenda")
d185 = Drug(name="Victoza")
d186 = Drug(name="Alimta")
d187 = Drug(name="Lotrisone")
d188 = Drug(name="Avastin")
d189 = Drug(name="Sovaldi")
d190 = Drug(name="Gilenya")
d191 = Drug(name="Epogen")
d192 = Drug(name="Seroquel")
d193 = Drug(name="Amaryl")
d194 = Drug(name="Percocet")
d195 = Drug(name="SandIMMUNE")
d196 = Drug(name="Neoral")
d197 = Drug(name="Lantus")
d198 = Drug(name="Cialis")
d199 = Drug(name="Elavil")
d200 = Drug(name="Vanatrip")
d201 = Drug(name="Lopid")
d202 = Drug(name="Flo-Pred")
d203 = Drug(name="Advil")
d204 = Drug(name="Aceon")
d205 = Drug(name="Desyrel")
d206 = Drug(name="Actos")
d207 = Drug(name="Proscar")
d208 = Drug(name="Inbrija")
d209 = Drug(name="Dopar")
d210 = Drug(name="Larodopa")
d211 = Drug(name="Actonel")
d212 = Drug(name="ProAir")
d213 = Drug(name="Ventolin")
d214 = Drug(name="Proventil")
d215 = Drug(name="Ultram")
d216 = Drug(name="Sonata")
d217 = Drug(name="Zebeta")
d218 = Drug(name="Zovirax")
d219 = Drug(name="Coumadin")
d220 = Drug(name="Luvox")
d221 = Drug(name="Plavix")
d222 = Drug(name="Vibramycin")
d223 = Drug(name="Adoxa")
d224 = Drug(name="Hyzaar")
d225 = Drug(name="Kytril")
d226 = Drug(name="Sancuso")
d227 = Drug(name="Restoril")
d228 = Drug(name="Prevacid")
d229 = Drug(name="Augmentin")
d230 = Drug(name="Mevacor")
d231 = Drug(name="Altoprev")

p1 = Pharmacy(name="CVS", address='580 Marketplace Dr. Bel Air, MD 21014')
p2 = Pharmacy(name="Walgreens", address='1927 Emmorton Rd, Bel Air, MD 21015')
p3 = Pharmacy(name="Walmart",
              address='401 Constant Friendship Blvd, Abingdon, MD 21009')
p4 = Pharmacy(name="Wegmans",
              address='21 Wegmans Boulevard, Abingdon, MD 21009')

""" CVS0 = Price(drug_name="Lexapro", pharmacy_name="CVS", price=100)
Walgreens0 = Price(drug_name="Lexapro", pharmacy_name="Walgreens", price=24)
Walmart0 = Price(drug_name="Lexapro", pharmacy_name="Walmart", price=33)
Wegmans0 = Price(drug_name="Lexapro", pharmacy_name="Wegmans", price=34)
CVS1 = Price(drug_name="Vicodin", pharmacy_name="CVS", price=46)
Walgreens1 = Price(drug_name="Vicodin", pharmacy_name="Walgreens", price=35)
Walmart1 = Price(drug_name="Vicodin", pharmacy_name="Walmart", price=56)
Wegmans1 = Price(drug_name="Vicodin", pharmacy_name="Wegmans", price=53)
CVS2 = Price(drug_name="Prinivil", pharmacy_name="CVS", price=53)
Walgreens2 = Price(drug_name="Prinivil", pharmacy_name="Walgreens", price=52)
Walmart2 = Price(drug_name="Prinivil", pharmacy_name="Walmart", price=42)
Wegmans2 = Price(drug_name="Prinivil", pharmacy_name="Wegmans", price=87)
CVS3 = Price(drug_name="Qbrelis", pharmacy_name="CVS", price=99)
Walgreens3 = Price(drug_name="Qbrelis", pharmacy_name="Walgreens", price=38)
Walmart3 = Price(drug_name="Qbrelis", pharmacy_name="Walmart", price=58)
Wegmans3 = Price(drug_name="Qbrelis", pharmacy_name="Wegmans", price=53)
CVS4 = Price(drug_name="Zocor", pharmacy_name="CVS", price=29)
Walgreens4 = Price(drug_name="Zocor", pharmacy_name="Walgreens", price=20)
Walmart4 = Price(drug_name="Zocor", pharmacy_name="Walmart", price=20)
Wegmans4 = Price(drug_name="Zocor", pharmacy_name="Wegmans", price=32)
CVS5 = Price(drug_name="Synthroid", pharmacy_name="CVS", price=25)
Walgreens5 = Price(drug_name="Synthroid", pharmacy_name="Walgreens", price=73)
Walmart5 = Price(drug_name="Synthroid", pharmacy_name="Walmart", price=76)
Wegmans5 = Price(drug_name="Synthroid", pharmacy_name="Wegmans", price=89)
CVS6 = Price(drug_name="Amoxil", pharmacy_name="CVS", price=72)
Walgreens6 = Price(drug_name="Amoxil", pharmacy_name="Walgreens", price=8)
Walmart6 = Price(drug_name="Amoxil", pharmacy_name="Walmart", price=8)
Wegmans6 = Price(drug_name="Amoxil", pharmacy_name="Wegmans", price=20)
CVS7 = Price(drug_name="Trimox", pharmacy_name="CVS", price=21)
Walgreens7 = Price(drug_name="Trimox", pharmacy_name="Walgreens", price=86)
Walmart7 = Price(drug_name="Trimox", pharmacy_name="Walmart", price=25)
Wegmans7 = Price(drug_name="Trimox", pharmacy_name="Wegmans", price=67)
CVS8 = Price(drug_name="Zithromax", pharmacy_name="CVS", price=83)
Walgreens8 = Price(drug_name="Zithromax", pharmacy_name="Walgreens", price=50)
Walmart8 = Price(drug_name="Zithromax", pharmacy_name="Walmart", price=79)
Wegmans8 = Price(drug_name="Zithromax", pharmacy_name="Wegmans", price=74)
CVS9 = Price(drug_name="Microzide", pharmacy_name="CVS", price=87)
Walgreens9 = Price(drug_name="Microzide", pharmacy_name="Walgreens", price=26)
Walmart9 = Price(drug_name="Microzide", pharmacy_name="Walmart", price=85)
Wegmans9 = Price(drug_name="Microzide", pharmacy_name="Wegmans", price=33)
CVS10 = Price(drug_name="Aquazide", pharmacy_name="CVS", price=30)
Walgreens10 = Price(drug_name="Aquazide", pharmacy_name="Walgreens", price=96)
Walmart10 = Price(drug_name="Aquazide", pharmacy_name="Walmart", price=63)
Wegmans10 = Price(drug_name="Aquazide", pharmacy_name="Wegmans", price=74)
CVS11 = Price(drug_name="Norvasc", pharmacy_name="CVS", price=58)
Walgreens11 = Price(drug_name="Norvasc", pharmacy_name="Walgreens", price=48)
Walmart11 = Price(drug_name="Norvasc", pharmacy_name="Walmart", price=71)
Wegmans11 = Price(drug_name="Norvasc", pharmacy_name="Wegmans", price=12)
CVS12 = Price(drug_name="Xanax", pharmacy_name="CVS", price=23)
Walgreens12 = Price(drug_name="Xanax", pharmacy_name="Walgreens", price=98)
Walmart12 = Price(drug_name="Xanax", pharmacy_name="Walmart", price=33)
Wegmans12 = Price(drug_name="Xanax", pharmacy_name="Wegmans", price=24)
CVS13 = Price(drug_name="Glucophage", pharmacy_name="CVS", price=88)
Walgreens13 = Price(drug_name="Glucophage",
                    pharmacy_name="Walgreens", price=74)
Walmart13 = Price(drug_name="Glucophage", pharmacy_name="Walmart", price=16)
Wegmans13 = Price(drug_name="Glucophage", pharmacy_name="Wegmans", price=68)
CVS14 = Price(drug_name="Lipitor", pharmacy_name="CVS", price=44)
Walgreens14 = Price(drug_name="Lipitor", pharmacy_name="Walgreens", price=59)
Walmart14 = Price(drug_name="Lipitor", pharmacy_name="Walmart", price=23)
Wegmans14 = Price(drug_name="Lipitor", pharmacy_name="Wegmans", price=32)
CVS15 = Price(drug_name="Prilosec", pharmacy_name="CVS", price=21)
Walgreens15 = Price(drug_name="Prilosec", pharmacy_name="Walgreens", price=67)
Walmart15 = Price(drug_name="Prilosec", pharmacy_name="Walmart", price=35)
Wegmans15 = Price(drug_name="Prilosec", pharmacy_name="Wegmans", price=86)
CVS16 = Price(drug_name="Cipro", pharmacy_name="CVS", price=61)
Walgreens16 = Price(drug_name="Cipro", pharmacy_name="Walgreens", price=8)
Walmart16 = Price(drug_name="Cipro", pharmacy_name="Walmart", price=14)
Wegmans16 = Price(drug_name="Cipro", pharmacy_name="Wegmans", price=43)
CVS17 = Price(drug_name="Proquin", pharmacy_name="CVS", price=63)
Walgreens17 = Price(drug_name="Proquin", pharmacy_name="Walgreens", price=34)
Walmart17 = Price(drug_name="Proquin", pharmacy_name="Walmart", price=85)
Wegmans17 = Price(drug_name="Proquin", pharmacy_name="Wegmans", price=81)
CVS18 = Price(drug_name="Zofran", pharmacy_name="CVS", price=30)
Walgreens18 = Price(drug_name="Zofran", pharmacy_name="Walgreens", price=96)
Walmart18 = Price(drug_name="Zofran", pharmacy_name="Walmart", price=19)
Wegmans18 = Price(drug_name="Zofran", pharmacy_name="Wegmans", price=83)
CVS19 = Price(drug_name="Clozaril", pharmacy_name="CVS", price=88)
Walgreens19 = Price(drug_name="Clozaril", pharmacy_name="Walgreens", price=94)
Walmart19 = Price(drug_name="Clozaril", pharmacy_name="Walmart", price=69)
Wegmans19 = Price(drug_name="Clozaril", pharmacy_name="Wegmans", price=90)
CVS20 = Price(drug_name="Lasix", pharmacy_name="CVS", price=16)
Walgreens20 = Price(drug_name="Lasix", pharmacy_name="Walgreens", price=33)
Walmart20 = Price(drug_name="Lasix", pharmacy_name="Walmart", price=53)
Wegmans20 = Price(drug_name="Lasix", pharmacy_name="Wegmans", price=65)
CVS21 = Price(drug_name="Levitra", pharmacy_name="CVS", price=99)
Walgreens21 = Price(drug_name="Levitra", pharmacy_name="Walgreens", price=6)
Walmart21 = Price(drug_name="Levitra", pharmacy_name="Walmart", price=25)
Wegmans21 = Price(drug_name="Levitra", pharmacy_name="Wegmans", price=7)
CVS22 = Price(drug_name="Sumycin", pharmacy_name="CVS", price=89)
Walgreens22 = Price(drug_name="Sumycin", pharmacy_name="Walgreens", price=56)
Walmart22 = Price(drug_name="Sumycin", pharmacy_name="Walmart", price=42)
Wegmans22 = Price(drug_name="Sumycin", pharmacy_name="Wegmans", price=69)
CVS23 = Price(drug_name="Ala-Tet", pharmacy_name="CVS", price=79)
Walgreens23 = Price(drug_name="Ala-Tet", pharmacy_name="Walgreens", price=85)
Walmart23 = Price(drug_name="Ala-Tet", pharmacy_name="Walmart", price=25)
Wegmans23 = Price(drug_name="Ala-Tet", pharmacy_name="Wegmans", price=69)
CVS24 = Price(drug_name="Brodspec", pharmacy_name="CVS", price=11)
Walgreens24 = Price(drug_name="Brodspec", pharmacy_name="Walgreens", price=65)
Walmart24 = Price(drug_name="Brodspec", pharmacy_name="Walmart", price=55)
Wegmans24 = Price(drug_name="Brodspec", pharmacy_name="Wegmans", price=42)
CVS25 = Price(drug_name="Heparin Sodium", pharmacy_name="CVS", price=20)
Walgreens25 = Price(drug_name="Heparin Sodium",
                    pharmacy_name="Walgreens", price=15)
Walmart25 = Price(drug_name="Heparin Sodium",
                  pharmacy_name="Walmart", price=76)
Wegmans25 = Price(drug_name="Heparin Sodium",
                  pharmacy_name="Wegmans", price=2)

CVS26 = Price(drug_name="Valcyte", pharmacy_name="CVS", price=50)
Walgreens26 = Price(drug_name="Valcyte", pharmacy_name="Walgreens", price=29)
Walmart26 = Price(drug_name="Valcyte", pharmacy_name="Walmart", price=97)
Wegmans26 = Price(drug_name="Valcyte", pharmacy_name="Wegmans", price=36)
CVS27 = Price(drug_name="Lamictal", pharmacy_name="CVS", price=34)
Walgreens27 = Price(drug_name="Lamictal", pharmacy_name="Walgreens", price=89)
Walmart27 = Price(drug_name="Lamictal", pharmacy_name="Walmart", price=74)
Wegmans27 = Price(drug_name="Lamictal", pharmacy_name="Wegmans", price=92)
CVS28 = Price(drug_name="Diflucan", pharmacy_name="CVS", price=13)
Walgreens28 = Price(drug_name="Diflucan",
                    pharmacy_name="Walgreens", price=100)

Walmart28 = Price(drug_name="Diflucan", pharmacy_name="Walmart", price=81)
Wegmans28 = Price(drug_name="Diflucan", pharmacy_name="Wegmans", price=9)
CVS29 = Price(drug_name="Tenormin", pharmacy_name="CVS", price=21)
Walgreens29 = Price(drug_name="Tenormin", pharmacy_name="Walgreens", price=57)
Walmart29 = Price(drug_name="Tenormin", pharmacy_name="Walmart", price=27)
Wegmans29 = Price(drug_name="Tenormin", pharmacy_name="Wegmans", price=60)
CVS30 = Price(drug_name="Singulair", pharmacy_name="CVS", price=55)
Walgreens30 = Price(drug_name="Singulair",
                    pharmacy_name="Walgreens", price=88)

Walmart30 = Price(drug_name="Singulair", pharmacy_name="Walmart", price=86)
Wegmans30 = Price(drug_name="Singulair", pharmacy_name="Wegmans", price=72)
CVS31 = Price(drug_name="Flonase Nasal Spray", pharmacy_name="CVS", price=20)
Walgreens31 = Price(drug_name="Flonase Nasal Spray", pharmacy_name="Walgreens",
                    price=59)
Walmart31 = Price(drug_name="Flonase Nasal Spray",
                  pharmacy_name="Walmart", price=58)
Wegmans31 = Price(drug_name="Flonase Nasal Spray",
                  pharmacy_name="Wegmans", price=81)
CVS32 = Price(drug_name="Zyloprim", pharmacy_name="CVS", price=6)
Walgreens32 = Price(drug_name="Zyloprim", pharmacy_name="Walgreens", price=6)
Walmart32 = Price(drug_name="Zyloprim", pharmacy_name="Walmart", price=2)
Wegmans32 = Price(drug_name="Zyloprim", pharmacy_name="Wegmans", price=55)
CVS33 = Price(drug_name="Fosamax", pharmacy_name="CVS", price=24)
Walgreens33 = Price(drug_name="Fosamax", pharmacy_name="Walgreens", price=29)
Walmart33 = Price(drug_name="Fosamax", pharmacy_name="Walmart", price=47)
Wegmans33 = Price(drug_name="Fosamax", pharmacy_name="Wegmans", price=36)
CVS34 = Price(drug_name="Pepcid", pharmacy_name="CVS", price=69)
Walgreens34 = Price(drug_name="Pepcid", pharmacy_name="Walgreens", price=78)
Walmart34 = Price(drug_name="Pepcid", pharmacy_name="Walmart", price=18)
Wegmans34 = Price(drug_name="Pepcid", pharmacy_name="Wegmans", price=69)
CVS35 = Price(drug_name="Omnicef", pharmacy_name="CVS", price=78)
Walgreens35 = Price(drug_name="Omnicef", pharmacy_name="Walgreens", price=73)
Walmart35 = Price(drug_name="Omnicef", pharmacy_name="Walmart", price=2)
Wegmans35 = Price(drug_name="Omnicef", pharmacy_name="Wegmans", price=100)
CVS36 = Price(drug_name="Yaz", pharmacy_name="CVS", price=79)
Walgreens36 = Price(drug_name="Yaz", pharmacy_name="Walgreens", price=91)
Walmart36 = Price(drug_name="Yaz", pharmacy_name="Walmart", price=12)
Wegmans36 = Price(drug_name="Yaz", pharmacy_name="Wegmans", price=55)
CVS37 = Price(drug_name="Apresoline", pharmacy_name="CVS", price=77)
Walgreens37 = Price(drug_name="Apresoline",
                    pharmacy_name="Walgreens", price=29)
Walmart37 = Price(drug_name="Apresoline", pharmacy_name="Walmart", price=46)
Wegmans37 = Price(drug_name="Apresoline", pharmacy_name="Wegmans", price=75)
CVS38 = Price(drug_name="Cogentin", pharmacy_name="CVS", price=53)
Walgreens38 = Price(drug_name="Cogentin", pharmacy_name="Walgreens", price=97)
Walmart38 = Price(drug_name="Cogentin", pharmacy_name="Walmart", price=10)
Wegmans38 = Price(drug_name="Cogentin", pharmacy_name="Wegmans", price=17)
CVS39 = Price(drug_name="Tussionex PennKinetic", pharmacy_name="CVS", price=15)

Walgreens39 = Price(drug_name="Tussionex PennKinetic",
                    pharmacy_name="Walgreens", price=50)
Walmart39 = Price(drug_name="Tussionex PennKinetic",
                  pharmacy_name="Walmart", price=74)
Wegmans39 = Price(drug_name="Tussionex PennKinetic",
                  pharmacy_name="Wegmans", price=27)
CVS40 = Price(drug_name="Paxil", pharmacy_name="CVS", price=11)
Walgreens40 = Price(drug_name="Paxil", pharmacy_name="Walgreens", price=1)
Walmart40 = Price(drug_name="Paxil", pharmacy_name="Walmart", price=92)
Wegmans40 = Price(drug_name="Paxil", pharmacy_name="Wegmans", price=48)
CVS41 = Price(drug_name="Ativan", pharmacy_name="CVS", price=93)
Walgreens41 = Price(drug_name="Ativan", pharmacy_name="Walgreens", price=31)
Walmart41 = Price(drug_name="Ativan", pharmacy_name="Walmart", price=34)
Wegmans41 = Price(drug_name="Ativan", pharmacy_name="Wegmans", price=49)
CVS42 = Price(drug_name="Pyridium", pharmacy_name="CVS", price=48)
Walgreens42 = Price(drug_name="Pyridium", pharmacy_name="Walgreens", price=25)
Walmart42 = Price(drug_name="Pyridium", pharmacy_name="Walmart", price=84)
Wegmans42 = Price(drug_name="Pyridium", pharmacy_name="Wegmans", price=9)
CVS43 = Price(drug_name="Plaquenil", pharmacy_name="CVS", price=61)
Walgreens43 = Price(drug_name="Plaquenil",
                    pharmacy_name="Walgreens", price=60)

Walmart43 = Price(drug_name="Plaquenil", pharmacy_name="Walmart", price=65)
Wegmans43 = Price(drug_name="Plaquenil", pharmacy_name="Wegmans", price=36)
CVS44 = Price(drug_name="Lidoderm", pharmacy_name="CVS", price=50)
Walgreens44 = Price(drug_name="Lidoderm", pharmacy_name="Walgreens", price=18)
Walmart44 = Price(drug_name="Lidoderm", pharmacy_name="Walmart", price=32)
Wegmans44 = Price(drug_name="Lidoderm", pharmacy_name="Wegmans", price=78)
CVS45 = Price(drug_name="Cataflam", pharmacy_name="CVS", price=43)
Walgreens45 = Price(drug_name="Cataflam", pharmacy_name="Walgreens", price=40)
Walmart45 = Price(drug_name="Cataflam", pharmacy_name="Walmart", price=58)
Wegmans45 = Price(drug_name="Cataflam", pharmacy_name="Wegmans", price=34)
CVS46 = Price(drug_name="Rayos", pharmacy_name="CVS", price=66)
Walgreens46 = Price(drug_name="Rayos", pharmacy_name="Walgreens", price=83)
Walmart46 = Price(drug_name="Rayos", pharmacy_name="Walmart", price=30)
Wegmans46 = Price(drug_name="Rayos", pharmacy_name="Wegmans", price=92)
CVS47 = Price(drug_name="Deltasone", pharmacy_name="CVS", price=26)
Walgreens47 = Price(drug_name="Deltasone",
                    pharmacy_name="Walgreens", price=82)

Walmart47 = Price(drug_name="Deltasone", pharmacy_name="Walmart", price=81)
Wegmans47 = Price(drug_name="Deltasone", pharmacy_name="Wegmans", price=77)
CVS48 = Price(drug_name="Zetia", pharmacy_name="CVS", price=16)
Walgreens48 = Price(drug_name="Zetia", pharmacy_name="Walgreens", price=100)
Walmart48 = Price(drug_name="Zetia", pharmacy_name="Walmart", price=38)
Wegmans48 = Price(drug_name="Zetia", pharmacy_name="Wegmans", price=61)
CVS49 = Price(drug_name="Evista", pharmacy_name="CVS", price=62)
Walgreens49 = Price(drug_name="Evista", pharmacy_name="Walgreens", price=55)
Walmart49 = Price(drug_name="Evista", pharmacy_name="Walmart", price=17)
Wegmans49 = Price(drug_name="Evista", pharmacy_name="Wegmans", price=86)
CVS50 = Price(drug_name="Dilantin", pharmacy_name="CVS", price=80)
Walgreens50 = Price(drug_name="Dilantin", pharmacy_name="Walgreens", price=30)
Walmart50 = Price(drug_name="Dilantin", pharmacy_name="Walmart", price=89)
Wegmans50 = Price(drug_name="Dilantin", pharmacy_name="Wegmans", price=43)
CVS51 = Price(drug_name="Lovaza", pharmacy_name="CVS", price=38)
Walgreens51 = Price(drug_name="Lovaza", pharmacy_name="Walgreens", price=59)
Walmart51 = Price(drug_name="Lovaza", pharmacy_name="Walmart", price=54)
Wegmans51 = Price(drug_name="Lovaza", pharmacy_name="Wegmans", price=16)
CVS52 = Price(drug_name="Zanaflex", pharmacy_name="CVS", price=15)
Walgreens52 = Price(drug_name="Zanaflex", pharmacy_name="Walgreens", price=64)
Walmart52 = Price(drug_name="Zanaflex", pharmacy_name="Walmart", price=95)
Wegmans52 = Price(drug_name="Zanaflex", pharmacy_name="Wegmans", price=48)
CVS53 = Price(drug_name="Hytrin", pharmacy_name="CVS", price=96)
Walgreens53 = Price(drug_name="Hytrin", pharmacy_name="Walgreens", price=9)
Walmart53 = Price(drug_name="Hytrin", pharmacy_name="Walmart", price=29)
Wegmans53 = Price(drug_name="Hytrin", pharmacy_name="Wegmans", price=57)
CVS54 = Price(drug_name="Dyrenium", pharmacy_name="CVS", price=98)
Walgreens54 = Price(drug_name="Dyrenium", pharmacy_name="Walgreens", price=85)
Walmart54 = Price(drug_name="Dyrenium", pharmacy_name="Walmart", price=75)
Wegmans54 = Price(drug_name="Dyrenium", pharmacy_name="Wegmans", price=30)
CVS55 = Price(drug_name="Altace", pharmacy_name="CVS", price=76)
Walgreens55 = Price(drug_name="Altace", pharmacy_name="Walgreens", price=41)
Walmart55 = Price(drug_name="Altace", pharmacy_name="Walmart", price=49)
Wegmans55 = Price(drug_name="Altace", pharmacy_name="Wegmans", price=66)
CVS56 = Price(drug_name="Pravachol", pharmacy_name="CVS", price=10)
Walgreens56 = Price(drug_name="Pravachol",
                    pharmacy_name="Walgreens", price=32)

Walmart56 = Price(drug_name="Pravachol", pharmacy_name="Walmart", price=51)
Wegmans56 = Price(drug_name="Pravachol", pharmacy_name="Wegmans", price=28)
CVS57 = Price(drug_name="Risperdal", pharmacy_name="CVS", price=49)
Walgreens57 = Price(drug_name="Risperdal",
                    pharmacy_name="Walgreens", price=35)

Walmart57 = Price(drug_name="Risperdal", pharmacy_name="Walmart", price=55)
Wegmans57 = Price(drug_name="Risperdal", pharmacy_name="Wegmans", price=15)
CVS58 = Price(drug_name="Lunesta", pharmacy_name="CVS", price=94)
Walgreens58 = Price(drug_name="Lunesta", pharmacy_name="Walgreens", price=55)
Walmart58 = Price(drug_name="Lunesta", pharmacy_name="Walmart", price=88)
Wegmans58 = Price(drug_name="Lunesta", pharmacy_name="Wegmans", price=76)
CVS59 = Price(drug_name="Celebrex", pharmacy_name="CVS", price=6)
Walgreens59 = Price(drug_name="Celebrex", pharmacy_name="Walgreens", price=17)
Walmart59 = Price(drug_name="Celebrex", pharmacy_name="Walmart", price=12)
Wegmans59 = Price(drug_name="Celebrex", pharmacy_name="Wegmans", price=53)
CVS60 = Price(drug_name="Premarin", pharmacy_name="CVS", price=73)
Walgreens60 = Price(drug_name="Premarin", pharmacy_name="Walgreens", price=97)
Walmart60 = Price(drug_name="Premarin", pharmacy_name="Walmart", price=90)
Wegmans60 = Price(drug_name="Premarin", pharmacy_name="Wegmans", price=84)
CVS61 = Price(drug_name="Avelox", pharmacy_name="CVS", price=38)
Walgreens61 = Price(drug_name="Avelox", pharmacy_name="Walgreens", price=85)
Walmart61 = Price(drug_name="Avelox", pharmacy_name="Walmart", price=39)
Wegmans61 = Price(drug_name="Avelox", pharmacy_name="Wegmans", price=4)
CVS62 = Price(drug_name="Aricept", pharmacy_name="CVS", price=73)
Walgreens62 = Price(drug_name="Aricept", pharmacy_name="Walgreens", price=90)
Walmart62 = Price(drug_name="Aricept", pharmacy_name="Walmart", price=41)
Wegmans62 = Price(drug_name="Aricept", pharmacy_name="Wegmans", price=94)
CVS63 = Price(drug_name="Macrobid", pharmacy_name="CVS", price=15)
Walgreens63 = Price(drug_name="Macrobid", pharmacy_name="Walgreens", price=85)
Walmart63 = Price(drug_name="Macrobid", pharmacy_name="Walmart", price=44)
Wegmans63 = Price(drug_name="Macrobid", pharmacy_name="Wegmans", price=69)
CVS64 = Price(drug_name="Macrodantin", pharmacy_name="CVS", price=56)
Walgreens64 = Price(drug_name="Macrodantin", pharmacy_name="Walgreens", price=35
                    )
Walmart64 = Price(drug_name="Macrodantin", pharmacy_name="Walmart", price=45)
Wegmans64 = Price(drug_name="Macrodantin", pharmacy_name="Wegmans", price=85)
CVS65 = Price(drug_name="Duragesic Skin Patch", pharmacy_name="CVS", price=46)
Walgreens65 = Price(drug_name="Duragesic Skin Patch", pharmacy_name="Walgreens",
                    price=78)
Walmart65 = Price(drug_name="Duragesic Skin Patch",
                  pharmacy_name="Walmart", price=7)
Wegmans65 = Price(drug_name="Duragesic Skin Patch",
                  pharmacy_name="Wegmans", price=67)
CVS66 = Price(drug_name="Imdur", pharmacy_name="CVS", price=36)
Walgreens66 = Price(drug_name="Imdur", pharmacy_name="Walgreens", price=46)
Walmart66 = Price(drug_name="Imdur", pharmacy_name="Walmart", price=87)
Wegmans66 = Price(drug_name="Imdur", pharmacy_name="Wegmans", price=19)
CVS67 = Price(drug_name="Prozac", pharmacy_name="CVS", price=54)
Walgreens67 = Price(drug_name="Prozac", pharmacy_name="Walgreens", price=91)
Walmart67 = Price(drug_name="Prozac", pharmacy_name="Walmart", price=78)
Wegmans67 = Price(drug_name="Prozac", pharmacy_name="Wegmans", price=88)
CVS68 = Price(drug_name="Sarafem", pharmacy_name="CVS", price=15)
Walgreens68 = Price(drug_name="Sarafem", pharmacy_name="Walgreens", price=76)
Walmart68 = Price(drug_name="Sarafem", pharmacy_name="Walmart", price=30)
Wegmans68 = Price(drug_name="Sarafem", pharmacy_name="Wegmans", price=69)
CVS69 = Price(drug_name="Aristocort", pharmacy_name="CVS", price=68)
Walgreens69 = Price(drug_name="Aristocort",
                    pharmacy_name="Walgreens", price=12)
Walmart69 = Price(drug_name="Aristocort", pharmacy_name="Walmart", price=32)
Wegmans69 = Price(drug_name="Aristocort", pharmacy_name="Wegmans", price=28)
CVS70 = Price(drug_name="Suboxone", pharmacy_name="CVS", price=42)
Walgreens70 = Price(drug_name="Suboxone", pharmacy_name="Walgreens", price=78)
Walmart70 = Price(drug_name="Suboxone", pharmacy_name="Walmart", price=64)
Wegmans70 = Price(drug_name="Suboxone", pharmacy_name="Wegmans", price=35)
CVS71 = Price(drug_name="Vyvanse", pharmacy_name="CVS", price=76)
Walgreens71 = Price(drug_name="Vyvanse", pharmacy_name="Walgreens", price=77)
Walmart71 = Price(drug_name="Vyvanse", pharmacy_name="Walmart", price=61)
Wegmans71 = Price(drug_name="Vyvanse", pharmacy_name="Wegmans", price=49)
CVS72 = Price(drug_name="Pamelor", pharmacy_name="CVS", price=39)
Walgreens72 = Price(drug_name="Pamelor", pharmacy_name="Walgreens", price=86)
Walmart72 = Price(drug_name="Pamelor", pharmacy_name="Walmart", price=94)
Wegmans72 = Price(drug_name="Pamelor", pharmacy_name="Wegmans", price=10)
CVS73 = Price(drug_name="HumaLOG", pharmacy_name="CVS", price=66)
Walgreens73 = Price(drug_name="HumaLOG", pharmacy_name="Walgreens", price=20)
Walmart73 = Price(drug_name="HumaLOG", pharmacy_name="Walmart", price=35)
Wegmans73 = Price(drug_name="HumaLOG", pharmacy_name="Wegmans", price=81)
CVS74 = Price(drug_name="Depacon", pharmacy_name="CVS", price=25)
Walgreens74 = Price(drug_name="Depacon", pharmacy_name="Walgreens", price=72)
Walmart74 = Price(drug_name="Depacon", pharmacy_name="Walmart", price=80)
Wegmans74 = Price(drug_name="Depacon", pharmacy_name="Wegmans", price=44)
CVS75 = Price(drug_name="Depakote", pharmacy_name="CVS", price=12)
Walgreens75 = Price(drug_name="Depakote", pharmacy_name="Walgreens", price=40)
Walmart75 = Price(drug_name="Depakote", pharmacy_name="Walmart", price=61)
Wegmans75 = Price(drug_name="Depakote", pharmacy_name="Wegmans", price=48)
CVS76 = Price(drug_name="BetaSept", pharmacy_name="CVS", price=69)
Walgreens76 = Price(drug_name="BetaSept", pharmacy_name="Walgreens", price=2)
Walmart76 = Price(drug_name="BetaSept", pharmacy_name="Walmart", price=67)
Wegmans76 = Price(drug_name="BetaSept", pharmacy_name="Wegmans", price=26)
CVS77 = Price(drug_name="ChloraPrep", pharmacy_name="CVS", price=8)
Walgreens77 = Price(drug_name="ChloraPrep",
                    pharmacy_name="Walgreens", price=43)
Walmart77 = Price(drug_name="ChloraPrep", pharmacy_name="Walmart", price=25)
Wegmans77 = Price(drug_name="ChloraPrep", pharmacy_name="Wegmans", price=93)
CVS78 = Price(drug_name="Bentyl", pharmacy_name="CVS", price=67)
Walgreens78 = Price(drug_name="Bentyl", pharmacy_name="Walgreens", price=46)
Walmart78 = Price(drug_name="Bentyl", pharmacy_name="Walmart", price=4)
Wegmans78 = Price(drug_name="Bentyl", pharmacy_name="Wegmans", price=27)
CVS79 = Price(drug_name="Imitrex", pharmacy_name="CVS", price=65)
Walgreens79 = Price(drug_name="Imitrex", pharmacy_name="Walgreens", price=33)
Walmart79 = Price(drug_name="Imitrex", pharmacy_name="Walmart", price=35)
Wegmans79 = Price(drug_name="Imitrex", pharmacy_name="Wegmans", price=12)
CVS80 = Price(drug_name="Protonix", pharmacy_name="CVS", price=55)
Walgreens80 = Price(drug_name="Protonix", pharmacy_name="Walgreens", price=94)
Walmart80 = Price(drug_name="Protonix", pharmacy_name="Walmart", price=36)
Wegmans80 = Price(drug_name="Protonix", pharmacy_name="Wegmans", price=27)
CVS81 = Price(drug_name="Lopressor", pharmacy_name="CVS", price=72)
Walgreens81 = Price(drug_name="Lopressor",
                    pharmacy_name="Walgreens", price=88)

Walmart81 = Price(drug_name="Lopressor", pharmacy_name="Walmart", price=92)
Wegmans81 = Price(drug_name="Lopressor", pharmacy_name="Wegmans", price=17)
CVS82 = Price(drug_name="Robitussen", pharmacy_name="CVS", price=53)
Walgreens82 = Price(drug_name="Robitussen",
                    pharmacy_name="Walgreens", price=84)
Walmart82 = Price(drug_name="Robitussen", pharmacy_name="Walmart", price=83)
Wegmans82 = Price(drug_name="Robitussen", pharmacy_name="Wegmans", price=80)
CVS83 = Price(drug_name="Valium", pharmacy_name="CVS", price=72)
Walgreens83 = Price(drug_name="Valium", pharmacy_name="Walgreens", price=9)
Walmart83 = Price(drug_name="Valium", pharmacy_name="Walmart", price=34)
Wegmans83 = Price(drug_name="Valium", pharmacy_name="Wegmans", price=57)
CVS84 = Price(drug_name="Viagra", pharmacy_name="CVS", price=72)
Walgreens84 = Price(drug_name="Viagra", pharmacy_name="Walgreens", price=39)
Walmart84 = Price(drug_name="Viagra", pharmacy_name="Walmart", price=9)
Wegmans84 = Price(drug_name="Viagra", pharmacy_name="Wegmans", price=32)
CVS85 = Price(drug_name="Bactroban", pharmacy_name="CVS", price=89)
Walgreens85 = Price(drug_name="Bactroban",
                    pharmacy_name="Walgreens", price=77)

Walmart85 = Price(drug_name="Bactroban", pharmacy_name="Walmart", price=7)
Wegmans85 = Price(drug_name="Bactroban", pharmacy_name="Wegmans", price=3)
CVS86 = Price(drug_name="Januvia", pharmacy_name="CVS", price=92)
Walgreens86 = Price(drug_name="Januvia", pharmacy_name="Walgreens", price=68)
Walmart86 = Price(drug_name="Januvia", pharmacy_name="Walmart", price=40)
Wegmans86 = Price(drug_name="Januvia", pharmacy_name="Wegmans", price=31)
CVS87 = Price(drug_name="Reglan", pharmacy_name="CVS", price=57)
Walgreens87 = Price(drug_name="Reglan", pharmacy_name="Walgreens", price=21)
Walmart87 = Price(drug_name="Reglan", pharmacy_name="Walmart", price=19)
Wegmans87 = Price(drug_name="Reglan", pharmacy_name="Wegmans", price=63)
CVS88 = Price(drug_name="Relafen", pharmacy_name="CVS", price=63)
Walgreens88 = Price(drug_name="Relafen", pharmacy_name="Walgreens", price=98)
Walmart88 = Price(drug_name="Relafen", pharmacy_name="Walmart", price=21)
Wegmans88 = Price(drug_name="Relafen", pharmacy_name="Wegmans", price=19)
CVS89 = Price(drug_name="Keflex", pharmacy_name="CVS", price=40)
Walgreens89 = Price(drug_name="Keflex", pharmacy_name="Walgreens", price=88)
Walmart89 = Price(drug_name="Keflex", pharmacy_name="Walmart", price=41)
Wegmans89 = Price(drug_name="Keflex", pharmacy_name="Wegmans", price=98)
CVS90 = Price(drug_name="Effexor", pharmacy_name="CVS", price=28)
Walgreens90 = Price(drug_name="Effexor", pharmacy_name="Walgreens", price=52)
Walmart90 = Price(drug_name="Effexor", pharmacy_name="Walmart", price=85)
Wegmans90 = Price(drug_name="Effexor", pharmacy_name="Wegmans", price=69)
CVS91 = Price(drug_name="Boniva", pharmacy_name="CVS", price=18)
Walgreens91 = Price(drug_name="Boniva", pharmacy_name="Walgreens", price=62)
Walmart91 = Price(drug_name="Boniva", pharmacy_name="Walmart", price=63)
Wegmans91 = Price(drug_name="Boniva", pharmacy_name="Wegmans", price=58)
CVS92 = Price(drug_name="Zantac", pharmacy_name="CVS", price=18)
Walgreens92 = Price(drug_name="Zantac", pharmacy_name="Walgreens", price=37)
Walmart92 = Price(drug_name="Zantac", pharmacy_name="Walmart", price=97)
Wegmans92 = Price(drug_name="Zantac", pharmacy_name="Wegmans", price=64)
CVS93 = Price(drug_name="Ex-Lax", pharmacy_name="CVS", price=60)
Walgreens93 = Price(drug_name="Ex-Lax", pharmacy_name="Walgreens", price=28)
Walmart93 = Price(drug_name="Ex-Lax", pharmacy_name="Walmart", price=73)
Wegmans93 = Price(drug_name="Ex-Lax", pharmacy_name="Wegmans", price=87)
CVS94 = Price(drug_name="Senna Lax", pharmacy_name="CVS", price=25)
Walgreens94 = Price(drug_name="Senna Lax", pharmacy_name="Walgreens", price=89)

Walmart94 = Price(drug_name="Senna Lax", pharmacy_name="Walmart", price=66)
Wegmans94 = Price(drug_name="Senna Lax", pharmacy_name="Wegmans", price=4)
CVS95 = Price(drug_name="NovoLog", pharmacy_name="CVS", price=90)
Walgreens95 = Price(drug_name="NovoLog", pharmacy_name="Walgreens", price=71)
Walmart95 = Price(drug_name="NovoLog", pharmacy_name="Walmart", price=100)
Wegmans95 = Price(drug_name="NovoLog", pharmacy_name="Wegmans", price=22)
CVS96 = Price(drug_name="Bayer", pharmacy_name="CVS", price=96)
Walgreens96 = Price(drug_name="Bayer", pharmacy_name="Walgreens", price=85)
Walmart96 = Price(drug_name="Bayer", pharmacy_name="Walmart", price=31)
Wegmans96 = Price(drug_name="Bayer", pharmacy_name="Wegmans", price=26)
CVS97 = Price(drug_name="Ecotrin", pharmacy_name="CVS", price=24)
Walgreens97 = Price(drug_name="Ecotrin", pharmacy_name="Walgreens", price=48)
Walmart97 = Price(drug_name="Ecotrin", pharmacy_name="Walmart", price=56)
Wegmans97 = Price(drug_name="Ecotrin", pharmacy_name="Wegmans", price=7)
CVS98 = Price(drug_name="Bufferin", pharmacy_name="CVS", price=57)
Walgreens98 = Price(drug_name="Bufferin", pharmacy_name="Walgreens", price=71)
Walmart98 = Price(drug_name="Bufferin", pharmacy_name="Walmart", price=66)
Wegmans98 = Price(drug_name="Bufferin", pharmacy_name="Wegmans", price=56)
CVS99 = Price(drug_name="Lioresal", pharmacy_name="CVS", price=58)
Walgreens99 = Price(drug_name="Lioresal", pharmacy_name="Walgreens", price=72)
Walmart99 = Price(drug_name="Lioresal", pharmacy_name="Walmart", price=29)
Wegmans99 = Price(drug_name="Lioresal", pharmacy_name="Wegmans", price=38)
CVS100 = Price(drug_name="Flagyl", pharmacy_name="CVS", price=53)
Walgreens100 = Price(drug_name="Flagyl", pharmacy_name="Walgreens", price=5)
Walmart100 = Price(drug_name="Flagyl", pharmacy_name="Walmart", price=10)
Wegmans100 = Price(drug_name="Flagyl", pharmacy_name="Wegmans", price=84)
CVS101 = Price(drug_name="Keppra", pharmacy_name="CVS", price=99)
Walgreens101 = Price(drug_name="Keppra", pharmacy_name="Walgreens", price=54)
Walmart101 = Price(drug_name="Keppra", pharmacy_name="Walmart", price=98)
Wegmans101 = Price(drug_name="Keppra", pharmacy_name="Wegmans", price=34)
CVS102 = Price(drug_name="Colcrys", pharmacy_name="CVS", price=98)
Walgreens102 = Price(drug_name="Colcrys", pharmacy_name="Walgreens", price=82)
Walmart102 = Price(drug_name="Colcrys", pharmacy_name="Walmart", price=28)
Wegmans102 = Price(drug_name="Colcrys", pharmacy_name="Wegmans", price=100)
CVS103 = Price(drug_name="Mitigare", pharmacy_name="CVS", price=60)
Walgreens103 = Price(drug_name="Mitigare", pharmacy_name="Walgreens", price=96)

Walmart103 = Price(drug_name="Mitigare", pharmacy_name="Walmart", price=29)
Wegmans103 = Price(drug_name="Mitigare", pharmacy_name="Wegmans", price=99)
CVS104 = Price(drug_name="Zyprexa", pharmacy_name="CVS", price=78)
Walgreens104 = Price(drug_name="Zyprexa", pharmacy_name="Walgreens", price=9)
Walmart104 = Price(drug_name="Zyprexa", pharmacy_name="Walmart", price=37)
Wegmans104 = Price(drug_name="Zyprexa", pharmacy_name="Wegmans", price=92)
CVS105 = Price(drug_name="Avodart", pharmacy_name="CVS", price=19)
Walgreens105 = Price(drug_name="Avodart", pharmacy_name="Walgreens", price=18)
Walmart105 = Price(drug_name="Avodart", pharmacy_name="Walmart", price=12)
Wegmans105 = Price(drug_name="Avodart", pharmacy_name="Wegmans", price=83)
CVS106 = Price(drug_name="TriCor", pharmacy_name="CVS", price=42)
Walgreens106 = Price(drug_name="TriCor", pharmacy_name="Walgreens", price=28)
Walmart106 = Price(drug_name="TriCor", pharmacy_name="Walmart", price=86)
Wegmans106 = Price(drug_name="TriCor", pharmacy_name="Wegmans", price=7)
CVS107 = Price(drug_name="Antara", pharmacy_name="CVS", price=26)
Walgreens107 = Price(drug_name="Antara", pharmacy_name="Walgreens", price=49)
Walmart107 = Price(drug_name="Antara", pharmacy_name="Walmart", price=30)
Wegmans107 = Price(drug_name="Antara", pharmacy_name="Wegmans", price=54)
CVS108 = Price(drug_name="Cardura", pharmacy_name="CVS", price=26)
Walgreens108 = Price(drug_name="Cardura", pharmacy_name="Walgreens", price=77)
Walmart108 = Price(drug_name="Cardura", pharmacy_name="Walmart", price=19)
Wegmans108 = Price(drug_name="Cardura", pharmacy_name="Wegmans", price=26)
CVS109 = Price(drug_name="Aleve", pharmacy_name="CVS", price=70)
Walgreens109 = Price(drug_name="Aleve", pharmacy_name="Walgreens", price=35)
Walmart109 = Price(drug_name="Aleve", pharmacy_name="Walmart", price=5)
Wegmans109 = Price(drug_name="Aleve", pharmacy_name="Wegmans", price=4)
CVS110 = Price(drug_name="Aldactone", pharmacy_name="CVS", price=36)
Walgreens110 = Price(drug_name="Aldactone",
                     pharmacy_name="Walgreens", price=33)
Walmart110 = Price(drug_name="Aldactone", pharmacy_name="Walmart", price=90)
Wegmans110 = Price(drug_name="Aldactone", pharmacy_name="Wegmans", price=27)
CVS111 = Price(drug_name="Namenda", pharmacy_name="CVS", price=69)
Walgreens111 = Price(drug_name="Namenda", pharmacy_name="Walgreens", price=10)
Walmart111 = Price(drug_name="Namenda", pharmacy_name="Walmart", price=31)
Wegmans111 = Price(drug_name="Namenda", pharmacy_name="Wegmans", price=97)
CVS112 = Price(drug_name="Methadose", pharmacy_name="CVS", price=74)
Walgreens112 = Price(drug_name="Methadose",
                     pharmacy_name="Walgreens", price=99)
Walmart112 = Price(drug_name="Methadose", pharmacy_name="Walmart", price=47)
Wegmans112 = Price(drug_name="Methadose", pharmacy_name="Wegmans", price=97)
CVS113 = Price(drug_name="Vasotec", pharmacy_name="CVS", price=26)
Walgreens113 = Price(drug_name="Vasotec", pharmacy_name="Walgreens", price=50)
Walmart113 = Price(drug_name="Vasotec", pharmacy_name="Walmart", price=8)
Wegmans113 = Price(drug_name="Vasotec", pharmacy_name="Wegmans", price=43)
CVS114 = Price(drug_name="Epaned", pharmacy_name="CVS", price=76)
Walgreens114 = Price(drug_name="Epaned", pharmacy_name="Walgreens", price=73)
Walmart114 = Price(drug_name="Epaned", pharmacy_name="Walmart", price=46)
Wegmans114 = Price(drug_name="Epaned", pharmacy_name="Wegmans", price=27)
CVS115 = Price(drug_name="Tamiflu", pharmacy_name="CVS", price=40)
Walgreens115 = Price(drug_name="Tamiflu", pharmacy_name="Walgreens", price=37)
Walmart115 = Price(drug_name="Tamiflu", pharmacy_name="Walmart", price=29)
Wegmans115 = Price(drug_name="Tamiflu", pharmacy_name="Wegmans", price=27)
CVS116 = Price(drug_name="Requip", pharmacy_name="CVS", price=66)
Walgreens116 = Price(drug_name="Requip", pharmacy_name="Walgreens", price=23)
Walmart116 = Price(drug_name="Requip", pharmacy_name="Walmart", price=99)
Wegmans116 = Price(drug_name="Requip", pharmacy_name="Wegmans", price=13)
CVS117 = Price(drug_name="PC Pen VK", pharmacy_name="CVS", price=45)
Walgreens117 = Price(drug_name="PC Pen VK",
                     pharmacy_name="Walgreens", price=70)
Walmart117 = Price(drug_name="PC Pen VK", pharmacy_name="Walmart", price=99)
Wegmans117 = Price(drug_name="PC Pen VK", pharmacy_name="Wegmans", price=9)
CVS118 = Price(drug_name="Pen V", pharmacy_name="CVS", price=59)
Walgreens118 = Price(drug_name="Pen V", pharmacy_name="Walgreens", price=33)
Walmart118 = Price(drug_name="Pen V", pharmacy_name="Walmart", price=22)
Wegmans118 = Price(drug_name="Pen V", pharmacy_name="Wegmans", price=11)
CVS119 = Price(drug_name="Strattera", pharmacy_name="CVS", price=69)
Walgreens119 = Price(drug_name="Strattera",
                     pharmacy_name="Walgreens", price=46)
Walmart119 = Price(drug_name="Strattera", pharmacy_name="Walmart", price=43)
Wegmans119 = Price(drug_name="Strattera", pharmacy_name="Wegmans", price=4)
CVS120 = Price(drug_name="Ambien", pharmacy_name="CVS", price=91)
Walgreens120 = Price(drug_name="Ambien", pharmacy_name="Walgreens", price=76)
Walmart120 = Price(drug_name="Ambien", pharmacy_name="Walmart", price=78)
Wegmans120 = Price(drug_name="Ambien", pharmacy_name="Wegmans", price=37)
CVS121 = Price(drug_name="Advair", pharmacy_name="CVS", price=23)
Walgreens121 = Price(drug_name="Advair", pharmacy_name="Walgreens", price=40)
Walmart121 = Price(drug_name="Advair", pharmacy_name="Walmart", price=70)
Wegmans121 = Price(drug_name="Advair", pharmacy_name="Wegmans", price=17)
CVS122 = Price(drug_name="Levaquin", pharmacy_name="CVS", price=7)
Walgreens122 = Price(drug_name="Levaquin",
                     pharmacy_name="Walgreens", price=68)

Walmart122 = Price(drug_name="Levaquin", pharmacy_name="Walmart", price=22)
Wegmans122 = Price(drug_name="Levaquin", pharmacy_name="Wegmans", price=62)
CVS123 = Price(drug_name="Tofranil", pharmacy_name="CVS", price=80)
Walgreens123 = Price(drug_name="Tofranil",
                     pharmacy_name="Walgreens", price=30)

Walmart123 = Price(drug_name="Tofranil", pharmacy_name="Walmart", price=28)
Wegmans123 = Price(drug_name="Tofranil", pharmacy_name="Wegmans", price=7)
CVS124 = Price(drug_name="Reclast", pharmacy_name="CVS", price=19)
Walgreens124 = Price(drug_name="Reclast", pharmacy_name="Walgreens", price=42)
Walmart124 = Price(drug_name="Reclast", pharmacy_name="Walmart", price=24)
Wegmans124 = Price(drug_name="Reclast", pharmacy_name="Wegmans", price=78)
CVS125 = Price(drug_name="Zometa", pharmacy_name="CVS", price=46)
Walgreens125 = Price(drug_name="Zometa", pharmacy_name="Walgreens", price=58)
Walmart125 = Price(drug_name="Zometa", pharmacy_name="Walmart", price=1)
Wegmans125 = Price(drug_name="Zometa", pharmacy_name="Wegmans", price=68)
CVS126 = Price(drug_name="Glucotrol", pharmacy_name="CVS", price=47)
Walgreens126 = Price(drug_name="Glucotrol",
                     pharmacy_name="Walgreens", price=79)
Walmart126 = Price(drug_name="Glucotrol", pharmacy_name="Walmart", price=13)
Wegmans126 = Price(drug_name="Glucotrol", pharmacy_name="Wegmans", price=2)
CVS127 = Price(drug_name="Constulose", pharmacy_name="CVS", price=96)
Walgreens127 = Price(drug_name="Constulose",
                     pharmacy_name="Walgreens", price=100)
Walmart127 = Price(drug_name="Constulose", pharmacy_name="Walmart", price=94)
Wegmans127 = Price(drug_name="Constulose", pharmacy_name="Wegmans", price=98)
CVS128 = Price(drug_name="AcipHex", pharmacy_name="CVS", price=75)
Walgreens128 = Price(drug_name="AcipHex", pharmacy_name="Walgreens", price=74)
Walmart128 = Price(drug_name="AcipHex", pharmacy_name="Walmart", price=84)
Wegmans128 = Price(drug_name="AcipHex", pharmacy_name="Wegmans", price=22)
CVS129 = Price(drug_name="Otrexup", pharmacy_name="CVS", price=79)
Walgreens129 = Price(drug_name="Otrexup", pharmacy_name="Walgreens", price=9)
Walmart129 = Price(drug_name="Otrexup", pharmacy_name="Walmart", price=2)
Wegmans129 = Price(drug_name="Otrexup", pharmacy_name="Wegmans", price=43)
CVS130 = Price(drug_name="Cleocin", pharmacy_name="CVS", price=23)
Walgreens130 = Price(drug_name="Cleocin", pharmacy_name="Walgreens", price=10)
Walmart130 = Price(drug_name="Cleocin", pharmacy_name="Walmart", price=25)
Wegmans130 = Price(drug_name="Cleocin", pharmacy_name="Wegmans", price=24)
CVS131 = Price(drug_name="Tylenol", pharmacy_name="CVS", price=69)
Walgreens131 = Price(drug_name="Tylenol", pharmacy_name="Walgreens", price=53)
Walmart131 = Price(drug_name="Tylenol", pharmacy_name="Walmart", price=13)
Wegmans131 = Price(drug_name="Tylenol", pharmacy_name="Wegmans", price=24)
CVS132 = Price(drug_name="Feosol", pharmacy_name="CVS", price=71)
Walgreens132 = Price(drug_name="Feosol", pharmacy_name="Walgreens", price=43)
Walmart132 = Price(drug_name="Feosol", pharmacy_name="Walmart", price=15)
Wegmans132 = Price(drug_name="Feosol", pharmacy_name="Wegmans", price=73)
CVS133 = Price(drug_name="Relpax", pharmacy_name="CVS", price=31)
Walgreens133 = Price(drug_name="Relpax", pharmacy_name="Walgreens", price=14)
Walmart133 = Price(drug_name="Relpax", pharmacy_name="Walmart", price=50)
Wegmans133 = Price(drug_name="Relpax", pharmacy_name="Wegmans", price=17)
CVS134 = Price(drug_name="Carbacot", pharmacy_name="CVS", price=6)
Walgreens134 = Price(drug_name="Carbacot",
                     pharmacy_name="Walgreens", price=44)

Walmart134 = Price(drug_name="Carbacot", pharmacy_name="Walmart", price=1)
Wegmans134 = Price(drug_name="Carbacot", pharmacy_name="Wegmans", price=42)
CVS135 = Price(drug_name="Robaxin", pharmacy_name="CVS", price=46)
Walgreens135 = Price(drug_name="Robaxin", pharmacy_name="Walgreens", price=98)
Walmart135 = Price(drug_name="Robaxin", pharmacy_name="Walmart", price=33)
Wegmans135 = Price(drug_name="Robaxin", pharmacy_name="Wegmans", price=36)
CVS136 = Price(drug_name="DiaBeta", pharmacy_name="CVS", price=73)
Walgreens136 = Price(drug_name="DiaBeta", pharmacy_name="Walgreens", price=59)
Walmart136 = Price(drug_name="DiaBeta", pharmacy_name="Walmart", price=47)
Wegmans136 = Price(drug_name="DiaBeta", pharmacy_name="Wegmans", price=48)
CVS137 = Price(drug_name="Celexa", pharmacy_name="CVS", price=16)
Walgreens137 = Price(drug_name="Celexa", pharmacy_name="Walgreens", price=45)
Walmart137 = Price(drug_name="Celexa", pharmacy_name="Walmart", price=46)
Wegmans137 = Price(drug_name="Celexa", pharmacy_name="Wegmans", price=97)
CVS138 = Price(drug_name="Benicar", pharmacy_name="CVS", price=27)
Walgreens138 = Price(drug_name="Benicar", pharmacy_name="Walgreens", price=27)
Walmart138 = Price(drug_name="Benicar", pharmacy_name="Walmart", price=73)
Wegmans138 = Price(drug_name="Benicar", pharmacy_name="Wegmans", price=92)
CVS139 = Price(drug_name="Coreg", pharmacy_name="CVS", price=44)
Walgreens139 = Price(drug_name="Coreg", pharmacy_name="Walgreens", price=36)
Walmart139 = Price(drug_name="Coreg", pharmacy_name="Walmart", price=78)
Wegmans139 = Price(drug_name="Coreg", pharmacy_name="Wegmans", price=100)
CVS140 = Price(drug_name="Spiriva", pharmacy_name="CVS", price=74)
Walgreens140 = Price(drug_name="Spiriva", pharmacy_name="Walgreens", price=73)
Walmart140 = Price(drug_name="Spiriva", pharmacy_name="Walmart", price=2)
Wegmans140 = Price(drug_name="Spiriva", pharmacy_name="Wegmans", price=58)
CVS141 = Price(drug_name="Xolair", pharmacy_name="CVS", price=42)
Walgreens141 = Price(drug_name="Xolair", pharmacy_name="Walgreens", price=1)
Walmart141 = Price(drug_name="Xolair", pharmacy_name="Walmart", price=36)
Wegmans141 = Price(drug_name="Xolair", pharmacy_name="Wegmans", price=46)
CVS142 = Price(drug_name="NitroStat Sublingual",
               pharmacy_name="CVS", price=22)

Walgreens142 = Price(drug_name="NitroStat Sublingual",
                     pharmacy_name="Walgreens", price=37)
Walmart142 = Price(drug_name="NitroStat Sublingual",
                   pharmacy_name="Walmart", price=50)
Wegmans142 = Price(drug_name="NitroStat Sublingual",
                   pharmacy_name="Wegmans", price=46)
CVS143 = Price(drug_name="Eliquis", pharmacy_name="CVS", price=91)
Walgreens143 = Price(drug_name="Eliquis", pharmacy_name="Walgreens", price=51)
Walmart143 = Price(drug_name="Eliquis", pharmacy_name="Walmart", price=40)
Wegmans143 = Price(drug_name="Eliquis", pharmacy_name="Wegmans", price=38)
CVS144 = Price(drug_name="Neurontin", pharmacy_name="CVS", price=20)
Walgreens144 = Price(drug_name="Neurontin",
                     pharmacy_name="Walgreens", price=9)

Walmart144 = Price(drug_name="Neurontin", pharmacy_name="Walmart", price=30)
Wegmans144 = Price(drug_name="Neurontin", pharmacy_name="Wegmans", price=79)
CVS145 = Price(drug_name="Enbrel", pharmacy_name="CVS", price=40)
Walgreens145 = Price(drug_name="Enbrel", pharmacy_name="Walgreens", price=32)
Walmart145 = Price(drug_name="Enbrel", pharmacy_name="Walmart", price=10)
Wegmans145 = Price(drug_name="Enbrel", pharmacy_name="Wegmans", price=45)
CVS146 = Price(drug_name="Herceptin", pharmacy_name="CVS", price=55)
Walgreens146 = Price(drug_name="Herceptin",
                     pharmacy_name="Walgreens", price=39)
Walmart146 = Price(drug_name="Herceptin", pharmacy_name="Walmart", price=59)
Wegmans146 = Price(drug_name="Herceptin", pharmacy_name="Wegmans", price=64)
CVS147 = Price(drug_name="Atripla", pharmacy_name="CVS", price=66)
Walgreens147 = Price(drug_name="Atripla", pharmacy_name="Walgreens", price=66)
Walmart147 = Price(drug_name="Atripla", pharmacy_name="Walmart", price=22)
Wegmans147 = Price(drug_name="Atripla", pharmacy_name="Wegmans", price=19)
CVS148 = Price(drug_name="Xarelto", pharmacy_name="CVS", price=34)
Walgreens148 = Price(drug_name="Xarelto", pharmacy_name="Walgreens", price=92)
Walmart148 = Price(drug_name="Xarelto", pharmacy_name="Walmart", price=45)
Wegmans148 = Price(drug_name="Xarelto", pharmacy_name="Wegmans", price=90)
CVS149 = Price(drug_name="Stalevo 50", pharmacy_name="CVS", price=22)
Walgreens149 = Price(drug_name="Stalevo 50",
                     pharmacy_name="Walgreens", price=83)
Walmart149 = Price(drug_name="Stalevo 50", pharmacy_name="Walmart", price=23)
Wegmans149 = Price(drug_name="Stalevo 50", pharmacy_name="Wegmans", price=72)
CVS150 = Price(drug_name="Fioricet", pharmacy_name="CVS", price=42)
Walgreens150 = Price(drug_name="Fioricet",
                     pharmacy_name="Walgreens", price=22)

Walmart150 = Price(drug_name="Fioricet", pharmacy_name="Walmart", price=13)
Wegmans150 = Price(drug_name="Fioricet", pharmacy_name="Wegmans", price=12)
CVS151 = Price(drug_name="Levemir", pharmacy_name="CVS", price=31)
Walgreens151 = Price(drug_name="Levemir", pharmacy_name="Walgreens", price=12)
Walmart151 = Price(drug_name="Levemir", pharmacy_name="Walmart", price=34)
Wegmans151 = Price(drug_name="Levemir", pharmacy_name="Wegmans", price=40)
CVS152 = Price(drug_name="Lovenox", pharmacy_name="CVS", price=1)
Walgreens152 = Price(drug_name="Lovenox", pharmacy_name="Walgreens", price=76)
Walmart152 = Price(drug_name="Lovenox", pharmacy_name="Walmart", price=44)
Wegmans152 = Price(drug_name="Lovenox", pharmacy_name="Wegmans", price=90)
CVS153 = Price(drug_name="Ritalin", pharmacy_name="CVS", price=96)
Walgreens153 = Price(drug_name="Ritalin", pharmacy_name="Walgreens", price=5)
Walmart153 = Price(drug_name="Ritalin", pharmacy_name="Walmart", price=19)
Wegmans153 = Price(drug_name="Ritalin", pharmacy_name="Wegmans", price=94)
CVS154 = Price(drug_name="Concerta", pharmacy_name="CVS", price=12)
Walgreens154 = Price(drug_name="Concerta",
                     pharmacy_name="Walgreens", price=67)

Walmart154 = Price(drug_name="Concerta", pharmacy_name="Walmart", price=86)
Wegmans154 = Price(drug_name="Concerta", pharmacy_name="Wegmans", price=59)
CVS155 = Price(drug_name="Crestor", pharmacy_name="CVS", price=40)
Walgreens155 = Price(drug_name="Crestor", pharmacy_name="Walgreens", price=84)
Walmart155 = Price(drug_name="Crestor", pharmacy_name="Walmart", price=99)
Wegmans155 = Price(drug_name="Crestor", pharmacy_name="Wegmans", price=95)
CVS156 = Price(drug_name="Xgeva", pharmacy_name="CVS", price=39)
Walgreens156 = Price(drug_name="Xgeva", pharmacy_name="Walgreens", price=6)
Walmart156 = Price(drug_name="Xgeva", pharmacy_name="Walmart", price=33)
Wegmans156 = Price(drug_name="Xgeva", pharmacy_name="Wegmans", price=61)
CVS157 = Price(drug_name="Prolia", pharmacy_name="CVS", price=98)
Walgreens157 = Price(drug_name="Prolia", pharmacy_name="Walgreens", price=78)
Walmart157 = Price(drug_name="Prolia", pharmacy_name="Walmart", price=90)
Wegmans157 = Price(drug_name="Prolia", pharmacy_name="Wegmans", price=90)
CVS158 = Price(drug_name="Pradaxa", pharmacy_name="CVS", price=62)
Walgreens158 = Price(drug_name="Pradaxa", pharmacy_name="Walgreens", price=72)
Walmart158 = Price(drug_name="Pradaxa", pharmacy_name="Walmart", price=61)
Wegmans158 = Price(drug_name="Pradaxa", pharmacy_name="Wegmans", price=46)
CVS159 = Price(drug_name="Sensipar", pharmacy_name="CVS", price=95)
Walgreens159 = Price(drug_name="Sensipar",
                     pharmacy_name="Walgreens", price=27)

Walmart159 = Price(drug_name="Sensipar", pharmacy_name="Walmart", price=81)
Wegmans159 = Price(drug_name="Sensipar", pharmacy_name="Wegmans", price=17)
CVS160 = Price(drug_name="Vesicare", pharmacy_name="CVS", price=39)
Walgreens160 = Price(drug_name="Vesicare",
                     pharmacy_name="Walgreens", price=38)

Walmart160 = Price(drug_name="Vesicare", pharmacy_name="Walmart", price=41)
Wegmans160 = Price(drug_name="Vesicare", pharmacy_name="Wegmans", price=5)
CVS161 = Price(drug_name="Haldol", pharmacy_name="CVS", price=13)
Walgreens161 = Price(drug_name="Haldol", pharmacy_name="Walgreens", price=90)
Walmart161 = Price(drug_name="Haldol", pharmacy_name="Walmart", price=77)
Wegmans161 = Price(drug_name="Haldol", pharmacy_name="Wegmans", price=15)
CVS162 = Price(drug_name="Ala-Cort", pharmacy_name="CVS", price=53)
Walgreens162 = Price(drug_name="Ala-Cort",
                     pharmacy_name="Walgreens", price=73)

Walmart162 = Price(drug_name="Ala-Cort", pharmacy_name="Walmart", price=6)
Wegmans162 = Price(drug_name="Ala-Cort", pharmacy_name="Wegmans", price=43)
CVS163 = Price(drug_name="HumuLIN", pharmacy_name="CVS", price=35)
Walgreens163 = Price(drug_name="HumuLIN", pharmacy_name="Walgreens", price=80)
Walmart163 = Price(drug_name="HumuLIN", pharmacy_name="Walmart", price=77)
Wegmans163 = Price(drug_name="HumuLIN", pharmacy_name="Wegmans", price=96)
CVS164 = Price(drug_name="Isentress", pharmacy_name="CVS", price=53)
Walgreens164 = Price(drug_name="Isentress",
                     pharmacy_name="Walgreens", price=71)
Walmart164 = Price(drug_name="Isentress", pharmacy_name="Walmart", price=68)
Wegmans164 = Price(drug_name="Isentress", pharmacy_name="Wegmans", price=71)
CVS165 = Price(drug_name="Stelara", pharmacy_name="CVS", price=99)
Walgreens165 = Price(drug_name="Stelara", pharmacy_name="Walgreens", price=86)
Walmart165 = Price(drug_name="Stelara", pharmacy_name="Walmart", price=97)
Wegmans165 = Price(drug_name="Stelara", pharmacy_name="Wegmans", price=66)
CVS166 = Price(drug_name="Mobic", pharmacy_name="CVS", price=45)
Walgreens166 = Price(drug_name="Mobic", pharmacy_name="Walgreens", price=28)
Walmart166 = Price(drug_name="Mobic", pharmacy_name="Walmart", price=23)
Wegmans166 = Price(drug_name="Mobic", pharmacy_name="Wegmans", price=55)
CVS167 = Price(drug_name="Remicade", pharmacy_name="CVS", price=16)
Walgreens167 = Price(drug_name="Remicade",
                     pharmacy_name="Walgreens", price=31)

Walmart167 = Price(drug_name="Remicade", pharmacy_name="Walmart", price=63)
Wegmans167 = Price(drug_name="Remicade", pharmacy_name="Wegmans", price=42)
CVS168 = Price(drug_name="Night Time", pharmacy_name="CVS", price=100)
Walgreens168 = Price(drug_name="Night Time", pharmacy_name="Walgreens", price=47
                     )
Walmart168 = Price(drug_name="Night Time", pharmacy_name="Walmart", price=12)
Wegmans168 = Price(drug_name="Night Time", pharmacy_name="Wegmans", price=100)
CVS169 = Price(drug_name="Renvela", pharmacy_name="CVS", price=62)
Walgreens169 = Price(drug_name="Renvela", pharmacy_name="Walgreens", price=7)
Walmart169 = Price(drug_name="Renvela", pharmacy_name="Walmart", price=44)
Wegmans169 = Price(drug_name="Renvela", pharmacy_name="Wegmans", price=35)
CVS170 = Price(drug_name="Fragmin", pharmacy_name="CVS", price=18)
Walgreens170 = Price(drug_name="Fragmin", pharmacy_name="Walgreens", price=92)
Walmart170 = Price(drug_name="Fragmin", pharmacy_name="Walmart", price=6)
Wegmans170 = Price(drug_name="Fragmin", pharmacy_name="Wegmans", price=53)
CVS171 = Price(drug_name="Zoloft", pharmacy_name="CVS", price=51)
Walgreens171 = Price(drug_name="Zoloft", pharmacy_name="Walgreens", price=80)
Walmart171 = Price(drug_name="Zoloft", pharmacy_name="Walmart", price=56)
Wegmans171 = Price(drug_name="Zoloft", pharmacy_name="Wegmans", price=30)
CVS172 = Price(drug_name="Klonopin", pharmacy_name="CVS", price=52)
Walgreens172 = Price(drug_name="Klonopin",
                     pharmacy_name="Walgreens", price=23)

Walmart172 = Price(drug_name="Klonopin", pharmacy_name="Walmart", price=10)
Wegmans172 = Price(drug_name="Klonopin", pharmacy_name="Wegmans", price=87)
CVS173 = Price(drug_name="Avalide", pharmacy_name="CVS", price=9)
Walgreens173 = Price(drug_name="Avalide", pharmacy_name="Walgreens", price=33)
Walmart173 = Price(drug_name="Avalide", pharmacy_name="Walmart", price=37)
Wegmans173 = Price(drug_name="Avalide", pharmacy_name="Wegmans", price=39)
CVS174 = Price(drug_name="Ceftin", pharmacy_name="CVS", price=60)
Walgreens174 = Price(drug_name="Ceftin", pharmacy_name="Walgreens", price=27)
Walmart174 = Price(drug_name="Ceftin", pharmacy_name="Walmart", price=67)
Wegmans174 = Price(drug_name="Ceftin", pharmacy_name="Wegmans", price=57)
CVS175 = Price(drug_name="Nizoral Topical", pharmacy_name="CVS", price=87)
Walgreens175 = Price(drug_name="Nizoral Topical",
                     pharmacy_name="Walgreens", price=1)
Walmart175 = Price(drug_name="Nizoral Topical",
                   pharmacy_name="Walmart", price=38)
Wegmans175 = Price(drug_name="Nizoral Topical",
                   pharmacy_name="Wegmans", price=36)
CVS176 = Price(drug_name="Lyrica", pharmacy_name="CVS", price=43)
Walgreens176 = Price(drug_name="Lyrica", pharmacy_name="Walgreens", price=16)
Walmart176 = Price(drug_name="Lyrica", pharmacy_name="Walmart", price=65)
Wegmans176 = Price(drug_name="Lyrica", pharmacy_name="Wegmans", price=26)
CVS177 = Price(drug_name="Nexium", pharmacy_name="CVS", price=54)
Walgreens177 = Price(drug_name="Nexium", pharmacy_name="Walgreens", price=14)
Walmart177 = Price(drug_name="Nexium", pharmacy_name="Walmart", price=88)
Wegmans177 = Price(drug_name="Nexium", pharmacy_name="Wegmans", price=38)
CVS178 = Price(drug_name="Combivent Respimat", pharmacy_name="CVS", price=74)
Walgreens178 = Price(drug_name="Combivent Respimat", pharmacy_name="Walgreens",
                     price=34)
Walmart178 = Price(drug_name="Combivent Respimat",
                   pharmacy_name="Walmart", price=48)
Wegmans178 = Price(drug_name="Combivent Respimat",
                   pharmacy_name="Wegmans", price=60)
CVS179 = Price(drug_name="Niaspan", pharmacy_name="CVS", price=19)
Walgreens179 = Price(drug_name="Niaspan", pharmacy_name="Walgreens", price=92)
Walmart179 = Price(drug_name="Niaspan", pharmacy_name="Walmart", price=85)
Wegmans179 = Price(drug_name="Niaspan", pharmacy_name="Wegmans", price=80)
CVS180 = Price(drug_name="Uroxatral", pharmacy_name="CVS", price=9)
Walgreens180 = Price(drug_name="Uroxatral",
                     pharmacy_name="Walgreens", price=40)
Walmart180 = Price(drug_name="Uroxatral", pharmacy_name="Walmart", price=45)
Wegmans180 = Price(drug_name="Uroxatral", pharmacy_name="Wegmans", price=2)
CVS181 = Price(drug_name="Biaxin", pharmacy_name="CVS", price=87)
Walgreens181 = Price(drug_name="Biaxin", pharmacy_name="Walgreens", price=7)
Walmart181 = Price(drug_name="Biaxin", pharmacy_name="Walmart", price=57)
Wegmans181 = Price(drug_name="Biaxin", pharmacy_name="Wegmans", price=16)
CVS182 = Price(drug_name="Zomig", pharmacy_name="CVS", price=89)
Walgreens182 = Price(drug_name="Zomig", pharmacy_name="Walgreens", price=85)
Walmart182 = Price(drug_name="Zomig", pharmacy_name="Walmart", price=2)
Wegmans182 = Price(drug_name="Zomig", pharmacy_name="Wegmans", price=53)
CVS183 = Price(drug_name="Invokana", pharmacy_name="CVS", price=48)
Walgreens183 = Price(drug_name="Invokana",
                     pharmacy_name="Walgreens", price=57)

Walmart183 = Price(drug_name="Invokana", pharmacy_name="Walmart", price=39)
Wegmans183 = Price(drug_name="Invokana", pharmacy_name="Wegmans", price=29)
CVS184 = Price(drug_name="Saxenda", pharmacy_name="CVS", price=60)
Walgreens184 = Price(drug_name="Saxenda", pharmacy_name="Walgreens", price=42)
Walmart184 = Price(drug_name="Saxenda", pharmacy_name="Walmart", price=70)
Wegmans184 = Price(drug_name="Saxenda", pharmacy_name="Wegmans", price=51)
CVS185 = Price(drug_name="Victoza", pharmacy_name="CVS", price=15)
Walgreens185 = Price(drug_name="Victoza", pharmacy_name="Walgreens", price=51)
Walmart185 = Price(drug_name="Victoza", pharmacy_name="Walmart", price=36)
Wegmans185 = Price(drug_name="Victoza", pharmacy_name="Wegmans", price=26)
CVS186 = Price(drug_name="Alimta", pharmacy_name="CVS", price=30)
Walgreens186 = Price(drug_name="Alimta", pharmacy_name="Walgreens", price=42)
Walmart186 = Price(drug_name="Alimta", pharmacy_name="Walmart", price=81)
Wegmans186 = Price(drug_name="Alimta", pharmacy_name="Wegmans", price=84)
CVS187 = Price(drug_name="Lotrisone", pharmacy_name="CVS", price=42)
Walgreens187 = Price(drug_name="Lotrisone",
                     pharmacy_name="Walgreens", price=33)
Walmart187 = Price(drug_name="Lotrisone", pharmacy_name="Walmart", price=21)
Wegmans187 = Price(drug_name="Lotrisone", pharmacy_name="Wegmans", price=14)
CVS188 = Price(drug_name="Avastin", pharmacy_name="CVS", price=83)
Walgreens188 = Price(drug_name="Avastin", pharmacy_name="Walgreens", price=83)
Walmart188 = Price(drug_name="Avastin", pharmacy_name="Walmart", price=86)
Wegmans188 = Price(drug_name="Avastin", pharmacy_name="Wegmans", price=4)
CVS189 = Price(drug_name="Sovaldi", pharmacy_name="CVS", price=55)
Walgreens189 = Price(drug_name="Sovaldi", pharmacy_name="Walgreens", price=75)
Walmart189 = Price(drug_name="Sovaldi", pharmacy_name="Walmart", price=64)
Wegmans189 = Price(drug_name="Sovaldi", pharmacy_name="Wegmans", price=5)
CVS190 = Price(drug_name="Gilenya", pharmacy_name="CVS", price=62)
Walgreens190 = Price(drug_name="Gilenya", pharmacy_name="Walgreens", price=20)
Walmart190 = Price(drug_name="Gilenya", pharmacy_name="Walmart", price=35)
Wegmans190 = Price(drug_name="Gilenya", pharmacy_name="Wegmans", price=34)
CVS191 = Price(drug_name="Epogen", pharmacy_name="CVS", price=63)
Walgreens191 = Price(drug_name="Epogen", pharmacy_name="Walgreens", price=83)
Walmart191 = Price(drug_name="Epogen", pharmacy_name="Walmart", price=99)
Wegmans191 = Price(drug_name="Epogen", pharmacy_name="Wegmans", price=11)
CVS192 = Price(drug_name="Seroquel", pharmacy_name="CVS", price=19)
Walgreens192 = Price(drug_name="Seroquel",
                     pharmacy_name="Walgreens", price=64)

Walmart192 = Price(drug_name="Seroquel", pharmacy_name="Walmart", price=36)
Wegmans192 = Price(drug_name="Seroquel", pharmacy_name="Wegmans", price=75)
CVS193 = Price(drug_name="Amaryl", pharmacy_name="CVS", price=49)
Walgreens193 = Price(drug_name="Amaryl", pharmacy_name="Walgreens", price=88)
Walmart193 = Price(drug_name="Amaryl", pharmacy_name="Walmart", price=78)
Wegmans193 = Price(drug_name="Amaryl", pharmacy_name="Wegmans", price=82)
CVS194 = Price(drug_name="Percocet", pharmacy_name="CVS", price=5)
Walgreens194 = Price(drug_name="Percocet",
                     pharmacy_name="Walgreens", price=94)

Walmart194 = Price(drug_name="Percocet", pharmacy_name="Walmart", price=43)
Wegmans194 = Price(drug_name="Percocet", pharmacy_name="Wegmans", price=41)
CVS195 = Price(drug_name="SandIMMUNE", pharmacy_name="CVS", price=83)
Walgreens195 = Price(drug_name="SandIMMUNE",
                     pharmacy_name="Walgreens", price=81)
Walmart195 = Price(drug_name="SandIMMUNE", pharmacy_name="Walmart", price=1)
Wegmans195 = Price(drug_name="SandIMMUNE", pharmacy_name="Wegmans", price=24)
CVS196 = Price(drug_name="Neoral", pharmacy_name="CVS", price=74)
Walgreens196 = Price(drug_name="Neoral", pharmacy_name="Walgreens", price=76)
Walmart196 = Price(drug_name="Neoral", pharmacy_name="Walmart", price=43)
Wegmans196 = Price(drug_name="Neoral", pharmacy_name="Wegmans", price=31)
CVS197 = Price(drug_name="Lantus", pharmacy_name="CVS", price=88)
Walgreens197 = Price(drug_name="Lantus", pharmacy_name="Walgreens", price=64)
Walmart197 = Price(drug_name="Lantus", pharmacy_name="Walmart", price=31)
Wegmans197 = Price(drug_name="Lantus", pharmacy_name="Wegmans", price=100)
CVS198 = Price(drug_name="Cialis", pharmacy_name="CVS", price=60)
Walgreens198 = Price(drug_name="Cialis", pharmacy_name="Walgreens", price=4)
Walmart198 = Price(drug_name="Cialis", pharmacy_name="Walmart", price=6)
Wegmans198 = Price(drug_name="Cialis", pharmacy_name="Wegmans", price=28)
CVS199 = Price(drug_name="Elavil", pharmacy_name="CVS", price=88)
Walgreens199 = Price(drug_name="Elavil", pharmacy_name="Walgreens", price=13)
Walmart199 = Price(drug_name="Elavil", pharmacy_name="Walmart", price=7)
Wegmans199 = Price(drug_name="Elavil", pharmacy_name="Wegmans", price=52)
CVS200 = Price(drug_name="Vanatrip", pharmacy_name="CVS", price=50)
Walgreens200 = Price(drug_name="Vanatrip",
                     pharmacy_name="Walgreens", price=40)

Walmart200 = Price(drug_name="Vanatrip", pharmacy_name="Walmart", price=44)
Wegmans200 = Price(drug_name="Vanatrip", pharmacy_name="Wegmans", price=67)
CVS201 = Price(drug_name="Lopid", pharmacy_name="CVS", price=39)
Walgreens201 = Price(drug_name="Lopid", pharmacy_name="Walgreens", price=78)
Walmart201 = Price(drug_name="Lopid", pharmacy_name="Walmart", price=2)
Wegmans201 = Price(drug_name="Lopid", pharmacy_name="Wegmans", price=40)
CVS202 = Price(drug_name="Flo-Pred", pharmacy_name="CVS", price=9)
Walgreens202 = Price(drug_name="Flo-Pred",
                     pharmacy_name="Walgreens", price=49)

Walmart202 = Price(drug_name="Flo-Pred", pharmacy_name="Walmart", price=71)
Wegmans202 = Price(drug_name="Flo-Pred", pharmacy_name="Wegmans", price=88)
CVS203 = Price(drug_name="Advil", pharmacy_name="CVS", price=89)
Walgreens203 = Price(drug_name="Advil", pharmacy_name="Walgreens", price=62)
Walmart203 = Price(drug_name="Advil", pharmacy_name="Walmart", price=77)
Wegmans203 = Price(drug_name="Advil", pharmacy_name="Wegmans", price=98)
CVS204 = Price(drug_name="Aceon", pharmacy_name="CVS", price=29)
Walgreens204 = Price(drug_name="Aceon", pharmacy_name="Walgreens", price=41)
Walmart204 = Price(drug_name="Aceon", pharmacy_name="Walmart", price=74)
Wegmans204 = Price(drug_name="Aceon", pharmacy_name="Wegmans", price=85)
CVS205 = Price(drug_name="Desyrel", pharmacy_name="CVS", price=89)
Walgreens205 = Price(drug_name="Desyrel", pharmacy_name="Walgreens", price=7)
Walmart205 = Price(drug_name="Desyrel", pharmacy_name="Walmart", price=17)
Wegmans205 = Price(drug_name="Desyrel", pharmacy_name="Wegmans", price=73)
CVS206 = Price(drug_name="Actos", pharmacy_name="CVS", price=35)
Walgreens206 = Price(drug_name="Actos", pharmacy_name="Walgreens", price=78)
Walmart206 = Price(drug_name="Actos", pharmacy_name="Walmart", price=76)
Wegmans206 = Price(drug_name="Actos", pharmacy_name="Wegmans", price=97)
CVS207 = Price(drug_name="Proscar", pharmacy_name="CVS", price=92)
Walgreens207 = Price(drug_name="Proscar", pharmacy_name="Walgreens", price=71)
Walmart207 = Price(drug_name="Proscar", pharmacy_name="Walmart", price=74)
Wegmans207 = Price(drug_name="Proscar", pharmacy_name="Wegmans", price=33)
CVS208 = Price(drug_name="Inbrija", pharmacy_name="CVS", price=56)
Walgreens208 = Price(drug_name="Inbrija", pharmacy_name="Walgreens", price=24)
Walmart208 = Price(drug_name="Inbrija", pharmacy_name="Walmart", price=55)
Wegmans208 = Price(drug_name="Inbrija", pharmacy_name="Wegmans", price=99)
CVS209 = Price(drug_name="Dopar", pharmacy_name="CVS", price=59)
Walgreens209 = Price(drug_name="Dopar", pharmacy_name="Walgreens", price=91)
Walmart209 = Price(drug_name="Dopar", pharmacy_name="Walmart", price=16)
Wegmans209 = Price(drug_name="Dopar", pharmacy_name="Wegmans", price=64)
CVS210 = Price(drug_name="Larodopa", pharmacy_name="CVS", price=46)
Walgreens210 = Price(drug_name="Larodopa",
                     pharmacy_name="Walgreens", price=17)

Walmart210 = Price(drug_name="Larodopa", pharmacy_name="Walmart", price=32)
Wegmans210 = Price(drug_name="Larodopa", pharmacy_name="Wegmans", price=91)
CVS211 = Price(drug_name="Actonel", pharmacy_name="CVS", price=66)
Walgreens211 = Price(drug_name="Actonel", pharmacy_name="Walgreens", price=25)
Walmart211 = Price(drug_name="Actonel", pharmacy_name="Walmart", price=88)
Wegmans211 = Price(drug_name="Actonel", pharmacy_name="Wegmans", price=1)
CVS212 = Price(drug_name="ProAir", pharmacy_name="CVS", price=24)
Walgreens212 = Price(drug_name="ProAir", pharmacy_name="Walgreens", price=7)
Walmart212 = Price(drug_name="ProAir", pharmacy_name="Walmart", price=55)
Wegmans212 = Price(drug_name="ProAir", pharmacy_name="Wegmans", price=71)
CVS213 = Price(drug_name="Ventolin", pharmacy_name="CVS", price=13)
Walgreens213 = Price(drug_name="Ventolin",
                     pharmacy_name="Walgreens", price=62)

Walmart213 = Price(drug_name="Ventolin", pharmacy_name="Walmart", price=67)
Wegmans213 = Price(drug_name="Ventolin", pharmacy_name="Wegmans", price=51)
CVS214 = Price(drug_name="Proventil", pharmacy_name="CVS", price=95)
Walgreens214 = Price(drug_name="Proventil",
                     pharmacy_name="Walgreens", price=43)
Walmart214 = Price(drug_name="Proventil", pharmacy_name="Walmart", price=75)
Wegmans214 = Price(drug_name="Proventil", pharmacy_name="Wegmans", price=33)
CVS215 = Price(drug_name="Ultram", pharmacy_name="CVS", price=8)
Walgreens215 = Price(drug_name="Ultram", pharmacy_name="Walgreens", price=8)
Walmart215 = Price(drug_name="Ultram", pharmacy_name="Walmart", price=65)
Wegmans215 = Price(drug_name="Ultram", pharmacy_name="Wegmans", price=41)
CVS216 = Price(drug_name="Sonata", pharmacy_name="CVS", price=51)
Walgreens216 = Price(drug_name="Sonata", pharmacy_name="Walgreens", price=20)
Walmart216 = Price(drug_name="Sonata", pharmacy_name="Walmart", price=31)
Wegmans216 = Price(drug_name="Sonata", pharmacy_name="Wegmans", price=64)
CVS217 = Price(drug_name="Zebeta", pharmacy_name="CVS", price=39)
Walgreens217 = Price(drug_name="Zebeta", pharmacy_name="Walgreens", price=84)
Walmart217 = Price(drug_name="Zebeta", pharmacy_name="Walmart", price=28)
Wegmans217 = Price(drug_name="Zebeta", pharmacy_name="Wegmans", price=36)
CVS218 = Price(drug_name="Zovirax", pharmacy_name="CVS", price=29)
Walgreens218 = Price(drug_name="Zovirax", pharmacy_name="Walgreens", price=93)
Walmart218 = Price(drug_name="Zovirax", pharmacy_name="Walmart", price=66)
Wegmans218 = Price(drug_name="Zovirax", pharmacy_name="Wegmans", price=67)
CVS219 = Price(drug_name="Coumadin", pharmacy_name="CVS", price=97)
Walgreens219 = Price(drug_name="Coumadin",
                     pharmacy_name="Walgreens", price=46)

Walmart219 = Price(drug_name="Coumadin", pharmacy_name="Walmart", price=72)
Wegmans219 = Price(drug_name="Coumadin", pharmacy_name="Wegmans", price=73)
CVS220 = Price(drug_name="Luvox", pharmacy_name="CVS", price=51)
Walgreens220 = Price(drug_name="Luvox", pharmacy_name="Walgreens", price=97)
Walmart220 = Price(drug_name="Luvox", pharmacy_name="Walmart", price=22)
Wegmans220 = Price(drug_name="Luvox", pharmacy_name="Wegmans", price=29)
CVS221 = Price(drug_name="Plavix", pharmacy_name="CVS", price=28)
Walgreens221 = Price(drug_name="Plavix", pharmacy_name="Walgreens", price=63)
Walmart221 = Price(drug_name="Plavix", pharmacy_name="Walmart", price=8)
Wegmans221 = Price(drug_name="Plavix", pharmacy_name="Wegmans", price=32)
CVS222 = Price(drug_name="Vibramycin", pharmacy_name="CVS", price=25)
Walgreens222 = Price(drug_name="Vibramycin",
                     pharmacy_name="Walgreens", price=40)
Walmart222 = Price(drug_name="Vibramycin", pharmacy_name="Walmart", price=83)
Wegmans222 = Price(drug_name="Vibramycin", pharmacy_name="Wegmans", price=8)
CVS223 = Price(drug_name="Adoxa", pharmacy_name="CVS", price=69)
Walgreens223 = Price(drug_name="Adoxa", pharmacy_name="Walgreens", price=29)
Walmart223 = Price(drug_name="Adoxa", pharmacy_name="Walmart", price=56)
Wegmans223 = Price(drug_name="Adoxa", pharmacy_name="Wegmans", price=67)
CVS224 = Price(drug_name="Hyzaar", pharmacy_name="CVS", price=19)
Walgreens224 = Price(drug_name="Hyzaar", pharmacy_name="Walgreens", price=68)
Walmart224 = Price(drug_name="Hyzaar", pharmacy_name="Walmart", price=50)
Wegmans224 = Price(drug_name="Hyzaar", pharmacy_name="Wegmans", price=23)
CVS225 = Price(drug_name="Kytril", pharmacy_name="CVS", price=98)
Walgreens225 = Price(drug_name="Kytril", pharmacy_name="Walgreens", price=68)
Walmart225 = Price(drug_name="Kytril", pharmacy_name="Walmart", price=72)
Wegmans225 = Price(drug_name="Kytril", pharmacy_name="Wegmans", price=31)
CVS226 = Price(drug_name="Sancuso", pharmacy_name="CVS", price=100)
Walgreens226 = Price(drug_name="Sancuso", pharmacy_name="Walgreens", price=97)
Walmart226 = Price(drug_name="Sancuso", pharmacy_name="Walmart", price=24)
Wegmans226 = Price(drug_name="Sancuso", pharmacy_name="Wegmans", price=20)
CVS227 = Price(drug_name="Restoril", pharmacy_name="CVS", price=69)
Walgreens227 = Price(drug_name="Restoril",
                     pharmacy_name="Walgreens", price=84)

Walmart227 = Price(drug_name="Restoril", pharmacy_name="Walmart", price=6)
Wegmans227 = Price(drug_name="Restoril", pharmacy_name="Wegmans", price=56)
CVS228 = Price(drug_name="Prevacid", pharmacy_name="CVS", price=25)
Walgreens228 = Price(drug_name="Prevacid",
                     pharmacy_name="Walgreens", price=34)

Walmart228 = Price(drug_name="Prevacid", pharmacy_name="Walmart", price=88)
Wegmans228 = Price(drug_name="Prevacid", pharmacy_name="Wegmans", price=73)
CVS229 = Price(drug_name="Augmentin", pharmacy_name="CVS", price=20)
Walgreens229 = Price(drug_name="Augmentin",
                     pharmacy_name="Walgreens", price=84)
Walmart229 = Price(drug_name="Augmentin", pharmacy_name="Walmart", price=23)
Wegmans229 = Price(drug_name="Augmentin", pharmacy_name="Wegmans", price=41)
CVS230 = Price(drug_name="Mevacor", pharmacy_name="CVS", price=77)
Walgreens230 = Price(drug_name="Mevacor", pharmacy_name="Walgreens", price=8)
Walmart230 = Price(drug_name="Mevacor", pharmacy_name="Walmart", price=82)
Wegmans230 = Price(drug_name="Mevacor", pharmacy_name="Wegmans", price=65)
CVS231 = Price(drug_name="Altoprev", pharmacy_name="CVS", price=47)
Walgreens231 = Price(drug_name="Altoprev",
                     pharmacy_name="Walgreens", price=46)

Walmart231 = Price(drug_name="Altoprev", pharmacy_name="Walmart", price=37)
Wegmans231 = Price(drug_name="Altoprev", pharmacy_name="Wegmans", price=91) """


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
""" db.session.add_all([CVS0,
                    Walgreens0,
                    Walmart0,
                    Wegmans0,
                    CVS1,
                    Walgreens1,
                    Walmart1,
                    Wegmans1,
                    CVS2,
                    Walgreens2,
                    Walmart2,
                    Wegmans2,
                    CVS3,
                    Walgreens3,
                    Walmart3,
                    Wegmans3,
                    CVS4,
                    Walgreens4,
                    Walmart4,
                    Wegmans4,
                    CVS5,
                    Walgreens5,
                    Walmart5,
                    Wegmans5,
                    CVS6,
                    Walgreens6,
                    Walmart6,
                    Wegmans6,
                    CVS7,
                    Walgreens7,
                    Walmart7,
                    Wegmans7,
                    CVS8,
                    Walgreens8,
                    Walmart8,
                    Wegmans8,
                    CVS9,
                    Walgreens9,
                    Walmart9,
                    Wegmans9,
                    CVS10,
                    Walgreens10,
                    Walmart10,
                    Wegmans10,
                    CVS11,
                    Walgreens11,
                    Walmart11,
                    Wegmans11,
                    CVS12,
                    Walgreens12,
                    Walmart12,
                    Wegmans12,
                    CVS13,
                    Walgreens13,
                    Walmart13,
                    Wegmans13,
                    CVS14,
                    Walgreens14,
                    Walmart14,
                    Wegmans14,
                    CVS15,
                    Walgreens15,
                    Walmart15,
                    Wegmans15,
                    CVS16,
                    Walgreens16,
                    Walmart16,
                    Wegmans16,
                    CVS17,
                    Walgreens17,
                    Walmart17,
                    Wegmans17,
                    CVS18,
                    Walgreens18,
                    Walmart18,
                    Wegmans18,
                    CVS19,
                    Walgreens19,
                    Walmart19,
                    Wegmans19,
                    CVS20,
                    Walgreens20,
                    Walmart20,
                    Wegmans20,
                    CVS21,
                    Walgreens21,
                    Walmart21,
                    Wegmans21,
                    CVS22,
                    Walgreens22,
                    Walmart22,
                    Wegmans22,
                    CVS23,
                    Walgreens23,
                    Walmart23,
                    Wegmans23,
                    CVS24,
                    Walgreens24,
                    Walmart24,
                    Wegmans24,
                    CVS25,
                    Walgreens25,
                    Walmart25,
                    Wegmans25,
                    CVS26,
                    Walgreens26,
                    Walmart26,
                    Wegmans26,
                    CVS27,
                    Walgreens27,
                    Walmart27,
                    Wegmans27,
                    CVS28,
                    Walgreens28,
                    Walmart28,
                    Wegmans28,
                    CVS29,
                    Walgreens29,
                    Walmart29,
                    Wegmans29,
                    CVS30,
                    Walgreens30,
                    Walmart30,
                    Wegmans30,
                    CVS31,
                    Walgreens31,
                    Walmart31,
                    Wegmans31,
                    CVS32,
                    Walgreens32,
                    Walmart32,
                    Wegmans32,
                    CVS33,
                    Walgreens33,
                    Walmart33,
                    Wegmans33,
                    CVS34,
                    Walgreens34,
                    Walmart34,
                    Wegmans34,
                    CVS35,
                    Walgreens35,
                    Walmart35,
                    Wegmans35,
                    CVS36,
                    Walgreens36,
                    Walmart36,
                    Wegmans36,
                    CVS37,
                    Walgreens37,
                    Walmart37,
                    Wegmans37,
                    CVS38,
                    Walgreens38,
                    Walmart38,
                    Wegmans38,
                    CVS39,
                    Walgreens39,
                    Walmart39,
                    Wegmans39,
                    CVS40,
                    Walgreens40,
                    Walmart40,
                    Wegmans40,
                    CVS41,
                    Walgreens41,
                    Walmart41,
                    Wegmans41,
                    CVS42,
                    Walgreens42,
                    Walmart42,
                    Wegmans42,
                    CVS43,
                    Walgreens43,
                    Walmart43,
                    Wegmans43,
                    CVS44,
                    Walgreens44,
                    Walmart44,
                    Wegmans44,
                    CVS45,
                    Walgreens45,
                    Walmart45,
                    Wegmans45,
                    CVS46,
                    Walgreens46,
                    Walmart46,
                    Wegmans46,
                    CVS47,
                    Walgreens47,
                    Walmart47,
                    Wegmans47,
                    CVS48,
                    Walgreens48,
                    Walmart48,
                    Wegmans48,
                    CVS49,
                    Walgreens49,
                    Walmart49,
                    Wegmans49,
                    CVS50,
                    Walgreens50,
                    Walmart50,
                    Wegmans50,
                    CVS51,
                    Walgreens51,
                    Walmart51,
                    Wegmans51,
                    CVS52,
                    Walgreens52,
                    Walmart52,
                    Wegmans52,
                    CVS53,
                    Walgreens53,
                    Walmart53,
                    Wegmans53,
                    CVS54,
                    Walgreens54,
                    Walmart54,
                    Wegmans54,
                    CVS55,
                    Walgreens55,
                    Walmart55,
                    Wegmans55,
                    CVS56,
                    Walgreens56,
                    Walmart56,
                    Wegmans56,
                    CVS57,
                    Walgreens57,
                    Walmart57,
                    Wegmans57,
                    CVS58,
                    Walgreens58,
                    Walmart58,
                    Wegmans58,
                    CVS59,
                    Walgreens59,
                    Walmart59,
                    Wegmans59,
                    CVS60,
                    Walgreens60,
                    Walmart60,
                    Wegmans60,
                    CVS61,
                    Walgreens61,
                    Walmart61,
                    Wegmans61,
                    CVS62,
                    Walgreens62,
                    Walmart62,
                    Wegmans62,
                    CVS63,
                    Walgreens63,
                    Walmart63,
                    Wegmans63,
                    CVS64,
                    Walgreens64,
                    Walmart64,
                    Wegmans64,
                    CVS65,
                    Walgreens65,
                    Walmart65,
                    Wegmans65,
                    CVS66,
                    Walgreens66,
                    Walmart66,
                    Wegmans66,
                    CVS67,
                    Walgreens67,
                    Walmart67,
                    Wegmans67,
                    CVS68,
                    Walgreens68,
                    Walmart68,
                    Wegmans68,
                    CVS69,
                    Walgreens69,
                    Walmart69,
                    Wegmans69,
                    CVS70,
                    Walgreens70,
                    Walmart70,
                    Wegmans70,
                    CVS71,
                    Walgreens71,
                    Walmart71,
                    Wegmans71,
                    CVS72,
                    Walgreens72,
                    Walmart72,
                    Wegmans72,
                    CVS73,
                    Walgreens73,
                    Walmart73,
                    Wegmans73,
                    CVS74,
                    Walgreens74,
                    Walmart74,
                    Wegmans74,
                    CVS75,
                    Walgreens75,
                    Walmart75,
                    Wegmans75,
                    CVS76,
                    Walgreens76,
                    Walmart76,
                    Wegmans76,
                    CVS77,
                    Walgreens77,
                    Walmart77,
                    Wegmans77,
                    CVS78,
                    Walgreens78,
                    Walmart78,
                    Wegmans78,
                    CVS79,
                    Walgreens79,
                    Walmart79,
                    Wegmans79,
                    CVS80,
                    Walgreens80,
                    Walmart80,
                    Wegmans80,
                    CVS81,
                    Walgreens81,
                    Walmart81,
                    Wegmans81,
                    CVS82,
                    Walgreens82,
                    Walmart82,
                    Wegmans82,
                    CVS83,
                    Walgreens83,
                    Walmart83,
                    Wegmans83,
                    CVS84,
                    Walgreens84,
                    Walmart84,
                    Wegmans84,
                    CVS85,
                    Walgreens85,
                    Walmart85,
                    Wegmans85,
                    CVS86,
                    Walgreens86,
                    Walmart86,
                    Wegmans86,
                    CVS87,
                    Walgreens87,
                    Walmart87,
                    Wegmans87,
                    CVS88,
                    Walgreens88,
                    Walmart88,
                    Wegmans88,
                    CVS89,
                    Walgreens89,
                    Walmart89,
                    Wegmans89,
                    CVS90,
                    Walgreens90,
                    Walmart90,
                    Wegmans90,
                    CVS91,
                    Walgreens91,
                    Walmart91,
                    Wegmans91,
                    CVS92,
                    Walgreens92,
                    Walmart92,
                    Wegmans92,
                    CVS93,
                    Walgreens93,
                    Walmart93,
                    Wegmans93,
                    CVS94,
                    Walgreens94,
                    Walmart94,
                    Wegmans94,
                    CVS95,
                    Walgreens95,
                    Walmart95,
                    Wegmans95,
                    CVS96,
                    Walgreens96,
                    Walmart96,
                    Wegmans96,
                    CVS97,
                    Walgreens97,
                    Walmart97,
                    Wegmans97,
                    CVS98,
                    Walgreens98,
                    Walmart98,
                    Wegmans98,
                    CVS99,
                    Walgreens99,
                    Walmart99,
                    Wegmans99,
                    CVS100,
                    Walgreens100,
                    Walmart100,
                    Wegmans100,
                    CVS101,
                    Walgreens101,
                    Walmart101,
                    Wegmans101,
                    CVS102,
                    Walgreens102,
                    Walmart102,
                    Wegmans102,
                    CVS103,
                    Walgreens103,
                    Walmart103,
                    Wegmans103,
                    CVS104,
                    Walgreens104,
                    Walmart104,
                    Wegmans104,
                    CVS105,
                    Walgreens105,
                    Walmart105,
                    Wegmans105,
                    CVS106,
                    Walgreens106,
                    Walmart106,
                    Wegmans106,
                    CVS107,
                    Walgreens107,
                    Walmart107,
                    Wegmans107,
                    CVS108,
                    Walgreens108,
                    Walmart108,
                    Wegmans108,
                    CVS109,
                    Walgreens109,
                    Walmart109,
                    Wegmans109,
                    CVS110,
                    Walgreens110,
                    Walmart110,
                    Wegmans110,
                    CVS111,
                    Walgreens111,
                    Walmart111,
                    Wegmans111,
                    CVS112,
                    Walgreens112,
                    Walmart112,
                    Wegmans112,
                    CVS113,
                    Walgreens113,
                    Walmart113,
                    Wegmans113,
                    CVS114,
                    Walgreens114,
                    Walmart114,
                    Wegmans114,
                    CVS115,
                    Walgreens115,
                    Walmart115,
                    Wegmans115,
                    CVS116,
                    Walgreens116,
                    Walmart116,
                    Wegmans116,
                    CVS117,
                    Walgreens117,
                    Walmart117,
                    Wegmans117,
                    CVS118,
                    Walgreens118,
                    Walmart118,
                    Wegmans118,
                    CVS119,
                    Walgreens119,
                    Walmart119,
                    Wegmans119,
                    CVS120,
                    Walgreens120,
                    Walmart120,
                    Wegmans120,
                    CVS121,
                    Walgreens121,
                    Walmart121,
                    Wegmans121,
                    CVS122,
                    Walgreens122,
                    Walmart122,
                    Wegmans122,
                    CVS123,
                    Walgreens123,
                    Walmart123,
                    Wegmans123,
                    CVS124,
                    Walgreens124,
                    Walmart124,
                    Wegmans124,
                    CVS125,
                    Walgreens125,
                    Walmart125,
                    Wegmans125,
                    CVS126,
                    Walgreens126,
                    Walmart126,
                    Wegmans126,
                    CVS127,
                    Walgreens127,
                    Walmart127,
                    Wegmans127,
                    CVS128,
                    Walgreens128,
                    Walmart128,
                    Wegmans128,
                    CVS129,
                    Walgreens129,
                    Walmart129,
                    Wegmans129,
                    CVS130,
                    Walgreens130,
                    Walmart130,
                    Wegmans130,
                    CVS131,
                    Walgreens131,
                    Walmart131,
                    Wegmans131,
                    CVS132,
                    Walgreens132,
                    Walmart132,
                    Wegmans132,
                    CVS133,
                    Walgreens133,
                    Walmart133,
                    Wegmans133,
                    CVS134,
                    Walgreens134,
                    Walmart134,
                    Wegmans134,
                    CVS135,
                    Walgreens135,
                    Walmart135,
                    Wegmans135,
                    CVS136,
                    Walgreens136,
                    Walmart136,
                    Wegmans136,
                    CVS137,
                    Walgreens137,
                    Walmart137,
                    Wegmans137,
                    CVS138,
                    Walgreens138,
                    Walmart138,
                    Wegmans138,
                    CVS139,
                    Walgreens139,
                    Walmart139,
                    Wegmans139,
                    CVS140,
                    Walgreens140,
                    Walmart140,
                    Wegmans140,
                    CVS141,
                    Walgreens141,
                    Walmart141,
                    Wegmans141,
                    CVS142,
                    Walgreens142,
                    Walmart142,
                    Wegmans142,
                    CVS143,
                    Walgreens143,
                    Walmart143,
                    Wegmans143,
                    CVS144,
                    Walgreens144,
                    Walmart144,
                    Wegmans144,
                    CVS145,
                    Walgreens145,
                    Walmart145,
                    Wegmans145,
                    CVS146,
                    Walgreens146,
                    Walmart146,
                    Wegmans146,
                    CVS147,
                    Walgreens147,
                    Walmart147,
                    Wegmans147,
                    CVS148,
                    Walgreens148,
                    Walmart148,
                    Wegmans148,
                    CVS149,
                    Walgreens149,
                    Walmart149,
                    Wegmans149,
                    CVS150,
                    Walgreens150,
                    Walmart150,
                    Wegmans150,
                    CVS151,
                    Walgreens151,
                    Walmart151,
                    Wegmans151,
                    CVS152,
                    Walgreens152,
                    Walmart152,
                    Wegmans152,
                    CVS153,
                    Walgreens153,
                    Walmart153,
                    Wegmans153,
                    CVS154,
                    Walgreens154,
                    Walmart154,
                    Wegmans154,
                    CVS155,
                    Walgreens155,
                    Walmart155,
                    Wegmans155,
                    CVS156,
                    Walgreens156,
                    Walmart156,
                    Wegmans156,
                    CVS157,
                    Walgreens157,
                    Walmart157,
                    Wegmans157,
                    CVS158,
                    Walgreens158,
                    Walmart158,
                    Wegmans158,
                    CVS159,
                    Walgreens159,
                    Walmart159,
                    Wegmans159,
                    CVS160,
                    Walgreens160,
                    Walmart160,
                    Wegmans160,
                    CVS161,
                    Walgreens161,
                    Walmart161,
                    Wegmans161,
                    CVS162,
                    Walgreens162,
                    Walmart162,
                    Wegmans162,
                    CVS163,
                    Walgreens163,
                    Walmart163,
                    Wegmans163,
                    CVS164,
                    Walgreens164,
                    Walmart164,
                    Wegmans164,
                    CVS165,
                    Walgreens165,
                    Walmart165,
                    Wegmans165,
                    CVS166,
                    Walgreens166,
                    Walmart166,
                    Wegmans166,
                    CVS167,
                    Walgreens167,
                    Walmart167,
                    Wegmans167,
                    CVS168,
                    Walgreens168,
                    Walmart168,
                    Wegmans168,
                    CVS169,
                    Walgreens169,
                    Walmart169,
                    Wegmans169,
                    CVS170,
                    Walgreens170,
                    Walmart170,
                    Wegmans170,
                    CVS171,
                    Walgreens171,
                    Walmart171,
                    Wegmans171,
                    CVS172,
                    Walgreens172,
                    Walmart172,
                    Wegmans172,
                    CVS173,
                    Walgreens173,
                    Walmart173,
                    Wegmans173,
                    CVS174,
                    Walgreens174,
                    Walmart174,
                    Wegmans174,
                    CVS175,
                    Walgreens175,
                    Walmart175,
                    Wegmans175,
                    CVS176,
                    Walgreens176,
                    Walmart176,
                    Wegmans176,
                    CVS177,
                    Walgreens177,
                    Walmart177,
                    Wegmans177,
                    CVS178,
                    Walgreens178,
                    Walmart178,
                    Wegmans178,
                    CVS179,
                    Walgreens179,
                    Walmart179,
                    Wegmans179,
                    CVS180,
                    Walgreens180,
                    Walmart180,
                    Wegmans180,
                    CVS181,
                    Walgreens181,
                    Walmart181,
                    Wegmans181,
                    CVS182,
                    Walgreens182,
                    Walmart182,
                    Wegmans182,
                    CVS183,
                    Walgreens183,
                    Walmart183,
                    Wegmans183,
                    CVS184,
                    Walgreens184,
                    Walmart184,
                    Wegmans184,
                    CVS185,
                    Walgreens185,
                    Walmart185,
                    Wegmans185,
                    CVS186,
                    Walgreens186,
                    Walmart186,
                    Wegmans186,
                    CVS187,
                    Walgreens187,
                    Walmart187,
                    Wegmans187,
                    CVS188,
                    Walgreens188,
                    Walmart188,
                    Wegmans188,
                    CVS189,
                    Walgreens189,
                    Walmart189,
                    Wegmans189,
                    CVS190,
                    Walgreens190,
                    Walmart190,
                    Wegmans190,
                    CVS191,
                    Walgreens191,
                    Walmart191,
                    Wegmans191,
                    CVS192,
                    Walgreens192,
                    Walmart192,
                    Wegmans192,
                    CVS193,
                    Walgreens193,
                    Walmart193,
                    Wegmans193,
                    CVS194,
                    Walgreens194,
                    Walmart194,
                    Wegmans194,
                    CVS195,
                    Walgreens195,
                    Walmart195,
                    Wegmans195,
                    CVS196,
                    Walgreens196,
                    Walmart196,
                    Wegmans196,
                    CVS197,
                    Walgreens197,
                    Walmart197,
                    Wegmans197,
                    CVS198,
                    Walgreens198,
                    Walmart198,
                    Wegmans198,
                    CVS199,
                    Walgreens199,
                    Walmart199,
                    Wegmans199,
                    CVS200,
                    Walgreens200,
                    Walmart200,
                    Wegmans200,
                    CVS201,
                    Walgreens201,
                    Walmart201,
                    Wegmans201,
                    CVS202,
                    Walgreens202,
                    Walmart202,
                    Wegmans202,
                    CVS203,
                    Walgreens203,
                    Walmart203,
                    Wegmans203,
                    CVS204,
                    Walgreens204,
                    Walmart204,
                    Wegmans204,
                    CVS205,
                    Walgreens205,
                    Walmart205,
                    Wegmans205,
                    CVS206,
                    Walgreens206,
                    Walmart206,
                    Wegmans206,
                    CVS207,
                    Walgreens207,
                    Walmart207,
                    Wegmans207,
                    CVS208,
                    Walgreens208,
                    Walmart208,
                    Wegmans208,
                    CVS209,
                    Walgreens209,
                    Walmart209,
                    Wegmans209,
                    CVS210,
                    Walgreens210,
                    Walmart210,
                    Wegmans210,
                    CVS211,
                    Walgreens211,
                    Walmart211,
                    Wegmans211,
                    CVS212,
                    Walgreens212,
                    Walmart212,
                    Wegmans212,
                    CVS213,
                    Walgreens213,
                    Walmart213,
                    Wegmans213,
                    CVS214,
                    Walgreens214,
                    Walmart214,
                    Wegmans214,
                    CVS215,
                    Walgreens215,
                    Walmart215,
                    Wegmans215,
                    CVS216,
                    Walgreens216,
                    Walmart216,
                    Wegmans216,
                    CVS217,
                    Walgreens217,
                    Walmart217,
                    Wegmans217,
                    CVS218,
                    Walgreens218,
                    Walmart218,
                    Wegmans218,
                    CVS219,
                    Walgreens219,
                    Walmart219,
                    Wegmans219,
                    CVS220,
                    Walgreens220,
                    Walmart220,
                    Wegmans220,
                    CVS221,
                    Walgreens221,
                    Walmart221,
                    Wegmans221,
                    CVS222,
                    Walgreens222,
                    Walmart222,
                    Wegmans222,
                    CVS223,
                    Walgreens223,
                    Walmart223,
                    Wegmans223,
                    CVS224,
                    Walgreens224,
                    Walmart224,
                    Wegmans224,
                    CVS225,
                    Walgreens225,
                    Walmart225,
                    Wegmans225,
                    CVS226,
                    Walgreens226,
                    Walmart226,
                    Wegmans226,
                    CVS227,
                    Walgreens227,
                    Walmart227,
                    Wegmans227,
                    CVS228,
                    Walgreens228,
                    Walmart228,
                    Wegmans228,
                    CVS229,
                    Walgreens229,
                    Walmart229,
                    Wegmans229,
                    CVS230,
                    Walgreens230,
                    Walmart230,
                    Wegmans230,
                    CVS231,
                    Walgreens231,
                    Walmart231,
                    Wegmans231]) """
db.session.commit()
