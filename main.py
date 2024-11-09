import config
herrerasauruscmp = 0.0
eoraptorcmp = 0.0
tawacmp = 0.0
syntarsuscmp = 0.0
coelophysiscmp = 0.0
dilophosauruscmp = 0.0
eodromaeuscmp = 0.0
carnotauruscmp = 0.0
africancmp = 0.0
xuanhanosauruscmp = 0.0
allosauruscmp = 0.0
torvosauruscmp = 0.0
acrocanthosauruscmp = 0.0
guanlongcmp = 0.0
albertosauruscmp = 0.0
gorgosauruscmp = 0.0
daspletosauruscmp = 0.0
tarbosauruscmp = 0.0
tyrannosauruscmp = 0.0
yutyrannuscmp = 0.0
haplocheiruscmp = 0.0
gualichocmp = 0.0

def pawcmp(input):
    herrerasauruscmp += abs(config.herrerasauruspaw - input)
    

def main():
    print("Hi! Welcome to the Dinosorter. Enter the requested measurement data to compare your specimen to our list of Theropods.")
    PAW = float(input("Enter PAW: "))
    BI = float(input("Enter BI: "))
    HEI = float(input("Enter HEI: "))
    OI = float(input("Enter OI: "))
    RRI = float(input("Enter RRI: "))
    MC3RI = float(input("Enter MC3RI: "))
    HAA = float(input("Enter HAA: "))
    print("calculating paw...")
    pawcmp(PAW)

if __name__ == "__main__":
    main()