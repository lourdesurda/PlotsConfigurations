#!/usr/bin/env python

import re
import os.path
from optparse import OptionParser
from math import sqrt,fabs
from collections import OrderedDict
import CMS_lumi, tdrstyle
import numpy as np

import ROOT
ROOT.gSystem.Load("libHiggsAnalysisCombinedLimit")

from HiggsAnalysis.CombinedLimit.DatacardParser import *


## Style features
tdrstyle.setTDRStyle()

parser = OptionParser()
#parser.add_option("-s", "--stat",   dest="stat",          default=False, action="store_true")  # ignore systematic uncertainties to consider statistical uncertainties only

(options, args) = parser.parse_args()
options.bin = True # fake that is a binary output, so that we parse shape lines
options.noJMax = False
options.nuisancesToExclude = ''
options.verbose = False
options.stat = False

DC = parseCard(file(args[0]), options)

signals_orig     = DC.list_of_signals()
signals = []

# choose here what signals you want to show
for s in signals_orig:
  if 'ggH' in s: signals.append(s)

signals = sorted(signals, key=lambda s: s.lower())

overallSignalRate = OrderedDict()
overallTotalSignal = OrderedDict()
channels_orig = DC.exp
channels = OrderedDict()


for i in sorted(channels_orig):
  channels[i] = channels_orig[i]


for c in channels:
  if "Top" in c or "DYtt" in c or "WW" in c or "wh3l_wz" in c or "wh3l_zg" in c or "zh4l_ZZ" in c: continue
  overallSignalRate[c] = OrderedDict()
  overallTotalSignal[c] = 0.
  for s in signals:
    overallSignalRate[c][s] = 0.
    if s not in channels[c].keys(): continue
    overallSignalRate[c][s] +=  channels[c][s]
    overallTotalSignal[c] += channels[c][s]

ncat=0
combChannelsToConsider = []
for k in channels:
  if "Top" in k or "DYtt" in k or "WW" in k or "wh3l_wz" in k or "wh3l_zg" in k or "zh4l_ZZ" in k: continue
  if overallTotalSignal[k] == 0: continue
  ncat+=1
  combChannelsToConsider.append(k)
  print k

matrix = ROOT.TH2F("matrix","matrix",len(combChannelsToConsider),0,len(combChannelsToConsider),len(signals),0,len(signals))

matrix.GetXaxis().SetLabelSize(0.04)
matrix.GetYaxis().SetLabelSize(0.04)
matrix.GetYaxis().SetTitleSize(0.05)
matrix.GetYaxis().SetTitleOffset(1.1)
matrix.SetTitle("")
matrix.SetStats(0)

events = {}
#ROOT.TColor.SetPalette(51)
#cols = ROOT.TColor.GetPalette()
stops = [0.00, 0.5, 1.00]
red   = [1.00, 0, 1.00]
green = [1.00, 0, 0.00]
blue  = [1.00, 1.0, 0.00]
s = np.array(stops)
r = np.array(red)
g = np.array(green)
b = np.array(blue)
ROOT.TColor.CreateGradientColorTable(len(s), s, r, g, b, 99)
ROOT.gStyle.SetNumberContours(99)


for i,c in enumerate(combChannelsToConsider):
#  if overallTotalSignal[c] == 0: continue
  matrix.GetXaxis().SetBinLabel(i+1,c)
  for num,s in enumerate(overallSignalRate[c]):
    matrix.GetYaxis().SetBinLabel(num+1,s)
    ratio = overallSignalRate[c][s]/overallTotalSignal[c]
    #if ratio < 0.005: ratio=0
    matrix.SetBinContent(i+1,num+1,ratio)
    print "category ", c," ", " signal ",s," signal fraction = ",overallSignalRate[c][s]/overallTotalSignal[c], " events = ", overallSignalRate[c][s]

#change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.lumi_13TeV = "41.5 fb^{-1}"
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
ROOT.gStyle.SetPaintTextFormat("4.2f")
ROOT.gStyle.SetHistMinimumZero()

#iPos = 33
iPos = 0

H_ref = 1000
W_ref = 1400
W = W_ref
H  = H_ref

# references for T, B, L, R
T = 0.08*H_ref
B = 0.12*H_ref
L = 0.28*W_ref
R = 0.16*W_ref

canvas = ROOT.TCanvas("c2","c2",50,50,W,H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(0)
canvas.SetTicky(0)
#canvas.SetGrid()


matrix.Draw("colz text")

CMS_lumi.CMS_lumi(canvas, 4, iPos)

ROOT.gPad.RedrawAxis()


a = raw_input()
