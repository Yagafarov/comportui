import math

# Global o'zgaruvchilar
d0 = 30  # O'rnatilgan ma'lumotlar
l1 = 200.0
l2 = 200.0
h0 = 140
f1_min = -45.0 * math.pi/180.0
f1_max =30* math.pi / 180
f2_min = -60 * math.pi / 180
f2_max =70* math.pi / 180
f_between = 140.0 * math.pi / 180.0

# Forward_task funksiyasi
def Forward_task(in_values):
    Ey_ = d0 - l1 * math.sin(in_values[0]) + l2 * math.cos(in_values[1])
    Ex = Ey_ * math.cos(in_values[2])
    Ey = Ey_ * math.sin(in_values[2])
    Ez = h0 + in_values[3] + l1 * math.cos(in_values[0]) + l2 * math.sin(in_values[1])
    return [Ex, Ey, Ez]


def Invers_task(in_vector):

    # Kirish ma'lumotlari
    ALPHA = in_vector[1] / in_vector[0]
    f3 = math.atan(ALPHA)  # atan2 ni o'rniga atan ishlatilsa xato bo'lishi mumkin
    L4_min, L4_max = 0.0, 1000.0

    A1 = math.sqrt(in_vector[0] ** 2 + in_vector[1] ** 2) - d0
    L4= 0.0

    while True:
        A2 = in_vector[2] - (L4 + h0)
        B = (l2 ** 2 - l1 ** 2 - A1 ** 2 - A2 ** 2) / (2 * l1)
        D = B ** 2 * A2 ** 2 - (A1 ** 2 + A2 ** 2) * (B ** 2 - A1 ** 2)

        if D < 0:
            L4 = 0.5 * (L4_min + L4_max)
            while (L4_max - L4_min) > 1.0e-6 or D < 0:
                A2 = in_vector[2] - (L4 + h0)
                B = (l2 ** 2 - l1 ** 2 - A1 ** 2 - A2 ** 2) / (2 * l1)
                D = B ** 2 * A2 ** 2 - (A1 ** 2 + A2 ** 2) * (B ** 2 - A1 ** 2)
                if D > 0:
                    L4_max = L4
                else:
                    L4_min = L4
                L4 = 0.5 * (L4_min + L4_max)

        cx1 = (-B * A2 + math.sqrt(D)) / (A1 ** 2 + A2 ** 2)
        cx2 = (-B * A2 - math.sqrt(D)) / (A1 ** 2 + A2 ** 2)
        D = B ** 2 * A1 ** 2 - (A1 ** 2 + A2 ** 2) * (B ** 2 - A2 ** 2)
        sx1 = (B * A1 + math.sqrt(D)) / (A1 ** 2 + A2 ** 2)
        sx2 = (B * A1 - math.sqrt(D)) / (A1 ** 2 + A2 ** 2)
        
        f11 = math.acos(cx1) if sx1 >= 0 else math.asin(sx1) if cx1 >= 0 else -math.acos(cx1)
        f12 = math.acos(cx2) if sx2 >= 0 else math.asin(sx2) if cx2 >= 0 else -math.acos(cx2)

        C = -(l1 ** 2 - l2 ** 2 - A1 ** 2 - A2 ** 2) / (2 * l2)
        D = C ** 2 * A1 ** 2 - (A1 ** 2 + A2 ** 2) * (C ** 2 - A2 ** 2)
        cx1 = (C * A1 + math.sqrt(D)) / (A1 ** 2 + A2 ** 2)
        cx2 = (C * A1 - math.sqrt(D)) / (A1 ** 2 + A2 ** 2)
        D = C ** 2 * A2 ** 2 - (A1 ** 2 + A2 ** 2) * (C ** 2 - A1 ** 2)
        sx2 = (C * A2 + math.sqrt(D)) / (A1 ** 2 + A2 ** 2)
        sx1 = (C * A2 - math.sqrt(D)) / (A1 ** 2 + A2 ** 2)

        f21 = math.acos(cx1) if sx1 >= 0 else math.asin(sx1) if cx1 >= 0 else -math.acos(cx1)
        f22 = math.acos(cx2) if sx2 >= 0 else math.asin(sx2) if cx2 >= 0 else -math.acos(cx2)

        # Cheklovni tekshirish
        cond11 = f11 < f1_min or f11 > f1_max
        cond12 = f12 < f1_min or f12 > f1_max
        cond1 = cond11 and cond12

        cond21 = f21 < f2_min or f21 > f2_max
        cond22 = f22 < f2_min or f22 > f2_max
        cond2 = cond21 and cond22

        cond31 = (math.pi / 2 + f21 - f11) > f_between
        cond32 = (math.pi / 2 + f22 - f12) > f_between
        cond3 = cond31 and cond32

        if cond1 or cond2 or cond3:
            L4 += 0.01
            continue

        if not (cond11 or cond21 or cond31):
            return [f11, f21, f3, L4]
        else:
            return [f12, f22, f3, L4]


def main():
    obob_coord = [-20.0 / 180.0 * math.pi, 45.0 / 180.0 *math.pi, 0, 0.0]
    coord_E = Forward_task(obob_coord)
    print(f"{d0}  {h0}")
    print(f"{d0}  {h0 + obob_coord[3]}")
    print(f"{d0 - l1 * math.sin(obob_coord[0])}  {h0 + obob_coord[3] + l1 * math.cos(obob_coord[0])}")
    print(f"{d0 - l1 * math.sin(obob_coord[0]) + l2 * math.cos(obob_coord[1]) }  {h0 + obob_coord[3] + l1 * math.cos(obob_coord[0]) + l2 * math.sin(obob_coord[1])}")


    U0 = 25
    N=10
    r0 = [ 0.1, 300.0, 200.0 ]
    rN = [ 50, 250.0, 600.0 ]
    trajectory = []
    trajectory.append(r0)
    for i in range(1,N):
        trajectory.append([ r0[0] + i * (rN[0] - r0[0]) / N, r0[1] + i * (rN[1] - r0[1]) / N, r0[2] + i * (rN[2] - r0[2]) / N ])
    trajectory.append(rN)

    time = 0.0

    trajectory_ref = []
    for  i in range(0,len(trajectory)):
        out = Invers_task(trajectory[i])
        trajectory_ref.append(out)

        if i > 0:
            dl = math.sqrt(math.pow(trajectory[i][0] - trajectory[i - 1][0], 2) + pow(trajectory[i][1] - trajectory[i - 1][1], 2) + math.pow(trajectory[i][2] - trajectory[i - 1][2], 2))
            dt = dl / U0
            time += dt
            speed0 = (trajectory_ref[i][0] - trajectory_ref[i - 1][0]) / dt
            speed1 = (trajectory_ref[i][1] - trajectory_ref[i - 1][1]) / dt
            speed2 = (trajectory_ref[i][2] - trajectory_ref[i - 1][2]) / dt
            speed3 = (trajectory_ref[i][3] - trajectory_ref[i - 1][3]) / dt
            print(f"{time}  {speed0}  {speed1}  {speed2}  {speed3}")


        print(f"{time}  {out[0]}  {out[1]}  {out[2]}  {out[3]}")
        if i % 1 == 0:
            
            print(f"{d0 * math.cos(out[2])}  {d0 * math.sin(out[2])}  {h0}")
            print(f"{d0 * math.cos(out[2])}  {d0 * math.sin(out[2])}  {h0+out[3]}")
            print(f"{d0 - l1 * math.sin(out[0]) * math.cos(out[2])}  {(d0 - l1 * math.sin(out[0])) * math.sin(out[2])}  {h0 + out[3] + l1 * math.cos(out[0])}")
            print(f"{(d0 - l1 * math.sin(out[0]) + l2 * math.cos(out[1])) * math.cos(out[2])}  {(d0 - l1 * math.sin(out[0]) + l2 * math.cos(out[1])) * math.sin(out[2])}  {h0 + out[3] + l1 * math.cos(out[0]) + l2 * math.sin(out[1])}")
            
            



if __name__ == "__main__":
    main()