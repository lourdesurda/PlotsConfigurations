# cuts
#cuts = {}
  
#supercut = 'mll>12  \
#            && std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>15 \
#            && std_vector_lepton_pt[2]<10 \
#            && metPfType1 > 20 \
#            && (njet>=1) \
#            '

supercut = 'mll>12  \
            && std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>15 \
            && std_vector_lepton_pt[2]<10 \
            && metPfType1 > 20 \
            && abs(std_vector_lepton_eta[0] - std_vector_lepton_eta[1])<2.0 \
            '

cuts['hww2l2v_13TeV_of2j_WH_SS_ll_1j'] = '((std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 13*13) || (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 11*11)) \
                                       && '+bVeto+' \
                                       && abs(mll-91.2)>15 \
                                       && std_vector_jet_pt[0]>30 \
                                       && std_vector_jet_pt[1]>20 \
                                       && std_vector_jet_pt[1]<30 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_ll_2j'] = '((std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 13*13) || (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 11*11)) \
                                       && '+bVeto+' \
                                       && abs(mll-91.2)>15 \
                                       && std_vector_jet_pt[0]>30 \
                                       && std_vector_jet_pt[1]>30 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = '(std_vector_lepton_flavour[0]*std_vector_lepton_flavour[1] == 11*13) \
                                       && '+bVeto+' \
                                       && std_vector_jet_pt[0]>30 \
                                       && std_vector_jet_pt[1]>20 \
                                       && std_vector_jet_pt[1]<30 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = '(std_vector_lepton_flavour[0]*std_vector_lepton_flavour[1] == 11*13) \
                                       && '+bVeto+' \
                                       && std_vector_jet_pt[0]>30 \
                                       && std_vector_jet_pt[1]>30 \
                                       '
#cuts['hww2l2v_13TeV_of2j_WH_SS_ue_1j'] = '((std_vector_lepton_flavour[0] == 13 && std_vector_lepton_flavour[1] == 11) || (std_vector_lepton_flavour[0] == -13 && std_vector_lepton_flavour[1] == -11)) \
#                                       && '+bVeto+' \
#                                       && std_vector_lepton_pt[1]>20 \
#                                       && abs(std_vector_lepton_eta[0] - std_vector_lepton_eta[1])<2.0 \
#                                       && std_vector_jet_pt[0]>30 \
#                                       && njet==1 \
#                                       '
#
#cuts['hww2l2v_13TeV_of2j_WH_SS_ue_2j'] = '((std_vector_lepton_flavour[0] == 13 && std_vector_lepton_flavour[1] == 11) || (std_vector_lepton_flavour[0] == -13 && std_vector_lepton_flavour[1] == -11)) \
#                                       && '+bVeto+' \
#                                       && std_vector_lepton_pt[1]>20 \
#                                       && abs(std_vector_lepton_eta[0] - std_vector_lepton_eta[1])<2.0 \
#                                       && std_vector_jet_pt[0]>30 \
#                                       && njet>1 \
#                                       && mjj<100 \
#                                       '
#
# control regions
#


#cuts['hww2l2v_13TeV_top_of2j_vbf']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
#                && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
#                && mll>50 \
#                && ( std_vector_jet_pt[0] >= 30 ) \
#                && ( std_vector_jet_pt[1] >= 30 ) \
#                && (njet==2) \
#                && (detajj>3.5 && mjj>400) \
#                && ( std_vector_jet_cmvav2[0]>-0.5884 || std_vector_jet_cmvav2[1]>-0.5884 ) \
#                '



#cuts['hww2l2v_13TeV_dytt_of2j_vbf']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)    \
#                && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
#                && ( mth<60) \
#                && mll>40 && mll<80 \
#                && ( std_vector_jet_pt[0] >= 30 ) \
#                && ( std_vector_jet_pt[1] >= 30 ) \
#                && (njet==2) \
#                && (detajj>3.5 && mjj>400) \
#                && '+bVeto+' \
#                '

# 11 = e
# 13 = mu
# 15 = tau
