# cuts

#cuts = {}
  
#supercut = 'abs(mll-91.1876)<15 \
supercut = ' mll>20 \
             && std_vector_lepton_pt[0]>20 && std_vector_lepton_pt[1]>10 \
             && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13) \
             && std_vector_lepton_pt[2]<10 \
            '

cuts['DYee']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
                 && std_vector_lepton_pt[0]>30 && std_vector_lepton_pt[1]>20 \
                 && mll>60 \
               '

cuts['DYmm']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
                 && mll>60 \
               '

cuts['DYee2lepEB']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
                 && mll>60 \
                 && std_vector_lepton_pt[0]>30 && std_vector_lepton_pt[1]>20 \
                 && abs(std_vector_lepton_eta[0])<1.46  \
                 && abs(std_vector_lepton_eta[1])<1.46  \
               '

cuts['DYee2lepEE']  = '(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
                 && mll>60 \
                 && std_vector_lepton_pt[0]>30 && std_vector_lepton_pt[1]>20 \
                 && abs(std_vector_lepton_eta[0])<1.46  \
                 && abs(std_vector_lepton_eta[1])>1.46  \
               '




