print("cloud2: Gotowy do akcji!")
# pobranie danych od użytkownika
dane = {
    "b" : float,
    "ck" : float,
    "co" : float,
    "a_inf" : float, # 1/Rad
    "beta" : float # stopnie
}

it = iter(dane)
x = next(it,"")
while x:
    tekst = "".join(["Podaj: ", x, " = "])
    podane = input(tekst)
    try:
        test = float(podane)
        dane[x] = test
        x = next(it,"")
    except ValueError:
        print("PODANO NIEPRAWIDŁOWĄ DANĄ:", podane,)
        print("SPRÓBUJ PONOWNIE (Podaj liczbę całkowitą lub dziesiętną)")


# przetworzenie danych
b = dane["b"]
ck = dane["ck"]
co = dane["co"]
a_inf = dane["a_inf"]
beta = dane["beta"]

tau=0.1
delta=0.1
l=ck/co
AR = 2*b/(ck+co)
t=AR/a_inf
tau1=0.023*t*t*t-0.03*t*t+0.25*t
tau2=0.18*l*l*l*l*l+1.52*l*l*l*l-3.51*l*l*l+3.5*l*l-1.33*l+0.17
delta1=0.0537*t-0.005
delta2=-0.43*l*l*l*l*l+1.83*l*l*l*l-3.06*l*l*l+2.56*l*l-l+0.148
delta3=(-2.2/10000000*AR*AR*AR+AR*AR/10000000+1.6/100000)*beta*beta*beta+1
tau=tau1*tau2/0.17
delta=delta1*delta2*delta3/0.048

print("wynik:")
print("tau = ", tau)
print("delta = ", delta)