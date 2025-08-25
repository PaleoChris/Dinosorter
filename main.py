import config
import os
import sys

def get_config_path(filename):
    # Access the temporary directory when bundled, otherwise, use current directory
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, filename)

config_path = get_config_path("config.py")

A,jubutuscmp = 0.0
C,caracalcmp = 0.0
C,temminckiicmp = 0.0
F,chauscmp = 0.0
F,margaritacmp = 0.0
F,nigripescmp = 0.0
F,silvestriscmp = 0.0
H,yagouaroundicmp = 0.0
L,pardaliscmp = 0.0
L,tigrinuscmp = 0.0
L,wiediicmp = 0.0
L,servalcmp = 0.0
L,canadensiscmp = 0.0
L,lynxcmp = 0.0
L,pardinuscmp = 0.0
L,rufuscmp = 0.0
N,nebulosacmp = 0.0
O,colocolocmp = 0.0
O,geoffroyicmp = 0.0
O,manulcmp = 0.0
P,leocmp = 0.0
P,oncacmp = 0.0
P,parduscmp = 0.0
P,tigriscmp = 0.0
P,unciacmp = 0.0
P,marmoratacmp = 0.0
P,bengalensis = 0.0
P,planiceps = 0.0
P,viverrinus = 0.0
P,aurata = 0.0
P,concolor = 0.0

def pawcmp(input):
    global A,jubutuscmp
    global C,caracalcmp
    global C,temminckiicmp
    global F,chauscmp
    global F,margaritacmp
    global F,nigripescmp
    global F,silvestriscmp
    global H,yagouaroundicmp
    global L,pardaliscmp
    global L,tigrinuscmp
    global L,wiediicmp
    global L,servalcmp
    global L,lynxcmp
    global L,pardinuscmp
    global L,rufuscmp
    global N,nebulosacmp
    global O,colocolocmp
    global O,geoffroyicmp
    global O,manulcmp
    global P,leocmp
    global P,parduscmp
    global P,tigriscmp
    global P,unciacmp
    global P,marmoratacmp
    global P,bengalensiscmp
    global P,planicepscmp
    global P,viverrinuscmp
    global P,auratacmp
    global P,concolorcmp
    A,jubutuscmp += abs(config.Ajubutuspaw - input)
    C,caracalcmp += abs(config.Ccaracalpaw - input)
    C,temminckiicmp += abs(config.Ctemminckiipaw - input)
    F,chauscmp += abs(config.Fchauspaw - input)
    F,margaritacmp += abs(config.Fmargaritapaw - input)
    F,nigripescmp += abs(config.Fnigripespaw - input)
    F,silvestriscmp += abs(config.Fsilvestrisspaw - input)
    H,yagouaroundicmp += abs(config.Hyagouaroundipaw - input)
    L,pardaliscmp += abs(config.Lpardalispaw - input)
    L,tigrinuscmp += abs(config.Ltigrinuspaw - input)
    L,wiediicmp += abs(config.Lwiediipaw - input)
    L,servalcmp += abs(config.Lservalpaw - input)
    L,canadensiscmp += abs(config.Lcanadensispaw - input)
    L,lynxcmp += abs(config.Llynxpaw - input)
    L,pardinuscmp += abs(config.Lpardinuspaw - input)
    L,rufuscmp += abs(config.Lrufuspaw - input)
    N,nebulosacmp += abs(config.Nnebulosapaw - input)
    O,colocolocmp += abs(config.Ocolocolopaw - input)
    O,geoffroyicmp += abs(config.Ogeoffroyipaw - input)
    O,manulcmp += abs(config.Omanulpaw - input)
    P,leocmp += abs(config.Pleopaw - input)
    P,oncacmp += abs(config.Poncapaw - input)
    P,parduscmp += abs(config.Pparduspaw - input)
    P,tigriscmp += abs(config.Ptigrispaw - input)
    P,unciacmp += abs(config.Punciapaw - input) 
    P,marmoratacmp += abs(config.Pmarmoratapaw - input)
    P,bengalensiscmp += abs(config.Pbengalensispaw - input)
    P,planicepscmp += abs(config.Pplanicepspaw - input)
    P,viverrinuscmp += abs(config.Pviverrinuspaw - input)
    P,auratacmp += abs(config.Pauratapaw - input)
    P,concolorcmp += abs(config.Pconcolorpaw - input)
def bicmp(input):
    global A,jubutuscmp
    global C,caracalcmp
    global C,temminckiicmp
    global F,chauscmp
    global F,margaritacmp
    global F,nigripescmp
    global F,silvestriscmp
    global H,yagouaroundicmp
    global L,pardaliscmp
    global L,tigrinuscmp
    global L,wiediicmp
    global L,servalcmp
    global L,lynxcmp
    global L,pardinuscmp
    global L,rufuscmp
    global N,nebulosacmp
    global O,colocolocmp
    global O,geoffroyicmp
    global O,manulcmp
    global P,leocmp
    global P,parduscmp
    global P,tigriscmp
    global P,unciacmp
    global P,marmoratacmp
    global P,bengalensiscmp
    global P,planicepscmp
    global P,viverrinuscmp
    global P,auratacmp
    global P,concolorcmp
    A,jubutuscmp += abs(config.Ajubutusbi - input)
    C,caracalcmp += abs(config.Ccaracalbi - input)
    C,temminckiicmp += abs(config.Ctemminckiibi - input)
    F,chauscmp += abs(config.Fchausbi - input)
    F,margaritacmp += abs(config.Fmargaritabi - input)
    F,nigripescmp += abs(config.Fnigripesbi - input)
    F,silvestriscmp += abs(config.Fsilvestrisbi - input)
    H,yagouaroundicmp += abs(config.Hyagouaroundibi - input)
    L,pardaliscmp += abs(config.Lpardalisbi - input)
    L,tigrinuscmp += abs(config.Ltigrinusbi - input)
    L,wiediicmp += abs(config.Lwiediibi - input)
    L,servalcmp += abs(config.Lservalbi - input)
    L,canadensiscmp += abs(config.Lcanadensisbi - input)
    L,lynxcmp += abs(config.Llynxbi - input)
    L,pardinuscmp += abs(config.Lpardinusbi - input)
    L,rufuscmp += abs(config.Lrufusbi - input)
    N,nebulosacmp += abs(config.Nnebulosabi - input)
    O,colocolocmp += abs(config.Ocolocolobi - input)
    O,geoffroyicmp += abs(config.Ogeoffroyibi - input)
    O,manulcmp += abs(config.Omanulbi - input)
    P,leocmp += abs(config.Pleobi - input)
    P,oncacmp += abs(config.Poncabi - input)
    P,parduscmp += abs(config.Ppardusbi - input)
    P,tigriscmp += abs(config.Ptigrisbi - input)
    P,unciacmp += abs(config.Punciabi - input) 
    P,marmoratacmp += abs(config.Pmarmoratabi - input)
    P,bengalensiscmp += abs(config.Pbengalensisbi - input)
    P,planicepscmp += abs(config.Pplanicepsbi - input)
    P,viverrinuscmp += abs(config.Pviverrinusbi - input)
    P,auratacmp += abs(config.Pauratabi - input)
    P,concolorcmp += abs(config.Pconcolorbi - input)

def heicmp(input):
    global A,jubutuscmp
    global C,caracalcmp
    global C,temminckiicmp
    global F,chauscmp
    global F,margaritacmp
    global F,nigripescmp
    global F,silvestriscmp
    global H,yagouaroundicmp
    global L,pardaliscmp
    global L,tigrinuscmp
    global L,wiediicmp
    global L,servalcmp
    global L,lynxcmp
    global L,pardinuscmp
    global L,rufuscmp
    global N,nebulosacmp
    global O,colocolocmp
    global O,geoffroyicmp
    global O,manulcmp
    global P,leocmp
    global P,parduscmp
    global P,tigriscmp
    global P,unciacmp
    global P,marmoratacmp
    global P,bengalensiscmp
    global P,planicepscmp
    global P,viverrinuscmp
    global P,auratacmp
    global P,concolorcmp
    A,jubutuscmp += abs(config.Ajubutushei - input)
    C,caracalcmp += abs(config.Ccaracalhei - input)
    C,temminckiicmp += abs(config.Ctemminckiihei - input)
    F,chauscmp += abs(config.Fchaushei - input)
    F,margaritacmp += abs(config.Fmargaritahei - input)
    F,nigripescmp += abs(config.Fnigripeshei - input)
    F,silvestriscmp += abs(config.Fsilvestrishei - input)
    H,yagouaroundicmp += abs(config.Hyagouaroundihei - input)
    L,pardaliscmp += abs(config.Lpardalishei - input)
    L,tigrinuscmp += abs(config.Ltigrinushei - input)
    L,wiediicmp += abs(config.Lwiediihei - input)
    L,servalcmp += abs(config.Lservalhei - input)
    L,canadensiscmp += abs(config.Lcanadensishei - input)
    L,lynxcmp += abs(config.Llynxhei - input)
    L,pardinuscmp += abs(config.Lpardinushei - input)
    L,rufuscmp += abs(config.Lrufushei - input)
    N,nebulosacmp += abs(config.Nnebulosahei - input)
    O,colocolocmp += abs(config.Ocolocolohei - input)
    O,geoffroyicmp += abs(config.Ogeoffroyihei - input)
    O,manulcmp += abs(config.Omanulhei - input)
    P,leocmp += abs(config.Pleohei - input)
    P,oncacmp += abs(config.Poncahei - input)
    P,parduscmp += abs(config.Ppardushei - input)
    P,tigriscmp += abs(config.Ptigrishei - input)
    P,unciacmp += abs(config.Punciahei - input) 
    P,marmoratacmp += abs(config.Pmarmoratahei- input)
    P,bengalensiscmp += abs(config.Pbengalensishei - input)
    P,planicepscmp += abs(config.Pplanicepshei - input)
    P,viverrinuscmp += abs(config.Pviverrinushei - input)
    P,auratacmp += abs(config.Pauratahei - input)
    P,concolorcmp += abs(config.Pconcolorhei - input)
  
def oicmp(input):
    global A,jubutuscmp
    global C,caracalcmp
    global C,temminckiicmp
    global F,chauscmp
    global F,margaritacmp
    global F,nigripescmp
    global F,silvestriscmp
    global H,yagouaroundicmp
    global L,pardaliscmp
    global L,tigrinuscmp
    global L,wiediicmp
    global L,servalcmp
    global L,lynxcmp
    global L,pardinuscmp
    global L,rufuscmp
    global N,nebulosacmp
    global O,colocolocmp
    global O,geoffroyicmp
    global O,manulcmp
    global P,leocmp
    global P,parduscmp
    global P,tigriscmp
    global P,unciacmp
    global P,marmoratacmp
    global P,bengalensiscmp
    global P,planicepscmp
    global P,viverrinuscmp
    global P,auratacmp
    global P,concolorcmp
    A,jubutuscmp += abs(config.Ajubutusoi - input)
    C,caracalcmp += abs(config.Ccaracaloi - input)
    C,temminckiicmp += abs(config.Ctemminckiioi - input)
    F,chauscmp += abs(config.Fchausoi - input)
    F,margaritacmp += abs(config.Fmargaritaoi - input)
    F,nigripescmp += abs(config.Fnigripesoi - input)
    F,silvestriscmp += abs(config.Fsilvestrisoi - input)
    H,yagouaroundicmp += abs(config.Hyagouaroundioi - input)
    L,pardaliscmp += abs(config.Lpardalisoi - input)
    L,tigrinuscmp += abs(config.Ltigrinusoi - input)
    L,wiediicmp += abs(config.Lwiediioi - input)
    L,servalcmp += abs(config.Lservaloi - input)
    L,canadensiscmp += abs(config.Lcanadensisoi - input)
    L,lynxcmp += abs(config.Llynxoi - input)
    L,pardinuscmp += abs(config.Lpardinusoi - input)
    L,rufuscmp += abs(config.Lrufusoi - input)
    N,nebulosacmp += abs(config.Nnebulosaoi - input)
    O,colocolocmp += abs(config.Ocolocolooi - input)
    O,geoffroyicmp += abs(config.Ogeoffroyioi - input)
    O,manulcmp += abs(config.Omanuloi - input)
    P,leocmp += abs(config.Pleooi - input)
    P,oncacmp += abs(config.Poncaoi - input)
    P,parduscmp += abs(config.Ppardusoi - input)
    P,tigriscmp += abs(config.Ptigrisoi - input)
    P,unciacmp += abs(config.Punciaoi - input) 
    P,marmoratacmp += abs(config.Pmarmorataoi- input)
    P,bengalensiscmp += abs(config.Pbengalensisoi - input)
    P,planicepscmp += abs(config.Pplanicepsoi - input)
    P,viverrinuscmp += abs(config.Pviverrinusoi - input)
    P,auratacmp += abs(config.Paurataoi - input)
    P,concolorcmp += abs(config.Pconcoloroi - input)

def rricmp(input):
    global A,jubutuscmp
    global C,caracalcmp
    global C,temminckiicmp
    global F,chauscmp
    global F,margaritacmp
    global F,nigripescmp
    global F,silvestriscmp
    global H,yagouaroundicmp
    global L,pardaliscmp
    global L,tigrinuscmp
    global L,wiediicmp
    global L,servalcmp
    global L,lynxcmp
    global L,pardinuscmp
    global L,rufuscmp
    global N,nebulosacmp
    global O,colocolocmp
    global O,geoffroyicmp
    global O,manulcmp
    global P,leocmp
    global P,parduscmp
    global P,tigriscmp
    global P,unciacmp
    global P,marmoratacmp
    global P,bengalensiscmp
    global P,planicepscmp
    global P,viverrinuscmp
    global P,auratacmp
    global P,concolorcmp
    A,jubutuscmp += abs(config.Ajubutusrri - input)
    C,caracalcmp += abs(config.Ccaracalrri - input)
    C,temminckiicmp += abs(config.Ctemminckiirri - input)
    F,chauscmp += abs(config.Fchausrri - input)
    F,margaritacmp += abs(config.Fmargaritarri - input)
    F,nigripescmp += abs(config.Fnigripesrri - input)
    F,silvestriscmp += abs(config.Fsilvestrisrri - input)
    H,yagouaroundicmp += abs(config.Hyagouaroundirri - input)
    L,pardaliscmp += abs(config.Lpardalisrri - input)
    L,tigrinuscmp += abs(config.Ltigrinusrri - input)
    L,wiediicmp += abs(config.Lwiediirri - input)
    L,servalcmp += abs(config.Lservalrri - input)
    L,canadensiscmp += abs(config.Lcanadensisrri - input)
    L,lynxcmp += abs(config.Llynxrri - input)
    L,pardinuscmp += abs(config.Lpardinusrri - input)
    L,rufuscmp += abs(config.Lrufusrri - input)
    N,nebulosacmp += abs(config.Nnebulosarri - input)
    O,colocolocmp += abs(config.Ocolocolorri - input)
    O,geoffroyicmp += abs(config.Ogeoffroyirri - input)
    O,manulcmp += abs(config.Omanulrri - input)
    P,leocmp += abs(config.Pleorri - input)
    P,oncacmp += abs(config.Poncarri - input)
    P,parduscmp += abs(config.Ppardusrri - input)
    P,tigriscmp += abs(config.Ptigrisrri - input)
    P,unciacmp += abs(config.Punciarri - input) 
    P,marmoratacmp += abs(config.Pmarmoratarri- input)
    P,bengalensiscmp += abs(config.Pbengalensisrri - input)
    P,planicepscmp += abs(config.Pplanicepsrri - input)
    P,viverrinuscmp += abs(config.Pviverrinusrri - input)
    P,auratacmp += abs(config.Pauratarri - input)
    P,concolorcmp += abs(config.Pconcolorrri - input)

def mc3ricmp(input):
    global A,jubutuscmp
    global C,caracalcmp
    global C,temminckiicmp
    global F,chauscmp
    global F,margaritacmp
    global F,nigripescmp
    global F,silvestriscmp
    global H,yagouaroundicmp
    global L,pardaliscmp
    global L,tigrinuscmp
    global L,wiediicmp
    global L,servalcmp
    global L,lynxcmp
    global L,pardinuscmp
    global L,rufuscmp
    global N,nebulosacmp
    global O,colocolocmp
    global O,geoffroyicmp
    global O,manulcmp
    global P,leocmp
    global P,parduscmp
    global P,tigriscmp
    global P,unciacmp
    global P,marmoratacmp
    global P,bengalensiscmp
    global P,planicepscmp
    global P,viverrinuscmp
    global P,auratacmp
    global P,concolorcmp
    A,jubutuscmp += abs(config.Ajubutusmc3ri - input)
    C,caracalcmp += abs(config.Ccaracalmc3ri - input)
    C,temminckiicmp += abs(config.Ctemminckiimc3ri - input)
    F,chauscmp += abs(config.Fchausmc3ri - input)
    F,margaritacmp += abs(config.Fmargaritamc3ri - input)
    F,nigripescmp += abs(config.Fnigripesmc3ri - input)
    F,silvestriscmp += abs(config.Fsilvestrismc3ri - input)
    H,yagouaroundicmp += abs(config.Hyagouaroundimc3ri - input)
    L,pardaliscmp += abs(config.Lpardalismc3ri - input)
    L,tigrinuscmp += abs(config.Ltigrinusmc3ri - input)
    L,wiediicmp += abs(config.Lwiediimc3ri - input)
    L,servalcmp += abs(config.Lservalmc3ri - input)
    L,canadensiscmp += abs(config.Lcanadensismc3ri - input)
    L,lynxcmp += abs(config.Llynxmc3ri - input)
    L,pardinuscmp += abs(config.Lpardinusmc3ri - input)
    L,rufuscmp += abs(config.Lrufusmc3ri - input)
    N,nebulosacmp += abs(config.Nnebulosamc3ri - input)
    O,colocolocmp += abs(config.Ocolocolomc3ri - input)
    O,geoffroyicmp += abs(config.Ogeoffroyimc3ri - input)
    O,manulcmp += abs(config.Omanulmc3ri - input)
    P,leocmp += abs(config.Pleomc3ri - input)
    P,oncacmp += abs(config.Poncamc3ri - input)
    P,parduscmp += abs(config.Ppardusmc3ri - input)
    P,tigriscmp += abs(config.Ptigrismc3ri - input)
    P,unciacmp += abs(config.Puncimc3ri - input) 
    P,marmoratacmp += abs(config.Pmarmoratamc3ri- input)
    P,bengalensiscmp += abs(config.Pbengalensismc3ri - input)
    P,planicepscmp += abs(config.Pplanicepsmc3ri - input)
    P,viverrinuscmp += abs(config.Pviverrinusmc3ri - input)
    P,auratacmp += abs(config.Pauratamc3ri - input)
    P,concolorcmp += abs(config.Pconcolormc3ri - input)

def haacmp(input):
    global A,jubutuscmp
    global C,caracalcmp
    global C,temminckiicmp
    global F,chauscmp
    global F,margaritacmp
    global F,nigripescmp
    global F,silvestriscmp
    global H,yagouaroundicmp
    global L,pardaliscmp
    global L,tigrinuscmp
    global L,wiediicmp
    global L,servalcmp
    global L,lynxcmp
    global L,pardinuscmp
    global L,rufuscmp
    global N,nebulosacmp
    global O,colocolocmp
    global O,geoffroyicmp
    global O,manulcmp
    global P,leocmp
    global P,parduscmp
    global P,tigriscmp
    global P,unciacmp
    global P,marmoratacmp
    global P,bengalensiscmp
    global P,planicepscmp
    global P,viverrinuscmp
    global P,auratacmp
    global P,concolorcmp
    A,jubutuscmp += abs(config.Ajubutushaa - input)
    C,caracalcmp += abs(config.Ccaracalhaa - input)
    C,temminckiicmp += abs(config.Ctemminckiihaa - input)
    F,chauscmp += abs(config.Fchaushaa - input)
    F,margaritacmp += abs(config.Fmargaritahaa - input)
    F,nigripescmp += abs(config.Fnigripeshaa - input)
    F,silvestriscmp += abs(config.Fsilvestrishaa - input)
    H,yagouaroundicmp += abs(config.Hyagouaroundihaa - input)
    L,pardaliscmp += abs(config.Lpardalishaa - input)
    L,tigrinuscmp += abs(config.Ltigrinushaa - input)
    L,wiediicmp += abs(config.Lwiediihaa - input)
    L,servalcmp += abs(config.Lservalhaa - input)
    L,canadensiscmp += abs(config.Lcanadensishaa - input)
    L,lynxcmp += abs(config.Llynxhaa - input)
    L,pardinuscmp += abs(config.Lpardinushaa - input)
    L,rufuscmp += abs(config.Lrufushaa - input)
    N,nebulosacmp += abs(config.Nnebulosahaa - input)
    O,colocolocmp += abs(config.Ocolocolohaa - input)
    O,geoffroyicmp += abs(config.Ogeoffroyihaa - input)
    O,manulcmp += abs(config.Omanulhaa - input)
    P,leocmp += abs(config.Pleohaa - input)
    P,oncacmp += abs(config.Poncahaa - input)
    P,parduscmp += abs(config.Ppardushaa - input)
    P,tigriscmp += abs(config.Ptigrishaa - input)
    P,unciacmp += abs(config.Puncihaa - input) 
    P,marmoratacmp += abs(config.Pmarmoratahaa- input)
    P,bengalensiscmp += abs(config.Pbengalensishaa - input)
    P,planicepscmp += abs(config.Pplanicepshaa - input)
    P,viverrinuscmp += abs(config.Pviverrinushaa - input)
    P,auratacmp += abs(config.Pauratahaa - input)
    P,concolorcmp += abs(config.Pconcolorhaa - input)

def sort():
    global A,jubutuscmp
    global C,caracalcmp
    global C,temminckiicmp
    global F,chauscmp
    global F,margaritacmp
    global F,nigripescmp
    global F,silvestriscmp
    global H,yagouaroundicmp
    global L,pardaliscmp
    global L,tigrinuscmp
    global L,wiediicmp
    global L,servalcmp
    global L,lynxcmp
    global L,pardinuscmp
    global L,rufuscmp
    global N,nebulosacmp
    global O,colocolocmp
    global O,geoffroyicmp
    global O,manulcmp
    global P,leocmp
    global P,parduscmp
    global P,tigriscmp
    global P,unciacmp
    global P,marmoratacmp
    global P,bengalensiscmp
    global P,planicepscmp
    global P,viverrinuscmp
    global P,auratacmp
    global P,concolorcmp
    float_dict = {'A,jubutus': A,jubutuscmp, 'C,caracal': C,caracalcmp, 'C,temminckii': C,temminckiicmp, 'F,chaus': F,chauscmp, 'F,margaritac' : F,margaritacmp, 'F,nigripes' : F,nigripescmp, 'F,silvestris' : F,silvestriscmp, 'H,yagouaroundi' : H,yagouaroundicmp, 'L,pardalis' : L,pardaliscmp, 'L,tigrinus' : L,tigrinuscmp, 'L,wiedii' : L,wiediicmp, 'L,serval' : L,servalcmp, 'L,lynx' : L,lynxcmp, 'L,pardinus' : L,pardinuscmp, 'L,rufus' : L,rufuscmp, 'N,nebulosa' : N,nebulosacmp, 'O,colocolo' : O,colocolocmp, 'O,geoffroyi' : O,geoffroyicmp, 'O,manul' : O,manulcmp, 'P,leo' : P,leocmp, 'P,pardus' : P,parduscmp, 'P,tigris' : P,tigriscmp, 'P,uncia' : P,unciacmp, 'P,marmorata' : P,marmoratacmp, 'P,planiceps' : P,planicepscmp, 'P,viverrinus' : P,viverrinuscmp, 'P,aurata' : P,auratacmp, 'P,concolor' : P,concolorcmp }
    sorted_floats = sorted(float_dict.items(), key=lambda item: item[1])
    print(sorted_floats)
    print("the Felid most similar to the data entered is " + str(sorted_floats[0]))
    print("second most similar: " + str(sorted_floats[1]))
    print("third most similar: " + str(sorted_floats[2]))
    print("least similar: " + str(sorted_floats[21]))


def main():
    global A,jubutuscmp
    global C,caracalcmp
    global C,temminckiicmp
    global F,chauscmp
    global F,margaritacmp
    global F,nigripescmp
    global F,silvestriscmp
    global H,yagouaroundicmp
    global L,pardaliscmp
    global L,tigrinuscmp
    global L,wiediicmp
    global L,servalcmp
    global L,lynxcmp
    global L,pardinuscmp
    global L,rufuscmp
    global N,nebulosacmp
    global O,colocolocmp
    global O,geoffroyicmp
    global O,manulcmp
    global P,leocmp
    global P,parduscmp
    global P,tigriscmp
    global P,unciacmp
    global P,marmoratacmp
    global P,bengalensiscmp
    global P,planicepscmp
    global P,viverrinuscmp
    global P,auratacmp
    global P,concolorcmp
    print("Hi! Welcome to the Dinosorter. Enter the requested measurement data to compare your specimen to our list of Felids.")
    PAW = float(input("Enter PAW: "))
    BI = float(input("Enter BI: "))
    HEI = float(input("Enter HEI: "))
    OI = float(input("Enter OI: "))
    RRI = float(input("Enter RRI: "))
    MC3RI = float(input("Enter MC3RI: "))
    HAA = float(input("Enter HAA: "))
    print("calculating PAW...")
    pawcmp(PAW)
    print("calculating BI...")
    bicmp(BI)
    print("calculating HEI...")
    heicmp(HEI)
    print("calculating OI...")
    oicmp(OI)
    print("calculating RRI...")
    rricmp(RRI)
    print("calculating MC3RI...")
    mc3ricmp(MC3RI)
    print("calculating HAA...")
    haacmp(HAA)
    print("determining closest measurements...")
    sort()
    woohoo = input("Enter anything to confirm: ")

if __name__ == "__main__":
    main()
