import math
g=9.81
def sin(a):
    radian=math.radians(a)
    x=math.sin(radian)
    return x
def cos(a):
    radian=math.radians(a)
    x=math.cos(radian)
    return x
def total_time_range(a,b):
    t=2*a*sin(b)/g
    r=a*cos(b)*t
    print(f"Time of flight is {t:.4f} seconds.")
    print(f"Range of flight is {r:.4f} meters.")
    return t,r
def table_format(time,range,a,b):
    list=[0,1/5,1/3,1/2,3/4,1]
    print(f"{'Time (s)':<15}{'x (m)':<15}{'y (m)':<15}")
    for i in list:
        t=i*time
        x=range*i
        y=a*sin(b)*t-0.5*g*t**2
        print(f"{t:<15.2f}{x:<15.2f}{y:<15.2f}")
def physics_calculate():
    print("Welcome to the projectile motion calculator!")
    a=int(input("Enter initial speed (m/s):"))
    b=int(input("Enter angle of projection (degree):"))
    print(end="\n")
    time,range=total_time_range(a, b)
    print(end="\n")
    table_format(time,range,a,b)

physics_calculate()