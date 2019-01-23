import os
import copy
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

# samples

#samples = {}
try:
  len(samples)
except NameError:
  samples = {}

################################################
################# SKIMS ########################
################################################

mcProduction = 'Apr2017_summer16'

dataReco = 'Apr2017_Run2016{era}_RemAOD'

mcSteps = 'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__wwSel'

fakeSteps = 'lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__dorochester__multiFakeW__formulasFAKE__hadd__wwSel'

dataSteps = 'lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd__l2tightOR__dorochester__formulasDATA__wwSel'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE :
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17'
elif  'gridui' in SITE: #PISA
  treeBaseDir = '/gpfs/ddn/srm/cms/store/user/lviliani/Full2016_Apr17'
elif 'sdfarm' in SITE : # KISTI T3
  treeBaseDir = '/xrootd/store/group/hww/Full2016_Apr17'

mcDirectory = os.path.join(treeBaseDir, mcProduction, mcSteps)
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [ 
  ['B','Run2016B-03Feb2017_ver2-v2'], 
  ['C','Run2016C-03Feb2017-v1'], 
  ['D','Run2016D-03Feb2017-v1'], 
  ['E','Run2016E-03Feb2017-v1'],
  ['F','Run2016F-03Feb2017-v1'], 
  ['G','Run2016G-03Feb2017-v1'], 
  ['H','Run2016H-03Feb2017_ver2-v1'], 
  ['H','Run2016H-03Feb2017_ver3-v1'],
] 

DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
  'MuonEG'         : ' trig_EleMu',
  'DoubleMuon'     : '!trig_EleMu &&  trig_DbleMu',
  'SingleMuon'     : '!trig_EleMu && !trig_DbleMu &&  trig_SnglMu',
  'DoubleEG'       : '!trig_EleMu && !trig_DbleMu && !trig_SnglMu &&  trig_DbleEle',
  'SingleElectron' : '!trig_EleMu && !trig_DbleMu && !trig_SnglMu && !trig_DbleEle &&  trig_SnglEle',
}

#########################################
############ MC COMMON ##################
#########################################

mcCommonWeight = 'XSWeight*sfWeight*GenLepMatch*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######

useDYHT = False       # be carefull DY HT is LO 
useDYtt = True     
mixDYttandHT = False  # be carefull DY HT is LO (HT better stat for HT>450 GEV)

### These weights were evaluated on ICHEP16 MC -> Update ?
ptllDYW_NLO = '(0.876979+gen_ptll*(4.11598e-03)-(2.35520e-05)*gen_ptll*gen_ptll)*(1.10211*(0.958512-0.131835*TMath::Erf((gen_ptll-14.1972)/10.1525)))*(gen_ptll<140)+0.891188*(gen_ptll>=140)'
ptllDYW_LO  = '(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683*(0.95-0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)'

samples['DY'] = {
  'weight': mcCommonWeight
}

if useDYtt :
  # Use e-mu exclusive trees
  samples['DY']['name'] = getSampleFiles(mcDirectory,'DYJetsToLL_M-10to50') \
                          + getSampleFiles(mcDirectory,'DYJetsToTT_MuEle_M-50') \
                          + getSampleFiles(mcDirectory,'DYJetsToTT_MuEle_M-50_ext1')

  # pt_ll weight
  addSampleWeight(samples,'DY','DYJetsToLL_M-10to50',ptllDYW_NLO)
  addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
  addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50_ext1',ptllDYW_NLO)
  # set baseW across both samples
  addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50', getBaseW(mcDirectory,['DYJetsToTT_MuEle_M-50','DYJetsToTT_MuEle_M-50_ext1'])+'/baseW')
  addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50_ext1', getBaseW(mcDirectory,['DYJetsToTT_MuEle_M-50','DYJetsToTT_MuEle_M-50_ext1'])+'/baseW')

  samples['DY']['FilesPerJob'] = 1

else:
  samples['DY']['name'] = getSampleFiles(mcDirectory,'DYJetsToLL_M-10to50') \
                          + getSampleFiles(mcDirectory,'DYJetsToLL_M-50')
  if useDYHT:
    # ... Add DY HT Samples
    samples['DY']['name'] += getSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-70to100') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-100to200')\
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-200to400') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-400to600') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-5to50_HT-600toInf') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-70to100') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200_ext1') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400_ext1') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-400to600') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-600to800') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-800to1200') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-1200to2500') \
                             + getSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-2500toInf')
  
    samples['DY']['FilesPerJob'] = 8

  addSampleWeight(samples,'DY','DYJetsToLL_M-10to50',ptllDYW_NLO)
  addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)

  if useDYHT :
    # Remove high HT from inclusive sample
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50', 'genHT<70.0')  
    addSampleWeight(samples,'DY','DYJetsToLL_M-50', 'genHT<70.0')  
    # pt_ll weight
    addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-70to100',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-100to200',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-200to400',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-400to600',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-600toInf',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200_ext1',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400_ext1',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500',ptllDYW_LO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',ptllDYW_LO)
    # Fix some x-sections
    addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-70to100', getBaseW(mcDirectory,['DYJetsToLL_M-5to50_HT-70to100'])+'/baseW')   # x-section update
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100', getBaseW(mcDirectory,['DYJetsToLL_M-50_HT-70to100'])+'/baseW')      # x-section update
    # set baseW across both samples
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200', getBaseW(mcDirectory,['DYJetsToLL_M-50_HT-100to200','DYJetsToLL_M-50_HT-100to200_ext1'])+'/baseW')
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200_ext1', getBaseW(mcDirectory,['DYJetsToLL_M-50_HT-100to200','DYJetsToLL_M-50_HT-100to200_ext1'])+'/baseW')
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400', getBaseW(mcDirectory,['DYJetsToLL_M-50_HT-200to400','DYJetsToLL_M-50_HT-200to400_ext1'])+'/baseW')
    addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400_ext1', getBaseW(mcDirectory,['DYJetsToLL_M-50_HT-200to400','DYJetsToLL_M-50_HT-200to400_ext1'])+'/baseW')

samples['DY_0j'] = copy.deepcopy(samples['DY'])
samples['DY_0j']['weight'] += '*(zeroJet)'

samples['DY_1j'] = copy.deepcopy(samples['DY'])
samples['DY_1j']['weight'] += '*(oneJet)'

samples['DY_ge2j'] = copy.deepcopy(samples['DY'])
samples['DY_ge2j']['weight'] += '*(manyJet)'

###### Top #######
# We should use in principle: ST_tW_antitop_noHad + ST_tW_antitop_noHad_ext1 + ST_tW_top_noHad + ST_tW_top_noHad_ext1   
# but first need to compute x-section and correct baseW
files = getSampleFiles(mcDirectory,'TTTo2L2Nu') \
        + getSampleFiles(mcDirectory,'ST_tW_antitop') \
        + getSampleFiles(mcDirectory,'ST_tW_top') \
        + getSampleFiles(mcDirectory,'ST_t-channel_antitop') \
        + getSampleFiles(mcDirectory,'ST_t-channel_top') \
        + getSampleFiles(mcDirectory,'ST_s-channel')

samples['top'] = {
  'name': files,
  'weight': mcCommonWeight,
  'FilesPerJob': 1,
  'EventsPerJob': 50000
}
                  
addSampleWeight(samples,'top','TTTo2L2Nu','toprwgt')

samples['top_0j'] = copy.deepcopy(samples['top'])
samples['top_0j']['weight'] += '*(zeroJet)'

samples['top_1j'] = copy.deepcopy(samples['top'])
samples['top_1j']['weight'] += '*(oneJet)'

samples['top_ge2j'] = copy.deepcopy(samples['top'])
samples['top_ge2j']['weight'] += '*(manyJet)'

###### WW ########
             
samples['WW'] = {
  'name': getSampleFiles(mcDirectory,'WWTo2L2Nu'),
  'weight': mcCommonWeight + '*nllW'
}

samples['ggWW'] = {
  'name': getSampleFiles(mcDirectory,'GluGluWWTo2L2Nu_MCFM'),      
  'weight': mcCommonWeight
}

## during tree production: 1.4 k-factor has been applied to both samples
## ggWW sample: k = 1.4 +/- 15%
## ggWW interference: k = 1.87 +/- 25%

######## Vg ########

samples['Vg'] = {
  'name': getSampleFiles(mcDirectory,'Wg_MADGRAPHMLM') + getSampleFiles(mcDirectory,'Zg'),
  'weight': 'XSWeight*sfWeight*METFilter_MC* !(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22)'
}

######## VgS ########

samples['WZgS_L'] = {
  'name': getSampleFiles(mcDirectory,'WZTo3LNu_mllmin01_ext1'),
  'weight': mcCommonWeight + '* (Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4)*0.94'
}

samples['WZgS_H'] = {
  'name': getSampleFiles(mcDirectory,'WZTo3LNu_mllmin01_ext1'),
  'weight': mcCommonWeight + '* (Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4)*1.14'
} 

######### VZ #########

files = getSampleFiles(mcDirectory,'ZZTo2L2Nu') \
        + getSampleFiles(mcDirectory,'WZTo2L2Q') \
        + getSampleFiles(mcDirectory,'ZZTo2L2Q')
# Should we include this as well here:
# + getSampleFiles(mcDirectory,'tZq_ll')

samples['VZ'] = {
  'name': files,
  'weight': mcCommonWeight + '*1.11',
  'FilesPerJob': 4
}

### 1.11 normalisation was measured in 3-lepton

########## VVV #########

files = getSampleFiles(mcDirectory,'ZZZ') \
        + getSampleFiles(mcDirectory,'WZZ') \
        + getSampleFiles(mcDirectory,'WWZ') \
        + getSampleFiles(mcDirectory,'WWW')
#  WWG: Might be added to WW by PYTHIA in tuning step, super small x-section anyway -> skipped for now 
#  + getSampleFiles(mcDirectory,'WWG')

samples['VVV'] = {
  'name': files,
  'weight': mcCommonWeight
}

###########################################
#############   SIGNALS  ##################
###########################################

#### Cuts for signal splitting
# ==2 OSOF leptons
# pt1 > 25
# pt2 > 10(13) el(mu)
# mll = sqrt(2*pt1*pt2*(cosh(eta1-eta2)-cos(phi1-phi2))) > 12
# MET > 20
# ptll = sqrt(pt1^2+pt2^2+2*pt1*pt2*cos(phi1-phi2)) > 30 
# mth = sqrt(2*met*(sqrt(pt1^2+pt2^2+2*pt1*pt2*cos(phi1-phi2))-cos(metphi)*(pt1*cos(phi1)+pt2*cos(phi2))-sin(metphi)*(pt1*sin(phi1)+pt2*sin(phi2)))) >= 60 
# mtw2 = sqrt(2*pt2*met*(1-cos(phi2-metphi))) > 30

pthBinning1 = [0., 20., 45., 80., 120., 200., 6500.]
pthBinning2 = [0., 30., 60., 100., 200., 350., 6500.]
yhBinning = [0., 0.15, 0.3, 0.6, 0.9, 1.2, 2.5, 10.]
njetBinning = [0, 1, 2, 3, 4]

signals = []

#### ggH -> WW

samples['ggH_hww']  = {
  'name': getSampleFiles(mcDirectory,'GluGluHToWWTo2L2NuPowheg_M125'),  
  'weight': mcCommonWeight+'*weight2MINLO'
}

signals.append('ggH_hww')

samples['ggH_hww_minloHJ']  = {
  'name': getSampleFiles(mcDirectory,'GluGluHToWWTo2L2Nu_M125_minloHJ_NNLOPS'),  
  'weight': mcCommonWeight,  
}

signals.append('ggH_hww_minloHJ')

##### VBF H -> WW
#
#samples['qqH_hww']  = { 
#  'name': getSampleFiles(mcDirectory,'VBFHToWWTo2L2Nu_M125'),
#  'weight': mcCommonWeight
#}
#
#signals.append('qqH_hww')
#
#### ZH ; H->WW
#
#samples['ZH_hww']   = { 
#  'name': getSampleFiles(mcDirectory,'HZJ_HToWW_M125'),
#  'weight': mcCommonWeight
#}
#
#signals.append('ZH_hww')
#
#samples['ggZH_hww'] = { 
#  'name': getSampleFiles(mcDirectory,'ggZH_HToWW_M125'),
#  'weight': mcCommonWeight
#}
#
#signals.append('ggZH_hww')
#
##### WH ; H->WW
#
#samples['WH_hww']   = { 
#  'name': getSampleFiles(mcDirectory,'HWminusJ_HToWW_M125') + getSampleFiles(mcDirectory,'HWplusJ_HToWW_M125'), 
#  'weight': mcCommonWeight
#}
#
#signals.append('WH_hww')
#
##### bbH ; H->WW 
#
#samples['bbH_hww']  = {
#  'name': getSampleFiles(mcDirectory,'bbHToWWTo2L2Nu_M125_yb2') + getSampleFiles(mcDirectory,'bbHToWWTo2L2Nu_M125_ybyt'),
#  'weight': mcCommonWeight,
#}
#
#signals.append('bbH_hww')
#
##### ttH ; H->WW 
#
#samples['ttH_hww']  = {
#  'name': getSampleFiles(mcDirectory,'ttHToNonbb_M125'),
#  'weight': mcCommonWeight,
#  'suppressNegativeNuisances': ['all']
#}
#
#signals.append('ttH_hww')

files = getSampleFiles(mcDirectory,'VBFHToWWTo2L2Nu_M125') + \
        getSampleFiles(mcDirectory,'HZJ_HToWW_M125') + \
        getSampleFiles(mcDirectory,'ttHToNonbb_M125') + \
        getSampleFiles(mcDirectory,'ggZH_HToWW_M125') + \
        getSampleFiles(mcDirectory,'HWminusJ_HToWW_M125') + getSampleFiles(mcDirectory,'HWplusJ_HToWW_M125') + \
        getSampleFiles(mcDirectory,'bbHToWWTo2L2Nu_M125_yb2') + getSampleFiles(mcDirectory,'bbHToWWTo2L2Nu_M125_ybyt') + \
        getSampleFiles(mcDirectory,'ttHToNonbb_M125')

samples['XH_hww']  = {
  'name': files,
  'weight': mcCommonWeight,
  'suppressNegativeNuisances': ['all'],
  'FilesPerJob': 1
}

signals.append('XH_hww')

for signal in signals:
    for ipt in range(len(pthBinning1) - 1):
      low, high = pthBinning1[ipt:ipt+2]

      samples[signal + '_pth_%.0f_%.0f_incl' % (low, high)] = copy.deepcopy(samples[signal])
      samples[signal + '_pth_%.0f_%.0f_incl' % (low, high)]['weight'] += '*(genPth > %f && genPth < %f)' % (low, high)

      samples[signal + '_pth_%.0f_%.0f_fid' % (low, high)] = copy.deepcopy(samples[signal])
      samples[signal + '_pth_%.0f_%.0f_fid' % (low, high)]['weight'] += '*(fiducial && genPth > %f && genPth < %f)' % (low, high)

      samples[signal + '_pth_%.0f_%.0f_nonfid' % (low, high)] = copy.deepcopy(samples[signal])
      samples[signal + '_pth_%.0f_%.0f_nonfid' % (low, high)]['weight'] += '*(!fiducial && genPth > %f && genPth < %f)' % (low, high)

    for ipt in range(len(pthBinning2) - 1):
      low, high = pthBinning2[ipt:ipt+2]

      samples[signal + '_pth_%.0f_%.0f_incl' % (low, high)] = copy.deepcopy(samples[signal])
      samples[signal + '_pth_%.0f_%.0f_incl' % (low, high)]['weight'] += '*(genPth > %f && genPth < %f)' % (low, high)

      samples[signal + '_pth_%.0f_%.0f_fid' % (low, high)] = copy.deepcopy(samples[signal])
      samples[signal + '_pth_%.0f_%.0f_fid' % (low, high)]['weight'] += '*(fiducial && genPth > %f && genPth < %f)' % (low, high)

      samples[signal + '_pth_%.0f_%.0f_nonfid' % (low, high)] = copy.deepcopy(samples[signal])
      samples[signal + '_pth_%.0f_%.0f_nonfid' % (low, high)]['weight'] += '*(!fiducial && genPth > %f && genPth < %f)' % (low, high)
    
    #samples[signal + '_yhbins'] = copy.deepcopy(samples[signal])
    #samples[signal + '_yhbins']['bins'] = {}
    #
    #for iy in range(len(yhBinning) - 1):
    #  low, high = yhBinning[iy:iy+2]
    #  samples[signal + '_yhbins']['bins'][('fid_yh_%.2f_%.2f' % (low, high)).replace('.', 'p')] = 'fiducial && absGenYH > %f && absGenYH < %f' % (low, high)
    #  samples[signal + '_yhbins']['bins'][('nonfid_yh_%.2f_%.2f' % (low, high)).replace('.', 'p')] = '!fiducial && absGenYH > %f && absGenYH < %f' % (low, high)
    
    #for n in njetBinning:
    #  samples[signal + '_nj_%d_fid' % n] = copy.deepcopy(samples[signal])
    #  if n == njetBinning[-1]:
    #    samples[signal + '_nj_%d_fid' % n]['weight'] += '*(fiducial && nGenJet >= %d)' % n
    #  else:
    #    samples[signal + '_nj_%d_fid' % n]['weight'] += '*(fiducial && nGenJet == %d)' % n
    #
    #  samples[signal + '_nj_%d_nonfid' % n] = copy.deepcopy(samples[signal])
    #  if n == njetBinning[-1]:
    #    samples[signal + '_nj_%d_nonfid' % n]['weight'] += '*(!fiducial && nGenJet >= %d)' % n
    #  else:
    #    samples[signal + '_nj_%d_nonfid' % n]['weight'] += '*(!fiducial && nGenJet == %d)' % n

#### H -> TauTau

splitHtt=False
if splitHtt:
  samples['ggH_htt'] = {
    'name': getSampleFiles(mcDirectory,'GluGluHToTauTau_M125'),
    'weight': mcCommonWeight,
    'suppressNegative': ['all'],
    'suppressNegativeNuisances': ['all']
  }

  samples['qqH_htt'] = {
    'name': getSampleFiles(mcDirectory,'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'suppressNegative': ['all'],
    'suppressNegativeNuisances': ['all'],
  }

  samples['ZH_htt'] = {
    'name': getSampleFiles(mcDirectory,'HZJ_HToTauTau_M125'),
    'weight': mcCommonWeight,
    'suppressNegative': ['all'],
    'suppressNegativeNuisances': ['all']
  }

  samples['WH_htt']  = {
    'name': getSampleFiles(mcDirectory,'HWplusJ_HToTauTau_M125') + getSampleFiles(mcDirectory,'HWminusJ_HToTauTau_M125'),
    'weight': mcCommonWeight,
    'suppressNegative': ['all'],
    'suppressNegativeNuisances': ['all']
  }

else:
  files = getSampleFiles(mcDirectory,'GluGluHToTauTau_M125') \
          + getSampleFiles(mcDirectory,'VBFHToTauTau_M125') \
          + getSampleFiles(mcDirectory,'HZJ_HToTauTau_M125') \
          + getSampleFiles(mcDirectory,'HWplusJ_HToTauTau_M125') \
          + getSampleFiles(mcDirectory,'HWminusJ_HToTauTau_M125')

  samples['H_htt']    = { 
    'name': files,
    'weight': mcCommonWeight,  
    'suppressNegative': ['all'],
    'suppressNegativeNuisances': ['all'],
  }


###########################################
################## FAKE ###################
###########################################

samples['Fake']  = {
  'name': [],
  'weight': 'fakeWeight*veto_EMTFBug*METFilter_DATA',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 6
}

for era, sd in DataRun:
  for pd in DataSets:
    files = getSampleFiles(fakeDirectory.format(era = era), pd + '_' + sd, True)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
################## DATA ###################
###########################################

samples['DATA']  = { 
  'name': [],     
  'weight': 'veto_EMTFBug*METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all']
}

for era, sd in DataRun:
  for pd in DataSets:
    files = getSampleFiles(dataDirectory.format(era = era), pd + '_' + sd, True)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
