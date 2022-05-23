from math import radians,cos,sin,tan

num=float(input("insira um ângulo em graus e te direi o seu sen, cos e tan: "))

print("Seno: {:.1f}\nCos: {:.1f}\nTan: {:.1f}".format(sin(radians(num)),cos(radians(num)),tan(radians(num))))