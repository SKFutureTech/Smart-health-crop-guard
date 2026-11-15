# -*- coding: utf-8 -*-
# ════════════════════════════════════════════════════════════════════
# 🌿 SMART HEALTH & CROP GUARD - WEB APP v2 (Flask)   by Mr_SK
# ચલાવવા માટે: Pydroid 3 માં આ ફાઈલ Run કરો, પછી Chrome માં
#              http://127.0.0.1:5000 ખોલો.   (pip install flask)
# ════════════════════════════════════════════════════════════════════
# ════════════════════════════════════════════════════════════════════
# SEED DATABASE - 170+ crops
# ════════════════════════════════════════════════════════════════════
SEED_DB = {
    # TREES
    "Neem": {"pic": "tree", "seed_guj": "લીમડાનો બીજ (ગોળી)", "seed_hin": "नीम का बीज",
             "look_guj": "લીલા-પીળા ગોળી જેવું, 1-1.5 સેમી", "look_hin": "हरे-पीले गोली जैसा, 1-1.5 सेमी",
             "rate": "2-3 kg/એકર", "germ": "15-20 દિવસ",
             "method_guj": "બીજા દિવસે પાણીમાં પલાળો, નર્સરીમાં વાવો.",
             "method_hin": "बीज को पानी में भिगोएं, नर्सरी में बोएं।",
             "season_guj": "જૂન-જુલાઈ", "care_guj": "દર 15 દિવસે પાણી",
             "harvest": "3-5 વર્ષ", "special": "🌿 ઔષધીય વૃક્ષ"},
    "Mango": {"pic": "mango", "seed_guj": "આંબાની ગોટલી", "seed_hin": "आम की गुठली",
              "look_guj": "લાંબી ચપટી ગોટલી, 10-15 સેમી", "look_hin": "लंबी चपटी गुठली",
              "rate": "ગ્રાફ્ટિંગ", "germ": "20-30 દિવસ",
              "method_guj": "ગોટલી 2-3 દિવસ પાણીમાં પલાળો.",
              "method_hin": "गुठली 2-3 दिन पानी में भिगोएं।",
              "season_guj": "જૂન-ઓગસ્ટ", "care_guj": "ડ્રિપ ઈરિગેશન",
              "harvest": "3-4 વર્ષ", "special": "🥭 ફળોનો રાજા"},
    "Banana": {"pic": "tree", "seed_guj": "કેળાનું સૂકું", "seed_hin": "केले का सकर",
               "look_guj": "જાડું થડ જેવું, 500g-1kg", "look_hin": "मोटा तना जैसा",
               "rate": "500-800 સકર/એકર", "germ": "15-20 દિવસ",
               "method_guj": "સ્વસ્થ સકર 3x3 ફૂટ ખાડામાં.",
               "method_hin": "स्वस्थ सकर 3x3 फीट गड्ढे में।",
               "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "દર 7 દિવસે પાણી",
               "harvest": "11-12 મહિના", "special": "🍌 આખું વર્ષ"},
    "Lemon": {"pic": "tree", "seed_guj": "લીંબુનો બીજ", "seed_hin": "नींबू का बीज",
              "look_guj": "નાનો સખત બીજ, 5-7mm", "look_hin": "छोटा सख्त बीज",
              "rate": "ગ્રાફ્ટિંગ", "germ": "15-20 દિવસ",
              "method_guj": "બીજ 24 કલાક પલાળો.",
              "method_hin": "बीज 24 घंटे भिगोएं।",
              "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
              "harvest": "3 વર્ષ", "special": "🍋 વિટામિન C"},
    "Papaya": {"pic": "tree", "seed_guj": "પપૈયાનો બીજ", "seed_hin": "पपीता बीज",
               "look_guj": "કાળા-ભૂરા નાનું બીજ", "look_hin": "काले-भूरे छोटा बीज",
               "rate": "200-250g/એકર", "germ": "10-15 દિવસ",
               "method_guj": "તાજા બીજ સીધા ખેતરમાં.",
               "method_hin": "ताजा बीज सीधे खेत में।",
               "season_guj": "જૂન-જુલાઈ", "care_guj": "વધુ પાણી ટાળો",
               "harvest": "9-11 મહિના", "special": "🍈 પાચન"},
    "Guava": {"pic": "tree", "seed_guj": "જામફળનો બીજ", "seed_hin": "अमरूद बीज",
              "look_guj": "નાનું સખત બીજ, 3-5mm", "look_hin": "छोटा सख्त बीज",
              "rate": "ગ્રાફ્ટિંગ", "germ": "20-25 દિવસ",
              "method_guj": "બીજ 2-3 દિવસ પલાળો.",
              "method_hin": "बीज 2-3 दिन भिगोएं।",
              "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
              "harvest": "2-3 વર્ષ", "special": "🍐 વિટામિન C"},
    "Pomegranate": {"pic": "fruit", "seed_guj": "દાડમનો બીજ/કટિંગ", "seed_hin": "अनार बीज",
                    "look_guj": "નાનું લાલ સખત બીજ", "look_hin": "छोटा लाल सख्त बीज",
                    "rate": "કટિંગ", "germ": "20-30 દિવસ",
                    "method_guj": "કટિંગ વધુ સારું.", "method_hin": "कटिंग बेहतर।",
                    "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
                    "harvest": "3 વર્ષ", "special": "🍎 એન્ટીઓક્સિડન્ટ"},
    "Coconut": {"pic": "tree", "seed_guj": "નાળિયેર", "seed_hin": "नारियल",
                "look_guj": "મોટું 1-1.5 kg", "look_hin": "बड़ा 1-1.5 kg",
                "rate": "70-80/એકર", "germ": "60-90 દિવસ",
                "method_guj": "30x30 ફૂટ. અડધું જમીનમાં.",
                "method_hin": "30x30 फीट। आधा जमीन में।",
                "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                "harvest": "5-7 વર્ષ", "special": "🥥 બહુ-ઉપયોગી"},
    "Teak": {"pic": "tree", "seed_guj": "સાગનું બીજ", "seed_hin": "सागौन बीज",
             "look_guj": "નાનું પાંખ જેવું", "look_hin": "छोटा पंख जैसा",
             "rate": "2-3 kg/એકર", "germ": "20-30 દિવસ",
             "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
             "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
             "harvest": "15-20 વર્ષ", "special": "🌳 મોંઘું લાકડું"},
    "Drumstick": {"pic": "tree", "seed_guj": "સરગવાનો બીજ", "seed_hin": "सहजन बीज",
                  "look_guj": "કાળું ગોળ બીજ, 1 સેમી", "look_hin": "काला गोल बीज",
                  "rate": "500g/એકર", "germ": "7-10 દિવસ",
                  "method_guj": "સીધા ખેતરમાં, 8x8 ફૂટ.",
                  "method_hin": "सीधे खेत में, 8x8 फीट।",
                  "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                  "harvest": "6-8 મહિના", "special": "🌿 પોષક"},
    "Sapota": {"pic": "tree", "seed_guj": "ચીકુનો બીજ", "seed_hin": "चीकू बीज",
               "look_guj": "કાળું ચળકતું બીજ", "look_hin": "काला चमकदार बीज",
               "rate": "ગ્રાફ્ટિંગ", "germ": "20-25 દિવસ",
               "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
               "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
               "harvest": "3-4 વર્ષ", "special": "🍯 મીઠું"},
    "Custard Apple": {"pic": "fruit", "seed_guj": "સીતાફળનો બીજ", "seed_hin": "सीताफल बीज",
                      "look_guj": "કાળું લાંબું બીજ", "look_hin": "काला लंबा बीज",
                      "rate": "ગ્રાફ્ટિંગ", "germ": "25-30 દિવસ",
                      "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                      "season_guj": "જૂન-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
                      "harvest": "3-4 વર્ષ", "special": "🍈 શિયાળાનું"},
    "Jamun Tree": {"pic": "tree", "seed_guj": "જાંબુનો બીજ", "seed_hin": "जामुन बीज",
                   "look_guj": "લાંબું લીલું-ભૂરું", "look_hin": "लंबा हरा-भूरा",
                   "rate": "2-3 kg/એકર", "germ": "20-30 દિવસ",
                   "method_guj": "તાજું બીજ સીધા.", "method_hin": "ताजा बीज सीधे।",
                   "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                   "harvest": "5-6 વર્ષ", "special": "🍇 ડાયાબિટીસ"},
    "Jackfruit": {"pic": "fruit", "seed_guj": "ફણસનો બીજ", "seed_hin": "कटहल बीज",
                  "look_guj": "મોટું 2-3 સેમી", "look_hin": "बड़ा 2-3 सेमी",
                  "rate": "ગ્રાફ્ટિંગ", "germ": "20-30 દિવસ",
                  "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                  "season_guj": "જૂન-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
                  "harvest": "3-5 વર્ષ", "special": "🍈 વિશાળ"},
    "Amla Tree": {"pic": "tree", "seed_guj": "આંવળાનો બીજ", "seed_hin": "आंवला बीज",
                  "look_guj": "લાકડા જેવું સખત", "look_hin": "लकड़ी जैसा सख्त",
                  "rate": "ગ્રાફ્ટિંગ", "germ": "30-45 દિવસ",
                  "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
                  "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
                  "harvest": "4-5 વર્ષ", "special": "🍏 વિટામિન C"},
    "Ber Tree": {"pic": "tree", "seed_guj": "બોરની ગોટલી", "seed_hin": "बेर गुठली",
                 "look_guj": "સખત લાકડા જેવી", "look_hin": "सख्त लकड़ी जैसी",
                 "rate": "ગ્રાફ્ટિંગ", "germ": "20-30 દિવસ",
                 "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                 "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
                 "harvest": "3 વર્ષ", "special": "🍇 શિયાળાનું"},
    "Fig Tree": {"pic": "tree", "seed_guj": "અંજીરનો બીજ/કટિંગ", "seed_hin": "अंजीर बीज",
                 "look_guj": "ખૂબ નાનું બીજ", "look_hin": "बहुत छोटा बीज",
                 "rate": "કટિંગ", "germ": "15-20 દિવસ",
                 "method_guj": "કટિંગ સારું.", "method_hin": "कटिंग बेहतर।",
                 "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
                 "harvest": "1-2 વર્ષ", "special": "🍯 મીઠું"},
    "Moringa": {"pic": "tree", "seed_guj": "મોરિંગા બીજ", "seed_hin": "मोरिंगा बीज",
                "look_guj": "કાળું ગોળ બીજ", "look_hin": "काला गोल बीज",
                "rate": "500g/એકર", "germ": "7-10 દિવસ",
                "method_guj": "સીધા ખેતરમાં.", "method_hin": "सीधे खेत में।",
                "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                "harvest": "6-8 મહિના", "special": "🌿 સુપરફૂડ"},
    "Gulmohar Tree": {"pic": "tree", "seed_guj": "ગુલમોહર બીજ", "seed_hin": "गुलमोहर बीज",
                      "look_guj": "લાંબું ચપટું બીજ", "look_hin": "लंबा चपटा बीज",
                      "rate": "2-3 kg/એકર", "germ": "20-30 દિવસ",
                      "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                      "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                      "harvest": "5-7 વર્ષ", "special": "🌺 લાલ ફૂલ"},
    "Kadamba Tree": {"pic": "tree", "seed_guj": "કદંબ બીજ", "seed_hin": "कदंब बीज",
                     "look_guj": "નાનું ગોળ બીજ", "look_hin": "छोटा गोल बीज",
                     "rate": "2-3 kg/એકર", "germ": "15-20 દિવસ",
                     "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                     "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                     "harvest": "3-5 વર્ષ", "special": "🌸 સુગંધી"},
    "Silver Oak": {"pic": "tree", "seed_guj": "સિલ્વર ઓક બીજ", "seed_hin": "सिल्वर ओक बीज",
                   "look_guj": "નાનું પાંખ જેવું", "look_hin": "छोटा पंख जैसा",
                   "rate": "2-3 kg/એકર", "germ": "15-20 દિવસ",
                   "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                   "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                   "harvest": "10-15 વર્ષ", "special": "🌳 શોભાવાળું"},
    "Rain Tree": {"pic": "tree", "seed_guj": "વરસાદી બીજ", "seed_hin": "बरसाती बीज",
                  "look_guj": "નાનું સખત બીજ", "look_hin": "छोटा सख्त बीज",
                  "rate": "2-3 kg/એકર", "germ": "15-20 દિવસ",
                  "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                  "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                  "harvest": "8-10 વર્ષ", "special": "🌳 છાયાદાર"},
    
    # GRAINS
    "Paddy": {"pic": "grain", "seed_guj": "ડાંગરનું બીજ (ધાન)", "seed_hin": "धान का बीज",
              "look_guj": "લાંબું પીળું-સોનેરી, 8-10mm", "look_hin": "लंबा पीला-सुनहरा",
              "rate": "8-10 kg/એકર", "germ": "5-7 દિવસ",
              "method_guj": "નર્સરીમાં વાવો, 25-30 દિવસ પછી રોપો.",
              "method_hin": "नर्सरी में बोएं, 25-30 दिन बाद रोपें।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી ભરેલું ખેતર",
              "harvest": "120-140 દિવસ", "special": "🌾 મુખ્ય અનાજ"},
    "Wheat": {"pic": "wheat", "seed_guj": "ઘઉંનું બીજ", "seed_hin": "गेहूं का बीज",
              "look_guj": "ગોળ-લાંબો સોનેરી, 6-8mm", "look_hin": "गोल-लंबा सुनहरा",
              "rate": "40-50 kg/એકર", "germ": "5-7 દિવસ",
              "method_guj": "સીધું ખેતરમાં, લાઈન થી લાઈન 20 સેમી.",
              "method_hin": "सीधे खेत में, लाइन से लाइन 20 सेमी।",
              "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "4-5 વાર પાણી",
              "harvest": "120-140 દિવસ", "special": "🌾 શિયાળાનો"},
    "Bajra": {"pic": "grain", "seed_guj": "બાજરીનું બીજ", "seed_hin": "बाजरा बीज",
              "look_guj": "નાનો ગોળ દાણો, 3-4mm", "look_hin": "छोटा गोल दाना",
              "rate": "3-4 kg/એકર", "germ": "3-5 દિવસ",
              "method_guj": "સીધું વાવો, 45x15 સેમી.", "method_hin": "सीधे बोएं।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
              "harvest": "75-90 દિવસ", "special": "🌾 સૂકો"},
    "Jowar": {"pic": "grain", "seed_guj": "જુવારનું બીજ", "seed_hin": "ज्वार बीज",
              "look_guj": "ગોળ દાણો, 4-5mm", "look_hin": "गोल दाना, 4-5mm",
              "rate": "4-5 kg/એકર", "germ": "4-6 દિવસ",
              "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
              "harvest": "100-120 દિવસ", "special": "🌾 લોહ તત્વ"},
    "Maize": {"pic": "grain", "seed_guj": "મકાઈનો દાણો", "seed_hin": "मक्का दाना",
              "look_guj": "મોટો પીળો દાણો", "look_hin": "बड़ा पीला दाना",
              "rate": "8-10 kg/એકર", "germ": "4-6 દિવસ",
              "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
              "harvest": "90-110 દિવસ", "special": "🌽"},
    "Ragi": {"pic": "grain", "seed_guj": "રાગીનું બીજ", "seed_hin": "रागी बीज",
             "look_guj": "ખૂબ નાનો લાલ", "look_hin": "बहुत छोटा लाल",
             "rate": "4-5 kg/એકર", "germ": "4-7 દિવસ",
             "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
             "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
             "harvest": "100-120 દિવસ", "special": "🌾 કેલ્શિયમ"},
    "Barley": {"pic": "grain", "seed_guj": "જવનું બીજ", "seed_hin": "जौ बीज",
               "look_guj": "લાંબો સોનેરી", "look_hin": "लंबा सुनहरा",
               "rate": "35-40 kg/એકર", "germ": "5-7 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "3-4 વાર પાણી",
               "harvest": "100-120 દિવસ", "special": "🌾"},
    "Oats": {"pic": "grain", "seed_guj": "ઓટ્સનું બીજ", "seed_hin": "जई बीज",
             "look_guj": "લાંબો પાતળો", "look_hin": "लंबा पतला",
             "rate": "30-40 kg/એકર", "germ": "6-8 દિવસ",
             "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
             "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "3-4 વાર પાણી",
             "harvest": "100-120 દિવસ", "special": "🌾 આરોગ્ય"},
    "Kodo Millet": {"pic": "grain", "seed_guj": "કોદરાનું બીજ", "seed_hin": "कोदो बीज",
                    "look_guj": "નાનો ગોળ દાણો", "look_hin": "छोटा गोल दाना",
                    "rate": "3-4 kg/એકર", "germ": "5-7 દિવસ",
                    "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                    "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                    "harvest": "100-120 દિવસ", "special": "🌾"},
    "Kutki": {"pic": "grain", "seed_guj": "કુટકીનું બીજ", "seed_hin": "कुटकी बीज",
              "look_guj": "ખૂબ નાનો દાણો", "look_hin": "बहुत छोटा दाना",
              "rate": "3-4 kg/એકર", "germ": "5-7 દિવસ",
              "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
              "harvest": "90-100 દિવસ", "special": "🌾"},
    "Barnyard Millet": {"pic": "grain", "seed_guj": "સામાનું બીજ", "seed_hin": "सामा बीज",
                        "look_guj": "નાનો દાણો", "look_hin": "छोटा दाना",
                        "rate": "4-5 kg/એકર", "germ": "4-6 દિવસ",
                        "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                        "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                        "harvest": "60-80 દિવસ", "special": "🌾 ઝડપી"},
    "Little Millet": {"pic": "grain", "seed_guj": "કંગનું બીજ", "seed_hin": "कुटकी बीज",
                      "look_guj": "નાનો દાણો", "look_hin": "छोटा दाना",
                      "rate": "3-4 kg/એકર", "germ": "5-7 દિવસ",
                      "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                      "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                      "harvest": "90-100 દિવસ", "special": "🌾"},
    "Foxtail Millet": {"pic": "grain", "seed_guj": "કાંગનું બીજ", "seed_hin": "कांगनी बीज",
                       "look_guj": "નાનો પીળો", "look_hin": "छोटा पीला",
                       "rate": "4-5 kg/એકર", "germ": "4-6 દિવસ",
                       "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                       "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                       "harvest": "75-90 દિવસ", "special": "🌾"},
    "Amaranth": {"pic": "grain", "seed_guj": "રાજગરાનું બીજ", "seed_hin": "राजगीरा बीज",
                 "look_guj": "ખૂબ નાનો લાલ", "look_hin": "बहुत छोटा लाल",
                 "rate": "1-2 kg/એકર", "germ": "4-6 દિવસ",
                 "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                 "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                 "harvest": "60-90 દિવસ", "special": "🌾 આયર્ન"},
    "Quinoa": {"pic": "grain", "seed_guj": "ક્વિનોઆનું બીજ", "seed_hin": "क्विनोआ बीज",
               "look_guj": "નાનો ગોળ દાણો", "look_hin": "छोटा गोल दाना",
               "rate": "2-3 kg/એકર", "germ": "5-7 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
               "harvest": "90-120 દિવસ", "special": "🌾 સુપરફૂડ"},
    
    # CASH CROPS
    "Cotton": {"pic": "cotton", "seed_guj": "કપાસનું બીજ", "seed_hin": "कपास बीज",
               "look_guj": "કાળું ગોળ રૂંવાળું", "look_hin": "काला गोल रोएंदार",
               "rate": "3-4 kg/એકર", "germ": "7-10 દિવસ",
               "method_guj": "B.T. સીધું વાવો, 3x2 ફૂટ.",
               "method_hin": "B.T. सीधे बोएं, 3x2 फीट।",
               "season_guj": "મે-જૂન", "care_guj": "જીવાત ધ્યાન",
               "harvest": "160-180 દિવસ", "special": "☁️ સફેદ સોનું"},
    "Groundnut": {"pic": "seed", "seed_guj": "મગફળીનો દાણો", "seed_hin": "मूंगफली दाना",
                  "look_guj": "ગુલાબી-લાલ દાણો", "look_hin": "गुलाबी-लाल दाना",
                  "rate": "40-50 kg/એકર", "germ": "5-7 દિવસ",
                  "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                  "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                  "harvest": "100-120 દિવસ", "special": "🥜 તેલ"},
    "Castor": {"pic": "seed", "seed_guj": "એરંડાનું બીજ", "seed_hin": "अरंडी बीज",
               "look_guj": "મોટું લાલ-કથ્થઈ", "look_hin": "बड़ा लाल-भूरा",
               "rate": "4-5 kg/એકર", "germ": "7-10 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
               "harvest": "120-150 દિવસ", "special": "🌰 ઔદ્યોગિક"},
    "Cumin": {"pic": "seed", "seed_guj": "જીરુંનું બીજ", "seed_hin": "जीरा बीज",
              "look_guj": "લાંબો પાતળો ભૂરો", "look_hin": "लंबा पतला भूरा",
              "rate": "10-12 kg/એકર", "germ": "7-10 દિવસ",
              "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
              "season_guj": "નવે-ડિસે", "care_guj": "2-3 વાર પાણી",
              "harvest": "90-110 દિવસ", "special": "🌿 મસાલો"},
    "Sesame": {"pic": "seed", "seed_guj": "તલનું બીજ", "seed_hin": "तिल बीज",
               "look_guj": "ખૂબ નાનો સફેદ-કાળો", "look_hin": "बहुत छोटा दाना",
               "rate": "2-3 kg/એકર", "germ": "4-6 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
               "harvest": "80-100 દિવસ", "special": "🌰 તેલ"},
    "Pigeon Pea": {"pic": "seed", "seed_guj": "તુવેરનો દાણો", "seed_hin": "अरहर दाना",
                   "look_guj": "ગોળ લાલ-કથ્થઈ", "look_hin": "गोल लाल-भूरा",
                   "rate": "6-8 kg/એકર", "germ": "7-10 દિવસ",
                   "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                   "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                   "harvest": "150-180 દિવસ", "special": "🫘 દાળ"},
    "Gram": {"pic": "seed", "seed_guj": "ચણાનો દાણો", "seed_hin": "चना दाना",
             "look_guj": "ગોળ-અંડાકાર ભૂરો", "look_hin": "गोल-अंडाकार भूरा",
             "rate": "30-40 kg/એકર", "germ": "5-7 દિવસ",
             "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
             "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "2-3 વાર પાણી",
             "harvest": "100-120 દિવસ", "special": "🫘 પ્રોટીન"},
    "Moong": {"pic": "seed", "seed_guj": "મગનો દાણો", "seed_hin": "मूंग दाना",
              "look_guj": "નાનો લીલો ગોળ", "look_hin": "छोटा हरा गोल",
              "rate": "8-10 kg/એકર", "germ": "4-6 દિવસ",
              "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
              "season_guj": "માર્ચ-એપ્રિ", "care_guj": "2-3 વાર પાણી",
              "harvest": "60-70 દિવસ", "special": "🫘"},
    "Urad": {"pic": "seed", "seed_guj": "અડદનો દાણો", "seed_hin": "उड़द दाना",
             "look_guj": "નાનો કાળો દાણો", "look_hin": "छोटा काला दाना",
             "rate": "8-10 kg/એકર", "germ": "5-7 દિવસ",
             "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
             "season_guj": "જૂન-જુલાઈ", "care_guj": "2-3 વાર પાણી",
             "harvest": "70-90 દિવસ", "special": "🫘"},
    "Mustard": {"pic": "seed", "seed_guj": "રાઈનું બીજ", "seed_hin": "सरसों बीज",
                "look_guj": "ખૂબ નાનો પીળો", "look_hin": "बहुत छोटा पीला",
                "rate": "2-3 kg/એકર", "germ": "4-6 દિવસ",
                "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "1-2 વાર પાણી",
                "harvest": "100-120 દિવસ", "special": "🌻 તેલ"},
    "Sunflower": {"pic": "flower", "seed_guj": "સૂરજમુખીનું બીજ", "seed_hin": "सूरजमुखी बीज",
                  "look_guj": "લાંબો કાળો-સફેદ", "look_hin": "लंबा काला-सफेद",
                  "rate": "3-4 kg/એકર", "germ": "5-7 દિવસ",
                  "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                  "season_guj": "આખું વર્ષ", "care_guj": "પાણી નિયમિત",
                  "harvest": "90-100 દિવસ", "special": "🌻 તેલ"},
    "Sugarcane": {"pic": "sugarcane", "seed_guj": "શેરડીની કલમ", "seed_hin": "गन्ना कलम",
                  "look_guj": "3 આંખવાળી લીલી", "look_hin": "3 आंख वाली कलम",
                  "rate": "3000-4000 કલમ/એકર", "germ": "15-20 દિવસ",
                  "method_guj": "3 આંખવાળી કલમ.", "method_hin": "3 आंख वाली कलम।",
                  "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી ભરેલું",
                  "harvest": "10-12 મહિના", "special": "🍯 ખાંડ"},
    "Soybean": {"pic": "seed", "seed_guj": "સોયાબીનનો દાણો", "seed_hin": "सोयाबीन दाना",
                "look_guj": "ગોળ પીળો-કાળો", "look_hin": "गोल पीला-काला",
                "rate": "30-40 kg/એકર", "germ": "5-7 દિવસ",
                "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                "season_guj": "જૂન-જુલાઈ", "care_guj": "2-3 વાર પાણી",
                "harvest": "90-100 દિવસ", "special": "🫘"},
    "Tobacco": {"pic": "herb", "seed_guj": "તમાકુનું બીજ", "seed_hin": "तंबाकू बीज",
                "look_guj": "ખૂબ નાનો ભૂરો", "look_hin": "बहुत छोटा भूरा",
                "rate": "50g/એકર", "germ": "7-10 દિવસ",
                "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                "harvest": "120-150 દિવસ", "special": "🍂"},
    "Jute": {"pic": "herb", "seed_guj": "શણનું બીજ", "seed_hin": "जूट बीज",
             "look_guj": "ખૂબ નાનો ભૂરો", "look_hin": "बहुत छोटा भूरा",
             "rate": "3-4 kg/એકર", "germ": "4-6 દિવસ",
             "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
             "season_guj": "માર્ચ-એપ્રિ", "care_guj": "પાણી નિયમિત",
             "harvest": "100-120 દિવસ", "special": "🧵"},
    "Cowpea": {"pic": "seed", "seed_guj": "ચોળાનો દાણો", "seed_hin": "लोबिया दाना",
               "look_guj": "લાલ-સફેદ ગોળ", "look_hin": "लाल-सफेद गोल",
               "rate": "10-12 kg/એકર", "germ": "4-6 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "જૂન-જુલાઈ", "care_guj": "2-3 વાર પાણી",
               "harvest": "60-90 દિવસ", "special": "🫘"},
    "Horse Gram": {"pic": "seed", "seed_guj": "કળથીનો દાણો", "seed_hin": "कुल्थी दाना",
                   "look_guj": "નાનો લાલ-કથ્થઈ", "look_hin": "छोटा लाल-भूरा",
                   "rate": "15-20 kg/એકર", "germ": "5-7 દિવસ",
                   "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                   "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                   "harvest": "100-120 દિવસ", "special": "🫘"},
    "Lentil": {"pic": "seed", "seed_guj": "મસૂરનો દાણો", "seed_hin": "मसूर दाना",
               "look_guj": "નાનો લાલ ચપટો", "look_hin": "छोटा लाल चपटा",
               "rate": "15-20 kg/એકર", "germ": "5-7 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "2-3 વાર પાણી",
               "harvest": "100-110 દિવસ", "special": "🫘"},
    "Rajma": {"pic": "seed", "seed_guj": "રાજમાનો દાણો", "seed_hin": "राजमा दाना",
              "look_guj": "લાલ લાંબો ગોળ", "look_hin": "लाल लंबा गोल",
              "rate": "20-25 kg/એકર", "germ": "5-7 દિવસ",
              "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
              "harvest": "90-110 દિવસ", "special": "🫘"},
    "Chickpea": {"pic": "seed", "seed_guj": "કાબુલી ચણાનો દાણો", "seed_hin": "काबुली चना",
                 "look_guj": "મોટો ગોળ સફેદ-ભૂરો", "look_hin": "बड़ा गोल सफेद-भूरा",
                 "rate": "30-40 kg/એકર", "germ": "5-7 દિવસ",
                 "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                 "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "2-3 વાર પાણી",
                 "harvest": "100-120 દિવસ", "special": "🫘"},
    
    # VEGETABLES
    "Tomato": {"pic": "veg", "seed_guj": "ટમેટાનું બીજ", "seed_hin": "टमाटर बीज",
               "look_guj": "ખૂબ નાનો સફેદ-પીળો", "look_hin": "छोटा सफेद-पीला",
               "rate": "100-150g/એકર", "germ": "7-10 દિવસ",
               "method_guj": "નર્સરીમાં વાવો.", "method_hin": "नर्सरी में बोएं।",
               "season_guj": "સપ્ટે-ઓક્ટો", "care_guj": "પાણી નિયમિત",
               "harvest": "90-120 દિવસ", "special": "🍅"},
    "Potato": {"pic": "seed", "seed_guj": "બટાટાનું કંદ", "seed_hin": "आलू कंद",
               "look_guj": "નાનું બટાટું 30-50g", "look_hin": "छोटा आलू 30-50g",
               "rate": "800-1000 kg/એકર", "germ": "10-15 દિવસ",
               "method_guj": "કંદ કાપો.", "method_hin": "कंद काटें।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
               "harvest": "90-110 દિવસ", "special": "🥔"},
    "Chili": {"pic": "veg", "seed_guj": "મરચીનું બીજ", "seed_hin": "मिर्च बीज",
              "look_guj": "નાનો પીળો ચપટો", "look_hin": "छोटा पीला चपटा",
              "rate": "100-150g/એકર", "germ": "8-12 દિવસ",
              "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
              "harvest": "120-150 દિવસ", "special": "🌶️"},
    "Brinjal": {"pic": "veg", "seed_guj": "રીંગણાનું બીજ", "seed_hin": "बैंगन बीज",
                "look_guj": "નાનો પીળો ચપટો", "look_hin": "छोटा पीला दाना",
                "rate": "100-150g/એકર", "germ": "8-12 દિવસ",
                "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                "season_guj": "આખું વર્ષ", "care_guj": "પાણી નિયમિત",
                "harvest": "100-120 દિવસ", "special": "🍆"},
    "Onion": {"pic": "seed", "seed_guj": "ડુંગળીનું બીજ", "seed_hin": "प्याज बीज",
              "look_guj": "ખૂબ નાનો કાળો", "look_hin": "बहुत छोटा काला",
              "rate": "3-4 kg/એકર", "germ": "7-10 દિવસ",
              "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
              "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
              "harvest": "120-150 દિવસ", "special": "🧅"},
    "Cabbage": {"pic": "veg", "seed_guj": "કોબીનું બીજ", "seed_hin": "पत्ता गोभी बीज",
                "look_guj": "નાનો ગોળ કથ્થઈ", "look_hin": "छोटा गोल भूरा",
                "rate": "150-200g/એકર", "germ": "7-10 દિવસ",
                "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                "season_guj": "સપ્ટે-ઓક્ટો", "care_guj": "પાણી નિયમિત",
                "harvest": "90-110 દિવસ", "special": "🥬"},
    "Cauliflower": {"pic": "veg", "seed_guj": "ફૂલકોબીનું બીજ", "seed_hin": "फूलगोभी बीज",
                    "look_guj": "નાનો ગોળ કથ્થઈ", "look_hin": "छोटा गोल भूरा",
                    "rate": "150-200g/એકર", "germ": "7-10 દિવસ",
                    "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                    "season_guj": "સપ્ટે-ઓક્ટો", "care_guj": "પાણી નિયમિત",
                    "harvest": "90-110 દિવસ", "special": "🥬"},
    "Bottle Gourd": {"pic": "veg", "seed_guj": "દૂધીનું બીજ", "seed_hin": "लौकी बीज",
                     "look_guj": "લાંબો સફેદ ચપટો", "look_hin": "लंबा सफेद",
                     "rate": "2-3 kg/એકર", "germ": "7-10 દિવસ",
                     "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                     "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                     "harvest": "60-90 દિવસ", "special": "🥒"},
    "Bitter Gourd": {"pic": "veg", "seed_guj": "કારેલાનું બીજ", "seed_hin": "करेला बीज",
                     "look_guj": "લાંબો ભૂરો ચપટો", "look_hin": "लंबा भूरा",
                     "rate": "4-5 kg/એકર", "germ": "7-10 દિવસ",
                     "method_guj": "બીજ 24 કલાક પલાળો.", "method_hin": "बीज 24 घंटे भिगोएं।",
                     "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                     "harvest": "60-80 દિવસ", "special": "🥒"},
    "Ladyfinger": {"pic": "veg", "seed_guj": "ભીંડાનું બીજ", "seed_hin": "भिंडी बीज",
                   "look_guj": "નાનો લીલો-કથ્થઈ", "look_hin": "छोटा हरा-भूरा",
                   "rate": "8-10 kg/એકર", "germ": "5-7 દિવસ",
                   "method_guj": "બીજ 12 કલાક પલાળો.", "method_hin": "बीज 12 घंटे भिगोएं।",
                   "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                   "harvest": "50-60 દિવસ", "special": "🌿"},
    "Cucumber": {"pic": "veg", "seed_guj": "કાકડીનું બીજ", "seed_hin": "खीरा बीज",
                 "look_guj": "લાંબો સફેદ ચપટો", "look_hin": "लंबा सफेद",
                 "rate": "1-2 kg/એકર", "germ": "5-7 દિવસ",
                 "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                 "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                 "harvest": "50-70 દિવસ", "special": "🥒"},
    "Pumpkin": {"pic": "veg", "seed_guj": "કોળાનું બીજ", "seed_hin": "कद्दू बीज",
                "look_guj": "લાંબો સફેદ ચપટો", "look_hin": "लंबा सफेद",
                "rate": "2-3 kg/એકર", "germ": "7-10 દિવસ",
                "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                "harvest": "90-120 દિવસ", "special": "🎃"},
    "Carrot": {"pic": "veg", "seed_guj": "ગાજરનું બીજ", "seed_hin": "गाजर बीज",
               "look_guj": "ખૂબ નાનો પાતળો", "look_hin": "छोटा पतला",
               "rate": "3-4 kg/એકર", "germ": "10-15 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
               "harvest": "70-90 દિવસ", "special": "🥕"},
    "Radish": {"pic": "veg", "seed_guj": "મૂળાનું બીજ", "seed_hin": "मूली बीज",
               "look_guj": "નાનો ગોળ કથ્થઈ", "look_hin": "छोटा गोल भूरा",
               "rate": "3-4 kg/એકર", "germ": "5-7 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
               "harvest": "30-45 દિવસ", "special": "🌶️"},
    "Spinach": {"pic": "herb", "seed_guj": "પાલકનું બીજ", "seed_hin": "पालक बीज",
                "look_guj": "નાનો ગોળ કથ્થઈ", "look_hin": "छोटा गोल भूरा",
                "rate": "4-5 kg/એકર", "germ": "5-7 દિવસ",
                "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                "harvest": "30-45 દિવસ", "special": "🥬"},
    "Fenugreek": {"pic": "herb", "seed_guj": "મેથીનું બીજ", "seed_hin": "मेथी बीज",
                  "look_guj": "લાંબો લાલ ચપટો", "look_hin": "लंबा लाल",
                  "rate": "8-10 kg/એકર", "germ": "5-7 દિવસ",
                  "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                  "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                  "harvest": "25-35 દિવસ", "special": "🌿"},
    "Coriander": {"pic": "herb", "seed_guj": "કોથમીરનું બીજ", "seed_hin": "धनिया बीज",
                  "look_guj": "ગોળ ભૂરો દાણો", "look_hin": "गोल भूरा दाना",
                  "rate": "8-10 kg/એકર", "germ": "7-10 દિવસ",
                  "method_guj": "બીજ ફોડીને વાવો.", "method_hin": "बीज फोड़कर बोएं।",
                  "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                  "harvest": "30-45 દિવસ", "special": "🌿"},
    "Pea": {"pic": "seed", "seed_guj": "વટાણાનું બીજ", "seed_hin": "मटर बीज",
            "look_guj": "ગોળ લીલો-પીળો", "look_hin": "गोल हरा-पीला",
            "rate": "25-30 kg/એકર", "germ": "7-10 દિવસ",
            "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
            "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "2-3 વાર પાણી",
            "harvest": "60-80 દિવસ", "special": "🫛"},
    "Beans": {"pic": "veg", "seed_guj": "ફણસીનું બીજ", "seed_hin": "बीन्स बीज",
              "look_guj": "લાંબો લાલ-સફેદ", "look_hin": "लंबा लाल-सफेद",
              "rate": "20-25 kg/એકર", "germ": "5-7 દિવસ",
              "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
              "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
              "harvest": "50-70 દિવસ", "special": "🌿"},
    "Cluster Beans": {"pic": "veg", "seed_guj": "ગુવારનું બીજ", "seed_hin": "ग्वार बीज",
                      "look_guj": "નાનો ગોળ કથ્થઈ", "look_hin": "छोटा गोल भूरा",
                      "rate": "15-20 kg/એકર", "germ": "5-7 દિવસ",
                      "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                      "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                      "harvest": "60-80 દિવસ", "special": "🌿"},
    "Ridge Gourd": {"pic": "veg", "seed_guj": "તૂરિયાનું બીજ", "seed_hin": "तुरई बीज",
                    "look_guj": "લાંબો સફેદ ચપટો", "look_hin": "लंबा सफेद",
                    "rate": "2-3 kg/એકર", "germ": "7-10 દિવસ",
                    "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                    "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                    "harvest": "60-80 દિવસ", "special": "🥒"},
    "Sponge Gourd": {"pic": "veg", "seed_guj": "ગલકાનું બીજ", "seed_hin": "गिलकी बीज",
                     "look_guj": "લાંબો કાળો ચપટો", "look_hin": "लंबा काला",
                     "rate": "2-3 kg/એકર", "germ": "7-10 દિવસ",
                     "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                     "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                     "harvest": "60-80 દિવસ", "special": "🥒"},
    "Pointed Gourd": {"pic": "veg", "seed_guj": "પરવળનું બીજ", "seed_hin": "परवल बीज",
                      "look_guj": "નાનો ગોળ લાલ", "look_hin": "छोटा गोल लाल",
                      "rate": "કટિંગ", "germ": "10-15 દિવસ",
                      "method_guj": "કટિંગ 15 સેમી.", "method_hin": "कटिंग 15 सेमी।",
                      "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                      "harvest": "60-80 દિવસ", "special": "🥒"},
    "Beetroot": {"pic": "veg", "seed_guj": "બીટનું બીજ", "seed_hin": "चुकंदर बीज",
                 "look_guj": "નાનો ગોળ કથ્થઈ", "look_hin": "छोटा गोल भूरा",
                 "rate": "4-5 kg/એકર", "germ": "10-15 દિવસ",
                 "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                 "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                 "harvest": "60-80 દિવસ", "special": "🍠"},
    "Bell Pepper": {"pic": "veg", "seed_guj": "શિમલા મરચીનું બીજ", "seed_hin": "शिमला मिर्च बीज",
                    "look_guj": "નાનો પીળો ચપટો", "look_hin": "छोटा पीला",
                    "rate": "150-200g/એકર", "germ": "8-12 દિવસ",
                    "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                    "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                    "harvest": "90-110 દિવસ", "special": "🫑"},
    "Sweet Corn": {"pic": "grain", "seed_guj": "ગળી મકાઈનો દાણો", "seed_hin": "स्वीट कॉर्न दाना",
                   "look_guj": "ગોળ પીળો સોનેરી", "look_hin": "गोल पीला",
                   "rate": "6-8 kg/એકર", "germ": "4-6 દિવસ",
                   "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                   "season_guj": "આખું વર્ષ", "care_guj": "પાણી નિયમિત",
                   "harvest": "70-90 દિવસ", "special": "🌽"},
    "Turnip": {"pic": "veg", "seed_guj": "શલગમનું બીજ", "seed_hin": "शलजम बीज",
               "look_guj": "નાનો ગોળ કથ્થઈ", "look_hin": "छोटा गोल भूरा",
               "rate": "2-3 kg/એકર", "germ": "5-7 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
               "harvest": "40-60 દિવસ", "special": "🥬"},
    "Sweet Potato": {"pic": "seed", "seed_guj": "શક્કરિયાની કલમ", "seed_hin": "शकरकंद कलम",
                     "look_guj": "કલમ 20-30 સેમી", "look_hin": "कलम 20-30 सेमी",
                     "rate": "કલમ", "germ": "7-10 દિવસ",
                     "method_guj": "કલમ 30 સેમી.", "method_hin": "कलम 30 सेमी।",
                     "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                     "harvest": "90-120 દિવસ", "special": "🍠"},
    "Colocasia": {"pic": "veg", "seed_guj": "અળવીનું કંદ", "seed_hin": "अरबी कंद",
                  "look_guj": "નાનું કંદ 30-50g", "look_hin": "छोटा कंद 30-50g",
                  "rate": "કંદ", "germ": "10-15 દિવસ",
                  "method_guj": "કંદ 30x15 સેમી.", "method_hin": "कंद 30x15 सेमी।",
                  "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                  "harvest": "120-150 દિવસ", "special": "🍠"},
    "Yam": {"pic": "seed", "seed_guj": "રતાળુનું કંદ", "seed_hin": "रतालू कंद",
            "look_guj": "નાનું કંદ 100-200g", "look_hin": "छोटा कंद 100-200g",
            "rate": "કંદ", "germ": "10-15 દિવસ",
            "method_guj": "કંદ 2x1 ફૂટ.", "method_hin": "कंद 2x1 फीट।",
            "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
            "harvest": "150-180 દિવસ", "special": "🍠"},
    "Broccoli": {"pic": "veg", "seed_guj": "બ્રોકોલીનું બીજ", "seed_hin": "ब्रोकली बीज",
                 "look_guj": "નાનો ગોળ કથ્થઈ", "look_hin": "छोटा गोल भूरा",
                 "rate": "150-200g/એકર", "germ": "7-10 દિવસ",
                 "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                 "season_guj": "સપ્ટે-ઓક્ટો", "care_guj": "પાણી નિયમિત",
                 "harvest": "80-100 દિવસ", "special": "🥦"},
    "Lettuce": {"pic": "veg", "seed_guj": "લેટ્યુસનું બીજ", "seed_hin": "लेट्यूस बीज",
                "look_guj": "ખૂબ નાનો સફેદ", "look_hin": "बहुत छोटा सफेद",
                "rate": "100-150g/એકર", "germ": "7-10 દિવસ",
                "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                "harvest": "45-60 દિવસ", "special": "🥬"},
    "Celery": {"pic": "herb", "seed_guj": "સેલરીનું બીજ", "seed_hin": "सेलरी बीज",
               "look_guj": "ખૂબ નાનો ભૂરો", "look_hin": "बहुत छोटा भूरा",
               "rate": "100-150g/એકર", "germ": "15-20 દિવસ",
               "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
               "harvest": "90-120 દિવસ", "special": "🌿"},
    "Asparagus": {"pic": "herb", "seed_guj": "શતાવરીનું બીજ", "seed_hin": "शतावरी बीज",
                  "look_guj": "નાનો કાળો ગોળ", "look_hin": "छोटा काला गोल",
                  "rate": "1-2 kg/એકર", "germ": "15-20 દિવસ",
                  "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                  "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                  "harvest": "2 વર્ષ", "special": "🌿"},
    "Zucchini": {"pic": "veg", "seed_guj": "ઝુકીનીનું બીજ", "seed_hin": "ज़ुकीनी बीज",
                 "look_guj": "લાંબો સફેદ", "look_hin": "लंबा सफेद",
                 "rate": "1-2 kg/એકર", "germ": "5-7 દિવસ",
                 "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                 "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                 "harvest": "50-60 દિવસ", "special": "🥒"},
    
    # FRUITS
    "Grape": {"pic": "fruit", "seed_guj": "દ્રાક્ષની કટિંગ", "seed_hin": "अंगूर कटिंग",
              "look_guj": "20-30 સેમી લીલી", "look_hin": "20-30 सेमी डाली",
              "rate": "કટિંગ", "germ": "15-20 દિવસ",
              "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
              "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
              "harvest": "2 વર્ષ", "special": "🍇"},
    "Watermelon": {"pic": "fruit", "seed_guj": "તરબૂચનું બીજ", "seed_hin": "तरबूज बीज",
                   "look_guj": "લાંબો કાળો ચપટો", "look_hin": "लंबा काला",
                   "rate": "2-3 kg/એકર", "germ": "7-10 દિવસ",
                   "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                   "season_guj": "જાન્યુ-ફેબ્રુ", "care_guj": "પાણી નિયમિત",
                   "harvest": "80-100 દિવસ", "special": "🍉"},
    "Muskmelon": {"pic": "fruit", "seed_guj": "શક્કરટેટીનું બીજ", "seed_hin": "खरबूजा बीज",
                  "look_guj": "લાંબો પીળો", "look_hin": "लंबा पीला",
                  "rate": "2-3 kg/એકર", "germ": "7-10 દિવસ",
                  "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                  "season_guj": "જાન્યુ-ફેબ્રુ", "care_guj": "પાણી નિયમિત",
                  "harvest": "70-90 દિવસ", "special": "🍈"},
    "Strawberry": {"pic": "fruit", "seed_guj": "સ્ટ્રોબેરી રનર", "seed_hin": "स्ट्रॉबेरी रनर",
                   "look_guj": "10-15 સેમી લીલી", "look_hin": "10-15 सेमी रनर",
                   "rate": "રનર", "germ": "15-20 દિવસ",
                   "method_guj": "રનર વાવો.", "method_hin": "रनर बोएं।",
                   "season_guj": "સપ્ટે-ઓક્ટો", "care_guj": "પાણી નિયમિત",
                   "harvest": "90-120 દિવસ", "special": "🍓"},
    "Pineapple": {"pic": "fruit", "seed_guj": "અનાનસ કૂંપળ", "seed_hin": "अनानस कोंपल",
                  "look_guj": "ઉપરની લીલી પાનવાળી", "look_hin": "ऊपर की हरी पत्ती",
                  "rate": "કૂંપળ", "germ": "20-30 દિવસ",
                  "method_guj": "કૂંપળ વાવો.", "method_hin": "कोंपल बोएं।",
                  "season_guj": "આખું વર્ષ", "care_guj": "પાણી નિયમિત",
                  "harvest": "15-18 મહિના", "special": "🍍"},
    "Fig": {"pic": "fruit", "seed_guj": "અંજીરની કટિંગ", "seed_hin": "अंजीर कटिंग",
            "look_guj": "15-20 સેમી લીલી", "look_hin": "15-20 सेमी डाली",
            "rate": "કટિંગ", "germ": "15-20 દિવસ",
            "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
            "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
            "harvest": "1-2 વર્ષ", "special": "🍯"},
    "Jamun": {"pic": "fruit", "seed_guj": "જાંબુનો બીજ", "seed_hin": "जामुन बीज",
              "look_guj": "લાંબું લીલું-ભૂરું", "look_hin": "लंबा हरा-भूरा",
              "rate": "2-3 kg/એકર", "germ": "20-30 દિવસ",
              "method_guj": "તાજું બીજ સીધા.", "method_hin": "ताजा बीज सीधे।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
              "harvest": "5-6 વર્ષ", "special": "🍇"},
    "Jackfruit": {"pic": "fruit", "seed_guj": "ફણસનો બીજ", "seed_hin": "कटहल बीज",
                  "look_guj": "મોટું 2-3 સેમી", "look_hin": "बड़ा 2-3 सेमी",
                  "rate": "ગ્રાફ્ટિંગ", "germ": "20-30 દિવસ",
                  "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                  "season_guj": "જૂન-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
                  "harvest": "3-5 વર્ષ", "special": "🍈"},
    "Ber": {"pic": "fruit", "seed_guj": "બોરની ગોટલી", "seed_hin": "बेर गुठली",
            "look_guj": "સખત લાકડા જેવી", "look_hin": "सख्त लकड़ी जैसी",
            "rate": "ગ્રાફ્ટિંગ", "germ": "20-30 દિવસ",
            "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
            "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
            "harvest": "3 વર્ષ", "special": "🍇"},
    "Amla": {"pic": "fruit", "seed_guj": "આંવળાનો બીજ", "seed_hin": "आंवला बीज",
             "look_guj": "લાકડા જેવું સખત", "look_hin": "लकड़ी जैसा सख्त",
             "rate": "ગ્રાફ્ટિંગ", "germ": "30-45 દિવસ",
             "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
             "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
             "harvest": "4-5 વર્ષ", "special": "🍏"},
    "Custard Fruit": {"pic": "fruit", "seed_guj": "સીતાફળનો બીજ", "seed_hin": "सीताफल बीज",
                      "look_guj": "કાળું લાંબું બીજ", "look_hin": "काला लंबा बीज",
                      "rate": "ગ્રાફ્ટિંગ", "germ": "25-30 દિવસ",
                      "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                      "season_guj": "જૂન-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
                      "harvest": "3-4 વર્ષ", "special": "🍈"},
    "Orange": {"pic": "fruit", "seed_guj": "સંતરાનો બીજ", "seed_hin": "संतरा बीज",
               "look_guj": "નાનો સફેદ ચપટો", "look_hin": "छोटा सफेद",
               "rate": "ગ્રાફ્ટિંગ", "germ": "20-25 દિવસ",
               "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
               "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
               "harvest": "3 વર્ષ", "special": "🍊"},
    "Sweet Lime": {"pic": "fruit", "seed_guj": "મોસંબીનો બીજ", "seed_hin": "मौसंबी बीज",
                   "look_guj": "નાનો સફેદ ચપટો", "look_hin": "छोटा सफेद",
                   "rate": "ગ્રાફ્ટિંગ", "germ": "20-25 દિવસ",
                   "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
                   "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
                   "harvest": "3 વર્ષ", "special": "🍋"},
    "Pear": {"pic": "fruit", "seed_guj": "નાસપતીનો બીજ", "seed_hin": "नाशपाती बीज",
             "look_guj": "નાનો કાળો ચપટો", "look_hin": "छोटा काला",
             "rate": "ગ્રાફ્ટિંગ", "germ": "20-30 દિવસ",
             "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
             "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
             "harvest": "3-4 વર્ષ", "special": "🍐"},
    "Peach": {"pic": "fruit", "seed_guj": "આલૂની ગોટલી", "seed_hin": "आड़ू गुठली",
              "look_guj": "લાકડા જેવી સખત", "look_hin": "लकड़ी जैसी सख्त",
              "rate": "ગ્રાફ્ટિંગ", "germ": "25-30 દિવસ",
              "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
              "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
              "harvest": "3-4 વર્ષ", "special": "🍑"},
    "Plum": {"pic": "fruit", "seed_guj": "આલુબુખારાની ગોટલી", "seed_hin": "आलूबुखारा गुठली",
             "look_guj": "લાકડા જેવી સખત", "look_hin": "लकड़ी जैसी सख्त",
             "rate": "ગ્રાફ્ટિંગ", "germ": "25-30 દિવસ",
             "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
             "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
             "harvest": "3-4 વર્ષ", "special": "🍑"},
    "Cherry": {"pic": "fruit", "seed_guj": "ચેરીની ગોટલી", "seed_hin": "चेरी गुठली",
               "look_guj": "નાની ગોળ ગોટલી", "look_hin": "छोटी गोल गुठली",
               "rate": "ગ્રાફ્ટિંગ", "germ": "30-40 દિવસ",
               "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
               "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઠંડું",
               "harvest": "4-5 વર્ષ", "special": "🍒"},
    "Kiwi": {"pic": "fruit", "seed_guj": "કીવીની કટિંગ", "seed_hin": "कीवी कटिंग",
             "look_guj": "15-20 સેમી લીલી", "look_hin": "15-20 सेमी डाली",
             "rate": "કટિંગ", "germ": "20-25 દિવસ",
             "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
             "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
             "harvest": "3-4 વર્ષ", "special": "🥝"},
    "Dragon Fruit": {"pic": "fruit", "seed_guj": "ડ્રેગન ફ્રુટ કટિંગ", "seed_hin": "ड्रैगन फ्रूट कटिंग",
                     "look_guj": "20-30 સેમી લીલી", "look_hin": "20-30 सेमी डाली",
                     "rate": "કટિંગ", "germ": "15-20 દિવસ",
                     "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                     "season_guj": "આખું વર્ષ", "care_guj": "ઓછું પાણી",
                     "harvest": "1-2 વર્ષ", "special": "🐉"},
    "Avocado": {"pic": "fruit", "seed_guj": "એવોકાડોનો બીજ", "seed_hin": "एवोकाडो बीज",
                "look_guj": "મોટો ગોળ બીજ 5-7 સેમી", "look_hin": "बड़ा गोल बीज",
                "rate": "ગ્રાફ્ટિંગ", "germ": "30-40 દિવસ",
                "method_guj": "ગ્રાફ્ટિંગ સારું.", "method_hin": "ग्राफ्टिंग बेहतर।",
                "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
                "harvest": "3-4 વર્ષ", "special": "🥑"},
    
    # FLOWERS
    "Rose": {"pic": "flower", "seed_guj": "ગુલાબની કટિંગ", "seed_hin": "गुलाब कटिंग",
             "look_guj": "15-20 સેમી લીલી ડાળી", "look_hin": "15-20 सेमी डाली",
             "rate": "કટિંગ", "germ": "15-20 દિવસ",
             "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
             "season_guj": "ઓક્ટો-ફેબ્રુ", "care_guj": "પાણી નિયમિત",
             "harvest": "3-4 મહિના", "special": "🌹"},
    "Marigold": {"pic": "flower", "seed_guj": "ગલગોટાનું બીજ", "seed_hin": "गेंदा बीज",
                 "look_guj": "લાંબો પાતળો કાળો", "look_hin": "लंबा काला दाना",
                 "rate": "400-500g/એકર", "germ": "4-7 દિવસ",
                 "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                 "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                 "harvest": "60-90 દિવસ", "special": "🌼"},
    "Jasmine": {"pic": "flower", "seed_guj": "મોગરાની કટિંગ", "seed_hin": "मोगरा कटिंग",
                "look_guj": "15-20 સેમી લીલી", "look_hin": "15-20 सेमी डाली",
                "rate": "કટિંગ", "germ": "20-25 દિવસ",
                "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                "harvest": "6-8 મહિના", "special": "🌸"},
    "Lotus": {"pic": "flower", "seed_guj": "કમળનું કંદ", "seed_hin": "कमल कंद",
              "look_guj": "કંદ 15-20 સેમી", "look_hin": "कंद 15-20 सेमी",
              "rate": "કંદ", "germ": "15-20 દિવસ",
              "method_guj": "કંદ પાણીમાં.", "method_hin": "कंद पानी में।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી ભરેલું",
              "harvest": "12-18 મહિના", "special": "🪷"},
    "Orchid": {"pic": "flower", "seed_guj": "ઓર્કિડની કટિંગ", "seed_hin": "ऑर्किड कटिंग",
               "look_guj": "10-15 સેમી લીલી", "look_hin": "10-15 सेमी डाली",
               "rate": "કટિંગ", "germ": "30-45 દિવસ",
               "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
               "season_guj": "આખું વર્ષ", "care_guj": "ભેજ",
               "harvest": "1-2 વર્ષ", "special": "🌺"},
    "Hibiscus": {"pic": "flower", "seed_guj": "જાસૂદની કટિંગ", "seed_hin": "हिबिस्कस कटिंग",
                 "look_guj": "15-20 સેમી લીલી", "look_hin": "15-20 सेमी डाली",
                 "rate": "કટિંગ", "germ": "20-25 દિવસ",
                 "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                 "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
                 "harvest": "6-8 મહિના", "special": "🌺"},
    "Lily": {"pic": "flower", "seed_guj": "લિલીનું બલ્બ", "seed_hin": "लिली बल्ब",
             "look_guj": "5-8 સેમી ગોળ કંદ", "look_hin": "5-8 सेमी कंद",
             "rate": "બલ્બ", "germ": "15-25 દિવસ",
             "method_guj": "બલ્બ વાવો.", "method_hin": "बल्ब बोएं।",
             "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
             "harvest": "90-120 દિવસ", "special": "🌷"},
    "Dahlia": {"pic": "flower", "seed_guj": "ડેહલિયાનું કંદ", "seed_hin": "डहेलिया कंद",
               "look_guj": "5-8 સેમી લાંબું", "look_hin": "5-8 सेमी कंद",
               "rate": "કંદ", "germ": "15-20 દિવસ",
               "method_guj": "કંદ વાવો.", "method_hin": "कंद बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
               "harvest": "90-120 દિવસ", "special": "🌺"},
    "Chrysanthemum": {"pic": "flower", "seed_guj": "સેવંતીની કટિંગ", "seed_hin": "गुलदाउदी कटिंग",
                      "look_guj": "10-15 સેમી લીલી", "look_hin": "10-15 सेमी डाली",
                      "rate": "કટિંગ", "germ": "15-20 દિવસ",
                      "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                      "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                      "harvest": "90-120 દિવસ", "special": "🌼"},
    "Bougainvillea": {"pic": "flower", "seed_guj": "ભોંગોની કટિંગ", "seed_hin": "बोगनवेलिया कटिंग",
                      "look_guj": "20-30 સેમી સખત", "look_hin": "20-30 सेमी डाली",
                      "rate": "કટિંગ", "germ": "20-30 દિવસ",
                      "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                      "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
                      "harvest": "6-8 મહિના", "special": "🌺"},
    "Ixora": {"pic": "flower", "seed_guj": "રંગૂનની કટિંગ", "seed_hin": "रंगून कटिंग",
              "look_guj": "10-15 સેમી લીલી", "look_hin": "10-15 सेमी डाली",
              "rate": "કટિંગ", "germ": "20-25 દિવસ",
              "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
              "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "પાણી નિયમિત",
              "harvest": "6-8 મહિના", "special": "🌸"},
    "Periwinkle": {"pic": "flower", "seed_guj": "સદાબહારનું બીજ", "seed_hin": "सदाबहार बीज",
                   "look_guj": "નાનો કાળો લાંબો", "look_hin": "छोटा काला",
                   "rate": "2-3 kg/એકર", "germ": "10-15 દિવસ",
                   "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                   "season_guj": "આખું વર્ષ", "care_guj": "ઓછું પાણી",
                   "harvest": "60-90 દિવસ", "special": "🌸"},
    "Crossandra": {"pic": "flower", "seed_guj": "અબોલીની કટિંગ", "seed_hin": "अबोली कटिंग",
                   "look_guj": "10-15 સેમી લીલી", "look_hin": "10-15 सेमी डाली",
                   "rate": "કટિંગ", "germ": "20-25 દિવસ",
                   "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                   "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                   "harvest": "6-8 મહિના", "special": "🌸"},
    "Aster": {"pic": "flower", "seed_guj": "તારલિયાનું બીજ", "seed_hin": "एस्टर बीज",
              "look_guj": "નાનો ભૂરો દાણો", "look_hin": "छोटा भूरा दाना",
              "rate": "200-300g/એકર", "germ": "10-15 દિવસ",
              "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
              "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
              "harvest": "90-120 દિવસ", "special": "🌸"},
    "Carnation": {"pic": "flower", "seed_guj": "કાર્નેશનનું બીજ", "seed_hin": "कार्नेशन बीज",
                  "look_guj": "નાનો કાળો ચપટો", "look_hin": "छोटा काला",
                  "rate": "200-300g/એકર", "germ": "10-15 દિવસ",
                  "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                  "season_guj": "સપ્ટે-ઓક્ટો", "care_guj": "પાણી નિયમિત",
                  "harvest": "90-120 દિવસ", "special": "🌹"},
    "Petunia": {"pic": "flower", "seed_guj": "પિટુનિયાનું બીજ", "seed_hin": "पेटुनिया बीज",
                "look_guj": "ખૂબ નાનો ભૂરો", "look_hin": "बहुत छोटा भूरा",
                "rate": "100-150g/એકર", "germ": "10-15 દિવસ",
                "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                "harvest": "60-90 દિવસ", "special": "🌺"},
    "Gerbera": {"pic": "flower", "seed_guj": "ગરબેરાનું બીજ", "seed_hin": "गेरबेरा बीज",
                "look_guj": "નાનો ભૂરો લાંબો", "look_hin": "छोटा भूरा",
                "rate": "100-150g/એકર", "germ": "10-15 દિવસ",
                "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
                "season_guj": "આખું વર્ષ", "care_guj": "પાણી નિયમિત",
                "harvest": "60-90 દિવસ", "special": "🌼"},
    "Tuberose": {"pic": "flower", "seed_guj": "રજનીગંધાનું કંદ", "seed_hin": "रजनीगंधा कंद",
                 "look_guj": "3-4 સેમી ગોળ", "look_hin": "3-4 सेमी कंद",
                 "rate": "કંદ", "germ": "15-20 દિવસ",
                 "method_guj": "કંદ વાવો.", "method_hin": "कंद बोएं।",
                 "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
                 "harvest": "90-120 દિવસ", "special": "🌸"},
    "Gladiolus": {"pic": "flower", "seed_guj": "ગ્લેડિયોલસનું કંદ", "seed_hin": "ग्लेडियोलस कंद",
                  "look_guj": "4-6 સેમી લાંબું", "look_hin": "4-6 सेमी कंद",
                  "rate": "કંદ", "germ": "15-20 દિવસ",
                  "method_guj": "કંદ વાવો.", "method_hin": "कंद बोएं।",
                  "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
                  "harvest": "90-120 દિવસ", "special": "🌺"},
    "Zinnia": {"pic": "flower", "seed_guj": "ઝીનિયાનું બીજ", "seed_hin": "ज़िन्निया बीज",
               "look_guj": "ચપટો ત્રિકોણાકાર", "look_hin": "चपटा त्रिकोण",
               "rate": "2-3 kg/એકર", "germ": "5-7 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
               "harvest": "60-80 દિવસ", "special": "🌸"},
    "Pansy": {"pic": "flower", "seed_guj": "પેન્સીનું બીજ", "seed_hin": "पैंसी बीज",
              "look_guj": "ખૂબ નાનો ભૂરો", "look_hin": "बहुत छोटा भूरा",
              "rate": "100-150g/એકર", "germ": "10-15 દિવસ",
              "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
              "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
              "harvest": "60-90 દિવસ", "special": "🌸"},
    "Daisy": {"pic": "flower", "seed_guj": "ગુલબહારનું બીજ", "seed_hin": "डेजी बीज",
              "look_guj": "ખૂબ નાનો ભૂરો", "look_hin": "बहुत छोटा भूरा",
              "rate": "200-300g/એકર", "germ": "10-15 દિવસ",
              "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
              "season_guj": "વસંત", "care_guj": "પાણી નિયમિત",
              "harvest": "60-90 દિવસ", "special": "🌼"},
    "Tulip": {"pic": "flower", "seed_guj": "ટ્યુલિપનું બલ્બ", "seed_hin": "ट्यूलिप बल्ब",
              "look_guj": "4-6 સેમી ગોળ", "look_hin": "4-6 सेमी बल्ब",
              "rate": "બલ્બ", "germ": "20-30 દિવસ",
              "method_guj": "બલ્બ વાવો.", "method_hin": "बल्ब बोएं।",
              "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "ઠંડું",
              "harvest": "60-90 દિવસ", "special": "🌷"},
    "Lavender": {"pic": "flower", "seed_guj": "લેવેન્ડરની કટિંગ", "seed_hin": "लैवेंडर कटिंग",
                 "look_guj": "10-15 સેમી લીલી", "look_hin": "10-15 सेमी डाली",
                 "rate": "કટિંગ", "germ": "20-30 દિવસ",
                 "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                 "season_guj": "જુલાઈ-ઓગસ્ટ", "care_guj": "ઓછું પાણી",
                 "harvest": "6-8 મહિના", "special": "💜"},
    "Anthurium": {"pic": "flower", "seed_guj": "એન્થુરિયમની કટિંગ", "seed_hin": "एंथुरियम कटिंग",
                  "look_guj": "10-15 સેમી લીલી", "look_hin": "10-15 सेमी डाली",
                  "rate": "કટિંગ", "germ": "25-30 દિવસ",
                  "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                  "season_guj": "આખું વર્ષ", "care_guj": "ભેજ",
                  "harvest": "1 વર્ષ", "special": "🌺"},
    "Champa": {"pic": "flower", "seed_guj": "ચંપાની કટિંગ", "seed_hin": "चंपा कटिंग",
               "look_guj": "20-30 સેમી ડાળી", "look_hin": "20-30 सेमी डाली",
               "rate": "કટિંગ", "germ": "20-30 દિવસ",
               "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
               "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
               "harvest": "2-3 વર્ષ", "special": "🌼"},
    "Kaner": {"pic": "flower", "seed_guj": "કનેરની કટિંગ", "seed_hin": "कनेर कटिंग",
              "look_guj": "15-20 સેમી ડાળી", "look_hin": "15-20 सेमी डाली",
              "rate": "કટિંગ", "germ": "20-30 દિવસ",
              "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
              "harvest": "1 વર્ષ", "special": "🌸"},
    "Rat Ki Rani": {"pic": "flower", "seed_guj": "રાતરાણીનું બીજ", "seed_hin": "रातरानी बीज",
                    "look_guj": "નાનો કાળો ગોળ", "look_hin": "छोटा काला",
                    "rate": "500g/એકર", "germ": "15-20 દિવસ",
                    "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                    "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                    "harvest": "4-5 મહિના", "special": "🌙"},
    "Mogra": {"pic": "flower", "seed_guj": "મોગરાની કટિંગ", "seed_hin": "मोगरा कटिंग",
              "look_guj": "15-20 સેમી લીલી", "look_hin": "15-20 सेमी डाली",
              "rate": "કટિંગ", "germ": "20-25 દિવસ",
              "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
              "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
              "harvest": "6-8 મહિના", "special": "🌸"},
    "Parijat": {"pic": "flower", "seed_guj": "પારિજાતની કટિંગ", "seed_hin": "पारिजात कटिंग",
                "look_guj": "15-20 સેમી ડાળી", "look_hin": "15-20 सेमी डाली",
                "rate": "કટિંગ", "germ": "20-30 દિવસ",
                "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                "harvest": "1 વર્ષ", "special": "🌸"},
    "Saffron": {"pic": "flower", "seed_guj": "કેસરનું કંદ", "seed_hin": "केसर कंद",
                "look_guj": "3-4 સેમી ગોળ", "look_hin": "3-4 सेमी कंद",
                "rate": "કંદ", "germ": "20-30 દિવસ",
                "method_guj": "કંદ વાવો.", "method_hin": "कंद बोएं।",
                "season_guj": "સપ્ટે-ઓક્ટો", "care_guj": "ઠંડું",
                "harvest": "1 વર્ષ", "special": "🌸"},
    "Kewda": {"pic": "flower", "seed_guj": "કેવડાની કટિંગ", "seed_hin": "केवड़ा कटिंग",
              "look_guj": "30-50 સેમી ડાળી", "look_hin": "30-50 सेमी डाली",
              "rate": "કટિંગ", "germ": "25-30 દિવસ",
              "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
              "harvest": "2-3 વર્ષ", "special": "🌸"},
    "Gulmohar": {"pic": "flower", "seed_guj": "ગુલમોહરનું બીજ", "seed_hin": "गुलमोहर बीज",
                 "look_guj": "લાંબું ચપટું બીજ", "look_hin": "लंबा चपटा बीज",
                 "rate": "2-3 kg/એકર", "germ": "20-30 દિવસ",
                 "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                 "season_guj": "જૂન-જુલાઈ", "care_guj": "ઓછું પાણી",
                 "harvest": "5-7 વર્ષ", "special": "🌺"},
    "Kadamba": {"pic": "flower", "seed_guj": "કદંબનું બીજ", "seed_hin": "कदंब बीज",
                "look_guj": "નાનું ગોળ બીજ", "look_hin": "छोटा गोल बीज",
                "rate": "2-3 kg/એકર", "germ": "15-20 દિવસ",
                "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                "harvest": "3-5 વર્ષ", "special": "🌸"},
    "Aparajita": {"pic": "flower", "seed_guj": "અપરાજિતાનું બીજ", "seed_hin": "अपराजिता बीज",
                  "look_guj": "નાનો ભૂરો ગોળ", "look_hin": "छोटा भूरा गोल",
                  "rate": "1-2 kg/એકર", "germ": "10-15 દિવસ",
                  "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                  "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                  "harvest": "60-90 દિવસ", "special": "💙"},
    
    # HERBS
    "Tulsi": {"pic": "herb", "seed_guj": "તુલસીનું બીજ", "seed_hin": "तुलसी बीज",
              "look_guj": "ખૂબ નાનો કાળો ગોળ", "look_hin": "बहुत छोटा काला",
              "rate": "200-300g/એકર", "germ": "7-10 દિવસ",
              "method_guj": "નર્સરીમાં.", "method_hin": "नर्सरी में।",
              "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
              "harvest": "60-90 દિવસ", "special": "🌿"},
    "Aloe Vera": {"pic": "herb", "seed_guj": "કુંવારપાઠું કૂંપળ", "seed_hin": "एलोवेरा कोंपल",
                  "look_guj": "છોટી કૂંપળ 10-15 સેમી", "look_hin": "छोटी कोंपल",
                  "rate": "કૂંપળ", "germ": "15-20 દિવસ",
                  "method_guj": "કૂંપળ વાવો.", "method_hin": "कोंपल बोएं।",
                  "season_guj": "આખું વર્ષ", "care_guj": "ઓછું પાણી",
                  "harvest": "8-10 મહિના", "special": "🌿"},
    "Mint": {"pic": "herb", "seed_guj": "ફુદીનાની કટિંગ", "seed_hin": "पुदीना कटिंग",
             "look_guj": "10-15 સેમી લીલી", "look_hin": "10-15 सेमी डाली",
             "rate": "કટિંગ", "germ": "7-10 દિવસ",
             "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
             "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
             "harvest": "30-45 દિવસ", "special": "🌿"},
    "Ashwagandha": {"pic": "herb", "seed_guj": "અશ્વગંધાનું બીજ", "seed_hin": "अश्वगंधा बीज",
                    "look_guj": "નાનો પીળો ગોળ", "look_hin": "छोटा पीला गोल",
                    "rate": "3-4 kg/એકર", "germ": "10-15 દિવસ",
                    "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                    "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "ઓછું પાણી",
                    "harvest": "150-180 દિવસ", "special": "🌿"},
    "Giloy": {"pic": "herb", "seed_guj": "ગિલોયની કટિંગ", "seed_hin": "गिलोय कटिंग",
              "look_guj": "15-20 સેમી લીલી વેલ", "look_hin": "15-20 सेमी बेल",
              "rate": "કટિંગ", "germ": "15-20 દિવસ",
              "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
              "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
              "harvest": "6-8 મહિના", "special": "🌿"},
    "Brahmi": {"pic": "herb", "seed_guj": "બ્રાહ્મીની કટિંગ", "seed_hin": "ब्राह्मी कटिंग",
               "look_guj": "10-15 સેમી લીલી વેલ", "look_hin": "10-15 सेमी बेल",
               "rate": "કટિંગ", "germ": "7-10 દિવસ",
               "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
               "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
               "harvest": "60-90 દિવસ", "special": "🌿"},
    "Lemongrass": {"pic": "herb", "seed_guj": "લેમનગ્રાસની કટિંગ", "seed_hin": "लेमनग्रास कटिंग",
                   "look_guj": "15-20 સેમી લીલી", "look_hin": "15-20 सेमी डाली",
                   "rate": "કટિંગ", "germ": "10-15 દિવસ",
                   "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                   "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                   "harvest": "90-120 દિવસ", "special": "🌿"},
    "Ajwain": {"pic": "seed", "seed_guj": "અજમાનું બીજ", "seed_hin": "अजवाइन बीज",
               "look_guj": "ખૂબ નાનો ભૂરો-લીલો", "look_hin": "बहुत छोटा भूरा",
               "rate": "2-3 kg/એકર", "germ": "7-10 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "2-3 વાર પાણી",
               "harvest": "100-120 દિવસ", "special": "🌿"},
    "Fennel": {"pic": "herb", "seed_guj": "વરિયાળીનું બીજ", "seed_hin": "सौंफ बीज",
               "look_guj": "લાંબો પાતળો લીલો", "look_hin": "लंबा पतला लंबा",
               "rate": "4-5 kg/એકર", "germ": "7-10 દિવસ",
               "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "2-3 વાર પાણી",
               "harvest": "120-150 દિવસ", "special": "🌿"},
    "Curry Leaf": {"pic": "herb", "seed_guj": "મીઠા લીમડાની કટિંગ", "seed_hin": "करी पत्ता कटिंग",
                   "look_guj": "15-20 સેમી લીલી", "look_hin": "15-20 सेमी डाली",
                   "rate": "કટિંગ", "germ": "20-30 દિવસ",
                   "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                   "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                   "harvest": "1 વર્ષ", "special": "🌿"},
    "Stevia": {"pic": "herb", "seed_guj": "સ્ટીવિયાની કટિંગ", "seed_hin": "स्टीविया कटिंग",
               "look_guj": "10-15 સેમી લીલી", "look_hin": "10-15 सेमी डाली",
               "rate": "કટિંગ", "germ": "10-15 દિવસ",
               "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
               "season_guj": "ફેબ્રુ-માર્ચ", "care_guj": "પાણી નિયમિત",
               "harvest": "60-90 દિવસ", "special": "🌿"},
    "Turmeric": {"pic": "herb", "seed_guj": "હળદરનું કંદ", "seed_hin": "हल्दी कंद",
                 "look_guj": "માતૃ કંદ 50-100g", "look_hin": "माँ कंद 50-100g",
                 "rate": "800-1000 kg/એકર", "germ": "15-20 દિવસ",
                 "method_guj": "કંદ વાવો.", "method_hin": "कंद बोएं।",
                 "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                 "harvest": "8-9 મહિના", "special": "🌿"},
    "Ginger": {"pic": "herb", "seed_guj": "આદુનું કંદ", "seed_hin": "अदरक कंद",
               "look_guj": "માતૃ કંદ 50-100g", "look_hin": "माँ कंद 50-100g",
               "rate": "800-1000 kg/એકર", "germ": "15-20 દિવસ",
               "method_guj": "કંદ વાવો.", "method_hin": "कंद बोएं।",
               "season_guj": "મે-જૂન", "care_guj": "પાણી નિયમિત",
               "harvest": "8-9 મહિના", "special": "🌿"},
    "Garlic": {"pic": "herb", "seed_guj": "લસણની કળી", "seed_hin": "लहसुन कली",
               "look_guj": "એક કળી 3-5g", "look_hin": "एक कली 3-5g",
               "rate": "200-250 kg/એકર", "germ": "10-15 દિવસ",
               "method_guj": "કળી વાવો.", "method_hin": "कली बोएं।",
               "season_guj": "ઓક્ટો-નવેમ્બર", "care_guj": "પાણી નિયમિત",
               "harvest": "120-150 દિવસ", "special": "🌿"},
    "Black Pepper": {"pic": "herb", "seed_guj": "કાળા મરીની કટિંગ", "seed_hin": "काली मिर्च कटिंग",
                     "look_guj": "15-20 સેમી લીલી વેલ", "look_hin": "15-20 सेमी बेल",
                     "rate": "કટિંગ", "germ": "20-30 દિવસ",
                     "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
                     "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                     "harvest": "2-3 વર્ષ", "special": "🌿"},
    "Cardamom": {"pic": "herb", "seed_guj": "ઈલાયચીની કટિંગ", "seed_hin": "इलायची कटिंग",
                 "look_guj": "15-20 સેમી રાઈઝોમ", "look_hin": "15-20 सेमी राइजोम",
                 "rate": "રાઈઝોમ", "germ": "20-30 દિવસ",
                 "method_guj": "રાઈઝોમ વાવો.", "method_hin": "राइजोम बोएं।",
                 "season_guj": "જૂન-જુલાઈ", "care_guj": "ભેજ",
                 "harvest": "2-3 વર્ષ", "special": "🌿"},
    "Shatavari": {"pic": "herb", "seed_guj": "શતાવરીનું બીજ", "seed_hin": "शतावरी बीज",
                  "look_guj": "નાનો કાળો ગોળ", "look_hin": "छोटा काला",
                  "rate": "3-4 kg/એકર", "germ": "15-20 દિવસ",
                  "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                  "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                  "harvest": "1-2 વર્ષ", "special": "🌿"},
    "Kalmegh": {"pic": "herb", "seed_guj": "કાળમેઘનું બીજ", "seed_hin": "कालमेघ बीज",
                "look_guj": "નાનો ભૂરો દાણો", "look_hin": "छोटा भूरा दाना",
                "rate": "1-2 kg/એકર", "germ": "10-15 દિવસ",
                "method_guj": "સીધું વાવો.", "method_hin": "सीधे बोएं।",
                "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                "harvest": "90-120 દિવસ", "special": "🌿"},
    "Vasaka": {"pic": "herb", "seed_guj": "અડૂલસાની કટિંગ", "seed_hin": "अडूसा कटिंग",
               "look_guj": "15-20 સેમી લીલી", "look_hin": "15-20 सेमी डाली",
               "rate": "કટિંગ", "germ": "20-30 દિવસ",
               "method_guj": "કટિંગ વાવો.", "method_hin": "कटिंग बोएं।",
               "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
               "harvest": "1 વર્ષ", "special": "🌿"},
    "Cinnamon": {"pic": "tree", "seed_guj": "તજનું બીજ", "seed_hin": "दालचीनी बीज",
                 "look_guj": "નાનો કથ્થઈ બીજ", "look_hin": "छोटा भूरा बीज",
                 "rate": "2-3 kg/એકર", "germ": "20-30 દિવસ",
                 "method_guj": "બીજ પલાળો.", "method_hin": "बीज भिगोएं।",
                 "season_guj": "જૂન-જુલાઈ", "care_guj": "પાણી નિયમિત",
                 "harvest": "2-3 વર્ષ", "special": "🌿"},
}

# ════════════════════════════════════════════════════════════════════
# MEDICINES (60+)
# ════════════════════════════════════════════════════════════════════
MED_DB = {
    "Quinalphos 25% EC": {"guj": "ક્વિનાલફોસ", "type": "કીટકનાશક", "price_100": 180, "price_1L": 1500, "dosage": "2ml/L", "target": "ઈયળ, થ્રિપ્સ", "safety": "🟡 માસ્ક", "wait": 7},
    "Chlorpyrifos 20% EC": {"guj": "ક્લોરપાયરીફોસ", "type": "કીટકનાશક", "price_100": 160, "price_1L": 1350, "dosage": "2.5ml/L", "target": "ઈયળ, બોરર", "safety": "🟠 ગ્લોવ્સ", "wait": 10},
    "Imidacloprid 17.8% SL": {"guj": "ઈમિડાક્લોપ્રિડ", "type": "કીટકનાશક", "price_100": 320, "price_1L": 2800, "dosage": "0.3ml/L", "target": "થ્રિપ્સ, સફેદ માખી", "safety": "🟠 ગ્લોવ્સ", "wait": 5},
    "Dimethoate 30% EC": {"guj": "ડાઈમેથોએટ", "type": "કીટકનાશક", "price_100": 140, "price_1L": 1200, "dosage": "2ml/L", "target": "માઈટ્સ, એફિડ", "safety": "🟠 ગ્લોવ્સ", "wait": 7},
    "Emamectin Benzoate": {"guj": "એમામેક્ટિન", "type": "કીટકનાશક", "price_100": 450, "price_1L": 4000, "dosage": "0.4g/L", "target": "આર્મીવોર્મ", "safety": "🟠 ગ્લોવ્સ", "wait": 7},
    "Thiamethoxam 25% WG": {"guj": "થાયામેથોક્સામ", "type": "કીટકનાશક", "price_100": 280, "price_1L": 2400, "dosage": "0.3g/L", "target": "થ્રિપ્સ, જેસિડ", "safety": "🟡 માસ્ક", "wait": 5},
    "Lambda Cyhalothrin": {"guj": "લેમ્બડા", "type": "કીટકનાશક", "price_100": 220, "price_1L": 1800, "dosage": "1ml/L", "target": "ઈયળ, થ્રિપ્સ", "safety": "🟠 ગ્લોવ્સ", "wait": 7},
    "Acephate 75% SP": {"guj": "એસેફેટ", "type": "કીટકનાશક", "price_100": 170, "price_1L": 1500, "dosage": "1g/L", "target": "થ્રિપ્સ", "safety": "🟡 માસ્ક", "wait": 7},
    "Fipronil 5% SC": {"guj": "ફિપ્રોનિલ", "type": "કીટકનાશક", "price_100": 380, "price_1L": 3200, "dosage": "1.5ml/L", "target": "બોરર", "safety": "🟠 ગ્લોવ્સ", "wait": 10},
    "Malathion 50% EC": {"guj": "મેલાથિઓન", "type": "કીટકનાશક", "price_100": 130, "price_1L": 1100, "dosage": "2ml/L", "target": "એફિડ", "safety": "🟡 માસ્ક", "wait": 5},
    "Cartap Hydrochloride": {"guj": "કાર્ટેપ", "type": "કીટકનાશક", "price_100": 250, "price_1L": 2200, "dosage": "1g/L", "target": "થડ બોરર", "safety": "🟡 માસ્ક", "wait": 10},
    "Monocrotophos 36%": {"guj": "મોનોક્રોટોફોસ", "type": "કીટકનાશક", "price_100": 150, "price_1L": 1300, "dosage": "1.5ml/L", "target": "ઈયળ", "safety": "🔴 ઝેરી", "wait": 15},
    "Profenofos 50% EC": {"guj": "પ્રોફેનોફોસ", "type": "કીટકનાશક", "price_100": 290, "price_1L": 2500, "dosage": "2ml/L", "target": "ઈયળ", "safety": "🟠 ગ્લોવ્સ", "wait": 10},
    "Mancozeb 75% WP": {"guj": "મેન્કોઝેબ", "type": "ફૂગનાશક", "price_100": 180, "price_1L": 1500, "dosage": "2.5g/L", "target": "બ્લાઈટ", "safety": "🟡 માસ્ક", "wait": 7},
    "Carbendazim 50% WP": {"guj": "કાર્બેન્ડાઝિમ", "type": "ફૂગનાશક", "price_100": 220, "price_1L": 1900, "dosage": "2g/L", "target": "વિલ્ટ", "safety": "🟡 માસ્ક", "wait": 7},
    "Copper Oxychloride": {"guj": "કોપર ઓક્સીક્લોરાઈડ", "type": "ફૂગનાશક", "price_100": 240, "price_1L": 2100, "dosage": "3g/L", "target": "બેક્ટેરિયલ", "safety": "🟡 માસ્ક", "wait": 7},
    "Propiconazole 25%": {"guj": "પ્રોપિકોનાઝોલ", "type": "ફૂગનાશક", "price_100": 320, "price_1L": 2800, "dosage": "1ml/L", "target": "રસ્ટ", "safety": "🟡 માસ્ક", "wait": 10},
    "Hexaconazole 5%": {"guj": "હેક્સાકોનાઝોલ", "type": "ફૂગનાશક", "price_100": 280, "price_1L": 2400, "dosage": "1ml/L", "target": "પાવડરી", "safety": "🟡 માસ્ક", "wait": 7},
    "Tebuconazole 25.9%": {"guj": "ટેબુકોનાઝોલ", "type": "ફૂગનાશક", "price_100": 380, "price_1L": 3300, "dosage": "1ml/L", "target": "રસ્ટ", "safety": "🟡 માસ્ક", "wait": 10},
    "Metalaxyl + Mancozeb": {"guj": "મેટાલેક્સિલ+મેન્કોઝેબ", "type": "ફૂગનાશક", "price_100": 380, "price_1L": 3200, "dosage": "2.5g/L", "target": "ડાઉની માઈલ્ડ્યુ", "safety": "🟡 માસ્ક", "wait": 7},
    "Sulphur 80% WDG": {"guj": "સલ્ફર", "type": "ફૂગનાશક", "price_100": 130, "price_1L": 1100, "dosage": "2g/L", "target": "પાવડરી", "safety": "🟢 સુરક્ષિત", "wait": 5},
    "Chlorothalonil 75%": {"guj": "ક્લોરોથાલોનિલ", "type": "ફૂગનાશક", "price_100": 340, "price_1L": 2900, "dosage": "2g/L", "target": "લીફ સ્પોટ", "safety": "🟡 માસ્ક", "wait": 7},
    "Azoxystrobin 23%": {"guj": "એઝોક્સિસ્ટ્રોબિન", "type": "ફૂગનાશક", "price_100": 520, "price_1L": 4500, "dosage": "1ml/L", "target": "બ્લાઈટ", "safety": "🟡 માસ્ક", "wait": 10},
    "Difenoconazole 25%": {"guj": "ડાઈફેનોકોનાઝોલ", "type": "ફૂગનાશક", "price_100": 420, "price_1L": 3600, "dosage": "0.5ml/L", "target": "સ્પોટ", "safety": "🟡 માસ્ક", "wait": 10},
    "Glyphosate 41% SL": {"guj": "ગ્લાયફોસેટ", "type": "નીંદણનાશક", "price_100": 180, "price_1L": 1500, "dosage": "10ml/L", "target": "નીંદણ", "safety": "🟡 માસ્ક", "wait": 0},
    "Paraquat 24% SL": {"guj": "પેરાક્વાટ", "type": "નીંદણનાશક", "price_100": 240, "price_1L": 2000, "dosage": "2ml/L", "target": "નીંદણ", "safety": "🔴 ઝેરી", "wait": 3},
    "Pendimethalin 30%": {"guj": "પેન્ડીમેથાલિન", "type": "નીંદણનાશક", "price_100": 240, "price_1L": 2100, "dosage": "3ml/L", "target": "ઘાસ", "safety": "🟡 માસ્ક", "wait": 0},
    "Atrazine 50% WP": {"guj": "એટ્રાઝીન", "type": "નીંદણનાશક", "price_100": 160, "price_1L": 1400, "dosage": "2g/L", "target": "ઘાસ", "safety": "🟡 માસ્ક", "wait": 0},
    "2,4-D Amine 58%": {"guj": "2,4-D", "type": "નીંદણનાશક", "price_100": 130, "price_1L": 1100, "dosage": "1ml/L", "target": "પહોળા પાન", "safety": "🟡 માસ્ક", "wait": 0},
    "Butachlor 50% EC": {"guj": "બ્યુટાક્લોર", "type": "નીંદણનાશક", "price_100": 180, "price_1L": 1500, "dosage": "2ml/L", "target": "ઘાસ", "safety": "🟡 માસ્ક", "wait": 0},
    "Carbendazim + Mancozeb": {"guj": "કાર્બેન્ડાઝિમ+મેન્કોઝેબ", "type": "કોમ્બો", "price_100": 280, "price_1L": 2400, "dosage": "2g/L", "target": "ફૂગ", "safety": "🟡 માસ્ક", "wait": 7},
    "Chlorpyrifos + Cypermethrin": {"guj": "ક્લોરપાયરીફોસ+સાયપરમેથ્રિન", "type": "કોમ્બો", "price_100": 320, "price_1L": 2800, "dosage": "2ml/L", "target": "ઈયળ", "safety": "🟠 ગ્લોવ્સ", "wait": 10},
    "Neem Oil 1500 PPM": {"guj": "નીમ તેલ", "type": "જૈવિક", "price_100": 250, "price_1L": 2200, "dosage": "5ml/L", "target": "ઈયળ", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Bacillus Thuringiensis": {"guj": "બી.ટી.", "type": "જૈવિક", "price_100": 320, "price_1L": 2800, "dosage": "2g/L", "target": "ઈયળ", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Trichoderma Viride": {"guj": "ટ્રાઈકોડર્મા", "type": "જૈવિક ફૂગનાશક", "price_100": 180, "price_1L": 1500, "dosage": "5g/L", "target": "મૂળ સડો", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Pseudomonas Fluorescens": {"guj": "સ્યુડોમોનાસ", "type": "જૈવિક ફૂગનાશક", "price_100": 200, "price_1L": 1700, "dosage": "5g/L", "target": "વિલ્ટ", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Urea (46% N)": {"guj": "યુરિયા", "type": "ખાતર", "price_100": 30, "price_1L": 250, "dosage": "50kg/એકર", "target": "નાઈટ્રોજન", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "DAP (18-46-0)": {"guj": "DAP", "type": "ખાતર", "price_100": 50, "price_1L": 420, "dosage": "50kg/એકર", "target": "N+P", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "MOP (60% K)": {"guj": "MOP", "type": "ખાતર", "price_100": 40, "price_1L": 320, "dosage": "30kg/એકર", "target": "પોટેશિયમ", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "NPK 19:19:19": {"guj": "NPK", "type": "ખાતર", "price_100": 80, "price_1L": 680, "dosage": "5g/L", "target": "સંતુલિત", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Zinc Sulphate 21%": {"guj": "ઝિંક સલ્ફેટ", "type": "સૂક્ષ્મ પોષક", "price_100": 120, "price_1L": 1000, "dosage": "0.5g/L", "target": "ઝિંક", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Ferrous Sulphate 19%": {"guj": "ફેરસ સલ્ફેટ", "type": "સૂક્ષ્મ પોષક", "price_100": 100, "price_1L": 850, "dosage": "0.5g/L", "target": "આયર્ન", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Boron 20%": {"guj": "બોરોન", "type": "સૂક્ષ્મ પોષક", "price_100": 150, "price_1L": 1300, "dosage": "0.3g/L", "target": "બોરોન", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Magnesium Sulphate": {"guj": "મેગ્નેશિયમ સલ્ફેટ", "type": "સૂક્ષ્મ પોષક", "price_100": 80, "price_1L": 700, "dosage": "0.5g/L", "target": "Mg", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Calcium Nitrate": {"guj": "કેલ્શિયમ નાઈટ્રેટ", "type": "ખાતર", "price_100": 90, "price_1L": 780, "dosage": "5g/L", "target": "Ca", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Potassium Sulphate": {"guj": "પોટેશિયમ સલ્ફેટ", "type": "ખાતર", "price_100": 70, "price_1L": 600, "dosage": "10g/L", "target": "K", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Vermicompost": {"guj": "વર્મીકમ્પોસ્ટ", "type": "જૈવિક ખાતર", "price_100": 15, "price_1L": 120, "dosage": "500kg/એકર", "target": "બધા", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Cow Dung Manure": {"guj": "ગોબર", "type": "જૈવિક ખાતર", "price_100": 5, "price_1L": 40, "dosage": "2 ton/એકર", "target": "બધા", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Poultry Manure": {"guj": "મરઘી ખાતર", "type": "જૈવિક ખાતર", "price_100": 8, "price_1L": 65, "dosage": "1 ton/એકર", "target": "N+P", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Bone Meal": {"guj": "હાડકાનો ભૂકો", "type": "જૈવિક ખાતર", "price_100": 25, "price_1L": 200, "dosage": "100kg/એકર", "target": "P", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Gibberellic Acid": {"guj": "GA3", "type": "વૃદ્ધિ નિયામક", "price_100": 250, "price_1L": 2200, "dosage": "0.1g/L", "target": "ફૂલ-ફળ", "safety": "🟡 ગ્લોવ્સ", "wait": 0},
    "NAA": {"guj": "NAA", "type": "વૃદ્ધિ નિયામક", "price_100": 200, "price_1L": 1750, "dosage": "0.5ml/L", "target": "ફૂલ ઝરવું", "safety": "🟡 ગ્લોવ્સ", "wait": 0},
    "Ethephon 39%": {"guj": "ઇથેફોન", "type": "વૃદ્ધિ નિયામક", "price_100": 220, "price_1L": 1900, "dosage": "1ml/L", "target": "ફળ પાકવું", "safety": "🟡 ગ્લોવ્સ", "wait": 0},
    "Panchagavya": {"guj": "પંચગવ્ય", "type": "જૈવિક ટોનિક", "price_100": 30, "price_1L": 250, "dosage": "30ml/L", "target": "સર્વાંગી", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Jeevamrut": {"guj": "જીવામૃત", "type": "જૈવિક ટોનિક", "price_100": 15, "price_1L": 120, "dosage": "100ml/L", "target": "જમીન", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Seaweed Extract": {"guj": "સીવીડ", "type": "જૈવિક ટોનિક", "price_100": 220, "price_1L": 1950, "dosage": "2ml/L", "target": "વૃદ્ધિ", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Humic Acid": {"guj": "હ્યુમિક એસિડ", "type": "જૈવિક ટોનિક", "price_100": 180, "price_1L": 1600, "dosage": "2ml/L", "target": "મૂળ", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Amino Acid": {"guj": "એમિનો એસિડ", "type": "જૈવિક ટોનિક", "price_100": 200, "price_1L": 1750, "dosage": "2ml/L", "target": "તણાવ", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Gypsum": {"guj": "જીપ્સમ", "type": "માટી સુધારક", "price_100": 8, "price_1L": 65, "dosage": "400kg/એકર", "target": "આલ્કલાઈન", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Agricultural Lime": {"guj": "ચૂનો", "type": "માટી સુધારક", "price_100": 6, "price_1L": 50, "dosage": "500kg/એકર", "target": "ઍસિડિક", "safety": "🟢 સુરક્ષિત", "wait": 0},
    "Zeolite": {"guj": "ઝિયોલાઈટ", "type": "માટી સુધારક", "price_100": 45, "price_1L": 380, "dosage": "100kg/એકર", "target": "પાણી ધારણ", "safety": "🟢 સુરક્ષિત", "wait": 0},
}

# ════════════════════════════════════════════════════════════════════
# HELPER DATA
# ════════════════════════════════════════════════════════════════════
def symptoms():
    return {
        "holes": {"problem": "Caterpillar", "problem_guj": "ઈયળ", "severity": "Moderate", "home": "નીમ તેલ 5ml/L", "market": "Quinalphos 2ml/L", "home_cost": "₹20-₹40", "market_cost": "₹100-₹180", "prevention": "નીમ સ્પ્રે."},
        "yellowing": {"problem": "Chlorosis", "problem_guj": "પાન પીળા", "severity": "Low", "home": "છાશ સ્પ્રે", "market": "Urea+Zinc", "home_cost": "₹15-₹30", "market_cost": "₹70-₹120", "prevention": "સંતુલિત ખાતર."},
        "spots": {"problem": "Fungal Spot", "problem_guj": "ફૂગ ડાઘ", "severity": "Moderate", "home": "હળદર+સોડા", "market": "Mancozeb 2.5g/L", "home_cost": "₹20-₹40", "market_cost": "₹130-₹220", "prevention": "ભેજ નિયંત્રણ."},
        "curl": {"problem": "Leaf Curl", "problem_guj": "પાન વળવા", "severity": "Moderate", "home": "લસણ-મરચી", "market": "Imidacloprid 0.3ml/L", "home_cost": "₹20-₹45", "market_cost": "₹130-₹220", "prevention": "સ્ટીકી ટ્રેપ."},
        "wilting": {"problem": "Wilt", "problem_guj": "કરમાવું", "severity": "Severe", "home": "ગૌમૂત્ર ડ્રેન્ચ", "market": "Carbendazim 2g/L", "home_cost": "₹25-₹50", "market_cost": "₹180-₹300", "prevention": "ડ્રેનેજ."},
        "healthy": {"problem": "Healthy", "problem_guj": "સ્વસ્થ", "severity": "None", "home": "ચાલુ રાખો", "market": "કોઈ નહીં", "home_cost": "₹0", "market_cost": "₹0", "prevention": "સંભાળ."},
    }

GUJ_NAMES = {
    "Neem": "લીમડો", "Mango": "આંબો", "Banana": "કેળા", "Lemon": "લીંબુ", "Papaya": "પપૈયા",
    "Guava": "જામફળ", "Pomegranate": "દાડમ", "Coconut": "નાળિયેરી", "Teak": "સાગ",
    "Drumstick": "સરગવો", "Sapota": "ચીકુ", "Custard Apple": "સીતાફળ", "Jamun Tree": "જાંબુ",
    "Jackfruit": "ફણસ", "Amla Tree": "આંવળા", "Ber Tree": "બોર", "Fig Tree": "અંજીર",
    "Moringa": "મોરિંગા", "Gulmohar Tree": "ગુલમોહર", "Kadamba Tree": "કદંબ",
    "Silver Oak": "સિલ્વર ઓક", "Rain Tree": "વરસાદી",
    "Paddy": "ડાંગર", "Wheat": "ઘઉં", "Bajra": "બાજરી", "Jowar": "જુવાર", "Maize": "મકાઈ",
    "Ragi": "રાગી", "Barley": "જવ", "Oats": "ઓટ્સ", "Kodo Millet": "કોદરો", "Kutki": "કુટકી",
    "Barnyard Millet": "સામો", "Little Millet": "કંગ", "Foxtail Millet": "કાંગ",
    "Amaranth": "રાજગરો", "Quinoa": "ક્વિનોઆ",
    "Cotton": "કપાસ", "Groundnut": "મગફળી", "Castor": "એરંડા", "Cumin": "જીરું",
    "Sesame": "તલ", "Pigeon Pea": "તુવેર", "Gram": "ચણા", "Moong": "મગ", "Urad": "અડદ",
    "Mustard": "રાઈ", "Sunflower": "સૂરજમુખી", "Sugarcane": "શેરડી", "Soybean": "સોયાબીન",
    "Tobacco": "તમાકુ", "Jute": "શણ", "Cowpea": "ચોળા", "Horse Gram": "કળથી",
    "Lentil": "મસૂર", "Rajma": "રાજમા", "Chickpea": "કાબુલી ચણા",
    "Tomato": "ટમેટી", "Potato": "બટાટા", "Chili": "મરચી", "Brinjal": "રીંગણી",
    "Onion": "ડુંગળી", "Cabbage": "કોબીજ", "Cauliflower": "ફૂલકોબી", "Bottle Gourd": "દૂધી",
    "Bitter Gourd": "કારેલા", "Ladyfinger": "ભીંડો", "Cucumber": "કાકડી", "Pumpkin": "કોળું",
    "Carrot": "ગાજર", "Radish": "મૂળો", "Spinach": "પાલક", "Fenugreek": "મેથી",
    "Coriander": "કોથમીર", "Pea": "વટાણા", "Beans": "ફણસી", "Cluster Beans": "ગુવાર",
    "Ridge Gourd": "તૂરિયા", "Sponge Gourd": "ગલકા", "Pointed Gourd": "પરવળ",
    "Beetroot": "બીટ", "Bell Pepper": "શિમલા મરચી", "Sweet Corn": "ગળી મકાઈ",
    "Turnip": "શલગમ", "Sweet Potato": "શક્કરિયા", "Colocasia": "અળવી", "Yam": "રતાળુ",
    "Broccoli": "બ્રોકોલી", "Lettuce": "લેટ્યુસ", "Celery": "સેલરી",
    "Asparagus": "શતાવરી", "Zucchini": "ઝુકીની",
    "Grape": "દ્રાક્ષ", "Watermelon": "તરબૂચ", "Muskmelon": "શક્કરટેટી",
    "Strawberry": "સ્ટ્રોબેરી", "Pineapple": "અનાનસ", "Fig": "અંજીર",
    "Jamun": "જાંબુ", "Jackfruit": "ફણસ", "Ber": "બોર", "Amla": "આંવળા",
    "Custard Fruit": "સીતાફળ", "Orange": "સંતરા", "Sweet Lime": "મોસંબી", "Pear": "નાસપતી",
    "Peach": "આલૂ", "Plum": "આલુબુખારા", "Cherry": "ચેરી", "Kiwi": "કીવી",
    "Dragon Fruit": "ડ્રેગન ફ્રુટ", "Avocado": "એવોકાડો",
    "Rose": "ગુલાબ", "Marigold": "ગલગોટો", "Jasmine": "મોગરો", "Lotus": "કમળ",
    "Orchid": "ઓર્કિડ", "Hibiscus": "જાસૂદ", "Lily": "લિલી", "Dahlia": "ડેહલિયા",
    "Chrysanthemum": "સેવંતી", "Bougainvillea": "ભોંગો", "Ixora": "રંગૂન",
    "Periwinkle": "સદાબહાર", "Crossandra": "અબોલી", "Aster": "તારલિયો",
    "Carnation": "કાર્નેશન", "Petunia": "પિટુનિયા", "Gerbera": "ગરબેરા",
    "Tuberose": "રજનીગંધા", "Gladiolus": "ગ્લેડિયોલસ", "Zinnia": "ઝીનિયા",
    "Pansy": "પેન્સી", "Daisy": "ગુલબહાર", "Tulip": "ટ્યુલિપ", "Lavender": "લેવેન્ડર",
    "Anthurium": "એન્થુરિયમ", "Champa": "ચંપો", "Kaner": "કનેર", "Rat Ki Rani": "રાતરાણી",
    "Mogra": "મોગરો", "Parijat": "પારિજાત", "Saffron": "કેસર", "Kewda": "કેવડો",
    "Gulmohar": "ગુલમોહર", "Kadamba": "કદંબ", "Aparajita": "અપરાજિતા",
    "Tulsi": "તુલસી", "Aloe Vera": "કુંવારપાઠું", "Mint": "ફુદીનો", "Ashwagandha": "અશ્વગંધા",
    "Giloy": "ગિલોય", "Brahmi": "બ્રાહ્મી", "Lemongrass": "લેમનગ્રાસ",
    "Ajwain": "અજમો", "Fennel": "વરિયાળી", "Curry Leaf": "મીઠો લીમડો",
    "Stevia": "સ્ટીવિયા", "Turmeric": "હળદર", "Ginger": "આદુ", "Garlic": "લસણ",
    "Black Pepper": "કાળા મરી", "Cardamom": "ઈલાયચી", "Shatavari": "શતાવરી",
    "Kalmegh": "કાળમેઘ", "Vasaka": "અડૂલસો", "Cinnamon": "તજ"
}

def determine_category(crop_name):
    grains = ["Paddy", "Wheat", "Bajra", "Jowar", "Maize", "Ragi", "Barley", "Oats",
              "Kodo Millet", "Kutki", "Barnyard Millet", "Little Millet", "Foxtail Millet",
              "Amaranth", "Quinoa"]
    cash = ["Cotton", "Groundnut", "Castor", "Cumin", "Sesame", "Pigeon Pea", "Gram",
            "Moong", "Urad", "Mustard", "Sunflower", "Sugarcane", "Soybean", "Tobacco",
            "Jute", "Cowpea", "Horse Gram", "Lentil", "Rajma", "Chickpea"]
    veg = ["Tomato", "Potato", "Chili", "Brinjal", "Onion", "Cabbage", "Cauliflower",
           "Bottle Gourd", "Bitter Gourd", "Ladyfinger", "Cucumber", "Pumpkin", "Carrot",
           "Radish", "Spinach", "Fenugreek", "Coriander", "Pea", "Beans", "Cluster Beans",
           "Ridge Gourd", "Sponge Gourd", "Pointed Gourd", "Beetroot", "Bell Pepper",
           "Sweet Corn", "Turnip", "Sweet Potato", "Colocasia", "Yam", "Broccoli",
           "Lettuce", "Celery", "Asparagus", "Zucchini"]
    fruit = ["Grape", "Watermelon", "Muskmelon", "Strawberry", "Pineapple", "Fig",
             "Jamun", "Jackfruit", "Ber", "Amla", "Custard Fruit", "Orange",
             "Sweet Lime", "Pear", "Peach", "Plum", "Cherry", "Kiwi", "Dragon Fruit",
             "Avocado"]
    flower = ["Rose", "Marigold", "Jasmine", "Lotus", "Orchid", "Hibiscus", "Lily",
              "Dahlia", "Chrysanthemum", "Bougainvillea", "Ixora", "Periwinkle",
              "Crossandra", "Aster", "Carnation", "Petunia", "Gerbera", "Tuberose",
              "Gladiolus", "Zinnia", "Pansy", "Daisy", "Tulip", "Lavender",
              "Anthurium", "Champa", "Kaner", "Rat Ki Rani", "Mogra", "Parijat",
              "Saffron", "Kewda", "Gulmohar", "Kadamba", "Aparajita"]
    herb = ["Tulsi", "Aloe Vera", "Mint", "Ashwagandha", "Giloy", "Brahmi",
            "Lemongrass", "Ajwain", "Fennel", "Curry Leaf", "Stevia", "Turmeric",
            "Ginger", "Garlic", "Black Pepper", "Cardamom", "Shatavari", "Kalmegh",
            "Vasaka", "Cinnamon"]
    if crop_name in EXTRA_CAT: return EXTRA_CAT[crop_name]
    if crop_name in grains: return "Grains"
    if crop_name in cash: return "Cash Crops"
    if crop_name in veg: return "Vegetables"
    if crop_name in fruit: return "Fruits"
    if crop_name in flower: return "Flowers"
    if crop_name in herb: return "Herbs"
    return "Trees"

# ════════════════════════════════════════════════════════════════════
# ➕ EXTRA CROPS (33 grains, 10 flowers, 10 trees) - added on top of SEED_DB
# ════════════════════════════════════════════════════════════════════
_EX_M = {1: ("સીધું વાવો.", "सीधे बोएं।"), 2: ("નર્સરીમાં વાવો.", "नर्सरी में बोएं।"), 3: ("બીજ પલાળો.", "बीज भिगोएं।"),
         4: ("સીધા ખેતરમાં.", "सीधे खेत में।"), 5: ("કટિંગ વાવો.", "कटिंग बोएं।"), 6: ("બીજ 12 કલાક પલાળો.", "बीज 12 घंटे भिगोएं।"),
         7: ("સીધું ખેતરમાં, લાઈન થી લાઈન 20 સેમી.", "सीधे खेत में, लाइन से लाइन 20 सेमी।")}
_EX_L = {"નાનો": "छोटा", "મોટો": "बड़ा", "લાંબો": "लंबा", "પાતળો": "पतला", "ગોળ": "गोल", "ચપટો": "चपटा", "અંડાકાર": "अंडाकार",
         "ત્રિકોણાકાર": "त्रिकोणाकार", "સફેદ": "सफेद", "કાળો": "काला", "ભૂરો": "भूरा", "પીળો": "पीला", "લાલ": "लाल",
         "ગુલાબી": "गुलाबी", "સોનેરી": "सुनहरा", "લીલો": "हरा"}
# n | gujarati | hindi | category | wikipedia | season | seed rate | germination | harvest | care | method | look | special
_EX_ROWS = """
Basmati Rice|બાસમતી ચોખા|बासमती चावल|Grains|Basmati|જૂન-જુલાઈ|8-10 kg/એકર|5-7 દિવસ|120-140 દિવસ|પાણી ભરેલું ખેતર|2|લાંબો પાતળો|🌾 મુખ્ય અનાજ
Black Rice|કાળા ચોખા|काला चावल|Grains|Black rice|જૂન-જુલાઈ|8-10 kg/એકર|5-7 દિવસ|130-150 દિવસ|પાણી ભરેલું ખેતર|2|કાળો અંડાકાર|🌾 સુપરફૂડ
Red Rice|લાલ ચોખા|लाल चावल|Grains|Red rice|જૂન-જુલાઈ|8-10 kg/એકર|5-7 દિવસ|120-140 દિવસ|પાણી ભરેલું ખેતર|2|લાલ અંડાકાર|🌾 આરોગ્ય
Durum Wheat|ડ્યુરમ ઘઉં|ड्यूरम गेहूं|Grains|Durum|ઓક્ટો-નવેમ્બર|40-50 kg/એકર|5-7 દિવસ|110-130 દિવસ|3-4 વાર પાણી|7|સોનેરી અંડાકાર|🌾 શિયાળાનો
Emmer Wheat|ખપલી ઘઉં|खपली गेहूं|Grains|Emmer|ઓક્ટો-નવેમ્બર|40-50 kg/એકર|7-10 દિવસ|110-120 દિવસ|2-3 વાર પાણી|7|ભૂરો લાંબો|🌾 આરોગ્ય
Sharbati Wheat|શરબતી ઘઉં|शरबती गेहूं|Grains|Wheat|ઓક્ટો-નવેમ્બર|40-50 kg/એકર|5-7 દિવસ|120-135 દિવસ|4-5 વાર પાણી|7|સોનેરી ગોળ|🌾 શિયાળાનો
Lokwan Wheat|લોકવન ઘઉં|लोकवन गेहूं|Grains|Wheat|ઓક્ટો-નવેમ્બર|40-50 kg/એકર|5-7 દિવસ|115-130 દિવસ|3-4 વાર પાણી|7|સોનેરી ગોળ|🌾 શિયાળાનો
Spelt|સ્પેલ્ટ ઘઉં|स्पेल्ट गेहूं|Grains|Spelt|ઓક્ટો-નવેમ્બર|40-50 kg/એકર|7-10 દિવસ|120-140 દિવસ|2-3 વાર પાણી|7|ભૂરો લાંબો|🌾 પ્રોટીન
Triticale|ટ્રિટિકેલ|ट्रिटिकेल|Grains|Triticale|ઓક્ટો-નવેમ્બર|40-50 kg/એકર|5-7 દિવસ|110-130 દિવસ|3-4 વાર પાણી|7|ભૂરો અંડાકાર|🌾 ઝડપી
Buckwheat|કુટ્ટુ|कुट्टू|Grains|Buckwheat|સપ્ટે-ઓક્ટો|20-25 kg/એકર|3-5 દિવસ|60-80 દિવસ|ઓછું પાણી|1|ત્રિકોણાકાર ભૂરો|🌾 આરોગ્ય
Proso Millet|ચેના|चेना|Grains|Proso millet|જૂન-જુલાઈ|8-10 kg/એકર|3-5 દિવસ|60-70 દિવસ|ઓછું પાણી|1|પીળો ગોળ|🌾 સૂકો
Browntop Millet|બ્રાઉનટોપ બાજરી|ब्राउनटॉप बाजरा|Grains|Browntop millet|જૂન-જુલાઈ|6-8 kg/એકર|3-5 દિવસ|70-90 દિવસ|ઓછું પાણી|1|નાનો ભૂરો|🌾 સૂકો
Sweet Sorghum|મીઠી જુવાર|मीठी ज्वार|Grains|Sweet sorghum|જૂન-જુલાઈ|3-4 kg/એકર|5-7 દિવસ|120-140 દિવસ|3-4 વાર પાણી|7|ગોળ લાલ|🌾 ઝડપી
Hybrid Sorghum|હાઇબ્રિડ જુવાર|हाइब्रिड ज्वार|Grains|Sorghum|જૂન-જુલાઈ|3-4 kg/એકર|5-7 દિવસ|100-120 દિવસ|2-3 વાર પાણી|7|ગોળ સફેદ|🌾 મુખ્ય અનાજ
Fodder Sorghum|ચારા જુવાર|चारा ज्वार|Grains|Sorghum|જૂન-જુલાઈ|10-12 kg/એકર|5-7 દિવસ|60-70 દિવસ|3-4 વાર પાણી|1|ગોળ ભૂરો|🌾 ઝડપી
Pearl Millet Hybrid|હાઇબ્રિડ બાજરી|हाइब्रिड बाजरा|Grains|Pearl millet|જૂન-જુલાઈ|1-2 kg/એકર|3-5 દિવસ|75-90 દિવસ|ઓછું પાણી|7|ગોળ ભૂરો|🌾 સૂકો
Popcorn|પોપકોર્ન મકાઈ|पॉपकॉर्न मक्का|Grains|Popcorn|જૂન-જુલાઈ|8-10 kg/એકર|5-7 દિવસ|90-110 દિવસ|3-4 વાર પાણી|7|પીળો ગોળ|🌾 ઝડપી
Baby Corn|બેબી કોર્ન|बेबी कॉर्न|Grains|Baby corn|ફેબ્રુ-માર્ચ|15-20 kg/એકર|5-7 દિવસ|50-60 દિવસ|3-4 વાર પાણી|7|પીળો ગોળ|🌾 ઝડપી
Wild Rice|જંગલી ચોખા|जंगली चावल|Grains|Wild rice|જૂન-જુલાઈ|8-10 kg/એકર|7-10 દિવસ|120-140 દિવસ|પાણી ભરેલું ખેતર|2|કાળો પાતળો|🌾 સુપરફૂડ
Teff|ટેફ|टेफ|Grains|Teff|જૂન-જુલાઈ|1-2 kg/એકર|3-5 દિવસ|90-110 દિવસ|ઓછું પાણી|1|નાનો ભૂરો|🌾 લોહ તત્વ
Fonio|ફોનિયો|फोनियो|Grains|Fonio|જૂન-જુલાઈ|3-4 kg/એકર|3-5 દિવસ|60-70 દિવસ|ઓછું પાણી|1|નાનો સફેદ|🌾 સૂકો
Jobs Tears|જોબ્સ ટીયર્સ|जॉब्स टियर्स|Grains|Coix lacryma-jobi|જૂન-જુલાઈ|8-10 kg/એકર|7-10 દિવસ|120-150 દિવસ|3-4 વાર પાણી|3|ગોળ ભૂરો|🌾 આરોગ્ય
Chia|ચિયા|चिया|Grains|Chia|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|5-7 દિવસ|100-120 દિવસ|ઓછું પાણી|1|નાનો કાળો|🌾 સુપરફૂડ
Flaxseed|અળસી|अलसी|Grains|Flax|ઓક્ટો-નવેમ્બર|10-12 kg/એકર|5-7 દિવસ|110-130 દિવસ|2-3 વાર પાણી|1|પાતળો ભૂરો|🥜 તેલ
Niger Seed|રામતલ|रामतिल|Grains|Guizotia abyssinica|જૂન-જુલાઈ|3-4 kg/એકર|5-7 દિવસ|90-100 દિવસ|ઓછું પાણી|1|નાનો કાળો|🥜 તેલ
Safflower|કુસુમ|कुसुम|Grains|Safflower|સપ્ટે-ઓક્ટો|8-10 kg/એકર|5-7 દિવસ|120-140 દિવસ|2-3 વાર પાણી|1|ચપટો સફેદ|🥜 તેલ
Rapeseed|રાયડો|राया|Grains|Rapeseed|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|3-5 દિવસ|100-120 દિવસ|2-3 વાર પાણી|1|નાનો કાળો|🥜 તેલ
Black Sesame|કાળા તલ|काले तिल|Grains|Sesame|જૂન-જુલાઈ|1-2 kg/એકર|3-5 દિવસ|80-100 દિવસ|ઓછું પાણી|1|નાનો કાળો|🥜 તેલ
Isabgol|ઇસબગુલ|इसबगोल|Grains|Psyllium|ઓક્ટો-નવેમ્બર|3-4 kg/એકર|5-7 દિવસ|110-130 દિવસ|2-3 વાર પાણી|1|નાનો ગુલાબી|🌿 ઔષધીય વૃક્ષ
Kalonji|કલોંજી|कलौंजी|Grains|Nigella sativa|ઓક્ટો-નવેમ્બર|3-4 kg/એકર|7-10 દિવસ|120-140 દિવસ|2-3 વાર પાણી|1|નાનો કાળો|🌿 મસાલો
Moth Bean|મઠ|मोठ|Grains|Vigna aconitifolia|જૂન-જુલાઈ|8-10 kg/એકર|3-5 દિવસ|60-80 દિવસ|ઓછું પાણી|1|નાનો ભૂરો|🫘 પ્રોટીન
Rice Bean|રાઈસ બીન|राइस बीन|Grains|Rice bean|જૂન-જુલાઈ|8-10 kg/એકર|5-7 દિવસ|90-110 દિવસ|3-4 વાર પાણી|1|નાનો પીળો|🫘 દાળ
Field Pea|ખેતરના વટાણા|खेत की मटर|Grains|Pea|ઓક્ટો-નવેમ્બર|40-50 kg/એકર|7-10 દિવસ|90-110 દિવસ|2-3 વાર પાણી|1|ગોળ પીળો|🫘 પ્રોટીન
Cosmos|કોસ્મોસ|कॉसमॉस|Flowers|Cosmos (plant)|ઓક્ટો-ફેબ્રુ|1-2 kg/એકર|7-10 દિવસ|60-90 દિવસ|પાણી નિયમિત|2|નાનો કાળો|🌸 શોભાવાળું
Calendula|કેલેન્ડુલા|कैलेंडुला|Flowers|Calendula|ઓક્ટો-ફેબ્રુ|1-2 kg/એકર|7-10 દિવસ|60-90 દિવસ|પાણી નિયમિત|2|ભૂરો લાંબો|🌸 સુગંધી
Gaillardia|ગેલાર્ડિયા|गेलार्डिया|Flowers|Gaillardia|ઓક્ટો-ફેબ્રુ|1-2 kg/એકર|7-10 દિવસ|60-90 દિવસ|ઓછું પાણી|2|નાનો ભૂરો|🌸 શોભાવાળું
Celosia|સેલોસિયા|सेलोशिया|Flowers|Celosia|જૂન-જુલાઈ|1-2 kg/એકર|7-10 દિવસ|60-80 દિવસ|પાણી નિયમિત|2|નાનો કાળો|🌸 શોભાવાળું
Canna|કેના|कैना|Flowers|Canna (plant)|જૂન-જુલાઈ|1-2 kg/એકર|15-20 દિવસ|90-120 દિવસ|પાણી નિયમિત|3|ગોળ કાળો|🌸 શોભાવાળું
Salvia|સાલ્વિયા|सालविया|Flowers|Salvia|ઓક્ટો-ફેબ્રુ|1-2 kg/એકર|7-10 દિવસ|60-90 દિવસ|પાણી નિયમિત|2|નાનો કાળો|🌸 લાલ ફૂલ
Snapdragon|સ્નેપડ્રેગન|स्नैपड्रैगन|Flowers|Snapdragon|ઓક્ટો-ફેબ્રુ|1-2 kg/એકર|7-10 દિવસ|80-100 દિવસ|પાણી નિયમિત|2|નાનો ભૂરો|🌸 શોભાવાળું
Sweet Pea|સ્વીટ પી|स्वीट पी|Flowers|Sweet pea|ઓક્ટો-નવેમ્બર|3-4 kg/એકર|7-10 દિવસ|80-100 દિવસ|પાણી નિયમિત|6|ગોળ ભૂરો|🌸 સુગંધી
Balsam|ગુલમેંદી|गुलमेंहदी|Flowers|Impatiens balsamina|જૂન-જુલાઈ|1-2 kg/એકર|7-10 દિવસ|60-80 દિવસ|પાણી નિયમિત|2|નાનો કાળો|🌸 શોભાવાળું
Hollyhock|હોલીહોક|होलीहॉक|Flowers|Hollyhock|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|7-10 દિવસ|90-120 દિવસ|ઓછું પાણી|2|ચપટો ભૂરો|🌸 શોભાવાળું
Banyan|વડ|वट वृक्ष|Trees|Ficus benghalensis|જૂન-જુલાઈ|1-2 kg/એકર|15-20 દિવસ|10-15 વર્ષ|ઓછું પાણી|2|નાનો લાલ|🌳 છાયાદાર
Peepal|પીપળો|पीपल|Trees|Ficus religiosa|જૂન-જુલાઈ|1-2 kg/એકર|15-20 દિવસ|10-15 વર્ષ|ઓછું પાણી|2|નાનો ભૂરો|🌳 છાયાદાર
Mahua|મહુડો|महुआ|Trees|Madhuca longifolia|જૂન-જુલાઈ|2-3 kg/એકર|20-30 દિવસ|8-10 વર્ષ|ઓછું પાણી|3|મોટો ભૂરો|🌳 મોંઘું લાકડું
Arjun Tree|અર્જુન|अर्जुन|Trees|Terminalia arjuna|જૂન-જુલાઈ|2-3 kg/એકર|15-20 દિવસ|10-15 વર્ષ|ઓછું પાણી|2|નાનો ભૂરો|🌿 ઔષધીય વૃક્ષ
Ashoka|અશોક|अशोक|Trees|Saraca asoca|જૂન-જુલાઈ|2-3 kg/એકર|20-30 દિવસ|8-10 વર્ષ|પાણી નિયમિત|3|મોટો ભૂરો|🌿 ઔષધીય વૃક્ષ
Babool|બાવળ|बबूल|Trees|Vachellia nilotica|જૂન-જુલાઈ|2-3 kg/એકર|7-10 દિવસ|8-10 વર્ષ|ઓછું પાણી|3|ચપટો ભૂરો|🌳 મોંઘું લાકડું
Khejri|ખીજડો|खेजड़ी|Trees|Prosopis cineraria|જૂન-જુલાઈ|2-3 kg/એકર|7-10 દિવસ|10-15 વર્ષ|ઓછું પાણી|3|નાનો ભૂરો|🌳 છાયાદાર
Sandalwood|ચંદન|चंदन|Trees|Sandalwood|જૂન-જુલાઈ|2-3 kg/એકર|20-30 દિવસ|15-20 વર્ષ|ઓછું પાણી|3|ગોળ કાળો|🌳 મોંઘું લાકડું
Eucalyptus|નીલગિરી|नीलगिरी|Trees|Eucalyptus|જૂન-જુલાઈ|1-2 kg/એકર|7-10 દિવસ|5-7 વર્ષ|ઓછું પાણી|2|નાનો ભૂરો|🌳 ઝડપી
Bamboo|વાંસ|बांस|Trees|Bamboo|જૂન-જુલાઈ|1-2 kg/એકર|15-20 દિવસ|3-5 વર્ષ|પાણી નિયમિત|5|નાનો ભૂરો|🌳 ઝડપી
"""
EXTRA_CAT, EXTRA_WIKI = {"Coriander": "Grains"}, {}
for _ln in _EX_ROWS.strip().splitlines():
    _n, _g, _h, _cat, _wk, _se, _ra, _ge, _ha, _ca, _mi, _lk, _sp = _ln.split("|")
    _adj = _lk.split()
    SEED_DB[_n] = {"pic": "plant", "seed_guj": _g + " બીજ", "seed_hin": _h + " बीज",
                   "look_guj": _lk + " દાણો", "look_hin": " ".join(_EX_L[a] for a in _adj) + " दाना",
                   "rate": _ra, "germ": _ge, "method_guj": _EX_M[int(_mi)][0], "method_hin": _EX_M[int(_mi)][1],
                   "season_guj": _se, "care_guj": _ca, "harvest": _ha, "special": _sp, "_h": _h}
    GUJ_NAMES[_n] = _g
    EXTRA_CAT[_n] = _cat
    EXTRA_WIKI[_n] = _wk

# ════════════════════════════════════════════════════════════════════
# ➕ MORE CROPS (110: vegetables, fruits, cash crops, herbs, flowers, trees)
# ════════════════════════════════════════════════════════════════════
_EX_M.update({8: ("નર્સરીમાં વાવો, 25-30 દિવસ પછી રોપો.", "नर्सरी में बोएं, 25-30 दिन बाद रोपें।"),
              9: ("ગ્રાફ્ટિંગ સારું.", "ग्राफ्टिंग बेहतर।"), 10: ("કટિંગ સારું.", "कटिंग बेहतर।")})
_EX_ROWS2 = """
Kohlrabi|નોલકોલ|गांठ गोभी|Vegetables|Kohlrabi|સપ્ટે-ઓક્ટો|250-300 g/એકર|5-7 દિવસ|55-65 દિવસ|પાણી નિયમિત|8|નાનો ગોળ|🥬
Red Cabbage|લાલ કોબી|लाल पत्तागोभी|Vegetables|Red cabbage|સપ્ટે-ઓક્ટો|250-300 g/એકર|5-7 દિવસ|90-100 દિવસ|પાણી નિયમિત|8|નાનો ગોળ|🥬
Chinese Cabbage|ચાઈનીઝ કોબી|चाइनीज़ पत्तागोभी|Vegetables|Napa cabbage|સપ્ટે-ઓક્ટો|250-300 g/એકર|5-7 દિવસ|60-70 દિવસ|પાણી નિયમિત|8|નાનો ગોળ|🥬
Brussels Sprouts|બ્રસેલ્સ સ્પ્રાઉટ્સ|ब्रसेल्स स्प्राउट्स|Vegetables|Brussels sprout|ઓક્ટો-નવેમ્બર|250-300 g/એકર|5-7 દિવસ|90-100 દિવસ|પાણી નિયમિત|8|નાનો ગોળ|🥬
Leek|લીક|लीक|Vegetables|Leek|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|7-10 દિવસ|120-150 દિવસ|પાણી નિયમિત|8|નાનો કાળો|🧅
Spring Onion|લીલી ડુંગળી|हरी प्याज|Vegetables|Scallion|ઓક્ટો-નવેમ્બર|3-4 kg/એકર|7-10 દિવસ|45-60 દિવસ|પાણી નિયમિત|1|નાનો કાળો|🧅
Shallot|નાની ડુંગળી|छोटा प्याज|Vegetables|Shallot|ઓક્ટો-નવેમ્બર|3-4 kg/એકર|7-10 દિવસ|60-75 દિવસ|પાણી નિયમિત|1|નાનો ગુલાબી|🧅
Ivy Gourd|ટીંડોળા|तोंडली|Vegetables|Coccinia grandis|જૂન-જુલાઈ|કટિંગ|10-15 દિવસ|60-70 દિવસ|પાણી નિયમિત|5|નાનો લીલો|🥒
Snake Gourd|પડવળ|चिचिंडा|Vegetables|Trichosanthes cucumerina|જૂન-જુલાઈ|1-2 kg/એકર|7-10 દિવસ|70-80 દિવસ|પાણી નિયમિત|1|ચપટો ભૂરો|🥒
Ash Gourd|પેઠા કોળું|पेठा|Vegetables|Benincasa hispida|ફેબ્રુ-માર્ચ|1-2 kg/એકર|5-7 દિવસ|90-110 દિવસ|પાણી નિયમિત|1|ચપટો સફેદ|🎃
Round Gourd|ટિંડા|टिंडा|Vegetables|Praecitrullus fistulosus|ફેબ્રુ-માર્ચ|2-3 kg/એકર|5-7 દિવસ|60-70 દિવસ|પાણી નિયમિત|1|ચપટો ભૂરો|🥒
Elephant Foot Yam|સૂરણ|सूरन|Vegetables|Amorphophallus paeoniifolius|માર્ચ-એપ્રિ|કંદ|20-30 દિવસ|7-8 મહિના|પાણી નિયમિત|7|મોટો ભૂરો|🥔
Lima Bean|વાલ|सेम (वाल)|Vegetables|Lima bean|ઓક્ટો-નવેમ્બર|8-10 kg/એકર|5-7 દિવસ|90-110 દિવસ|2-3 વાર પાણી|1|ચપટો સફેદ|🫘
Hyacinth Bean|વાલોળ|सेम की फली|Vegetables|Lablab purpureus|જૂન-જુલાઈ|8-10 kg/એકર|5-7 દિવસ|90-100 દિવસ|2-3 વાર પાણી|1|ચપટો કાળો|🫘
French Bean|ફણસી|फ्रेंच बीन|Vegetables|Green bean|ઓક્ટો-નવેમ્બર|30-35 kg/એકર|5-7 દિવસ|50-60 દિવસ|2-3 વાર પાણી|1|લાંબો ભૂરો|🫘
Winged Bean|પાંખિયા વાલ|पंखिया सेम|Vegetables|Psophocarpus tetragonolobus|જૂન-જુલાઈ|8-10 kg/એકર|7-10 દિવસ|90-110 દિવસ|પાણી નિયમિત|1|ગોળ ભૂરો|🫘
Red Okra|લાલ ભીંડા|लाल भिंडी|Vegetables|Okra|ફેબ્રુ-માર્ચ|4-5 kg/એકર|5-7 દિવસ|50-60 દિવસ|પાણી નિયમિત|1|ગોળ કાળો|🌶️
Cherry Tomato|ચેરી ટમેટા|चेरी टमाटर|Vegetables|Cherry tomato|સપ્ટે-ઓક્ટો|100-150 g/એકર|5-7 દિવસ|70-80 દિવસ|ડ્રિપ ઈરિગેશન|8|ચપટો પીળો|🍅
Red Capsicum|લાલ સિમલા મરચાં|लाल शिमला मिर्च|Vegetables|Bell pepper|સપ્ટે-ઓક્ટો|100-150 g/એકર|7-10 દિવસ|90-100 દિવસ|ડ્રિપ ઈરિગેશન|8|ચપટો પીળો|🫑
Button Mushroom|મશરૂમ|मशरूम|Vegetables|Agaricus bisporus|ઓક્ટો-ફેબ્રુ|ઠંડું|15-20 દિવસ|30-40 દિવસ|ભેજ|4|નાનો સફેદ|🍄
Kale|કેલ|केल|Vegetables|Kale|ઓક્ટો-નવેમ્બર|250-300 g/એકર|5-7 દિવસ|55-65 દિવસ|પાણી નિયમિત|8|નાનો કાળો|🥬
Pak Choi|પાક ચોઈ|पाक चोई|Vegetables|Bok choy|ઓક્ટો-નવેમ્બર|250-300 g/એકર|3-5 દિવસ|40-50 દિવસ|પાણી નિયમિત|1|નાનો કાળો|🥬
Swiss Chard|સ્વિસ ચાર્ડ|स्विस चार्ड|Vegetables|Chard|ઓક્ટો-નવેમ્બર|3-4 kg/એકર|5-7 દિવસ|45-55 દિવસ|પાણી નિયમિત|1|ગોળ ભૂરો|🥬
Mustard Greens|સરસવની ભાજી|सरसों का साग|Vegetables|Mustard greens|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|3-5 દિવસ|30-40 દિવસ|પાણી નિયમિત|1|નાનો કાળો|🥬
Dill|સુવા|सोया (सुवा)|Vegetables|Dill|ઓક્ટો-નવેમ્બર|3-4 kg/એકર|7-10 દિવસ|30-40 દિવસ|પાણી નિયમિત|1|ચપટો ભૂરો|🌿
Parsley|પાર્સલી|अजमोदा|Vegetables|Parsley|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|10-15 દિવસ|60-70 દિવસ|પાણી નિયમિત|1|નાનો કાળો|🌿
Water Spinach|કલમી શાક|करमुआ साग|Vegetables|Ipomoea aquatica|જૂન-જુલાઈ|કટિંગ|5-7 દિવસ|30-40 દિવસ|પાણી ભરેલું|5|નાનો ભૂરો|🥬
Red Amaranth|લાલ તાંદળજો|लाल चौलाई|Vegetables|Amaranth|જૂન-જુલાઈ|1-2 kg/એકર|3-5 દિવસ|25-30 દિવસ|પાણી નિયમિત|1|નાનો લાલ|🥬
Cassava|કસાવા|कसावा|Vegetables|Cassava|માર્ચ-એપ્રિ|કટિંગ|10-15 દિવસ|8-10 મહિના|ઓછું પાણી|5|લાંબો ભૂરો|🥔
Garden Cress|અળીવ|हलीम (असालिया)|Vegetables|Garden cress|ઓક્ટો-નવેમ્બર|3-4 kg/એકર|3-5 દિવસ|90-100 દિવસ|ઓછું પાણી|1|નાનો લાલ|🌿
Red Radish|લાલ મૂળો|लाल मूली|Vegetables|Radish|ઓક્ટો-નવેમ્બર|4-5 kg/એકર|3-5 દિવસ|25-30 દિવસ|પાણી નિયમિત|1|ગોળ લાલ|🥕
Sword Bean|તલવાર વાલ|तलवार सेम|Vegetables|Canavalia gladiata|જૂન-જુલાઈ|8-10 kg/એકર|7-10 દિવસ|100-120 દિવસ|ઓછું પાણી|1|મોટો સફેદ|🫘
Yardlong Bean|ચોળા|लोबिया (चौला)|Vegetables|Yardlong bean|ફેબ્રુ-માર્ચ|8-10 kg/એકર|5-7 દિવસ|50-60 દિવસ|2-3 વાર પાણી|1|લાંબો ભૂરો|🫘
Broad Bean|બાકલા|बाकला|Vegetables|Vicia faba|ઓક્ટો-નવેમ્બર|30-40 kg/એકર|7-10 દિવસ|90-110 દિવસ|2-3 વાર પાણી|1|મોટો ભૂરો|🫘
Snow Pea|સ્નો પી|स्नो पी|Vegetables|Snow pea|ઓક્ટો-નવેમ્બર|30-35 kg/એકર|7-10 દિવસ|60-70 દિવસ|2-3 વાર પાણી|1|ગોળ પીળો|🫛
Kesar Mango|કેસર કેરી|केसर आम|Fruits|Mango|ફેબ્રુ-માર્ચ|ગ્રાફ્ટિંગ|20-30 દિવસ|4-5 વર્ષ|ડ્રિપ ઈરિગેશન|9|મોટો ભૂરો|🥭
Alphonso Mango|હાફૂસ કેરી|हापुस आम|Fruits|Mango|ફેબ્રુ-માર્ચ|ગ્રાફ્ટિંગ|20-30 દિવસ|4-5 વર્ષ|ડ્રિપ ઈરિગેશન|9|મોટો ભૂરો|🥭
Date Palm|ખજૂર|खजूर|Fruits|Date palm|ફેબ્રુ-માર્ચ|સકર|30-40 દિવસ|4-5 વર્ષ|ઓછું પાણી|9|લાંબો ભૂરો|🌴
Litchi|લીચી|लीची|Fruits|Lychee|જૂન-જુલાઈ|ગ્રાફ્ટિંગ|20-30 દિવસ|5-6 વર્ષ|પાણી નિયમિત|9|ગોળ લાલ|🍒
Mulberry|શેતૂર|शहतूत|Fruits|Mulberry|ઓક્ટો-ફેબ્રુ|કટિંગ|15-20 દિવસ|1-2 વર્ષ|પાણી નિયમિત|10|નાનો કાળો|🍇
Pomelo|પોમેલો|चकोतरा|Fruits|Pomelo|જૂન-જુલાઈ|ગ્રાફ્ટિંગ|20-30 દિવસ|4-5 વર્ષ|પાણી નિયમિત|9|મોટો પીળો|🍊
Apple|સફરજન|सेब|Fruits|Apple|ઓક્ટો-ફેબ્રુ|ગ્રાફ્ટિંગ|30-40 દિવસ|5-6 વર્ષ|ઠંડું|9|ગોળ ભૂરો|🍎
Apricot|જરદાળુ|खुबानी|Fruits|Apricot|ઓક્ટો-ફેબ્રુ|ગ્રાફ્ટિંગ|30-40 દિવસ|4-5 વર્ષ|ઠંડું|9|ગોળ ભૂરો|🍑
Mandarin|નારંગી|मंदारिन संतरा|Fruits|Mandarin orange|જૂન-જુલાઈ|ગ્રાફ્ટિંગ|20-30 દિવસ|4-5 વર્ષ|પાણી નિયમિત|9|ગોળ પીળો|🍊
Tamarind|આંબલી|इमली|Fruits|Tamarind|જૂન-જુલાઈ|2-3 kg/એકર|7-10 દિવસ|6-8 વર્ષ|ઓછું પાણી|3|ચપટો ભૂરો|🌳
Phalsa|ફાલસા|फालसा|Fruits|Grewia asiatica|ફેબ્રુ-માર્ચ|કટિંગ|10-15 દિવસ|1-2 વર્ષ|ઓછું પાણી|10|નાનો કાળો|🍇
Karonda|કરમદા|करौंदा|Fruits|Carissa carandas|જૂન-જુલાઈ|કટિંગ|15-20 દિવસ|2-3 વર્ષ|ઓછું પાણી|10|નાનો લાલ|🍒
Passion Fruit|પેશન ફ્રૂટ|पैशन फ्रूट|Fruits|Passion fruit|ફેબ્રુ-માર્ચ|કટિંગ|15-20 દિવસ|1-2 વર્ષ|પાણી નિયમિત|10|ગોળ ભૂરો|🍈
Wood Apple|કોઠું|कैथा|Fruits|Wood apple|જૂન-જુલાઈ|2-3 kg/એકર|15-20 દિવસ|6-8 વર્ષ|ઓછું પાણી|3|ગોળ ભૂરો|🌳
Bael|બીલી|बेल|Fruits|Aegle marmelos|જૂન-જુલાઈ|2-3 kg/એકર|15-20 દિવસ|6-8 વર્ષ|ઓછું પાણી|3|ગોળ પીળો|🌿 ઔષધીય વૃક્ષ
Star Fruit|કમરખ|कमरख|Fruits|Carambola|જૂન-જુલાઈ|ગ્રાફ્ટિંગ|20-30 દિવસ|3-4 વર્ષ|પાણી નિયમિત|9|લાંબો પીળો|⭐
Persimmon|જાપાની ફળ|जापानी फल|Fruits|Persimmon|ઓક્ટો-ફેબ્રુ|ગ્રાફ્ટિંગ|30-40 દિવસ|4-5 વર્ષ|ઠંડું|9|ગોળ લાલ|🍅
Banana G9|કેળા જી-9|केला जी-9|Fruits|Banana|જૂન-જુલાઈ|સકર|15-20 દિવસ|11-12 મહિના|ડ્રિપ ઈરિગેશન|9|લાંબો પીળો|🍌
Bhagwa Pomegranate|ભગવા દાડમ|भगवा अनार|Fruits|Pomegranate|જૂન-જુલાઈ|કટિંગ|15-20 દિવસ|2-3 વર્ષ|ડ્રિપ ઈરિગેશન|10|ગોળ લાલ|🍎
Allahabad Guava|અલ્હાબાદી જામફળ|इलाहाबादी अमरूद|Fruits|Guava|જૂન-જુલાઈ|ગ્રાફ્ટિંગ|15-20 દિવસ|2-3 વર્ષ|પાણી નિયમિત|9|ગોળ પીળો|🍈
Bt Cotton|બીટી કપાસ|बीटी कपास|Cash Crops|Cotton|જૂન-જુલાઈ|1-2 kg/એકર|5-7 દિવસ|150-180 દિવસ|3-4 વાર પાણી|1|ગોળ સફેદ|☁️ સફેદ સોનું
Desi Cotton|દેશી કપાસ|देसी कपास|Cash Crops|Cotton|જૂન-જુલાઈ|3-4 kg/એકર|5-7 દિવસ|140-160 દિવસ|ઓછું પાણી|1|ગોળ સફેદ|☁️ સફેદ સોનું
Sugar Beet|સુગર બીટ|चुकंदर (चीनी)|Cash Crops|Sugar beet|ઓક્ટો-નવેમ્બર|3-4 kg/એકર|7-10 દિવસ|150-180 દિવસ|3-4 વાર પાણી|1|ગોળ ભૂરો|🍬 ખાંડ
Coffee|કોફી|कॉफ़ी|Cash Crops|Coffee|જૂન-જુલાઈ|1-2 kg/એકર|30-40 દિવસ|3-4 વર્ષ|ઠંડું|2|ગોળ લાલ|☕
Tea|ચા|चाय|Cash Crops|Tea|જૂન-જુલાઈ|કટિંગ|30-40 દિવસ|3-4 વર્ષ|પાણી નિયમિત|10|નાનો ભૂરો|🍵
Rubber|રબર|रबर|Cash Crops|Rubber tree|જૂન-જુલાઈ|ગ્રાફ્ટિંગ|20-30 દિવસ|6-7 વર્ષ|પાણી નિયમિત|9|મોટો ભૂરો|🌳
Cashew|કાજુ|काजू|Cash Crops|Cashew|જૂન-જુલાઈ|ગ્રાફ્ટિંગ|15-20 દિવસ|3-4 વર્ષ|ઓછું પાણી|9|ચપટો ભૂરો|🥜
Arecanut|સોપારી|सुपारी|Cash Crops|Areca nut|જૂન-જુલાઈ|1-2 kg/એકર|30-40 દિવસ|6-8 વર્ષ|પાણી નિયમિત|3|ગોળ ભૂરો|🌴
Oil Palm|ઓઈલ પામ|ऑयल पाम|Cash Crops|Oil palm|જૂન-જુલાઈ|1-2 kg/એકર|30-40 દિવસ|3-4 વર્ષ|પાણી નિયમિત|2|ગોળ ભૂરો|🥜 તેલ
Jatropha|રતનજ્યોત|रतनजोत|Cash Crops|Jatropha curcas|જૂન-જુલાઈ|કટિંગ|10-15 દિવસ|2-3 વર્ષ|ઓછું પાણી|10|ચપટો કાળો|🥜 તેલ
Sunn Hemp|શણ|सनई|Cash Crops|Crotalaria juncea|જૂન-જુલાઈ|10-12 kg/એકર|3-5 દિવસ|45-60 દિવસ|ઓછું પાણી|1|ચપટો ભૂરો|🌿
Dhaincha|ઢેંચા|ढैंचा|Cash Crops|Sesbania bispinosa|જૂન-જુલાઈ|10-12 kg/એકર|3-5 દિવસ|45-60 દિવસ|ઓછું પાણી|1|નાનો ભૂરો|🌿
Mesta|અંબાડી|मेस्ता|Cash Crops|Hibiscus sabdariffa|જૂન-જુલાઈ|5-6 kg/એકર|5-7 દિવસ|120-140 દિવસ|3-4 વાર પાણી|1|નાનો ભૂરો|🌿
Vanilla|વેનીલા|वेनिला|Cash Crops|Vanilla|જૂન-જુલાઈ|કટિંગ|20-30 દિવસ|3-4 વર્ષ|ઠંડું|10|લાંબો કાળો|🌸 સુગંધી
Cocoa|કોકો|कोको|Cash Crops|Cocoa bean|જૂન-જુલાઈ|1-2 kg/એકર|15-20 દિવસ|3-4 વર્ષ|ઠંડું|2|ચપટો ભૂરો|🍫
Betel Leaf|નાગરવેલ પાન|पान|Cash Crops|Piper betle|ફેબ્રુ-માર્ચ|કટિંગ|15-20 દિવસ|3-4 મહિના|પાણી નિયમિત|5|નાનો લીલો|🌿
Chicory|કાસની|कासनी|Cash Crops|Chicory|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|7-10 દિવસ|90-100 દિવસ|2-3 વાર પાણી|1|નાનો ભૂરો|🌿
Summer Groundnut|ઉનાળુ મગફળી|गर्मी की मूंगफली|Cash Crops|Peanut|ફેબ્રુ-માર્ચ|40-50 kg/એકર|5-7 દિવસ|100-110 દિવસ|4-5 વાર પાણી|7|ગોળ ગુલાબી|🥜
Summer Moong|ઉનાળુ મગ|गर्मी की मूंग|Cash Crops|Mung bean|ફેબ્રુ-માર્ચ|8-10 kg/એકર|3-5 દિવસ|60-65 દિવસ|2-3 વાર પાણી|7|ગોળ લીલો|🫘 પ્રોટીન
Sweet Basil|બાસિલ|बेसिल|Herbs|Basil|ફેબ્રુ-માર્ચ|250-300 g/એકર|5-7 દિવસ|45-60 દિવસ|પાણી નિયમિત|1|નાનો કાળો|🌿 સુગંધી
Oregano|ઓરેગાનો|ओरिगैनो|Herbs|Oregano|ઓક્ટો-નવેમ્બર|કટિંગ|10-15 દિવસ|60-80 દિવસ|ઓછું પાણી|10|નાનો ભૂરો|🌿 મસાલો
Thyme|થાઇમ|थाइम|Herbs|Thyme|ઓક્ટો-નવેમ્બર|કટિંગ|10-15 દિવસ|60-80 દિવસ|ઓછું પાણી|10|નાનો ભૂરો|🌿 મસાલો
Rosemary|રોઝમેરી|रोज़मेरी|Herbs|Rosemary|ઓક્ટો-નવેમ્બર|કટિંગ|15-20 દિવસ|90-120 દિવસ|ઓછું પાણી|10|નાનો ભૂરો|🌿 સુગંધી
Chamomile|કેમોમાઈલ|कैमोमाइल|Herbs|Chamomile|ઓક્ટો-નવેમ્બર|250-300 g/એકર|7-10 દિવસ|90-100 દિવસ|પાણી નિયમિત|1|નાનો ભૂરો|🌼 આરોગ્ય
Safed Musli|સફેદ મુસળી|सफेद मूसली|Herbs|Chlorophytum borivilianum|જૂન-જુલાઈ|કંદ|15-20 દિવસ|90-120 દિવસ|પાણી નિયમિત|7|લાંબો સફેદ|🌿 ઔષધીય વૃક્ષ
Sarpagandha|સર્પગંધા|सर्पगंधा|Herbs|Rauvolfia serpentina|જૂન-જુલાઈ|કટિંગ|20-30 દિવસ|18-24 મહિના|પાણી નિયમિત|10|નાનો કાળો|🌿 ઔષધીય વૃક્ષ
Citronella|સિટ્રોનેલા|सिट्रोनेला|Herbs|Cymbopogon nardus|જૂન-જુલાઈ|કટિંગ|10-15 દિવસ|90-120 દિવસ|પાણી નિયમિત|10|નાનો લીલો|🌿 સુગંધી
Palmarosa|પામારોઝા|पामारोज़ा|Herbs|Cymbopogon martinii|જૂન-જુલાઈ|કટિંગ|10-15 દિવસ|90-120 દિવસ|ઓછું પાણી|10|નાનો લીલો|🌿 સુગંધી
Vetiver|વેટીવર|खस (वेटिवर)|Herbs|Vetiver|જૂન-જુલાઈ|કટિંગ|10-15 દિવસ|12-18 મહિના|ઓછું પાણી|10|લાંબો પાતળો|🌿 સુગંધી
Patchouli|પચૌલી|पचौली|Herbs|Patchouli|જૂન-જુલાઈ|કટિંગ|15-20 દિવસ|4-6 મહિના|પાણી નિયમિત|10|નાનો લીલો|🌿 સુગંધી
Clove|લવિંગ|लौंग|Herbs|Clove|જૂન-જુલાઈ|1-2 kg/એકર|30-40 દિવસ|6-8 વર્ષ|પાણી નિયમિત|2|નાનો ભૂરો|🌿 મસાલો
Nutmeg|જાયફળ|जायफल|Herbs|Nutmeg|જૂન-જુલાઈ|1-2 kg/એકર|30-40 દિવસ|6-8 વર્ષ|પાણી નિયમિત|2|ગોળ ભૂરો|🌿 મસાલો
Bay Leaf|તમાલપત્ર|तेज पत्ता|Herbs|Bay leaf|જૂન-જુલાઈ|કટિંગ|20-30 દિવસ|3-4 વર્ષ|પાણી નિયમિત|10|લાંબો લીલો|🌿 મસાલો
Poppy|ખસખસ|खसखस|Herbs|Opium poppy|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|7-10 દિવસ|100-120 દિવસ|2-3 વાર પાણી|1|નાનો સફેદ|🌿 મસાલો
Nasturtium|નાસ્તુર્ટિયમ|नैस्टर्शियम|Flowers|Nasturtium|ઓક્ટો-ફેબ્રુ|3-4 kg/એકર|7-10 દિવસ|50-60 દિવસ|પાણી નિયમિત|1|ગોળ ભૂરો|🌸 શોભાવાળું
Phlox|ફ્લોક્સ|फ्लॉक्स|Flowers|Phlox|ઓક્ટો-ફેબ્રુ|1-2 kg/એકર|7-10 દિવસ|60-80 દિવસ|પાણી નિયમિત|2|નાનો કાળો|🌸 શોભાવાળું
Verbena|વર્બેના|वर्बेना|Flowers|Verbena|ઓક્ટો-ફેબ્રુ|1-2 kg/એકર|10-15 દિવસ|70-90 દિવસ|પાણી નિયમિત|2|નાનો કાળો|🌸 શોભાવાળું
Larkspur|લાર્કસ્પર|लार्कस्पर|Flowers|Larkspur|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|10-15 દિવસ|80-100 દિવસ|ઠંડું|1|નાનો કાળો|🌸 શોભાવાળું
Impatiens|ઈમ્પેશન્સ|इम्पेशन्स|Flowers|Impatiens walleriana|જૂન-જુલાઈ|1-2 kg/એકર|7-10 દિવસ|50-60 દિવસ|પાણી નિયમિત|2|નાનો કાળો|🌸 શોભાવાળું
Bird of Paradise|બર્ડ ઓફ પેરેડાઈઝ|बर्ड ऑफ पैराडाइज़|Flowers|Strelitzia|જૂન-જુલાઈ|કંદ|30-40 દિવસ|2-3 વર્ષ|પાણી નિયમિત|7|મોટો ભૂરો|🌸 શોભાવાળું
Heliconia|હેલિકોનિયા|हेलिकोनिया|Flowers|Heliconia|જૂન-જુલાઈ|કંદ|30-40 દિવસ|12-18 મહિના|પાણી નિયમિત|7|મોટો લાલ|🌸 શોભાવાળું
Hydrangea|હાઈડ્રેંજા|हाइड्रेंजा|Flowers|Hydrangea|ઓક્ટો-ફેબ્રુ|કટિંગ|15-20 દિવસ|1-2 વર્ષ|ઠંડું|10|નાનો ગુલાબી|🌸 શોભાવાળું
Freesia|ફ્રીસિયા|फ्रीसिया|Flowers|Freesia|ઓક્ટો-નવેમ્બર|બલ્બ|15-20 દિવસ|90-110 દિવસ|પાણી નિયમિત|7|નાનો પીળો|🌸 સુગંધી
Lisianthus|લિસિયન્થસ|लिसिएन्थस|Flowers|Eustoma grandiflorum|ઓક્ટો-નવેમ્બર|1-2 kg/એકર|10-15 દિવસ|120-150 દિવસ|ઠંડું|2|નાનો કાળો|🌸 શોભાવાળું
Rosewood|શીશમ|शीशम|Trees|Dalbergia sissoo|જૂન-જુલાઈ|2-3 kg/એકર|7-10 દિવસ|15-20 વર્ષ|ઓછું પાણી|3|ચપટો ભૂરો|🌳 મોંઘું લાકડું
Casuarina|સુરુ|सुरू|Trees|Casuarina|જૂન-જુલાઈ|1-2 kg/એકર|7-10 દિવસ|4-5 વર્ષ|ઓછું પાણી|2|નાનો ભૂરો|🌳 ઝડપી
Karanj|કરંજ|करंज|Trees|Pongamia pinnata|જૂન-જુલાઈ|2-3 kg/એકર|15-20 દિવસ|5-6 વર્ષ|ઓછું પાણી|3|ચપટો ભૂરો|🌳 છાયાદાર
Subabul|સુબાવળ|सुबबूल|Trees|Leucaena leucocephala|જૂન-જુલાઈ|2-3 kg/એકર|7-10 દિવસ|2-3 વર્ષ|ઓછું પાણી|3|ચપટો ભૂરો|🌳 ઝડપી
Semal|શિમળો|सेमल|Trees|Bombax ceiba|જૂન-જુલાઈ|1-2 kg/એકર|10-15 દિવસ|8-10 વર્ષ|ઓછું પાણી|3|નાનો ભૂરો|🌳 છાયાદાર
Indian Almond|દરિયાઈ બદામ|जंगली बादाम|Trees|Terminalia catappa|જૂન-જુલાઈ|2-3 kg/એકર|20-30 દિવસ|5-6 વર્ષ|ઓછું પાણી|3|મોટો ભૂરો|🌳 છાયાદાર
Toon|તુન|तून|Trees|Toona ciliata|જૂન-જુલાઈ|1-2 kg/એકર|10-15 દિવસ|10-15 વર્ષ|પાણી નિયમિત|2|નાનો ભૂરો|🌳 મોંઘું લાકડું
Palash|ખાખરો|पलाश|Trees|Butea monosperma|જૂન-જુલાઈ|2-3 kg/એકર|7-10 દિવસ|8-10 વર્ષ|ઓછું પાણી|3|ચપટો ભૂરો|🌳 શોભાવાળું
Amaltas|ગરમાળો|अमलतास|Trees|Cassia fistula|જૂન-જુલાઈ|2-3 kg/એકર|10-15 દિવસ|5-6 વર્ષ|ઓછું પાણી|3|ચપટો ભૂરો|🌳 શોભાવાળું
Bakul|બોરસલ્લી|मौलसिरी|Trees|Mimusops elengi|જૂન-જુલાઈ|2-3 kg/એકર|20-30 દિવસ|6-8 વર્ષ|પાણી નિયમિત|3|ગોળ ભૂરો|🌳 સુગંધી
"""
for _ln in _EX_ROWS2.strip().splitlines():
    _n, _g, _h, _cat, _wk, _se, _ra, _ge, _ha, _ca, _mi, _lk, _sp = _ln.split("|")
    _adj = _lk.split()
    SEED_DB[_n] = {"pic": "plant", "seed_guj": _g + " બીજ", "seed_hin": _h + " बीज",
                   "look_guj": _lk + " દાણો", "look_hin": " ".join(_EX_L[a] for a in _adj) + " दाना",
                   "rate": _ra, "germ": _ge, "method_guj": _EX_M[int(_mi)][0], "method_hin": _EX_M[int(_mi)][1],
                   "season_guj": _se, "care_guj": _ca, "harvest": _ha, "special": _sp, "_h": _h}
    GUJ_NAMES[_n] = _g
    EXTRA_CAT[_n] = _cat
    EXTRA_WIKI[_n] = _wk

# ════════════════════════════════════════════════════════════════════
# ➕ MORE MEDICINES / FERTILIZERS / BIO-PRODUCTS (40)
# ════════════════════════════════════════════════════════════════════
def _med(guj, typ, p100, p1l, dose, target, safety, wait):
    return {"guj": guj, "type": typ, "price_100": p100, "price_1L": p1l, "dosage": dose, "target": target, "safety": safety, "wait": wait}

_S_OK, _S_MASK, _S_GL, _S_TOX = "🟢 સુરક્ષિત", "🟡 માસ્ક", "🟠 ગ્લોવ્સ", "🔴 ઝેરી"
MED_DB.update({
    "Spinosad 45% SC": _med("સ્પિનોસેડ", "કીટકનાશક", 420, 3800, "0.3ml/L", "ઈયળ, થ્રિપ્સ", _S_MASK, 3),
    "Chlorantraniliprole 18.5% SC": _med("ક્લોરેન્ટ્રાનિલિપ્રોલ", "કીટકનાશક", 480, 4400, "0.3ml/L", "ઈયળ, બોરર", _S_OK, 3),
    "Flubendiamide 39.35% SC": _med("ફ્લુબેન્ડિયામાઇડ", "કીટકનાશક", 450, 4100, "0.3ml/L", "ઈયળ, બોરર", _S_MASK, 5),
    "Cypermethrin 10% EC": _med("સાયપરમેથ્રિન", "કીટકનાશક", 90, 750, "1ml/L", "ઈયળ", _S_GL, 7),
    "Deltamethrin 2.8% EC": _med("ડેલ્ટામેથ્રિન", "કીટકનાશક", 110, 900, "1ml/L", "ઈયળ, બોરર", _S_GL, 7),
    "Buprofezin 25% SC": _med("બુપ્રોફેઝિન", "કીટકનાશક", 260, 2300, "1.5ml/L", "જેસિડ, સફેદ માખી", _S_MASK, 7),
    "Diafenthiuron 50% WP": _med("ડાયફેન્થિયુરોન", "કીટકનાશક", 300, 2700, "1g/L", "માઈટ્સ, સફેદ માખી", _S_MASK, 7),
    "Spiromesifen 22.9% SC": _med("સ્પાઇરોમેસિફેન", "કીટકનાશક", 380, 3400, "1ml/L", "માઈટ્સ, સફેદ માખી", _S_MASK, 7),
    "Fenpropathrin 30% EC": _med("ફેનપ્રોપેથ્રિન", "કીટકનાશક", 240, 2100, "1ml/L", "માઈટ્સ, થ્રિપ્સ", _S_GL, 7),
    "Indoxacarb 14.5% SC": _med("ઇન્ડોક્સાકાર્બ", "કીટકનાશક", 280, 2500, "1ml/L", "ઈયળ", _S_MASK, 5),
    "Thiacloprid 21.7% SC": _med("થાયાક્લોપ્રિડ", "કીટકનાશક", 350, 3200, "0.5ml/L", "એફિડ, જેસિડ", _S_MASK, 7),
    "Pymetrozine 50% WG": _med("પાયમેટ્રોઝિન", "કીટકનાશક", 320, 2900, "0.6g/L", "જેસિડ, એફિડ", _S_OK, 7),
    "Hexaconazole 5% EC": _med("હેક્ઝાકોનાઝોલ", "ફૂગનાશક", 150, 1300, "1ml/L", "પાવડરી, રસ્ટ", _S_MASK, 7),
    "Propiconazole 25% EC": _med("પ્રોપિકોનાઝોલ", "ફૂગનાશક", 180, 1600, "1ml/L", "રસ્ટ, લીફ સ્પોટ", _S_MASK, 10),
    "Tebuconazole 25.9% EC": _med("ટેબ્યુકોનાઝોલ", "ફૂગનાશક", 200, 1750, "1ml/L", "રસ્ટ, લીફ સ્પોટ", _S_MASK, 10),
    "Azoxystrobin 23% SC": _med("એઝોક્સીસ્ટ્રોબિન", "ફૂગનાશક", 320, 2900, "1ml/L", "બ્લાઈટ, પાવડરી", _S_OK, 7),
    "Copper Hydroxide 77% WP": _med("કોપર હાઇડ્રોક્સાઇડ", "ફૂગનાશક", 130, 1100, "2g/L", "બેક્ટેરિયલ, બ્લાઈટ", _S_GL, 7),
    "Thiophanate Methyl 70% WP": _med("થાયોફેનેટ મિથાઈલ", "ફૂગનાશક", 140, 1200, "1g/L", "વિલ્ટ, મૂળ સડો", _S_MASK, 7),
    "Trifloxystrobin + Tebuconazole 75% WG": _med("ટ્રાયફ્લોક્સીસ્ટ્રોબિન + ટેબ્યુકોનાઝોલ", "કોમ્બો", 360, 3300, "0.5g/L", "રસ્ટ, બ્લાઈટ", _S_MASK, 14),
    "Wettable Sulphur 80% WP": _med("વેટેબલ સલ્ફર", "ફૂગનાશક", 60, 450, "2.5g/L", "પાવડરી, માઈટ્સ", _S_MASK, 5),
    "Fosetyl-Al 80% WP": _med("ફોસેટાઇલ એલ્યુમિનિયમ", "ફૂગનાશક", 220, 1900, "2g/L", "ડાઉની માઈલ્ડ્યુ", _S_OK, 7),
    "Pendimethalin 30% EC": _med("પેન્ડીમેથાલિન", "નીંદણનાશક", 140, 1100, "3ml/L", "નીંદણ", _S_GL, 0),
    "Quizalofop-ethyl 5% EC": _med("ક્વિઝાલોફોપ ઈથાઈલ", "નીંદણનાશક", 150, 1250, "2ml/L", "ઘાસ", _S_MASK, 30),
    "Metsulfuron Methyl 20% WP": _med("મેટસલ્ફ્યુરોન મિથાઈલ", "નીંદણનાશક", 90, 800, "0.02g/L", "પહોળા પાન", _S_OK, 30),
    "Imazethapyr 10% SL": _med("ઈમાઝેથાપાયર", "નીંદણનાશક", 160, 1400, "1ml/L", "નીંદણ", _S_MASK, 30),
    "Potassium Nitrate 13-0-45": _med("પોટેશિયમ નાઈટ્રેટ", "ખાતર", 90, 700, "5g/L", "પોટેશિયમ", _S_OK, 0),
    "Mono Ammonium Phosphate 12-61-0": _med("મોનો એમોનિયમ ફોસ્ફેટ", "ખાતર", 100, 800, "5g/L", "ફોસ્ફરસ", _S_OK, 0),
    "Calcium Nitrate": _med("કેલ્શિયમ નાઈટ્રેટ", "ખાતર", 80, 600, "3g/L", "કેલ્શિયમ", _S_OK, 0),
    "Humic Acid 12%": _med("હ્યુમિક એસિડ", "વૃદ્ધિ નિયામક", 120, 950, "2ml/L", "મૂળ, વૃદ્ધિ", _S_OK, 0),
    "Seaweed Extract": _med("સીવીડ એક્સટ્રેક્ટ", "જૈવિક ટોનિક", 150, 1200, "2ml/L", "તણાવ, વૃદ્ધિ", _S_OK, 0),
    "Gibberellic Acid 0.001%": _med("જિબ્રેલિક એસિડ", "વૃદ્ધિ નિયામક", 110, 900, "1ml/L", "વૃદ્ધિ", _S_OK, 0),
    "Trichoderma viride": _med("ટ્રાઇકોડર્મા", "જૈવિક ફૂગનાશક", 80, 600, "5g/L", "મૂળ સડો, વિલ્ટ", _S_OK, 0),
    "Pseudomonas fluorescens": _med("સ્યુડોમોનાસ", "જૈવિક ફૂગનાશક", 80, 600, "5g/L", "વિલ્ટ, બ્લાઈટ", _S_OK, 0),
    "Beauveria bassiana": _med("બ્યુવેરિયા", "જૈવિક", 90, 700, "5g/L", "થ્રિપ્સ, એફિડ", _S_OK, 0),
    "Rhizobium Culture": _med("રાઈઝોબિયમ", "જૈવિક ખાતર", 40, 300, "5g/L", "નાઈટ્રોજન", _S_OK, 0),
    "Azotobacter": _med("એઝોટોબેક્ટર", "જૈવિક ખાતર", 40, 300, "5g/L", "નાઈટ્રોજન", _S_OK, 0),
    "PSB (Phosphate Solubilizing Bacteria)": _med("પી.એસ.બી.", "જૈવિક ખાતર", 40, 300, "5g/L", "ફોસ્ફરસ", _S_OK, 0),
    "Gypsum": _med("જિપ્સમ", "માટી સુધારક", 20, 150, "200kg/એકર", "કેલ્શિયમ, જમીન", _S_OK, 0),
    "Vermicompost": _med("વર્મી કમ્પોસ્ટ", "જૈવિક ખાતર", 30, 220, "1000kg/એકર", "સર્વાંગી", _S_OK, 0),
    "Neem Cake": _med("લીમડા ખોળ", "જૈવિક ખાતર", 35, 250, "100kg/એકર", "જીવાત, નાઈટ્રોજન", _S_OK, 0),
})
crop_database = {}
for cn, si in SEED_DB.items():
    crop_database[cn] = {
        "gujarati": GUJ_NAMES.get(cn, cn),
        "english": cn,
        "category": determine_category(cn),
        "season": si["season_guj"],
        "water": "Medium",
        "symptoms": symptoms()
    }

# ════════════════════════════════════════════════════════════════════
# FARMER DATA + HELPERS
# ════════════════════════════════════════════════════════════════════

ORGANIC_RECIPES = {
    "નીમ તેલ સ્પ્રે": {"items": "નીમ તેલ 5 ml + સાબુ 1 ml + પાણી 1 લિટર", "use": "ઈયળ, એફિડ, સફેદ માખી", "cost": "₹20-₹40 / પંપ"},
    "દશપર્ણી અર્ક": {"items": "10 પ્રકારના કડવા પાન 5 kg + ગૌમૂત્ર 5 L + છાણ 2 kg, 30 દિવસ આથો", "use": "બધા પ્રકારની જીવાત", "cost": "₹50-₹80 / 100 L"},
    "છાશ + હિંગ સ્પ્રે": {"items": "5 દિવસ જૂની છાશ 1 L + હિંગ 5 g + પાણી 10 L", "use": "ફૂગ, પાન પીળા", "cost": "₹15-₹30"},
    "લસણ-મરચી અર્ક": {"items": "લસણ 100 g + લીલા મરચા 100 g વાટીને પાણી 1 L, ગાળીને 10 L પાણીમાં", "use": "પાન વળવા, થ્રિપ્સ, માઈટ્સ", "cost": "₹20-₹45"},
    "હળદર + બેકિંગ સોડા": {"items": "હળદર 10 g + સોડા 10 g + પાણી 1 L", "use": "પાવડરી માઈલ્ડ્યુ, ડાઘ", "cost": "₹10-₹25"},
    "જીવામૃત": {"items": "દેશી ગાય છાણ 10 kg + ગૌમૂત્ર 10 L + ગોળ 2 kg + બેસન 2 kg + માટી 1 મુઠ્ઠી + પાણી 200 L, 5-7 દિવસ", "use": "માટી સુધારણા, પોષણ", "cost": "₹80-₹120 / એકર"},
    "રાખ (લાકડાની) ભૂકી": {"items": "લાકડાની રાખ સીધી છાંટવી", "use": "ઈયળ, કીડી, ભેજ નિયંત્રણ", "cost": "₹0-₹10"},
    "ગૌમૂત્ર ડ્રેન્ચ": {"items": "ગૌમૂત્ર 1 L + પાણી 10 L", "use": "કરમાવું, મૂળ રોગ", "cost": "₹25-₹50"},
}


SCHEMES = [
    ("PM-KISAN", "નાના-સીમાંત ખેડૂતોને વાર્ષિક આર્થિક સહાય (હપ્તામાં)"),
    ("પ્રધાનમંત્રી ફસલ બીમા યોજના", "કુદરતી આફતથી પાક નુકસાનનો વીમો"),
    ("સોઈલ હેલ્થ કાર્ડ", "માટી પરીક્ષણ અને ખાતરની સલાહ"),
    ("કિસાન ક્રેડિટ કાર્ડ (KCC)", "ખેતી માટે ઓછા વ્યાજે લોન"),
    ("ઈ-નામ (e-NAM)", "ઓનલાઈન બજારમાં પાક વેચાણ"),
    ("i-ખેડૂત પોર્ટલ (ગુજરાત)", "ગુજરાતની ખેતી યોજનાઓ માટે ઓનલાઈન અરજી"),
]



# ════════════════════════════════════════════════════════════════════
# 🌐 LANGUAGES (ગુજરાતી / हिन्दी / English), STATES, APP ICON  (new)
# ════════════════════════════════════════════════════════════════════
HIN_NAMES = {
    "Neem": "नीम", "Mango": "आम", "Banana": "केला", "Lemon": "नींबू", "Papaya": "पपीता", "Guava": "अमरूद",
    "Pomegranate": "अनार", "Coconut": "नारियल", "Teak": "सागौन", "Drumstick": "सहजन", "Sapota": "चीकू",
    "Custard Apple": "सीताफल", "Jamun Tree": "जामुन का पेड़", "Jackfruit": "कटहल", "Amla Tree": "आंवला का पेड़",
    "Ber Tree": "बेर का पेड़", "Fig Tree": "अंजीर का पेड़", "Moringa": "मोरिंगा", "Gulmohar Tree": "गुलमोहर का पेड़",
    "Kadamba Tree": "कदंब का पेड़", "Silver Oak": "सिल्वर ओक", "Rain Tree": "रेन ट्री", "Paddy": "धान",
    "Wheat": "गेहूं", "Bajra": "बाजरा", "Jowar": "ज्वार", "Maize": "मक्का", "Ragi": "रागी", "Barley": "जौ",
    "Oats": "जई", "Kodo Millet": "कोदो", "Kutki": "कुटकी", "Barnyard Millet": "सांवा", "Little Millet": "छोटा बाजरा",
    "Foxtail Millet": "कंगनी", "Amaranth": "चौलाई", "Quinoa": "क्विनोआ", "Cotton": "कपास", "Groundnut": "मूंगफली",
    "Castor": "अरंडी", "Cumin": "जीरा", "Sesame": "तिल", "Pigeon Pea": "अरहर", "Gram": "चना", "Moong": "मूंग",
    "Urad": "उड़द", "Mustard": "सरसों", "Sunflower": "सूरजमुखी", "Sugarcane": "गन्ना", "Soybean": "सोयाबीन",
    "Tobacco": "तंबाकू", "Jute": "जूट", "Cowpea": "लोबिया", "Horse Gram": "कुलथी", "Lentil": "मसूर",
    "Rajma": "राजमा", "Chickpea": "काबुली चना", "Tomato": "टमाटर", "Potato": "आलू", "Chili": "मिर्च",
    "Brinjal": "बैंगन", "Onion": "प्याज", "Cabbage": "पत्तागोभी", "Cauliflower": "फूलगोभी", "Bottle Gourd": "लौकी",
    "Bitter Gourd": "करेला", "Ladyfinger": "भिंडी", "Cucumber": "खीरा", "Pumpkin": "कद्दू", "Carrot": "गाजर",
    "Radish": "मूली", "Spinach": "पालक", "Fenugreek": "मेथी", "Coriander": "धनिया", "Pea": "मटर", "Beans": "सेम",
    "Cluster Beans": "ग्वार", "Ridge Gourd": "तोरई", "Sponge Gourd": "घिया तोरई", "Pointed Gourd": "परवल",
    "Beetroot": "चुकंदर", "Bell Pepper": "शिमला मिर्च", "Sweet Corn": "स्वीट कॉर्न", "Turnip": "शलजम",
    "Sweet Potato": "शकरकंद", "Colocasia": "अरबी", "Yam": "जिमीकंद", "Broccoli": "ब्रोकली", "Lettuce": "सलाद पत्ता",
    "Celery": "अजमोद", "Asparagus": "शतावरी", "Zucchini": "ज़ुकीनी", "Grape": "अंगूर", "Watermelon": "तरबूज",
    "Muskmelon": "खरबूजा", "Strawberry": "स्ट्रॉबेरी", "Pineapple": "अनानास", "Fig": "अंजीर", "Jamun": "जामुन",
    "Ber": "बेर", "Amla": "आंवला", "Custard Fruit": "सीताफल", "Orange": "संतरा", "Sweet Lime": "मौसंबी",
    "Pear": "नाशपाती", "Peach": "आड़ू", "Plum": "आलूबुखारा", "Cherry": "चेरी", "Kiwi": "कीवी",
    "Dragon Fruit": "ड्रैगन फ्रूट", "Avocado": "एवोकाडो", "Rose": "गुलाब", "Marigold": "गेंदा", "Jasmine": "चमेली",
    "Lotus": "कमल", "Orchid": "ऑर्किड", "Hibiscus": "गुड़हल", "Lily": "लिली", "Dahlia": "डहलिया",
    "Chrysanthemum": "गुलदाउदी", "Bougainvillea": "बोगनवेलिया", "Ixora": "इक्सोरा", "Periwinkle": "सदाबहार",
    "Crossandra": "कनकांबरम", "Aster": "एस्टर", "Carnation": "कार्नेशन", "Petunia": "पेटुनिया", "Gerbera": "जरबेरा",
    "Tuberose": "रजनीगंधा", "Gladiolus": "ग्लैडियोलस", "Zinnia": "ज़िनिया", "Pansy": "पैंसी", "Daisy": "डेज़ी",
    "Tulip": "ट्यूलिप", "Lavender": "लैवेंडर", "Anthurium": "एंथुरियम", "Champa": "चंपा", "Kaner": "कनेर",
    "Rat Ki Rani": "रात की रानी", "Mogra": "मोगरा", "Parijat": "पारिजात", "Saffron": "केसर", "Kewda": "केवड़ा",
    "Gulmohar": "गुलमोहर", "Kadamba": "कदंब", "Aparajita": "अपराजिता", "Tulsi": "तुलसी", "Aloe Vera": "एलोवेरा",
    "Mint": "पुदीना", "Ashwagandha": "अश्वगंधा", "Giloy": "गिलोय", "Brahmi": "ब्राह्मी", "Lemongrass": "लेमनग्रास",
    "Ajwain": "अजवाइन", "Fennel": "सौंफ", "Curry Leaf": "कढ़ी पत्ता", "Stevia": "स्टीविया", "Turmeric": "हल्दी",
    "Ginger": "अदरक", "Garlic": "लहसुन", "Black Pepper": "काली मिर्च", "Cardamom": "इलायची",
    "Shatavari": "शतावरी", "Kalmegh": "कालमेघ", "Vasaka": "अडूसा", "Cinnamon": "दालचीनी",
}

HIN_NAMES.update({k: v["_h"] for k, v in SEED_DB.items() if "_h" in v})

# (key for Google News, ગુજરાતી, हिन्दी, English)
STATES = [
    ("Gujarat", "ગુજરાત", "गुजरात", "Gujarat"), ("Maharashtra", "મહારાષ્ટ્ર", "महाराष्ट्र", "Maharashtra"),
    ("Rajasthan", "રાજસ્થાન", "राजस्थान", "Rajasthan"), ("Madhya Pradesh", "મધ્ય પ્રદેશ", "मध्य प्रदेश", "Madhya Pradesh"),
    ("Uttar Pradesh", "ઉત્તર પ્રદેશ", "उत्तर प्रदेश", "Uttar Pradesh"), ("Punjab", "પંજાબ", "पंजाब", "Punjab"),
    ("Haryana", "હરિયાણા", "हरियाणा", "Haryana"), ("Bihar", "બિહાર", "बिहार", "Bihar"),
    ("Karnataka", "કર્ણાટક", "कर्नाटक", "Karnataka"), ("Tamil Nadu", "તમિલનાડુ", "तमिलनाडु", "Tamil Nadu"),
    ("Andhra Pradesh", "આંધ્ર પ્રદેશ", "आंध्र प्रदेश", "Andhra Pradesh"), ("Telangana", "તેલંગાણા", "तेलंगाना", "Telangana"),
    ("West Bengal", "પશ્ચિમ બંગાળ", "पश्चिम बंगाल", "West Bengal"), ("Odisha", "ઓડિશા", "ओडिशा", "Odisha"),
    ("Kerala", "કેરળ", "केरल", "Kerala"), ("Chhattisgarh", "છત્તીસગઢ", "छत्तीसगढ़", "Chhattisgarh"),
]

I18N_TABLE = r"""
# gu|hi|en   (hi "~" = auto-transliterate Gujarati -> Devanagari)
# ---- header / nav / categories ----
ડિજિટલ પ્લાન્ટ ડૉક્ટર|डिजिटल प्लांट डॉक्टर|Digital Plant Doctor
હોમ|होम|Home
નિદાન|जांच|Test
પાક|फसल|Crops
દવા|दवा|Medicine
સાધનો|औज़ार|Tools
ક્વિઝ|क्विज़|Quiz
વધુ|और|More
બધા|सभी|All
વૃક્ષ|पेड़|Trees
અનાજ|अनाज|Grains
રોકડિયા|नकदी फसलें|Cash crops
શાકભાજી|सब्ज़ियाँ|Vegetables
ફળ|फल|Fruits
ફૂલ|फूल|Flowers
ઔષધિ|औषधि|Herbs
કીટકનાશક|कीटनाशक|Insecticide
ફૂગનાશક|फफूंदनाशक|Fungicide
નીંદણનાશક|खरपतवारनाशक|Herbicide
માટી સુધારક|मिट्टी सुधारक|Soil conditioner
કોમ્બો|कॉम्बो|Combo
જૈવિક|जैविक|Organic
જૈવિક ફૂગનાશક|जैविक फफूंदनाशक|Bio-fungicide
સૂક્ષ્મ પોષક|सूक्ष्म पोषक तत्व|Micronutrient
જૈવિક ખાતર|जैविक खाद|Organic manure
વૃદ્ધિ નિયામક|वृद्धि नियामक|Growth regulator
જૈવિક ટોનિક|जैविक टॉनिक|Bio-tonic
ઓછી|कम|Low
મધ્યમ|मध्यम|Medium
ગંભીર|गंभीर|Severe
નથી|नहीं|None
કાણાં|छेद|Holes
કરડવું|कुतरना|chewing
પાન પીળા|पत्ते पीले|Yellow leaves
ફૂગ ડાઘ|फफूंद के दाग|Fungal spots
પાન વળવા|पत्ते मुड़ना|Leaf curl
કરમાવું|मुरझाना|Wilting
સ્વસ્થ|स्वस्थ|Healthy
# ---- diagnose ----
પાક પસંદ કરો|फसल चुनें|Select crop
પાક રોગ નિદાન|फसल रोग निदान|Crop disease diagnosis
૧|1|1
૨|2|2
લક્ષણ પસંદ કરો|लक्षण चुनें|Select symptom
નિદાન અને ઉપચાર જુઓ|निदान और उपचार देखें|See diagnosis and remedy
કૃપા કરીને પહેલા પાક અને લક્ષણ બંને પસંદ કરો|कृपया पहले फसल और लक्षण दोनों चुनें|Please select both crop and symptom first
રિપોર્ટ|रिपोर्ट|Report
સમસ્યા|समस्या|Problem
તીવ્રતા|गंभीरता|Severity
ઋતુ|मौसम|Season
ઘરેલું ઉપાય|घरेलू उपाय|Home remedy
ખર્ચ|खर्च|Cost
બજારની દવા|बाज़ार की दवा|Market medicine
રાહ|इंतज़ार|Wait
દિવસ|दिन|days
કાર્ટમાં ઉમેરો|कार्ट में जोड़ें|Add to cart
નિવારણ|बचाव|Prevention
ફેવરિટ|पसंदीदा|Favorite
શેર|शेयर|Share
પાક શોધો|फसल खोजें|Search crop
# ---- crops ----
કોઈ પાક મળ્યો નહીં|कोई फसल नहीं मिली|No crop found
બીજ|बीज|Seed
દેખાવ|दिखावट|Appearance
બીજ દર|बीज दर|Seed rate
ઉગવાનો સમય|उगने का समय|Germination time
વાવેતર સમય|बुवाई का समय|Sowing time
લણણી|कटाई|Harvest
સંભાળ|देखभाल|Care
પદ્ધતિ|विधि|Method
આ પાકનું નિદાન કરો|इस फसल की जांच करें|Diagnose this crop
ફેવરિટમાંથી કાઢો|पसंदीदा से हटाएं|Remove from favorites
બંધ|बंद|Close
# ---- medicines / cart ----
દવા દુકાન|दवा दुकान|Medicine shop
કાર્ટ|कार्ट|Cart
જુઓ|देखें|View
ડોઝ|खुराक|Dose
ઉમેરો|जोड़ें|Add
કાર્ટમાં ઉમેર્યું|कार्ट में जोड़ा गया|Added to cart
કાર્ટ ખાલી છે|कार्ट खाली है|Cart is empty
ખરીદી કાર્ટ|खरीदारी कार्ट|Shopping cart
કુલ|कुल|Total
ભાવ મુજબ|दाम के अनुसार|at rate
પ્રિન્ટ|प्रिंट|Print
ખાલી કરો|खाली करें|Clear
# ---- tools ----
ખેતી સાધનો|खेती के औज़ार|Farming tools
ખાતર કેલ્ક્યુલેટર|खाद कैलकुलेटर|Fertilizer calculator
એકર|एकड़|acre
ગણતરી|गणना|Calculate
સ્પ્રે ટાંકી કેલ્ક્યુલેટર|स्प्रे टंकी कैलकुलेटर|Spray tank calculator
પંપ લિટર|पंप लीटर|Pump litres
કેટલા પંપ|कितने पंप|How many pumps
હવામાન રોગ જોખમ|मौसम रोग जोखिम|Weather disease risk
તાપમાન|तापमान|Temperature
ભેજ|नमी|Humidity
દિવસ વરસાદ|दिन बारिश|days rainfall
લાઈવ હવામાન|लाइव मौसम|Live weather
મારું લોકેશન|मेरी लोकेशन|My location
તપાસો|जांचें|Check
લણણી સલામતી|कटाई सुरक्षा|Harvest safety
છંટકાવને કેટલા દિવસ થયા|छिड़काव को कितने दिन हुए|Days since spraying
ચેક કરો|चेक करें|Check
એકમ કન્વર્ટર|इकाई कन्वर्टर|Unit converter
વીઘા|बीघा|Bigha
હેક્ટર|हेक्टेयर|Hectare
ક્વિન્ટલ|क्विंटल|Quintal
કિલો|किलो|Kg
મણ|मन|Maund
કિંમત|मान|Value
બદલો|बदलें|Convert
હવામાન સલાહ|मौसम सलाह|Weather advice
તડકો|धूप|Sunny
વરસાદ|बारिश|Rain
વાદળ|बादल|Cloudy
પવન|हवा|Wind
ગરમી|गर्मी|Heat
ઠંડી|ठंड|Cold
યુરિયા|यूरिया|Urea
લેબલ મુજબ|लेबल के अनुसार|as per label
પંપ|पंप|Pump
મોજા|दस्ताने पहनें|Wear gloves
માસ્ક પહેરો|मास्क|mask
પવનની દિશામાં છાંટો|हवा की दिशा में छिड़कें|Spray downwind
ભેજ ખૂબ વધારે|नमी बहुत अधिक|Very high humidity
ફૂગ|फफूंद|Fungus
બ્લાઈટ|ब्लाइट|Blight
ભેજ મધ્યમ-વધુ|नमी मध्यम-अधिक|Humidity medium-high
ગરમ-ભેજવાળું હવામાન ફૂગ માટે અનુકૂળ|गर्म-नम मौसम फफूंद के लिए अनुकूल|Warm humid weather favors fungus
વધુ વરસાદ|ज़्यादा बारिश|Heavy rain
મૂળ સડો|जड़ सड़न|Root rot
માઈલ્ડ્યુ|मिल्ड्यू|Mildew
પાન ભીના રહે|पत्ते गीले रहते हैं|Leaves stay wet
ગરમ-સૂકું|गर्म-सूखा|Hot-dry
થ્રિપ્સ|थ्रिप्स|Thrips
માઈટ્સ|माइट्स|Mites
ઊંચું|ऊंचा|High
તાત્કાલિક ખેતર તપાસો અને નિવારક છંટકાવ કરો|तुरंत खेत जांचें और बचाव का छिड़काव करें|Inspect the field immediately and spray preventively
દિવસમાં પાન તપાસો|दिनों में पत्ते जांचें|days — check the leaves
નીમ સ્પ્રે કરો|नीम स्प्रे करें|do a neem spray
નીચું|निम्न|Low
સામાન્ય દેખરેખ|सामान्य निगरानी|Normal monitoring
જોખમ|जोखिम|Risk
સ્કોર|स्कोर|Score
સુરક્ષિત|सुरक्षित|Safe
દિવસની રાહ પૂર્ણ|दिन का इंतज़ार पूरा|days waiting period complete
હજી|अभी|Still
દિવસ રાહ જુઓ|दिन इंतज़ार करें|days to wait
વીઘા માપ વિસ્તાર મુજબ બદલાય|बीघा माप क्षेत्र के अनुसार बदलता है|Bigha size varies by region
પાણી સવારે|पानी सुबह|Water in the morning
સાંજે|शाम को|evening
છંટકાવ સાંજે|छिड़काव शाम को|Spray in the evening
ફૂગ રોગ ધ્યાન|फफूंद रोग पर ध्यान दें|Watch for fungal disease
ડ્રેનેજ રાખો|जल निकासी रखें|Keep drainage
પાણી ઓછું|पानी कम|Less water
જીવાત તપાસો|कीट जांचें|Check for pests
છંટકાવ ટાળો|छिड़काव टालें|Avoid spraying
છોડને ટેકો આપો|पौधों को सहारा दें|Support the plants
દિવસે પાણી નહીં|दिन में पानी नहीं|No watering in daytime
સાંજે આપો|शाम को दें|water in the evening
છોડ ઢાંકો|पौधे ढकें|Cover the plants
ઓછું પાણી|कम पानी|Less water
# ---- more / diary / history ----
હજી કોઈ નિદાન નથી|अभी कोई निदान नहीं|No diagnosis yet
કોઈ ફેવરિટ નથી|कोई पसंदीदा नहीं|No favorites
રિપોર્ટ ડાઉનલોડ|रिपोर्ट डाउनलोड|Download report
ઈમરજન્સી હેલ્પલાઈન|इमरजेंसी हेल्पलाइन|Emergency helpline
કિસાન કોલ સેન્ટર|किसान कॉल सेंटर|Kisan Call Center
એમ્બ્યુલન્સ|एम्बुलेंस|Ambulance
પોલીસ|पुलिस|Police
દવાનું ઝેર|दवा का ज़हर|Pesticide poisoning
તરત ડૉક્ટર પાસે જાઓ|तुरंत डॉक्टर के पास जाएं|go to a doctor immediately
દવાનું પેકેટ સાથે લઈ જાઓ|दवा का पैकेट साथ ले जाएं|take the medicine packet along
ખેતર ડાયરી|खेत डायरी|Farm diary
નવી નોંધ લખો|नया नोट लिखें|Write a new note
સાચવો|सहेजें|Save
ફેવરિટ પાક|पसंदीदा फसलें|Favorite crops
નિદાન ઇતિહાસ|निदान इतिहास|Diagnosis history
બધો ઇતિહાસ કાઢી નાખવો|सारा इतिहास हटाना है|Delete all history
ઇતિહાસ સાફ|इतिहास साफ़ करें|Clear history
જૈવિક રેસીપી બુક|जैविक रेसिपी बुक|Organic recipe book
સરકારી યોજનાઓ|सरकारी योजनाएं|Government schemes
નવીનતમ શરતો માટે નજીકની ખેતી કચેરી તપાસો|नवीनतम शर्तों के लिए नज़दीकी कृषि कार्यालय से पूछें|For the latest terms check your nearest agriculture office
ડાયરી|डायरी|Diary
નવો કિસાન|नया किसान|New Farmer
કુશળ કિસાન|कुशल किसान|Skilled Farmer
માસ્ટર કિસાન|मास्टर किसान|Master Farmer
ચેમ્પિયન|चैंपियन|Champion
કિસાન રાજા|किसान राजा|Kisan Raja
શરૂઆત|शुरुआत|Beginner
પોઈન્ટ|पॉइंट|Points
નવો બેજ|नया बैज|New badge
રિપોર્ટ ડાઉનલોડ થયો|रिपोर्ट डाउनलोड हुई|Report downloaded
# ---- months / seasons ----
જાન્યુ|जनवरी|Jan
ફેબ્રુ|फ़रवरी|Feb
માર્ચ|मार्च|Mar
એપ્રિલ|अप्रैल|Apr
એપ્રિ|अप्रैल|Apr
મે|मई|May
જૂન|जून|Jun
જુલાઈ|जुलाई|Jul
ઓગસ્ટ|अगस्त|Aug
સપ્ટેમ્બર|सितंबर|Sep
સપ્ટે|सितंबर|Sep
ઓક્ટોબર|अक्टूबर|Oct
ઓક્ટો|अक्टूबर|Oct
નવેમ્બર|नवंबर|Nov
નવે|नवंबर|Nov
ડિસેમ્બર|दिसंबर|Dec
ડિસે|दिसंबर|Dec
આખું વર્ષ|पूरे साल|All year
વસંત|वसंत|Spring
માં વાવેતર લાયક|में बुवाई योग्य|– suitable to sow
ઉગવું|उगना|Germination
વાવેતર|बुवाई|Sowing
આવક|आमदनी|Income
નફો|मुनाफ़ा|Profit
ખોટ|नुकसान|Loss
પ્રતિ એકર|प्रति एकड़|Per acre
# ---- live weather tool / misc messages ----
લોકેશન સપોર્ટ નથી|लोकेशन सपोर्ट नहीं है|Location not supported
લોકેશન મેળવી રહ્યા છીએ|लोकेशन ली जा रही है|Getting location
લાઈવ હવામાન લોડ થયું|लाइव मौसम लोड हुआ|Live weather loaded
ઈન્ટરનેટ|इंटरनेट|Internet
હવામાન ડેટા મળ્યો નહીં|मौसम डेटा नहीं मिला|Weather data not found
હાથથી લખો|हाथ से लिखें|enter manually
લોકેશન પરવાનગી મળી નથી|लोकेशन की अनुमति नहीं मिली|Location permission not granted
આ મહિને શું વાવવું|इस महीने क्या बोएं|What to sow this month
પાક બતાવો|फसलें दिखाएं|Show crops
બે પાકની સરખામણી|दो फसलों की तुलना|Compare two crops
સરખામણી કરો|तुलना करें|Compare
નફો કેલ્ક્યુલેટર|मुनाफ़ा कैलकुलेटर|Profit calculator
ઉત્પાદન ક્વિન્ટલ|उत्पादन क्विंटल|Yield quintal
ભાવ|भाव|Price
લખાણ અને તારીખ નાખો|नोट और तारीख डालें|Enter the note and date
રિમાઇન્ડર|रिमाइंडर|Reminder
રિમાઇન્ડર બાકી છે|रिमाइंडर बाकी हैं|reminders pending
નું વાવેતર ક્યારે થાય|की बुवाई कब होती है|– when is it sown?
નું બીજ ઉગતા કેટલો સમય લાગે|का बीज उगने में कितना समय लगता है|– how long does the seed take to germinate?
ક્યા વર્ગનો પાક છે|किस वर्ग की फसल है|– which category of crop is it?
ક્યા પ્રકારની દવા છે|किस प्रकार की दवा है|– what type of medicine is it?
સાચો જવાબ|सही जवाब|Correct answer
કિસાન ક્વિઝ|किसान क्विज़|Kisan Quiz
આગળનો પ્રશ્ન|अगला प्रश्न|Next question
બેજ|बैज|Badge
છંટકાવ|छिड़काव|Spraying
પાણી|पानी|Water
ખાતર|खाद|Fertilizer
દા.ત|उदा|e.g
કપાસમાં દવા છાંટવી|कपास में दवा छिड़कना|spray medicine on cotton
મોડું|देर|Late
હવામાન|मौसम|Weather
# ---- NEW: setup form ----
સ્વાગત છે|स्वागत है|Welcome
શરૂ કરતા પહેલા તમારી માહિતી આપો|शुरू करने से पहले अपनी जानकारी दें|Enter your details before you start
ભાષા પસંદ કરો|भाषा चुनें|Choose language
ખેડૂતનું નામ|किसान का नाम|Farmer's name
તમારું પૂરું નામ લખો|अपना पूरा नाम लिखें|Type your full name
ગામનું નામ|गांव का नाम|Village name
તમારા ગામનું નામ લખો|अपने गांव का नाम लिखें|Type your village name
કુલ ખેતર વીઘામાં|कुल खेत (बीघा में)|Total farm in bigha
એપ ખોલો|ऐप खोलें|Open the app
કૃપા કરીને નામ ગામ અને વીઘા સાચી રીતે લખો|कृपया नाम गांव और बीघा सही लिखें|Please enter name village and bigha correctly
# ---- NEW: home ----
નમસ્તે|नमस्ते|Namaste
ગામ|गांव|Village
ખેતર|खेत|Farm
શું તપાસવું છે|क्या जांचना है|What do you want to check
પાક રોગ તપાસ|फसल रोग जांच|Crop disease test
પાકની માહિતી|फसल की जानकारी|Crop info
વધુ માહિતી|और जानकारी|More info
પાકના રોગ અને જીવાતની તપાસ|फसल के रोग और कीट की जांच|Check crop diseases and pests
બીજ વાવેતર અને લણણીની માહિતી|बीज बुवाई और कटाई की जानकारी|Seed sowing and harvest info
દવા અને ખાતરના ભાવ ડોઝ અને કાર્ટ|दवा और खाद के भाव खुराक और कार्ट|Medicine and fertilizer prices dose and cart
ખાતર સ્પ્રે નફો અને રોગ જોખમ ગણતરી|खाद स्प्रे मुनाफ़ा और रोग जोखिम की गणना|Fertilizer spray profit and disease-risk calculators
જ્ઞાન ચકાસો પોઈન્ટ જીતો રિમાઇન્ડર|ज्ञान जांचें पॉइंट जीतें रिमाइंडर|Test knowledge win points set reminders
યોજનાઓ રેસીપી ડાયરી અને ઇતિહાસ|योजनाएं रेसिपी डायरी और इतिहास|Schemes recipes diary and history
આજના ખેડૂત સમાચાર ભારત અને ગુજરાત|आज की किसान खबरें भारत और गुजरात|Today's farmer news India and Gujarat
# ---- NEW: weather ----
તાપમાન અને હવામાન|तापमान और मौसम|Temperature and weather
હવામાન લોડ થઈ રહ્યું છે|मौसम लोड हो रहा है|Loading weather
ટેપ કરીને દરેક દિવસનું તાપમાન જુઓ|टैप करके हर दिन का तापमान देखें|Tap to see each day's temperature
હવામાન લોડ ન થયું ટેપ કરો|मौसम लोड नहीं हुआ टैप करें|Weather not loaded tap to retry
આજ|आज|Today
હવામાન અને તાપમાન|मौसम और तापमान|Weather and temperature
અનુભવાય છે|महसूस होता है|Feels like
આજના કલાકવાર તાપમાન|आज का घंटेवार तापमान|Today's hourly temperature
દરેક દિવસનું તાપમાન|हर दिन का तापमान|Daily temperature
પાછલા દિવસો|पिछले दिन|Past days
આજ અને આગામી દિવસો|आज और आने वाले दिन|Today and coming days
ફરી લોડ કરો|फिर लोड करें|Reload
મારું લોકેશન વાપરો|मेरी लोकेशन इस्तेमाल करें|Use my location
ગામનું સ્થાન મળ્યું નહીં તમારું લોકેશન વાપરો|गांव का स्थान नहीं मिला अपनी लोकेशन इस्तेमाल करें|Village location not found use your location
ઈન્ટરનેટ ચાલુ કરો અને ફરી પ્રયત્ન કરો|इंटरनेट चालू करें और फिर कोशिश करें|Turn on internet and try again
જૂનો ડેટા દેખાય છે ઑફલાઇન|पुराना डेटा दिख रहा है ऑफ़लाइन|Showing old data offline
છેલ્લે અપડેટ|आखिरी अपडेट|Last updated
ખેડૂત સલાહ|किसान सलाह|Farmer advice
ભારે વરસાદની શક્યતા ખેતરમાંથી પાણી કાઢો અને છંટકાવ ટાળો|भारी बारिश की संभावना खेत से पानी निकालें और छिड़काव टालें|Heavy rain likely drain water from the field and avoid spraying
ખૂબ ગરમી સવાર સાંજ પાણી આપો|बहुत गर्मी सुबह शाम पानी दें|Very hot water in the morning and evening
ઠંડી વધુ છે પાકને ઠંડીથી બચાવો|ठंड ज़्यादा है फसल को ठंड से बचाएं|It is very cold protect crops from the cold
હવામાન સામાન્ય છે નિયમિત દેખરેખ રાખો|मौसम सामान्य है नियमित निगरानी रखें|Weather is normal keep regular watch
સ્વચ્છ આકાશ|साफ आसमान|Clear sky
મોટે ભાગે સ્વચ્છ|ज़्यादातर साफ|Mostly clear
આંશિક વાદળછાયું|आंशिक बादल|Partly cloudy
વાદળછાયું|बादल छाए|Cloudy
ધુમ્મસ|कोहरा|Fog
ઝરમર વરસાદ|हल्की बूंदाबांदी|Drizzle
ભારે વરસાદ|भारी बारिश|Heavy rain
વરસાદી ઝાપટાં|बारिश की बौछारें|Rain showers
હિમવર્ષા|हिमपात|Snow
ગાજવીજ સાથે વરસાદ|गरज के साथ बारिश|Thunderstorm
# ---- NEW: news ----
ખેડૂત સમાચાર|किसान समाचार|Farmer news
દરરોજ અપડેટ થતા ખેડૂત સમાચાર|रोज़ अपडेट होने वाली किसान खबरें|Farmer news updated every day
સમગ્ર ભારત|पूरा भारत|All India
ગુજરાત|गुजरात|Gujarat
બીજું રાજ્ય|दूसरा राज्य|Other state
રાજ્ય પસંદ કરો|राज्य चुनें|Choose state
સમાચાર લોડ થઈ રહ્યા છે|समाचार लोड हो रहे हैं|Loading news
સમાચાર લોડ ન થયા ઈન્ટરનેટ તપાસો|समाचार लोड नहीं हुए इंटरनेट जांचें|Could not load news check your internet
બ્રાઉઝરમાં સમાચાર ખોલો|ब्राउज़र में समाचार खोलें|Open news in browser
કોઈ સમાચાર મળ્યા નહીં|कोई समाचार नहीं मिला|No news found
હમણાં જ|अभी अभी|Just now
મિનિટ પહેલા|मिनट पहले|min ago
કલાક પહેલા|घंटे पहले|h ago
દિવસ પહેલા|दिन पहले|d ago
સ્ત્રોત|स्रोत|Source
# ---- DATA: crop look / adjectives ----
લીલા|हरे|green
પીળા|पीले|yellow
ગોળી|गोली|pellet
જેવું|जैसा|like
સેમી|सेमी|cm
લાંબી|लंबी|long
ચપટી|चपटी|flat
ગોટલી|गुठली|Soak the stone
જાડું|मोटा|thick
થડ|तना|stem
નાનો|छोटा|small
સખત|सख्त|hard
કાળા|काले|black
ભૂરા|भूरे|brown
નાનું|छोटा|small
લાલ|लाल|red
મોટું|बड़ा|large
પાંખ|पंख|wing
કાળું|काला|black
ગોળ|गोल|round
ચળકતું|चमकदार|shiny
લાંબું|लंबा|long
લીલું|हरा|green
ભૂરું|भूरा|brown
લાકડા|लकड़ी|wood
જેવી|जैसी|like
ખૂબ|बहुत|very
ચપટું|चपटा|flat
પીળું|पीला|yellow
સોનેરી|सुनहरा|golden
લાંબો|लंबा|long
દાણો|दाना|grain
મોટો|बड़ा|large
પીળો|पीला|yellow
પાતળો|पतला|thin
રૂંવાળું|रोएंदार|hairy
ગુલાબી|गुलाबी|pink
કથ્થઈ|कत्थई|brown
ભૂરો|भूरा|brown
સફેદ|सफेद|white
કાળો|काला|black
અંડાકાર|अंडाकार|oval
લીલો|हरा|green
આંખવાળી કલમ|आंख वाली कलम|eyed setts
આંખવાળી લીલી|आंख वाली हरी|eyed green
ચપટો|चपटा|flat
બટાટું|आलू|potato
ઉપરની|ऊपर की|top
પાનવાળી|पत्ते वाली|leafy
નાની|छोटी|small
ડાળી|डाली|branch
ત્રિકોણાકાર|त्रिकोणाकार|triangular
છોટી|छोटी|small
વેલ|बेल|vine
માતૃ|मातृ|mother
એક|एक|one
# ---- DATA: planting method (English only; Hindi uses method_hin) ----
બીજા દિવસે પાણીમાં પલાળો|अगले दिन पानी में भिगोएं|Soak in water the next day
નર્સરીમાં વાવો|नर्सरी में बोएं|Sow in the nursery
દિવસ પાણીમાં પલાળો|दिन पानी में भिगोएं|days in water
સ્વસ્થ સકર|स्वस्थ सकर|Healthy sucker in a
ફૂટ ખાડામાં|फीट गड्ढे में|ft pit
કલાક પલાળો|घंटे भिगोएं|hours soaking
તાજા બીજ સીધા ખેતરમાં|ताज़ा बीज सीधे खेत में|Fresh seed directly in the field
દિવસ પલાળો|दिन भिगोएं|days soaking
કટિંગ વધુ સારું|कटिंग बेहतर|Cuttings work better
ફૂટ|फीट|ft
અડધું જમીનમાં|आधा ज़मीन में|Half buried in soil
બીજ પલાળો|बीज भिगोएं|Soak the seed
સીધા ખેતરમાં|सीधे खेत में|Directly in the field
ગ્રાફ્ટિંગ સારું|ग्राफ्टिंग बेहतर|Grafting works better
તાજું બીજ સીધા|ताज़ा बीज सीधे|Fresh seed direct
કટિંગ સારું|कटिंग बेहतर|Cuttings work better
દિવસ પછી રોપો|दिन बाद रोपें|days then transplant
સીધું ખેતરમાં|सीधे खेत में|Directly in the field
લાઈન થી લાઈન|लाइन से लाइन|Line to line
સીધું વાવો|सीधे बोएं|Sow directly
નર્સરીમાં|नर्सरी में|In the nursery
કંદ કાપો|कंद काटें|Cut the tubers
બીજ ફોડીને વાવો|बीज फोड़कर बोएं|Crack the seed and sow
કટિંગ વાવો|कटिंग लगाएं|Plant cuttings
રનર વાવો|रनर लगाएं|Plant runners
કૂંપળ વાવો|कोंपल लगाएं|Plant shoots
કંદ પાણીમાં|कंद पानी में|Tubers in water
બલ્બ વાવો|बल्ब लगाएं|Plant bulbs
કંદ વાવો|कंद लगाएं|Plant tubers
કળી વાવો|कली लगाएं|Plant buds
રાઈઝોમ વાવો|राइज़ोम लगाएं|Plant rhizomes
# ---- DATA: care / rate / harvest ----
દર|हर|Every
દિવસે પાણી|दिन में पानी|days: water
ડ્રિપ ઈરિગેશન|ड्रिप सिंचाई|Drip irrigation
પાણી નિયમિત|नियमित पानी|Regular watering
વધુ પાણી ટાળો|ज़्यादा पानी से बचें|Avoid excess water
પાણી ભરેલું ખેતર|पानी भरा खेत|Flooded field
વાર પાણી|बार पानी|waterings
જીવાત ધ્યાન|कीट पर ध्यान|Watch for pests
પાણી ભરેલું|पानी भरा|Flooded
ઠંડું|ठंडा|Cool
ગ્રાફ્ટિંગ|ग्राफ्टिंग|Grafting
સકર|सकर|Suckers
કટિંગ|कटिंग|Cuttings
કલમ|कलम|Setts
કંદ|कंद|Tubers
રનર|रनर|Runners
કૂંપળ|कोंपल|Shoots
બલ્બ|बल्ब|Bulbs
રાઈઝોમ|राइज़ोम|Rhizomes
વર્ષ|साल|yr
મહિના|महीने|months
# ---- DATA: special tags ----
ઔષધીય વૃક્ષ|औषधीय वृक्ष|Medicinal tree
ફળોનો રાજા|फलों का राजा|King of fruits
વિટામિન|विटामिन|Vitamin
પાચન|पाचन|Digestion
એન્ટીઓક્સિડન્ટ|एंटीऑक्सीडेंट|Antioxidant
બહુ-ઉપયોગી|बहुउपयोगी|Multi-purpose
મોંઘું લાકડું|महंगी लकड़ी|Valuable timber
પોષક|पौष्टिक|Nutritious
મીઠું|मीठा|Sweet
શિયાળાનું|सर्दी का|Winter
ડાયાબિટીસ|डायबिटीज़|Diabetes
સુપરફૂડ|सुपरफूड|Superfood
લાલ ફૂલ|लाल फूल|Red flowers
સુગંધી|सुगंधित|Fragrant
શોભાવાળું|सजावटी|Ornamental
છાયાદાર|छायादार|Shady
મુખ્ય અનાજ|मुख्य अनाज|Staple grain
શિયાળાનો|सर्दी का|Winter
સૂકો|सूखा|Dry-land
લોહ તત્વ|आयरन तत्व|Iron-rich
કેલ્શિયમ|कैल्शियम|Calcium
આરોગ્ય|सेहत|Health
ઝડપી|तेज़|Fast
આયર્ન|आयरन|Iron
સફેદ સોનું|सफेद सोना|White gold
તેલ|तेल|Oil
ઔદ્યોગિક|औद्योगिक|Industrial
મસાલો|मसाला|Spice
દાળ|दाल|Pulse
પ્રોટીન|प्रोटीन|Protein
ખાંડ|चीनी|Sugar
# ---- DATA: medicines ----
ઈયળ|इल्ली|Caterpillar
બોરર|बोरर|Borer
સફેદ માખી|सफेद मक्खी|Whitefly
એફિડ|एफिड|Aphid
આર્મીવોર્મ|आर्मीवर्म|Armyworm
જેસિડ|जैसिड|Jassid
થડ બોરર|तना बोरर|Stem borer
વિલ્ટ|विल्ट|Wilt
બેક્ટેરિયલ|बैक्टीरियल|Bacterial
રસ્ટ|रस्ट|Rust
પાવડરી|पाउडरी|Powdery
ડાઉની માઈલ્ડ્યુ|डाउनी मिल्ड्यू|Downy mildew
લીફ સ્પોટ|लीफ स्पॉट|Leaf spot
સ્પોટ|स्पॉट|Spot
નીંદણ|खरपतवार|Weeds
ઘાસ|घास|Grass
પહોળા પાન|चौड़ी पत्ती|Broadleaf
નાઈટ્રોજન|नाइट्रोजन|Nitrogen
પોટેશિયમ|पोटैशियम|Potassium
સંતુલિત|संतुलित|Balanced
ઝિંક|ज़िंक|Zinc
બોરોન|बोरॉन|Boron
ફૂલ-ફળ|फूल-फल|Flower-fruit
ફૂલ ઝરવું|फूल झड़ना|Flower drop
ફળ પાકવું|फल पकना|Fruit ripening
સર્વાંગી|सर्वांगीण|All-round
જમીન|ज़मीन|Soil
વૃદ્ધિ|वृद्धि|Growth
મૂળ|जड़|Roots
તણાવ|तनाव|Stress
આલ્કલાઈન|क्षारीय|Alkaline
ઍસિડિક|अम्लीय|Acidic
પાણી ધારણ|पानी धारण|Water retention
માસ્ક|मास्क|Mask
ગ્લોવ્સ|दस्ताने|Gloves
ઝેરી|ज़हरीला|Toxic
# ---- DATA: symptoms ----
નીમ તેલ|नीम तेल|Neem oil
છાશ સ્પ્રે|छाछ स्प्रे|Buttermilk spray
હળદર|हल्दी|Turmeric
સોડા|सोडा|Soda
લસણ|लहसुन|Garlic
મરચી|मिर्च|Chili
ગૌમૂત્ર ડ્રેન્ચ|गौमूत्र ड्रेंच|Cow-urine drench
ચાલુ રાખો|जारी रखें|Continue
કોઈ નહીં|कोई नहीं|None
નીમ સ્પ્રે|नीम स्प्रे|Neem spray
સંતુલિત ખાતર|संतुलित खाद|Balanced fertilizer
ભેજ નિયંત્રણ|नमी नियंत्रण|Humidity control
સ્ટીકી ટ્રેપ|स्टिकी ट्रैप|Sticky trap
ડ્રેનેજ|ड्रेनेज|Drainage
# ---- DATA: organic recipes ----
નીમ તેલ સ્પ્રે|नीम तेल स्प्रे|Neem oil spray
દશપર્ણી અર્ક|दशपर्णी अर्क|Dashaparni extract
છાશ|छाछ|Buttermilk
હિંગ સ્પ્રે|हींग स्प्रे|Asafoetida spray
લસણ-મરચી અર્ક|लहसुन-मिर्च अर्क|Garlic-chili extract
બેકિંગ સોડા|बेकिंग सोडा|Baking soda
જીવામૃત|जीवामृत|Jeevamrut
રાખ|राख|Ash
લાકડાની|लकड़ी की|Wood
ભૂકી|चूर्ण|powder
ગૌમૂત્ર|गौमूत्र|Cow urine
સાબુ|साबुन|Soap
લિટર|लीटर|litre
પ્રકારના કડવા પાન|प्रकार के कड़वे पत्ते|types of bitter leaves
છાણ|गोबर|Dung
દિવસ આથો|दिन किण्वन|days fermentation
દિવસ જૂની છાશ|दिन पुरानी छाछ|days old buttermilk
હિંગ|हींग|Asafoetida
લીલા મરચા|हरी मिर्च|Green chilies
વાટીને પાણી|पीसकर पानी|grind with water
ગાળીને|छानकर|strain
પાણીમાં|पानी में|in water
દેશી ગાય છાણ|देसी गाय का गोबर|Desi cow dung
ગૂળ|गुड़|Jaggery
બેસન|बेसन|Gram flour
માટી|मिट्टी|Soil
મુઠ્ઠી|मुट्ठी|handful
લાકડાની રાખ સીધી છાંટવી|लकड़ी की राख सीधे छिड़कें|Sprinkle wood ash directly
બધા પ્રકારની જીવાત|सभी प्रकार के कीट|All kinds of pests
કીડી|चींटी|Ants
માટી સુધારણા|मिट्टी सुधार|Soil improvement
પોષણ|पोषण|Nutrition
મૂળ રોગ|जड़ रोग|Root disease
ડાઘ|दाग|Spots
જીવાત|कीट|Pests
અર્ક|अर्क|Extract
# ---- DATA: government schemes ----
પ્રધાનમંત્રી ફસલ બીમા યોજના|प्रधानमंत्री फसल बीमा योजना|PM Crop Insurance Scheme
સોઈલ હેલ્થ કાર્ડ|सॉइल हेल्थ कार्ड|Soil Health Card
કિસાન ક્રેડિટ કાર્ડ|किसान क्रेडिट कार्ड|Kisan Credit Card
ઈ-નામ|ई-नाम|e-NAM
ખેડૂત પોર્ટલ|किसान पोर्टल|Khedut Portal
નાના-સીમાંત ખેડૂતોને વાર્ષિક આર્થિક સહાય|छोटे-सीमांत किसानों को वार्षिक आर्थिक सहायता|Annual financial aid for small and marginal farmers
હપ્તામાં|किस्तों में|in installments
કુદરતી આફતથી પાક નુકસાનનો વીમો|प्राकृतिक आपदा से फसल नुकसान का बीमा|Insurance against crop loss from natural disasters
માટી પરીક્ષણ અને ખાતરની સલાહ|मिट्टी परीक्षण और खाद की सलाह|Soil testing and fertilizer advice
ખેતી માટે ઓછા વ્યાજે લોન|खेती के लिए कम ब्याज पर लोन|Low-interest loans for farming
ઓનલાઈન બજારમાં પાક વેચાણ|ऑनलाइन बाज़ार में फसल बिक्री|Sell crops in the online market
ગુજરાતની ખેતી યોજનાઓ માટે ઓનલાઈન અરજી|गुजरात की कृषि योजनाओं के लिए ऑनलाइन आवेदन|Online application for Gujarat farming schemes
# ---- NEW (round 2): accounts, icons ----
ખેતીનો હિસાબ|खेती का हिसाब|Farm accounts
કુલ આવક|कुल आमदनी|Total income
કુલ ખર્ચ|कुल खर्च|Total expense
ચોખ્ખો નફો|शुद्ध मुनाफ़ा|Net profit
ચોખ્ખી ખોટ|शुद्ध नुकसान|Net loss
રકમ|राशि|Amount
નોંધ લખો|नोट लिखें|Write a note
હજી કોઈ નોંધ નથી|अभी कोई नोट नहीं|No entries yet
રકમ સાચી લખો|राशि सही लिखें|Enter a valid amount
રોગ અને જીવાત|रोग और कीट|Diseases and pests
બીજ વાવેતર લણણી|बीज बुवाई कटाई|Seed sowing harvest
દવા ખાતર ભાવ|दवा खाद भाव|Medicine fertilizer prices
ખાતર સ્પ્રે ગણતરી|खाद स्प्रे गणना|Fertilizer spray calculators
આજના ખેડૂત સમાચાર|आज की किसान खबरें|Today's farmer news
આવક ખર્ચ નફો|आमदनी खर्च मुनाफ़ा|Income expense profit
જ્ઞાન ચકાસો|ज्ञान जांचें|Test your knowledge
યોજના રેસીપી ડાયરી|योजना रेसिपी डायरी|Schemes recipes diary
# ---- NEW (round 3): seeds / tracker / nearby ----
બીજ સંગ્રહ|बीज संग्रह|Seed collection
ફોટા સાથે બધા બીજ|फोटो के साथ सभी बीज|All seeds with photos
બીજ શોધો|बीज खोजें|Search seed
કોઈ બીજ મળ્યું નહીં|कोई बीज नहीं मिला|No seed found
તમારા ખેતર માટે જથ્થો|आपके खेत के लिए मात्रा|Quantity for your farm
મારો પાક ટ્રેકર|मेरा फसल ट्रैकर|My crop tracker
વાવેતરથી લણણી સુધી|बुवाई से कटाई तक|From sowing to harvest
વાવેતર તારીખ|बुवाई की तारीख|Sowing date
પાક ઉમેરો|फसल जोड़ें|Add crop
લણણી અંદાજ|कटाई का अंदाज़ा|Expected harvest
દિવસ થયા|दिन हुए|days passed
લણણી લાયક છે|कटाई योग्य है|Ready to harvest
લણણી નજીક છે|कटाई नज़दीक है|Harvest is near
હજી વધી રહ્યો છે|अभी बढ़ रही है|Still growing
હજી કોઈ પાક ઉમેર્યો નથી|अभी कोई फसल नहीं जोड़ी|No crop added yet
વાવેતરથી|बुवाई से|From sowing
નજીકની કૃષિ દુકાન|नज़दीकी कृषि दुकान|Nearby agri shop
દુકાન અને કેન્દ્ર શોધો|दुकान और केंद्र खोजें|Find shops and centres
નજીકની કૃષિ સેવાઓ|नज़दीकी कृषि सेवाएं|Nearby agri services
ગૂગલ મેપમાં ખુલશે|गूगल मैप में खुलेगा|Opens in Google Maps
કૃષિ દુકાન બીજ ખાતર|कृषि दुकान बीज खाद|Agro shop seeds fertilizer
કૃષિ વિજ્ઞાન કેન્દ્ર|कृषि विज्ञान केंद्र|Krishi Vigyan Kendra
માર્કેટ યાર્ડ|मार्केट यार्ड|Market yard
પશુ દવાખાનું|पशु दवाखाना|Veterinary clinic
# ---- round 4 ----
રિપોર્ટ કોપી કરો|रिपोर्ट कॉपी करें|Copy report
ફોસ્ફરસ|फॉस्फोरस|Phosphorus
"""


def _build_i18n():
    hi, en = {}, {}
    for line in I18N_TABLE.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = line.split("|")
        if len(p) != 3:
            continue
        g, h, e = [x.strip() for x in p]
        hi[g] = "" if h == "~" else h      # "" => auto-transliterate
        en[g] = e
    for k, g in GUJ_NAMES.items():         # crop names (Gujarati -> Hindi / English)
        hi.setdefault(g, HIN_NAMES.get(k, ""))
        en.setdefault(g, k)
    return {"hi": hi, "en": en}


I18N = _build_i18n()

NEW_TXT = r"""# key|gu|hi|en  (';;' = line break / bullet separator)
ui.learn|📚 શીખો અને માર્ગદર્શન|📚 सीखें और मार्गदर्शन|📚 Learn and guides
ui.core|🔍 શું તપાસવું છે?|🔍 क्या जांचना है?|🔍 What do you want to check?
ui.back|⬅️ પાછા|⬅️ वापस|⬅️ Back
ui.prev|⏮️ પાછળ|⏮️ पीछे|⏮️ Previous
ui.next|આગળ ⏭️|आगे ⏭️|Next ⏭️
ui.play|▶️ ઓટો પ્લે|▶️ ऑटो प्ले|▶️ Auto play
ui.pause|⏸️ રોકો|⏸️ रोकें|⏸️ Pause
ui.step|સ્ટેપ|स्टेप|Step
ui.open|ખોલો|खोलें|Open
ui.copied|📋 કોપી થયું|📋 कॉपी हो गया|📋 Copied
ui.copy|📋 રિપોર્ટ કોપી કરો|📋 रिपोर्ट कॉपी करें|📋 Copy report
ui.nolink|ℹ️ બધી માહિતી એપમાં જ છે|ℹ️ सारी जानकारी ऐप में ही है|ℹ️ All information is inside the app
t.fg|ખેતી માર્ગદર્શિકા|खेती मार्गदर्शिका|Farming guide
d.fg|પાક પ્રમાણે પૂરી ખેતી|फसल के अनुसार पूरी खेती|Full farming per crop
t.mkf|ખાતર બનાવો|खाद बनाएं|Make fertilizer
d.mkf|સ્ટેપ બાય સ્ટેપ વિડીયો|स्टेप बाय स्टेप वीडियो|Step by step video
t.mkp|જૈવિક દવા બનાવો|जैविक दवा बनाएं|Make bio-spray
d.mkp|ઘરે દવા બનાવવાની રીત|घर पर दवा बनाने की विधि|Home-made sprays
t.mkt|ખેતી તકનીક|खेती तकनीक|Farming techniques
d.mkt|નર્સરી ગ્રાફ્ટિંગ ડ્રિપ|नर्सरी ग्राफ्टिंग ड्रिप|Nursery grafting drip
t.soil|જમીન માર્ગદર્શિકા|मिट्टी मार्गदर्शिका|Soil guide
d.soil|જમીન પ્રકાર અને ટેસ્ટ સલાહ|मिट्टी के प्रकार और जांच सलाह|Soil types and test advice
t.irr|પિયત અને પાણી|सिंचाई और पानी|Irrigation and water
d.irr|પાણીની ગણતરી|पानी की गणना|Water calculator
t.pest|જીવાત ગ્રંથાલય|कीट पुस्तकालय|Pest library
d.pest|ઓળખ અને નિયંત્રણ|पहचान और नियंत्रण|Identify and control
t.dis|રોગ ગ્રંથાલય|रोग पुस्तकालय|Disease library
d.dis|લક્ષણ અને ઉપચાર|लक्षण और उपचार|Symptoms and cure
t.org|જૈવિક ખેતી|जैविक खेती|Organic farming
d.org|શરૂઆતથી પ્રમાણપત્ર સુધી|शुरुआत से प्रमाणन तक|From start to certification
t.cal|ઋતુ કેલેન્ડર|मौसम कैलेंडर|Season calendar
d.cal|મહિના પ્રમાણે કામ|महीने के अनुसार काम|Month-wise work
t.adv|સ્પ્રે અને પિયત સલાહ|स्प्रे और सिंचाई सलाह|Spray and irrigation advice
d.adv|હવામાન મુજબ આગામી 3 દિવસ|मौसम के अनुसार अगले 3 दिन|Next 3 days by weather
t.safe|સુરક્ષા અને પ્રાથમિક સારવાર|सुरक्षा और प्राथमिक उपचार|Safety and first aid
d.safe|દવા છાંટતી વખતે સાવચેતી|दवा छिड़कते समय सावधानी|Care while spraying
t.gloss|કૃષિ શબ્દકોશ|कृषि शब्दकोश|Farm glossary
d.gloss|ખેતીના શબ્દોના અર્થ|खेती के शब्दों के अर्थ|Meanings of farm terms
t.tip|આજની ટીપ|आज की टिप|Tip of the day
d.tip|રોજ એક નવી ટીપ|रोज़ एक नई टिप|A new tip every day
t.mach|યંત્ર માર્ગદર્શિકા|यंत्र मार्गदर्शिका|Machinery guide
d.mach|ટ્રેક્ટર અને ઓજારો|ट्रैक्टर और औज़ार|Tractor and implements
t.animal|પશુપાલન|पशुपालन|Animal husbandry
d.animal|ગાય ભેંસ બકરી સંભાળ|गाय भैंस बकरी देखभाल|Cow buffalo goat care
t.store|સંગ્રહ અને વેચાણ|भंडारण और बिक्री|Storage and selling
d.store|કાપણી પછીની સંભાળ|कटाई के बाद की देखभाल|Post-harvest care
fg.pick|પાક પસંદ કરો|फसल चुनें|Choose a crop
fg.h1|🚜 જમીન તૈયારી|🚜 ज़मीन की तैयारी|🚜 Land preparation
fg.h2|🌰 બીજ અને વાવેતર|🌰 बीज और बुवाई|🌰 Seed and sowing
fg.h3|💧 પાણી વ્યવસ્થાપન|💧 जल प्रबंधन|💧 Water management
fg.h4|🧪 ખાતર|🧪 खाद|🧪 Fertilizer
fg.h5|🛡️ રોગ જીવાત અને નીંદણ|🛡️ रोग कीट और खरपतवार|🛡️ Pests diseases and weeds
fg.h6|🌾 લણણી અને સંગ્રહ|🌾 कटाई और भंडारण|🌾 Harvest and storage
fg.1.tree|ખાડા 1x1x1 મીટર ખોદી 15 દિવસ તપાવો પછી છાણિયું ખાતર અને માટી ભરો.|1x1x1 मीटर गड्ढे खोदकर 15 दिन धूप लगाएं फिर गोबर खाद और मिट्टी भरें।|Dig 1x1x1 m pits sun-dry them for 15 days then fill with farmyard manure and soil.
fg.1.grain|ઊંડી ખેડ કરી 2 વાર કરબ ચલાવો જમીન સમતળ કરી ભૂકો જેવી બનાવો.|गहरी जुताई कर 2 बार हैरो चलाएं ज़मीन समतल कर भुरभुरी बनाएं।|Plough deep harrow twice then level the field to a fine tilth.
fg.1.cash|ઊંડી ખેડ કરી છાણિયું ખાતર 4-5 ટન પ્રતિ એકર નાખી જમીન સમતળ કરો.|गहरी जुताई कर 4-5 टन गोबर खाद प्रति एकड़ डालें और ज़मीन समतल करें।|Plough deep add 4-5 tons farmyard manure per acre and level the land.
fg.1.veg|ખેતર ખેડી ક્યારા અથવા પાળા બનાવો અને સારું સડેલું છાણિયું ખાતર નાખો.|खेत जोतकर क्यारियां या मेड़ बनाएं और अच्छी सड़ी गोबर खाद डालें।|Plough the field make beds or ridges and add well-rotted farmyard manure.
fg.1.fruit|ખાડા 1x1x1 મીટર કરી ખાતર માટી ભરો અને છોડ વચ્ચે યોગ્ય અંતર રાખો.|1x1x1 मीटर गड्ढे बनाकर खाद मिट्टी भरें और पौधों में उचित दूरी रखें।|Make 1x1x1 m pits fill with manure and soil and keep proper plant spacing.
fg.1.flower|જમીન ઝીણી અને પોચી કરી ક્યારા બનાવો પાણીનો નિકાલ સારો રાખો.|ज़मीन बारीक और भुरभुरी कर क्यारियां बनाएं पानी की निकासी अच्छी रखें।|Make the soil fine and loose prepare beds and keep good drainage.
fg.1.herb|હળવી ખેડ કરી સારા નિતારવાળી જમીન પસંદ કરો અને જૈવિક ખાતર ભેળવો.|हल्की जुताई कर अच्छे जल निकास वाली ज़मीन चुनें और जैविक खाद मिलाएं।|Light ploughing choose well-drained land and mix organic manure.
fg.2|🌰 બીજ: {seed};; ⚖️ બીજ દર: {rate};; ⏱️ ઉગવાનો સમય: {germ};; 📅 વાવેતર સમય: {season};; 🧭 રીત: {method}|🌰 बीज: {seed};; ⚖️ बीज दर: {rate};; ⏱️ उगने का समय: {germ};; 📅 बुवाई का समय: {season};; 🧭 विधि: {method}|🌰 Seed: {seed};; ⚖️ Seed rate: {rate};; ⏱️ Germination: {germ};; 📅 Sowing time: {season};; 🧭 Method: {method}
fg.3|💧 {care};; વાવેતર પછી તરત હળવું પિયત આપો;; ફૂલ અને દાણા ભરાવાના સમયે પાણી ચૂકશો નહીં|💧 {care};; बुवाई के तुरंत बाद हल्की सिंचाई दें;; फूल और दाना भरने के समय पानी न चूकें|💧 {care};; Give a light irrigation right after sowing;; Do not miss water at flowering and grain filling
fg.4.tree|છાણિયું ખાતર 10 kg અને {npk} દર વર્ષે બે હપ્તામાં આપો.|गोबर खाद 10 kg और {npk} हर साल दो किस्तों में दें।|Give 10 kg farmyard manure and {npk} every year in two splits.
fg.4.grain|{npk}: અડધો નાઈટ્રોજન અને પૂરો ફોસ્ફરસ પોટાશ વાવેતર વખતે બાકી નાઈટ્રોજન 30 દિવસે.|{npk}: आधा नाइट्रोजन और पूरा फॉस्फोरस पोटाश बुवाई पर बाकी नाइट्रोजन 30 दिन पर।|{npk}: half nitrogen with full phosphorus and potash at sowing the rest nitrogen at 30 days.
fg.4.cash|{npk}: ફોસ્ફરસ પોટાશ પાયામાં અને નાઈટ્રોજન 2-3 હપ્તામાં આપો.|{npk}: फॉस्फोरस पोटाश आधार में और नाइट्रोजन 2-3 किस्तों में दें।|{npk}: phosphorus and potash as basal and nitrogen in 2-3 splits.
fg.4.veg|{npk}: પાયામાં અડધું અને બાકીનું 25-30 દિવસે અને ફૂલ સમયે આપો.|{npk}: आधार में आधा और बाकी 25-30 दिन पर और फूल के समय दें।|{npk}: half as basal and the rest at 25-30 days and at flowering.
fg.4.fruit|પ્રતિ ઝાડ છાણિયું ખાતર 20 kg સાથે {npk} ચોમાસા અને શિયાળામાં આપો.|प्रति पेड़ गोबर खाद 20 kg के साथ {npk} मानसून और सर्दी में दें।|Per tree 20 kg farmyard manure with {npk} in monsoon and winter.
fg.4.flower|{npk}: દર 20-25 દિવસે હળવા હપ્તામાં આપો અને ફૂલ આવે ત્યારે પોટાશ વધારો.|{npk}: हर 20-25 दिन में हल्की किस्तों में दें और फूल आने पर पोटाश बढ़ाएं।|{npk}: give in light doses every 20-25 days and raise potash at flowering.
fg.4.herb|{npk}: મુખ્યત્વે જૈવિક ખાતર વર્મી કમ્પોસ્ટ અને જીવામૃત વાપરો.|{npk}: मुख्यतः जैविक खाद वर्मी कम्पोस्ट और जीवामृत का उपयोग करें।|{npk}: mainly use organic manure vermicompost and jeevamrut.
fg.npk.tree|NPK 500 g પ્રતિ ઝાડ|NPK 500 g प्रति पेड़|NPK 500 g per tree
fg.npk.grain|NPK 48-24-16 kg/એકર|NPK 48-24-16 kg/एकड़|NPK 48-24-16 kg/acre
fg.npk.cash|NPK 48-24-24 kg/એકર|NPK 48-24-24 kg/एकड़|NPK 48-24-24 kg/acre
fg.npk.veg|NPK 40-20-20 kg/એકર|NPK 40-20-20 kg/एकड़|NPK 40-20-20 kg/acre
fg.npk.fruit|NPK 1 kg પ્રતિ ઝાડ|NPK 1 kg प्रति पेड़|NPK 1 kg per tree
fg.npk.flower|NPK 40-20-20 kg/એકર|NPK 40-20-20 kg/एकड़|NPK 40-20-20 kg/acre
fg.npk.herb|જૈવિક ખાતર 4 ટન/એકર|जैविक खाद 4 टन/एकड़|Organic manure 4 tons/acre
fg.acre|kg/એકર|kg/एकड़|kg/acre
fg.5|🌿 20-25 દિવસે પહેલી નિંદામણ અને 45 દિવસે બીજી કરો;; 🐛 દર અઠવાડિયે પાન તપાસો અને શરૂઆતમાં જ લીમડા અર્ક છાંટો;; 🧪 જરૂર પડે તો જ ભલામણ મુજબ દવા છાંટો|🌿 20-25 दिन पर पहली निराई और 45 दिन पर दूसरी करें;; 🐛 हर हफ्ते पत्ते जांचें और शुरुआत में ही नीम अर्क छिड़कें;; 🧪 ज़रूरत हो तभी सिफारिश अनुसार दवा छिड़कें|🌿 Weed at 20-25 days and again at 45 days;; 🐛 Check leaves every week and spray neem extract early;; 🧪 Use chemical sprays only if needed as per label
fg.6|🌾 લણણીનો સમય: {harvest};; ☀️ કાપણી પછી સારી રીતે સૂકવો;; 📦 સ્વચ્છ સૂકી જગ્યાએ સંગ્રહ કરો અને ભાવ જોઈને વેચો|🌾 कटाई का समय: {harvest};; ☀️ कटाई के बाद अच्छी तरह सुखाएं;; 📦 साफ सूखी जगह पर भंडारण करें और भाव देखकर बेचें|🌾 Harvest time: {harvest};; ☀️ Dry well after harvest;; 📦 Store in a clean dry place and sell after checking prices
# ---- soil advisor / irrigation calc / weather advisor ----
sa.title|🧪 જમીન ટેસ્ટ સલાહકાર|🧪 मिट्टी जांच सलाहकार|🧪 Soil test advisor
sa.ph|pH (6-8)|pH (6-8)|pH (6-8)
sa.n|નાઈટ્રોજન|नाइट्रोजन|Nitrogen
sa.p|ફોસ્ફરસ|फॉस्फोरस|Phosphorus
sa.k|પોટાશ|पोटाश|Potash
sa.low|ઓછું|कम|Low
sa.med|મધ્યમ|मध्यम|Medium
sa.high|વધુ|ज़्यादा|High
sa.go|સલાહ જુઓ|सलाह देखें|Get advice
sa.ph.acid|⚠️ જમીન ખાટી છે: ચૂનો 200 kg/એકર અને છાણિયું ખાતર નાખો.|⚠️ मिट्टी अम्लीय है: चूना 200 kg/एकड़ और गोबर खाद डालें।|⚠️ Soil is acidic: add lime 200 kg/acre and farmyard manure.
sa.ph.ok|✅ pH યોગ્ય છે: મોટાભાગના પાક માટે સારી જમીન.|✅ pH सही है: अधिकतर फसलों के लिए अच्छी मिट्टी।|✅ pH is fine: good soil for most crops.
sa.ph.alk|⚠️ જમીન ક્ષારીય છે: જિપ્સમ 200 kg/એકર અને લીલો પડવાશ કરો.|⚠️ मिट्टी क्षारीय है: जिप्सम 200 kg/एकड़ और हरी खाद करें।|⚠️ Soil is alkaline: add gypsum 200 kg/acre and green manure.
sa.n.low|🌱 નાઈટ્રોજન ઓછું: યુરિયા અથવા છાણિયું ખાતર વધારો.|🌱 नाइट्रोजन कम: यूरिया या गोबर खाद बढ़ाएं।|🌱 Low nitrogen: increase urea or farmyard manure.
sa.n.med|🌱 નાઈટ્રોજન મધ્યમ: ભલામણ મુજબ ખાતર આપો.|🌱 नाइट्रोजन मध्यम: सिफारिश अनुसार खाद दें।|🌱 Medium nitrogen: apply the recommended dose.
sa.n.high|🌱 નાઈટ્રોજન વધુ: યુરિયા ઘટાડો અને વધુ પાણી ટાળો.|🌱 नाइट्रोजन ज़्यादा: यूरिया घटाएं और ज़्यादा पानी से बचें।|🌱 High nitrogen: cut urea and avoid excess water.
sa.p.low|🌱 ફોસ્ફરસ ઓછું: DAP અથવા SSP પાયામાં આપો.|🌱 फॉस्फोरस कम: DAP या SSP आधार में दें।|🌱 Low phosphorus: apply DAP or SSP as basal.
sa.p.med|🌱 ફોસ્ફરસ મધ્યમ: જાળવણી માત્રા આપો.|🌱 फॉस्फोरस मध्यम: रखरखाव मात्रा दें।|🌱 Medium phosphorus: apply maintenance dose.
sa.p.high|🌱 ફોસ્ફરસ વધુ: આ વર્ષે ફોસ્ફરસ ખાતર બંધ રાખો.|🌱 फॉस्फोरस ज़्यादा: इस साल फॉस्फोरस खाद रोकें।|🌱 High phosphorus: skip phosphorus fertilizer this year.
sa.k.low|🌱 પોટાશ ઓછું: MOP અથવા પોટેશિયમ નાઈટ્રેટ આપો.|🌱 पोटाश कम: MOP या पोटैशियम नाइट्रेट दें।|🌱 Low potash: apply MOP or potassium nitrate.
sa.k.med|🌱 પોટાશ મધ્યમ: ભલામણ મુજબ આપો.|🌱 पोटाश मध्यम: सिफारिश अनुसार दें।|🌱 Medium potash: apply as recommended.
sa.k.high|🌱 પોટાશ વધુ: આ વર્ષે પોટાશ ઘટાડો.|🌱 पोटाश ज़्यादा: इस साल पोटाश घटाएं।|🌱 High potash: reduce potash this year.
ic.title|💧 પાણીની ગણતરી|💧 पानी की गणना|💧 Water calculator
ic.cat|પાક પ્રકાર|फसल का प्रकार|Crop type
ic.method|પિયત પદ્ધતિ|सिंचाई विधि|Irrigation method
ic.flood|પાટ પિયત|क्यारी सिंचाई|Flood
ic.spr|ફુવારા|फव्वारा|Sprinkler
ic.drip|ટપક|ड्रिप|Drip
ic.bigha|ખેતર વીઘા|खेत बीघा|Farm bigha
ic.depth|પાણીની ઊંડાઈ સેમી|पानी की गहराई सेमी|Water depth cm
ic.pump|પંપ લિટર પ્રતિ મિનિટ|पंप लीटर प्रति मिनट|Pump litres per minute
ic.go|ગણતરી કરો|गणना करें|Calculate
ic.res|કુલ પાણી|कुल पानी|Total water
ic.hours|પંપ ચલાવવાનો સમય|पंप चलाने का समय|Pump running time
ic.hr|કલાક|घंटे|hours
ic.save|બચત|बचत|Saving
adv.title|🌦️ આગામી 3 દિવસ|🌦️ अगले 3 दिन|🌦️ Next 3 days
adv.spray.ok|✅ છંટકાવ માટે સારો દિવસ|✅ छिड़काव के लिए अच्छा दिन|✅ Good day to spray
adv.spray.no|❌ છંટકાવ ટાળો|❌ छिड़काव टालें|❌ Avoid spraying
adv.rain|વરસાદ|बारिश|Rain
adv.wind|પવન|हवा|Wind
adv.irr.skip|💧 પિયત જરૂરી નથી વરસાદ આવશે|💧 सिंचाई ज़रूरी नहीं बारिश आएगी|💧 No irrigation needed rain is coming
adv.irr.hot|🔥 ગરમી વધુ: સાંજે પિયત આપો|🔥 गर्मी ज़्यादा: शाम को सिंचाई दें|🔥 Very hot: irrigate in the evening
adv.irr.norm|💧 જમીન ભેજ તપાસી જરૂર મુજબ પિયત આપો|💧 मिट्टी की नमी जांचकर ज़रूरत अनुसार सिंचाई दें|💧 Check soil moisture and irrigate as needed
adv.frost|❄️ ઠંડી: પાકને ઢાંકો અથવા સાંજે હળવું પિયત આપો|❄️ ठंड: फसल ढकें या शाम को हल्की सिंचाई दें|❄️ Cold: cover crops or give a light evening irrigation
adv.nodata|⚠️ હવામાન ડેટા લોડ થયો નથી પહેલા હવામાન પેજ ખોલો|⚠️ मौसम डेटा लोड नहीं हुआ पहले मौसम पेज खोलें|⚠️ Weather data not loaded open the weather page first
cal.pick|મહિનો પસંદ કરો|महीना चुनें|Choose month
cal.sow|આ મહિને વાવી શકાય|इस महीने बो सकते हैं|Can be sown this month
cal.work|આ મહિનાનું કામ|इस महीने का काम|This month's work
tip.next|નવી ટીપ|नई टिप|New tip
gl.search|શબ્દ શોધો|शब्द खोजें|Search a term
# ---- how-to guides (step player) ----
h.jeevamrut.t|🐄 જીવામૃત બનાવો|🐄 जीवामृत बनाएं|🐄 Make Jeevamrut
h.jeevamrut.1|🛢️ 200 લિટરના ડ્રમમાં 180 લિટર પાણી ભરો.|🛢️ 200 लीटर के ड्रम में 180 लीटर पानी भरें।|🛢️ Fill a 200 litre drum with 180 litres of water.
h.jeevamrut.2|🐄 દેશી ગાયનું 10 kg તાજું છાણ અને 10 લિટર ગૌમૂત્ર નાખો.|🐄 देसी गाय का 10 kg ताज़ा गोबर और 10 लीटर गौमूत्र डालें।|🐄 Add 10 kg fresh desi cow dung and 10 litres cow urine.
h.jeevamrut.3|🍯 2 kg ગોળ 2 kg ચણાનો લોટ અને મુઠ્ઠીભર ખેતરની માટી ઉમેરો.|🍯 2 kg गुड़ 2 kg बेसन और मुट्ठी भर खेत की मिट्टी मिलाएं।|🍯 Add 2 kg jaggery 2 kg gram flour and a handful of farm soil.
h.jeevamrut.4|🌀 લાકડીથી સવાર સાંજ ઘડિયાળની દિશામાં હલાવો અને છાંયડામાં 5-7 દિવસ રાખો.|🌀 लकड़ी से सुबह शाम घड़ी की दिशा में हिलाएं और छाया में 5-7 दिन रखें।|🌀 Stir clockwise morning and evening with a stick and keep in shade for 5-7 days.
h.jeevamrut.5|💦 એક એકરે 200 લિટર પિયત સાથે અથવા 10 ગણું પાણી ભેળવી છાંટો.|💦 एक एकड़ में 200 लीटर सिंचाई के साथ या 10 गुना पानी मिलाकर छिड़कें।|💦 Apply 200 litres per acre with irrigation or spray after mixing with 10 times water.
h.vermi.t|🪱 વર્મી કમ્પોસ્ટ બનાવો|🪱 वर्मी कम्पोस्ट बनाएं|🪱 Make vermicompost
h.vermi.1|🏗️ છાંયડાવાળી જગ્યાએ 10x3 ફૂટનો ક્યારો કે ટાંકો બનાવો.|🏗️ छायादार जगह पर 10x3 फुट का बेड या टैंक बनाएं।|🏗️ Build a 10x3 ft bed or tank in a shaded place.
h.vermi.2|🌾 નીચે પાંદડા અને સૂકો ચારો 4 ઇંચ પાથરો.|🌾 नीचे पत्ते और सूखा चारा 4 इंच बिछाएं।|🌾 Spread a 4 inch layer of leaves and dry fodder at the bottom.
h.vermi.3|💩 અડધું સડેલું છાણ 1 ફૂટ ઊંચાઈ સુધી ભરો અને પાણી છાંટો.|💩 आधा सड़ा गोबर 1 फुट ऊंचाई तक भरें और पानी छिड़कें।|💩 Fill half-rotted dung up to 1 ft and sprinkle water.
h.vermi.4|🪱 પ્રતિ ચોરસ મીટર 1 kg અળસિયા છોડો અને ભીના બોરીથી ઢાંકો.|🪱 प्रति वर्ग मीटर 1 kg केंचुए छोड़ें और गीली बोरी से ढकें।|🪱 Release 1 kg earthworms per sq metre and cover with a wet jute sack.
h.vermi.5|🗓️ રોજ પાણી છાંટો 45-60 દિવસે ચા જેવું કાળું ખાતર તૈયાર થશે.|🗓️ रोज़ पानी छिड़कें 45-60 दिन में चाय जैसी काली खाद तैयार होगी।|🗓️ Sprinkle water daily and dark tea-like compost is ready in 45-60 days.
h.compost.t|♻️ ખાડા કમ્પોસ્ટ|♻️ गड्ढा कम्पोस्ट|♻️ Pit compost
h.compost.1|⛏️ 6x4x3 ફૂટનો ખાડો છાંયડામાં ખોદો.|⛏️ 6x4x3 फुट का गड्ढा छाया में खोदें।|⛏️ Dig a 6x4x3 ft pit in shade.
h.compost.2|🌿 ખેતરનો કચરો સૂકા અને લીલા પાંદડાં પાથરો.|🌿 खेत का कचरा सूखे और हरे पत्ते बिछाएं।|🌿 Spread farm waste with dry and green leaves.
h.compost.3|🐄 છાણનું પાતળું પડ કરો અને ઉપર માટી નાખો.|🐄 गोबर की पतली परत करें और ऊपर मिट्टी डालें।|🐄 Add a thin layer of dung and cover with soil.
h.compost.4|💧 15 દિવસે પાણી છાંટી ઉલટ-પલટ કરો.|💧 15 दिन पर पानी छिड़ककर पलटें।|💧 Sprinkle water and turn it at 15 days.
h.compost.5|✅ 90-120 દિવસે ખાતર કાળું અને ભૂકો જેવું બને ત્યારે વાપરો.|✅ 90-120 दिन में खाद काली और भुरभुरी बनने पर उपयोग करें।|✅ Use when it turns dark and crumbly in 90-120 days.
h.panch.t|🐮 પંચગવ્ય બનાવો|🐮 पंचगव्य बनाएं|🐮 Make Panchagavya
h.panch.1|🐄 5 kg છાણ અને 1 kg ઘી ભેળવી 3 દિવસ રાખો.|🐄 5 kg गोबर और 1 kg घी मिलाकर 3 दिन रखें।|🐄 Mix 5 kg dung and 1 kg ghee and keep for 3 days.
h.panch.2|💧 3 લિટર ગૌમૂત્ર અને 10 લિટર પાણી ઉમેરો.|💧 3 लीटर गौमूत्र और 10 लीटर पानी मिलाएं।|💧 Add 3 litres cow urine and 10 litres water.
h.panch.3|🥛 2 લિટર દૂધ 2 લિટર દહીં 3 લિટર નાળિયેર પાણી ઉમેરો.|🥛 2 लीटर दूध 2 लीटर दही 3 लीटर नारियल पानी मिलाएं।|🥛 Add 2 litres milk 2 litres curd and 3 litres coconut water.
h.panch.4|🍌 પાકાં 12 કેળાં અને 3 લિટર ગોળનું પાણી નાખો 15 દિવસ સવાર સાંજ હલાવો.|🍌 12 पके केले और 3 लीटर गुड़ का पानी डालें 15 दिन सुबह शाम हिलाएं।|🍌 Add 12 ripe bananas and 3 litres jaggery water and stir for 15 days.
h.panch.5|🌱 3% દ્રાવણ (100 લિટર પાણીમાં 3 લિટર) પાક પર છાંટો.|🌱 3% घोल (100 लीटर पानी में 3 लीटर) फसल पर छिड़कें।|🌱 Spray a 3% solution (3 litres in 100 litres water) on the crop.
h.ghan.t|🧱 ઘન જીવામૃત|🧱 घन जीवामृत|🧱 Ghan Jeevamrut
h.ghan.1|🐄 100 kg સૂકું છાણ છાંયડામાં પાથરો.|🐄 100 kg सूखा गोबर छाया में बिछाएं।|🐄 Spread 100 kg dry dung in shade.
h.ghan.2|🍯 પ્રવાહી જીવામૃત 10 લિટર ગોળ અને ચણાનો લોટ સાથે ભેળવો.|🍯 10 लीटर तरल जीवामृत गुड़ और बेसन के साथ मिलाएं।|🍯 Mix 10 litres liquid jeevamrut with jaggery and gram flour.
h.ghan.3|✋ હાથથી ગોળા બનાવી બોરીથી ઢાંકી 48 કલાક રાખો.|✋ हाथ से गोले बनाकर बोरी से ढक 48 घंटे रखें।|✋ Make lumps by hand cover with a sack and keep 48 hours.
h.ghan.4|☀️ છાંયડામાં સૂકવી ભૂકો કરો અને કોથળામાં ભરો.|☀️ छाया में सुखाकर चूर्ण करें और बोरी में भरें।|☀️ Dry in shade crush and fill in bags.
h.ghan.5|🌾 વાવેતર વખતે 100-200 kg પ્રતિ એકર આપો.|🌾 बुवाई पर 100-200 kg प्रति एकड़ दें।|🌾 Apply 100-200 kg per acre at sowing.
h.neemark.t|🌿 નીમ અર્ક|🌿 नीम अर्क|🌿 Neem extract
h.neemark.1|🍃 5 kg લીમડાના પાન વાટી લો.|🍃 5 kg नीम की पत्तियां पीस लें।|🍃 Grind 5 kg neem leaves.
h.neemark.2|💧 10 લિટર પાણીમાં ભેળવી રાતભર રાખો.|💧 10 लीटर पानी में मिलाकर रात भर रखें।|💧 Mix in 10 litres water and keep overnight.
h.neemark.3|🧵 કપડાથી ગાળી લો અને 1 ml સાબુ ઉમેરો.|🧵 कपड़े से छानें और 1 ml साबुन मिलाएं।|🧵 Strain through cloth and add 1 ml soap.
h.neemark.4|🌅 100 લિટર પાણીમાં 10 લિટર અર્ક ભેળવો અને સાંજે છાંટો.|🌅 100 लीटर पानी में 10 लीटर अर्क मिलाएं और शाम को छिड़कें।|🌅 Mix 10 litres extract in 100 litres water and spray in the evening.
h.neemark.5|🔁 દર 10 દિવસે ફરી છાંટો.|🔁 हर 10 दिन पर दोबारा छिड़कें।|🔁 Repeat every 10 days.
h.dash.t|🍃 દશપર્ણી અર્ક|🍃 दशपर्णी अर्क|🍃 Dashaparni extract
h.dash.1|🌿 10 પ્રકારના કડવા પાન 5 kg ભેગા કરો.|🌿 10 प्रकार के कड़वे पत्ते 5 kg इकट्ठा करें।|🌿 Collect 5 kg of 10 kinds of bitter leaves.
h.dash.2|🐄 ગૌમૂત્ર 5 લિટર અને છાણ 2 kg ઉમેરો.|🐄 गौमूत्र 5 लीटर और गोबर 2 kg मिलाएं।|🐄 Add 5 litres cow urine and 2 kg dung.
h.dash.3|🧄 લસણ અને તીખાં મરચાં વાટીને ભેળવો.|🧄 लहसुन और तीखी मिर्च पीसकर मिलाएं।|🧄 Add ground garlic and hot chilli.
h.dash.4|🛢️ ડ્રમમાં ઢાંકીને 30 દિવસ આથો આવવા દો રોજ હલાવો.|🛢️ ड्रम में ढककर 30 दिन किण्वन होने दें रोज़ हिलाएं।|🛢️ Ferment covered in a drum for 30 days stirring daily.
h.dash.5|💦 ગાળીને 100 લિટર પાણીમાં 3 લિટર ભેળવી છાંટો.|💦 छानकर 100 लीटर पानी में 3 लीटर मिलाकर छिड़कें।|💦 Strain and spray 3 litres in 100 litres water.
h.agni.t|🔥 અગ્નિઅસ્ત્ર|🔥 अग्निअस्त्र|🔥 Agniastra
h.agni.1|🐄 20 લિટર ગૌમૂત્ર લો.|🐄 20 लीटर गौमूत्र लें।|🐄 Take 20 litres cow urine.
h.agni.2|🌿 1 kg તમાકુ પાન 500 g તીખાં મરચાં અને 250 g લસણ વાટી ઉમેરો.|🌿 1 kg तंबाकू पत्ती 500 g तीखी मिर्च और 250 g लहसुन पीसकर मिलाएं।|🌿 Add 1 kg tobacco leaf 500 g hot chilli and 250 g crushed garlic.
h.agni.3|🔥 ધીમા તાપે 4-5 ઉભરા સુધી ઉકાળો.|🔥 धीमी आंच पर 4-5 उबाल तक पकाएं।|🔥 Boil on low heat until 4-5 boils.
h.agni.4|🌙 48 કલાક રાખી કપડાથી ગાળો.|🌙 48 घंटे रखकर कपड़े से छानें।|🌙 Keep 48 hours and strain through cloth.
h.agni.5|💦 100 લિટર પાણીમાં 3 લિટર ભેળવી ઈયળ પર છાંટો.|💦 100 लीटर पानी में 3 लीटर मिलाकर इल्ली पर छिड़कें।|💦 Spray 3 litres in 100 litres water on caterpillars.
h.garlic.t|🧄 લસણ મરચી અર્ક|🧄 लहसुन मिर्च अर्क|🧄 Garlic chilli extract
h.garlic.1|🧄 500 g લસણ વાટી 1 લિટર પાણીમાં રાતભર પલાળો.|🧄 500 g लहसुन पीसकर 1 लीटर पानी में रात भर भिगोएं।|🧄 Soak 500 g crushed garlic in 1 litre water overnight.
h.garlic.2|🌶️ 500 g તીખાં મરચાં વાટી અલગ પલાળો.|🌶️ 500 g तीखी मिर्च पीसकर अलग भिगोएं।|🌶️ Soak 500 g ground hot chilli separately.
h.garlic.3|🥣 બંને ભેળવી ગાળી 20 ml સાબુ નાખો.|🥣 दोनों मिलाकर छानें और 20 ml साबुन डालें।|🥣 Mix both strain and add 20 ml soap.
h.garlic.4|💧 15 લિટર પંપમાં 250 ml અર્ક નાખો.|💧 15 लीटर पंप में 250 ml अर्क डालें।|💧 Put 250 ml extract in a 15 litre pump.
h.garlic.5|🌅 સાંજે છાંટો અને 7 દિવસે ફરી કરો.|🌅 शाम को छिड़कें और 7 दिन पर दोबारा करें।|🌅 Spray in the evening and repeat after 7 days.
h.nursery.t|🌱 નર્સરી તૈયાર કરો|🌱 नर्सरी तैयार करें|🌱 Raise a nursery
h.nursery.1|🧱 1 મીટર પહોળા અને 15 સેમી ઊંચા ઉભા ક્યારા બનાવો.|🧱 1 मीटर चौड़ी और 15 सेमी ऊंची उठी क्यारियां बनाएं।|🧱 Make raised beds 1 m wide and 15 cm high.
h.nursery.2|🌿 સડેલું છાણિયું ખાતર અને રેતી ભેળવો.|🌿 सड़ी गोबर खाद और रेत मिलाएं।|🌿 Mix rotted farmyard manure and sand.
h.nursery.3|🌰 બીજને દવાનો પટ આપી 5 સેમી અંતરે લાઈનમાં વાવો.|🌰 बीज को दवा का उपचार देकर 5 सेमी दूरी पर कतार में बोएं।|🌰 Treat seed and sow in lines 5 cm apart.
h.nursery.4|🌾 ઘાસથી ઢાંકી રોજ ઝારીથી હળવું પાણી આપો.|🌾 घास से ढककर रोज़ झारी से हल्का पानी दें।|🌾 Cover with straw and water lightly daily with a can.
h.nursery.5|✅ 25-30 દિવસે મજબૂત છોડ સાંજે ખેતરમાં રોપો.|✅ 25-30 दिन में मज़बूत पौधे शाम को खेत में रोपें।|✅ Transplant strong seedlings in the evening at 25-30 days.
h.graft.t|✂️ ગ્રાફ્ટિંગ કરો|✂️ ग्राफ्टिंग करें|✂️ Do grafting
h.graft.1|🌳 સ્વસ્થ મૂળકાંડ (રૂટસ્ટોક) અને સારી જાતની ડાળી પસંદ કરો.|🌳 स्वस्थ मूलवृंत (रूटस्टॉक) और अच्छी किस्म की डाली चुनें।|🌳 Select a healthy rootstock and a good variety scion.
h.graft.2|🔪 તીક્ષ્ણ છરીથી 4 સેમી લાંબો ત્રાંસો કાપ મૂકો.|🔪 तेज़ चाकू से 4 सेमी लंबा तिरछा कट लगाएं।|🔪 Make a 4 cm slanting cut with a sharp knife.
h.graft.3|🔗 બંને કાપ બરાબર જોડો.|🔗 दोनों कट ठीक से जोड़ें।|🔗 Join both cuts neatly.
h.graft.4|🎗️ પ્લાસ્ટિક પટ્ટીથી કસીને બાંધો.|🎗️ प्लास्टिक पट्टी से कसकर बांधें।|🎗️ Tie tightly with plastic tape.
h.graft.5|💧 છાંયડામાં રાખી 30 દિવસે નવી કૂંપળ આવે ત્યારે પટ્ટી કાઢો.|💧 छाया में रखकर 30 दिन में नई कोंपल आने पर पट्टी हटाएं।|💧 Keep in shade and remove tape when new shoots come after 30 days.
h.mulch.t|🌾 મલ્ચિંગ કરો|🌾 मल्चिंग करें|🌾 Do mulching
h.mulch.1|🪨 ખેતરની સપાટી સાફ કરી પિયત આપો.|🪨 खेत की सतह साफ कर सिंचाई दें।|🪨 Clean the field surface and irrigate.
h.mulch.2|🌾 સૂકા પાંદડાં ઘાસ અથવા પાકના અવશેષ 5 સેમી પાથરો.|🌾 सूखे पत्ते घास या फसल अवशेष 5 सेमी बिछाएं।|🌾 Spread 5 cm of dry leaves grass or crop residue.
h.mulch.3|⬛ અથવા પ્લાસ્ટિક મલ્ચ ફિલ્મ પાથરી કિનારે માટી દબાવો.|⬛ या प्लास्टिक मल्च फिल्म बिछाकर किनारे मिट्टी दबाएं।|⬛ Or lay plastic mulch film and press soil on the edges.
h.mulch.4|🕳️ છોડની જગ્યાએ કાણાં પાડી રોપણી કરો.|🕳️ पौधे की जगह छेद कर रोपाई करें।|🕳️ Punch holes at plant spots and transplant.
h.mulch.5|✅ ભેજ બચે નીંદણ ઘટે અને 25% પાણી બચે છે.|✅ नमी बचती है खरपतवार घटता है और 25% पानी बचता है।|✅ It saves moisture cuts weeds and saves 25% water.
h.drip.t|💧 ટપક સિંચાઈ ગોઠવો|💧 ड्रिप सिंचाई लगाएं|💧 Set up drip irrigation
h.drip.1|🚰 પંપ સાથે ફિલ્ટર અને પ્રેશર ગેજ જોડો.|🚰 पंप के साथ फ़िल्टर और प्रेशर गेज जोड़ें।|🚰 Connect a filter and pressure gauge to the pump.
h.drip.2|🟫 મુખ્ય અને સબ-મેઈન પાઈપ ખેતરમાં પાથરો.|🟫 मुख्य और सब-मेन पाइप खेत में बिछाएं।|🟫 Lay main and sub-main pipes in the field.
h.drip.3|➖ દરેક લાઈનમાં ડ્રિપ લેટરલ પાથરો અને ડ્રિપર છોડ પાસે રાખો.|➖ हर कतार में ड्रिप लेटरल बिछाएं और ड्रिपर पौधे के पास रखें।|➖ Lay a drip lateral along each row with drippers near plants.
h.drip.4|🔧 લીકેજ તપાસી પાઈપના છેડા બંધ કરો.|🔧 रिसाव जांचकर पाइप के सिरे बंद करें।|🔧 Check leaks and close the pipe ends.
h.drip.5|🧪 ફિલ્ટર સાફ રાખો અને દ્રાવ્ય ખાતર ટપક દ્વારા આપો.|🧪 फ़िल्टर साफ रखें और घुलनशील खाद ड्रिप से दें।|🧪 Keep the filter clean and give soluble fertilizer through drip.
h.seedtreat.t|🌰 બીજ માવજત|🌰 बीज उपचार|🌰 Seed treatment
h.seedtreat.1|🪣 બીજને સ્વચ્છ ટબમાં લો.|🪣 बीज को साफ टब में लें।|🪣 Take seed in a clean tub.
h.seedtreat.2|🧪 પ્રતિ કિલો બીજ 4 g ટ્રાઇકોડર્મા ભેળવો.|🧪 प्रति किलो बीज 4 g ट्राइकोडर्मा मिलाएं।|🧪 Mix 4 g Trichoderma per kg of seed.
h.seedtreat.3|🥣 થોડું ગોળનું પાણી છાંટી બીજ પર પટ ચડાવો.|🥣 थोड़ा गुड़ का पानी छिड़ककर बीज पर परत चढ़ाएं।|🥣 Sprinkle a little jaggery water to coat the seed.
h.seedtreat.4|🌥️ છાંયડામાં 30 મિનિટ સૂકવો.|🌥️ छाया में 30 मिनट सुखाएं।|🌥️ Dry in shade for 30 minutes.
h.seedtreat.5|✅ તે જ દિવસે વાવેતર કરો.|✅ उसी दिन बुवाई करें।|✅ Sow on the same day.
h.sample.t|🪴 જમીનનો નમૂનો લો|🪴 मिट्टी का नमूना लें|🪴 Take a soil sample
h.sample.1|🗺️ ખેતરમાં ઝિગ-ઝેગ રીતે 8-10 જગ્યા પસંદ કરો.|🗺️ खेत में ज़िग-ज़ैग तरीके से 8-10 जगह चुनें।|🗺️ Choose 8-10 spots in a zig-zag pattern.
h.sample.2|⛏️ દરેક જગ્યાએ ઉપરનું ઘાસ હટાવી 15 સેમી ઊંડો V આકારનો ખાડો કરો.|⛏️ हर जगह ऊपर की घास हटाकर 15 सेमी गहरा V आकार का गड्ढा करें।|⛏️ Remove surface grass and dig a 15 cm deep V-shaped hole.
h.sample.3|🥄 બાજુમાંથી એક સરખી માટીની પટ્ટી કાપો.|🥄 किनारे से एक समान मिट्टी की पट्टी काटें।|🥄 Cut an even slice of soil from the side.
h.sample.4|🪣 બધી માટી ભેળવી ચાર ભાગ કરી અડધો કિલો રાખો.|🪣 सारी मिट्टी मिलाकर चार भाग कर आधा किलो रखें।|🪣 Mix all soil quarter it and keep half a kg.
h.sample.5|🏷️ કોથળીમાં ભરી નામ અને ખેતર નંબર લખી પ્રયોગશાળામાં આપો.|🏷️ थैली में भरकर नाम और खेत नंबर लिखकर प्रयोगशाला में दें।|🏷️ Bag it label with name and field number and give it to the lab.
# ---- pests ----
pest.1.n|🐛 મોલો (એફિડ)|🐛 माहू (एफिड)|🐛 Aphid
pest.1.d|નાના લીલા-કાળા કીડા પાનનો રસ ચૂસે છે પાન વળી જાય અને ચીકણા થાય.|छोटे हरे-काले कीड़े पत्तों का रस चूसते हैं पत्ते मुड़ जाते हैं और चिपचिपे होते हैं।|Tiny green-black insects suck sap leaves curl and turn sticky.
pest.1.c|🌿 નીમ તેલ 5 ml/L અને પીળા ચીકણા પિંજર લગાવો;; 🧪 થાયામેથોક્સામ 0.3 g/L|🌿 नीम तेल 5 ml/L और पीले चिपचिपे ट्रैप लगाएं;; 🧪 थायामेथोक्साम 0.3 g/L|🌿 Neem oil 5 ml/L and yellow sticky traps;; 🧪 Thiamethoxam 0.3 g/L
pest.2.n|🦟 સફેદ માખી|🦟 सफेद मक्खी|🦟 Whitefly
pest.2.d|પાનની નીચે રહી રસ ચૂસે છે અને પાન પીળા પડે; વાઈરસ ફેલાવે છે.|पत्ते के नीचे रहकर रस चूसती है पत्ते पीले पड़ते हैं; वायरस फैलाती है।|Lives under leaves sucks sap leaves yellow; spreads virus.
pest.2.c|🌿 પીળા ચીકણા પિંજર અને નીમ અર્ક;; 🧪 ડાયફેન્થિયુરોન 1 g/L|🌿 पीले चिपचिपे ट्रैप और नीम अर्क;; 🧪 डायफेंथियूरोन 1 g/L|🌿 Yellow sticky traps and neem extract;; 🧪 Diafenthiuron 1 g/L
pest.3.n|🐛 ગુલાબી ઈયળ (કપાસ)|🐛 गुलाबी सुंडी (कपास)|🐛 Pink bollworm
pest.3.d|જીંડવા અંદરથી કોરી ખાય છે અને રૂ બગડે છે.|टिंडे अंदर से खाती है और रुई खराब होती है।|Eats bolls from inside and spoils the lint.
pest.3.c|🌿 ફેરોમોન ટ્રેપ 5 પ્રતિ એકર અને નીમ અર્ક;; 🧪 સાયપરમેથ્રિન 1 ml/L|🌿 फेरोमोन ट्रैप 5 प्रति एकड़ और नीम अर्क;; 🧪 साइपरमेथ्रिन 1 ml/L|🌿 5 pheromone traps per acre and neem extract;; 🧪 Cypermethrin 1 ml/L
pest.4.n|🐛 લશ્કરી ઈયળ (મકાઈ)|🐛 फॉल आर्मीवर्म (मक्का)|🐛 Fall armyworm
pest.4.d|પાનની પૂંછડીમાં રહી પાન કોરે છે અને ગભામાં ઘૂસે છે.|पौधे के भुट्टे की गांठ में रहकर पत्ते खाती है और भुट्टे में घुसती है।|Hides in the whorl chews leaves and enters the cob.
pest.4.c|🌿 રેતી-ચૂનો ભેળવી પૂંછડીમાં નાખો અને ફેરોમોન ટ્રેપ;; 🧪 ઈમામેક્ટિન 0.4 g/L|🌿 रेत-चूना मिलाकर पौधे की गांठ में डालें और फेरोमोन ट्रैप;; 🧪 इमामेक्टिन 0.4 g/L|🌿 Put sand-lime mix in the whorl and pheromone traps;; 🧪 Emamectin 0.4 g/L
pest.5.n|🦗 થ્રિપ્સ|🦗 थ्रिप्स|🦗 Thrips
pest.5.d|પાનની ધાર ચાંદી જેવી થાય અને પાન ઉપર વળે છે.|पत्ते की धार चांदी जैसी हो जाती है और पत्ते ऊपर मुड़ते हैं।|Leaf edges turn silvery and leaves curl upward.
pest.5.c|🌿 વાદળી ચીકણા પિંજર અને નીમ તેલ;; 🧪 સ્પિનોસેડ 0.3 ml/L|🌿 नीले चिपचिपे ट्रैप और नीम तेल;; 🧪 स्पिनोसैड 0.3 ml/L|🌿 Blue sticky traps and neem oil;; 🧪 Spinosad 0.3 ml/L
pest.6.n|🕷️ લાલ કથીરી (માઈટ્સ)|🕷️ लाल मकड़ी (माइट्स)|🕷️ Red mites
pest.6.d|ગરમ સૂકા હવામાનમાં પાનની નીચે જાળાં અને ટપકાં થાય.|गर्म सूखे मौसम में पत्ते के नीचे जाले और धब्बे बनते हैं।|In hot dry weather webs and spots appear under leaves.
pest.6.c|🌿 પાણીનો ફુવારો અને નીમ તેલ;; 🧪 વેટેબલ સલ્ફર 2.5 g/L|🌿 पानी का फव्वारा और नीम तेल;; 🧪 वेटेबल सल्फर 2.5 g/L|🌿 Water spray and neem oil;; 🧪 Wettable sulphur 2.5 g/L
pest.7.n|🪲 થડ છિદ્રક (સ્ટેમ બોરર)|🪲 तना छेदक (स्टेम बोरर)|🪲 Stem borer
pest.7.d|ડૂંખ સુકાય છે અને છોડ સહેલાઈથી ખેંચાઈ આવે છે.|गोभ सूखती है और पौधा आसानी से खिंच जाता है।|Central shoot dries and the plant pulls out easily.
pest.7.c|🌿 ટ્રાઇકોકાર્ડ 2 પ્રતિ એકર અને સૂકી ડૂંખ કાઢો;; 🧪 ક્લોરેન્ટ્રાનિલિપ્રોલ 0.3 ml/L|🌿 ट्राइकोकार्ड 2 प्रति एकड़ और सूखी गोभ निकालें;; 🧪 क्लोरेंट्रानिलिप्रोल 0.3 ml/L|🌿 2 trichocards per acre and remove dried shoots;; 🧪 Chlorantraniliprole 0.3 ml/L
pest.8.n|🍅 ફળ છિદ્રક (ફ્રૂટ બોરર)|🍅 फल छेदक (फ्रूट बोरर)|🍅 Fruit borer
pest.8.d|ફળમાં કાણું પાડી અંદર ખાય છે અને ફળ સડે છે.|फल में छेद कर अंदर खाती है और फल सड़ता है।|Bores into fruit and eats inside fruit rots.
pest.8.c|🌿 ફેરોમોન ટ્રેપ અને નીમ અર્ક;; 🧪 ઈન્ડોક્સાકાર્બ 1 ml/L|🌿 फेरोमोन ट्रैप और नीम अर्क;; 🧪 इंडोक्साकार्ब 1 ml/L|🌿 Pheromone traps and neem extract;; 🧪 Indoxacarb 1 ml/L
# ---- diseases ----
dis.1.n|⚪ ભૂકી છારો (પાવડરી માઈલ્ડ્યુ)|⚪ चूर्णिल आसिता (पाउडरी मिल्ड्यू)|⚪ Powdery mildew
dis.1.d|પાન પર સફેદ ભૂકી જેવું પડ જામે છે.|पत्तों पर सफेद चूर्ण जैसी परत जम जाती है।|A white powdery coating forms on leaves.
dis.1.c|🌿 છાશ 1 લિટર + 10 લિટર પાણી;; 🧪 વેટેબલ સલ્ફર 2.5 g/L અથવા હેક્ઝાકોનાઝોલ 1 ml/L|🌿 छाछ 1 लीटर + 10 लीटर पानी;; 🧪 वेटेबल सल्फर 2.5 g/L या हेक्साकोनाज़ोल 1 ml/L|🌿 Buttermilk 1 litre + 10 litres water;; 🧪 Wettable sulphur 2.5 g/L or hexaconazole 1 ml/L
dis.2.n|🟣 તળછારો (ડાઉની માઈલ્ડ્યુ)|🟣 मृदुरोमिल आसिता (डाउनी मिल्ड्यू)|🟣 Downy mildew
dis.2.d|પાનની ઉપર પીળા ધબ્બા અને નીચે રાખોડી ફૂગ.|पत्ते के ऊपर पीले धब्बे और नीचे धूसर फफूंद।|Yellow spots on top and grey mould underneath.
dis.2.c|🌿 જૈવિક સ્યુડોમોનાસ 5 g/L;; 🧪 ફોસેટાઇલ એલ્યુમિનિયમ 2 g/L|🌿 जैविक स्यूडोमोनास 5 g/L;; 🧪 फोसेटाइल एल्युमिनियम 2 g/L|🌿 Bio Pseudomonas 5 g/L;; 🧪 Fosetyl-Al 2 g/L
dis.3.n|🟠 ગેરુ (રસ્ટ)|🟠 रतुआ (रस्ट)|🟠 Rust
dis.3.d|પાન અને થડ પર નારંગી-કથ્થઈ ગેરુ જેવા ટપકાં.|पत्ते और तने पर नारंगी-भूरे रतुए जैसे धब्बे।|Orange-brown rust-like pustules on leaves and stems.
dis.3.c|🌿 પ્રતિકારક જાત વાવો;; 🧪 પ્રોપિકોનાઝોલ 1 ml/L|🌿 प्रतिरोधी किस्म बोएं;; 🧪 प्रोपिकोनाज़ोल 1 ml/L|🌿 Sow resistant varieties;; 🧪 Propiconazole 1 ml/L
dis.4.n|🥀 સુકારો (વિલ્ટ)|🥀 उकठा (विल्ट)|🥀 Wilt
dis.4.d|છોડ અચાનક કરમાઈ જાય છે અને થડ કાપતા અંદર કાળાશ દેખાય છે.|पौधा अचानक मुरझा जाता है और तना काटने पर अंदर कालापन दिखता है।|Plants suddenly wilt and the stem shows browning inside.
dis.4.c|🌿 ટ્રાઇકોડર્મા 5 g/L ડ્રેન્ચિંગ અને પાક ફેરબદલી;; 🧪 થાયોફેનેટ મિથાઈલ 1 g/L|🌿 ट्राइकोडर्मा 5 g/L ड्रेंचिंग और फसल चक्र;; 🧪 थायोफेनेट मिथाइल 1 g/L|🌿 Trichoderma 5 g/L drenching and crop rotation;; 🧪 Thiophanate methyl 1 g/L
dis.5.n|🍂 ઝાળ (બ્લાઈટ)|🍂 झुलसा (ब्लाइट)|🍂 Blight
dis.5.d|પાન પર ભૂરાં ધબ્બા ઝડપથી મોટા થઈ પાન સુકાવે છે.|पत्तों पर भूरे धब्बे तेज़ी से बढ़कर पत्ते सुखा देते हैं।|Brown spots spread fast and dry the leaves.
dis.5.c|🌿 રોગિષ્ઠ પાન કાઢી નાખો;; 🧪 એઝોક્સીસ્ટ્રોબિન 1 ml/L અથવા કોપર હાઇડ્રોક્સાઇડ 2 g/L|🌿 रोगी पत्ते हटा दें;; 🧪 एज़ोक्सीस्ट्रोबिन 1 ml/L या कॉपर हाइड्रोक्साइड 2 g/L|🌿 Remove infected leaves;; 🧪 Azoxystrobin 1 ml/L or copper hydroxide 2 g/L
dis.6.n|🟤 પાનના ટપકાં (લીફ સ્પોટ)|🟤 पत्ती धब्बा (लीफ स्पॉट)|🟤 Leaf spot
dis.6.d|પાન પર ગોળ ભૂરાં ટપકાં અને ફરતે પીળી કિનારી.|पत्तों पर गोल भूरे धब्बे और चारों ओर पीला किनारा।|Round brown spots with a yellow halo on leaves.
dis.6.c|🌿 નીમ અર્ક અને ખેતર સ્વચ્છ રાખો;; 🧪 ટેબ્યુકોનાઝોલ 1 ml/L|🌿 नीम अर्क और खेत साफ रखें;; 🧪 टेबुकोनाज़ोल 1 ml/L|🌿 Neem extract and keep the field clean;; 🧪 Tebuconazole 1 ml/L
dis.7.n|🌱 મૂળ સડો|🌱 जड़ सड़न|🌱 Root rot
dis.7.d|પાણી ભરાવાથી મૂળ કાળા થઈ સડે છે અને છોડ પીળો પડે છે.|पानी भरने से जड़ें काली होकर सड़ती हैं और पौधा पीला पड़ता है।|Waterlogging turns roots black and rotten and plants yellow.
dis.7.c|🌿 પાણીનો નિકાલ અને ટ્રાઇકોડર્મા;; 🧪 થાયોફેનેટ મિથાઈલ 1 g/L ડ્રેન્ચિંગ|🌿 जल निकास और ट्राइकोडर्मा;; 🧪 थायोफेनेट मिथाइल 1 g/L ड्रेंचिंग|🌿 Drain water and use Trichoderma;; 🧪 Thiophanate methyl 1 g/L drench
dis.8.n|🟡 પીળો પંજો (મોઝેક વાઈરસ)|🟡 पीला मोज़ेक वायरस|🟡 Yellow mosaic virus
dis.8.d|પાન પર પીળા-લીલા ચટાપટા અને છોડ ઠીંગણા રહે છે.|पत्तों पर पीले-हरे धारियां और पौधे बौने रहते हैं।|Yellow-green mottling on leaves and stunted plants.
dis.8.c|🌿 રોગિષ્ઠ છોડ ઉખાડી બાળો અને સફેદ માખી કાબૂમાં રાખો;; 🧪 ડાયફેન્થિયુરોન 1 g/L|🌿 रोगी पौधे उखाड़कर जलाएं और सफेद मक्खी नियंत्रित करें;; 🧪 डायफेंथियूरोन 1 g/L|🌿 Uproot and burn infected plants and control whitefly;; 🧪 Diafenthiuron 1 g/L
# ---- static guide pages ----
s.soil.1.h|🏜️ કાળી જમીન|🏜️ काली मिट्टी|🏜️ Black soil
s.soil.1.b|ભેજ સાચવે છે;; કપાસ મગફળી ઘઉં માટે સારી;; ભીની હોય ત્યારે ચીકણી થાય માટે ખેડ યોગ્ય સમયે કરો|नमी संभालती है;; कपास मूंगफली गेहूं के लिए अच्छी;; गीली होने पर चिपचिपी होती है इसलिए जुताई सही समय पर करें|Holds moisture;; good for cotton groundnut wheat;; sticky when wet so plough at the right time
s.soil.2.h|🏖️ રેતાળ જમીન|🏖️ रेतीली मिट्टी|🏖️ Sandy soil
s.soil.2.b|પાણી ઝડપથી નીકળી જાય;; બાજરી તલ કઠોળ માટે યોગ્ય;; છાણિયું ખાતર અને ટપક સિંચાઈ વાપરો|पानी जल्दी निकल जाता है;; बाजरा तिल दलहन के लिए उपयुक्त;; गोबर खाद और ड्रिप सिंचाई उपयोग करें|Drains fast;; suited to bajra sesame pulses;; use manure and drip irrigation
s.soil.3.h|🌊 ગોરાડુ કાંપની જમીન|🌊 दोमट जलोढ़ मिट्टी|🌊 Loam alluvial soil
s.soil.3.b|સૌથી સારી ફળદ્રુપ જમીન;; ઘઉં તમાકુ શાકભાજી કેળા માટે;; નિયમિત ખાતર આપો|सबसे अच्छी उपजाऊ मिट्टी;; गेहूं तंबाकू सब्ज़ी केला के लिए;; नियमित खाद दें|Best fertile soil;; for wheat tobacco vegetables banana;; apply manure regularly
s.soil.4.h|🧂 ક્ષારીય જમીન|🧂 खारी मिट्टी|🧂 Saline soil
s.soil.4.b|સફેદ પોપડી દેખાય;; જિપ્સમ અને લીલા પડવાશ કરો;; ક્ષાર સહનશીલ પાક જેમ કે જવ ખજૂર વાવો|सफेद परत दिखती है;; जिप्सम और हरी खाद करें;; नमक सहनशील फसल जैसे जौ खजूर बोएं|White crust appears;; use gypsum and green manure;; grow salt-tolerant crops like barley and date palm
s.irr.1.h|💧 પાટ (ક્યારા) પિયત|💧 क्यारी सिंचाई|💧 Flood irrigation
s.irr.1.b|સસ્તું અને સરળ;; પાણીનો બગાડ વધુ;; સમતળ જમીનમાં જ વાપરો|सस्ती और आसान;; पानी की बर्बादी ज़्यादा;; समतल ज़मीन में ही उपयोग करें|Cheap and simple;; wastes more water;; use only on levelled land
s.irr.2.h|🌧️ ફુવારા સિંચાઈ|🌧️ फव्वारा सिंचाई|🌧️ Sprinkler irrigation
s.irr.2.b|30% પાણી બચે;; ઘઉં ચણા મગફળી માટે સારી;; પવન ઓછો હોય ત્યારે ચલાવો|30% पानी बचता है;; गेहूं चना मूंगफली के लिए अच्छी;; हवा कम हो तब चलाएं|Saves 30% water;; good for wheat gram groundnut;; run when wind is low
s.irr.3.h|🚰 ટપક સિંચાઈ|🚰 ड्रिप सिंचाई|🚰 Drip irrigation
s.irr.3.b|50-60% પાણી બચે;; શાકભાજી ફળ કપાસ માટે શ્રેષ્ઠ;; દ્રાવ્ય ખાતર સાથે આપી શકાય|50-60% पानी बचता है;; सब्ज़ी फल कपास के लिए सर्वोत्तम;; घुलनशील खाद के साथ दे सकते हैं|Saves 50-60% water;; best for vegetables fruits cotton;; can be used with soluble fertilizer
s.org.1.h|🌱 શરૂઆત કેવી રીતે કરવી|🌱 शुरुआत कैसे करें|🌱 How to start
s.org.1.b|નાના ખેતરથી શરૂ કરો;; રાસાયણિક ખાતર અને દવા ધીમે ધીમે બંધ કરો;; છાણિયું ખાતર અને જીવામૃત વાપરો|छोटे खेत से शुरू करें;; रासायनिक खाद और दवा धीरे धीरे बंद करें;; गोबर खाद और जीवामृत उपयोग करें|Start with a small plot;; phase out chemical fertilizer and sprays slowly;; use manure and jeevamrut
s.org.2.h|🌿 જમીન સુધારણા|🌿 मिट्टी सुधार|🌿 Soil building
s.org.2.b|લીલો પડવાશ (ઢેંચા શણ) કરો;; પાક ફેરબદલી રાખો;; મલ્ચિંગ કરો|हरी खाद (ढैंचा सनई) करें;; फसल चक्र रखें;; मल्चिंग करें|Grow green manure (dhaincha sunn hemp);; rotate crops;; use mulch
s.org.3.h|🛡️ જીવાત રોગ નિયંત્રણ|🛡️ कीट रोग नियंत्रण|🛡️ Pest and disease control
s.org.3.b|નીમ અર્ક દશપર્ણી અગ્નિઅસ્ત્ર વાપરો;; ફેરોમોન અને ચીકણા પિંજર લગાવો;; મિત્ર કીટકો બચાવો|नीम अर्क दशपर्णी अग्निअस्त्र उपयोग करें;; फेरोमोन और चिपचिपे ट्रैप लगाएं;; मित्र कीटों को बचाएं|Use neem extract dashaparni agniastra;; set pheromone and sticky traps;; protect friendly insects
s.org.4.h|📜 પ્રમાણપત્ર|📜 प्रमाणन|📜 Certification
s.org.4.b|3 વર્ષ રાસાયણિક વગર ખેતી જરૂરી;; ખેતીનો હિસાબ અને ડાયરી રાખો;; માન્ય સંસ્થા પાસે નોંધણી કરાવો|3 साल बिना रसायन खेती ज़रूरी;; खेती का हिसाब और डायरी रखें;; मान्य संस्था में पंजीकरण कराएं|3 years without chemicals are needed;; keep farm accounts and diary;; register with an accredited agency
s.safe.1.h|😷 છંટકાવ પહેલાં|😷 छिड़काव से पहले|😷 Before spraying
s.safe.1.b|મોજા માસ્ક ચશ્મા અને પૂરી બાંયના કપડાં પહેરો;; લેબલ ધ્યાનથી વાંચો;; પંપ લીકેજ તપાસો|दस्ताने मास्क चश्मा और पूरी बांह के कपड़े पहनें;; लेबल ध्यान से पढ़ें;; पंप का रिसाव जांचें|Wear gloves mask goggles and full sleeves;; read the label carefully;; check the pump for leaks
s.safe.2.h|🌬️ છંટકાવ વખતે|🌬️ छिड़काव के समय|🌬️ While spraying
s.safe.2.b|પવનની દિશામાં છાંટો;; સવાર કે સાંજે છાંટો;; ખાવું પીવું કે ધૂમ્રપાન ન કરો|हवा की दिशा में छिड़कें;; सुबह या शाम छिड़कें;; खाना पीना या धूम्रपान न करें|Spray downwind;; spray in morning or evening;; do not eat drink or smoke
s.safe.3.h|🧼 છંટકાવ પછી|🧼 छिड़काव के बाद|🧼 After spraying
s.safe.3.b|સાબુથી હાથ મોઢું નહાવ;; કપડાં અલગ ધોવો;; ખાલી ડબ્બા તોડી જમીનમાં દાટી દો|साबुन से हाथ मुंह नहाएं;; कपड़े अलग धोएं;; खाली डिब्बे तोड़कर ज़मीन में दबाएं|Wash hands face and bathe with soap;; wash clothes separately;; crush empty containers and bury them
s.safe.4.h|🚑 ઝેર ચડે તો|🚑 ज़हर चढ़े तो|🚑 In case of poisoning
s.safe.4.b|દર્દીને તાજી હવામાં લઈ જાઓ;; દૂષિત કપડાં કાઢો અને ત્વચા ધોવો;; દવાનું પેકેટ લઈ તરત હોસ્પિટલ જાઓ ઉલટી કરાવશો નહીં|मरीज़ को ताज़ी हवा में ले जाएं;; दूषित कपड़े उतारें और त्वचा धोएं;; दवा का पैकेट लेकर तुरंत अस्पताल जाएं उल्टी न कराएं|Move the patient to fresh air;; remove soiled clothes and wash skin;; take the pack and go to hospital at once do not induce vomiting
s.mach.1.h|🚜 ટ્રેક્ટર|🚜 ट्रैक्टर|🚜 Tractor
s.mach.1.b|ખેડ વાવણી અને પરિવહન માટે;; દર 250 કલાકે તેલ ફિલ્ટર બદલો;; ટાયરનું પ્રેશર તપાસો|जुताई बुवाई और परिवहन के लिए;; हर 250 घंटे पर तेल फ़िल्टर बदलें;; टायर का दबाव जांचें|For ploughing sowing and transport;; change oil and filter every 250 hours;; check tyre pressure
s.mach.2.h|🔱 કલ્ટીવેટર અને હળ|🔱 कल्टीवेटर और हल|🔱 Cultivator and plough
s.mach.2.b|હળથી ઊંડી ખેડ;; કલ્ટીવેટરથી ઉપરની માટી ભૂકો કરો;; પાટા ફેરવી સમતળ કરો|हल से गहरी जुताई;; कल्टीवेटर से ऊपरी मिट्टी भुरभुरी करें;; पाटा चलाकर समतल करें|Plough for deep tillage;; cultivator for fine top soil;; use a leveller to flatten
s.mach.3.h|🌰 સીડ ડ્રિલ|🌰 सीड ड्रिल|🌰 Seed drill
s.mach.3.b|બીજ એકસરખી ઊંડાઈ અને અંતરે વાવે;; 20% બીજ બચે;; દરેક વાવણી પહેલાં દર ગોઠવો|बीज एक समान गहराई और दूरी पर बोता है;; 20% बीज बचता है;; हर बुवाई से पहले दर सेट करें|Sows seed at even depth and spacing;; saves 20% seed;; set the rate before each sowing
s.mach.4.h|💦 પાવર સ્પ્રેયર|💦 पावर स्प्रेयर|💦 Power sprayer
s.mach.4.b|મોટા ખેતર માટે ઝડપી છંટકાવ;; દર ઉપયોગ પછી પાણીથી સાફ કરો;; નોઝલ સમયાંતરે બદલો|बड़े खेत के लिए तेज़ छिड़काव;; हर उपयोग के बाद पानी से साफ करें;; नोज़ल समय-समय पर बदलें|Fast spraying for big fields;; rinse with water after use;; replace nozzles regularly
s.mach.5.h|🌾 કમ્બાઈન હાર્વેસ્ટર અને થ્રેશર|🌾 कंबाइन हार्वेस्टर और थ्रेशर|🌾 Combine harvester and thresher
s.mach.5.b|કાપણી અને દાણા છૂટા પાડવાનું એકસાથે;; દાણાનો ભેજ 14% હોય ત્યારે કાપો;; મજૂરી અને સમય બચે|कटाई और दाना अलग करना एक साथ;; दाने की नमी 14% हो तब काटें;; मज़दूरी और समय बचता है|Cuts and threshes together;; harvest at 14% grain moisture;; saves labour and time
s.animal.1.h|🐄 દૂધાળા પશુનો ખોરાક|🐄 दुधारू पशु का चारा|🐄 Feeding milch animals
s.animal.1.b|લીલો ચારો સૂકો ચારો અને દાણ સંતુલિત આપો;; રોજ ખનિજ મિશ્રણ 50 g આપો;; સ્વચ્છ ઠંડું પાણી પાવો|हरा चारा सूखा चारा और दाना संतुलित दें;; रोज़ खनिज मिश्रण 50 g दें;; साफ ठंडा पानी पिलाएं|Give balanced green fodder dry fodder and concentrate;; give 50 g mineral mixture daily;; offer clean cool water
s.animal.2.h|💉 રસીકરણ|💉 टीकाकरण|💉 Vaccination
s.animal.2.b|ખરવા-મોવાસા રસી વર્ષમાં 2 વાર;; ગળસૂંઢો અને ગાંઠિયો તાવની રસી ચોમાસા પહેલાં;; રસીનો રેકોર્ડ રાખો|खुरपका-मुंहपका टीका साल में 2 बार;; गलघोंटू और लंगड़ी बुखार का टीका मानसून से पहले;; टीके का रिकॉर्ड रखें|FMD vaccine twice a year;; HS and BQ vaccines before monsoon;; keep a vaccination record
s.animal.3.h|🏠 રહેઠાણ|🏠 आवास|🏠 Housing
s.animal.3.b|હવાઉજાસવાળું સૂકું શેડ;; ફરસ ઢાળવાળું અને સાફ;; ગરમીમાં પંખા અને છાંયડો રાખો|हवादार सूखा शेड;; फर्श ढालदार और साफ;; गर्मी में पंखे और छाया रखें|Airy dry shed;; sloped clean floor;; fans and shade in summer
s.animal.4.h|🩺 બીમારીના ચિહ્નો|🩺 बीमारी के संकेत|🩺 Signs of illness
s.animal.4.b|ખાવાનું બંધ કરવું અને સુસ્તી;; તાવ અથવા દૂધ ઘટવું;; તરત પશુચિકિત્સકને બતાવો|खाना बंद करना और सुस्ती;; बुखार या दूध घटना;; तुरंत पशु चिकित्सक को दिखाएं|Stopped eating and dullness;; fever or drop in milk;; show a veterinarian at once
s.store.1.h|☀️ સૂકવણી|☀️ सुखाना|☀️ Drying
s.store.1.b|દાણો 12% ભેજ સુધી સૂકવો;; તાડપત્રી પર પાથરી ઉલટ-પલટ કરો;; કરડવાથી તૂટે તો બરાબર સુકાયો|दाना 12% नमी तक सुखाएं;; तिरपाल पर फैलाकर पलटते रहें;; दांत से काटने पर टूटे तो ठीक सूखा है|Dry grain to 12% moisture;; spread on a tarpaulin and turn;; if it snaps when bitten it is dry
s.store.2.h|📦 સંગ્રહ|📦 भंडारण|📦 Storage
s.store.2.b|સ્વચ્છ સૂકા કોથળા કે કોઠીમાં ભરો;; દીવાલથી દૂર લાકડાના પાટિયા પર મૂકો;; લીમડાના પાન ભેળવો|साफ सूखे बोरे या कोठी में भरें;; दीवार से दूर लकड़ी के पट्टों पर रखें;; नीम की पत्तियां मिलाएं|Fill clean dry bags or bins;; keep on wooden pallets away from walls;; mix in neem leaves
s.store.3.h|🐭 જીવાત અને ઉંદર|🐭 कीट और चूहे|🐭 Pests and rats
s.store.3.b|કોઠાર સાફ રાખો;; ઉંદરના દર બંધ કરો;; સંગ્રહ કરેલા દાણા દર મહિને તપાસો|गोदाम साफ रखें;; चूहों के बिल बंद करें;; भंडारित दाने हर महीने जांचें|Keep the godown clean;; close rat holes;; inspect stored grain monthly
s.store.4.h|💰 વેચાણ|💰 बिक्री|💰 Selling
s.store.4.b|પાકને ગ્રેડિંગ કરી વેચો;; બજાર ભાવ જોઈ યોગ્ય સમયે વેચો;; વેચાણની રસીદ સાચવો|फसल की ग्रेडिंग कर बेचें;; बाज़ार भाव देखकर सही समय पर बेचें;; बिक्री की रसीद संभालें|Grade the produce before selling;; sell at the right time after checking prices;; keep sale receipts
# ---- glossary ----
gl.1.t|બીજ માવજત|बीज उपचार|Seed treatment
gl.1.d|બીજને દવા કે જૈવિક પટ આપવો.|बीज को दवा या जैविक परत देना।|Coating seed with a fungicide or bio-agent.
gl.2.t|નિંદામણ|निराई|Weeding
gl.2.d|પાકમાંથી નકામું ઘાસ કાઢવું.|फसल से बेकार घास निकालना।|Removing unwanted weeds from the crop.
gl.3.t|પિયત|सिंचाई|Irrigation
gl.3.d|પાકને પાણી આપવું.|फसल को पानी देना।|Giving water to the crop.
gl.4.t|પાયાનું ખાતર|आधार खाद|Basal fertilizer
gl.4.d|વાવેતર વખતે આપવામાં આવતું ખાતર.|बुवाई के समय दी जाने वाली खाद।|Fertilizer given at sowing.
gl.5.t|પૂર્તિ ખાતર|ऊपरी खाद|Top dressing
gl.5.d|પાક ઉગ્યા પછી આપવામાં આવતું ખાતર.|फसल उगने के बाद दी जाने वाली खाद।|Fertilizer given after the crop has grown.
gl.6.t|ફેરબદલી|फसल चक्र|Crop rotation
gl.6.d|દર વર્ષે જુદા જુદા પાક વાવવા.|हर साल अलग अलग फसल बोना।|Growing different crops in turn each year.
gl.7.t|લીલો પડવાશ|हरी खाद|Green manure
gl.7.d|લીલા પાક ખેતરમાં દબાવી ખાતર બનાવવું.|हरी फसल खेत में दबाकर खाद बनाना।|Ploughing in green crops to make manure.
gl.8.t|મલ્ચિંગ|मल्चिंग|Mulching
gl.8.d|જમીન પર પાંદડાં કે પ્લાસ્ટિકનું આવરણ.|ज़मीन पर पत्ते या प्लास्टिक का आवरण।|Covering soil with leaves or plastic.
gl.9.t|ગ્રાફ્ટિંગ|ग्राफ्टिंग|Grafting
gl.9.d|બે છોડના ભાગ જોડી નવો છોડ બનાવવો.|दो पौधों के भाग जोड़कर नया पौधा बनाना।|Joining parts of two plants to make a new one.
gl.10.t|ફેરોમોન ટ્રેપ|फेरोमोन ट्रैप|Pheromone trap
gl.10.d|ગંધથી નર કીટકને ફસાવતું પિંજર.|गंध से नर कीट को फंसाने वाला जाल।|A trap that lures male insects by scent.
gl.11.t|EC|EC|EC
gl.11.d|દવાનું પ્રવાહી ઈમલ્સન સ્વરૂપ.|दवा का तरल इमल्शन रूप।|Emulsifiable concentrate liquid form.
gl.12.t|WP|WP|WP
gl.12.d|પાણીમાં ભેળવવાનો દવાનો પાઉડર.|पानी में घोलने वाला दवा का पाउडर।|Wettable powder to mix in water.
gl.13.t|વાટિંગ પીરિયડ|प्रतीक्षा अवधि|Waiting period
gl.13.d|છંટકાવ અને કાપણી વચ્ચે રાખવાના દિવસ.|छिड़काव और कटाई के बीच रखे जाने वाले दिन।|Days to wait between spraying and harvest.
gl.14.t|ખરીફ|खरीफ|Kharif
gl.14.d|ચોમાસુ ઋતુનો પાક (જૂન-ઓક્ટોબર).|मानसून मौसम की फसल (जून-अक्टूबर)।|Monsoon season crop (June-October).
gl.15.t|રવિ|रबी|Rabi
gl.15.d|શિયાળુ ઋતુનો પાક (નવેમ્બર-માર્ચ).|सर्दी के मौसम की फसल (नवंबर-मार्च)।|Winter season crop (November-March).
# ---- tips of the day ----
tip.1|💧 સવારે વહેલા કે સાંજે પિયત આપવાથી પાણીનું બાષ્પીભવન ઓછું થાય છે.|💧 सुबह जल्दी या शाम को सिंचाई देने से पानी का वाष्पीकरण कम होता है।|💧 Irrigating early morning or evening reduces evaporation.
tip.2|🌿 દર અઠવાડિયે ખેતરમાં આંટો મારી પાન તપાસો જીવાત જલદી પકડાશે.|🌿 हर हफ्ते खेत का चक्कर लगाकर पत्ते जांचें कीट जल्दी पकड़ में आएंगे।|🌿 Walk the field weekly and check leaves to catch pests early.
tip.3|🐄 છાણિયું ખાતર સારી રીતે સડેલું જ વાપરો કાચું ખાતર ઊધઈ લાવે છે.|🐄 गोबर खाद अच्छी तरह सड़ी हुई ही उपयोग करें कच्ची खाद दीमक लाती है।|🐄 Use only well-rotted manure raw manure invites termites.
tip.4|🧪 દવા છાંટતા પહેલા હંમેશા લેબલ વાંચો અને માત્રા વધારે ન કરો.|🧪 दवा छिड़कने से पहले हमेशा लेबल पढ़ें और मात्रा ज़्यादा न करें।|🧪 Always read the label before spraying and never overdose.
tip.5|🌱 દર વર્ષે પાક ફેરબદલી કરવાથી જમીન અને ઉત્પાદન સારું રહે છે.|🌱 हर साल फसल चक्र अपनाने से ज़मीन और उत्पादन अच्छा रहता है।|🌱 Rotating crops every year keeps soil and yield healthy.
tip.6|🪴 ત્રણ વર્ષે એકવાર જમીનનું પરીક્ષણ કરાવો અને ખાતર તે મુજબ આપો.|🪴 तीन साल में एक बार मिट्टी की जांच कराएं और खाद उसी अनुसार दें।|🪴 Test your soil once in three years and fertilize accordingly.
tip.7|🌾 બીજ હંમેશા પ્રમાણિત અને માવજત કરેલા જ વાવો.|🌾 बीज हमेशा प्रमाणित और उपचारित ही बोएं।|🌾 Sow only certified and treated seed.
tip.8|☀️ ગરમીમાં બપોરે છંટકાવ ન કરો દવા બળી શકે છે.|☀️ गर्मी में दोपहर को छिड़काव न करें दवा जल सकती है।|☀️ Do not spray at noon in summer the chemical can burn leaves.
tip.9|🐝 મધમાખી અને મિત્ર કીટકોને બચાવો તેઓ પરાગનયન અને જીવાત નિયંત્રણમાં મદદ કરે છે.|🐝 मधुमक्खी और मित्र कीटों को बचाएं वे परागण और कीट नियंत्रण में मदद करते हैं।|🐝 Protect bees and friendly insects they help pollination and pest control.
tip.10|💰 દરેક ખર્ચ અને આવકનો હિસાબ લખો તેનાથી ખોટ ક્યાં થાય છે તે સમજાય છે.|💰 हर खर्च और आमदनी का हिसाब लिखें इससे पता चलता है नुकसान कहां हो रहा है।|💰 Record every expense and income to see where you lose money.
tip.11|🌧️ ભારે વરસાદ પહેલા ખેતરમાં પાણી નિકાલની નીક સાફ કરી રાખો.|🌧️ भारी बारिश से पहले खेत में पानी निकासी की नालियां साफ रखें।|🌧️ Clear drainage channels before heavy rain.
tip.12|🧅 ડુંગળી બટાટા સૂકા અને હવાઉજાસવાળી જગ્યાએ સંગ્રહ કરો.|🧅 प्याज आलू सूखी और हवादार जगह पर रखें।|🧅 Store onion and potato in a dry airy place.
tip.13|🌿 લીમડાનો ખોળ જમીનમાં આપવાથી ઊધઈ અને નેમાટોડ ઘટે છે.|🌿 नीम की खली मिट्टी में देने से दीमक और निमेटोड घटते हैं।|🌿 Neem cake in soil reduces termites and nematodes.
tip.14|🪣 ઢોરનું છાણ અને ગૌમૂત્ર વેડફશો નહીં તેમાંથી જીવામૃત બનાવો.|🪣 पशुओं का गोबर और गौमूत्र बर्बाद न करें उससे जीवामृत बनाएं।|🪣 Do not waste dung and cow urine make jeevamrut from them.
tip.15|🔥 પાકના અવશેષ બાળશો નહીં તેનું ખાતર બનાવો.|🔥 फसल अवशेष न जलाएं उसकी खाद बनाएं।|🔥 Do not burn crop residue make compost from it.
tip.16|📱 હવામાન જોઈને જ છંટકાવ અને પિયતનું આયોજન કરો.|📱 मौसम देखकर ही छिड़काव और सिंचाई की योजना बनाएं।|📱 Plan spraying and irrigation after checking the weather.
tip.17|🥕 શાકભાજી સવારે વહેલા તોડો તાજગી વધુ સમય રહે છે.|🥕 सब्ज़ियां सुबह जल्दी तोड़ें ताज़गी ज़्यादा समय रहती है।|🥕 Pick vegetables early morning they stay fresh longer.
tip.18|🌴 ઝાડ વચ્ચે અંતર યોગ્ય રાખો ગીચ વાવેતર રોગ વધારે છે.|🌴 पेड़ों के बीच उचित दूरी रखें घना रोपण रोग बढ़ाता है।|🌴 Keep proper tree spacing crowding increases disease.
tip.19|🧤 સ્પ્રે પંપ વાપર્યા પછી સારી રીતે ધોઈ દો જેથી બીજા પાકને નુકસાન ન થાય.|🧤 स्प्रे पंप उपयोग के बाद अच्छी तरह धो दें ताकि दूसरी फसल को नुकसान न हो।|🧤 Wash the spray pump well after use to avoid harming other crops.
tip.20|📚 નવી જાત કે દવા પહેલા નાના ભાગમાં અજમાવો પછી આખા ખેતરમાં વાપરો.|📚 नई किस्म या दवा पहले छोटे हिस्से में आज़माएं फिर पूरे खेत में उपयोग करें।|📚 Try a new variety or chemical on a small patch before the whole field.
# ---- calendar tips by month (0=Jan) ----
cal.m.0|જાન્યુઆરી: ઘઉં ચણામાં પિયત; ઠંડીથી શાકભાજી બચાવો|जनवरी: गेहूं चना में सिंचाई; ठंड से सब्ज़ियां बचाएं|January: irrigate wheat and gram; protect vegetables from cold
cal.m.1|ફેબ્રુઆરી: ઉનાળુ શાકભાજી અને મગની તૈયારી; ઘઉં પાકવા આવે|फ़रवरी: गर्मी की सब्ज़ी और मूंग की तैयारी; गेहूं पकने लगे|February: prepare summer vegetables and moong; wheat nears maturity
cal.m.2|માર્ચ: રવિ પાકની કાપણી; ઉનાળુ મગફળી અને તલ વાવો|मार्च: रबी फसल की कटाई; गर्मी की मूंगफली और तिल बोएं|March: harvest rabi crops; sow summer groundnut and sesame
cal.m.3|એપ્રિલ: ઊંડી ખેડ કરી જમીન તપાવો; પાણીની બચત કરો|अप्रैल: गहरी जुताई कर ज़मीन तपाएं; पानी बचाएं|April: deep plough and sun-bake the land; save water
cal.m.4|મે: ખેતર તૈયાર કરો; બીજ અને ખાતરનો સ્ટોક કરો|मई: खेत तैयार करें; बीज और खाद का स्टॉक करें|May: prepare fields; stock seed and fertilizer
cal.m.5|જૂન: ચોમાસું વાવણી - કપાસ મગફળી બાજરી જુવાર|जून: मानसून बुवाई - कपास मूंगफली बाजरा ज्वार|June: monsoon sowing - cotton groundnut bajra jowar
cal.m.6|જુલાઈ: નિંદામણ અને પહેલું ખાતર; પાણી ભરાવો ટાળો|जुलाई: निराई और पहली खाद; जलभराव से बचें|July: weeding and first fertilizer; avoid waterlogging
cal.m.7|ઓગસ્ટ: રોગ જીવાતનું ધ્યાન; પૂર્તિ ખાતર આપો|अगस्त: रोग कीट पर ध्यान; ऊपरी खाद दें|August: watch for pests and diseases; top-dress fertilizer
cal.m.8|સપ્ટેમ્બર: શાકભાજી નર્સરી; કપાસમાં ગુલાબી ઈયળ તપાસો|सितंबर: सब्ज़ी नर्सरी; कपास में गुलाबी सुंडी जांचें|September: vegetable nursery; check cotton for pink bollworm
cal.m.9|ઓક્ટોબર: ખરીફ કાપણી; રવિ માટે જમીન તૈયાર કરો|अक्टूबर: खरीफ कटाई; रबी के लिए ज़मीन तैयार करें|October: kharif harvest; prepare land for rabi
cal.m.10|નવેમ્બર: ઘઉં ચણા જીરું રાઈ વાવો; બીજ માવજત કરો|नवंबर: गेहूं चना जीरा सरसों बोएं; बीज उपचार करें|November: sow wheat gram cumin mustard; treat seed
cal.m.11|ડિસેમ્બર: પહેલું પિયત અને નિંદામણ; ઠંડી અને ઝાકળ સામે રક્ષણ|दिसंबर: पहली सिंचाई और निराई; ठंड और कोहरे से सुरक्षा|December: first irrigation and weeding; protect from cold and fog
"""


def _build_t3():
    out = {}
    for line in NEW_TXT.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        p = line.split("|")
        if len(p) == 4:
            out[p[0]] = [p[1].strip(), p[2].strip(), p[3].strip()]
    return out


T3 = _build_t3()

ICON_SVG = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#40916c"/><stop offset="1" stop-color="#1b4332"/></linearGradient></defs><rect width="512" height="512" rx="112" fill="url(#g)"/><path d="M112.9 219.7 L119.8 233.5 L130.6 247.3 L140.4 249.2 L152.2 244.3 L157.1 244.3 L158.1 253.2 L158.1 265.0 L163.0 278.8 L169.0 301.4 L175.8 320.1 L178.8 327.0 L183.7 339.7 L191.6 355.5 L195.5 367.3 L204.4 373.2 L211.2 365.3 L220.1 355.5 L228.0 351.5 L227.0 340.7 L231.9 324.0 L229.9 305.3 L237.8 297.4 L251.6 289.6 L262.4 277.8 L276.2 263.0 L287.0 258.1 L296.8 246.3 L298.8 240.4 L309.6 239.4 L317.5 234.5 L314.5 224.7 L310.6 216.8 L310.6 208.9 L307.6 203.0 L311.6 195.1 L324.4 197.1 L326.3 204.0 L342.1 206.0 L348.0 207.9 L349.0 215.8 L341.1 224.7 L344.0 227.6 L349.9 223.7 L352.9 236.5 L359.8 228.6 L360.8 218.8 L369.6 212.9 L372.6 204.0 L378.5 191.2 L387.3 184.3 L397.1 179.4 L388.3 166.6 L373.5 164.7 L357.8 173.5 L343.0 179.4 L331.2 176.5 L318.5 182.4 L316.5 178.4 L308.6 179.4 L307.6 192.2 L297.8 193.2 L278.1 189.2 L268.3 183.3 L256.5 182.4 L244.7 174.5 L233.9 162.7 L230.9 153.8 L219.1 146.0 L216.2 134.2 L221.1 125.3 L216.2 113.5 L207.3 103.7 L194.5 100.7 L181.7 102.7 L170.9 110.6 L175.8 118.4 L173.9 128.3 L181.7 132.2 L176.8 141.0 L170.9 148.9 L169.9 157.8 L162.1 165.6 L150.3 175.5 L139.4 179.4 L132.6 188.3 L130.6 200.1 L139.4 211.9 L133.5 215.8 L123.7 217.8Z" fill="#d8f3dc" stroke="#ffffff" stroke-width="5" stroke-linejoin="round"/><path d="M112.9 219.7 L123.7 217.8 L133.5 215.8 L139.4 211.9 L145.3 213.8 L154.2 212.9 L161.1 211.9 L166.0 215.8 L170.9 223.7 L171.9 232.5 L167.0 238.4 L164.0 246.3 L159.1 252.2 L158.1 253.2 L157.1 244.3 L152.2 244.3 L140.4 249.2 L130.6 247.3 L119.8 233.5 L125.7 227.6 L132.6 227.6 L139.4 225.6 L132.6 225.6 L124.7 223.7 L118.8 224.7Z" fill="#ff9f1c" stroke="#fff" stroke-width="4" stroke-linejoin="round"/><circle cx="140" cy="234" r="15" fill="#fff"/><circle cx="140" cy="234" r="7" fill="#d62828"/><path d="M340 372c-34 16-46 56-30 92 22-6 46-24 56-52 6-16 4-30-26-40z" fill="#52b788" stroke="#fff" stroke-width="4"/><circle cx="410" cy="410" r="58" fill="#fff"/><path d="M410 378v64M378 410h64" stroke="#d62828" stroke-width="20" stroke-linecap="round"/></svg>"""
ICON_192 = "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"
ICON_512 = "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"

# ════════════════════════════════════════════════════════════════════
# 🌐 FLASK WEB APP (Backend)  -  Smart Health & Crop Guard v12 Web
# ════════════════════════════════════════════════════════════════════
import json
import base64
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from flask import Flask, Response, request

app = Flask(__name__)

FERT = {"Paddy": (48, 24, 24), "Wheat": (48, 24, 16), "Cotton": (64, 32, 32),
        "Sugarcane": (100, 40, 40), "Maize": (48, 24, 16), "Tomato": (40, 20, 20),
        "Potato": (48, 32, 32), "Groundnut": (16, 16, 16), "Onion": (40, 24, 24),
        "Chili": (48, 24, 24)}


# 🖼️ Wikipedia ના સાચા નામ (ફોટા માટે) - જે નામ અલગ છે તે જ અહીં છે
WIKI = {
 "Neem":"Azadirachta indica","Drumstick":"Moringa oleifera","Moringa":"Moringa oleifera","Sapota":"Sapodilla",
 "Jamun Tree":"Syzygium cumini","Amla Tree":"Phyllanthus emblica","Ber Tree":"Ziziphus mauritiana","Fig Tree":"Ficus carica",
 "Gulmohar Tree":"Delonix regia","Kadamba Tree":"Neolamarckia cadamba","Silver Oak":"Grevillea robusta","Rain Tree":"Samanea saman",
 "Groundnut":"Peanut","Castor":"Castor oil plant","Gram":"Chickpea","Moong":"Mung bean","Urad":"Vigna mungo",
 "Mustard":"Mustard plant","Horse Gram":"Macrotyloma uniflorum","Rajma":"Kidney bean","Tobacco":"Nicotiana tabacum",
 "Marigold":"Tagetes","Lotus":"Nelumbo nucifera","Periwinkle":"Catharanthus roseus","Crossandra":"Crossandra infundibuliformis",
 "Aster":"Callistephus chinensis","Tuberose":"Agave amica","Daisy":"Bellis perennis","Champa":"Plumeria","Kaner":"Nerium",
 "Rat Ki Rani":"Cestrum nocturnum","Mogra":"Jasminum sambac","Parijat":"Nyctanthes arbor-tristis","Kewda":"Pandanus odorifer",
 "Gulmohar":"Delonix regia","Kadamba":"Neolamarckia cadamba","Aparajita":"Clitoria ternatea","Lily":"Lilium","Jasmine":"Jasmine",
 "Muskmelon":"Cantaloupe","Fig":"Ficus carica","Jamun":"Syzygium cumini","Ber":"Ziziphus mauritiana","Amla":"Phyllanthus emblica",
 "Custard Fruit":"Custard apple","Orange":"Orange (fruit)","Sweet Lime":"Citrus limetta","Kiwi":"Kiwifruit","Dragon Fruit":"Pitaya",
 "Paddy":"Rice","Bajra":"Pearl millet","Jowar":"Sorghum","Ragi":"Finger millet","Kodo Millet":"Paspalum scrobiculatum",
 "Kutki":"Picrorhiza kurroa","Barnyard Millet":"Echinochloa frumentacea","Little Millet":"Panicum sumatrense",
 "Foxtail Millet":"Setaria italica","Tulsi":"Ocimum tenuiflorum","Ashwagandha":"Withania somnifera","Giloy":"Tinospora cordifolia",
 "Brahmi":"Bacopa monnieri","Ajwain":"Trachyspermum ammi","Curry Leaf":"Murraya koenigii","Shatavari":"Asparagus racemosus",
 "Kalmegh":"Andrographis paniculata","Vasaka":"Justicia adhatoda","Chili":"Chili pepper","Brinjal":"Eggplant",
 "Bottle Gourd":"Calabash","Bitter Gourd":"Momordica charantia","Ladyfinger":"Okra","Beans":"Common bean","Cluster Beans":"Guar",
 "Ridge Gourd":"Luffa acutangula","Sponge Gourd":"Luffa aegyptiaca","Pointed Gourd":"Trichosanthes dioica","Colocasia":"Taro",
 "Yam":"Dioscorea alata","Sweet Corn":"Sweet corn","Bell Pepper":"Bell pepper","Aloe Vera":"Aloe vera","Black Pepper":"Black pepper",
}

def build_payload():
    crops = []
    for name, cd in crop_database.items():
        s = SEED_DB.get(name, {})
        crops.append({"n": name, "h": HIN_NAMES.get(name, cd["gujarati"]), "w": EXTRA_WIKI.get(name, WIKI.get(name, name)), "g": cd["gujarati"], "c": cd["category"], "season": cd["season"],
                      "seed": {k: s.get(k, "") for k in ("seed_guj", "look_guj", "rate", "germ",
                               "method_guj", "season_guj", "care_guj", "harvest", "special",
                               "seed_hin", "look_hin", "method_hin")}})
    meds = [dict(v, n=k) for k, v in MED_DB.items()]
    return {"crops": crops, "meds": meds, "symptoms": symptoms(), "recipes": ORGANIC_RECIPES,
            "schemes": SCHEMES, "fert": FERT, "tr": I18N, "t3": T3, "states": [list(s) for s in STATES]}

PAYLOAD = json.dumps(build_payload(), ensure_ascii=False)

@app.route("/")
def home():
    return Response(HTML_PAGE, mimetype="text/html")

@app.route("/api/data")
def api_data():
    return Response(PAYLOAD, mimetype="application/json")


# ── App icon + install (Add to Home screen) ─────────────────────────
@app.route("/icon.svg")
def icon_svg():
    return Response(ICON_SVG, mimetype="image/svg+xml")


@app.route("/icon-192.png")
def icon_192():
    return Response(base64.b64decode(ICON_192), mimetype="image/png")


@app.route("/icon-512.png")
def icon_512():
    return Response(base64.b64decode(ICON_512), mimetype="image/png")


@app.route("/manifest.json")
def manifest():
    m = {"name": "Smart Health & Crop Guard", "short_name": "Kisan AI", "start_url": "/", "display": "standalone",
         "background_color": "#1b4332", "theme_color": "#1b4332",
         "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
                   {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}
    return Response(json.dumps(m), mimetype="application/manifest+json")


# ── SK News: daily farmer news (Google News RSS, fetched server-side) ──
NEWS_TTL = 900
_NEWS_CACHE = {}
NEWS_Q = {"gu": "(ખેડૂત OR ખેતી OR કૃષિ)", "hi": "(किसान OR खेती OR कृषि)",
          "en": "(farmers OR farming OR agriculture)"}
NEWS_ED = {"gu": ("gu", "IN:gu"), "hi": ("hi", "IN:hi"), "en": ("en-IN", "IN:en")}


def _http_get(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36"})
    with urllib.request.urlopen(req, timeout=12) as r:
        return r.read()


def _news_url(q, lang, rss=True):
    hl, ceid = NEWS_ED[lang]
    base = "https://news.google.com/rss/search" if rss else "https://news.google.com/search"
    return base + "?q=" + urllib.parse.quote(q) + "&hl=" + hl + "&gl=IN&ceid=" + urllib.parse.quote(ceid, safe=":")


def _parse_rss(raw):
    items = []
    for it in ET.fromstring(raw).iter("item"):
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        src = (it.findtext("source") or "").strip()
        if src and title.endswith(" - " + src):
            title = title[: -len(" - " + src)].strip()
        elif not src and " - " in title:
            title, src = title.rsplit(" - ", 1)
        try:
            ts = int(parsedate_to_datetime(it.findtext("pubDate") or "").timestamp() * 1000)
        except Exception:
            ts = 0
        if title and link.startswith("http"):
            items.append({"t": title, "l": link, "s": src, "d": ts})
    return items


def _news_query(lang, state_key):
    st = next((s for s in STATES if s[0] == state_key), None)
    q = NEWS_Q[lang]
    if st:
        q += " " + {"gu": st[1], "hi": st[2], "en": st[3]}[lang]
    elif lang == "en":
        q += " India"
    return q


def get_news(lang, state_key):
    key = (lang, state_key)
    c = _NEWS_CACHE.get(key)
    if c and time.time() - c[0] < NEWS_TTL:
        return c[1]
    items, ok = [], False
    for lg in ([lang] if lang == "en" else [lang, "en"]):     # fall back to English if too few
        q = _news_query(lg, state_key)
        for when in ("1d", "7d"):                              # today first, then this week
            try:
                got = _parse_rss(_http_get(_news_url(q + " when:" + when, lg)))
                ok = True
            except Exception:
                got = []
            items += got
            if len(got) >= 6:
                break
        if len(items) >= 8:
            break
    seen, out = set(), []
    for it in sorted(items, key=lambda x: x["d"], reverse=True):
        k = it["t"].lower()
        if k not in seen:
            seen.add(k)
            out.append(it)
    res = {"ok": ok, "items": out[:25], "url": _news_url(_news_query(lang, state_key), lang, rss=False)}
    if ok and out:
        _NEWS_CACHE[key] = (time.time(), res)
    return res


@app.route("/api/news")
def api_news():
    lang = request.args.get("lang", "gu")
    lang = lang if lang in NEWS_Q else "gu"
    state = request.args.get("state", "")
    state = state if state in [s[0] for s in STATES] else ""
    r = Response(json.dumps(get_news(lang, state), ensure_ascii=False), mimetype="application/json")
    r.headers["Cache-Control"] = "no-store"
    return r


HTML_PAGE = r"""<!DOCTYPE html>
<html lang="gu"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Smart Health & Crop Guard</title>
<link rel="icon" href="/icon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/icon-192.png"><link rel="manifest" href="/manifest.json"><meta name="theme-color" content="#1b4332">
<style>
*{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',Roboto,Arial,sans-serif}
body{background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);min-height:100vh;display:flex;justify-content:center;color:#222}
#splash{position:fixed;inset:0;background:linear-gradient(135deg,#1b4332,#081c15);display:flex;flex-direction:column;justify-content:center;align-items:center;z-index:99;color:#fff;transition:opacity .5s}
#splash .l{font-size:56px;animation:b 1.4s infinite}@keyframes b{50%{transform:translateY(-10px)}}
.sp{width:42px;height:42px;border:4px solid #fff3;border-top-color:#52b788;border-radius:50%;animation:r 1s linear infinite;margin-top:20px}@keyframes r{to{transform:rotate(360deg)}}
.app{background:#fff;width:100%;max-width:480px;min-height:100vh;display:none;flex-direction:column;position:relative}
header{background:linear-gradient(135deg,#1b4332,#2d6a4f);color:#fff;padding:18px 16px 14px;text-align:center;border-radius:0 0 24px 24px}
header .bd{background:#fff3;padding:3px 12px;border-radius:20px;font-size:11px;display:inline-block;margin-bottom:6px}
header h1{font-size:20px}header p{font-size:12px;color:#b7e4c7}
main{flex:1;padding:16px 14px 90px;overflow-y:auto}
nav{position:fixed;bottom:0;width:100%;max-width:480px;display:flex;background:#fff;border-top:1px solid #ddd;z-index:5}
nav button{flex:1;border:0;background:none;padding:8px 2px;font-size:11px;color:#555}nav button span{display:block;font-size:20px}
nav button.on{color:#1b4332;font-weight:700;background:#d8f3dc}
h2{font-size:17px;color:#1b4332;margin:4px 0 10px}h3{font-size:14px;color:#1b4332;margin:10px 0 6px}
label{display:block;font-weight:600;font-size:13px;color:#1b4332;margin:10px 0 5px}
select,input{width:100%;padding:11px 12px;border-radius:12px;border:2px solid #d8f3dc;background:#f8f9fa;font-size:15px}
.btn{width:100%;padding:13px;margin-top:12px;background:linear-gradient(135deg,#2d6a4f,#40916c);color:#fff;border:0;border-radius:14px;font-size:15px;font-weight:700}
.btn.s{width:auto;padding:8px 14px;font-size:13px;margin:4px 4px 0 0}.btn.r{background:#c1121f}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.card{background:#f1faee;border-radius:14px;overflow:hidden;border:1px solid #d8f3dc}
.card .t{padding:6px 8px;font-size:13px;font-weight:600;text-align:center}.card .t small{display:block;font-weight:400;color:#555}
.ph{height:100px;background:#d8f3dc;display:flex;align-items:center;justify-content:center;font-size:40px;overflow:hidden}
.ph img{width:100%;height:100%;object-fit:cover}.ph.big{height:190px}
.chips{display:flex;gap:6px;overflow-x:auto;padding:8px 0}.chip{white-space:nowrap;padding:6px 12px;border-radius:20px;background:#e9ecef;font-size:13px;border:0}.chip.on{background:#2d6a4f;color:#fff}
.sym{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-top:6px}.sym button{padding:12px 6px;border-radius:12px;border:2px solid #d8f3dc;background:#fff;font-size:13px}.sym button.on{background:#2d6a4f;color:#fff}
.res{margin-top:14px;background:#f1faee;border-left:5px solid #2d6a4f;border-radius:14px;padding:14px}
.box{padding:10px;border-radius:10px;margin-top:8px;font-size:14px;line-height:1.5}.home{background:#d8f3dc}.mkt{background:#e0fbfc;border-left:3px solid #0077b6}
.sev{display:inline-block;padding:3px 10px;border-radius:12px;color:#fff;font-size:12px;font-weight:700}
.row{display:flex;gap:10px;align-items:center;background:#f8f9fa;border-radius:12px;padding:8px;margin-bottom:8px;font-size:13px}.row .ph{width:60px;height:60px;border-radius:10px;font-size:26px;flex:none}.row div.i{flex:1}
.modal{position:fixed;inset:0;background:#000a;z-index:20;display:none;align-items:flex-end;justify-content:center}.modal .in{background:#fff;width:100%;max-width:480px;max-height:90vh;overflow-y:auto;border-radius:22px 22px 0 0;padding:14px}
.kv{font-size:14px;line-height:1.7}.out{background:#fefae0;border-radius:12px;padding:12px;margin-top:10px;font-size:14px;line-height:1.7}
.tool{background:#f8f9fa;border-radius:14px;padding:12px;margin-bottom:12px}
footer{text-align:center;font-size:12px;padding:8px;color:#1b4332;font-weight:700}
header{box-shadow:0 6px 18px #0004;position:relative}
header .bd{animation:glow 3s infinite}@keyframes glow{50%{background:#ffffff55}}
.hb{display:flex;justify-content:center;gap:8px;align-items:center;margin-top:8px;font-size:12px}
.hb span{background:#ffffff30;padding:4px 10px;border-radius:14px}.hb button{background:#ffffff30;border:0;border-radius:14px;padding:4px 10px;font-size:14px}
.card{box-shadow:0 3px 10px #0002;transition:transform .2s}.card:active{transform:scale(.96)}
.row{box-shadow:0 1px 6px #0001}.tool{box-shadow:0 2px 8px #0001}
.toast{position:fixed;top:14px;left:50%;transform:translateX(-50%);background:#1b4332;color:#fff;padding:10px 18px;border-radius:22px;z-index:99;font-size:14px;transition:opacity .5s;box-shadow:0 4px 14px #0006}
nav button{font-size:10px}nav button span{font-size:19px}
body.dk .app{background:#12201a;color:#e8f5e9}body.dk main{color:#e8f5e9}
body.dk h2,body.dk h3,body.dk label,body.dk footer{color:#95d5b2}
body.dk .card,body.dk .row,body.dk .tool,body.dk .res{background:#1e332a;color:#e8f5e9;border-color:#2d4a3c}
body.dk select,body.dk input{background:#1e332a;color:#fff;border-color:#2d6a4f}
body.dk .box.home{background:#2d6a4f}body.dk .box.mkt,body.dk .out,body.dk .box{background:#26413a!important;color:#e8f5e9}
body.dk nav{background:#12201a;border-color:#2d4a3c}body.dk nav button{color:#b7e4c7}body.dk nav button.on{background:#2d6a4f;color:#fff}
body.dk .modal .in{background:#12201a;color:#e8f5e9}body.dk .chip{background:#2d4a3c;color:#e8f5e9}body.dk .chip.on{background:#40916c}
body.dk .sym button{background:#1e332a;color:#e8f5e9;border-color:#2d4a3c}body.dk .sym button.on{background:#40916c}
body.dk .ph{background:#2d4a3c}
/* ===== v3 additions ===== */
#splash .sbg{position:absolute;inset:0;width:100%;height:100%;font-size:0;background:transparent;opacity:.4}
#splash .sc{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center}
#splash .slogo{width:112px;height:112px;border-radius:28px;box-shadow:0 8px 28px #0008;animation:b 1.4s infinite}
.lbar{width:190px;height:6px;background:#fff3;border-radius:4px;margin-top:22px;overflow:hidden}.lbar i{display:block;height:100%;width:40%;background:#52b788;border-radius:4px;animation:ld 1.3s ease-in-out infinite}@keyframes ld{0%{margin-left:-40%}100%{margin-left:100%}}
.hl{width:26px;height:26px;border-radius:7px;vertical-align:middle}
#setup{position:fixed;inset:0;z-index:90;overflow-y:auto;background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);display:none;padding:16px;align-items:center;justify-content:center}
#setup .sbg{position:fixed;inset:0;width:100%;height:100%;font-size:0;background:transparent;opacity:.5;z-index:0}
.sbox{position:relative;z-index:2;background:#fffffff2;width:100%;max-width:440px;border-radius:22px;padding:20px 18px 22px;margin:auto;box-shadow:0 10px 30px #0006}
.slogo img,.slogo{display:flex;justify-content:center}.sbox .slogo img{width:78px;height:78px;border-radius:20px;box-shadow:0 4px 12px #0004}
.sbox h2{text-align:center;font-size:21px;margin:8px 0 2px}.ssub{text-align:center;font-size:13px;color:#555;margin-bottom:6px}
.lg{display:flex;gap:8px}.lg button{flex:1;padding:12px 4px;border-radius:12px;border:2px solid #d8f3dc;background:#fff;font-size:15px;font-weight:700;color:#1b4332}.lg button.on{background:#2d6a4f;color:#fff;border-color:#2d6a4f}
.hello{position:relative;overflow:hidden;border-radius:16px;color:#fff;background:linear-gradient(135deg,#1b4332,#2d6a4f);min-height:84px}
.hello .ph.hp{position:absolute;inset:0;width:100%;height:100%;font-size:0;background:transparent;z-index:0}
.hello::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#081c15ee,#081c1599);z-index:1}
.hello .ht{position:relative;z-index:2;padding:14px;font-size:16px;line-height:1.6}.hello small{color:#d8f3dc;font-size:12px}
.wxm{margin-top:10px;background:linear-gradient(135deg,#0077b6,#48cae4);color:#fff;border-radius:16px;padding:12px 14px;cursor:pointer;box-shadow:0 3px 10px #0003}
.wxm .wm1{display:flex;align-items:center;gap:10px;font-size:26px}.wxm .wme{font-size:32px}.wxm .wmt{font-size:14px;font-weight:600}.wxm small{display:block;font-size:12px;margin-top:4px}
.ig{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.ic{position:relative;overflow:hidden;aspect-ratio:1/1;min-height:100px;border:0;border-radius:18px;box-shadow:0 3px 10px #0003;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:2px;padding:8px 5px;text-align:center;color:#fff}
.ic .ph.tp{position:absolute;inset:0;width:100%;height:100%;background:transparent;font-size:0;z-index:0}
.ic::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,#0000 20%,#000c);z-index:1}
.ic>*:not(.ph){position:relative;z-index:2}.ic .ie{font-size:30px;line-height:1;text-shadow:0 2px 6px #0008;margin-bottom:auto}
.ic b{font-size:12px;line-height:1.2}.ic small{font-size:10px;opacity:.93;line-height:1.2}.ic:active{transform:scale(.96)}
.wbig{background:linear-gradient(135deg,#0077b6,#48cae4);color:#fff;border-radius:18px;padding:16px;text-align:center;box-shadow:0 3px 10px #0003}.wbig .wt1{font-size:44px}.wbig b{font-size:44px}.wbig small{display:block;font-size:12.5px;margin-top:5px}
.hs{display:flex;gap:8px;overflow-x:auto;padding:4px 0 8px}.hc{flex:none;min-width:58px;text-align:center;background:#f1faee;border:1px solid #d8f3dc;border-radius:12px;padding:8px 6px}.hc small{display:block;font-size:11px;color:#555}.hc b{font-size:16px}
.wr{display:flex;align-items:center;gap:8px;background:#f8f9fa;border-radius:12px;padding:8px 10px;margin-bottom:6px;font-size:13px}.wr.past{opacity:.65}.wr.now{border:2px solid #2d6a4f;background:#d8f3dc}
.wd{width:76px}.wd b{display:block;font-size:13px}.wd small{display:block;font-size:10.5px;color:#555;line-height:1.2}.we{font-size:24px;width:30px;text-align:center}
.wtp{flex:1;display:flex;align-items:center;gap:6px;font-weight:700}.bar{flex:1;height:8px;background:#dde5e0;border-radius:6px;position:relative}.bar i{position:absolute;top:0;bottom:0;border-radius:6px;background:linear-gradient(90deg,#48cae4,#f4a261,#e63946)}
.wp{width:64px;text-align:right;font-size:12px}.wp small{display:block;color:#555;font-size:10.5px}
.nw{display:block;background:#f8f9fa;border-radius:12px;padding:11px 12px;margin-bottom:8px;text-decoration:none;color:#222;border-left:4px solid #2d6a4f;box-shadow:0 1px 6px #0001}.nw b{display:block;font-size:14px;line-height:1.45}.nw small{display:block;margin-top:5px;color:#666;font-size:11.5px}
.lgs{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.lc{border-radius:14px;padding:10px 4px;text-align:center;color:#fff}.lc small{display:block;font-size:11px;opacity:.92}.lc b{font-size:16px}
.lc.g{background:linear-gradient(135deg,#2d6a4f,#40916c)}.lc.r{background:linear-gradient(135deg,#9b2226,#d62828)}
nav button{font-size:9.5px;padding:6px 0;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}nav button span{font-size:19px}
body.dk .sbox{background:#12201af2;color:#e8f5e9}body.dk .ssub{color:#b7e4c7}body.dk .lg button{background:#1e332a;color:#e8f5e9;border-color:#2d4a3c}body.dk .lg button.on{background:#40916c}
body.dk .hc,body.dk .wr,body.dk .nw{background:#1e332a;color:#e8f5e9;border-color:#2d4a3c}body.dk .wr.now{background:#2d6a4f}
body.dk .hc small,body.dk .wd small,body.dk .wp small,body.dk .nw small{color:#b7e4c7}body.dk .bar{background:#2d4a3c}
.pb{height:10px;background:#dde5e0;border-radius:8px;overflow:hidden;margin:8px 0}.pb i{display:block;height:100%;background:linear-gradient(90deg,#40916c,#95d5b2)}
body.dk .pb{background:#2d4a3c}
.bl{margin:6px 0 0;padding-left:20px}.bl li{margin-bottom:5px;line-height:1.5}
.pl{text-align:center;padding:10px 6px}.pe{font-size:84px;line-height:1.1;animation:b 1.4s infinite}.pt{font-size:17px;line-height:1.6;margin:10px 0}
.plc{display:flex;gap:8px;margin:8px 0}.plc button{flex:1}
details.tool summary{cursor:pointer;font-size:15px}details.tool p{margin:8px 0 2px}
</style></head><body>
<div id="splash"><div class="ph sbg" data-q="Wheat|golden wheat field sunrise"></div><div class="sc"><img class="slogo" src="/icon.svg" alt=""><h2 style="color:#fff;margin-top:14px">Smart Health & Crop Guard</h2><p style="color:#b7e4c7;font-size:13px">Loading AI Plant Doctor...</p><div class="lbar"><i></i></div></div></div>
<div class="app" id="app">
<header><div class="bd">🔬 Science Exhibition AI Model</div><h1><img class="hl" src="/icon.svg" alt=""> Smart Health & Crop Guard</h1><p id="hsub">ડિજિટલ પ્લાન્ટ ડૉક્ટર | Created by Mr_SK</p><div class="hb"><span id="pts"></span><button id="lgb" onclick="cycleLang()">🌐</button><button onclick="openSetup()">👤</button><button onclick="toggleTheme()">🌙</button></div></header>
<main id="main"></main>
<nav id="nav"></nav>
<div class="modal" id="modal" onclick="if(event.target==this)closeM()"><div class="in" id="mbody"></div></div>
</div>
<div id="setup"></div>
<script>
var D=null,TAB='home',CAT='બધા',Q='',SYM='',CROP='';
var EM={Trees:'🌳',Grains:'🌾','Cash Crops':'🌱',Vegetables:'🥬',Fruits:'🍎',Flowers:'🌸',Herbs:'🌿'};
var CATG={Trees:'વૃક્ષ',Grains:'અનાજ','Cash Crops':'રોકડિયા',Vegetables:'શાકભાજી',Fruits:'ફળ',Flowers:'ફૂલ',Herbs:'ઔષધિ'};
var MEM={'કીટકનાશક':'🐛','ફૂગનાશક':'🍄','નીંદણનાશક':'🌱','માટી સુધારક':'🪨'};
var SEV={Low:['ઓછી','#52b788',1],Moderate:['મધ્યમ','#f4a261',2],Severe:['ગંભીર','#c1121f',3],None:['નથી','#2d6a4f',0]};
var SYL={holes:'🕳️ કાણાં / કરડવું',yellowing:'🟡 પાન પીળા',spots:'🍂 ફૂગ ડાઘ',curl:'🌀 પાન વળવા',wilting:'🥀 કરમાવું',healthy:'✅ સ્વસ્થ'};
function ls(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function sv(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
var FAV=ls('fav',[]),HIST=ls('hist',[]),CART=ls('cart',[]),DIARY=ls('diary',[]);
function $(i){return document.getElementById(i)}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function num(id,d){var v=parseFloat($(id).value);return isNaN(v)?d:v}
/* ---------- Internet photos (Wikipedia, multi-step) with emoji fallback ---------- */
var obs=null;
function ph(q,e,big){return '<div class="ph'+(big?' big':'')+'" data-q="'+esc(q)+'">'+e+'</div>'}
function loadImg(el){
  var q=el.getAttribute('data-q'),ck='img2:'+q,c=ls(ck,null),pt=q.split('|'),title=pt[0],alt=pt[1]||pt[0];
  function put(u){if(!u)return;var im=new Image();im.onload=function(){el.innerHTML='';el.appendChild(im)};im.src=u}
  if(c!==null){put(c);return}
  function search(){
    fetch('https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch='+encodeURIComponent(alt)+'&gsrlimit=6&prop=pageimages&pithumbsize=400&format=json&origin=*')
    .then(function(r){return r.json()}).then(function(j){var u='';try{var ps=Object.keys(j.query.pages).map(function(k){return j.query.pages[k]}).sort(function(a,b){return a.index-b.index});
      for(var i=0;i<ps.length;i++){if(ps[i].thumbnail){u=ps[i].thumbnail.source;break}}}catch(e){}
      sv(ck,u);put(u)}).catch(function(){})}
  fetch('https://en.wikipedia.org/api/rest_v1/page/summary/'+encodeURIComponent(title.replace(/ /g,'_')))
  .then(function(r){return r.ok?r.json():Promise.reject()}).then(function(j){var u=(j.type!='disambiguation'&&j.thumbnail)?j.thumbnail.source:'';if(u){sv(ck,u);put(u)}else search()}).catch(search)
}
function scanImgs(){
  var els=document.querySelectorAll('.ph[data-q]');
  if(!('IntersectionObserver' in window)){els.forEach(loadImg);return}
  if(!obs)obs=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){obs.unobserve(x.target);loadImg(x.target)}})},{rootMargin:'200px'});
  els.forEach(function(el){obs.observe(el)});
}
function cq(c){return c.w+'|'+c.n+(c.c=='Flowers'?' flower':c.c=='Trees'?' tree':c.c=='Fruits'?' fruit':c.c=='Vegetables'?' vegetable':' plant')}
/* ---------- Tabs ---------- */
var TABS=[['home','🏠','હોમ'],['diag','🩺','નિદાન'],['crops','🌱','પાક'],['meds','💊','દવા'],['tools','🧰','સાધનો'],['play','🎓','ક્વિઝ'],['more','🏛️','વધુ']];
function nav(){$('nav').innerHTML=TR(TABS.map(function(t){var on=(TAB==t[0])||(t[0]=='home'&&['diag','crops','meds','tools','play','more'].indexOf(TAB)<0);return '<button class="'+(on?'on':'')+'" onclick="go(\''+t[0]+'\')"><span>'+t[1]+'</span>'+t[2]+'</button>'}).join(''))}
function go(t){TAB=t;nav();render();window.scrollTo(0,0)}
function render(){var f=({home:vHome,diag:vDiag,crops:vCrops,meds:vMeds,tools:vTools,play:vPlay,more:vMore,wx:vWx,news:vNews,ledger:vLedger,seeds:vSeeds,track:vTrack,fg:vFG,mkf:function(){return vHow('mkf')},mkp:function(){return vHow('mkp')},mkt:function(){return vHow('mkt')}})[TAB]||vMisc;$('main').innerHTML=TR(f()+'<footer>Created by Mr_SK 🌿</footer>');scanImgs()}
/* ---------- Diagnose ---------- */
function cropOpts(){var o='<option value="">-- પાક પસંદ કરો --</option>';Object.keys(CATG).forEach(function(k){var l=D.crops.filter(function(c){return c.c==k});if(l.length)o+='<optgroup label="'+EM[k]+' '+CATG[k]+'">'+l.map(function(c){return '<option value="'+esc(c.n)+'"'+(c.n==CROP?' selected':'')+'>'+esc(c.g)+' ('+esc(c.n)+')</option>'}).join('')+'</optgroup>'});return o}
function vDiag(){
  var h='<h2>🩺 પાક રોગ નિદાન</h2><label>🌱 ૧. પાક પસંદ કરો</label><select id="dc" onchange="CROP=this.value;render()">'+cropOpts()+'</select>';
  var c=D.crops.filter(function(x){return x.n==CROP})[0];
  if(c)h+='<div style="margin-top:10px">'+ph(cq(c),EM[c.c],1)+'</div>';
  h+='<label>🔍 ૨. લક્ષણ પસંદ કરો</label><div class="sym">'+Object.keys(SYL).map(function(k){return '<button class="'+(SYM==k?'on':'')+'" onclick="SYM=\''+k+'\';render()">'+SYL[k]+'</button>'}).join('')+'</div>';
  h+='<button class="btn" onclick="diagnose()">⚡ નિદાન અને ઉપચાર જુઓ</button><div id="dres"></div>';
  return h}
function findMed(t){var w=t.split(' ')[0].toLowerCase();return D.meds.filter(function(m){return m.n.toLowerCase().indexOf(w)>-1})[0]}
function diagnose(){
  if(!CROP||!SYM){alert(TR('કૃપા કરીને પહેલા પાક અને લક્ષણ બંને પસંદ કરો!'));return}
  var s=D.symptoms[SYM],c=D.crops.filter(function(x){return x.n==CROP})[0],v=SEV[s.severity]||SEV.None;
  var m=findMed(s.market),bar='';for(var i=1;i<=3;i++)bar+=i<=v[2]?'🟥':'⬜';
  var t=new Date().toLocaleString();
  HIST.unshift({t:t,c:c.n,g:c.g,s:SYL[SYM],sev:s.severity});HIST=HIST.slice(0,50);sv('hist',HIST);addPts(10,'નિદાન');LASTDX='🌿 Smart Health & Crop Guard\n🌱 '+c.g+' ('+c.n+')\n📌 '+s.problem_guj+'\n🏡 '+s.home+'\n💊 '+s.market+'\n📞 Kisan Call Center: 1800-180-1551';
  $('dres').innerHTML=TR('<div class="res"><h3>📋 રિપોર્ટ: '+esc(c.g)+' ('+esc(c.n)+')</h3>'+
  '<div class="kv">📌 <b>સમસ્યા:</b> '+esc(s.problem_guj)+' ('+esc(s.problem)+')<br>⚠️ <b>તીવ્રતા:</b> <span class="sev" style="background:'+v[1]+'">'+v[0]+'</span> '+bar+'<br>📅 ઋતુ: '+esc(c.season)+'</div>'+
  '<div class="box home">🏡 <b>ઘરેલું ઉપાય:</b> '+esc(s.home)+'<br>💰 ખર્ચ: '+esc(s.home_cost)+'</div>'+
  '<div class="box mkt">💊 <b>બજારની દવા:</b> '+esc(s.market)+'<br>💰 ખર્ચ: '+esc(s.market_cost)+
  (m?'<div class="row" style="margin-top:8px;background:#fff">'+bottle(m)+'<div class="i"><b>'+esc(m.n)+'</b><br>'+esc(m.guj)+'<br>₹'+m.price_100+' / 100ml<br>'+esc(m.safety)+' | રાહ: '+m.wait+' દિવસ</div></div><button class="btn s" onclick="addCart(\''+esc(m.n)+'\')">🛒 કાર્ટમાં ઉમેરો</button>':'')+'</div>'+
  '<div class="box" style="background:#fefae0">🛡️ <b>નિવારણ:</b> '+esc(s.prevention)+'</div>'+
  '<div style="margin-top:8px"><button class="btn s" onclick="toggleFav(\''+esc(c.n)+'\')">⭐ ફેવરિટ</button></div></div>');
  $('dres').firstChild.insertAdjacentHTML('beforeend',TR('<button class="btn s" onclick="shareDx()">📋 રિપોર્ટ કોપી કરો</button>'));scanImgs();$('dres').scrollIntoView({behavior:'smooth'})}
/* ---------- Crops ---------- */
function vCrops(){
  var cats=['બધા'].concat(Object.keys(CATG)),h='<h2>🌱 પાક ('+D.crops.length+')</h2><input placeholder="🔎 પાક શોધો (Neem / લીમડો)" value="'+esc(Q)+'" oninput="Q=this.value;listCrops()">';
  h+='<div class="chips">'+cats.map(function(k,i){return '<button class="chip '+(CAT==k?'on':'')+'" onclick="CAT=CATS['+i+'];render()">'+(EM[k]||'🌍')+' '+(CATG[k]||k)+'</button>'}).join('')+'</div><div class="grid" id="cl"></div>';
  setTimeout(listCrops,0);return h}
function listCrops(){
  var q=Q.toLowerCase(),l=D.crops.filter(function(c){return (CAT=='બધા'||c.c==CAT)&&(!q||c.n.toLowerCase().indexOf(q)>-1||c.g.indexOf(Q)>-1)});
  $('cl').innerHTML=TR(l.map(function(c){return '<div class="card" onclick="openCrop(\''+esc(c.n)+'\')">'+ph(cq(c),EM[c.c])+'<div class="t">'+(FAV.indexOf(c.n)>-1?'⭐ ':'')+esc(c.g)+'<small>'+esc(c.n)+'</small></div></div>'}).join('')||'<p>કોઈ પાક મળ્યો નહીં</p>');scanImgs()}
function openCrop(n){
  var c=D.crops.filter(function(x){return x.n==n})[0],s=c.seed;
  $('mbody').innerHTML=TR(ph(cq(c),EM[c.c],1)+'<h2 style="margin-top:10px">'+esc(c.g)+' ('+esc(c.n)+') '+esc(s.special)+'</h2><div class="kv">'+
  '🌱 <b>બીજ:</b> '+esc(s.seed_guj)+'<br>👁️ <b>દેખાવ:</b> '+esc(s.look_guj)+'<br>⚖️ <b>બીજ દર:</b> '+esc(s.rate)+'<br>⏱️ <b>ઉગવાનો સમય:</b> '+esc(s.germ)+'<br>📅 <b>વાવેતર સમય:</b> '+esc(s.season_guj)+'<br>🌾 <b>લણણી:</b> '+esc(s.harvest)+'<br>💧 <b>સંભાળ:</b> '+esc(s.care_guj)+'<br>📖 <b>પદ્ધતિ:</b> '+esc(s.method_guj)+'</div>'+
  '<button class="btn" onclick="CROP=\''+esc(n)+'\';SYM=\'\';closeM();go(\'diag\')">🩺 આ પાકનું નિદાન કરો</button><button class="btn s" onclick="toggleFav(\''+esc(n)+'\');openCrop(\''+esc(n)+'\')">'+(FAV.indexOf(n)>-1?'★ ફેવરિટમાંથી કાઢો':'⭐ ફેવરિટ')+'</button><button class="btn s r" onclick="closeM()">બંધ</button>');
  $('modal').style.display='flex';scanImgs()}
function closeM(){$('modal').style.display='none'}
function toggleFav(n){var i=FAV.indexOf(n);if(i>-1)FAV.splice(i,1);else FAV.push(n);sv('fav',FAV)}
/* ---------- Medicines + cart ---------- */
var MT='બધા';
function vMeds(){
  var ts=['બધા'].concat(Object.keys(MEM)),h='<h2>💊 દવા દુકાન ('+D.meds.length+')</h2><div class="chips">'+ts.map(function(t,i){return '<button class="chip '+(MT==t?'on':'')+'" onclick="MT=MTS['+i+'];render()">'+(MEM[t]||'🏪')+' '+t+'</button>'}).join('')+'</div>';
  h+='<div class="tool" onclick="showCart()" style="text-align:center;font-weight:700">🛒 કાર્ટ ('+CART.length+') - જુઓ</div>';
  return h+D.meds.filter(function(m){return MT=='બધા'||m.type==MT}).map(function(m){return '<div class="row">'+bottle(m)+'<div class="i"><b>'+esc(m.n)+'</b> ('+esc(m.guj)+')<br>'+esc(m.type)+' | ડોઝ: '+esc(m.dosage)+'<br>🎯 '+esc(m.target)+'<br>₹'+m.price_100+'/100ml | ₹'+m.price_1L+'/1L<br>'+esc(m.safety)+' | રાહ '+m.wait+' દિવસ<br><button class="btn s" onclick="addCart(\''+esc(m.n)+'\')">🛒 ઉમેરો</button></div></div>'}).join('')}
function addCart(n){CART.push(n);sv('cart',CART);toast('🛒 કાર્ટમાં ઉમેર્યું')}
function showCart(){
  var t=0,cnt={};CART.forEach(function(n){cnt[n]=(cnt[n]||0)+1});
  var rows=Object.keys(cnt).map(function(n){var m=D.meds.filter(function(x){return x.n==n})[0],p=m?m.price_100*cnt[n]:0;t+=p;return '<div class="row"><div class="i">'+esc(n)+' × '+cnt[n]+'</div><b>₹'+p+'</b></div>'}).join('')||'<p>કાર્ટ ખાલી છે</p>';
  $('mbody').innerHTML=TR('<h2>🛒 ખરીદી કાર્ટ</h2>'+rows+'<h3>કુલ: ₹'+t+' (100ml ભાવ મુજબ)</h3><button class="btn s" onclick="window.print()">🖨️ પ્રિન્ટ</button><button class="btn s r" onclick="CART=[];sv(\'cart\',CART);showCart()">🗑️ ખાલી કરો</button><button class="btn s" onclick="closeM()">બંધ</button>');
  $('modal').style.display='flex'}
/* ---------- Tools ---------- */
function vTools(){
  var fo=Object.keys(D.fert).map(function(k){return '<option>'+k+'</option>'}).join('');
  var mo=D.meds.map(function(m,i){return '<option value="'+i+'">'+esc(m.n)+' ('+esc(m.dosage)+')</option>'}).join('');
  return '<h2>🧰 ખેતી સાધનો</h2>'+newTools()+
  '<div class="tool"><h3>🧪 ખાતર કેલ્ક્યુલેટર</h3><select id="fc">'+fo+'</select><input id="fa" type="number" placeholder="એકર ['+ACR()+']"><button class="btn" onclick="fert()">ગણતરી</button><div id="fo"></div></div>'+
  '<div class="tool"><h3>🧴 સ્પ્રે ટાંકી કેલ્ક્યુલેટર</h3><select id="sm">'+mo+'</select><input id="st" type="number" placeholder="પંપ લિટર [15]"><input id="sp" type="number" placeholder="કેટલા પંપ [1]" style="margin-top:6px"><button class="btn" onclick="spray()">ગણતરી</button><div id="so"></div></div>'+
  '<div class="tool"><h3>🌦️ હવામાન રોગ જોખમ</h3><input id="rt" type="number" placeholder="તાપમાન °C [28]"><input id="rh" type="number" placeholder="ભેજ % [70]" style="margin-top:6px"><input id="rr" type="number" placeholder="3 દિવસ વરસાદ mm [0]" style="margin-top:6px"><button class="btn" onclick="live()" style="background:#0077b6">📡 લાઈવ હવામાન (મારું લોકેશન)</button><button class="btn" onclick="risk()">તપાસો</button><div id="ro"></div></div>'+
  '<div class="tool"><h3>⏳ લણણી સલામતી</h3><select id="hm">'+mo+'</select><input id="hd" type="number" placeholder="છંટકાવને કેટલા દિવસ થયા [0]"><button class="btn" onclick="harv()">ચેક કરો</button><div id="ho"></div></div>'+
  '<div class="tool"><h3>📐 એકમ કન્વર્ટર</h3><select id="uc"><option value="1">એકર → વીઘા</option><option value="2">વીઘા → એકર</option><option value="3">એકર → હેક્ટર</option><option value="4">ક્વિન્ટલ → કિલો</option><option value="5">મણ → કિલો</option></select><input id="uv" type="number" placeholder="કિંમત [1]"><button class="btn" onclick="conv()">બદલો</button><div id="uo"></div></div>'+
  '<div class="tool"><h3>🌤️ હવામાન સલાહ</h3><div class="chips" style="flex-wrap:wrap"><button class="chip" onclick="wx(0)">☀️ તડકો</button><button class="chip" onclick="wx(1)">🌧️ વરસાદ</button><button class="chip" onclick="wx(2)">☁️ વાદળ</button><button class="chip" onclick="wx(3)">💨 પવન</button><button class="chip" onclick="wx(4)">🔥 ગરમી</button><button class="chip" onclick="wx(5)">❄️ ઠંડી</button></div><div id="wo"></div></div>'}
function out(id,h){$(id).innerHTML=TR('<div class="out">'+h+'</div>')}
function fert(){var k=$('fc').value,a=num('fa',ACR()),f=D.fert[k];out('fo','🌱 '+k+' - '+a+' એકર<br>N: '+(f[0]*a).toFixed(1)+' kg | P: '+(f[1]*a).toFixed(1)+' kg | K: '+(f[2]*a).toFixed(1)+' kg<br>યુરિયા: '+(f[0]*a*2.17).toFixed(1)+' kg<br>DAP: '+(f[1]*a*2.17).toFixed(1)+' kg<br>MOP: '+(f[2]*a*1.67).toFixed(1)+' kg')}
function spray(){var m=D.meds[$('sm').value],t=num('st',15),p=num('sp',1),r=/^([\d.]+)\s*([a-zA-Z]+)/.exec(m.dosage);if(!r){out('so','ડોઝ: '+esc(m.dosage)+' (લેબલ મુજબ)');return}
  out('so','💊 '+esc(m.n)+'<br>ડોઝ '+esc(m.dosage)+'<br>1 પંપ ('+t+' L): '+(r[1]*t).toFixed(1)+' '+r[2]+'<br>'+p+' પંપ: '+(r[1]*t*p).toFixed(1)+' '+r[2]+'<br>🛡️ '+esc(m.safety)+' | રાહ '+m.wait+' દિવસ<br>⚠️ મોજા/માસ્ક પહેરો, પવનની દિશામાં છાંટો.')}
function risk(){var t=num('rt',28),h=num('rh',70),r=num('rr',0),s=0,n=[];
  if(h>=80){s+=2;n.push('ભેજ ખૂબ વધારે → ફૂગ/બ્લાઈટ')}else if(h>=65){s+=1;n.push('ભેજ મધ્યમ-વધુ')}
  if(t>=20&&t<=30&&h>=70){s+=1;n.push('ગરમ-ભેજવાળું હવામાન ફૂગ માટે અનુકૂળ')}
  if(r>=20){s+=2;n.push('વધુ વરસાદ → મૂળ સડો, માઈલ્ડ્યુ')}else if(r>0){s+=1;n.push('પાન ભીના રહે')}
  if(t>=35&&h<50){s+=1;n.push('ગરમ-સૂકું → થ્રિપ્સ, માઈટ્સ')}
  var L=s>=5?['🔴 ઊંચું','તાત્કાલિક ખેતર તપાસો અને નિવારક છંટકાવ કરો.']:s>=3?['🟠 મધ્યમ','2 દિવસમાં પાન તપાસો, નીમ સ્પ્રે કરો.']:['🟢 નીચું','સામાન્ય દેખરેખ.'];
  out('ro','📊 જોખમ: <b>'+L[0]+'</b> (સ્કોર '+s+'/7)<br>'+n.map(function(x){return '• '+x}).join('<br>')+'<br>💡 '+L[1])}
function harv(){var m=D.meds[$('hm').value],d=num('hd',0);out('ho',d>=m.wait?'✅ સુરક્ષિત! '+m.wait+' દિવસની રાહ પૂર્ણ.':'❌ હજી '+(m.wait-d)+' દિવસ રાહ જુઓ (કુલ '+m.wait+').')}
function conv(){var c=$('uc').value,v=num('uv',1),r={1:v*2.5+' વીઘા',2:(v/2.5).toFixed(2)+' એકર',3:(v*0.4047).toFixed(3)+' હેક્ટર',4:v*100+' કિલો',5:v*20+' કિલો'};out('uo',v+' → <b>'+r[c]+'</b><br><small>વીઘા માપ વિસ્તાર મુજબ બદલાય.</small>')}
function wx(i){var a=['પાણી સવારે/સાંજે. છંટકાવ સાંજે.','ફૂગ રોગ ધ્યાન. ડ્રેનેજ રાખો.','પાણી ઓછું. જીવાત તપાસો.','છંટકાવ ટાળો. છોડને ટેકો આપો.','દિવસે પાણી નહીં, સાંજે આપો.','છોડ ઢાંકો. ઓછું પાણી.'];out('wo','💡 '+a[i])}
/* ---------- More ---------- */
function vMore(){
  var r=Object.keys(D.recipes).map(function(k){var x=D.recipes[k];return '<div class="tool"><b>🌿 '+esc(k)+'</b><div class="kv">🧪 '+esc(x.items)+'<br>🎯 '+esc(x.use)+'<br>💰 '+esc(x.cost)+'</div></div>'}).join('');
  var sc=D.schemes.map(function(x){return '<div class="row"><div class="i"><b>'+esc(x[0])+'</b><br>'+esc(x[1])+'</div></div>'}).join('');
  var hi=HIST.map(function(h){return '<div class="row"><div class="i">'+esc(h.g)+' ('+esc(h.c)+') - '+esc(h.s)+'<br><small>'+esc(h.t)+' | '+esc(h.sev)+'</small></div></div>'}).join('')||'<p>હજી કોઈ નિદાન નથી</p>';
  var fv=FAV.map(function(n){return '<span class="chip" onclick="openCrop(\''+esc(n)+'\')">⭐ '+esc(n)+'</span> '}).join('')||'<p>કોઈ ફેવરિટ નથી</p>';
  var di=DIARY.map(function(d){return '<div class="row"><div class="i">'+uT(d.n)+'<br><small>'+esc(d.t)+'</small></div></div>'}).join('');
  return '<div class="tool"><button class="btn" onclick="dlReport()">📄 રિપોર્ટ ડાઉનલોડ (TXT)</button></div><h2>🚨 ઈમરજન્સી હેલ્પલાઈન</h2><div class="tool" style="background:#ffe5e5"><b>📞 કિસાન કોલ સેન્ટર: <a href="tel:18001801551">1800-180-1551</a></b><br>🚑 એમ્બ્યુલન્સ 108 | 🚓 પોલીસ 112<br>⚠️ દવાનું ઝેર: તરત ડૉક્ટર પાસે જાઓ, દવાનું પેકેટ સાથે લઈ જાઓ.</div>'+
  '<h2>📔 ખેતર ડાયરી</h2><input id="dn" placeholder="નવી નોંધ લખો"><button class="btn" onclick="addDiary()">✍️ સાચવો</button>'+di+
  '<h2 style="margin-top:14px">⭐ ફેવરિટ પાક</h2>'+fv+'<h2 style="margin-top:14px">📜 નિદાન ઇતિહાસ</h2>'+hi+
  '<button class="btn s r" onclick="if(confirm(\'બધો ઇતિહાસ કાઢી નાખવો?\')){HIST=[];sv(\'hist\',HIST);render()}">🗑️ ઇતિહાસ સાફ</button>'+
  '<h2 style="margin-top:14px">🏡 જૈવિક રેસીપી બુક</h2>'+r+'<h2>🏛️ સરકારી યોજનાઓ</h2>'+sc+'<p style="font-size:12px;margin-top:6px">ℹ️ નવીનતમ શરતો માટે નજીકની ખેતી કચેરી તપાસો.</p>'}
function addDiary(){var v=$('dn').value.trim();if(!v)return;DIARY.unshift({n:v,t:new Date().toLocaleString()});sv('diary',DIARY);addPts(1,'ડાયરી');render()}
/* ---------- v2: Points, theme, toast ---------- */
var PTS=ls('pts',0),THEME=ls('theme','l'),RM=ls('rm',[]),QS=ls('qs',{c:0,t:0}),QZ=null,LASTDX=null;
var BADGES=[[20,'🌱 નવો કિસાન'],[60,'🌿 કુશળ કિસાન'],[150,'🌾 માસ્ટર કિસાન'],[300,'🏆 ચેમ્પિયન'],[600,'👑 કિસાન રાજા']];
function myBadge(){var b='🌰 શરૂઆત';BADGES.forEach(function(x){if(PTS>=x[0])b=x[1]});return b}
function hdr(){$('pts').innerHTML=TR('✨ '+PTS+' પોઈન્ટ | '+myBadge())}
function addPts(n,why){var old=myBadge();PTS+=n;sv('pts',PTS);hdr();toast('✨ +'+n+' પોઈન્ટ'+(why?' ('+why+')':''));if(myBadge()!=old)setTimeout(function(){toast('🏆 નવો બેજ: '+myBadge())},1800)}
function toast(m){var t=document.createElement('div');t.className='toast';t.textContent=TR(m);document.body.appendChild(t);setTimeout(function(){t.style.opacity=0},1600);setTimeout(function(){t.remove()},2100)}
function applyTheme(){document.body.className=THEME=='d'?'dk':''}
function toggleTheme(){THEME=THEME=='d'?'l':'d';sv('theme',THEME);applyTheme()}
/* ---------- Bottle illustration for medicines ---------- */
var BC={'કીટકનાશક':['#e76f51','#f4a261'],'ફૂગનાશક':['#2a9d8f','#76c893'],'નીંદણનાશક':['#e9c46a','#f4e285'],'માટી સુધારક':['#8d6e63','#bcaaa4']};
function bottle(m){var c=BC[m.type]||['#457b9d','#a8dadc'],w=(m.n.split(' ')[0]).slice(0,9);
  return '<div class="ph" style="background:linear-gradient(135deg,'+c[1]+'55,#fff)"><svg viewBox="0 0 60 80" style="height:92%"><rect x="22" y="4" width="16" height="10" rx="2" fill="#333"/><rect x="25" y="14" width="10" height="8" fill="'+c[0]+'"/><rect x="12" y="22" width="36" height="52" rx="8" fill="'+c[0]+'"/><rect x="16" y="38" width="28" height="24" rx="3" fill="#fff"/><text x="30" y="52" font-size="5.5" text-anchor="middle" fill="#222" font-weight="700">'+esc(w)+'</text><text x="30" y="59" font-size="4" text-anchor="middle" fill="#555">'+esc(m.dosage)+'</text><rect x="16" y="26" width="6" height="40" rx="3" fill="#fff" opacity=".25"/></svg></div>'}
/* ---------- Share / report ---------- */
function shareDx(){if(!LASTDX)return;cpText(TR(LASTDX))}
function dlReport(){
  var L=['SMART HEALTH & CROP GUARD - REPORT','Date: '+new Date().toLocaleString(),'Farmer: '+(PROF.name||'-')+' | Village: '+(PROF.village||'-')+' | Land: '+(PROF.bigha||'-')+' bigha','Points: '+PTS+' | '+TR(myBadge()),'','DIAGNOSIS HISTORY'];
  HIST.forEach(function(h){L.push(h.t+' | '+h.c+' | '+h.s+' | '+h.sev)});L.push('','FAVORITES: '+FAV.join(', '),'','DIARY');
  DIARY.forEach(function(d){L.push(d.t+' | '+d.n)});
  var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([L.join('\n')],{type:'text/plain;charset=utf-8'}));a.download='crop_guard_report.txt';a.click();toast('📄 રિપોર્ટ ડાઉનલોડ થયો')}
/* ---------- New tools ---------- */
var MN=['જાન્યુ','ફેબ્રુ','માર્ચ','એપ્રિલ','મે','જૂન','જુલાઈ','ઓગસ્ટ','સપ્ટેમ્બર','ઓક્ટોબર','નવેમ્બર','ડિસેમ્બર'];
function mIdx(s){var map={'જાન્યુ':0,'ફેબ્રુ':1,'માર્ચ':2,'એપ્રિ':3,'મે':4,'જૂન':5,'જુલાઈ':6,'ઓગસ્ટ':7,'સપ્ટે':8,'ઓક્ટો':9,'નવે':10,'ડિસે':11};for(var k in map){if(s.indexOf(k)==0)return map[k]}return -1}
function inSeason(se,m){if(se.indexOf('આખું')>-1)return true;if(se.indexOf('વસંત')>-1)return m==1||m==2;
  var p=se.split('-');if(p.length<2)return false;var a=mIdx(p[0]),b=mIdx(p[1]);if(a<0||b<0)return false;return a<=b?(m>=a&&m<=b):(m>=a||m<=b)}
function plan(){var m=parseInt($('pm').value),l=D.crops.filter(function(c){return inSeason(c.season,m)});
  out('po','📅 <b>'+MN[m]+'</b> માં વાવેતર લાયક: <b>'+l.length+'</b> પાક<div class="chips" style="flex-wrap:wrap">'+l.map(function(c){return '<span class="chip" onclick="openCrop(\''+esc(c.n)+'\')">'+EM[c.c]+' '+esc(c.g)+'</span>'}).join('')+'</div>')}
function cmp(){var a=D.crops.filter(function(x){return x.n==$('ca').value})[0],b=D.crops.filter(function(x){return x.n==$('cb').value})[0];if(!a||!b)return;
  var F=[['seed_guj','🌱 બીજ'],['rate','⚖️ બીજ દર'],['germ','⏱️ ઉગવું'],['season_guj','📅 વાવેતર'],['harvest','🌾 લણણી'],['care_guj','💧 સંભાળ']];
  out('co','<table style="width:100%;font-size:13px;border-collapse:collapse"><tr><td></td><td>'+ph(a.w+'|'+a.n,EM[a.c])+'</td><td>'+ph(b.w+'|'+b.n,EM[b.c])+'</td></tr><tr><th></th><th>'+esc(a.g)+'</th><th>'+esc(b.g)+'</th></tr>'+F.map(function(f){return '<tr style="border-top:1px solid #ccc"><td><b>'+f[1]+'</b></td><td>'+esc(a.seed[f[0]])+'</td><td>'+esc(b.seed[f[0]])+'</td></tr>'}).join('')+'</table>');scanImgs()}
function profit(){var ac=num('pa',ACR()),y=num('py',10),r=num('pr',2000),c=num('pc',15000),inc=ac*y*r,cost=ac*c,p=inc-cost;
  out('pro','💵 આવક: ₹'+inc.toLocaleString()+'<br>💸 ખર્ચ: ₹'+cost.toLocaleString()+'<br>'+(p>=0?'✅ નફો':'❌ ખોટ')+': <b>₹'+Math.abs(p).toLocaleString()+'</b> ('+(cost?(p/cost*100).toFixed(0):0)+'%)<br>📐 પ્રતિ એકર: ₹'+(p/ac).toFixed(0))}
function live(){
  if(!navigator.geolocation){toast('📍 લોકેશન સપોર્ટ નથી');return}
  out('ro','📡 લોકેશન મેળવી રહ્યા છીએ...');
  navigator.geolocation.getCurrentPosition(function(p){
    fetch('https://api.open-meteo.com/v1/forecast?latitude='+p.coords.latitude+'&longitude='+p.coords.longitude+'&current=temperature_2m,relative_humidity_2m&daily=precipitation_sum&past_days=3&forecast_days=1&timezone=auto')
    .then(function(r){return r.json()}).then(function(j){var rain=0;j.daily.precipitation_sum.slice(0,3).forEach(function(x){rain+=x||0});
      $('rt').value=j.current.temperature_2m;$('rh').value=j.current.relative_humidity_2m;$('rr').value=rain.toFixed(1);risk();toast('📡 લાઈવ હવામાન લોડ થયું')})
    .catch(function(){out('ro','⚠️ ઈન્ટરનેટ/હવામાન ડેટા મળ્યો નહીં. હાથથી લખો.')})
  },function(){out('ro','⚠️ લોકેશન પરવાનગી મળી નથી. તાપમાન/ભેજ હાથથી લખો.')},{timeout:10000})}
function newTools(){
  var co=D.crops.map(function(c){return '<option value="'+esc(c.n)+'">'+esc(c.g)+' ('+esc(c.n)+')</option>'}).join('');
  var mo=MN.map(function(m,i){return '<option value="'+i+'"'+(i==new Date().getMonth()?' selected':'')+'>'+m+'</option>'}).join('');
  return '<div class="tool"><h3>📅 આ મહિને શું વાવવું?</h3><select id="pm">'+mo+'</select><button class="btn" onclick="plan()">પાક બતાવો</button><div id="po"></div></div>'+
  '<div class="tool"><h3>⚖️ બે પાકની સરખામણી</h3><select id="ca">'+co+'</select><select id="cb" style="margin-top:6px">'+co+'</select><button class="btn" onclick="cmp()">સરખામણી કરો</button><div id="co"></div></div>'+
  '<div class="tool"><h3>💰 નફો કેલ્ક્યુલેટર</h3><input id="pa" type="number" placeholder="એકર ['+ACR()+']"><input id="py" type="number" placeholder="ઉત્પાદન ક્વિન્ટલ/એકર [10]" style="margin-top:6px"><input id="pr" type="number" placeholder="ભાવ ₹/ક્વિન્ટલ [2000]" style="margin-top:6px"><input id="pc" type="number" placeholder="ખર્ચ ₹/એકર [15000]" style="margin-top:6px"><button class="btn" onclick="profit()">ગણતરી</button><div id="pro"></div></div>'}
/* ---------- Reminders ---------- */
function addRm(){var t=$('rmt').value.trim(),d=$('rmd').value;if(!t||!d){toast('લખાણ અને તારીખ નાખો');return}RM.push({t:t,d:d,x:0});sv('rm',RM);addPts(1,'રિમાઇન્ડર');render()}
function doneRm(i){RM[i].x=1;sv('rm',RM);render()}
function delRm(i){RM.splice(i,1);sv('rm',RM);render()}
function checkDue(){var td=new Date().toISOString().slice(0,10),n=RM.filter(function(r){return !r.x&&r.d<=td}).length;if(n)setTimeout(function(){toast('⏰ '+n+' રિમાઇન્ડર બાકી છે!')},2200)}
/* ---------- Quiz ---------- */
function shuf(a){return a.slice().sort(function(){return Math.random()-.5})}
function uniq(a){return a.filter(function(x,i){return x&&a.indexOf(x)==i})}
function newQ(){
  for(var k=0;k<30;k++){var t=Math.floor(Math.random()*4),c=D.crops[Math.floor(Math.random()*D.crops.length)],q,ans,pool;
    if(t==0){q='🌱 "'+c.g+'" નું વાવેતર ક્યારે થાય?';ans=c.seed.season_guj;pool=uniq(D.crops.map(function(x){return x.seed.season_guj}))}
    else if(t==1){q='⏱️ "'+c.g+'" નું બીજ ઉગતા કેટલો સમય લાગે?';ans=c.seed.germ;pool=uniq(D.crops.map(function(x){return x.seed.germ}))}
    else if(t==2){q='🗂️ "'+c.g+'" ('+c.n+') ક્યા વર્ગનો પાક છે?';ans=CATG[c.c];pool=Object.keys(CATG).map(function(x){return CATG[x]})}
    else{var m=D.meds[Math.floor(Math.random()*D.meds.length)];q='💊 "'+m.n+'" ક્યા પ્રકારની દવા છે?';ans=m.type;pool=Object.keys(MEM)}
    var o=shuf(pool.filter(function(x){return x!=ans})).slice(0,3);if(!ans||o.length<3)continue;
    o.push(ans);QZ={q:q,o:shuf(o),a:ans,d:-1};return}
}
function ansQ(i){if(QZ.d>-1)return;QZ.d=i;QS.t++;if(QZ.o[i]==QZ.a){QS.c++;addPts(5,'સાચો જવાબ')}sv('qs',QS);render()}
function vPlay(){
  if(!QZ)newQ();
  var h='<h2>🎓 કિસાન ક્વિઝ</h2><div class="tool"><div style="font-weight:700;margin-bottom:8px">'+QZ.q+'</div>'+QZ.o.map(function(o,i){var st='';if(QZ.d>-1){if(o==QZ.a)st='background:#52b788;color:#fff';else if(i==QZ.d)st='background:#e63946;color:#fff'}return '<button class="btn" style="background:#fff;color:#222;border:2px solid #d8f3dc;margin-top:6px;text-align:left;'+st+'" onclick="ansQ('+i+')">'+esc(o)+'</button>'}).join('')+
  (QZ.d>-1?'<div class="out">'+(QZ.o[QZ.d]==QZ.a?'✅ સાચો જવાબ! +5 પોઈન્ટ':'❌ સાચો જવાબ: <b>'+esc(QZ.a)+'</b>')+'</div><button class="btn" onclick="QZ=null;render()">➡️ આગળનો પ્રશ્ન</button>':'')+'</div>'+
  '<div class="tool">📊 સ્કોર: <b>'+QS.c+'/'+QS.t+'</b> | ✨ પોઈન્ટ: <b>'+PTS+'</b><br>🏅 બેજ: <b>'+myBadge()+'</b><br><small>'+BADGES.map(function(b){return (PTS>=b[0]?'✅ ':'🔒 ')+b[1]+' ('+b[0]+')'}).join('<br>')+'</small></div>'+
  '<h2>⏰ રિમાઇન્ડર (છંટકાવ/પાણી/ખાતર)</h2><input id="rmt" placeholder="દા.ત. કપાસમાં દવા છાંટવી"><input id="rmd" type="date" style="margin-top:6px"><button class="btn" onclick="addRm()">➕ ઉમેરો</button>';
  var td=new Date().toISOString().slice(0,10);
  h+=RM.map(function(r,i){var late=!r.x&&r.d<td;return '<div class="row" style="margin-top:8px"><div class="i" style="'+(r.x?'text-decoration:line-through;opacity:.6':'')+'">'+(late?'🔴 ':r.x?'✅ ':'⏰ ')+(r.c?'🌾 '+esc(rcn(r.c))+' લણણી':uT(r.t))+'<br><small>'+esc(r.d)+(late?' (મોડું!)':'')+'</small></div>'+(r.x?'':'<button class="btn s" onclick="doneRm('+i+')">✔</button>')+'<button class="btn s r" onclick="delRm('+i+')">✖</button></div>'}).join('');
  return h}
/* ================= v3: 3 languages / registration / home / weather / news / accounts ================= */
var LANG=ls('lang','gu'),PROF=ls('prof',{}),DR=null,I={},PD=null,LG=ls('ledger',[]),LK='out';
if(['gu','hi','en'].indexOf(LANG)<0)LANG='gu';
if(!PROF||typeof PROF!='object')PROF={};
if(!(LG instanceof Array))LG=[];
var LN={gu:'ગુજરાતી',hi:'हिन्दी',en:'English'},LNS={gu:'ગુ',hi:'हि',en:'EN'};
var CATS=['બધા'].concat(Object.keys(CATG)),MTS=['બધા'].concat(Object.keys(MEM));
var GRE=/[\u0A80-\u0AFF]+(?:(?:[ \-]|\.(?=[\u0A80-\u0AFF]))[\u0A80-\u0AFF]+)*/g;
function g2d(s){return s.replace(/[\u0A81-\u0AEF]/g,function(c){return String.fromCharCode(c.charCodeAt(0)-384)})}
function has(k){return Object.prototype.hasOwnProperty.call(I,k)}
function xl(v,o){return (v===''&&LANG=='hi')?g2d(o):v}
function trTok(w){
  if(has(w))return xl(I[w],w);
  return w.replace(/[\u0A80-\u0AFF]+/g,function(p){return has(p)?xl(I[p],p):(LANG=='hi'?g2d(p):p)})}
function trRun(r){
  if(has(r))return xl(I[r],r);
  var w=r.split(' '),o=[],i=0,j,ph,hit;
  while(i<w.length){hit=false;
    for(j=Math.min(w.length,i+6);j>i+1;j--){ph=w.slice(i,j).join(' ');if(has(ph)){o.push(xl(I[ph],ph));i=j;hit=true;break}}
    if(!hit){o.push(trTok(w[i]));i++}}
  return o.join(' ')}
/* TR: translate Gujarati text in an HTML/text string to the chosen language (no-op for Gujarati) */
function TR(h){
  if(h==null)return '';h=String(h);
  if(LANG=='gu')return h.replace(/\u2063/g,'');
  var p=h.split('\u2063'),i;
  for(i=0;i<p.length;i+=2)p[i]=p[i].replace(GRE,trRun);
  var o=p.join('');
  if(LANG=='en')o=o.replace(/([A-Za-z][A-Za-z ]*[A-Za-z]) \(\1\)/g,'$1').replace(/\(([A-Za-z ]+) \/ \1\)/g,'($1)').replace(/>((?:⭐ )?)([^<>]+)<small>\2<\/small>/g,'>$1$2<');
  return o}
function uT(s){return '\u2063'+esc(s)+'\u2063'}   /* user text: never translated */
function fm(n){return Math.round(n).toLocaleString('en-IN')}
function ACR(){var b=parseFloat(PROF&&PROF.bigha);return b>0?+(b*0.4).toFixed(2):1}
function loc(R){
  var o={},k;for(k in R)o[k]=R[k];
  o.crops=R.crops.map(function(c){var n={},s={},k2;for(k2 in c)n[k2]=c[k2];for(k2 in c.seed)s[k2]=c.seed[k2];n.seed=s;
    if(LANG=='hi'){n.g=c.h||c.g;s.seed_guj=s.seed_hin||s.seed_guj;s.look_guj=s.look_hin||s.look_guj;s.method_guj=s.method_hin||s.method_guj}
    else if(LANG=='en'){n.g=c.n;s.seed_guj=c.n+' seed'}
    return n});
  if(LANG=='en')o.meds=R.meds.map(function(m){var x={},q;for(q in m)x[q]=m[q];var g=String(m.n).replace(/\s+(?=[\d(]).*$/,'');x.guj=(g&&g!==m.n)?g:m.type;return x});
  if(LANG!='gu'){var rc={};Object.keys(R.recipes).forEach(function(k){var x=R.recipes[k],y={},q;for(q in x)y[q]=x[q];y.items=String(x.items).replace(/ગોળ/g,'ગૂળ');rc[k]=y});o.recipes=rc}
  return o}
function setLang(l){
  LANG=l;sv('lang',l);I=(DR&&DR.tr&&DR.tr[l])||{};if(DR)D=loc(DR);QZ=null;document.documentElement.lang=l;
  var b=$('lgb');if(b)b.textContent='🌐 '+LNS[l];
  var hs=$('hsub');if(hs)hs.innerHTML=TR('ડિજિટલ પ્લાન્ટ ડૉક્ટર')+' | Created by Mr_SK';
  hdr();if($('app').style.display=='flex'){nav();render()}}
function cycleLang(){var o=['gu','hi','en'];setLang(o[(o.indexOf(LANG)+1)%3])}

/* ---------- registration ---------- */
function readSetup(){var n=$('s_n');if(!n)return;PD={name:n.value,village:$('s_v').value,bigha:$('s_b').value}}
function pickLang(k){readSetup();setLang(k);drawSetup()}
function drawSetup(){
  var d=PD||{name:PROF.name||'',village:PROF.village||'',bigha:PROF.bigha||''},ed=$('app').style.display=='flex';
  var lb=['gu','hi','en'].map(function(k){return '<button class="'+(LANG==k?'on':'')+'" onclick="pickLang(\''+k+'\')">'+LN[k]+'</button>'}).join('');
  $('setup').innerHTML='<div class="ph sbg" data-q="Rice paddy|rice paddy field farmer India"></div><div class="sbox"><div class="slogo"><img src="/icon.svg" alt=""></div><h2>'+TR('સ્વાગત છે')+'!</h2><p class="ssub">'+TR('શરૂ કરતા પહેલા તમારી માહિતી આપો')+'</p>'+
  '<label>🌐 '+TR('ભાષા પસંદ કરો')+'</label><div class="lg">'+lb+'</div>'+
  '<label>👨‍🌾 '+TR('ખેડૂતનું નામ')+'</label><input id="s_n" value="'+esc(d.name)+'" placeholder="'+esc(TR('તમારું પૂરું નામ લખો'))+'">'+
  '<label>🏡 '+TR('ગામનું નામ')+'</label><input id="s_v" value="'+esc(d.village)+'" placeholder="'+esc(TR('તમારા ગામનું નામ લખો'))+'">'+
  '<label>🌾 '+TR('કુલ ખેતર વીઘામાં')+'</label><input id="s_b" type="number" step="any" min="0" value="'+esc(d.bigha)+'" placeholder="'+TR('દા.ત')+'. 5">'+
  '<button class="btn" onclick="submitSetup()">🚀 '+TR('એપ ખોલો')+'</button>'+(ed?'<button class="btn s r" onclick="closeSetup()">'+TR('બંધ')+'</button>':'')+'</div>';
  var bg=document.querySelector('#setup .sbg');if(bg)loadImg(bg)}
function submitSetup(){
  var n=$('s_n').value.trim(),v=$('s_v').value.trim(),b=parseFloat($('s_b').value);
  if(!n||!v||isNaN(b)||b<=0){alert(TR('કૃપા કરીને નામ ગામ અને વીઘા સાચી રીતે લખો'));return}
  var same=(PROF.village==v);
  PROF={name:n,village:v,bigha:b,lat:same?PROF.lat:null,lon:same?PROF.lon:null,place:same?PROF.place:'',gv:same?PROF.gv:''};
  sv('prof',PROF);PD=null;WX=null;TAB='home';
  $('setup').style.display='none';$('app').style.display='flex';
  applyTheme();hdr();nav();render();checkDue();window.scrollTo(0,0)}
function closeSetup(){PD=null;$('setup').style.display='none'}
function openSetup(){PD=null;drawSetup();$('setup').style.display='flex'}

/* ---------- home: core icons + learn icons ---------- */
function vHome(){
  var p=PROF||{},T=[
   ['diag','🩺','પાક રોગ તપાસ','રોગ અને જીવાત','Plant pathology|plant leaf disease','#2d6a4f'],
   ['crops','🌱','પાકની માહિતી','બીજ વાવેતર લણણી','Wheat|wheat field crop','#40916c'],
   ['seeds','🌰','બીજ સંગ્રહ','ફોટા સાથે બધા બીજ','Seed|seeds in hand','#8d6e2f'],
   ['meds','💊','દવા દુકાન','દવા ખાતર ભાવ','Pesticide|pesticide spraying farm','#0077b6'],
   ['tools','🧰','ખેતી સાધનો','ખાતર સ્પ્રે ગણતરી','Tractor|tractor farm field','#bc6c25'],
   ['wx','🌦️','હવામાન અને તાપમાન','દરેક દિવસનું તાપમાન','Monsoon|monsoon rain clouds field','#0096c7'],
   ['news','📰','SK News','આજના ખેડૂત સમાચાર','Newspaper|newspaper','#6a4c93'],
   ['ledger','📒','ખેતીનો હિસાબ','આવક ખર્ચ નફો','Indian rupee|indian rupee banknotes','#2a9d8f'],
   ['track','🌾','મારો પાક ટ્રેકર','વાવેતરથી લણણી સુધી','Crop|crop growing field','#52796f'],
   ['play','🎓','કિસાન ક્વિઝ','જ્ઞાન ચકાસો','Sunflower|sunflower field','#e9a100'],
   ['more','🏛️','વધુ માહિતી','યોજના રેસીપી ડાયરી','Village|village india farm','#9b2226']];
  var N=[['fg','📚','Agriculture|farming crops field','#386641'],['mkf','🪱','Vermicompost|vermicompost worms compost','#6f4e37'],
   ['mkp','🧴','Neem|neem leaves tree','#2d6a4f'],['mkt','✂️','Grafting|grafting plant','#7f5539'],
   ['i_soil','🏜️','Soil|soil field farm','#9c6644'],['i_irr','💧','Drip irrigation|drip irrigation field','#0077b6'],
   ['i_pest','🐛','Pest (organism)|crop pest insect','#bc4749'],['i_dis','🍄','Plant disease|plant leaf disease','#6a994e'],
   ['i_org','🌿','Organic farming|organic farm','#386641'],['i_cal','🗓️','Crop|crops harvest field','#e07a5f'],
   ['i_adv','🌤️','Weather forecasting|weather clouds sky','#0096c7'],['i_safe','🦺','Personal protective equipment|protective suit farmer','#d62828'],
   ['i_gloss','📖','Glossary|dictionary book','#5e548e'],['i_tip','💡','Idea|light bulb','#e9a100'],
   ['i_mach','🚜','Tractor|farm tractor','#bc6c25'],['i_animal','🐄','Dairy cattle|cow dairy farm','#7f4f24'],
   ['i_store','📦','Granary|grain storage','#8d6e2f']];
  var h='<div class="hello"><div class="ph hp" data-q="Agriculture in India|green farmland India crops"></div><div class="ht">🙏 '+'નમસ્તે'+' <b>'+uT(p.name)+'</b><br><small>🏡 '+'ગામ'+': '+uT(p.village)+' | 🌾 '+'ખેતર'+': '+esc(p.bigha)+' '+'વીઘા'+' (≈ '+ACR()+' '+'એકર'+')</small></div></div>';
  h+='<div class="wxm" id="hwx" onclick="go(\'wx\')">🌡️ હવામાન લોડ થઈ રહ્યું છે...</div><h2 style="margin-top:14px">🔍 શું તપાસવું છે?</h2><div class="ig">';
  h+=T.map(function(t){return '<button class="ic" style="background:'+t[5]+'" onclick="go(\''+t[0]+'\')"><div class="ph tp" data-q="'+esc(t[4])+'"></div><span class="ie">'+t[1]+'</span><b>'+t[2]+'</b><small>'+t[3]+'</small></button>'}).join('');
  h+='</div><h2 style="margin-top:16px">'+X('ui.learn')+'</h2><div class="ig">';
  h+=N.map(function(t){var id=t[0].replace(/^i_/,'');return '<button class="ic" style="background:'+t[3]+'" onclick="go(\''+t[0]+'\')"><div class="ph tp" data-q="'+esc(t[2])+'"></div><span class="ie">'+t[1]+'</span><b>'+X('t.'+id)+'</b><small>'+X('d.'+id)+'</small></button>'}).join('');
  h+='</div>';
  setTimeout(homeWx,0);return h}

/* ---------- weather (Open-Meteo, live) ---------- */
var WX=null,WXT=0,WLOC={gu:'gu-IN',hi:'hi-IN',en:'en-IN'};
function wcode(c){
  if(c==0)return['☀️','સ્વચ્છ આકાશ'];if(c==1)return['🌤️','મોટે ભાગે સ્વચ્છ'];if(c==2)return['⛅','આંશિક વાદળછાયું'];if(c==3)return['☁️','વાદળછાયું'];
  if(c==45||c==48)return['🌫️','ધુમ્મસ'];if(c>=51&&c<=57)return['🌦️','ઝરમર વરસાદ'];if(c==63||c==65||c==67)return['🌧️','ભારે વરસાદ'];
  if(c>=61&&c<=66)return['🌧️','વરસાદ'];if((c>=71&&c<=77)||c==85||c==86)return['❄️','હિમવર્ષા'];if(c>=80&&c<=82)return['🌦️','વરસાદી ઝાપટાં'];
  if(c>=95)return['⛈️','ગાજવીજ સાથે વરસાદ'];return['🌡️','હવામાન']}
function fmtD(s){var p=s.split('-'),d=new Date(+p[0],+p[1]-1,+p[2]);try{return d.toLocaleDateString(WLOC[LANG],{weekday:'short',day:'numeric',month:'short'})}catch(e){return s}}
function setPlace(la,lo,pl,gv){PROF.lat=la;PROF.lon=lo;PROF.place=pl||'';PROF.gv=gv;sv('prof',PROF)}
function getLoc(cb){
  if(PROF.lat!=null&&PROF.lon!=null&&PROF.gv){cb(null);return}
  var v=PROF.village||'';if(!v){cb('noloc');return}
  fetch('https://geocoding-api.open-meteo.com/v1/search?name='+encodeURIComponent(v)+'&count=10&language=en&format=json')
  .then(function(r){return r.json()}).then(function(j){
    var rs=(j.results||[]).filter(function(x){return x.country_code=='IN'});if(!rs.length)throw 0;
    var g=rs.filter(function(x){return x.admin1=='Gujarat'})[0]||rs[0];
    setPlace(g.latitude,g.longitude,[g.name,g.admin1].filter(Boolean).join(', '),v);cb(null)})
  .catch(function(e){cb(e===0?'noloc':'net')})}
function loadWx(force,cb){
  if(WX&&!force&&Date.now()-WXT<600000){cb(WX,null);return}
  getLoc(function(e){
    if(e){cb(null,e);return}
    var k=PROF.lat+','+PROF.lon,u='https://api.open-meteo.com/v1/forecast?latitude='+PROF.lat+'&longitude='+PROF.lon+'&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max,wind_speed_10m_max&hourly=temperature_2m&past_days=3&forecast_days=10&timezone=auto';
    fetch(u).then(function(r){return r.json()}).then(function(j){if(!j.daily||!j.current)throw 0;WX=j;WXT=Date.now();sv('wxc',{t:WXT,k:k,j:j});cb(WX,null)})
    .catch(function(){var c=ls('wxc',null);if(c&&c.k==k&&c.j){WX=c.j;WXT=0;cb(WX,'offline')}else cb(null,'net')})})}
function useGps(){
  if(!navigator.geolocation){toast('📍 લોકેશન સપોર્ટ નથી');return}
  navigator.geolocation.getCurrentPosition(function(p){setPlace(p.coords.latitude,p.coords.longitude,'','gps');WX=null;render()},function(){toast('⚠️ લોકેશન પરવાનગી મળી નથી')},{timeout:10000})}
function wxTip(d,ti){var rn=d.precipitation_sum[ti]||0,mx=d.temperature_2m_max[ti],mn=d.temperature_2m_min[ti];
  return rn>=10?'ભારે વરસાદની શક્યતા ખેતરમાંથી પાણી કાઢો અને છંટકાવ ટાળો':mx>=38?'ખૂબ ગરમી સવાર સાંજ પાણી આપો':mn<=10?'ઠંડી વધુ છે પાકને ઠંડીથી બચાવો':'હવામાન સામાન્ય છે નિયમિત દેખરેખ રાખો'}
function homeWx(){
  loadWx(false,function(w,e){var el=$('hwx');if(!el)return;
    if(!w){el.innerHTML=TR('🌡️ હવામાન લોડ ન થયું ટેપ કરો');return}
    var c=w.current,d=w.daily,ti=d.time.indexOf(String(c.time||'').slice(0,10));if(ti<0)ti=0;var cw=wcode(c.weather_code);
    el.innerHTML=TR('<div class="wm1"><span class="wme">'+cw[0]+'</span><b>'+Math.round(c.temperature_2m)+'°C</b><span class="wmt">'+cw[1]+'</span></div><small>આજ: '+Math.round(d.temperature_2m_min[ti])+'° – '+Math.round(d.temperature_2m_max[ti])+'° | 🌧️ '+(d.precipitation_sum[ti]||0).toFixed(1)+' mm | 💧 '+c.relative_humidity_2m+'%</small><small>ટેપ કરીને દરેક દિવસનું તાપમાન જુઓ ›</small>')})}
function wxBtns(){return '<button class="btn" onclick="useGps()">📍 મારું લોકેશન વાપરો</button><button class="btn" style="background:#0077b6" onclick="WX=null;render()">🔄 ફરી લોડ કરો</button>'}
function wxHtml(w,e){
  var c=w.current,d=w.daily,h=w.hourly,td=String(c.time||'').slice(0,10),ti=d.time.indexOf(td);if(ti<0)ti=Math.min(3,d.time.length-1);
  var cw=wcode(c.weather_code),mn=Math.min.apply(null,d.temperature_2m_min),mx=Math.max.apply(null,d.temperature_2m_max),sp=Math.max(mx-mn,1),
      pl=PROF.gv=='gps'?'મારું લોકેશન':uT(PROF.place||PROF.village);
  var s='<div class="wbig"><div class="wt1">'+cw[0]+' <b>'+Math.round(c.temperature_2m)+'°C</b></div><div>'+cw[1]+'</div><small>📍 '+pl+'</small><small>🌡️ અનુભવાય છે '+Math.round(c.apparent_temperature)+'°C | 💧 ભેજ '+c.relative_humidity_2m+'% | 💨 પવન '+Math.round(c.wind_speed_10m)+' km/h</small></div>';
  s+='<div class="box home">💡 <b>ખેડૂત સલાહ:</b> '+wxTip(d,ti)+'</div>';
  var hr='',k;for(k=0;k<h.time.length;k++){if(h.time[k].slice(0,10)==td&&(+h.time[k].slice(11,13))%3==0)hr+='<div class="hc"><small>'+h.time[k].slice(11,16)+'</small><b>'+Math.round(h.temperature_2m[k])+'°</b></div>'}
  s+='<h3 style="margin-top:12px">🕒 આજના કલાકવાર તાપમાન</h3><div class="hs">'+hr+'</div><h2 style="margin-top:12px">📅 દરેક દિવસનું તાપમાન</h2>';
  for(var i=0;i<d.time.length;i++){
    if(i==0&&ti>0)s+='<h3>⏪ પાછલા દિવસો</h3>';if(i==ti)s+='<h3>⏩ આજ અને આગામી દિવસો</h3>';
    var lo=d.temperature_2m_min[i],hg=d.temperature_2m_max[i],l=(lo-mn)/sp*100,wd=Math.min(Math.max((hg-lo)/sp*100,8),100-l),wc=wcode(d.weather_code[i]),rn=d.precipitation_sum[i]||0,pr=d.precipitation_probability_max?d.precipitation_probability_max[i]:null;
    s+='<div class="wr'+(i<ti?' past':'')+(i==ti?' now':'')+'"><div class="wd"><b>'+(i==ti?'આજ':esc(fmtD(d.time[i])))+'</b><small>'+wc[1]+'</small></div><div class="we">'+wc[0]+'</div><div class="wtp"><span>'+Math.round(lo)+'°</span><div class="bar"><i style="left:'+l.toFixed(0)+'%;width:'+wd.toFixed(0)+'%"></i></div><span>'+Math.round(hg)+'°</span></div><div class="wp">🌧️ '+rn.toFixed(1)+' mm'+(pr!=null?'<small>'+pr+'%</small>':'')+'</div></div>'}
  s+='<small>'+(e=='offline'?'⚠️ જૂનો ડેટા દેખાય છે ઑફલાઇન':'🕒 છેલ્લે અપડેટ '+new Date(WXT).toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'}))+'</small>'+wxBtns();
  return s}
function drawWx(){
  loadWx(false,function(w,e){var b=$('wxb');if(!b)return;
    if(!w){b.innerHTML=TR('<div class="tool">⚠️ '+(e=='noloc'?'ગામનું સ્થાન મળ્યું નહીં તમારું લોકેશન વાપરો':'ઈન્ટરનેટ ચાલુ કરો અને ફરી પ્રયત્ન કરો')+'</div>'+wxBtns());return}
    b.innerHTML=TR(wxHtml(w,e))})}
function vWx(){setTimeout(drawWx,0);return '<h2>🌡️ હવામાન અને તાપમાન</h2><div id="wxb"><div class="tool">⏳ હવામાન લોડ થઈ રહ્યું છે...</div></div>'}

/* ---------- SK News ---------- */
var NSC=ls('nsc','in'),NST=ls('nst','Gujarat'),NC={};
function stName(s){return LANG=='gu'?s[1]:LANG=='hi'?s[2]:s[3]}
function nsState(){return NSC=='in'?'':NSC=='gj'?'Gujarat':NST}
function setNs(k){NSC=k;sv('nsc',k);render()}
function ago(ts){if(!ts)return '';var m=Math.round((Date.now()-ts)/60000);if(m<1)return 'હમણાં જ';if(m<60)return m+' મિનિટ પહેલા';if(m<1440)return Math.round(m/60)+' કલાક પહેલા';return Math.round(m/1440)+' દિવસ પહેલા'}
function vNews(){
  var tb=[['in','🇮🇳','સમગ્ર ભારત'],['gj','📍','ગુજરાત'],['st','🗺️','બીજું રાજ્ય']];
  var h='<h2>📰 SK News</h2><p style="font-size:13px;margin:-4px 0 6px">દરરોજ અપડેટ થતા ખેડૂત સમાચાર</p><div class="chips">'+tb.map(function(t){return '<button class="chip '+(NSC==t[0]?'on':'')+'" onclick="setNs(\''+t[0]+'\')">'+t[1]+' '+t[2]+'</button>'}).join('')+'<button class="chip" onclick="loadNews(true)">🔄</button></div>';
  if(NSC=='st')h+='<label>🗺️ રાજ્ય પસંદ કરો</label><select onchange="NST=this.value;sv(\'nst\',NST);loadNews(false)">'+(D.states||[]).map(function(s){return '<option value="'+esc(s[0])+'"'+(s[0]==NST?' selected':'')+'>'+esc(stName(s))+'</option>'}).join('')+'</select>';
  h+='<div id="nl" style="margin-top:8px"><div class="tool">⏳ સમાચાર લોડ થઈ રહ્યા છે...</div></div>';
  setTimeout(function(){loadNews(false)},0);return h}
function drawNews(o,key){
  var el=$('nl');if(!el||key!=LANG+'|'+nsState())return;
  if(!o.items||!o.items.length){el.innerHTML=TR('<div class="tool">'+(o.ok?'📭 કોઈ સમાચાર મળ્યા નહીં':'⚠️ સમાચાર લોડ ન થયા ઈન્ટરનેટ તપાસો')+'</div>'+'');return}
  el.innerHTML=TR(o.items.map(function(n){return '<div class="nw"><b>'+uT(n.t)+'</b><small>'+(n.s?uT(n.s)+' • ':'')+ago(n.d)+'</small></div>'}).join(''))}
function loadNews(force){
  var st=nsState(),key=LANG+'|'+st,c=NC[key];
  if(!force&&c&&Date.now()-c.t<900000){drawNews(c,key);return}
  var el=$('nl');if(el)el.innerHTML=TR('<div class="tool">⏳ સમાચાર લોડ થઈ રહ્યા છે...</div>');
  fetch('/api/news?lang='+LANG+'&state='+encodeURIComponent(st)).then(function(r){return r.json()}).then(function(j){
    var o={t:Date.now(),items:j.items||[],ok:j.ok,url:j.url};if(j.ok&&o.items.length)NC[key]=o;drawNews(o,key)})
  .catch(function(){drawNews({ok:false,items:[],url:''},key)})}

/* ---------- farm accounts (new feature) ---------- */
function vLedger(){
  var ti=0,to=0,b=parseFloat(PROF.bigha)||1;LG.forEach(function(e){if(e.k=='in')ti+=e.a;else to+=e.a});var pf=ti-to;
  var h='<h2>📒 ખેતીનો હિસાબ</h2><div class="lgs"><div class="lc g"><small>કુલ આવક</small><b>₹'+fm(ti)+'</b></div><div class="lc r"><small>કુલ ખર્ચ</small><b>₹'+fm(to)+'</b></div><div class="lc '+(pf>=0?'g':'r')+'"><small>'+(pf>=0?'ચોખ્ખો નફો':'ચોખ્ખી ખોટ')+'</small><b>₹'+fm(Math.abs(pf))+'</b></div></div>';
  h+='<p style="font-size:12px;text-align:center;margin:6px 0">≈ ₹'+fm(Math.abs(pf)/b)+' / '+'વીઘા'+'</p>';
  h+='<div class="tool"><div class="chips"><button class="chip '+(LK=='out'?'on':'')+'" onclick="LK=\'out\';render()">🔴 ખર્ચ</button><button class="chip '+(LK=='in'?'on':'')+'" onclick="LK=\'in\';render()">🟢 આવક</button></div><input id="la" type="number" placeholder="રકમ ₹"><input id="ln" placeholder="નોંધ લખો" style="margin-top:8px"><button class="btn" onclick="addLg()">➕ ઉમેરો</button></div>';
  h+=LG.length?LG.map(function(e,i){return '<div class="row"><div class="i"><b>'+(e.k=='in'?'🟢':'🔴')+' ₹'+fm(e.a)+'</b><br><small>'+(e.n?uT(e.n)+' • ':'')+esc(fmtD(e.d))+'</small></div><button class="chip" onclick="delLg('+i+')">🗑️</button></div>'}).join(''):'<p>📭 હજી કોઈ નોંધ નથી</p>';
  return h}
function addLg(){var a=num('la',0),n=$('ln').value.trim();if(!(a>0)){toast('⚠️ રકમ સાચી લખો');return}
  LG.unshift({k:LK,a:a,n:n,d:new Date().toISOString().slice(0,10)});sv('ledger',LG);addPts(2,'📒');render()}
function delLg(i){LG.splice(i,1);sv('ledger',LG);render()}


/* ---------- seeds collection (photos of every crop's seeds) ---------- */
var SQ='',SCAT='બધા',sobs=null;
function seedQty(rate){var m=/([\d.]+)(?:-([\d.]+))?\s*(kg|g)\/એકર/.exec(rate||'');if(!m)return '';
  var a=parseFloat(m[1]),b=m[2]?parseFloat(m[2]):a,ac=ACR(),u=m[3];
  function f(x){x=x*ac;return (u=='g'&&x>=1000)?(x/1000).toFixed(2)+' kg':(x<10?x.toFixed(1):Math.round(x))+' '+u}
  return f(a)+(b!=a?' – '+f(b):'')}
function loadSeedImg(el){
  var q=el.getAttribute('data-sq'),ck='seed3:'+q,c=ls(ck,null);
  function put(u){if(!u)return;var im=new Image();im.onload=function(){el.innerHTML='';el.appendChild(im)};im.src=u}
  function fallback(){el.removeAttribute('data-sq');el.setAttribute('data-q',el.getAttribute('data-t')+'|'+q.replace(/ seeds$/,' plant'));loadImg(el)}
  if(c){put(c);return}
  fetch('https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch='+encodeURIComponent(q)+'&gsrlimit=8&prop=imageinfo&iiprop=url&iiurlwidth=320&format=json&origin=*')
  .then(function(r){return r.json()}).then(function(j){
    var ps=j.query?Object.keys(j.query.pages).map(function(k){return j.query.pages[k]}):[];
    ps.sort(function(a,b){return a.index-b.index});
    var u='',i,ii;for(i=0;i<ps.length;i++){ii=ps[i].imageinfo&&ps[i].imageinfo[0];if(ii&&/\.(jpe?g|png)$/i.test(ps[i].title)&&ii.thumburl){u=ii.thumburl;break}}
    if(u){sv(ck,u);put(u)}else fallback()}).catch(fallback)}
function scanSeeds(){var els=document.querySelectorAll('.ph[data-sq]');
  if(!('IntersectionObserver' in window)){els.forEach(loadSeedImg);return}
  if(!sobs)sobs=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){sobs.unobserve(x.target);loadSeedImg(x.target)}})},{rootMargin:'200px'});
  els.forEach(function(el){sobs.observe(el)})}
function vSeeds(){
  var h='<h2>🌰 બીજ સંગ્રહ ('+D.crops.length+')</h2><input id="sq" placeholder="🔎 બીજ શોધો" value="'+esc(SQ)+'" oninput="SQ=this.value;listSeeds()"><div class="chips">'+CATS.map(function(k,i){return '<button class="chip '+(SCAT==k?'on':'')+'" onclick="SCAT=CATS['+i+'];render()">'+(EM[k]||'🌍')+' '+(CATG[k]||k)+'</button>'}).join('')+'</div><div class="grid" id="sl"></div>';
  setTimeout(listSeeds,0);return h}
function listSeeds(){
  var el=$('sl');if(!el)return;var q=SQ.trim().toLowerCase();
  var l=D.crops.filter(function(c){return (SCAT=='બધા'||c.c==SCAT)&&(!q||c.n.toLowerCase().indexOf(q)>-1||c.g.toLowerCase().indexOf(q)>-1)});
  el.innerHTML=TR(l.map(function(c){return '<div class="card" onclick="openSeed(\''+esc(c.n)+'\')"><div class="ph" data-sq="'+esc(c.n+' seeds')+'" data-t="'+esc(c.w)+'">🌰</div><div class="t">'+esc(c.g)+'<small>'+esc(c.seed.rate)+'</small></div></div>'}).join('')||'<p>કોઈ બીજ મળ્યું નહીં</p>');scanSeeds()}
function openSeed(n){
  var c=D.crops.filter(function(x){return x.n==n})[0];if(!c)return;var s=c.seed,qy=seedQty(s.rate);
  $('mbody').innerHTML=TR('<div class="ph big" data-sq="'+esc(c.n+' seeds')+'" data-t="'+esc(c.w)+'">🌰</div><h2 style="margin-top:10px">'+esc(c.g)+' ('+esc(c.n)+') '+esc(s.special)+'</h2><div class="kv">🌰 <b>બીજ:</b> '+esc(s.seed_guj)+'<br>👁️ <b>દેખાવ:</b> '+esc(s.look_guj)+'<br>⚖️ <b>બીજ દર:</b> '+esc(s.rate)+(qy?'<br>🌾 <b>તમારા ખેતર માટે જથ્થો:</b> '+qy:'')+'<br>⏱️ <b>ઉગવાનો સમય:</b> '+esc(s.germ)+'<br>📅 <b>વાવેતર સમય:</b> '+esc(s.season_guj)+'</div><button class="btn" onclick="closeM();openCrop(\''+esc(c.n)+'\')">🌱 પાકની માહિતી</button><button class="btn s r" onclick="closeM()">બંધ</button>');
  $('modal').style.display='flex';scanSeeds()}

/* ---------- my crop tracker (sowing -> harvest) ---------- */
var TRK=ls('trk',[]);if(!(TRK instanceof Array))TRK=[];
function hDays(h){var m=/(\d+)(?:-(\d+))?\s*(દિવસ|મહિના|વર્ષ)/.exec(h||'');if(!m)return null;var f=m[3]=='દિવસ'?1:m[3]=='મહિના'?30:365;return [+m[1]*f,(m[2]?+m[2]:+m[1])*f]}
function isoPlus(d,n){var x=new Date(d+'T00:00:00');x.setDate(x.getDate()+n);return x.getFullYear()+'-'+('0'+(x.getMonth()+1)).slice(-2)+'-'+('0'+x.getDate()).slice(-2)}
function vTrack(){
  var opts=D.crops.slice().sort(function(a,b){return a.g.localeCompare(b.g)}).map(function(c){return '<option value="'+esc(c.n)+'">'+esc(c.g)+' ('+esc(c.n)+')</option>'}).join('');
  var td=new Date().toISOString().slice(0,10);
  var h='<h2>🌾 મારો પાક ટ્રેકર</h2><div class="tool"><label>🌱 પાક પસંદ કરો</label><select id="tc">'+opts+'</select><label>📅 વાવેતર તારીખ</label><input id="tdt" type="date" value="'+td+'"><label>🌾 વીઘા</label><input id="tb" type="number" step="any" value="'+esc(PROF.bigha||'')+'"><button class="btn" onclick="addTrk()">➕ પાક ઉમેરો</button></div>';
  h+=TRK.length?TRK.map(function(t,i){
    var c=D.crops.filter(function(x){return x.n==t.n})[0];if(!c)return '';
    var days=Math.floor((Date.now()-new Date(t.d+'T00:00:00').getTime())/864e5),hd=hDays(c.seed.harvest),pct=hd?Math.max(0,Math.min(100,days/hd[1]*100)):0,st='',rg='';
    if(hd){rg=esc(fmtD(isoPlus(t.d,hd[0])))+(hd[1]!=hd[0]?' – '+esc(fmtD(isoPlus(t.d,hd[1]))):'');st=days>=hd[0]?'🟢 લણણી લાયક છે':days>=hd[0]*0.85?'🟡 લણણી નજીક છે':'🌱 હજી વધી રહ્યો છે'}
    return '<div class="tool"><b>🌾 '+esc(c.g)+' ('+esc(c.n)+')</b> • '+esc(t.b)+' વીઘા<div class="pb"><i style="width:'+pct.toFixed(0)+'%"></i></div><small>⏱️ '+Math.max(days,0)+' દિવસ થયા'+(rg?' | 📅 લણણી અંદાજ: '+rg:'')+'</small><br><b>'+st+'</b><br><small>💧 '+esc(c.seed.care_guj)+'</small> <button class="chip" onclick="delTrk('+i+')">🗑️</button></div>'}).join(''):'<p>📭 હજી કોઈ પાક ઉમેર્યો નથી</p>';
  return h}
function addTrk(){
  var n=$('tc').value,d=$('tdt').value,b=num('tb',parseFloat(PROF.bigha)||1);if(!n||!d){toast('લખાણ અને તારીખ નાખો');return}
  TRK.unshift({n:n,d:d,b:b});sv('trk',TRK);
  var c=D.crops.filter(function(x){return x.n==n})[0],hd=c?hDays(c.seed.harvest):null;
  if(hd){RM.push({t:'🌾 '+c.g,c:n,d:isoPlus(d,hd[0]),x:0});sv('rm',RM)}
  addPts(3,'🌾');render()}
function rcn(n){var c=D.crops.filter(function(x){return x.n==n})[0];return c?c.g:n}
function delTrk(i){TRK.splice(i,1);sv('trk',TRK);render()}


/* ================= v4: guides, how-to videos (in-app), libraries, calculators ================= */
function X(k){var v=(D.t3||{})[k];return v?v[LANG=='gu'?0:LANG=='hi'?1:2]:k}
function bl(s){return '<ul class="bl">'+String(s).split(';;').map(function(x){return '<li>'+esc(x.trim())+'</li>'}).join('')+'</ul>'}
var TEMO={mkf:'🪱',mkp:'🧴',mkt:'✂️',soil:'🏜️',irr:'💧',pest:'🐛',dis:'🍄',org:'🌿',cal:'🗓️',adv:'🌤️',safe:'🦺',gloss:'📖',tip:'💡',mach:'🚜',animal:'🐄',store:'📦'};
function vMisc(){
  if(TAB.indexOf('i_')==0){var id=TAB.slice(2);
    if(id=='pest')return vLib('pest',8);if(id=='dis')return vLib('dis',8);if(id=='cal')return vCal();if(id=='adv')return vAdv();
    if(id=='gloss')return vGloss();if(id=='tip')return vTip();return vInfo(id)}
  return vHome()}
/* generic guide pages */
var INFO={soil:4,irr:3,org:4,safe:4,mach:5,animal:4,store:4};
function vInfo(id){
  var h='<h2>'+TEMO[id]+' '+X('t.'+id)+'</h2><p style="font-size:12.5px;margin:-4px 0 8px">'+X('ui.nolink')+'</p>';
  for(var i=1;i<=INFO[id];i++)h+='<div class="tool"><h3>'+X('s.'+id+'.'+i+'.h')+'</h3>'+bl(X('s.'+id+'.'+i+'.b'))+'</div>';
  if(id=='soil')h+=soilAdv();if(id=='irr')h+=irrCalc();return h}
/* soil test advisor */
function soilAdv(){
  function o(id,l){return '<label>'+X('sa.'+l)+'</label><select id="'+id+'"><option value="low">'+X('sa.low')+'</option><option value="med" selected>'+X('sa.med')+'</option><option value="high">'+X('sa.high')+'</option></select>'}
  return '<div class="tool"><h3>'+X('sa.title')+'</h3><input id="sa_ph" type="number" step="0.1" placeholder="'+X('sa.ph')+'">'+o('sa_n','n')+o('sa_p','p')+o('sa_k','k')+'<button class="btn" onclick="soilGo()">'+X('sa.go')+'</button><div id="sar"></div></div>'}
function soilGo(){
  var ph=parseFloat($('sa_ph').value),r='';
  if(!isNaN(ph))r+='<p>'+esc(X(ph<5.5?'sa.ph.acid':ph>7.8?'sa.ph.alk':'sa.ph.ok'))+'</p>';
  ['n','p','k'].forEach(function(x){r+='<p>'+esc(X('sa.'+x+'.'+$('sa_'+x).value))+'</p>'});
  $('sar').innerHTML='<div class="out">'+r+'</div>'}
/* water calculator */
var DEPTH={Trees:6,Grains:5,'Cash Crops':5,Vegetables:4,Fruits:6,Flowers:4,Herbs:3};
function irrCalc(){
  return '<div class="tool"><h3>'+X('ic.title')+'</h3><label>'+X('ic.cat')+'</label><select id="ic_c" onchange="$(\'ic_d\').value=DEPTH[this.value]">'+CATS.slice(1).map(function(k){return '<option value="'+k+'">'+(EM[k]||'')+' '+(CATG[k]||k)+'</option>'}).join('')+'</select><label>'+X('ic.method')+'</label><select id="ic_m"><option value="1">'+X('ic.flood')+'</option><option value="0.7">'+X('ic.spr')+'</option><option value="0.4">'+X('ic.drip')+'</option></select><label>'+X('ic.bigha')+'</label><input id="ic_b" type="number" step="any" value="'+esc(PROF.bigha||1)+'"><label>'+X('ic.depth')+'</label><input id="ic_d" type="number" step="any" value="'+DEPTH.Trees+'"><label>'+X('ic.pump')+'</label><input id="ic_p" type="number" value="300"><button class="btn" onclick="irrGo()">'+X('ic.go')+'</button><div id="ic_r"></div></div>'}
function irrGo(){
  var b=num('ic_b',1),d=num('ic_d',5),p=num('ic_p',300),f=parseFloat($('ic_m').value)||1,L=b*1619*d*10*f,hr=L/(p*60);
  $('ic_r').innerHTML='<div class="out">💧 '+X('ic.res')+': <b>'+fm(L)+' L</b> ('+(L/1000).toFixed(1)+' m³)<br>⏱️ '+X('ic.hours')+': <b>'+hr.toFixed(1)+'</b> '+X('ic.hr')+(f<1?'<br>✅ '+X('ic.save')+': '+Math.round((1-f)*100)+'%':'')+'</div>'}
/* pest and disease libraries */
function vLib(k,n){
  var h='<h2>'+TEMO[k]+' '+X('t.'+k)+'</h2><p style="font-size:12.5px;margin:-4px 0 8px">'+X('ui.nolink')+'</p>';
  for(var i=1;i<=n;i++){var p=k+'.'+i;h+='<details class="tool"><summary><b>'+esc(X(p+'.n'))+'</b></summary><p>⚠️ '+esc(X(p+'.d'))+'</p>'+bl(X(p+'.c'))+'</details>'}
  return h}
/* glossary, tip of the day, season calendar, weather advisor */
var GQ='';
function vGloss(){setTimeout(listGloss,0);return '<h2>📖 '+X('t.gloss')+'</h2><input placeholder="🔎 '+X('gl.search')+'" value="'+esc(GQ)+'" oninput="GQ=this.value;listGloss()"><div id="gll"></div>'}
function listGloss(){var q=GQ.toLowerCase(),h='',i,t,d;for(i=1;i<=15;i++){t=X('gl.'+i+'.t');d=X('gl.'+i+'.d');if(!q||(t+' '+d).toLowerCase().indexOf(q)>-1)h+='<div class="row"><div class="i"><b>'+esc(t)+'</b><br><small>'+esc(d)+'</small></div></div>'}var el=$('gll');if(el)el.innerHTML=h}
var TIPI=null;
function vTip(){
  if(TIPI===null){var d=new Date();TIPI=(Math.floor((d-new Date(d.getFullYear(),0,0))/864e5)%20)+1}
  return '<h2>💡 '+X('t.tip')+'</h2><div class="tool" style="font-size:17px;line-height:1.7">'+esc(X('tip.'+TIPI))+'</div><button class="btn" onclick="TIPI=TIPI%20+1;render()">'+X('tip.next')+'</button>'}
var CALM=new Date().getMonth();
function vCal(){
  var h='<h2>🗓️ '+X('t.cal')+'</h2><label>'+X('cal.pick')+'</label><select onchange="CALM=+this.value;render()">'+MN.map(function(m,i){return '<option value="'+i+'"'+(i==CALM?' selected':'')+'>'+m+'</option>'}).join('')+'</select>';
  h+='<div class="box home"><b>'+X('cal.work')+':</b> '+esc(X('cal.m.'+CALM))+'</div><h3>'+X('cal.sow')+'</h3>';
  CATS.slice(1).forEach(function(k){var l=D.crops.filter(function(c){return c.c==k&&inSeason(c.season,CALM)});if(l.length)h+='<div class="tool"><b>'+(EM[k]||'')+' '+(CATG[k]||k)+' ('+l.length+')</b><br><small>'+l.map(function(c){return esc(c.g)}).join(' • ')+'</small></div>'});
  return h}
function vAdv(){setTimeout(drawAdv,0);return '<h2>🌤️ '+X('t.adv')+'</h2><div id="advb"><div class="tool">⏳</div></div>'}
function drawAdv(){
  loadWx(false,function(w,e){var b=$('advb');if(!b)return;
    if(!w){b.innerHTML='<div class="tool">'+X('adv.nodata')+'</div>';return}
    var d=w.daily,td=String(w.current.time||'').slice(0,10),ti=d.time.indexOf(td);if(ti<0)ti=0;
    var h='<h3>'+X('adv.title')+'</h3>',rain3=0,hot=false,cold=false,i,rn,wd,mx,mn,ok;
    for(i=ti;i<ti+3&&i<d.time.length;i++){
      rn=d.precipitation_sum[i]||0;wd=d.wind_speed_10m_max?d.wind_speed_10m_max[i]:0;mx=d.temperature_2m_max[i];mn=d.temperature_2m_min[i];
      rain3+=rn;if(mx>=36)hot=true;if(mn<=6)cold=true;ok=rn<1&&wd<15&&mx<36;
      h+='<div class="wr"><div class="wd"><b>'+(i==ti?TR('આજ'):esc(fmtD(d.time[i])))+'</b></div><div class="we">'+wcode(d.weather_code[i])[0]+'</div><div style="flex:1;font-size:12.5px">'+(ok?X('adv.spray.ok'):X('adv.spray.no'))+'<br><small>'+X('adv.rain')+' '+rn.toFixed(1)+' mm • '+X('adv.wind')+' '+Math.round(wd)+' km/h</small></div></div>'}
    h+='<div class="box home">'+(rain3>=10?X('adv.irr.skip'):hot?X('adv.irr.hot'):X('adv.irr.norm'))+'</div>';
    if(cold)h+='<div class="box home">'+X('adv.frost')+'</div>';
    b.innerHTML=h})}
/* crop-wise full farming guide */
var FGC=ls('fgc','Wheat'),FGK={Trees:'tree',Grains:'grain','Cash Crops':'cash',Vegetables:'veg',Fruits:'fruit',Flowers:'flower',Herbs:'herb'};
function vFG(){
  var opts=D.crops.slice().sort(function(a,b){return a.g.localeCompare(b.g)}).map(function(c){return '<option value="'+esc(c.n)+'"'+(c.n==FGC?' selected':'')+'>'+esc(c.g)+' ('+esc(c.n)+')</option>'}).join('');
  var c=D.crops.filter(function(x){return x.n==FGC})[0]||D.crops[0],k=FGK[c.c]||'tree',s=c.seed,f=(D.fert||{})[c.n];
  var R={seed:s.seed_guj,rate:s.rate,germ:s.germ,season:s.season_guj,method:s.method_guj,care:s.care_guj,harvest:s.harvest,npk:f?('NPK '+f.join('-')+' '+X('fg.acre')):X('fg.npk.'+k)};
  function T(key){var t=X(key),q;for(q in R)t=t.split('{'+q+'}').join(R[q]);return t}
  var h='<h2>📚 '+X('t.fg')+'</h2><p style="font-size:12.5px;margin:-4px 0 8px">'+X('ui.nolink')+'</p><label>🌱 '+X('fg.pick')+'</label><select onchange="FGC=this.value;sv(\'fgc\',FGC);render()">'+opts+'</select><div class="ph big" data-q="'+esc(c.w+'|'+c.n+' plant')+'"></div><h2 style="margin-top:8px">'+esc(c.g)+' ('+esc(c.n)+') '+esc(s.special)+'</h2>';
  [['fg.h1','fg.1.'+k],['fg.h2','fg.2'],['fg.h3','fg.3'],['fg.h4','fg.4.'+k],['fg.h5','fg.5'],['fg.h6','fg.6']].forEach(function(x){h+='<div class="tool"><h3>'+X(x[0])+'</h3>'+bl(T(x[1]))+'</div>'});
  return h}
/* in-app step-by-step "video" player */
var HOW={mkf:['jeevamrut','vermi','compost','panch','ghan'],mkp:['neemark','dash','agni','garlic'],mkt:['nursery','graft','mulch','drip','seedtreat','sample']},PL=null,PLT=null;
function vHow(k){
  return '<h2>'+TEMO[k]+' '+X('t.'+k)+'</h2><p style="font-size:12.5px;margin:-4px 0 8px">'+X('ui.nolink')+'</p>'+HOW[k].map(function(g){return '<button class="btn" style="text-align:left" onclick="openHow(\''+g+'\')">'+esc(X('h.'+g+'.t'))+' • 5 '+X('ui.step')+'</button>'}).join('')}
function openHow(g){clearInterval(PLT);PL={g:g,i:1,auto:false};drawHow();$('modal').style.display='flex'}
function drawHow(){
  var s=X('h.'+PL.g+'.'+PL.i),m=/^(\S+)\s+([\s\S]*)$/.exec(s),em=m?m[1]:'🌱',tx=m?m[2]:s;
  $('mbody').innerHTML='<h2>'+esc(X('h.'+PL.g+'.t'))+'</h2><div class="pl"><div class="pe">'+em+'</div><div class="pt">'+esc(tx)+'</div><div class="pb"><i style="width:'+(PL.i/5*100)+'%"></i></div><small>'+X('ui.step')+' '+PL.i+' / 5</small></div><div class="plc"><button class="btn s" onclick="plGo(-1)">'+X('ui.prev')+'</button><button class="btn s" onclick="plAuto()">'+(PL.auto?X('ui.pause'):X('ui.play'))+'</button><button class="btn s" onclick="plGo(1)">'+X('ui.next')+'</button></div><button class="btn s r" onclick="closeHow()">'+TR('બંધ')+'</button>'}
function plGo(d){PL.i=Math.min(5,Math.max(1,PL.i+d));if(PL.i==5&&PL.auto){PL.auto=false;clearInterval(PLT)}drawHow()}
function plAuto(){
  PL.auto=!PL.auto;clearInterval(PLT);
  if(PL.auto){if(PL.i==5)PL.i=1;PLT=setInterval(function(){if($('modal').style.display=='none'){clearInterval(PLT);return}if(PL.i>=5){PL.auto=false;clearInterval(PLT)}else PL.i++;drawHow()},4500)}
  drawHow()}
function closeHow(){clearInterval(PLT);closeM()}

/* copy to clipboard (no outside apps / links) */
function cpText(t){
  function fb(){var a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity=0;document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}document.body.removeChild(a);toast(X('ui.copied'))}
  try{navigator.clipboard.writeText(t).then(function(){toast(X('ui.copied'))},fb)}catch(e){fb()}}
/* ---------- Start ---------- */
(function(){var sb=document.querySelector('#splash .sbg');if(sb)loadImg(sb)})();
fetch('/api/data').then(function(r){return r.json()}).then(function(j){
  DR=j;applyTheme();setLang(LANG);drawSetup();
  setTimeout(function(){$('splash').style.opacity=0;$('setup').style.display='flex';setTimeout(function(){$('splash').style.display='none'},500)},1800)
}).catch(function(e){document.body.innerHTML='<h2 style="color:#fff;padding:20px">ડેટા લોડ ન થયો: '+e+'</h2>'});
</script></body></html>
"""

if __name__ == "__main__":
    print("\n🌿 Smart Health & Crop Guard ચાલુ છે!")
    print("👉 Chrome માં ખોલો: http://127.0.0.1:5000\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
