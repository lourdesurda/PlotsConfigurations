# cuts
cuts = {}
# this should be checked in postprocessing, just to be sure
supercut = '\
    Alt$(Lepton_pt[1],0)<=10 \
&&  abs(Lepton_eta[0])<2.5 \
'
# LepWPCut already implemented in Steps.py

##=== Define categories ===###
LepCats={}
LepCats['incl_']='( (abs(Lepton_pdgId[0])==11) && Lepton_pt[0]>38 \
                 || (abs(Lepton_pdgId[0])==13) && Lepton_pt[0]>30 )'
LepCats['ElCh_']='( (abs(Lepton_pdgId[0])==11) && Lepton_pt[0]>38 )'
LepCats['MuCh_']='( (abs(Lepton_pdgId[0])==13) && Lepton_pt[0]>30 )'

WvsQCD = 'Alt$(FatJet_deepTag_WvsQCD[CleanFatJet_jetIdx[idxCleanFatJetW]], -1)'
MD_WvsQCD = 'Alt$(FatJet_deepTagMD_WvsQCD[CleanFatJet_jetIdx[idxCleanFatJetW]], -1)'

# mistag rate in permille
DeepTagCats= {
    '25_': '({0} > 0.772)'.format(WvsQCD),
    '10_': '({0} > 0.925)'.format(WvsQCD),
    '05_': '({0} > 0.964)'.format(WvsQCD),

    '25MD_': '({0} > 0.506)'.format(MD_WvsQCD),
    '10MD_': '({0} > 0.739)'.format(MD_WvsQCD),
    '05MD_': '({0} > 0.838)'.format(MD_WvsQCD),
}

BoostProcCats={
    '': '1',
    'VBF_': 'DNN_isVBF_OTF[0] > 0.7',
    'GGF_': 'DNN_isVBF_OTF[0] <= 0.7',
}

BoostCats={
'AK8SR_': '1 \
            && boostedNoTau21[0] \
            && boostedSignalWMassNoTau21[0] \
            && bVeto[0]',
'AK8SB_': '1 \
            && boosted[0] \
            && !boostedSignalWMassNoTau21[0] \
            && boostedSidebandWMassNoTau21[0] \
            && bVeto[0]',
'AK8TopCR_': '1 \
            && boostedNoTau21[0] \
            && boostedSignalWMassNoTau21[0] \
            && !bVeto[0]',
}


ResolveProcCats={}
ResolveProcCats['']='1'
ResolveProcCats['VBF_']='DNN_isVBF_OTF[0] > 0.75'
ResolveProcCats['GGF_']='DNN_isVBF_OTF[0] <= 0.75'

ResolveCats={}
# ResolveCats['Resolved']='resolved[0]'
ResolveCats['ResolvedSR_']='resolved[0] && resolvedSignalWMass[0] && bVeto[0]'
ResolveCats['ResolvedSB_']='resolved[0] \
                           && !resolvedSignalWMass[0] \
                           && resolvedSidebandWMass[0] \
                           && bVeto[0]'
ResolveCats['ResolvedTopCR_']='resolved[0] && resolvedSignalWMass[0] && !bVeto[0]'


##=== Define cuts ===###
for Lep in LepCats:
    for BCat in BoostCats:
        for BProcCat in BoostProcCats:
            for DTCat in DeepTagCats:
                cuts[Lep+DTCat+BProcCat+BCat]=  BoostCats[BCat]\
                                +'&&'+BoostProcCats[BProcCat]\
                                +'&&'+LepCats[Lep]\
                                +'&&'+DeepTagCats[DTCat]


    for RCat in ResolveCats:
        for RProcCat in ResolveProcCats:
            cuts[Lep+RProcCat+RCat]=  ResolveCats[RCat]\
                                +'&&'+ResolveProcCats[RProcCat]\
                                +'&&'+LepCats[Lep]




# High Mass category
dPhiWWCut  ='&& abs(dPhi_WW_boosted[0]) > 2.2'
sumPtCut   ='&& Lepton_pt[0] + PuppiMET_pt + Alt$(HM_CleanFatJetPassMBoosted_pt[0], -9999) > 850'

HMProcCats={}
HMProcCats['55']='tau21DDT<0.55'+dPhiWWCut+sumPtCut


HMCats={}
HMCats['HMSR_']='boostedNoTau21[0] \
                && boostedSignalWMassNoTau21[0] \
                && bVeto[0]'
HMCats['HMSB_']='boostedNoTau21[0] \
               && !boostedSignalWMassNoTau21[0] \
               && boostedSidebandWMassNoTau21[0] \
               && bVeto[0]'
HMCats['HMTopCR_']='boostedNoTau21[0] \
               && boostedSignalWMassNoTau21[0] \
               && !bVeto[0]'




##=== Define cuts ===###
for Lep in LepCats:
    for HCat in HMCats:
        for HProcCat in HMProcCats:
            cuts[Lep+HProcCat+HCat]=  HMCats[HCat]\
                                +'&&'+HMProcCats[HProcCat]\
                                +'&&'+LepCats[Lep]
